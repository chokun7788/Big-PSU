# ชุด 17 — มะลิ / Jasmine

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

เกม สถานที่ ราคา กฎ บุคคล และสถานะทั้งหมดในชุดใหม่นี้แต่งขึ้นเพื่อทดสอบ ไม่ได้เป็นข้อมูล PSU หรือเกมที่มีจำหน่ายจริง คำแปลยังไม่ผ่านมนุษย์

แพลตฟอร์มตัวอย่าง: PS5 • จำนวนผู้เล่น 1–4 • เวลาเล่น 120 นาที / กินช่องจอง 120 นาที

## ข้อมูลครบ 24 หมวด

### ข้อมูลศูนย์ (`center`)

รหัส `demo20_center_17`

คำถามตัวอย่าง:

- ศูนย์ทดลอง มะลิ อยู่ตรงไหน
- Demo venue Jasmine Where is it located?
- ศูนย์ทดลอง มะลิ อยู่ตึกอะไร ชั้นไหน

**address — known**
```json
{
  "en": "Fictional address 119, Example Road, Test District",
  "th": "เลขที่สมมุติ 119 ถนนตัวอย่าง แขวงทดลอง"
}
```
**building — known**
```json
"DEMO Tower C"
```
**description — known**
```json
{
  "en": "Synthetic scenario 17: Paper Town, not a real venue",
  "th": "สถานการณ์ทดลอง 17: เมืองกระดาษ ไม่ใช่สถานที่จริง"
}
```
**floor — known**
```json
"3"
```
**map_url — known**
```json
"https://example.invalid/demo20/map/17"
```
**name — known**
```json
{
  "en": "Demo venue Jasmine",
  "th": "ศูนย์ทดลอง มะลิ"
}
```
**operator — known**
```json
{
  "en": "Fictional Jasmine operator",
  "th": "ผู้ประกอบการสมมุติ มะลิ"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/center/demo20_center_17.json)

### โซนบริการ (`zone`)

รหัส `demo20_zone_17`

คำถามตัวอย่าง:

- โซนทดลอง มะลิ มีที่นั่งกี่ที่
- Demo zone Jasmine How many seats are there?
- โซนทดลอง มะลิ โซนนี้อยู่ตรงไหนและมีที่นั่งกี่ที่

**description — known**
```json
{
  "en": "Synthetic PS5 zone for Paper Town",
  "th": "โซนจำลอง PS5 สำหรับเมืองกระดาษ"
}
```
**location — known**
```json
{
  "en": "Test building, floor 3, room 117",
  "th": "อาคารทดสอบ ชั้น 3 ห้อง 117"
}
```
**name — known**
```json
{
  "en": "Demo zone Jasmine",
  "th": "โซนทดลอง มะลิ"
}
```
**room_seats — known**
```json
8
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_17.json)

### รุ่นและสเปกอุปกรณ์ (`equipment_model`)

รหัส `demo20_equipment_model_17`

คำถามตัวอย่าง:

- รุ่นอุปกรณ์ มะลิ สเปกมีอะไรบ้าง
- Demo model Jasmine What are its specifications?
- รุ่นอุปกรณ์ มะลิ เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง

**device_type — known**
```json
"console"
```
**name — known**
```json
{
  "en": "Demo model Jasmine",
  "th": "รุ่นอุปกรณ์ มะลิ"
}
```
**specifications — known**
```json
[
  {
    "key": "DEMO screen",
    "unit": "inch",
    "value": "30"
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
  "en": "Fictional equipment for PS5; not a PSU specification",
  "th": "เครื่องสมมุติใช้กับ PS5; ห้ามอ้างเป็นสเปกศูนย์"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_17.json)

### เครื่องหรือทรัพยากรจริง (`resource`)

รหัส `demo20_resource_17`

คำถามตัวอย่าง:

- เครื่องทดลอง มะลิ เล่นพร้อมกันได้กี่คน
- Demo station Jasmine How many people can play at once?
- เครื่องทดลอง มะลิ เครื่องยังใช้งานได้ไหมและรองรับกี่คน

**capacity_persons — known**
```json
4
```
**equipment_model_ids — known**
```json
[
  "demo20_equipment_model_17"
]
```
**name — known**
```json
{
  "en": "Demo station Jasmine",
  "th": "เครื่องทดลอง มะลิ"
}
```
**operational_status — known**
```json
"in_service"
```
**physical_pool_key — known**
```json
"demo20_pool_17"
```
**zone_id — known**
```json
"demo20_zone_17"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/resource/demo20_resource_17.json)

### รายการที่เลือกในระบบจอง (`service`)

รหัส `demo20_service_17`

คำถามตัวอย่าง:

- รอบทดลอง มะลิ หนึ่งรอบเล่นได้กี่นาที
- Demo session Jasmine How many minutes does one session last?
- รอบทดลอง มะลิ เวลาเล่นกับเวลาที่กินช่องจองกี่นาที

**booking_product_key — known**
```json
"DEMO20_BOOKING_17"
```
**capacity_max — known**
```json
4
```
**capacity_min — known**
```json
1
```
**name — known**
```json
{
  "en": "Demo session Jasmine",
  "th": "รอบทดลอง มะลิ"
}
```
**occupancy_minutes — known**
```json
120
```
**platform — known**
```json
"PS5"
```
**resource_ids — known**
```json
[
  "demo20_resource_17"
]
```
**session_minutes — known**
```json
120
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_17.json)

### ข้อมูลเกม (`game`)

รหัส `demo20_game_17`

คำถามตัวอย่าง:

- เกมสมมุติ มะลิ เล่นยังไง
- Fictional game Jasmine How do I play it?
- เกมสมมุติ มะลิ เกมเกี่ยวกับอะไรและเล่นยังไง

**age_rating — known**
```json
{
  "en": "Synthetic DEMO rating 6",
  "th": "เรตอายุสมมุติ DEMO 6"
}
```
**edition — known**
```json
"DEMO fiction revision 17"
```
**genre — known**
```json
{
  "en": "Simulation",
  "th": "จำลอง"
}
```
**how_to_play — known**
```json
{
  "en": "Build a town and trade resources; follow the demonstration controls",
  "th": "ต่อชิ้นส่วนเมืองแล้วแลกเปลี่ยนทรัพยากร; ใช้คำสั่งตามชุดควบคุมทดลอง"
}
```
**publisher_url — known**
```json
"https://example.invalid/demo20/fictional-game/17"
```
**summary — known**
```json
{
  "en": "Fictional test game: Build a town and trade resources",
  "th": "เกมแต่งขึ้นเพื่อทดสอบ: ต่อชิ้นส่วนเมืองแล้วแลกเปลี่ยนทรัพยากร"
}
```
**supported_platforms — known**
```json
[
  "PS5"
]
```
**title — known**
```json
{
  "en": "Fictional Paper Town",
  "th": "เกมสมมุติ เมืองกระดาษ"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_17.json)

### กลุ่มผู้ใช้ (`audience`)

รหัส `demo20_audience_17`

คำถามตัวอย่าง:

- กลุ่มผู้ใช้ มะลิ ต้องใช้หลักฐานอะไร
- Demo visitors Jasmine What proof is required?
- กลุ่มผู้ใช้ มะลิ ใครใช้สิทธิ์กลุ่มนี้ได้และต้องแสดงหลักฐานอะไร

**eligibility — known**
```json
{
  "en": "Fictional group 17: demo sessions only",
  "th": "ผู้ใช้สมมุติกลุ่ม 17: ใช้บริการตามรอบทดลอง"
}
```
**name — known**
```json
{
  "en": "Demo visitors Jasmine",
  "th": "กลุ่มผู้ใช้ มะลิ"
}
```
**required_proofs — known**
```json
[
  "DEMO pass Jasmine"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/audience/demo20_audience_17.json)

### ติดต่อ (`contact`)

รหัส `demo20_contact_17`

คำถามตัวอย่าง:

- ช่องทางช่วยเหลือ มะลิ ติดต่อทางไหน
- Demo help channel Jasmine How can I contact them?
- ช่องทางช่วยเหลือ มะลิ ติดต่อที่ไหนและติดต่อได้ช่วงไหน

**channel — known**
```json
"facebook"
```
**office_hours — known**
```json
{
  "en": "Demo hours 09:00–18:00",
  "th": "ช่วงทดลอง 09:00–18:00"
}
```
**purpose — known**
```json
{
  "en": "Fictional support for Changing dates",
  "th": "สอบถามสมมุติเรื่อง เลื่อนวัน"
}
```
**value — known**
```json
"https://example.invalid/demo20/social/17"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_17.json)

### ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`)

รหัส `demo20_procedure_17`

คำถามตัวอย่าง:

- ขั้นตอนทดลอง มะลิ ต้องทำยังไงบ้าง
- Demo procedure Jasmine What steps should I follow?
- ขั้นตอนทดลอง มะลิ มีขั้นตอนอะไรและต้องใช้เอกสารอะไร

**deadline_minutes — known**
```json
15
```
**outcome — known**
```json
{
  "en": "Demo outcome: Changing dates checked",
  "th": "ผลทดสอบ: ตรวจสอบ เลื่อนวัน เสร็จ"
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
  "DEMO pass Jasmine"
]
```
**steps — known**
```json
[
  {
    "contact_id": null,
    "instruction": {
      "en": "Select the fictional Jasmine service",
      "th": "เลือกบริการสมมุติ มะลิ"
    },
    "order": 1
  },
  {
    "contact_id": "demo20_contact_17",
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
"DEMO Changing dates"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_17.json)

### นโยบายและกฎศูนย์ (`policy`)

รหัส `demo20_policy_17`

คำถามตัวอย่าง:

- ข้อกำหนดทดลอง มะลิ กฎเป็นยังไง
- Demo policy Jasmine What are the rules?
- ข้อกำหนดทดลอง มะลิ อนุญาตไหมและมีข้อยกเว้นอะไร

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
"conditional"
```
**details — known**
```json
{
  "en": "Fictional rule for Changing dates: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "กติกาสมมุติเรื่องเลื่อนวัน: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
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
"demo20_procedure_17"
```
**subject — known**
```json
{
  "en": "Demo policy Jasmine",
  "th": "ข้อกำหนดทดลอง มะลิ"
}
```
**topic — known**
```json
"DEMO Changing dates"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/policy/demo20_policy_17.json)

### สิ่งอำนวยความสะดวก (`facility`)

รหัส `demo20_facility_17`

คำถามตัวอย่าง:

- พื้นที่พัก มะลิ อยู่ตรงไหนในร้าน
- Demo amenity Jasmine Where in the venue is it?
- พื้นที่พัก มะลิ อยู่ตรงไหนและคนที่ต้องการความช่วยเหลือเข้าใช้ยังไง

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
  "en": "Rescheduling waiting area in demo room 117",
  "th": "มุมรอรอบใหม่ อยู่ห้องทดสอบ 117"
}
```
**name — known**
```json
{
  "en": "Demo amenity Jasmine",
  "th": "พื้นที่พัก มะลิ"
}
```
**usage_conditions — known**
```json
{
  "en": "Demo sessions only; ask the operator first",
  "th": "ใช้ตามรอบทดลอง; ต้องขอผู้ดูแลก่อน"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/facility/demo20_facility_17.json)

### เกมที่ศูนย์มีให้เล่นจริง (`game_service`)

รหัส `demo20_game_service_17`

คำถามตัวอย่าง:

- การติดตั้งทดลอง มะลิ มีให้เล่นหรือยัง
- Demo installation Jasmine Is this game offered?
- การติดตั้งทดลอง มะลิ มีให้เล่นไหมและติดตั้งรุ่นไหน

**account_policy_id — known**
```json
"demo20_policy_17"
```
**game_id — known**
```json
"demo20_game_17"
```
**game_version — known**
```json
"DEMO BUILD 17"
```
**installed_resource_ids — known**
```json
[
  "demo20_resource_17"
]
```
**offered — known**
```json
true
```
**service_id — known**
```json
"demo20_service_17"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_service/demo20_game_service_17.json)

### รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`)

รหัส `demo20_game_mode_17`

คำถามตัวอย่าง:

- โหมดทดลอง มะลิ เล่นพร้อมกันได้สูงสุดกี่คน
- Demo mode Jasmine How many people can play together at most?
- โหมดทดลอง มะลิ ต้องมีขั้นต่ำกี่คนและเล่นได้สูงสุดกี่คน

**game_id — known**
```json
"demo20_game_17"
```
**mode_name — known**
```json
{
  "en": "Demo mode Jasmine",
  "th": "โหมดทดลอง มะลิ"
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
"PS5"
```
**players_max — known**
```json
4
```
**players_min — known**
```json
1
```
**studio_supported — known**
```json
true
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_mode/demo20_game_mode_17.json)

### วิธีเล่นและปุ่ม (`control_set`)

รหัส `demo20_control_set_17`

คำถามตัวอย่าง:

- ชุดควบคุมทดลอง มะลิ ปุ่มอะไรบ้าง
- Demo controls Jasmine What are the controls?
- ชุดควบคุมทดลอง มะลิ ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร

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
      "en": "Fictional input for Paper Town",
      "th": "คำสั่งสมมุติของ เมืองกระดาษ"
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
      "en": "Fictional input for Paper Town",
      "th": "คำสั่งสมมุติของ เมืองกระดาษ"
    },
    "gesture": "press"
  },
  {
    "action": {
      "en": "Back",
      "th": "ย้อนกลับ"
    },
    "buttons": [
      "DEMO_gamepad_3"
    ],
    "context": {
      "en": "Fictional input for Paper Town",
      "th": "คำสั่งสมมุติของ เมืองกระดาษ"
    },
    "gesture": "press"
  }
]
```
**game_id — known**
```json
"demo20_game_17"
```
**game_version — known**
```json
"DEMO BUILD 17"
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
"PS5"
```
**preset — known**
```json
"DEMO_LAYOUT_17"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_17.json)

### ราคาต่อบริการ (`rate`)

รหัส `demo20_rate_17`

คำถามตัวอย่าง:

- อัตราทดลอง มะลิ ราคาเท่าไหร่
- Demo tariff Jasmine How much does it cost?
- อัตราทดลอง มะลิ ราคาเท่าไหร่และได้กี่นาที

**amount_minor — known**
```json
22000
```
**audience_id — known**
```json
"demo20_audience_17"
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
120
```
**persons_max — known**
```json
4
```
**persons_min — known**
```json
1
```
**service_id — known**
```json
"demo20_service_17"
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
"per_hour"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rate/demo20_rate_17.json)

### ราคาเหมาโซน/ห้อง (`rental_package`)

รหัส `demo20_rental_package_17`

คำถามตัวอย่าง:

- แพ็กเกจทดลอง มะลิ เหมาเท่าไหร่
- Demo package Jasmine How much is the rental?
- แพ็กเกจทดลอง มะลิ ราคาเหมาเท่าไหร่และรวมอุปกรณ์อะไร

**amount_minor — known**
```json
67250
```
**audience_id — known**
```json
"demo20_audience_17"
```
**currency — known**
```json
"THB"
```
**duration_minutes — known**
```json
240
```
**equipment_included — known**
```json
{
  "en": "Fictional Jasmine station and PS5 inputs",
  "th": "เครื่องสมมุติ มะลิ พร้อมอุปกรณ์ PS5"
}
```
**name — known**
```json
{
  "en": "Demo package Jasmine",
  "th": "แพ็กเกจทดลอง มะลิ"
}
```
**period_label — known**
```json
"custom"
```
**room_seats — known**
```json
8
```
**terms — known**
```json
{
  "en": "Synthetic package excludes extensions; 1–4 people per session",
  "th": "แพ็กเกจสมมุติไม่รวมค่าต่อเวลา; รอบละ 1–4 คน"
}
```
**zone_ids — known**
```json
[
  "demo20_zone_17"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rental_package/demo20_rental_package_17.json)

### ตารางบริการ (`schedule`)

รหัส `demo20_schedule_17`

คำถามตัวอย่าง:

- ตารางทดลอง มะลิ จองช่วงไหนได้บ้าง
- Demo timetable Jasmine What are the booking hours?
- ตารางทดลอง มะลิ เปิดช่วงไหนและพักบำรุงรักษาตอนไหน

**bookable_periods — known**
```json
[
  {
    "end": "12:00",
    "start": "09:00"
  },
  {
    "end": "18:00",
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
    "end": "18:00",
    "start": "09:00"
  }
]
```
**reason — known**
```json
{
  "en": "Synthetic Jasmine schedule with maintenance",
  "th": "ตารางสมมุติ มะลิ มีพักบำรุงรักษา"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```
**weekday — known**
```json
3
```
**zone_ids — known**
```json
[
  "demo20_zone_17"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_17.json)

### วันปิด/ข้อยกเว้น (`closure`)

รหัส `demo20_closure_17`

คำถามตัวอย่าง:

- ประกาศวันทดลอง มะลิ วันนั้นปิดไหม
- Demo date notice Jasmine Is it closed on that date?
- ประกาศวันทดลอง มะลิ วันนั้นเปิดปิดยังไงและเพราะอะไร

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
"2026-12-17"
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
  "en": "Synthetic Jasmine date notice: open_override",
  "th": "ประกาศสมมุติ มะลิ: open_override"
}
```
**resolution_policy_id — known**
```json
"demo20_policy_17"
```
**state — known**
```json
"open_override"
```
**zone_ids — known**
```json
[
  "demo20_zone_17"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/closure/demo20_closure_17.json)

### รายการแข่งขันและฉบับกติกา (`competition`)

รหัส `demo20_competition_17`

คำถามตัวอย่าง:

- รายการฝึก มะลิ ใช้กติกาฉบับไหน
- Demo event Jasmine Which rulebook release applies?
- รายการฝึก มะลิ ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่

**competition_dates — known**
```json
[
  "2026-12-17"
]
```
**coverage — known**
```json
"complete"
```
**division — known**
```json
{
  "en": "Practice group 1–4 players",
  "th": "กลุ่มฝึก 1–4 คน"
}
```
**event_name — known**
```json
{
  "en": "Demo event Jasmine",
  "th": "รายการฝึก มะลิ"
}
```
**game_id — known**
```json
"demo20_game_17"
```
**rulebook_release — known**
```json
"DEMO20_REV_17"
```
**supersedes_id — not_applicable**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_17.json)

### ข้อกติกาการแข่งขัน (`competition_rule`)

รหัส `demo20_competition_rule_17`

คำถามตัวอย่าง:

- ข้อการแข่งขันทดลอง มะลิ ข้อนี้กำหนดอะไร
- Demo rule Jasmine What does this rule require?
- ข้อการแข่งขันทดลอง มะลิ กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม

**competition_id — known**
```json
"demo20_competition_17"
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
"fair_play_conduct"
```
**heading — known**
```json
{
  "en": "Demo rule Jasmine",
  "th": "ข้อการแข่งขันทดลอง มะลิ"
}
```
**section_number — known**
```json
"3.17"
```
**text — known**
```json
{
  "en": "Fictional clause 17: for Changing dates, follow decision conditional; exception requires written demo operator approval; not actual rules",
  "th": "ข้อสมมุติ 17: เลื่อนวัน ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_17.json)

### ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`)

รหัส `demo20_news_17`

คำถามตัวอย่าง:

- ข่าวทดลอง มะลิ ประกาศว่าอะไร
- Demo bulletin Jasmine What does the announcement say?
- ข่าวทดลอง มะลิ ประกาศอะไรและกิจกรรมเริ่มจบเมื่อไหร่

**audience_ids — known**
```json
[
  "demo20_audience_17"
]
```
**body — known**
```json
{
  "en": "Synthetic bulletin: Paper Town activity for 1–4 people; no actual payment",
  "th": "ข่าวสมมุติ: กิจกรรมเมืองกระดาษ สำหรับกลุ่ม 1–4 คน; ไม่มีรับเงินจริง"
}
```
**contact_id — known**
```json
"demo20_contact_17"
```
**event_end — known**
```json
"2026-12-17T12:00:00+07:00"
```
**event_start — known**
```json
"2026-12-17T10:00:00+07:00"
```
**registration_url — known**
```json
"https://example.invalid/demo20/register/17"
```
**title — known**
```json
{
  "en": "Demo bulletin Jasmine",
  "th": "ข่าวทดลอง มะลิ"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/news/demo20_news_17.json)

### บุคลากร/ทีมที่เปิดเผยได้ (`person`)

รหัส `demo20_person_17`

คำถามตัวอย่าง:

- ผู้ดูแลสมมุติ มะลิ รับผิดชอบอะไร
- Fictional host Jasmine What is their role?
- ผู้ดูแลสมมุติ มะลิ รับผิดชอบเรื่องอะไรและติดต่อทางไหน

**display_name — known**
```json
{
  "en": "Fictional host Jasmine",
  "th": "ผู้ดูแลสมมุติ มะลิ"
}
```
**public_contact_id — known**
```json
"demo20_contact_17"
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
  "en": "Fictional host for Changing dates",
  "th": "ผู้ดูแลสมมุติเรื่อง เลื่อนวัน"
}
```
**team — known**
```json
{
  "en": "Demo Jasmine team",
  "th": "ทีมทดสอบ มะลิ"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/person/demo20_person_17.json)

### คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`)

รหัส `demo20_faq_17`

คำถามตัวอย่าง:

- คำถามตัวอย่าง มะลิ คำตอบคืออะไร
- Demo enquiry Jasmine What is the answer?
- คำถามตัวอย่าง มะลิ คำตอบคืออะไรและใช้กับกรณีไหน

**answer — known**
```json
{
  "en": "Example answer: Fictional rule for Changing dates: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องเลื่อนวัน: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
}
```
**question — known**
```json
{
  "en": "Demo enquiry Jasmine",
  "th": "คำถามตัวอย่าง มะลิ"
}
```
**related_ids — known**
```json
[
  "demo20_policy_17",
  "demo20_procedure_17"
]
```
**scope_note — known**
```json
{
  "en": "Only applies to fictional Jasmine scenario",
  "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ มะลิ"
}
```
**topic — known**
```json
"DEMO Changing dates"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_17.json)

### การเชื่อมสถานะสด (`live_binding`)

รหัส `demo20_live_binding_17`

คำถามตัวอย่าง:

- ตัวเชื่อมทดลอง มะลิ จับคู่สถานะยังไง
- Demo binding Jasmine How are statuses mapped?
- ตัวเชื่อมทดลอง มะลิ จับคู่สถานะแบบไหนและเก็บข้อมูลนานเท่าไหร่

**external_resource_key — known**
```json
"DEMO20_EXTERNAL_17"
```
**freshness_policy — known**
```json
{
  "en": "Synthetic TTL 100 seconds; no API call or live status claim",
  "th": "ค่าจำลอง TTL 100 วินาที; ไม่เรียก API และไม่ยืนยันสถานะสด"
}
```
**physical_pool_key — known**
```json
"demo20_pool_17"
```
**provider — known**
```json
"wordpress_booking"
```
**service_id — known**
```json
"demo20_service_17"
```
**status_mapping — known**
```json
[
  {
    "normalized": "free",
    "raw": "DEMO_EMPTY_17"
  },
  {
    "normalized": "occupied",
    "raw": "DEMO_BUSY_17"
  },
  {
    "normalized": "unknown",
    "raw": "DEMO_UNKNOWN_17"
  }
]
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/live_binding/demo20_live_binding_17.json)

