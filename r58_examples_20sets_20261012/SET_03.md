# ชุด 03 — ละอองฝน / Drizzle

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

เกม สถานที่ ราคา กฎ บุคคล และสถานะทั้งหมดในชุดใหม่นี้แต่งขึ้นเพื่อทดสอบ ไม่ได้เป็นข้อมูล PSU หรือเกมที่มีจำหน่ายจริง คำแปลยังไม่ผ่านมนุษย์

แพลตฟอร์มตัวอย่าง: VR • จำนวนผู้เล่น 1–1 • เวลาเล่น 30 นาที / กินช่องจอง 60 นาที

## ข้อมูลครบ 24 หมวด

### ข้อมูลศูนย์ (`center`)

รหัส `demo20_center_03`

คำถามตัวอย่าง:

- ศูนย์ทดลอง ละอองฝน อยู่ตรงไหน
- Demo venue Drizzle Where is it located?
- ศูนย์ทดลอง ละอองฝน อยู่ตึกอะไร ชั้นไหน

**address — known**
```json
{
  "en": "Fictional address 21, Example Road, Test District",
  "th": "เลขที่สมมุติ 21 ถนนตัวอย่าง แขวงทดลอง"
}
```
**building — known**
```json
"DEMO Tower D"
```
**description — known**
```json
{
  "en": "Synthetic scenario 3: Virtual Beacon, not a real venue",
  "th": "สถานการณ์ทดลอง 3: ประภาคารเสมือน ไม่ใช่สถานที่จริง"
}
```
**floor — known**
```json
"4"
```
**map_url — known**
```json
"https://example.invalid/demo20/map/3"
```
**name — known**
```json
{
  "en": "Demo venue Drizzle",
  "th": "ศูนย์ทดลอง ละอองฝน"
}
```
**operator — known**
```json
{
  "en": "Fictional Drizzle operator",
  "th": "ผู้ประกอบการสมมุติ ละอองฝน"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/center/demo20_center_03.json)

### โซนบริการ (`zone`)

รหัส `demo20_zone_03`

คำถามตัวอย่าง:

- โซนทดลอง ละอองฝน มีที่นั่งกี่ที่
- Demo zone Drizzle How many seats are there?
- โซนทดลอง ละอองฝน โซนนี้อยู่ตรงไหนและมีที่นั่งกี่ที่

**description — known**
```json
{
  "en": "Synthetic VR zone for Virtual Beacon",
  "th": "โซนจำลอง VR สำหรับประภาคารเสมือน"
}
```
**location — known**
```json
{
  "en": "Test building, floor 4, room 103",
  "th": "อาคารทดสอบ ชั้น 4 ห้อง 103"
}
```
**name — known**
```json
{
  "en": "Demo zone Drizzle",
  "th": "โซนทดลอง ละอองฝน"
}
```
**room_seats — known**
```json
3
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_03.json)

### รุ่นและสเปกอุปกรณ์ (`equipment_model`)

รหัส `demo20_equipment_model_03`

คำถามตัวอย่าง:

- รุ่นอุปกรณ์ ละอองฝน สเปกมีอะไรบ้าง
- Demo model Drizzle What are its specifications?
- รุ่นอุปกรณ์ ละอองฝน เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง

**device_type — known**
```json
"vr"
```
**name — known**
```json
{
  "en": "Demo model Drizzle",
  "th": "รุ่นอุปกรณ์ ละอองฝน"
}
```
**specifications — known**
```json
[
  {
    "key": "DEMO screen",
    "unit": "inch",
    "value": "33"
  },
  {
    "key": "DEMO input",
    "unit": "",
    "value": "vr_motion"
  }
]
```
**usage — known**
```json
{
  "en": "Fictional equipment for VR; not a PSU specification",
  "th": "เครื่องสมมุติใช้กับ VR; ห้ามอ้างเป็นสเปกศูนย์"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_03.json)

### เครื่องหรือทรัพยากรจริง (`resource`)

รหัส `demo20_resource_03`

คำถามตัวอย่าง:

- เครื่องทดลอง ละอองฝน เล่นพร้อมกันได้กี่คน
- Demo station Drizzle How many people can play at once?
- เครื่องทดลอง ละอองฝน เครื่องยังใช้งานได้ไหมและรองรับกี่คน

**capacity_persons — known**
```json
1
```
**equipment_model_ids — known**
```json
[
  "demo20_equipment_model_03"
]
```
**name — known**
```json
{
  "en": "Demo station Drizzle",
  "th": "เครื่องทดลอง ละอองฝน"
}
```
**operational_status — known**
```json
"in_service"
```
**physical_pool_key — known**
```json
"demo20_pool_03"
```
**zone_id — known**
```json
"demo20_zone_03"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/resource/demo20_resource_03.json)

### รายการที่เลือกในระบบจอง (`service`)

รหัส `demo20_service_03`

คำถามตัวอย่าง:

- รอบทดลอง ละอองฝน หนึ่งรอบเล่นได้กี่นาที
- Demo session Drizzle How many minutes does one session last?
- รอบทดลอง ละอองฝน เวลาเล่นกับเวลาที่กินช่องจองกี่นาที

**booking_product_key — known**
```json
"DEMO20_BOOKING_03"
```
**capacity_max — known**
```json
1
```
**capacity_min — known**
```json
1
```
**name — known**
```json
{
  "en": "Demo session Drizzle",
  "th": "รอบทดลอง ละอองฝน"
}
```
**occupancy_minutes — known**
```json
60
```
**platform — known**
```json
"VR"
```
**resource_ids — known**
```json
[
  "demo20_resource_03"
]
```
**session_minutes — known**
```json
30
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_03.json)

### ข้อมูลเกม (`game`)

รหัส `demo20_game_03`

คำถามตัวอย่าง:

- เกมสมมุติ ละอองฝน เล่นยังไง
- Fictional game Drizzle How do I play it?
- เกมสมมุติ ละอองฝน เกมเกี่ยวกับอะไรและเล่นยังไง

**age_rating — known**
```json
{
  "en": "Synthetic DEMO rating 12",
  "th": "เรตอายุสมมุติ DEMO 12"
}
```
**edition — known**
```json
"DEMO fiction revision 3"
```
**genre — known**
```json
{
  "en": "Rhythm",
  "th": "จังหวะ"
}
```
**how_to_play — known**
```json
{
  "en": "Use motion inputs to arrange lights guiding ships; follow the demonstration controls",
  "th": "ใช้มือเสมือนจัดแสงนำทางเรือ; ใช้คำสั่งตามชุดควบคุมทดลอง"
}
```
**publisher_url — known**
```json
"https://example.invalid/demo20/fictional-game/3"
```
**summary — known**
```json
{
  "en": "Fictional test game: Use motion inputs to arrange lights guiding ships",
  "th": "เกมแต่งขึ้นเพื่อทดสอบ: ใช้มือเสมือนจัดแสงนำทางเรือ"
}
```
**supported_platforms — known**
```json
[
  "VR"
]
```
**title — known**
```json
{
  "en": "Fictional Virtual Beacon",
  "th": "เกมสมมุติ ประภาคารเสมือน"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_03.json)

### กลุ่มผู้ใช้ (`audience`)

รหัส `demo20_audience_03`

คำถามตัวอย่าง:

- กลุ่มผู้ใช้ ละอองฝน ต้องใช้หลักฐานอะไร
- Demo visitors Drizzle What proof is required?
- กลุ่มผู้ใช้ ละอองฝน ใครใช้สิทธิ์กลุ่มนี้ได้และต้องแสดงหลักฐานอะไร

**eligibility — known**
```json
{
  "en": "Fictional group 3: demo sessions only",
  "th": "ผู้ใช้สมมุติกลุ่ม 3: ใช้บริการตามรอบทดลอง"
}
```
**name — known**
```json
{
  "en": "Demo visitors Drizzle",
  "th": "กลุ่มผู้ใช้ ละอองฝน"
}
```
**required_proofs — known**
```json
[
  "DEMO pass Drizzle"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/audience/demo20_audience_03.json)

### ติดต่อ (`contact`)

รหัส `demo20_contact_03`

คำถามตัวอย่าง:

- ช่องทางช่วยเหลือ ละอองฝน ติดต่อทางไหน
- Demo help channel Drizzle How can I contact them?
- ช่องทางช่วยเหลือ ละอองฝน ติดต่อที่ไหนและติดต่อได้ช่วงไหน

**channel — known**
```json
"website"
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
  "en": "Fictional support for Motion discomfort breaks",
  "th": "สอบถามสมมุติเรื่อง พักเมื่อเวียนหัว"
}
```
**value — known**
```json
"https://example.invalid/demo20/contact/3"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_03.json)

### ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`)

รหัส `demo20_procedure_03`

คำถามตัวอย่าง:

- ขั้นตอนทดลอง ละอองฝน ต้องทำยังไงบ้าง
- Demo procedure Drizzle What steps should I follow?
- ขั้นตอนทดลอง ละอองฝน มีขั้นตอนอะไรและต้องใช้เอกสารอะไร

**deadline_minutes — known**
```json
30
```
**outcome — known**
```json
{
  "en": "Demo outcome: Motion discomfort breaks checked",
  "th": "ผลทดสอบ: ตรวจสอบ พักเมื่อเวียนหัว เสร็จ"
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
  "DEMO pass Drizzle"
]
```
**steps — known**
```json
[
  {
    "contact_id": null,
    "instruction": {
      "en": "Select the fictional Drizzle service",
      "th": "เลือกบริการสมมุติ ละอองฝน"
    },
    "order": 1
  },
  {
    "contact_id": "demo20_contact_03",
    "instruction": {
      "en": "Check names and conditions before confirming",
      "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
    },
    "order": 2
  },
  {
    "contact_id": "demo20_contact_03",
    "instruction": {
      "en": "Ask the demo operator for session-specific help",
      "th": "แจ้งผู้ดูแลเพื่อขอความช่วยเหลือเฉพาะรอบทดลอง"
    },
    "order": 3
  }
]
```
**topic — known**
```json
"DEMO Motion discomfort breaks"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_03.json)

### นโยบายและกฎศูนย์ (`policy`)

รหัส `demo20_policy_03`

คำถามตัวอย่าง:

- ข้อกำหนดทดลอง ละอองฝน กฎเป็นยังไง
- Demo policy Drizzle What are the rules?
- ข้อกำหนดทดลอง ละอองฝน อนุญาตไหมและมีข้อยกเว้นอะไร

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
  "en": "Fictional rule for Motion discomfort breaks: required; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "กติกาสมมุติเรื่องพักเมื่อเวียนหัว: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
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
"demo20_procedure_03"
```
**subject — known**
```json
{
  "en": "Demo policy Drizzle",
  "th": "ข้อกำหนดทดลอง ละอองฝน"
}
```
**topic — known**
```json
"DEMO Motion discomfort breaks"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/policy/demo20_policy_03.json)

### สิ่งอำนวยความสะดวก (`facility`)

รหัส `demo20_facility_03`

คำถามตัวอย่าง:

- พื้นที่พัก ละอองฝน อยู่ตรงไหนในร้าน
- Demo amenity Drizzle Where in the venue is it?
- พื้นที่พัก ละอองฝน อยู่ตรงไหนและคนที่ต้องการความช่วยเหลือเข้าใช้ยังไง

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
  "en": "VR rest chair in demo room 103",
  "th": "เก้าอี้พัก VR อยู่ห้องทดสอบ 103"
}
```
**name — known**
```json
{
  "en": "Demo amenity Drizzle",
  "th": "พื้นที่พัก ละอองฝน"
}
```
**usage_conditions — known**
```json
{
  "en": "Demo sessions only; ask the operator first",
  "th": "ใช้ตามรอบทดลอง; ต้องขอผู้ดูแลก่อน"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/facility/demo20_facility_03.json)

### เกมที่ศูนย์มีให้เล่นจริง (`game_service`)

รหัส `demo20_game_service_03`

คำถามตัวอย่าง:

- การติดตั้งทดลอง ละอองฝน มีให้เล่นหรือยัง
- Demo installation Drizzle Is this game offered?
- การติดตั้งทดลอง ละอองฝน มีให้เล่นไหมและติดตั้งรุ่นไหน

**account_policy_id — known**
```json
"demo20_policy_03"
```
**game_id — known**
```json
"demo20_game_03"
```
**game_version — known**
```json
"DEMO BUILD 3"
```
**installed_resource_ids — known**
```json
[
  "demo20_resource_03"
]
```
**offered — known**
```json
true
```
**service_id — known**
```json
"demo20_service_03"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_service/demo20_game_service_03.json)

### รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`)

รหัส `demo20_game_mode_03`

คำถามตัวอย่าง:

- โหมดทดลอง ละอองฝน เล่นพร้อมกันได้สูงสุดกี่คน
- Demo mode Drizzle How many people can play together at most?
- โหมดทดลอง ละอองฝน ต้องมีขั้นต่ำกี่คนและเล่นได้สูงสุดกี่คน

**game_id — known**
```json
"demo20_game_03"
```
**mode_name — known**
```json
{
  "en": "Demo mode Drizzle",
  "th": "โหมดทดลอง ละอองฝน"
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
"VR"
```
**players_max — known**
```json
1
```
**players_min — known**
```json
1
```
**studio_supported — known**
```json
true
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_mode/demo20_game_mode_03.json)

### วิธีเล่นและปุ่ม (`control_set`)

รหัส `demo20_control_set_03`

คำถามตัวอย่าง:

- ชุดควบคุมทดลอง ละอองฝน ปุ่มอะไรบ้าง
- Demo controls Drizzle What are the controls?
- ชุดควบคุมทดลอง ละอองฝน ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร

**bindings — known**
```json
[
  {
    "action": {
      "en": "Confirm",
      "th": "ยืนยัน"
    },
    "buttons": [
      "DEMO_vr_motion_1"
    ],
    "context": {
      "en": "Fictional input for Virtual Beacon",
      "th": "คำสั่งสมมุติของ ประภาคารเสมือน"
    },
    "gesture": "press"
  }
]
```
**game_id — known**
```json
"demo20_game_03"
```
**game_version — known**
```json
"DEMO BUILD 3"
```
**input_device — known**
```json
"vr_motion"
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
"VR"
```
**preset — known**
```json
"DEMO_LAYOUT_3"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_03.json)

### ราคาต่อบริการ (`rate`)

รหัส `demo20_rate_03`

คำถามตัวอย่าง:

- อัตราทดลอง ละอองฝน ราคาเท่าไหร่
- Demo tariff Drizzle How much does it cost?
- อัตราทดลอง ละอองฝน ราคาเท่าไหร่และได้กี่นาที

**amount_minor — known**
```json
7500
```
**audience_id — known**
```json
"demo20_audience_03"
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
30
```
**persons_max — known**
```json
1
```
**persons_min — known**
```json
1
```
**service_id — known**
```json
"demo20_service_03"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rate/demo20_rate_03.json)

### ราคาเหมาโซน/ห้อง (`rental_package`)

รหัส `demo20_rental_package_03`

คำถามตัวอย่าง:

- แพ็กเกจทดลอง ละอองฝน เหมาเท่าไหร่
- Demo package Drizzle How much is the rental?
- แพ็กเกจทดลอง ละอองฝน ราคาเหมาเท่าไหร่และรวมอุปกรณ์อะไร

**amount_minor — known**
```json
23750
```
**audience_id — known**
```json
"demo20_audience_03"
```
**currency — known**
```json
"THB"
```
**duration_minutes — known**
```json
180
```
**equipment_included — known**
```json
{
  "en": "Fictional Drizzle station and VR inputs",
  "th": "เครื่องสมมุติ ละอองฝน พร้อมอุปกรณ์ VR"
}
```
**name — known**
```json
{
  "en": "Demo package Drizzle",
  "th": "แพ็กเกจทดลอง ละอองฝน"
}
```
**period_label — known**
```json
"half_day"
```
**room_seats — known**
```json
3
```
**terms — known**
```json
{
  "en": "Synthetic package excludes extensions; 1–1 people per session",
  "th": "แพ็กเกจสมมุติไม่รวมค่าต่อเวลา; รอบละ 1–1 คน"
}
```
**zone_ids — known**
```json
[
  "demo20_zone_03"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rental_package/demo20_rental_package_03.json)

### ตารางบริการ (`schedule`)

รหัส `demo20_schedule_03`

คำถามตัวอย่าง:

- ตารางทดลอง ละอองฝน จองช่วงไหนได้บ้าง
- Demo timetable Drizzle What are the booking hours?
- ตารางทดลอง ละอองฝน เปิดช่วงไหนและพักบำรุงรักษาตอนไหน

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
  "en": "Synthetic Drizzle schedule with maintenance",
  "th": "ตารางสมมุติ ละอองฝน มีพักบำรุงรักษา"
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
  "demo20_zone_03"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_03.json)

### วันปิด/ข้อยกเว้น (`closure`)

รหัส `demo20_closure_03`

คำถามตัวอย่าง:

- ประกาศวันทดลอง ละอองฝน วันนั้นปิดไหม
- Demo date notice Drizzle Is it closed on that date?
- ประกาศวันทดลอง ละอองฝน วันนั้นเปิดปิดยังไงและเพราะอะไร

**bookable_periods — known**
```json
[]
```
**local_date — known**
```json
"2026-12-03"
```
**open_periods — known**
```json
[]
```
**reason — known**
```json
{
  "en": "Synthetic Drizzle date notice: closed",
  "th": "ประกาศสมมุติ ละอองฝน: closed"
}
```
**resolution_policy_id — known**
```json
"demo20_policy_03"
```
**state — known**
```json
"closed"
```
**zone_ids — known**
```json
[
  "demo20_zone_03"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/closure/demo20_closure_03.json)

### รายการแข่งขันและฉบับกติกา (`competition`)

รหัส `demo20_competition_03`

คำถามตัวอย่าง:

- รายการฝึก ละอองฝน ใช้กติกาฉบับไหน
- Demo event Drizzle Which rulebook release applies?
- รายการฝึก ละอองฝน ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่

**competition_dates — known**
```json
[
  "2026-12-03"
]
```
**coverage — known**
```json
"partial"
```
**division — known**
```json
{
  "en": "Practice group 1–1 players",
  "th": "กลุ่มฝึก 1–1 คน"
}
```
**event_name — known**
```json
{
  "en": "Demo event Drizzle",
  "th": "รายการฝึก ละอองฝน"
}
```
**game_id — known**
```json
"demo20_game_03"
```
**rulebook_release — known**
```json
"DEMO20_REV_3"
```
**supersedes_id — not_applicable**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_03.json)

### ข้อกติกาการแข่งขัน (`competition_rule`)

รหัส `demo20_competition_rule_03`

คำถามตัวอย่าง:

- ข้อการแข่งขันทดลอง ละอองฝน ข้อนี้กำหนดอะไร
- Demo rule Drizzle What does this rule require?
- ข้อการแข่งขันทดลอง ละอองฝน กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม

**competition_id — known**
```json
"demo20_competition_03"
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
"competition_format"
```
**heading — known**
```json
{
  "en": "Demo rule Drizzle",
  "th": "ข้อการแข่งขันทดลอง ละอองฝน"
}
```
**section_number — known**
```json
"4.3"
```
**text — known**
```json
{
  "en": "Fictional clause 3: for Motion discomfort breaks, follow decision required; exception requires written demo operator approval; not actual rules",
  "th": "ข้อสมมุติ 3: พักเมื่อเวียนหัว ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_03.json)

### ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`)

รหัส `demo20_news_03`

คำถามตัวอย่าง:

- ข่าวทดลอง ละอองฝน ประกาศว่าอะไร
- Demo bulletin Drizzle What does the announcement say?
- ข่าวทดลอง ละอองฝน ประกาศอะไรและกิจกรรมเริ่มจบเมื่อไหร่

**audience_ids — known**
```json
[
  "demo20_audience_03"
]
```
**body — known**
```json
{
  "en": "Synthetic bulletin: Virtual Beacon activity for 1–1 people; no actual payment",
  "th": "ข่าวสมมุติ: กิจกรรมประภาคารเสมือน สำหรับกลุ่ม 1–1 คน; ไม่มีรับเงินจริง"
}
```
**contact_id — known**
```json
"demo20_contact_03"
```
**event_end — known**
```json
"2026-12-03T12:00:00+07:00"
```
**event_start — known**
```json
"2026-12-03T10:00:00+07:00"
```
**registration_url — known**
```json
"https://example.invalid/demo20/register/3"
```
**title — known**
```json
{
  "en": "Demo bulletin Drizzle",
  "th": "ข่าวทดลอง ละอองฝน"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/news/demo20_news_03.json)

### บุคลากร/ทีมที่เปิดเผยได้ (`person`)

รหัส `demo20_person_03`

คำถามตัวอย่าง:

- ผู้ดูแลสมมุติ ละอองฝน รับผิดชอบอะไร
- Fictional host Drizzle What is their role?
- ผู้ดูแลสมมุติ ละอองฝน รับผิดชอบเรื่องอะไรและติดต่อทางไหน

**display_name — known**
```json
{
  "en": "Fictional host Drizzle",
  "th": "ผู้ดูแลสมมุติ ละอองฝน"
}
```
**public_contact_id — known**
```json
"demo20_contact_03"
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
  "en": "Fictional host for Motion discomfort breaks",
  "th": "ผู้ดูแลสมมุติเรื่อง พักเมื่อเวียนหัว"
}
```
**team — known**
```json
{
  "en": "Demo Drizzle team",
  "th": "ทีมทดสอบ ละอองฝน"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/person/demo20_person_03.json)

### คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`)

รหัส `demo20_faq_03`

คำถามตัวอย่าง:

- คำถามตัวอย่าง ละอองฝน คำตอบคืออะไร
- Demo enquiry Drizzle What is the answer?
- คำถามตัวอย่าง ละอองฝน คำตอบคืออะไรและใช้กับกรณีไหน

**answer — known**
```json
{
  "en": "Example answer: Fictional rule for Motion discomfort breaks: required; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องพักเมื่อเวียนหัว: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
}
```
**question — known**
```json
{
  "en": "Demo enquiry Drizzle",
  "th": "คำถามตัวอย่าง ละอองฝน"
}
```
**related_ids — known**
```json
[
  "demo20_policy_03",
  "demo20_procedure_03"
]
```
**scope_note — known**
```json
{
  "en": "Only applies to fictional Drizzle scenario",
  "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ละอองฝน"
}
```
**topic — known**
```json
"DEMO Motion discomfort breaks"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_03.json)

### การเชื่อมสถานะสด (`live_binding`)

รหัส `demo20_live_binding_03`

คำถามตัวอย่าง:

- ตัวเชื่อมทดลอง ละอองฝน จับคู่สถานะยังไง
- Demo binding Drizzle How are statuses mapped?
- ตัวเชื่อมทดลอง ละอองฝน จับคู่สถานะแบบไหนและเก็บข้อมูลนานเท่าไหร่

**external_resource_key — known**
```json
"DEMO20_EXTERNAL_3"
```
**freshness_policy — known**
```json
{
  "en": "Synthetic TTL 30 seconds; no API call or live status claim",
  "th": "ค่าจำลอง TTL 30 วินาที; ไม่เรียก API และไม่ยืนยันสถานะสด"
}
```
**physical_pool_key — known**
```json
"demo20_pool_03"
```
**provider — known**
```json
"wordpress_booking"
```
**service_id — known**
```json
"demo20_service_03"
```
**status_mapping — known**
```json
[
  {
    "normalized": "free",
    "raw": "DEMO_EMPTY_3"
  },
  {
    "normalized": "occupied",
    "raw": "DEMO_BUSY_3"
  },
  {
    "normalized": "unknown",
    "raw": "DEMO_UNKNOWN_3"
  }
]
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/live_binding/demo20_live_binding_03.json)

