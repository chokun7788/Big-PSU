# ชุด 02 — ดาวเหนือ พลัส / Northstar Plus

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

เกม สถานที่ ราคา กฎ บุคคล และสถานะทั้งหมดในชุดใหม่นี้แต่งขึ้นเพื่อทดสอบ ไม่ได้เป็นข้อมูล PSU หรือเกมที่มีจำหน่ายจริง คำแปลยังไม่ผ่านมนุษย์

แพลตฟอร์มตัวอย่าง: PS5 • จำนวนผู้เล่น 2–2 • เวลาเล่น 90 นาที / กินช่องจอง 90 นาที

## ข้อมูลครบ 24 หมวด

### ข้อมูลศูนย์ (`center`)

รหัส `demo20_center_02`

คำถามตัวอย่าง:

- ศูนย์ทดลอง ดาวเหนือ พลัส อยู่ตรงไหน
- Demo venue Northstar Plus Where is it located?
- ศูนย์ทดลอง ดาวเหนือ พลัส อยู่ตึกอะไร ชั้นไหน

**address — known**
```json
{
  "en": "Fictional address 14, Example Road, Test District",
  "th": "เลขที่สมมุติ 14 ถนนตัวอย่าง แขวงทดลอง"
}
```
**building — known**
```json
"DEMO Tower C"
```
**description — known**
```json
{
  "en": "Synthetic scenario 2: Orbit Duo, not a real venue",
  "th": "สถานการณ์ทดลอง 2: วงโคจรคู่ ไม่ใช่สถานที่จริง"
}
```
**floor — known**
```json
"3"
```
**map_url — known**
```json
"https://example.invalid/demo20/map/2"
```
**name — known**
```json
{
  "en": "Demo venue Northstar Plus",
  "th": "ศูนย์ทดลอง ดาวเหนือ พลัส"
}
```
**operator — known**
```json
{
  "en": "Fictional Northstar Plus operator",
  "th": "ผู้ประกอบการสมมุติ ดาวเหนือ พลัส"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/center/demo20_center_02.json)

### โซนบริการ (`zone`)

รหัส `demo20_zone_02`

คำถามตัวอย่าง:

- โซนทดลอง ดาวเหนือ พลัส มีที่นั่งกี่ที่
- Demo zone Northstar Plus How many seats are there?
- โซนทดลอง ดาวเหนือ พลัส โซนนี้อยู่ตรงไหนและมีที่นั่งกี่ที่

**description — known**
```json
{
  "en": "Synthetic PS5 zone for Orbit Duo",
  "th": "โซนจำลอง PS5 สำหรับวงโคจรคู่"
}
```
**location — known**
```json
{
  "en": "Test building, floor 3, room 102",
  "th": "อาคารทดสอบ ชั้น 3 ห้อง 102"
}
```
**name — known**
```json
{
  "en": "Demo zone Northstar Plus",
  "th": "โซนทดลอง ดาวเหนือ พลัส"
}
```
**room_seats — known**
```json
6
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_02.json)

### รุ่นและสเปกอุปกรณ์ (`equipment_model`)

รหัส `demo20_equipment_model_02`

คำถามตัวอย่าง:

- รุ่นอุปกรณ์ ดาวเหนือ พลัส สเปกมีอะไรบ้าง
- Demo model Northstar Plus What are its specifications?
- รุ่นอุปกรณ์ ดาวเหนือ พลัส เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง

**device_type — known**
```json
"console"
```
**name — known**
```json
{
  "en": "Demo model Northstar Plus",
  "th": "รุ่นอุปกรณ์ ดาวเหนือ พลัส"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_02.json)

### เครื่องหรือทรัพยากรจริง (`resource`)

รหัส `demo20_resource_02`

คำถามตัวอย่าง:

- เครื่องทดลอง ดาวเหนือ พลัส เล่นพร้อมกันได้กี่คน
- Demo station Northstar Plus How many people can play at once?
- เครื่องทดลอง ดาวเหนือ พลัส เครื่องยังใช้งานได้ไหมและรองรับกี่คน

**capacity_persons — known**
```json
2
```
**equipment_model_ids — known**
```json
[
  "demo20_equipment_model_02"
]
```
**name — known**
```json
{
  "en": "Demo station Northstar Plus",
  "th": "เครื่องทดลอง ดาวเหนือ พลัส"
}
```
**operational_status — known**
```json
"in_service"
```
**physical_pool_key — known**
```json
"demo20_pool_02"
```
**zone_id — known**
```json
"demo20_zone_02"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/resource/demo20_resource_02.json)

### รายการที่เลือกในระบบจอง (`service`)

รหัส `demo20_service_02`

คำถามตัวอย่าง:

- รอบทดลอง ดาวเหนือ พลัส หนึ่งรอบเล่นได้กี่นาที
- Demo session Northstar Plus How many minutes does one session last?
- รอบทดลอง ดาวเหนือ พลัส เวลาเล่นกับเวลาที่กินช่องจองกี่นาที

**booking_product_key — known**
```json
"DEMO20_BOOKING_02"
```
**capacity_max — known**
```json
2
```
**capacity_min — known**
```json
2
```
**name — known**
```json
{
  "en": "Demo session Northstar Plus",
  "th": "รอบทดลอง ดาวเหนือ พลัส"
}
```
**occupancy_minutes — known**
```json
90
```
**platform — known**
```json
"PS5"
```
**resource_ids — known**
```json
[
  "demo20_resource_02"
]
```
**session_minutes — known**
```json
90
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_02.json)

### ข้อมูลเกม (`game`)

รหัส `demo20_game_02`

คำถามตัวอย่าง:

- เกมสมมุติ ดาวเหนือ พลัส เล่นยังไง
- Fictional game Northstar Plus How do I play it?
- เกมสมมุติ ดาวเหนือ พลัส เกมเกี่ยวกับอะไรและเล่นยังไง

**age_rating — known**
```json
{
  "en": "Synthetic DEMO rating 9",
  "th": "เรตอายุสมมุติ DEMO 9"
}
```
**edition — known**
```json
"DEMO fiction revision 2"
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
  "en": "Two players coordinate buttons to fly through rings; follow the demonstration controls",
  "th": "ผู้เล่นสองคนประสานปุ่มเพื่อพายานผ่านวงแหวน; ใช้คำสั่งตามชุดควบคุมทดลอง"
}
```
**publisher_url — known**
```json
"https://example.invalid/demo20/fictional-game/2"
```
**summary — known**
```json
{
  "en": "Fictional test game: Two players coordinate buttons to fly through rings",
  "th": "เกมแต่งขึ้นเพื่อทดสอบ: ผู้เล่นสองคนประสานปุ่มเพื่อพายานผ่านวงแหวน"
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
  "en": "Fictional Orbit Duo",
  "th": "เกมสมมุติ วงโคจรคู่"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_02.json)

### กลุ่มผู้ใช้ (`audience`)

รหัส `demo20_audience_02`

คำถามตัวอย่าง:

- กลุ่มผู้ใช้ ดาวเหนือ พลัส ต้องใช้หลักฐานอะไร
- Demo visitors Northstar Plus What proof is required?
- กลุ่มผู้ใช้ ดาวเหนือ พลัส ใครใช้สิทธิ์กลุ่มนี้ได้และต้องแสดงหลักฐานอะไร

**eligibility — known**
```json
{
  "en": "Fictional group 2: demo sessions only",
  "th": "ผู้ใช้สมมุติกลุ่ม 2: ใช้บริการตามรอบทดลอง"
}
```
**name — known**
```json
{
  "en": "Demo visitors Northstar Plus",
  "th": "กลุ่มผู้ใช้ ดาวเหนือ พลัส"
}
```
**required_proofs — known**
```json
[
  "DEMO pass Northstar Plus"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/audience/demo20_audience_02.json)

### ติดต่อ (`contact`)

รหัส `demo20_contact_02`

คำถามตัวอย่าง:

- ช่องทางช่วยเหลือ ดาวเหนือ พลัส ติดต่อทางไหน
- Demo help channel Northstar Plus How can I contact them?
- ช่องทางช่วยเหลือ ดาวเหนือ พลัส ติดต่อที่ไหนและติดต่อได้ช่วงไหน

**channel — known**
```json
"facebook"
```
**office_hours — known**
```json
{
  "en": "Demo hours 10:00–19:00",
  "th": "ช่วงทดลอง 10:00–19:00"
}
```
**purpose — known**
```json
{
  "en": "Fictional support for Player substitution",
  "th": "สอบถามสมมุติเรื่อง เปลี่ยนผู้เล่น"
}
```
**value — known**
```json
"https://example.invalid/demo20/social/2"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_02.json)

### ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`)

รหัส `demo20_procedure_02`

คำถามตัวอย่าง:

- ขั้นตอนทดลอง ดาวเหนือ พลัส ต้องทำยังไงบ้าง
- Demo procedure Northstar Plus What steps should I follow?
- ขั้นตอนทดลอง ดาวเหนือ พลัส มีขั้นตอนอะไรและต้องใช้เอกสารอะไร

**deadline_minutes — known**
```json
15
```
**outcome — known**
```json
{
  "en": "Demo outcome: Player substitution checked",
  "th": "ผลทดสอบ: ตรวจสอบ เปลี่ยนผู้เล่น เสร็จ"
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
  "DEMO pass Northstar Plus"
]
```
**steps — known**
```json
[
  {
    "contact_id": null,
    "instruction": {
      "en": "Select the fictional Northstar Plus service",
      "th": "เลือกบริการสมมุติ ดาวเหนือ พลัส"
    },
    "order": 1
  },
  {
    "contact_id": "demo20_contact_02",
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
"DEMO Player substitution"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_02.json)

### นโยบายและกฎศูนย์ (`policy`)

รหัส `demo20_policy_02`

คำถามตัวอย่าง:

- ข้อกำหนดทดลอง ดาวเหนือ พลัส กฎเป็นยังไง
- Demo policy Northstar Plus What are the rules?
- ข้อกำหนดทดลอง ดาวเหนือ พลัส อนุญาตไหมและมีข้อยกเว้นอะไร

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
"prohibited"
```
**details — known**
```json
{
  "en": "Fictional rule for Player substitution: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "กติกาสมมุติเรื่องเปลี่ยนผู้เล่น: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
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
"demo20_procedure_02"
```
**subject — known**
```json
{
  "en": "Demo policy Northstar Plus",
  "th": "ข้อกำหนดทดลอง ดาวเหนือ พลัส"
}
```
**topic — known**
```json
"DEMO Player substitution"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/policy/demo20_policy_02.json)

### สิ่งอำนวยความสะดวก (`facility`)

รหัส `demo20_facility_02`

คำถามตัวอย่าง:

- พื้นที่พัก ดาวเหนือ พลัส อยู่ตรงไหนในร้าน
- Demo amenity Northstar Plus Where in the venue is it?
- พื้นที่พัก ดาวเหนือ พลัส อยู่ตรงไหนและคนที่ต้องการความช่วยเหลือเข้าใช้ยังไง

**accessibility — known**
```json
{
  "en": "Synthetic accessibility: operator assistance needed",
  "th": "ข้อมูลสมมุติ: ต้องมีผู้ดูแลช่วย"
}
```
**location — known**
```json
{
  "en": "Eye-rest corner in demo room 102",
  "th": "จุดพักสายตา อยู่ห้องทดสอบ 102"
}
```
**name — known**
```json
{
  "en": "Demo amenity Northstar Plus",
  "th": "พื้นที่พัก ดาวเหนือ พลัส"
}
```
**usage_conditions — known**
```json
{
  "en": "Demo sessions only; may use while waiting",
  "th": "ใช้ตามรอบทดลอง; ใช้ได้ระหว่างรอ"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/facility/demo20_facility_02.json)

### เกมที่ศูนย์มีให้เล่นจริง (`game_service`)

รหัส `demo20_game_service_02`

คำถามตัวอย่าง:

- การติดตั้งทดลอง ดาวเหนือ พลัส มีให้เล่นหรือยัง
- Demo installation Northstar Plus Is this game offered?
- การติดตั้งทดลอง ดาวเหนือ พลัส มีให้เล่นไหมและติดตั้งรุ่นไหน

**account_policy_id — known**
```json
"demo20_policy_02"
```
**game_id — known**
```json
"demo20_game_02"
```
**game_version — known**
```json
"DEMO BUILD 2"
```
**installed_resource_ids — known**
```json
[
  "demo20_resource_02"
]
```
**offered — known**
```json
true
```
**service_id — known**
```json
"demo20_service_02"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_service/demo20_game_service_02.json)

### รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`)

รหัส `demo20_game_mode_02`

คำถามตัวอย่าง:

- โหมดทดลอง ดาวเหนือ พลัส เล่นพร้อมกันได้สูงสุดกี่คน
- Demo mode Northstar Plus How many people can play together at most?
- โหมดทดลอง ดาวเหนือ พลัส ต้องมีขั้นต่ำกี่คนและเล่นได้สูงสุดกี่คน

**game_id — known**
```json
"demo20_game_02"
```
**mode_name — known**
```json
{
  "en": "Demo mode Northstar Plus",
  "th": "โหมดทดลอง ดาวเหนือ พลัส"
}
```
**network_requirement — known**
```json
{
  "en": "Synthetic network: offline",
  "th": "เครือข่ายจำลอง: เล่นออฟไลน์"
}
```
**platform — known**
```json
"PS5"
```
**players_max — known**
```json
2
```
**players_min — known**
```json
2
```
**studio_supported — known**
```json
true
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_mode/demo20_game_mode_02.json)

### วิธีเล่นและปุ่ม (`control_set`)

รหัส `demo20_control_set_02`

คำถามตัวอย่าง:

- ชุดควบคุมทดลอง ดาวเหนือ พลัส ปุ่มอะไรบ้าง
- Demo controls Northstar Plus What are the controls?
- ชุดควบคุมทดลอง ดาวเหนือ พลัส ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร

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
      "en": "Fictional input for Orbit Duo",
      "th": "คำสั่งสมมุติของ วงโคจรคู่"
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
      "en": "Fictional input for Orbit Duo",
      "th": "คำสั่งสมมุติของ วงโคจรคู่"
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
      "en": "Fictional input for Orbit Duo",
      "th": "คำสั่งสมมุติของ วงโคจรคู่"
    },
    "gesture": "press"
  }
]
```
**game_id — known**
```json
"demo20_game_02"
```
**game_version — known**
```json
"DEMO BUILD 2"
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
"DEMO_LAYOUT_2"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_02.json)

### ราคาต่อบริการ (`rate`)

รหัส `demo20_rate_02`

คำถามตัวอย่าง:

- อัตราทดลอง ดาวเหนือ พลัส ราคาเท่าไหร่
- Demo tariff Northstar Plus How much does it cost?
- อัตราทดลอง ดาวเหนือ พลัส ราคาเท่าไหร่และได้กี่นาที

**amount_minor — known**
```json
12000
```
**audience_id — known**
```json
"demo20_audience_02"
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
90
```
**persons_max — known**
```json
2
```
**persons_min — known**
```json
2
```
**service_id — known**
```json
"demo20_service_02"
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
"per_person"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rate/demo20_rate_02.json)

### ราคาเหมาโซน/ห้อง (`rental_package`)

รหัส `demo20_rental_package_02`

คำถามตัวอย่าง:

- แพ็กเกจทดลอง ดาวเหนือ พลัส เหมาเท่าไหร่
- Demo package Northstar Plus How much is the rental?
- แพ็กเกจทดลอง ดาวเหนือ พลัส ราคาเหมาเท่าไหร่และรวมอุปกรณ์อะไร

**amount_minor — known**
```json
37250
```
**audience_id — known**
```json
"demo20_audience_02"
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
  "en": "Fictional Northstar Plus station and PS5 inputs",
  "th": "เครื่องสมมุติ ดาวเหนือ พลัส พร้อมอุปกรณ์ PS5"
}
```
**name — known**
```json
{
  "en": "Demo package Northstar Plus",
  "th": "แพ็กเกจทดลอง ดาวเหนือ พลัส"
}
```
**period_label — known**
```json
"custom"
```
**room_seats — known**
```json
6
```
**terms — known**
```json
{
  "en": "Synthetic package excludes extensions; 2–2 people per session",
  "th": "แพ็กเกจสมมุติไม่รวมค่าต่อเวลา; รอบละ 2–2 คน"
}
```
**zone_ids — known**
```json
[
  "demo20_zone_02"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rental_package/demo20_rental_package_02.json)

### ตารางบริการ (`schedule`)

รหัส `demo20_schedule_02`

คำถามตัวอย่าง:

- ตารางทดลอง ดาวเหนือ พลัส จองช่วงไหนได้บ้าง
- Demo timetable Northstar Plus What are the booking hours?
- ตารางทดลอง ดาวเหนือ พลัส เปิดช่วงไหนและพักบำรุงรักษาตอนไหน

**bookable_periods — known**
```json
[
  {
    "end": "12:00",
    "start": "10:00"
  },
  {
    "end": "19:00",
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
    "end": "19:00",
    "start": "10:00"
  }
]
```
**reason — known**
```json
{
  "en": "Synthetic Northstar Plus schedule with maintenance",
  "th": "ตารางสมมุติ ดาวเหนือ พลัส มีพักบำรุงรักษา"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```
**weekday — known**
```json
2
```
**zone_ids — known**
```json
[
  "demo20_zone_02"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_02.json)

### วันปิด/ข้อยกเว้น (`closure`)

รหัส `demo20_closure_02`

คำถามตัวอย่าง:

- ประกาศวันทดลอง ดาวเหนือ พลัส วันนั้นปิดไหม
- Demo date notice Northstar Plus Is it closed on that date?
- ประกาศวันทดลอง ดาวเหนือ พลัส วันนั้นเปิดปิดยังไงและเพราะอะไร

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
"2026-12-02"
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
  "en": "Synthetic Northstar Plus date notice: open_override",
  "th": "ประกาศสมมุติ ดาวเหนือ พลัส: open_override"
}
```
**resolution_policy_id — known**
```json
"demo20_policy_02"
```
**state — known**
```json
"open_override"
```
**zone_ids — known**
```json
[
  "demo20_zone_02"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/closure/demo20_closure_02.json)

### รายการแข่งขันและฉบับกติกา (`competition`)

รหัส `demo20_competition_02`

คำถามตัวอย่าง:

- รายการฝึก ดาวเหนือ พลัส ใช้กติกาฉบับไหน
- Demo event Northstar Plus Which rulebook release applies?
- รายการฝึก ดาวเหนือ พลัส ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่

**competition_dates — known**
```json
[
  "2026-12-02"
]
```
**coverage — known**
```json
"complete"
```
**division — known**
```json
{
  "en": "Practice group 2–2 players",
  "th": "กลุ่มฝึก 2–2 คน"
}
```
**event_name — known**
```json
{
  "en": "Demo event Northstar Plus",
  "th": "รายการฝึก ดาวเหนือ พลัส"
}
```
**game_id — known**
```json
"demo20_game_02"
```
**rulebook_release — known**
```json
"DEMO20_REV_2"
```
**supersedes_id — not_applicable**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_02.json)

### ข้อกติกาการแข่งขัน (`competition_rule`)

รหัส `demo20_competition_rule_02`

คำถามตัวอย่าง:

- ข้อการแข่งขันทดลอง ดาวเหนือ พลัส ข้อนี้กำหนดอะไร
- Demo rule Northstar Plus What does this rule require?
- ข้อการแข่งขันทดลอง ดาวเหนือ พลัส กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม

**competition_id — known**
```json
"demo20_competition_02"
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
"roster_composition"
```
**heading — known**
```json
{
  "en": "Demo rule Northstar Plus",
  "th": "ข้อการแข่งขันทดลอง ดาวเหนือ พลัส"
}
```
**section_number — known**
```json
"3.2"
```
**text — known**
```json
{
  "en": "Fictional clause 2: for Player substitution, follow decision prohibited; exception requires written demo operator approval; not actual rules",
  "th": "ข้อสมมุติ 2: เปลี่ยนผู้เล่น ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_02.json)

### ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`)

รหัส `demo20_news_02`

คำถามตัวอย่าง:

- ข่าวทดลอง ดาวเหนือ พลัส ประกาศว่าอะไร
- Demo bulletin Northstar Plus What does the announcement say?
- ข่าวทดลอง ดาวเหนือ พลัส ประกาศอะไรและกิจกรรมเริ่มจบเมื่อไหร่

**audience_ids — known**
```json
[
  "demo20_audience_02"
]
```
**body — known**
```json
{
  "en": "Synthetic bulletin: Orbit Duo activity for 2–2 people; no actual payment",
  "th": "ข่าวสมมุติ: กิจกรรมวงโคจรคู่ สำหรับกลุ่ม 2–2 คน; ไม่มีรับเงินจริง"
}
```
**contact_id — known**
```json
"demo20_contact_02"
```
**event_end — known**
```json
"2026-12-02T12:00:00+07:00"
```
**event_start — known**
```json
"2026-12-02T10:00:00+07:00"
```
**registration_url — known**
```json
"https://example.invalid/demo20/register/2"
```
**title — known**
```json
{
  "en": "Demo bulletin Northstar Plus",
  "th": "ข่าวทดลอง ดาวเหนือ พลัส"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/news/demo20_news_02.json)

### บุคลากร/ทีมที่เปิดเผยได้ (`person`)

รหัส `demo20_person_02`

คำถามตัวอย่าง:

- ผู้ดูแลสมมุติ ดาวเหนือ พลัส รับผิดชอบอะไร
- Fictional host Northstar Plus What is their role?
- ผู้ดูแลสมมุติ ดาวเหนือ พลัส รับผิดชอบเรื่องอะไรและติดต่อทางไหน

**display_name — known**
```json
{
  "en": "Fictional host Northstar Plus",
  "th": "ผู้ดูแลสมมุติ ดาวเหนือ พลัส"
}
```
**public_contact_id — known**
```json
"demo20_contact_02"
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
  "en": "Fictional host for Player substitution",
  "th": "ผู้ดูแลสมมุติเรื่อง เปลี่ยนผู้เล่น"
}
```
**team — known**
```json
{
  "en": "Demo Northstar Plus team",
  "th": "ทีมทดสอบ ดาวเหนือ พลัส"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/person/demo20_person_02.json)

### คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`)

รหัส `demo20_faq_02`

คำถามตัวอย่าง:

- คำถามตัวอย่าง ดาวเหนือ พลัส คำตอบคืออะไร
- Demo enquiry Northstar Plus What is the answer?
- คำถามตัวอย่าง ดาวเหนือ พลัส คำตอบคืออะไรและใช้กับกรณีไหน

**answer — known**
```json
{
  "en": "Example answer: Fictional rule for Player substitution: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องเปลี่ยนผู้เล่น: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
}
```
**question — known**
```json
{
  "en": "Demo enquiry Northstar Plus",
  "th": "คำถามตัวอย่าง ดาวเหนือ พลัส"
}
```
**related_ids — known**
```json
[
  "demo20_policy_02",
  "demo20_procedure_02"
]
```
**scope_note — known**
```json
{
  "en": "Only applies to fictional Northstar Plus scenario",
  "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ดาวเหนือ พลัส"
}
```
**topic — known**
```json
"DEMO Player substitution"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_02.json)

### การเชื่อมสถานะสด (`live_binding`)

รหัส `demo20_live_binding_02`

คำถามตัวอย่าง:

- ตัวเชื่อมทดลอง ดาวเหนือ พลัส จับคู่สถานะยังไง
- Demo binding Northstar Plus How are statuses mapped?
- ตัวเชื่อมทดลอง ดาวเหนือ พลัส จับคู่สถานะแบบไหนและเก็บข้อมูลนานเท่าไหร่

**external_resource_key — known**
```json
"DEMO20_EXTERNAL_2"
```
**freshness_policy — known**
```json
{
  "en": "Synthetic TTL 25 seconds; no API call or live status claim",
  "th": "ค่าจำลอง TTL 25 วินาที; ไม่เรียก API และไม่ยืนยันสถานะสด"
}
```
**physical_pool_key — known**
```json
"demo20_pool_02"
```
**provider — known**
```json
"wordpress_booking"
```
**service_id — known**
```json
"demo20_service_02"
```
**status_mapping — known**
```json
[
  {
    "normalized": "free",
    "raw": "DEMO_EMPTY_2"
  },
  {
    "normalized": "occupied",
    "raw": "DEMO_BUSY_2"
  },
  {
    "normalized": "unknown",
    "raw": "DEMO_UNKNOWN_2"
  }
]
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/live_binding/demo20_live_binding_02.json)

