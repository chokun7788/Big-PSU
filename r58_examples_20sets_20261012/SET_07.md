# ชุด 07 — ตะวันอ่อน / Gentle Sun

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

เกม สถานที่ ราคา กฎ บุคคล และสถานะทั้งหมดในชุดใหม่นี้แต่งขึ้นเพื่อทดสอบ ไม่ได้เป็นข้อมูล PSU หรือเกมที่มีจำหน่ายจริง คำแปลยังไม่ผ่านมนุษย์

แพลตฟอร์มตัวอย่าง: PC • จำนวนผู้เล่น 5–10 • เวลาเล่น 120 นาที / กินช่องจอง 120 นาที

## ข้อมูลครบ 24 หมวด

### ข้อมูลศูนย์ (`center`)

รหัส `demo20_center_07`

คำถามตัวอย่าง:

- ศูนย์ทดลอง ตะวันอ่อน อยู่ตรงไหน
- Demo venue Gentle Sun Where is it located?
- ศูนย์ทดลอง ตะวันอ่อน อยู่ตึกอะไร ชั้นไหน

**address — known**
```json
{
  "en": "Fictional address 49, Example Road, Test District",
  "th": "เลขที่สมมุติ 49 ถนนตัวอย่าง แขวงทดลอง"
}
```
**building — known**
```json
"DEMO Tower C"
```
**description — known**
```json
{
  "en": "Synthetic scenario 7: Meteor Team, not a real venue",
  "th": "สถานการณ์ทดลอง 7: ทีมดาวตก ไม่ใช่สถานที่จริง"
}
```
**floor — known**
```json
"3"
```
**map_url — known**
```json
"https://example.invalid/demo20/map/7"
```
**name — known**
```json
{
  "en": "Demo venue Gentle Sun",
  "th": "ศูนย์ทดลอง ตะวันอ่อน"
}
```
**operator — known**
```json
{
  "en": "Fictional Gentle Sun operator",
  "th": "ผู้ประกอบการสมมุติ ตะวันอ่อน"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/center/demo20_center_07.json)

### โซนบริการ (`zone`)

รหัส `demo20_zone_07`

คำถามตัวอย่าง:

- โซนทดลอง ตะวันอ่อน มีที่นั่งกี่ที่
- Demo zone Gentle Sun How many seats are there?
- โซนทดลอง ตะวันอ่อน โซนนี้อยู่ตรงไหนและมีที่นั่งกี่ที่

**description — known**
```json
{
  "en": "Synthetic PC zone for Meteor Team",
  "th": "โซนจำลอง PC สำหรับทีมดาวตก"
}
```
**location — known**
```json
{
  "en": "Test building, floor 3, room 107",
  "th": "อาคารทดสอบ ชั้น 3 ห้อง 107"
}
```
**name — known**
```json
{
  "en": "Demo zone Gentle Sun",
  "th": "โซนทดลอง ตะวันอ่อน"
}
```
**room_seats — known**
```json
13
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_07.json)

### รุ่นและสเปกอุปกรณ์ (`equipment_model`)

รหัส `demo20_equipment_model_07`

คำถามตัวอย่าง:

- รุ่นอุปกรณ์ ตะวันอ่อน สเปกมีอะไรบ้าง
- Demo model Gentle Sun What are its specifications?
- รุ่นอุปกรณ์ ตะวันอ่อน เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง

**device_type — known**
```json
"pc"
```
**name — known**
```json
{
  "en": "Demo model Gentle Sun",
  "th": "รุ่นอุปกรณ์ ตะวันอ่อน"
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
    "value": "keyboard_mouse"
  }
]
```
**usage — known**
```json
{
  "en": "Fictional equipment for PC; not a PSU specification",
  "th": "เครื่องสมมุติใช้กับ PC; ห้ามอ้างเป็นสเปกศูนย์"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_07.json)

### เครื่องหรือทรัพยากรจริง (`resource`)

รหัส `demo20_resource_07`

คำถามตัวอย่าง:

- เครื่องทดลอง ตะวันอ่อน เล่นพร้อมกันได้กี่คน
- Demo station Gentle Sun How many people can play at once?
- เครื่องทดลอง ตะวันอ่อน เครื่องยังใช้งานได้ไหมและรองรับกี่คน

**capacity_persons — known**
```json
10
```
**equipment_model_ids — known**
```json
[
  "demo20_equipment_model_07"
]
```
**name — known**
```json
{
  "en": "Demo station Gentle Sun",
  "th": "เครื่องทดลอง ตะวันอ่อน"
}
```
**operational_status — known**
```json
"in_service"
```
**physical_pool_key — known**
```json
"demo20_pool_07"
```
**zone_id — known**
```json
"demo20_zone_07"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/resource/demo20_resource_07.json)

### รายการที่เลือกในระบบจอง (`service`)

รหัส `demo20_service_07`

คำถามตัวอย่าง:

- รอบทดลอง ตะวันอ่อน หนึ่งรอบเล่นได้กี่นาที
- Demo session Gentle Sun How many minutes does one session last?
- รอบทดลอง ตะวันอ่อน เวลาเล่นกับเวลาที่กินช่องจองกี่นาที

**booking_product_key — known**
```json
"DEMO20_BOOKING_07"
```
**capacity_max — known**
```json
10
```
**capacity_min — known**
```json
5
```
**name — known**
```json
{
  "en": "Demo session Gentle Sun",
  "th": "รอบทดลอง ตะวันอ่อน"
}
```
**occupancy_minutes — known**
```json
120
```
**platform — known**
```json
"PC"
```
**resource_ids — known**
```json
[
  "demo20_resource_07"
]
```
**session_minutes — known**
```json
120
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_07.json)

### ข้อมูลเกม (`game`)

รหัส `demo20_game_07`

คำถามตัวอย่าง:

- เกมสมมุติ ตะวันอ่อน เล่นยังไง
- Fictional game Gentle Sun How do I play it?
- เกมสมมุติ ตะวันอ่อน เกมเกี่ยวกับอะไรและเล่นยังไง

**age_rating — known**
```json
{
  "en": "Synthetic DEMO rating 12",
  "th": "เรตอายุสมมุติ DEMO 12"
}
```
**edition — known**
```json
"DEMO fiction revision 7"
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
  "en": "Two teams compete to collect energy points; follow the demonstration controls",
  "th": "ทีมสองฝั่งแข่งขันเก็บจุดพลังงาน; ใช้คำสั่งตามชุดควบคุมทดลอง"
}
```
**publisher_url — known**
```json
"https://example.invalid/demo20/fictional-game/7"
```
**summary — known**
```json
{
  "en": "Fictional test game: Two teams compete to collect energy points",
  "th": "เกมแต่งขึ้นเพื่อทดสอบ: ทีมสองฝั่งแข่งขันเก็บจุดพลังงาน"
}
```
**supported_platforms — known**
```json
[
  "PC"
]
```
**title — known**
```json
{
  "en": "Fictional Meteor Team",
  "th": "เกมสมมุติ ทีมดาวตก"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_07.json)

### กลุ่มผู้ใช้ (`audience`)

รหัส `demo20_audience_07`

คำถามตัวอย่าง:

- กลุ่มผู้ใช้ ตะวันอ่อน ต้องใช้หลักฐานอะไร
- Demo visitors Gentle Sun What proof is required?
- กลุ่มผู้ใช้ ตะวันอ่อน ใครใช้สิทธิ์กลุ่มนี้ได้และต้องแสดงหลักฐานอะไร

**eligibility — known**
```json
{
  "en": "Fictional group 7: demo sessions only",
  "th": "ผู้ใช้สมมุติกลุ่ม 7: ใช้บริการตามรอบทดลอง"
}
```
**name — known**
```json
{
  "en": "Demo visitors Gentle Sun",
  "th": "กลุ่มผู้ใช้ ตะวันอ่อน"
}
```
**required_proofs — known**
```json
[
  "DEMO pass Gentle Sun",
  "DEMO group list 7"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/audience/demo20_audience_07.json)

### ติดต่อ (`contact`)

รหัส `demo20_contact_07`

คำถามตัวอย่าง:

- ช่องทางช่วยเหลือ ตะวันอ่อน ติดต่อทางไหน
- Demo help channel Gentle Sun How can I contact them?
- ช่องทางช่วยเหลือ ตะวันอ่อน ติดต่อที่ไหนและติดต่อได้ช่วงไหน

**channel — known**
```json
"facebook"
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
  "en": "Fictional support for Team roster",
  "th": "สอบถามสมมุติเรื่อง จำนวนสมาชิกทีม"
}
```
**value — known**
```json
"https://example.invalid/demo20/social/7"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_07.json)

### ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`)

รหัส `demo20_procedure_07`

คำถามตัวอย่าง:

- ขั้นตอนทดลอง ตะวันอ่อน ต้องทำยังไงบ้าง
- Demo procedure Gentle Sun What steps should I follow?
- ขั้นตอนทดลอง ตะวันอ่อน มีขั้นตอนอะไรและต้องใช้เอกสารอะไร

**deadline_minutes — known**
```json
15
```
**outcome — known**
```json
{
  "en": "Demo outcome: Team roster checked",
  "th": "ผลทดสอบ: ตรวจสอบ จำนวนสมาชิกทีม เสร็จ"
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
  "DEMO pass Gentle Sun",
  "DEMO group list 7"
]
```
**steps — known**
```json
[
  {
    "contact_id": null,
    "instruction": {
      "en": "Select the fictional Gentle Sun service",
      "th": "เลือกบริการสมมุติ ตะวันอ่อน"
    },
    "order": 1
  },
  {
    "contact_id": "demo20_contact_07",
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
"DEMO Team roster"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_07.json)

### นโยบายและกฎศูนย์ (`policy`)

รหัส `demo20_policy_07`

คำถามตัวอย่าง:

- ข้อกำหนดทดลอง ตะวันอ่อน กฎเป็นยังไง
- Demo policy Gentle Sun What are the rules?
- ข้อกำหนดทดลอง ตะวันอ่อน อนุญาตไหมและมีข้อยกเว้นอะไร

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
  "en": "Fictional rule for Team roster: required; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "กติกาสมมุติเรื่องจำนวนสมาชิกทีม: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
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
"demo20_procedure_07"
```
**subject — known**
```json
{
  "en": "Demo policy Gentle Sun",
  "th": "ข้อกำหนดทดลอง ตะวันอ่อน"
}
```
**topic — known**
```json
"DEMO Team roster"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/policy/demo20_policy_07.json)

### สิ่งอำนวยความสะดวก (`facility`)

รหัส `demo20_facility_07`

คำถามตัวอย่าง:

- พื้นที่พัก ตะวันอ่อน อยู่ตรงไหนในร้าน
- Demo amenity Gentle Sun Where in the venue is it?
- พื้นที่พัก ตะวันอ่อน อยู่ตรงไหนและคนที่ต้องการความช่วยเหลือเข้าใช้ยังไง

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
  "en": "Team table in demo room 107",
  "th": "โต๊ะรวมทีม อยู่ห้องทดสอบ 107"
}
```
**name — known**
```json
{
  "en": "Demo amenity Gentle Sun",
  "th": "พื้นที่พัก ตะวันอ่อน"
}
```
**usage_conditions — known**
```json
{
  "en": "Demo sessions only; ask the operator first",
  "th": "ใช้ตามรอบทดลอง; ต้องขอผู้ดูแลก่อน"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/facility/demo20_facility_07.json)

### เกมที่ศูนย์มีให้เล่นจริง (`game_service`)

รหัส `demo20_game_service_07`

คำถามตัวอย่าง:

- การติดตั้งทดลอง ตะวันอ่อน มีให้เล่นหรือยัง
- Demo installation Gentle Sun Is this game offered?
- การติดตั้งทดลอง ตะวันอ่อน มีให้เล่นไหมและติดตั้งรุ่นไหน

**account_policy_id — known**
```json
"demo20_policy_07"
```
**game_id — known**
```json
"demo20_game_07"
```
**game_version — known**
```json
"DEMO BUILD 7"
```
**installed_resource_ids — known**
```json
[
  "demo20_resource_07"
]
```
**offered — known**
```json
true
```
**service_id — known**
```json
"demo20_service_07"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_service/demo20_game_service_07.json)

### รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`)

รหัส `demo20_game_mode_07`

คำถามตัวอย่าง:

- โหมดทดลอง ตะวันอ่อน เล่นพร้อมกันได้สูงสุดกี่คน
- Demo mode Gentle Sun How many people can play together at most?
- โหมดทดลอง ตะวันอ่อน ต้องมีขั้นต่ำกี่คนและเล่นได้สูงสุดกี่คน

**game_id — known**
```json
"demo20_game_07"
```
**mode_name — known**
```json
{
  "en": "Demo mode Gentle Sun",
  "th": "โหมดทดลอง ตะวันอ่อน"
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
"PC"
```
**players_max — known**
```json
10
```
**players_min — known**
```json
5
```
**studio_supported — known**
```json
true
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_mode/demo20_game_mode_07.json)

### วิธีเล่นและปุ่ม (`control_set`)

รหัส `demo20_control_set_07`

คำถามตัวอย่าง:

- ชุดควบคุมทดลอง ตะวันอ่อน ปุ่มอะไรบ้าง
- Demo controls Gentle Sun What are the controls?
- ชุดควบคุมทดลอง ตะวันอ่อน ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร

**bindings — known**
```json
[
  {
    "action": {
      "en": "Confirm",
      "th": "ยืนยัน"
    },
    "buttons": [
      "DEMO_keyboard_mouse_1"
    ],
    "context": {
      "en": "Fictional input for Meteor Team",
      "th": "คำสั่งสมมุติของ ทีมดาวตก"
    },
    "gesture": "press"
  },
  {
    "action": {
      "en": "Move",
      "th": "เคลื่อนที่"
    },
    "buttons": [
      "DEMO_keyboard_mouse_2"
    ],
    "context": {
      "en": "Fictional input for Meteor Team",
      "th": "คำสั่งสมมุติของ ทีมดาวตก"
    },
    "gesture": "press"
  }
]
```
**game_id — known**
```json
"demo20_game_07"
```
**game_version — known**
```json
"DEMO BUILD 7"
```
**input_device — known**
```json
"keyboard_mouse"
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
"PC"
```
**preset — known**
```json
"DEMO_LAYOUT_7"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_07.json)

### ราคาต่อบริการ (`rate`)

รหัส `demo20_rate_07`

คำถามตัวอย่าง:

- อัตราทดลอง ตะวันอ่อน ราคาเท่าไหร่
- Demo tariff Gentle Sun How much does it cost?
- อัตราทดลอง ตะวันอ่อน ราคาเท่าไหร่และได้กี่นาที

**amount_minor — known**
```json
50000
```
**audience_id — known**
```json
"demo20_audience_07"
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
10
```
**persons_min — known**
```json
5
```
**service_id — known**
```json
"demo20_service_07"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rate/demo20_rate_07.json)

### ราคาเหมาโซน/ห้อง (`rental_package`)

รหัส `demo20_rental_package_07`

คำถามตัวอย่าง:

- แพ็กเกจทดลอง ตะวันอ่อน เหมาเท่าไหร่
- Demo package Gentle Sun How much is the rental?
- แพ็กเกจทดลอง ตะวันอ่อน ราคาเหมาเท่าไหร่และรวมอุปกรณ์อะไร

**amount_minor — known**
```json
151250
```
**audience_id — known**
```json
"demo20_audience_07"
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
  "en": "Fictional Gentle Sun station and PC inputs",
  "th": "เครื่องสมมุติ ตะวันอ่อน พร้อมอุปกรณ์ PC"
}
```
**name — known**
```json
{
  "en": "Demo package Gentle Sun",
  "th": "แพ็กเกจทดลอง ตะวันอ่อน"
}
```
**period_label — known**
```json
"full_day"
```
**room_seats — known**
```json
13
```
**terms — known**
```json
{
  "en": "Synthetic package excludes extensions; 5–10 people per session",
  "th": "แพ็กเกจสมมุติไม่รวมค่าต่อเวลา; รอบละ 5–10 คน"
}
```
**zone_ids — known**
```json
[
  "demo20_zone_07"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rental_package/demo20_rental_package_07.json)

### ตารางบริการ (`schedule`)

รหัส `demo20_schedule_07`

คำถามตัวอย่าง:

- ตารางทดลอง ตะวันอ่อน จองช่วงไหนได้บ้าง
- Demo timetable Gentle Sun What are the booking hours?
- ตารางทดลอง ตะวันอ่อน เปิดช่วงไหนและพักบำรุงรักษาตอนไหน

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
  "en": "Synthetic Gentle Sun schedule with maintenance",
  "th": "ตารางสมมุติ ตะวันอ่อน มีพักบำรุงรักษา"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```
**weekday — known**
```json
0
```
**zone_ids — known**
```json
[
  "demo20_zone_07"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_07.json)

### วันปิด/ข้อยกเว้น (`closure`)

รหัส `demo20_closure_07`

คำถามตัวอย่าง:

- ประกาศวันทดลอง ตะวันอ่อน วันนั้นปิดไหม
- Demo date notice Gentle Sun Is it closed on that date?
- ประกาศวันทดลอง ตะวันอ่อน วันนั้นเปิดปิดยังไงและเพราะอะไร

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
"2026-12-07"
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
  "en": "Synthetic Gentle Sun date notice: modified_hours",
  "th": "ประกาศสมมุติ ตะวันอ่อน: modified_hours"
}
```
**resolution_policy_id — known**
```json
"demo20_policy_07"
```
**state — known**
```json
"modified_hours"
```
**zone_ids — known**
```json
[
  "demo20_zone_07"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/closure/demo20_closure_07.json)

### รายการแข่งขันและฉบับกติกา (`competition`)

รหัส `demo20_competition_07`

คำถามตัวอย่าง:

- รายการฝึก ตะวันอ่อน ใช้กติกาฉบับไหน
- Demo event Gentle Sun Which rulebook release applies?
- รายการฝึก ตะวันอ่อน ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่

**competition_dates — known**
```json
[
  "2026-12-07"
]
```
**coverage — known**
```json
"complete"
```
**division — known**
```json
{
  "en": "Practice group 5–10 players",
  "th": "กลุ่มฝึก 5–10 คน"
}
```
**event_name — known**
```json
{
  "en": "Demo event Gentle Sun",
  "th": "รายการฝึก ตะวันอ่อน"
}
```
**game_id — known**
```json
"demo20_game_07"
```
**rulebook_release — known**
```json
"DEMO20_REV_7"
```
**supersedes_id — not_applicable**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_07.json)

### ข้อกติกาการแข่งขัน (`competition_rule`)

รหัส `demo20_competition_rule_07`

คำถามตัวอย่าง:

- ข้อการแข่งขันทดลอง ตะวันอ่อน ข้อนี้กำหนดอะไร
- Demo rule Gentle Sun What does this rule require?
- ข้อการแข่งขันทดลอง ตะวันอ่อน กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม

**competition_id — known**
```json
"demo20_competition_07"
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
  "en": "Demo rule Gentle Sun",
  "th": "ข้อการแข่งขันทดลอง ตะวันอ่อน"
}
```
**section_number — known**
```json
"3.7"
```
**text — known**
```json
{
  "en": "Fictional clause 7: for Team roster, follow decision required; exception requires written demo operator approval; not actual rules",
  "th": "ข้อสมมุติ 7: จำนวนสมาชิกทีม ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_07.json)

### ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`)

รหัส `demo20_news_07`

คำถามตัวอย่าง:

- ข่าวทดลอง ตะวันอ่อน ประกาศว่าอะไร
- Demo bulletin Gentle Sun What does the announcement say?
- ข่าวทดลอง ตะวันอ่อน ประกาศอะไรและกิจกรรมเริ่มจบเมื่อไหร่

**audience_ids — known**
```json
[
  "demo20_audience_07"
]
```
**body — known**
```json
{
  "en": "Synthetic bulletin: Meteor Team activity for 5–10 people; no actual payment",
  "th": "ข่าวสมมุติ: กิจกรรมทีมดาวตก สำหรับกลุ่ม 5–10 คน; ไม่มีรับเงินจริง"
}
```
**contact_id — known**
```json
"demo20_contact_07"
```
**event_end — known**
```json
"2026-12-07T12:00:00+07:00"
```
**event_start — known**
```json
"2026-12-07T10:00:00+07:00"
```
**registration_url — known**
```json
"https://example.invalid/demo20/register/7"
```
**title — known**
```json
{
  "en": "Demo bulletin Gentle Sun",
  "th": "ข่าวทดลอง ตะวันอ่อน"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/news/demo20_news_07.json)

### บุคลากร/ทีมที่เปิดเผยได้ (`person`)

รหัส `demo20_person_07`

คำถามตัวอย่าง:

- ผู้ดูแลสมมุติ ตะวันอ่อน รับผิดชอบอะไร
- Fictional host Gentle Sun What is their role?
- ผู้ดูแลสมมุติ ตะวันอ่อน รับผิดชอบเรื่องอะไรและติดต่อทางไหน

**display_name — known**
```json
{
  "en": "Fictional host Gentle Sun",
  "th": "ผู้ดูแลสมมุติ ตะวันอ่อน"
}
```
**public_contact_id — known**
```json
"demo20_contact_07"
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
  "en": "Fictional host for Team roster",
  "th": "ผู้ดูแลสมมุติเรื่อง จำนวนสมาชิกทีม"
}
```
**team — known**
```json
{
  "en": "Demo Gentle Sun team",
  "th": "ทีมทดสอบ ตะวันอ่อน"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/person/demo20_person_07.json)

### คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`)

รหัส `demo20_faq_07`

คำถามตัวอย่าง:

- คำถามตัวอย่าง ตะวันอ่อน คำตอบคืออะไร
- Demo enquiry Gentle Sun What is the answer?
- คำถามตัวอย่าง ตะวันอ่อน คำตอบคืออะไรและใช้กับกรณีไหน

**answer — known**
```json
{
  "en": "Example answer: Fictional rule for Team roster: required; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องจำนวนสมาชิกทีม: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
}
```
**question — known**
```json
{
  "en": "Demo enquiry Gentle Sun",
  "th": "คำถามตัวอย่าง ตะวันอ่อน"
}
```
**related_ids — known**
```json
[
  "demo20_policy_07",
  "demo20_procedure_07"
]
```
**scope_note — known**
```json
{
  "en": "Only applies to fictional Gentle Sun scenario",
  "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ตะวันอ่อน"
}
```
**topic — known**
```json
"DEMO Team roster"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_07.json)

### การเชื่อมสถานะสด (`live_binding`)

รหัส `demo20_live_binding_07`

คำถามตัวอย่าง:

- ตัวเชื่อมทดลอง ตะวันอ่อน จับคู่สถานะยังไง
- Demo binding Gentle Sun How are statuses mapped?
- ตัวเชื่อมทดลอง ตะวันอ่อน จับคู่สถานะแบบไหนและเก็บข้อมูลนานเท่าไหร่

**external_resource_key — known**
```json
"DEMO20_EXTERNAL_7"
```
**freshness_policy — known**
```json
{
  "en": "Synthetic TTL 50 seconds; no API call or live status claim",
  "th": "ค่าจำลอง TTL 50 วินาที; ไม่เรียก API และไม่ยืนยันสถานะสด"
}
```
**physical_pool_key — known**
```json
"demo20_pool_07"
```
**provider — known**
```json
"wordpress_booking"
```
**service_id — known**
```json
"demo20_service_07"
```
**status_mapping — known**
```json
[
  {
    "normalized": "free",
    "raw": "DEMO_EMPTY_7"
  },
  {
    "normalized": "occupied",
    "raw": "DEMO_BUSY_7"
  },
  {
    "normalized": "unknown",
    "raw": "DEMO_UNKNOWN_7"
  }
]
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/live_binding/demo20_live_binding_07.json)

