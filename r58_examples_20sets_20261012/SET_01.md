# ชุด 01 — ดาวเหนือ / Northstar

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

เกม สถานที่ ราคา กฎ บุคคล และสถานะทั้งหมดในชุดใหม่นี้แต่งขึ้นเพื่อทดสอบ ไม่ได้เป็นข้อมูล PSU หรือเกมที่มีจำหน่ายจริง คำแปลยังไม่ผ่านมนุษย์

แพลตฟอร์มตัวอย่าง: Nintendo Switch • จำนวนผู้เล่น 1–4 • เวลาเล่น 60 นาที / กินช่องจอง 60 นาที

## ข้อมูลครบ 24 หมวด

### ข้อมูลศูนย์ (`center`)

รหัส `demo20_center_01`

คำถามตัวอย่าง:

- ศูนย์ทดลอง ดาวเหนือ อยู่ตรงไหน
- Demo venue Northstar Where is it located?
- ศูนย์ทดลอง ดาวเหนือ อยู่ตึกอะไร ชั้นไหน

**address — known**
```json
{
  "en": "Fictional address 7, Example Road, Test District",
  "th": "เลขที่สมมุติ 7 ถนนตัวอย่าง แขวงทดลอง"
}
```
**building — known**
```json
"DEMO Tower B"
```
**description — known**
```json
{
  "en": "Synthetic scenario 1: Cloud Garden, not a real venue",
  "th": "สถานการณ์ทดลอง 1: สวนเมฆ ไม่ใช่สถานที่จริง"
}
```
**floor — known**
```json
"2"
```
**map_url — known**
```json
"https://example.invalid/demo20/map/1"
```
**name — known**
```json
{
  "en": "Demo venue Northstar",
  "th": "ศูนย์ทดลอง ดาวเหนือ"
}
```
**operator — known**
```json
{
  "en": "Fictional Northstar operator",
  "th": "ผู้ประกอบการสมมุติ ดาวเหนือ"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/center/demo20_center_01.json)

### โซนบริการ (`zone`)

รหัส `demo20_zone_01`

คำถามตัวอย่าง:

- โซนทดลอง ดาวเหนือ มีที่นั่งกี่ที่
- Demo zone Northstar How many seats are there?
- โซนทดลอง ดาวเหนือ โซนนี้อยู่ตรงไหนและมีที่นั่งกี่ที่

**description — known**
```json
{
  "en": "Synthetic Nintendo Switch zone for Cloud Garden",
  "th": "โซนจำลอง Nintendo Switch สำหรับสวนเมฆ"
}
```
**location — known**
```json
{
  "en": "Test building, floor 2, room 101",
  "th": "อาคารทดสอบ ชั้น 2 ห้อง 101"
}
```
**name — known**
```json
{
  "en": "Demo zone Northstar",
  "th": "โซนทดลอง ดาวเหนือ"
}
```
**room_seats — known**
```json
7
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_01.json)

### รุ่นและสเปกอุปกรณ์ (`equipment_model`)

รหัส `demo20_equipment_model_01`

คำถามตัวอย่าง:

- รุ่นอุปกรณ์ ดาวเหนือ สเปกมีอะไรบ้าง
- Demo model Northstar What are its specifications?
- รุ่นอุปกรณ์ ดาวเหนือ เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง

**device_type — known**
```json
"console"
```
**name — known**
```json
{
  "en": "Demo model Northstar",
  "th": "รุ่นอุปกรณ์ ดาวเหนือ"
}
```
**specifications — known**
```json
[
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
```
**usage — known**
```json
{
  "en": "Fictional equipment for Nintendo Switch; not a PSU specification",
  "th": "เครื่องสมมุติใช้กับ Nintendo Switch; ห้ามอ้างเป็นสเปกศูนย์"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_01.json)

### เครื่องหรือทรัพยากรจริง (`resource`)

รหัส `demo20_resource_01`

คำถามตัวอย่าง:

- เครื่องทดลอง ดาวเหนือ เล่นพร้อมกันได้กี่คน
- Demo station Northstar How many people can play at once?
- เครื่องทดลอง ดาวเหนือ เครื่องยังใช้งานได้ไหมและรองรับกี่คน

**capacity_persons — known**
```json
4
```
**equipment_model_ids — known**
```json
[
  "demo20_equipment_model_01"
]
```
**name — known**
```json
{
  "en": "Demo station Northstar",
  "th": "เครื่องทดลอง ดาวเหนือ"
}
```
**operational_status — known**
```json
"in_service"
```
**physical_pool_key — known**
```json
"demo20_pool_01"
```
**zone_id — known**
```json
"demo20_zone_01"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/resource/demo20_resource_01.json)

### รายการที่เลือกในระบบจอง (`service`)

รหัส `demo20_service_01`

คำถามตัวอย่าง:

- รอบทดลอง ดาวเหนือ หนึ่งรอบเล่นได้กี่นาที
- Demo session Northstar How many minutes does one session last?
- รอบทดลอง ดาวเหนือ เวลาเล่นกับเวลาที่กินช่องจองกี่นาที

**booking_product_key — known**
```json
"DEMO20_BOOKING_01"
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
  "en": "Demo session Northstar",
  "th": "รอบทดลอง ดาวเหนือ"
}
```
**occupancy_minutes — known**
```json
60
```
**platform — known**
```json
"Nintendo Switch"
```
**resource_ids — known**
```json
[
  "demo20_resource_01"
]
```
**session_minutes — known**
```json
60
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_01.json)

### ข้อมูลเกม (`game`)

รหัส `demo20_game_01`

คำถามตัวอย่าง:

- เกมสมมุติ ดาวเหนือ เล่นยังไง
- Fictional game Northstar How do I play it?
- เกมสมมุติ ดาวเหนือ เกมเกี่ยวกับอะไรและเล่นยังไง

**age_rating — known**
```json
{
  "en": "Synthetic DEMO rating 6",
  "th": "เรตอายุสมมุติ DEMO 6"
}
```
**edition — known**
```json
"DEMO fiction revision 1"
```
**genre — known**
```json
{
  "en": "Puzzle",
  "th": "ปริศนา"
}
```
**how_to_play — known**
```json
{
  "en": "Plant together and split seed collecting tasks; follow the demonstration controls",
  "th": "ปลูกต้นไม้ร่วมกันและแบ่งหน้าที่เก็บเมล็ด; ใช้คำสั่งตามชุดควบคุมทดลอง"
}
```
**publisher_url — known**
```json
"https://example.invalid/demo20/fictional-game/1"
```
**summary — known**
```json
{
  "en": "Fictional test game: Plant together and split seed collecting tasks",
  "th": "เกมแต่งขึ้นเพื่อทดสอบ: ปลูกต้นไม้ร่วมกันและแบ่งหน้าที่เก็บเมล็ด"
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
  "en": "Fictional Cloud Garden",
  "th": "เกมสมมุติ สวนเมฆ"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_01.json)

### กลุ่มผู้ใช้ (`audience`)

รหัส `demo20_audience_01`

คำถามตัวอย่าง:

- กลุ่มผู้ใช้ ดาวเหนือ ต้องใช้หลักฐานอะไร
- Demo visitors Northstar What proof is required?
- กลุ่มผู้ใช้ ดาวเหนือ ใครใช้สิทธิ์กลุ่มนี้ได้และต้องแสดงหลักฐานอะไร

**eligibility — known**
```json
{
  "en": "Fictional group 1: demo sessions only",
  "th": "ผู้ใช้สมมุติกลุ่ม 1: ใช้บริการตามรอบทดลอง"
}
```
**name — known**
```json
{
  "en": "Demo visitors Northstar",
  "th": "กลุ่มผู้ใช้ ดาวเหนือ"
}
```
**required_proofs — known**
```json
[
  "DEMO pass Northstar"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/audience/demo20_audience_01.json)

### ติดต่อ (`contact`)

รหัส `demo20_contact_01`

คำถามตัวอย่าง:

- ช่องทางช่วยเหลือ ดาวเหนือ ติดต่อทางไหน
- Demo help channel Northstar How can I contact them?
- ช่องทางช่วยเหลือ ดาวเหนือ ติดต่อที่ไหนและติดต่อได้ช่วงไหน

**channel — known**
```json
"email"
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
  "en": "Fictional support for Watching friends",
  "th": "สอบถามสมมุติเรื่อง ดูเพื่อนเล่น"
}
```
**value — known**
```json
"fiction01@example.invalid"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_01.json)

### ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`)

รหัส `demo20_procedure_01`

คำถามตัวอย่าง:

- ขั้นตอนทดลอง ดาวเหนือ ต้องทำยังไงบ้าง
- Demo procedure Northstar What steps should I follow?
- ขั้นตอนทดลอง ดาวเหนือ มีขั้นตอนอะไรและต้องใช้เอกสารอะไร

**deadline_minutes — known**
```json
10
```
**outcome — known**
```json
{
  "en": "Demo outcome: Watching friends checked",
  "th": "ผลทดสอบ: ตรวจสอบ ดูเพื่อนเล่น เสร็จ"
}
```
**preconditions — known**
```json
[]
```
**required_documents — known**
```json
[
  "DEMO pass Northstar"
]
```
**steps — known**
```json
[
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
```
**topic — known**
```json
"DEMO Watching friends"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_01.json)

### นโยบายและกฎศูนย์ (`policy`)

รหัส `demo20_policy_01`

คำถามตัวอย่าง:

- ข้อกำหนดทดลอง ดาวเหนือ กฎเป็นยังไง
- Demo policy Northstar What are the rules?
- ข้อกำหนดทดลอง ดาวเหนือ อนุญาตไหมและมีข้อยกเว้นอะไร

**conditions_all — known**
```json
[]
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
"allowed"
```
**details — known**
```json
{
  "en": "Fictional rule for Watching friends: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "กติกาสมมุติเรื่องดูเพื่อนเล่น: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
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
"demo20_procedure_01"
```
**subject — known**
```json
{
  "en": "Demo policy Northstar",
  "th": "ข้อกำหนดทดลอง ดาวเหนือ"
}
```
**topic — known**
```json
"DEMO Watching friends"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/policy/demo20_policy_01.json)

### สิ่งอำนวยความสะดวก (`facility`)

รหัส `demo20_facility_01`

คำถามตัวอย่าง:

- พื้นที่พัก ดาวเหนือ อยู่ตรงไหนในร้าน
- Demo amenity Northstar Where in the venue is it?
- พื้นที่พัก ดาวเหนือ อยู่ตรงไหนและคนที่ต้องการความช่วยเหลือเข้าใช้ยังไง

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
  "en": "Spectator corner in demo room 101",
  "th": "มุมดูเพื่อน อยู่ห้องทดสอบ 101"
}
```
**name — known**
```json
{
  "en": "Demo amenity Northstar",
  "th": "พื้นที่พัก ดาวเหนือ"
}
```
**usage_conditions — known**
```json
{
  "en": "Demo sessions only; ask the operator first",
  "th": "ใช้ตามรอบทดลอง; ต้องขอผู้ดูแลก่อน"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/facility/demo20_facility_01.json)

### เกมที่ศูนย์มีให้เล่นจริง (`game_service`)

รหัส `demo20_game_service_01`

คำถามตัวอย่าง:

- การติดตั้งทดลอง ดาวเหนือ มีให้เล่นหรือยัง
- Demo installation Northstar Is this game offered?
- การติดตั้งทดลอง ดาวเหนือ มีให้เล่นไหมและติดตั้งรุ่นไหน

**account_policy_id — known**
```json
"demo20_policy_01"
```
**game_id — known**
```json
"demo20_game_01"
```
**game_version — known**
```json
"DEMO BUILD 1"
```
**installed_resource_ids — known**
```json
[
  "demo20_resource_01"
]
```
**offered — known**
```json
true
```
**service_id — known**
```json
"demo20_service_01"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_service/demo20_game_service_01.json)

### รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`)

รหัส `demo20_game_mode_01`

คำถามตัวอย่าง:

- โหมดทดลอง ดาวเหนือ เล่นพร้อมกันได้สูงสุดกี่คน
- Demo mode Northstar How many people can play together at most?
- โหมดทดลอง ดาวเหนือ ต้องมีขั้นต่ำกี่คนและเล่นได้สูงสุดกี่คน

**game_id — known**
```json
"demo20_game_01"
```
**mode_name — known**
```json
{
  "en": "Demo mode Northstar",
  "th": "โหมดทดลอง ดาวเหนือ"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_mode/demo20_game_mode_01.json)

### วิธีเล่นและปุ่ม (`control_set`)

รหัส `demo20_control_set_01`

คำถามตัวอย่าง:

- ชุดควบคุมทดลอง ดาวเหนือ ปุ่มอะไรบ้าง
- Demo controls Northstar What are the controls?
- ชุดควบคุมทดลอง ดาวเหนือ ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร

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
```
**game_id — known**
```json
"demo20_game_01"
```
**game_version — known**
```json
"DEMO BUILD 1"
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
"DEMO_LAYOUT_1"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_01.json)

### ราคาต่อบริการ (`rate`)

รหัส `demo20_rate_01`

คำถามตัวอย่าง:

- อัตราทดลอง ดาวเหนือ ราคาเท่าไหร่
- Demo tariff Northstar How much does it cost?
- อัตราทดลอง ดาวเหนือ ราคาเท่าไหร่และได้กี่นาที

**amount_minor — known**
```json
4500
```
**audience_id — known**
```json
"demo20_audience_01"
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
60
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
"demo20_service_01"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rate/demo20_rate_01.json)

### ราคาเหมาโซน/ห้อง (`rental_package`)

รหัส `demo20_rental_package_01`

คำถามตัวอย่าง:

- แพ็กเกจทดลอง ดาวเหนือ เหมาเท่าไหร่
- Demo package Northstar How much is the rental?
- แพ็กเกจทดลอง ดาวเหนือ ราคาเหมาเท่าไหร่และรวมอุปกรณ์อะไร

**amount_minor — known**
```json
14750
```
**audience_id — known**
```json
"demo20_audience_01"
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
  "en": "Fictional Northstar station and Nintendo Switch inputs",
  "th": "เครื่องสมมุติ ดาวเหนือ พร้อมอุปกรณ์ Nintendo Switch"
}
```
**name — known**
```json
{
  "en": "Demo package Northstar",
  "th": "แพ็กเกจทดลอง ดาวเหนือ"
}
```
**period_label — known**
```json
"full_day"
```
**room_seats — known**
```json
7
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
  "demo20_zone_01"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rental_package/demo20_rental_package_01.json)

### ตารางบริการ (`schedule`)

รหัส `demo20_schedule_01`

คำถามตัวอย่าง:

- ตารางทดลอง ดาวเหนือ จองช่วงไหนได้บ้าง
- Demo timetable Northstar What are the booking hours?
- ตารางทดลอง ดาวเหนือ เปิดช่วงไหนและพักบำรุงรักษาตอนไหน

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
  "en": "Synthetic Northstar schedule with maintenance",
  "th": "ตารางสมมุติ ดาวเหนือ มีพักบำรุงรักษา"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```
**weekday — known**
```json
1
```
**zone_ids — known**
```json
[
  "demo20_zone_01"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_01.json)

### วันปิด/ข้อยกเว้น (`closure`)

รหัส `demo20_closure_01`

คำถามตัวอย่าง:

- ประกาศวันทดลอง ดาวเหนือ วันนั้นปิดไหม
- Demo date notice Northstar Is it closed on that date?
- ประกาศวันทดลอง ดาวเหนือ วันนั้นเปิดปิดยังไงและเพราะอะไร

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
"2026-12-01"
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
  "en": "Synthetic Northstar date notice: modified_hours",
  "th": "ประกาศสมมุติ ดาวเหนือ: modified_hours"
}
```
**resolution_policy_id — known**
```json
"demo20_policy_01"
```
**state — known**
```json
"modified_hours"
```
**zone_ids — known**
```json
[
  "demo20_zone_01"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/closure/demo20_closure_01.json)

### รายการแข่งขันและฉบับกติกา (`competition`)

รหัส `demo20_competition_01`

คำถามตัวอย่าง:

- รายการฝึก ดาวเหนือ ใช้กติกาฉบับไหน
- Demo event Northstar Which rulebook release applies?
- รายการฝึก ดาวเหนือ ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่

**competition_dates — known**
```json
[
  "2026-12-01"
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
  "en": "Demo event Northstar",
  "th": "รายการฝึก ดาวเหนือ"
}
```
**game_id — known**
```json
"demo20_game_01"
```
**rulebook_release — known**
```json
"DEMO20_REV_1"
```
**supersedes_id — not_applicable**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_01.json)

### ข้อกติกาการแข่งขัน (`competition_rule`)

รหัส `demo20_competition_rule_01`

คำถามตัวอย่าง:

- ข้อการแข่งขันทดลอง ดาวเหนือ ข้อนี้กำหนดอะไร
- Demo rule Northstar What does this rule require?
- ข้อการแข่งขันทดลอง ดาวเหนือ กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม

**competition_id — known**
```json
"demo20_competition_01"
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
"eligibility_registration"
```
**heading — known**
```json
{
  "en": "Demo rule Northstar",
  "th": "ข้อการแข่งขันทดลอง ดาวเหนือ"
}
```
**section_number — known**
```json
"2.1"
```
**text — known**
```json
{
  "en": "Fictional clause 1: for Watching friends, follow decision allowed; exception requires written demo operator approval; not actual rules",
  "th": "ข้อสมมุติ 1: ดูเพื่อนเล่น ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_01.json)

### ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`)

รหัส `demo20_news_01`

คำถามตัวอย่าง:

- ข่าวทดลอง ดาวเหนือ ประกาศว่าอะไร
- Demo bulletin Northstar What does the announcement say?
- ข่าวทดลอง ดาวเหนือ ประกาศอะไรและกิจกรรมเริ่มจบเมื่อไหร่

**audience_ids — known**
```json
[
  "demo20_audience_01"
]
```
**body — known**
```json
{
  "en": "Synthetic bulletin: Cloud Garden activity for 1–4 people; no actual payment",
  "th": "ข่าวสมมุติ: กิจกรรมสวนเมฆ สำหรับกลุ่ม 1–4 คน; ไม่มีรับเงินจริง"
}
```
**contact_id — known**
```json
"demo20_contact_01"
```
**event_end — known**
```json
"2026-12-01T12:00:00+07:00"
```
**event_start — known**
```json
"2026-12-01T10:00:00+07:00"
```
**registration_url — known**
```json
"https://example.invalid/demo20/register/1"
```
**title — known**
```json
{
  "en": "Demo bulletin Northstar",
  "th": "ข่าวทดลอง ดาวเหนือ"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/news/demo20_news_01.json)

### บุคลากร/ทีมที่เปิดเผยได้ (`person`)

รหัส `demo20_person_01`

คำถามตัวอย่าง:

- ผู้ดูแลสมมุติ ดาวเหนือ รับผิดชอบอะไร
- Fictional host Northstar What is their role?
- ผู้ดูแลสมมุติ ดาวเหนือ รับผิดชอบเรื่องอะไรและติดต่อทางไหน

**display_name — known**
```json
{
  "en": "Fictional host Northstar",
  "th": "ผู้ดูแลสมมุติ ดาวเหนือ"
}
```
**public_contact_id — known**
```json
"demo20_contact_01"
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
  "en": "Fictional host for Watching friends",
  "th": "ผู้ดูแลสมมุติเรื่อง ดูเพื่อนเล่น"
}
```
**team — known**
```json
{
  "en": "Demo Northstar team",
  "th": "ทีมทดสอบ ดาวเหนือ"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/person/demo20_person_01.json)

### คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`)

รหัส `demo20_faq_01`

คำถามตัวอย่าง:

- คำถามตัวอย่าง ดาวเหนือ คำตอบคืออะไร
- Demo enquiry Northstar What is the answer?
- คำถามตัวอย่าง ดาวเหนือ คำตอบคืออะไรและใช้กับกรณีไหน

**answer — known**
```json
{
  "en": "Example answer: Fictional rule for Watching friends: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องดูเพื่อนเล่น: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
}
```
**question — known**
```json
{
  "en": "Demo enquiry Northstar",
  "th": "คำถามตัวอย่าง ดาวเหนือ"
}
```
**related_ids — known**
```json
[
  "demo20_policy_01",
  "demo20_procedure_01"
]
```
**scope_note — known**
```json
{
  "en": "Only applies to fictional Northstar scenario",
  "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ดาวเหนือ"
}
```
**topic — known**
```json
"DEMO Watching friends"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_01.json)

### การเชื่อมสถานะสด (`live_binding`)

รหัส `demo20_live_binding_01`

คำถามตัวอย่าง:

- ตัวเชื่อมทดลอง ดาวเหนือ จับคู่สถานะยังไง
- Demo binding Northstar How are statuses mapped?
- ตัวเชื่อมทดลอง ดาวเหนือ จับคู่สถานะแบบไหนและเก็บข้อมูลนานเท่าไหร่

**external_resource_key — known**
```json
"DEMO20_EXTERNAL_1"
```
**freshness_policy — known**
```json
{
  "en": "Synthetic TTL 20 seconds; no API call or live status claim",
  "th": "ค่าจำลอง TTL 20 วินาที; ไม่เรียก API และไม่ยืนยันสถานะสด"
}
```
**physical_pool_key — known**
```json
"demo20_pool_01"
```
**provider — known**
```json
"wordpress_booking"
```
**service_id — known**
```json
"demo20_service_01"
```
**status_mapping — known**
```json
[
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
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/live_binding/demo20_live_binding_01.json)

