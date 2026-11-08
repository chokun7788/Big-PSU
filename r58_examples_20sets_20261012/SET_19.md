# ชุด 19 — แปะก๊วย / Ginkgo

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

เกม สถานที่ ราคา กฎ บุคคล และสถานะทั้งหมดในชุดใหม่นี้แต่งขึ้นเพื่อทดสอบ ไม่ได้เป็นข้อมูล PSU หรือเกมที่มีจำหน่ายจริง คำแปลยังไม่ผ่านมนุษย์

แพลตฟอร์มตัวอย่าง: Nintendo Switch • จำนวนผู้เล่น 2–6 • เวลาเล่น 180 นาที / กินช่องจอง 180 นาที

## ข้อมูลครบ 24 หมวด

### ข้อมูลศูนย์ (`center`)

รหัส `demo20_center_19`

คำถามตัวอย่าง:

- ศูนย์ทดลอง แปะก๊วย อยู่ตรงไหน
- Demo venue Ginkgo Where is it located?
- ศูนย์ทดลอง แปะก๊วย อยู่ตึกอะไร ชั้นไหน

**address — known**
```json
{
  "en": "Fictional address 133, Example Road, Test District",
  "th": "เลขที่สมมุติ 133 ถนนตัวอย่าง แขวงทดลอง"
}
```
**building — known**
```json
"DEMO Tower E"
```
**description — known**
```json
{
  "en": "Synthetic scenario 19: Explorer Yard, not a real venue",
  "th": "สถานการณ์ทดลอง 19: ลานนักสำรวจ ไม่ใช่สถานที่จริง"
}
```
**floor — known**
```json
"5"
```
**map_url — known**
```json
"https://example.invalid/demo20/map/19"
```
**name — known**
```json
{
  "en": "Demo venue Ginkgo",
  "th": "ศูนย์ทดลอง แปะก๊วย"
}
```
**operator — known**
```json
{
  "en": "Fictional Ginkgo operator",
  "th": "ผู้ประกอบการสมมุติ แปะก๊วย"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/center/demo20_center_19.json)

### โซนบริการ (`zone`)

รหัส `demo20_zone_19`

คำถามตัวอย่าง:

- โซนทดลอง แปะก๊วย มีที่นั่งกี่ที่
- Demo zone Ginkgo How many seats are there?
- โซนทดลอง แปะก๊วย โซนนี้อยู่ตรงไหนและมีที่นั่งกี่ที่

**description — known**
```json
{
  "en": "Synthetic Nintendo Switch zone for Explorer Yard",
  "th": "โซนจำลอง Nintendo Switch สำหรับลานนักสำรวจ"
}
```
**location — known**
```json
{
  "en": "Test building, floor 5, room 119",
  "th": "อาคารทดสอบ ชั้น 5 ห้อง 119"
}
```
**name — known**
```json
{
  "en": "Demo zone Ginkgo",
  "th": "โซนทดลอง แปะก๊วย"
}
```
**room_seats — known**
```json
9
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_19.json)

### รุ่นและสเปกอุปกรณ์ (`equipment_model`)

รหัส `demo20_equipment_model_19`

คำถามตัวอย่าง:

- รุ่นอุปกรณ์ แปะก๊วย สเปกมีอะไรบ้าง
- Demo model Ginkgo What are its specifications?
- รุ่นอุปกรณ์ แปะก๊วย เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง

**device_type — known**
```json
"console"
```
**name — known**
```json
{
  "en": "Demo model Ginkgo",
  "th": "รุ่นอุปกรณ์ แปะก๊วย"
}
```
**specifications — known**
```json
[
  {
    "key": "DEMO screen",
    "unit": "inch",
    "value": "36"
  },
  {
    "key": "DEMO input",
    "unit": "",
    "value": "gamepad"
  }
]
```
**usage — known**
```json
{
  "en": "Fictional equipment for Nintendo Switch; not a PSU specification",
  "th": "เครื่องสมมุติใช้กับ Nintendo Switch; ห้ามอ้างเป็นสเปกศูนย์"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_19.json)

### เครื่องหรือทรัพยากรจริง (`resource`)

รหัส `demo20_resource_19`

คำถามตัวอย่าง:

- เครื่องทดลอง แปะก๊วย เล่นพร้อมกันได้กี่คน
- Demo station Ginkgo How many people can play at once?
- เครื่องทดลอง แปะก๊วย เครื่องยังใช้งานได้ไหมและรองรับกี่คน

**capacity_persons — known**
```json
6
```
**equipment_model_ids — known**
```json
[
  "demo20_equipment_model_19"
]
```
**name — known**
```json
{
  "en": "Demo station Ginkgo",
  "th": "เครื่องทดลอง แปะก๊วย"
}
```
**operational_status — known**
```json
"in_service"
```
**physical_pool_key — known**
```json
"demo20_pool_19"
```
**zone_id — known**
```json
"demo20_zone_19"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/resource/demo20_resource_19.json)

### รายการที่เลือกในระบบจอง (`service`)

รหัส `demo20_service_19`

คำถามตัวอย่าง:

- รอบทดลอง แปะก๊วย หนึ่งรอบเล่นได้กี่นาที
- Demo session Ginkgo How many minutes does one session last?
- รอบทดลอง แปะก๊วย เวลาเล่นกับเวลาที่กินช่องจองกี่นาที

**booking_product_key — known**
```json
"DEMO20_BOOKING_19"
```
**capacity_max — known**
```json
6
```
**capacity_min — known**
```json
2
```
**name — known**
```json
{
  "en": "Demo session Ginkgo",
  "th": "รอบทดลอง แปะก๊วย"
}
```
**occupancy_minutes — known**
```json
180
```
**platform — known**
```json
"Nintendo Switch"
```
**resource_ids — known**
```json
[
  "demo20_resource_19"
]
```
**session_minutes — known**
```json
180
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_19.json)

### ข้อมูลเกม (`game`)

รหัส `demo20_game_19`

คำถามตัวอย่าง:

- เกมสมมุติ แปะก๊วย เล่นยังไง
- Fictional game Ginkgo How do I play it?
- เกมสมมุติ แปะก๊วย เกมเกี่ยวกับอะไรและเล่นยังไง

**age_rating — known**
```json
{
  "en": "Synthetic DEMO rating 12",
  "th": "เรตอายุสมมุติ DEMO 12"
}
```
**edition — known**
```json
"DEMO fiction revision 19"
```
**genre — known**
```json
{
  "en": "Strategy",
  "th": "กลยุทธ์"
}
```
**how_to_play — known**
```json
{
  "en": "Collect clues as a group and agree on a route; follow the demonstration controls",
  "th": "รวมกลุ่มเก็บเบาะแสและสรุปเส้นทาง; ใช้คำสั่งตามชุดควบคุมทดลอง"
}
```
**publisher_url — known**
```json
"https://example.invalid/demo20/fictional-game/19"
```
**summary — known**
```json
{
  "en": "Fictional test game: Collect clues as a group and agree on a route",
  "th": "เกมแต่งขึ้นเพื่อทดสอบ: รวมกลุ่มเก็บเบาะแสและสรุปเส้นทาง"
}
```
**supported_platforms — known**
```json
[
  "Nintendo Switch"
]
```
**title — known**
```json
{
  "en": "Fictional Explorer Yard",
  "th": "เกมสมมุติ ลานนักสำรวจ"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_19.json)

### กลุ่มผู้ใช้ (`audience`)

รหัส `demo20_audience_19`

คำถามตัวอย่าง:

- กลุ่มผู้ใช้ แปะก๊วย ต้องใช้หลักฐานอะไร
- Demo visitors Ginkgo What proof is required?
- กลุ่มผู้ใช้ แปะก๊วย ใครใช้สิทธิ์กลุ่มนี้ได้และต้องแสดงหลักฐานอะไร

**eligibility — known**
```json
{
  "en": "Fictional group 19: demo sessions only",
  "th": "ผู้ใช้สมมุติกลุ่ม 19: ใช้บริการตามรอบทดลอง"
}
```
**name — known**
```json
{
  "en": "Demo visitors Ginkgo",
  "th": "กลุ่มผู้ใช้ แปะก๊วย"
}
```
**required_proofs — known**
```json
[
  "DEMO pass Ginkgo",
  "DEMO group list 19"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/audience/demo20_audience_19.json)

### ติดต่อ (`contact`)

รหัส `demo20_contact_19`

คำถามตัวอย่าง:

- ช่องทางช่วยเหลือ แปะก๊วย ติดต่อทางไหน
- Demo help channel Ginkgo How can I contact them?
- ช่องทางช่วยเหลือ แปะก๊วย ติดต่อที่ไหนและติดต่อได้ช่วงไหน

**channel — known**
```json
"phone"
```
**office_hours — known**
```json
{
  "en": "Demo hours 11:00–20:00",
  "th": "ช่วงทดลอง 11:00–20:00"
}
```
**purpose — known**
```json
{
  "en": "Fictional support for Check-in proof",
  "th": "สอบถามสมมุติเรื่อง หลักฐานเช็กอิน"
}
```
**value — known**
```json
"DEMO-NON-DIALABLE-19"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_19.json)

### ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`)

รหัส `demo20_procedure_19`

คำถามตัวอย่าง:

- ขั้นตอนทดลอง แปะก๊วย ต้องทำยังไงบ้าง
- Demo procedure Ginkgo What steps should I follow?
- ขั้นตอนทดลอง แปะก๊วย มีขั้นตอนอะไรและต้องใช้เอกสารอะไร

**deadline_minutes — known**
```json
60
```
**outcome — known**
```json
{
  "en": "Demo outcome: Check-in proof checked",
  "th": "ผลทดสอบ: ตรวจสอบ หลักฐานเช็กอิน เสร็จ"
}
```
**preconditions — known**
```json
[
  {
    "field": "demo_session",
    "operator": "eq",
    "value": true
  }
]
```
**required_documents — known**
```json
[
  "DEMO pass Ginkgo",
  "DEMO group list 19"
]
```
**steps — known**
```json
[
  {
    "contact_id": null,
    "instruction": {
      "en": "Select the fictional Ginkgo service",
      "th": "เลือกบริการสมมุติ แปะก๊วย"
    },
    "order": 1
  },
  {
    "contact_id": "demo20_contact_19",
    "instruction": {
      "en": "Check names and conditions before confirming",
      "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
    },
    "order": 2
  }
]
```
**topic — known**
```json
"DEMO Check-in proof"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_19.json)

### นโยบายและกฎศูนย์ (`policy`)

รหัส `demo20_policy_19`

คำถามตัวอย่าง:

- ข้อกำหนดทดลอง แปะก๊วย กฎเป็นยังไง
- Demo policy Ginkgo What are the rules?
- ข้อกำหนดทดลอง แปะก๊วย อนุญาตไหมและมีข้อยกเว้นอะไร

**conditions_all — known**
```json
[
  {
    "field": "demo_session",
    "operator": "eq",
    "value": true
  }
]
```
**consequence — known**
```json
{
  "en": "Pause and ask the fictional operator",
  "th": "ให้หยุดขั้นตอนและสอบถามผู้ดูแลสมมุติ"
}
```
**decision — known**
```json
"required"
```
**details — known**
```json
{
  "en": "Fictional rule for Check-in proof: required; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "กติกาสมมุติเรื่องหลักฐานเช็กอิน: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
}
```
**exceptions — known**
```json
{
  "en": "Synthetic exception: permission from the demo event operator is required",
  "th": "ข้อยกเว้นสมมุติ: ต้องได้รับอนุญาตจากผู้ดูแลกิจกรรมเฉพาะครั้ง"
}
```
**procedure_id — known**
```json
"demo20_procedure_19"
```
**subject — known**
```json
{
  "en": "Demo policy Ginkgo",
  "th": "ข้อกำหนดทดลอง แปะก๊วย"
}
```
**topic — known**
```json
"DEMO Check-in proof"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/policy/demo20_policy_19.json)

### สิ่งอำนวยความสะดวก (`facility`)

รหัส `demo20_facility_19`

คำถามตัวอย่าง:

- พื้นที่พัก แปะก๊วย อยู่ตรงไหนในร้าน
- Demo amenity Ginkgo Where in the venue is it?
- พื้นที่พัก แปะก๊วย อยู่ตรงไหนและคนที่ต้องการความช่วยเหลือเข้าใช้ยังไง

**accessibility — known**
```json
{
  "en": "Synthetic accessibility: step-free route",
  "th": "ข้อมูลสมมุติ: เข้าถึงได้ไม่มีขั้น"
}
```
**location — known**
```json
{
  "en": "Document desk in demo room 119",
  "th": "โต๊ะตรวจเอกสาร อยู่ห้องทดสอบ 119"
}
```
**name — known**
```json
{
  "en": "Demo amenity Ginkgo",
  "th": "พื้นที่พัก แปะก๊วย"
}
```
**usage_conditions — known**
```json
{
  "en": "Demo sessions only; ask the operator first",
  "th": "ใช้ตามรอบทดลอง; ต้องขอผู้ดูแลก่อน"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/facility/demo20_facility_19.json)

### เกมที่ศูนย์มีให้เล่นจริง (`game_service`)

รหัส `demo20_game_service_19`

คำถามตัวอย่าง:

- การติดตั้งทดลอง แปะก๊วย มีให้เล่นหรือยัง
- Demo installation Ginkgo Is this game offered?
- การติดตั้งทดลอง แปะก๊วย มีให้เล่นไหมและติดตั้งรุ่นไหน

**account_policy_id — known**
```json
"demo20_policy_19"
```
**game_id — known**
```json
"demo20_game_19"
```
**game_version — known**
```json
"DEMO BUILD 19"
```
**installed_resource_ids — known**
```json
[
  "demo20_resource_19"
]
```
**offered — known**
```json
true
```
**service_id — known**
```json
"demo20_service_19"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_service/demo20_game_service_19.json)

### รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`)

รหัส `demo20_game_mode_19`

คำถามตัวอย่าง:

- โหมดทดลอง แปะก๊วย เล่นพร้อมกันได้สูงสุดกี่คน
- Demo mode Ginkgo How many people can play together at most?
- โหมดทดลอง แปะก๊วย ต้องมีขั้นต่ำกี่คนและเล่นได้สูงสุดกี่คน

**game_id — known**
```json
"demo20_game_19"
```
**mode_name — known**
```json
{
  "en": "Demo mode Ginkgo",
  "th": "โหมดทดลอง แปะก๊วย"
}
```
**network_requirement — known**
```json
{
  "en": "Synthetic network: online",
  "th": "เครือข่ายจำลอง: ออนไลน์"
}
```
**platform — known**
```json
"Nintendo Switch"
```
**players_max — known**
```json
6
```
**players_min — known**
```json
2
```
**studio_supported — known**
```json
true
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_mode/demo20_game_mode_19.json)

### วิธีเล่นและปุ่ม (`control_set`)

รหัส `demo20_control_set_19`

คำถามตัวอย่าง:

- ชุดควบคุมทดลอง แปะก๊วย ปุ่มอะไรบ้าง
- Demo controls Ginkgo What are the controls?
- ชุดควบคุมทดลอง แปะก๊วย ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร

**bindings — known**
```json
[
  {
    "action": {
      "en": "Confirm",
      "th": "ยืนยัน"
    },
    "buttons": [
      "DEMO_gamepad_1"
    ],
    "context": {
      "en": "Fictional input for Explorer Yard",
      "th": "คำสั่งสมมุติของ ลานนักสำรวจ"
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
      "en": "Fictional input for Explorer Yard",
      "th": "คำสั่งสมมุติของ ลานนักสำรวจ"
    },
    "gesture": "press"
  }
]
```
**game_id — known**
```json
"demo20_game_19"
```
**game_version — known**
```json
"DEMO BUILD 19"
```
**input_device — known**
```json
"gamepad"
```
**limitations — known**
```json
{
  "en": "Controls for a fictional game; testing only",
  "th": "ชุดควบคุมเกมแต่งขึ้น ใช้ทดสอบเท่านั้น"
}
```
**platform — known**
```json
"Nintendo Switch"
```
**preset — known**
```json
"DEMO_LAYOUT_19"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_19.json)

### ราคาต่อบริการ (`rate`)

รหัส `demo20_rate_19`

คำถามตัวอย่าง:

- อัตราทดลอง แปะก๊วย ราคาเท่าไหร่
- Demo tariff Ginkgo How much does it cost?
- อัตราทดลอง แปะก๊วย ราคาเท่าไหร่และได้กี่นาที

**amount_minor — known**
```json
30000
```
**audience_id — known**
```json
"demo20_audience_19"
```
**calculation_rule — known**
```json
"no_extrapolation"
```
**currency — known**
```json
"THB"
```
**duration_minutes — known**
```json
180
```
**persons_max — known**
```json
6
```
**persons_min — known**
```json
2
```
**service_id — known**
```json
"demo20_service_19"
```
**tax_note — known**
```json
{
  "en": "Synthetic price; never collect actual payment",
  "th": "ราคาสมมุติ ไม่ใช้เรียกเก็บเงินจริง"
}
```
**unit — known**
```json
"per_group"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rate/demo20_rate_19.json)

### ราคาเหมาโซน/ห้อง (`rental_package`)

รหัส `demo20_rental_package_19`

คำถามตัวอย่าง:

- แพ็กเกจทดลอง แปะก๊วย เหมาเท่าไหร่
- Demo package Ginkgo How much is the rental?
- แพ็กเกจทดลอง แปะก๊วย ราคาเหมาเท่าไหร่และรวมอุปกรณ์อะไร

**amount_minor — known**
```json
91250
```
**audience_id — known**
```json
"demo20_audience_19"
```
**currency — known**
```json
"THB"
```
**duration_minutes — known**
```json
360
```
**equipment_included — known**
```json
{
  "en": "Fictional Ginkgo station and Nintendo Switch inputs",
  "th": "เครื่องสมมุติ แปะก๊วย พร้อมอุปกรณ์ Nintendo Switch"
}
```
**name — known**
```json
{
  "en": "Demo package Ginkgo",
  "th": "แพ็กเกจทดลอง แปะก๊วย"
}
```
**period_label — known**
```json
"full_day"
```
**room_seats — known**
```json
9
```
**terms — known**
```json
{
  "en": "Synthetic package excludes extensions; 2–6 people per session",
  "th": "แพ็กเกจสมมุติไม่รวมค่าต่อเวลา; รอบละ 2–6 คน"
}
```
**zone_ids — known**
```json
[
  "demo20_zone_19"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rental_package/demo20_rental_package_19.json)

### ตารางบริการ (`schedule`)

รหัส `demo20_schedule_19`

คำถามตัวอย่าง:

- ตารางทดลอง แปะก๊วย จองช่วงไหนได้บ้าง
- Demo timetable Ginkgo What are the booking hours?
- ตารางทดลอง แปะก๊วย เปิดช่วงไหนและพักบำรุงรักษาตอนไหน

**bookable_periods — known**
```json
[
  {
    "end": "12:00",
    "start": "11:00"
  },
  {
    "end": "20:00",
    "start": "13:00"
  }
]
```
**maintenance_periods — known**
```json
[
  {
    "end": "13:00",
    "start": "12:00"
  }
]
```
**open_periods — known**
```json
[
  {
    "end": "20:00",
    "start": "11:00"
  }
]
```
**reason — known**
```json
{
  "en": "Synthetic Ginkgo schedule with maintenance",
  "th": "ตารางสมมุติ แปะก๊วย มีพักบำรุงรักษา"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```
**weekday — known**
```json
5
```
**zone_ids — known**
```json
[
  "demo20_zone_19"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_19.json)

### วันปิด/ข้อยกเว้น (`closure`)

รหัส `demo20_closure_19`

คำถามตัวอย่าง:

- ประกาศวันทดลอง แปะก๊วย วันนั้นปิดไหม
- Demo date notice Ginkgo Is it closed on that date?
- ประกาศวันทดลอง แปะก๊วย วันนั้นเปิดปิดยังไงและเพราะอะไร

**bookable_periods — known**
```json
[
  {
    "end": "18:00",
    "start": "14:00"
  }
]
```
**local_date — known**
```json
"2026-12-19"
```
**open_periods — known**
```json
[
  {
    "end": "18:00",
    "start": "14:00"
  }
]
```
**reason — known**
```json
{
  "en": "Synthetic Ginkgo date notice: modified_hours",
  "th": "ประกาศสมมุติ แปะก๊วย: modified_hours"
}
```
**resolution_policy_id — known**
```json
"demo20_policy_19"
```
**state — known**
```json
"modified_hours"
```
**zone_ids — known**
```json
[
  "demo20_zone_19"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/closure/demo20_closure_19.json)

### รายการแข่งขันและฉบับกติกา (`competition`)

รหัส `demo20_competition_19`

คำถามตัวอย่าง:

- รายการฝึก แปะก๊วย ใช้กติกาฉบับไหน
- Demo event Ginkgo Which rulebook release applies?
- รายการฝึก แปะก๊วย ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่

**competition_dates — known**
```json
[
  "2026-12-19"
]
```
**coverage — known**
```json
"complete"
```
**division — known**
```json
{
  "en": "Practice group 2–6 players",
  "th": "กลุ่มฝึก 2–6 คน"
}
```
**event_name — known**
```json
{
  "en": "Demo event Ginkgo",
  "th": "รายการฝึก แปะก๊วย"
}
```
**game_id — known**
```json
"demo20_game_19"
```
**rulebook_release — known**
```json
"DEMO20_REV_19"
```
**supersedes_id — not_applicable**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_19.json)

### ข้อกติกาการแข่งขัน (`competition_rule`)

รหัส `demo20_competition_rule_19`

คำถามตัวอย่าง:

- ข้อการแข่งขันทดลอง แปะก๊วย ข้อนี้กำหนดอะไร
- Demo rule Ginkgo What does this rule require?
- ข้อการแข่งขันทดลอง แปะก๊วย กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม

**competition_id — known**
```json
"demo20_competition_19"
```
**completeness — known**
```json
"complete"
```
**depends_on_ids — known**
```json
[]
```
**facet — known**
```json
"protest_dispute"
```
**heading — known**
```json
{
  "en": "Demo rule Ginkgo",
  "th": "ข้อการแข่งขันทดลอง แปะก๊วย"
}
```
**section_number — known**
```json
"5.19"
```
**text — known**
```json
{
  "en": "Fictional clause 19: for Check-in proof, follow decision required; exception requires written demo operator approval; not actual rules",
  "th": "ข้อสมมุติ 19: หลักฐานเช็กอิน ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_19.json)

### ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`)

รหัส `demo20_news_19`

คำถามตัวอย่าง:

- ข่าวทดลอง แปะก๊วย ประกาศว่าอะไร
- Demo bulletin Ginkgo What does the announcement say?
- ข่าวทดลอง แปะก๊วย ประกาศอะไรและกิจกรรมเริ่มจบเมื่อไหร่

**audience_ids — known**
```json
[
  "demo20_audience_19"
]
```
**body — known**
```json
{
  "en": "Synthetic bulletin: Explorer Yard activity for 2–6 people; no actual payment",
  "th": "ข่าวสมมุติ: กิจกรรมลานนักสำรวจ สำหรับกลุ่ม 2–6 คน; ไม่มีรับเงินจริง"
}
```
**contact_id — known**
```json
"demo20_contact_19"
```
**event_end — known**
```json
"2026-12-19T12:00:00+07:00"
```
**event_start — known**
```json
"2026-12-19T10:00:00+07:00"
```
**registration_url — known**
```json
"https://example.invalid/demo20/register/19"
```
**title — known**
```json
{
  "en": "Demo bulletin Ginkgo",
  "th": "ข่าวทดลอง แปะก๊วย"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/news/demo20_news_19.json)

### บุคลากร/ทีมที่เปิดเผยได้ (`person`)

รหัส `demo20_person_19`

คำถามตัวอย่าง:

- ผู้ดูแลสมมุติ แปะก๊วย รับผิดชอบอะไร
- Fictional host Ginkgo What is their role?
- ผู้ดูแลสมมุติ แปะก๊วย รับผิดชอบเรื่องอะไรและติดต่อทางไหน

**display_name — known**
```json
{
  "en": "Fictional host Ginkgo",
  "th": "ผู้ดูแลสมมุติ แปะก๊วย"
}
```
**public_contact_id — known**
```json
"demo20_contact_19"
```
**public_scope — known**
```json
{
  "en": "Fictional identity; no actual personal data",
  "th": "บุคคลแต่งขึ้น ไม่มีข้อมูลส่วนตัวจริง"
}
```
**role — known**
```json
{
  "en": "Fictional host for Check-in proof",
  "th": "ผู้ดูแลสมมุติเรื่อง หลักฐานเช็กอิน"
}
```
**team — known**
```json
{
  "en": "Demo Ginkgo team",
  "th": "ทีมทดสอบ แปะก๊วย"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/person/demo20_person_19.json)

### คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`)

รหัส `demo20_faq_19`

คำถามตัวอย่าง:

- คำถามตัวอย่าง แปะก๊วย คำตอบคืออะไร
- Demo enquiry Ginkgo What is the answer?
- คำถามตัวอย่าง แปะก๊วย คำตอบคืออะไรและใช้กับกรณีไหน

**answer — known**
```json
{
  "en": "Example answer: Fictional rule for Check-in proof: required; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องหลักฐานเช็กอิน: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
}
```
**question — known**
```json
{
  "en": "Demo enquiry Ginkgo",
  "th": "คำถามตัวอย่าง แปะก๊วย"
}
```
**related_ids — known**
```json
[
  "demo20_policy_19",
  "demo20_procedure_19"
]
```
**scope_note — known**
```json
{
  "en": "Only applies to fictional Ginkgo scenario",
  "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ แปะก๊วย"
}
```
**topic — known**
```json
"DEMO Check-in proof"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_19.json)

### การเชื่อมสถานะสด (`live_binding`)

รหัส `demo20_live_binding_19`

คำถามตัวอย่าง:

- ตัวเชื่อมทดลอง แปะก๊วย จับคู่สถานะยังไง
- Demo binding Ginkgo How are statuses mapped?
- ตัวเชื่อมทดลอง แปะก๊วย จับคู่สถานะแบบไหนและเก็บข้อมูลนานเท่าไหร่

**external_resource_key — known**
```json
"DEMO20_EXTERNAL_19"
```
**freshness_policy — known**
```json
{
  "en": "Synthetic TTL 110 seconds; no API call or live status claim",
  "th": "ค่าจำลอง TTL 110 วินาที; ไม่เรียก API และไม่ยืนยันสถานะสด"
}
```
**physical_pool_key — known**
```json
"demo20_pool_19"
```
**provider — known**
```json
"wordpress_booking"
```
**service_id — known**
```json
"demo20_service_19"
```
**status_mapping — known**
```json
[
  {
    "normalized": "free",
    "raw": "DEMO_EMPTY_19"
  },
  {
    "normalized": "occupied",
    "raw": "DEMO_BUSY_19"
  },
  {
    "normalized": "unknown",
    "raw": "DEMO_UNKNOWN_19"
  }
]
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/live_binding/demo20_live_binding_19.json)

