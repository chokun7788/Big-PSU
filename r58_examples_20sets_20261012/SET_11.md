# ชุด 11 — ต้นเฟิร์น / Fern

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

เกม สถานที่ ราคา กฎ บุคคล และสถานะทั้งหมดในชุดใหม่นี้แต่งขึ้นเพื่อทดสอบ ไม่ได้เป็นข้อมูล PSU หรือเกมที่มีจำหน่ายจริง คำแปลยังไม่ผ่านมนุษย์

แพลตฟอร์มตัวอย่าง: PC • จำนวนผู้เล่น 2–3 • เวลาเล่น 90 นาที / กินช่องจอง 90 นาที

## ข้อมูลครบ 24 หมวด

### ข้อมูลศูนย์ (`center`)

รหัส `demo20_center_11`

คำถามตัวอย่าง:

- ศูนย์ทดลอง ต้นเฟิร์น อยู่ตรงไหน
- Demo venue Fern Where is it located?
- ศูนย์ทดลอง ต้นเฟิร์น อยู่ตึกอะไร ชั้นไหน

**address — known**
```json
{
  "en": "Fictional address 77, Example Road, Test District",
  "th": "เลขที่สมมุติ 77 ถนนตัวอย่าง แขวงทดลอง"
}
```
**building — known**
```json
"DEMO Tower B"
```
**description — known**
```json
{
  "en": "Synthetic scenario 11: Shadow Maze, not a real venue",
  "th": "สถานการณ์ทดลอง 11: เขาวงกตเงา ไม่ใช่สถานที่จริง"
}
```
**floor — known**
```json
"2"
```
**map_url — known**
```json
"https://example.invalid/demo20/map/11"
```
**name — known**
```json
{
  "en": "Demo venue Fern",
  "th": "ศูนย์ทดลอง ต้นเฟิร์น"
}
```
**operator — known**
```json
{
  "en": "Fictional Fern operator",
  "th": "ผู้ประกอบการสมมุติ ต้นเฟิร์น"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/center/demo20_center_11.json)

### โซนบริการ (`zone`)

รหัส `demo20_zone_11`

คำถามตัวอย่าง:

- โซนทดลอง ต้นเฟิร์น มีที่นั่งกี่ที่
- Demo zone Fern How many seats are there?
- โซนทดลอง ต้นเฟิร์น โซนนี้อยู่ตรงไหนและมีที่นั่งกี่ที่

**description — known**
```json
{
  "en": "Synthetic PC zone for Shadow Maze",
  "th": "โซนจำลอง PC สำหรับเขาวงกตเงา"
}
```
**location — known**
```json
{
  "en": "Test building, floor 2, room 111",
  "th": "อาคารทดสอบ ชั้น 2 ห้อง 111"
}
```
**name — known**
```json
{
  "en": "Demo zone Fern",
  "th": "โซนทดลอง ต้นเฟิร์น"
}
```
**room_seats — known**
```json
7
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_11.json)

### รุ่นและสเปกอุปกรณ์ (`equipment_model`)

รหัส `demo20_equipment_model_11`

คำถามตัวอย่าง:

- รุ่นอุปกรณ์ ต้นเฟิร์น สเปกมีอะไรบ้าง
- Demo model Fern What are its specifications?
- รุ่นอุปกรณ์ ต้นเฟิร์น เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง

**device_type — known**
```json
"pc"
```
**name — known**
```json
{
  "en": "Demo model Fern",
  "th": "รุ่นอุปกรณ์ ต้นเฟิร์น"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_11.json)

### เครื่องหรือทรัพยากรจริง (`resource`)

รหัส `demo20_resource_11`

คำถามตัวอย่าง:

- เครื่องทดลอง ต้นเฟิร์น เล่นพร้อมกันได้กี่คน
- Demo station Fern How many people can play at once?
- เครื่องทดลอง ต้นเฟิร์น เครื่องยังใช้งานได้ไหมและรองรับกี่คน

**capacity_persons — known**
```json
3
```
**equipment_model_ids — known**
```json
[
  "demo20_equipment_model_11"
]
```
**name — known**
```json
{
  "en": "Demo station Fern",
  "th": "เครื่องทดลอง ต้นเฟิร์น"
}
```
**operational_status — known**
```json
"in_service"
```
**physical_pool_key — known**
```json
"demo20_pool_11"
```
**zone_id — known**
```json
"demo20_zone_11"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/resource/demo20_resource_11.json)

### รายการที่เลือกในระบบจอง (`service`)

รหัส `demo20_service_11`

คำถามตัวอย่าง:

- รอบทดลอง ต้นเฟิร์น หนึ่งรอบเล่นได้กี่นาที
- Demo session Fern How many minutes does one session last?
- รอบทดลอง ต้นเฟิร์น เวลาเล่นกับเวลาที่กินช่องจองกี่นาที

**booking_product_key — known**
```json
"DEMO20_BOOKING_11"
```
**capacity_max — known**
```json
3
```
**capacity_min — known**
```json
2
```
**name — known**
```json
{
  "en": "Demo session Fern",
  "th": "รอบทดลอง ต้นเฟิร์น"
}
```
**occupancy_minutes — known**
```json
90
```
**platform — known**
```json
"PC"
```
**resource_ids — known**
```json
[
  "demo20_resource_11"
]
```
**session_minutes — known**
```json
90
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_11.json)

### ข้อมูลเกม (`game`)

รหัส `demo20_game_11`

คำถามตัวอย่าง:

- เกมสมมุติ ต้นเฟิร์น เล่นยังไง
- Fictional game Fern How do I play it?
- เกมสมมุติ ต้นเฟิร์น เกมเกี่ยวกับอะไรและเล่นยังไง

**age_rating — known**
```json
{
  "en": "Synthetic DEMO rating 12",
  "th": "เรตอายุสมมุติ DEMO 12"
}
```
**edition — known**
```json
"DEMO fiction revision 11"
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
  "en": "Find an exit by describing paths to teammates; follow the demonstration controls",
  "th": "หาทางออกโดยบอกเส้นทางให้เพื่อนฟัง; ใช้คำสั่งตามชุดควบคุมทดลอง"
}
```
**publisher_url — known**
```json
"https://example.invalid/demo20/fictional-game/11"
```
**summary — known**
```json
{
  "en": "Fictional test game: Find an exit by describing paths to teammates",
  "th": "เกมแต่งขึ้นเพื่อทดสอบ: หาทางออกโดยบอกเส้นทางให้เพื่อนฟัง"
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
  "en": "Fictional Shadow Maze",
  "th": "เกมสมมุติ เขาวงกตเงา"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_11.json)

### กลุ่มผู้ใช้ (`audience`)

รหัส `demo20_audience_11`

คำถามตัวอย่าง:

- กลุ่มผู้ใช้ ต้นเฟิร์น ต้องใช้หลักฐานอะไร
- Demo visitors Fern What proof is required?
- กลุ่มผู้ใช้ ต้นเฟิร์น ใครใช้สิทธิ์กลุ่มนี้ได้และต้องแสดงหลักฐานอะไร

**eligibility — known**
```json
{
  "en": "Fictional group 11: demo sessions only",
  "th": "ผู้ใช้สมมุติกลุ่ม 11: ใช้บริการตามรอบทดลอง"
}
```
**name — known**
```json
{
  "en": "Demo visitors Fern",
  "th": "กลุ่มผู้ใช้ ต้นเฟิร์น"
}
```
**required_proofs — known**
```json
[
  "DEMO pass Fern"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/audience/demo20_audience_11.json)

### ติดต่อ (`contact`)

รหัส `demo20_contact_11`

คำถามตัวอย่าง:

- ช่องทางช่วยเหลือ ต้นเฟิร์น ติดต่อทางไหน
- Demo help channel Fern How can I contact them?
- ช่องทางช่วยเหลือ ต้นเฟิร์น ติดต่อที่ไหนและติดต่อได้ช่วงไหน

**channel — known**
```json
"email"
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
  "en": "Fictional support for Personal devices",
  "th": "สอบถามสมมุติเรื่อง อุปกรณ์ส่วนตัว"
}
```
**value — known**
```json
"fiction11@example.invalid"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_11.json)

### ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`)

รหัส `demo20_procedure_11`

คำถามตัวอย่าง:

- ขั้นตอนทดลอง ต้นเฟิร์น ต้องทำยังไงบ้าง
- Demo procedure Fern What steps should I follow?
- ขั้นตอนทดลอง ต้นเฟิร์น มีขั้นตอนอะไรและต้องใช้เอกสารอะไร

**deadline_minutes — known**
```json
10
```
**outcome — known**
```json
{
  "en": "Demo outcome: Personal devices checked",
  "th": "ผลทดสอบ: ตรวจสอบ อุปกรณ์ส่วนตัว เสร็จ"
}
```
**preconditions — known**
```json
[]
```
**required_documents — known**
```json
[
  "DEMO pass Fern"
]
```
**steps — known**
```json
[
  {
    "contact_id": null,
    "instruction": {
      "en": "Select the fictional Fern service",
      "th": "เลือกบริการสมมุติ ต้นเฟิร์น"
    },
    "order": 1
  },
  {
    "contact_id": "demo20_contact_11",
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
"DEMO Personal devices"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_11.json)

### นโยบายและกฎศูนย์ (`policy`)

รหัส `demo20_policy_11`

คำถามตัวอย่าง:

- ข้อกำหนดทดลอง ต้นเฟิร์น กฎเป็นยังไง
- Demo policy Fern What are the rules?
- ข้อกำหนดทดลอง ต้นเฟิร์น อนุญาตไหมและมีข้อยกเว้นอะไร

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
  "en": "Fictional rule for Personal devices: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "กติกาสมมุติเรื่องอุปกรณ์ส่วนตัว: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
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
"demo20_procedure_11"
```
**subject — known**
```json
{
  "en": "Demo policy Fern",
  "th": "ข้อกำหนดทดลอง ต้นเฟิร์น"
}
```
**topic — known**
```json
"DEMO Personal devices"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/policy/demo20_policy_11.json)

### สิ่งอำนวยความสะดวก (`facility`)

รหัส `demo20_facility_11`

คำถามตัวอย่าง:

- พื้นที่พัก ต้นเฟิร์น อยู่ตรงไหนในร้าน
- Demo amenity Fern Where in the venue is it?
- พื้นที่พัก ต้นเฟิร์น อยู่ตรงไหนและคนที่ต้องการความช่วยเหลือเข้าใช้ยังไง

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
  "en": "Device shelf in demo room 111",
  "th": "ชั้นวางอุปกรณ์ อยู่ห้องทดสอบ 111"
}
```
**name — known**
```json
{
  "en": "Demo amenity Fern",
  "th": "พื้นที่พัก ต้นเฟิร์น"
}
```
**usage_conditions — known**
```json
{
  "en": "Demo sessions only; ask the operator first",
  "th": "ใช้ตามรอบทดลอง; ต้องขอผู้ดูแลก่อน"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/facility/demo20_facility_11.json)

### เกมที่ศูนย์มีให้เล่นจริง (`game_service`)

รหัส `demo20_game_service_11`

คำถามตัวอย่าง:

- การติดตั้งทดลอง ต้นเฟิร์น มีให้เล่นหรือยัง
- Demo installation Fern Is this game offered?
- การติดตั้งทดลอง ต้นเฟิร์น มีให้เล่นไหมและติดตั้งรุ่นไหน

**account_policy_id — known**
```json
"demo20_policy_11"
```
**game_id — known**
```json
"demo20_game_11"
```
**game_version — known**
```json
"DEMO BUILD 11"
```
**installed_resource_ids — known**
```json
[
  "demo20_resource_11"
]
```
**offered — known**
```json
true
```
**service_id — known**
```json
"demo20_service_11"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_service/demo20_game_service_11.json)

### รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`)

รหัส `demo20_game_mode_11`

คำถามตัวอย่าง:

- โหมดทดลอง ต้นเฟิร์น เล่นพร้อมกันได้สูงสุดกี่คน
- Demo mode Fern How many people can play together at most?
- โหมดทดลอง ต้นเฟิร์น ต้องมีขั้นต่ำกี่คนและเล่นได้สูงสุดกี่คน

**game_id — known**
```json
"demo20_game_11"
```
**mode_name — known**
```json
{
  "en": "Demo mode Fern",
  "th": "โหมดทดลอง ต้นเฟิร์น"
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
3
```
**players_min — known**
```json
2
```
**studio_supported — known**
```json
true
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_mode/demo20_game_mode_11.json)

### วิธีเล่นและปุ่ม (`control_set`)

รหัส `demo20_control_set_11`

คำถามตัวอย่าง:

- ชุดควบคุมทดลอง ต้นเฟิร์น ปุ่มอะไรบ้าง
- Demo controls Fern What are the controls?
- ชุดควบคุมทดลอง ต้นเฟิร์น ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร

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
      "en": "Fictional input for Shadow Maze",
      "th": "คำสั่งสมมุติของ เขาวงกตเงา"
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
      "en": "Fictional input for Shadow Maze",
      "th": "คำสั่งสมมุติของ เขาวงกตเงา"
    },
    "gesture": "press"
  },
  {
    "action": {
      "en": "Back",
      "th": "ย้อนกลับ"
    },
    "buttons": [
      "DEMO_keyboard_mouse_3"
    ],
    "context": {
      "en": "Fictional input for Shadow Maze",
      "th": "คำสั่งสมมุติของ เขาวงกตเงา"
    },
    "gesture": "press"
  }
]
```
**game_id — known**
```json
"demo20_game_11"
```
**game_version — known**
```json
"DEMO BUILD 11"
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
"DEMO_LAYOUT_11"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_11.json)

### ราคาต่อบริการ (`rate`)

รหัส `demo20_rate_11`

คำถามตัวอย่าง:

- อัตราทดลอง ต้นเฟิร์น ราคาเท่าไหร่
- Demo tariff Fern How much does it cost?
- อัตราทดลอง ต้นเฟิร์น ราคาเท่าไหร่และได้กี่นาที

**amount_minor — known**
```json
10000
```
**audience_id — known**
```json
"demo20_audience_11"
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
3
```
**persons_min — known**
```json
2
```
**service_id — known**
```json
"demo20_service_11"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rate/demo20_rate_11.json)

### ราคาเหมาโซน/ห้อง (`rental_package`)

รหัส `demo20_rental_package_11`

คำถามตัวอย่าง:

- แพ็กเกจทดลอง ต้นเฟิร์น เหมาเท่าไหร่
- Demo package Fern How much is the rental?
- แพ็กเกจทดลอง ต้นเฟิร์น ราคาเหมาเท่าไหร่และรวมอุปกรณ์อะไร

**amount_minor — known**
```json
31250
```
**audience_id — known**
```json
"demo20_audience_11"
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
  "en": "Fictional Fern station and PC inputs",
  "th": "เครื่องสมมุติ ต้นเฟิร์น พร้อมอุปกรณ์ PC"
}
```
**name — known**
```json
{
  "en": "Demo package Fern",
  "th": "แพ็กเกจทดลอง ต้นเฟิร์น"
}
```
**period_label — known**
```json
"custom"
```
**room_seats — known**
```json
7
```
**terms — known**
```json
{
  "en": "Synthetic package excludes extensions; 2–3 people per session",
  "th": "แพ็กเกจสมมุติไม่รวมค่าต่อเวลา; รอบละ 2–3 คน"
}
```
**zone_ids — known**
```json
[
  "demo20_zone_11"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rental_package/demo20_rental_package_11.json)

### ตารางบริการ (`schedule`)

รหัส `demo20_schedule_11`

คำถามตัวอย่าง:

- ตารางทดลอง ต้นเฟิร์น จองช่วงไหนได้บ้าง
- Demo timetable Fern What are the booking hours?
- ตารางทดลอง ต้นเฟิร์น เปิดช่วงไหนและพักบำรุงรักษาตอนไหน

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
  "en": "Synthetic Fern schedule with maintenance",
  "th": "ตารางสมมุติ ต้นเฟิร์น มีพักบำรุงรักษา"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```
**weekday — known**
```json
4
```
**zone_ids — known**
```json
[
  "demo20_zone_11"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_11.json)

### วันปิด/ข้อยกเว้น (`closure`)

รหัส `demo20_closure_11`

คำถามตัวอย่าง:

- ประกาศวันทดลอง ต้นเฟิร์น วันนั้นปิดไหม
- Demo date notice Fern Is it closed on that date?
- ประกาศวันทดลอง ต้นเฟิร์น วันนั้นเปิดปิดยังไงและเพราะอะไร

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
"2026-12-11"
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
  "en": "Synthetic Fern date notice: open_override",
  "th": "ประกาศสมมุติ ต้นเฟิร์น: open_override"
}
```
**resolution_policy_id — known**
```json
"demo20_policy_11"
```
**state — known**
```json
"open_override"
```
**zone_ids — known**
```json
[
  "demo20_zone_11"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/closure/demo20_closure_11.json)

### รายการแข่งขันและฉบับกติกา (`competition`)

รหัส `demo20_competition_11`

คำถามตัวอย่าง:

- รายการฝึก ต้นเฟิร์น ใช้กติกาฉบับไหน
- Demo event Fern Which rulebook release applies?
- รายการฝึก ต้นเฟิร์น ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่

**competition_dates — known**
```json
[
  "2026-12-11"
]
```
**coverage — known**
```json
"complete"
```
**division — known**
```json
{
  "en": "Practice group 2–3 players",
  "th": "กลุ่มฝึก 2–3 คน"
}
```
**event_name — known**
```json
{
  "en": "Demo event Fern",
  "th": "รายการฝึก ต้นเฟิร์น"
}
```
**game_id — known**
```json
"demo20_game_11"
```
**rulebook_release — known**
```json
"DEMO20_REV_11"
```
**supersedes_id — not_applicable**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_11.json)

### ข้อกติกาการแข่งขัน (`competition_rule`)

รหัส `demo20_competition_rule_11`

คำถามตัวอย่าง:

- ข้อการแข่งขันทดลอง ต้นเฟิร์น ข้อนี้กำหนดอะไร
- Demo rule Fern What does this rule require?
- ข้อการแข่งขันทดลอง ต้นเฟิร์น กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม

**competition_id — known**
```json
"demo20_competition_11"
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
  "en": "Demo rule Fern",
  "th": "ข้อการแข่งขันทดลอง ต้นเฟิร์น"
}
```
**section_number — known**
```json
"2.11"
```
**text — known**
```json
{
  "en": "Fictional clause 11: for Personal devices, follow decision allowed; exception requires written demo operator approval; not actual rules",
  "th": "ข้อสมมุติ 11: อุปกรณ์ส่วนตัว ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_11.json)

### ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`)

รหัส `demo20_news_11`

คำถามตัวอย่าง:

- ข่าวทดลอง ต้นเฟิร์น ประกาศว่าอะไร
- Demo bulletin Fern What does the announcement say?
- ข่าวทดลอง ต้นเฟิร์น ประกาศอะไรและกิจกรรมเริ่มจบเมื่อไหร่

**audience_ids — known**
```json
[
  "demo20_audience_11"
]
```
**body — known**
```json
{
  "en": "Synthetic bulletin: Shadow Maze activity for 2–3 people; no actual payment",
  "th": "ข่าวสมมุติ: กิจกรรมเขาวงกตเงา สำหรับกลุ่ม 2–3 คน; ไม่มีรับเงินจริง"
}
```
**contact_id — known**
```json
"demo20_contact_11"
```
**event_end — known**
```json
"2026-12-11T12:00:00+07:00"
```
**event_start — known**
```json
"2026-12-11T10:00:00+07:00"
```
**registration_url — known**
```json
"https://example.invalid/demo20/register/11"
```
**title — known**
```json
{
  "en": "Demo bulletin Fern",
  "th": "ข่าวทดลอง ต้นเฟิร์น"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/news/demo20_news_11.json)

### บุคลากร/ทีมที่เปิดเผยได้ (`person`)

รหัส `demo20_person_11`

คำถามตัวอย่าง:

- ผู้ดูแลสมมุติ ต้นเฟิร์น รับผิดชอบอะไร
- Fictional host Fern What is their role?
- ผู้ดูแลสมมุติ ต้นเฟิร์น รับผิดชอบเรื่องอะไรและติดต่อทางไหน

**display_name — known**
```json
{
  "en": "Fictional host Fern",
  "th": "ผู้ดูแลสมมุติ ต้นเฟิร์น"
}
```
**public_contact_id — known**
```json
"demo20_contact_11"
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
  "en": "Fictional host for Personal devices",
  "th": "ผู้ดูแลสมมุติเรื่อง อุปกรณ์ส่วนตัว"
}
```
**team — known**
```json
{
  "en": "Demo Fern team",
  "th": "ทีมทดสอบ ต้นเฟิร์น"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/person/demo20_person_11.json)

### คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`)

รหัส `demo20_faq_11`

คำถามตัวอย่าง:

- คำถามตัวอย่าง ต้นเฟิร์น คำตอบคืออะไร
- Demo enquiry Fern What is the answer?
- คำถามตัวอย่าง ต้นเฟิร์น คำตอบคืออะไรและใช้กับกรณีไหน

**answer — known**
```json
{
  "en": "Example answer: Fictional rule for Personal devices: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องอุปกรณ์ส่วนตัว: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
}
```
**question — known**
```json
{
  "en": "Demo enquiry Fern",
  "th": "คำถามตัวอย่าง ต้นเฟิร์น"
}
```
**related_ids — known**
```json
[
  "demo20_policy_11",
  "demo20_procedure_11"
]
```
**scope_note — known**
```json
{
  "en": "Only applies to fictional Fern scenario",
  "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ต้นเฟิร์น"
}
```
**topic — known**
```json
"DEMO Personal devices"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_11.json)

### การเชื่อมสถานะสด (`live_binding`)

รหัส `demo20_live_binding_11`

คำถามตัวอย่าง:

- ตัวเชื่อมทดลอง ต้นเฟิร์น จับคู่สถานะยังไง
- Demo binding Fern How are statuses mapped?
- ตัวเชื่อมทดลอง ต้นเฟิร์น จับคู่สถานะแบบไหนและเก็บข้อมูลนานเท่าไหร่

**external_resource_key — known**
```json
"DEMO20_EXTERNAL_11"
```
**freshness_policy — known**
```json
{
  "en": "Synthetic TTL 70 seconds; no API call or live status claim",
  "th": "ค่าจำลอง TTL 70 วินาที; ไม่เรียก API และไม่ยืนยันสถานะสด"
}
```
**physical_pool_key — known**
```json
"demo20_pool_11"
```
**provider — known**
```json
"wordpress_booking"
```
**service_id — known**
```json
"demo20_service_11"
```
**status_mapping — known**
```json
[
  {
    "normalized": "free",
    "raw": "DEMO_EMPTY_11"
  },
  {
    "normalized": "occupied",
    "raw": "DEMO_BUSY_11"
  },
  {
    "normalized": "unknown",
    "raw": "DEMO_UNKNOWN_11"
  }
]
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/live_binding/demo20_live_binding_11.json)

