# ชุด 15 — กิ่งไผ่ / Bamboo

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

เกม สถานที่ ราคา กฎ บุคคล และสถานะทั้งหมดในชุดใหม่นี้แต่งขึ้นเพื่อทดสอบ ไม่ได้เป็นข้อมูล PSU หรือเกมที่มีจำหน่ายจริง คำแปลยังไม่ผ่านมนุษย์

แพลตฟอร์มตัวอย่าง: PC • จำนวนผู้เล่น 1–2 • เวลาเล่น 75 นาที / กินช่องจอง 75 นาที

## ข้อมูลครบ 24 หมวด

### ข้อมูลศูนย์ (`center`)

รหัส `demo20_center_15`

คำถามตัวอย่าง:

- ศูนย์ทดลอง กิ่งไผ่ อยู่ตรงไหน
- Demo venue Bamboo Where is it located?
- ศูนย์ทดลอง กิ่งไผ่ อยู่ตึกอะไร ชั้นไหน

**address — known**
```json
{
  "en": "Fictional address 105, Example Road, Test District",
  "th": "เลขที่สมมุติ 105 ถนนตัวอย่าง แขวงทดลอง"
}
```
**building — known**
```json
"DEMO Tower A"
```
**description — known**
```json
{
  "en": "Synthetic scenario 15: Puzzle Box, not a real venue",
  "th": "สถานการณ์ทดลอง 15: กล่องปริศนา ไม่ใช่สถานที่จริง"
}
```
**floor — known**
```json
"1"
```
**map_url — unknown**
```json
null
```
**name — known**
```json
{
  "en": "Demo venue Bamboo",
  "th": "ศูนย์ทดลอง กิ่งไผ่"
}
```
**operator — known**
```json
{
  "en": "Fictional Bamboo operator",
  "th": "ผู้ประกอบการสมมุติ กิ่งไผ่"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/center/demo20_center_15.json)

### โซนบริการ (`zone`)

รหัส `demo20_zone_15`

คำถามตัวอย่าง:

- โซนทดลอง กิ่งไผ่ มีที่นั่งกี่ที่
- Demo zone Bamboo How many seats are there?
- โซนทดลอง กิ่งไผ่ โซนนี้อยู่ตรงไหนและมีที่นั่งกี่ที่

**description — known**
```json
{
  "en": "Synthetic PC zone for Puzzle Box",
  "th": "โซนจำลอง PC สำหรับกล่องปริศนา"
}
```
**location — known**
```json
{
  "en": "Test building, floor 1, room 115",
  "th": "อาคารทดสอบ ชั้น 1 ห้อง 115"
}
```
**name — known**
```json
{
  "en": "Demo zone Bamboo",
  "th": "โซนทดลอง กิ่งไผ่"
}
```
**room_seats — known**
```json
4
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_15.json)

### รุ่นและสเปกอุปกรณ์ (`equipment_model`)

รหัส `demo20_equipment_model_15`

คำถามตัวอย่าง:

- รุ่นอุปกรณ์ กิ่งไผ่ สเปกมีอะไรบ้าง
- Demo model Bamboo What are its specifications?
- รุ่นอุปกรณ์ กิ่งไผ่ เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง

**device_type — known**
```json
"pc"
```
**name — known**
```json
{
  "en": "Demo model Bamboo",
  "th": "รุ่นอุปกรณ์ กิ่งไผ่"
}
```
**specifications — unknown**
```json
null
```
**usage — known**
```json
{
  "en": "Fictional equipment for PC; not a PSU specification",
  "th": "เครื่องสมมุติใช้กับ PC; ห้ามอ้างเป็นสเปกศูนย์"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_15.json)

### เครื่องหรือทรัพยากรจริง (`resource`)

รหัส `demo20_resource_15`

คำถามตัวอย่าง:

- เครื่องทดลอง กิ่งไผ่ เล่นพร้อมกันได้กี่คน
- Demo station Bamboo How many people can play at once?
- เครื่องทดลอง กิ่งไผ่ เครื่องยังใช้งานได้ไหมและรองรับกี่คน

**capacity_persons — known**
```json
2
```
**equipment_model_ids — known**
```json
[
  "demo20_equipment_model_15"
]
```
**name — known**
```json
{
  "en": "Demo station Bamboo",
  "th": "เครื่องทดลอง กิ่งไผ่"
}
```
**operational_status — known**
```json
"out_of_service"
```
**physical_pool_key — known**
```json
"demo20_pool_15"
```
**zone_id — known**
```json
"demo20_zone_15"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/resource/demo20_resource_15.json)

### รายการที่เลือกในระบบจอง (`service`)

รหัส `demo20_service_15`

คำถามตัวอย่าง:

- รอบทดลอง กิ่งไผ่ หนึ่งรอบเล่นได้กี่นาที
- Demo session Bamboo How many minutes does one session last?
- รอบทดลอง กิ่งไผ่ เวลาเล่นกับเวลาที่กินช่องจองกี่นาที

**booking_product_key — unknown**
```json
null
```
**capacity_max — known**
```json
2
```
**capacity_min — known**
```json
1
```
**name — known**
```json
{
  "en": "Demo session Bamboo",
  "th": "รอบทดลอง กิ่งไผ่"
}
```
**occupancy_minutes — known**
```json
75
```
**platform — known**
```json
"PC"
```
**resource_ids — known**
```json
[
  "demo20_resource_15"
]
```
**session_minutes — known**
```json
75
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_15.json)

### ข้อมูลเกม (`game`)

รหัส `demo20_game_15`

คำถามตัวอย่าง:

- เกมสมมุติ กิ่งไผ่ เล่นยังไง
- Fictional game Bamboo How do I play it?
- เกมสมมุติ กิ่งไผ่ เกมเกี่ยวกับอะไรและเล่นยังไง

**age_rating — unknown**
```json
null
```
**edition — known**
```json
"DEMO fiction revision 15"
```
**genre — known**
```json
{
  "en": "Cooperative",
  "th": "ร่วมมือ"
}
```
**how_to_play — known**
```json
{
  "en": "Take turns solving puzzles and recording codes; follow the demonstration controls",
  "th": "ผลัดกันแก้ปริศนาและบันทึกรหัส; ใช้คำสั่งตามชุดควบคุมทดลอง"
}
```
**publisher_url — known**
```json
"https://example.invalid/demo20/fictional-game/15"
```
**summary — known**
```json
{
  "en": "Fictional test game: Take turns solving puzzles and recording codes",
  "th": "เกมแต่งขึ้นเพื่อทดสอบ: ผลัดกันแก้ปริศนาและบันทึกรหัส"
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
  "en": "Fictional Puzzle Box",
  "th": "เกมสมมุติ กล่องปริศนา"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_15.json)

### กลุ่มผู้ใช้ (`audience`)

รหัส `demo20_audience_15`

คำถามตัวอย่าง:

- กลุ่มผู้ใช้ กิ่งไผ่ ต้องใช้หลักฐานอะไร
- Demo visitors Bamboo What proof is required?
- กลุ่มผู้ใช้ กิ่งไผ่ ใครใช้สิทธิ์กลุ่มนี้ได้และต้องแสดงหลักฐานอะไร

**eligibility — known**
```json
{
  "en": "Fictional group 15: demo sessions only",
  "th": "ผู้ใช้สมมุติกลุ่ม 15: ใช้บริการตามรอบทดลอง"
}
```
**name — known**
```json
{
  "en": "Demo visitors Bamboo",
  "th": "กลุ่มผู้ใช้ กิ่งไผ่"
}
```
**required_proofs — unknown**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/audience/demo20_audience_15.json)

### ติดต่อ (`contact`)

รหัส `demo20_contact_15`

คำถามตัวอย่าง:

- ช่องทางช่วยเหลือ กิ่งไผ่ ติดต่อทางไหน
- Demo help channel Bamboo How can I contact them?
- ช่องทางช่วยเหลือ กิ่งไผ่ ติดต่อที่ไหนและติดต่อได้ช่วงไหน

**channel — known**
```json
"onsite"
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
  "en": "Fictional support for Software installation",
  "th": "สอบถามสมมุติเรื่อง ติดตั้งโปรแกรม"
}
```
**value — known**
```json
"DEMO desk Bamboo"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_15.json)

### ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`)

รหัส `demo20_procedure_15`

คำถามตัวอย่าง:

- ขั้นตอนทดลอง กิ่งไผ่ ต้องทำยังไงบ้าง
- Demo procedure Bamboo What steps should I follow?
- ขั้นตอนทดลอง กิ่งไผ่ มีขั้นตอนอะไรและต้องใช้เอกสารอะไร

**deadline_minutes — known**
```json
0
```
**outcome — known**
```json
{
  "en": "Demo outcome: Software installation checked",
  "th": "ผลทดสอบ: ตรวจสอบ ติดตั้งโปรแกรม เสร็จ"
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
  "DEMO pass Bamboo"
]
```
**steps — known**
```json
[
  {
    "contact_id": null,
    "instruction": {
      "en": "Select the fictional Bamboo service",
      "th": "เลือกบริการสมมุติ กิ่งไผ่"
    },
    "order": 1
  },
  {
    "contact_id": "demo20_contact_15",
    "instruction": {
      "en": "Check names and conditions before confirming",
      "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
    },
    "order": 2
  },
  {
    "contact_id": "demo20_contact_15",
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
"DEMO Software installation"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_15.json)

### นโยบายและกฎศูนย์ (`policy`)

รหัส `demo20_policy_15`

คำถามตัวอย่าง:

- ข้อกำหนดทดลอง กิ่งไผ่ กฎเป็นยังไง
- Demo policy Bamboo What are the rules?
- ข้อกำหนดทดลอง กิ่งไผ่ อนุญาตไหมและมีข้อยกเว้นอะไร

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
  "en": "Fictional rule for Software installation: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "กติกาสมมุติเรื่องติดตั้งโปรแกรม: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
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
"demo20_procedure_15"
```
**subject — known**
```json
{
  "en": "Demo policy Bamboo",
  "th": "ข้อกำหนดทดลอง กิ่งไผ่"
}
```
**topic — known**
```json
"DEMO Software installation"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/policy/demo20_policy_15.json)

### สิ่งอำนวยความสะดวก (`facility`)

รหัส `demo20_facility_15`

คำถามตัวอย่าง:

- พื้นที่พัก กิ่งไผ่ อยู่ตรงไหนในร้าน
- Demo amenity Bamboo Where in the venue is it?
- พื้นที่พัก กิ่งไผ่ อยู่ตรงไหนและคนที่ต้องการความช่วยเหลือเข้าใช้ยังไง

**accessibility — unknown**
```json
null
```
**location — known**
```json
{
  "en": "Technical counter in demo room 115",
  "th": "เคาน์เตอร์เทคนิค อยู่ห้องทดสอบ 115"
}
```
**name — known**
```json
{
  "en": "Demo amenity Bamboo",
  "th": "พื้นที่พัก กิ่งไผ่"
}
```
**usage_conditions — known**
```json
{
  "en": "Demo sessions only; ask the operator first",
  "th": "ใช้ตามรอบทดลอง; ต้องขอผู้ดูแลก่อน"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/facility/demo20_facility_15.json)

### เกมที่ศูนย์มีให้เล่นจริง (`game_service`)

รหัส `demo20_game_service_15`

คำถามตัวอย่าง:

- การติดตั้งทดลอง กิ่งไผ่ มีให้เล่นหรือยัง
- Demo installation Bamboo Is this game offered?
- การติดตั้งทดลอง กิ่งไผ่ มีให้เล่นไหมและติดตั้งรุ่นไหน

**account_policy_id — known**
```json
"demo20_policy_15"
```
**game_id — known**
```json
"demo20_game_15"
```
**game_version — unknown**
```json
null
```
**installed_resource_ids — known**
```json
[
  "demo20_resource_15"
]
```
**offered — known**
```json
true
```
**service_id — known**
```json
"demo20_service_15"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_service/demo20_game_service_15.json)

### รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`)

รหัส `demo20_game_mode_15`

คำถามตัวอย่าง:

- โหมดทดลอง กิ่งไผ่ เล่นพร้อมกันได้สูงสุดกี่คน
- Demo mode Bamboo How many people can play together at most?
- โหมดทดลอง กิ่งไผ่ ต้องมีขั้นต่ำกี่คนและเล่นได้สูงสุดกี่คน

**game_id — known**
```json
"demo20_game_15"
```
**mode_name — known**
```json
{
  "en": "Demo mode Bamboo",
  "th": "โหมดทดลอง กิ่งไผ่"
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
2
```
**players_min — known**
```json
1
```
**studio_supported — known**
```json
true
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_mode/demo20_game_mode_15.json)

### วิธีเล่นและปุ่ม (`control_set`)

รหัส `demo20_control_set_15`

คำถามตัวอย่าง:

- ชุดควบคุมทดลอง กิ่งไผ่ ปุ่มอะไรบ้าง
- Demo controls Bamboo What are the controls?
- ชุดควบคุมทดลอง กิ่งไผ่ ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร

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
      "en": "Fictional input for Puzzle Box",
      "th": "คำสั่งสมมุติของ กล่องปริศนา"
    },
    "gesture": "press"
  }
]
```
**game_id — known**
```json
"demo20_game_15"
```
**game_version — known**
```json
"DEMO BUILD 15"
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
"DEMO_LAYOUT_15"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_15.json)

### ราคาต่อบริการ (`rate`)

รหัส `demo20_rate_15`

คำถามตัวอย่าง:

- อัตราทดลอง กิ่งไผ่ ราคาเท่าไหร่
- Demo tariff Bamboo How much does it cost?
- อัตราทดลอง กิ่งไผ่ ราคาเท่าไหร่และได้กี่นาที

**amount_minor — known**
```json
8000
```
**audience_id — known**
```json
"demo20_audience_15"
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
75
```
**persons_max — known**
```json
2
```
**persons_min — known**
```json
1
```
**service_id — known**
```json
"demo20_service_15"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rate/demo20_rate_15.json)

### ราคาเหมาโซน/ห้อง (`rental_package`)

รหัส `demo20_rental_package_15`

คำถามตัวอย่าง:

- แพ็กเกจทดลอง กิ่งไผ่ เหมาเท่าไหร่
- Demo package Bamboo How much is the rental?
- แพ็กเกจทดลอง กิ่งไผ่ ราคาเหมาเท่าไหร่และรวมอุปกรณ์อะไร

**amount_minor — known**
```json
25250
```
**audience_id — known**
```json
"demo20_audience_15"
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
  "en": "Fictional Bamboo station and PC inputs",
  "th": "เครื่องสมมุติ กิ่งไผ่ พร้อมอุปกรณ์ PC"
}
```
**name — known**
```json
{
  "en": "Demo package Bamboo",
  "th": "แพ็กเกจทดลอง กิ่งไผ่"
}
```
**period_label — known**
```json
"half_day"
```
**room_seats — known**
```json
4
```
**terms — known**
```json
{
  "en": "Synthetic package excludes extensions; 1–2 people per session",
  "th": "แพ็กเกจสมมุติไม่รวมค่าต่อเวลา; รอบละ 1–2 คน"
}
```
**zone_ids — known**
```json
[
  "demo20_zone_15"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rental_package/demo20_rental_package_15.json)

### ตารางบริการ (`schedule`)

รหัส `demo20_schedule_15`

คำถามตัวอย่าง:

- ตารางทดลอง กิ่งไผ่ จองช่วงไหนได้บ้าง
- Demo timetable Bamboo What are the booking hours?
- ตารางทดลอง กิ่งไผ่ เปิดช่วงไหนและพักบำรุงรักษาตอนไหน

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
  "en": "Synthetic Bamboo schedule with maintenance",
  "th": "ตารางสมมุติ กิ่งไผ่ มีพักบำรุงรักษา"
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
  "demo20_zone_15"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_15.json)

### วันปิด/ข้อยกเว้น (`closure`)

รหัส `demo20_closure_15`

คำถามตัวอย่าง:

- ประกาศวันทดลอง กิ่งไผ่ วันนั้นปิดไหม
- Demo date notice Bamboo Is it closed on that date?
- ประกาศวันทดลอง กิ่งไผ่ วันนั้นเปิดปิดยังไงและเพราะอะไร

**bookable_periods — known**
```json
[]
```
**local_date — known**
```json
"2026-12-15"
```
**open_periods — known**
```json
[]
```
**reason — known**
```json
{
  "en": "Synthetic Bamboo date notice: closed",
  "th": "ประกาศสมมุติ กิ่งไผ่: closed"
}
```
**resolution_policy_id — known**
```json
"demo20_policy_15"
```
**state — known**
```json
"closed"
```
**zone_ids — known**
```json
[
  "demo20_zone_15"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/closure/demo20_closure_15.json)

### รายการแข่งขันและฉบับกติกา (`competition`)

รหัส `demo20_competition_15`

คำถามตัวอย่าง:

- รายการฝึก กิ่งไผ่ ใช้กติกาฉบับไหน
- Demo event Bamboo Which rulebook release applies?
- รายการฝึก กิ่งไผ่ ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่

**competition_dates — known**
```json
[
  "2026-12-15"
]
```
**coverage — known**
```json
"partial"
```
**division — known**
```json
{
  "en": "Practice group 1–2 players",
  "th": "กลุ่มฝึก 1–2 คน"
}
```
**event_name — known**
```json
{
  "en": "Demo event Bamboo",
  "th": "รายการฝึก กิ่งไผ่"
}
```
**game_id — known**
```json
"demo20_game_15"
```
**rulebook_release — known**
```json
"DEMO20_REV_15"
```
**supersedes_id — not_applicable**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_15.json)

### ข้อกติกาการแข่งขัน (`competition_rule`)

รหัส `demo20_competition_rule_15`

คำถามตัวอย่าง:

- ข้อการแข่งขันทดลอง กิ่งไผ่ ข้อนี้กำหนดอะไร
- Demo rule Bamboo What does this rule require?
- ข้อการแข่งขันทดลอง กิ่งไผ่ กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม

**competition_id — known**
```json
"demo20_competition_15"
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
"pre_match_on_site"
```
**heading — known**
```json
{
  "en": "Demo rule Bamboo",
  "th": "ข้อการแข่งขันทดลอง กิ่งไผ่"
}
```
**section_number — known**
```json
"1.15"
```
**text — known**
```json
{
  "en": "Fictional clause 15: for Software installation, follow decision prohibited; exception requires written demo operator approval; not actual rules",
  "th": "ข้อสมมุติ 15: ติดตั้งโปรแกรม ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_15.json)

### ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`)

รหัส `demo20_news_15`

คำถามตัวอย่าง:

- ข่าวทดลอง กิ่งไผ่ ประกาศว่าอะไร
- Demo bulletin Bamboo What does the announcement say?
- ข่าวทดลอง กิ่งไผ่ ประกาศอะไรและกิจกรรมเริ่มจบเมื่อไหร่

**audience_ids — known**
```json
[
  "demo20_audience_15"
]
```
**body — known**
```json
{
  "en": "Synthetic bulletin: Puzzle Box activity for 1–2 people; no actual payment",
  "th": "ข่าวสมมุติ: กิจกรรมกล่องปริศนา สำหรับกลุ่ม 1–2 คน; ไม่มีรับเงินจริง"
}
```
**contact_id — known**
```json
"demo20_contact_15"
```
**event_end — known**
```json
"2026-12-15T12:00:00+07:00"
```
**event_start — known**
```json
"2026-12-15T10:00:00+07:00"
```
**registration_url — known**
```json
"https://example.invalid/demo20/register/15"
```
**title — known**
```json
{
  "en": "Demo bulletin Bamboo",
  "th": "ข่าวทดลอง กิ่งไผ่"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/news/demo20_news_15.json)

### บุคลากร/ทีมที่เปิดเผยได้ (`person`)

รหัส `demo20_person_15`

คำถามตัวอย่าง:

- ผู้ดูแลสมมุติ กิ่งไผ่ รับผิดชอบอะไร
- Fictional host Bamboo What is their role?
- ผู้ดูแลสมมุติ กิ่งไผ่ รับผิดชอบเรื่องอะไรและติดต่อทางไหน

**display_name — known**
```json
{
  "en": "Fictional host Bamboo",
  "th": "ผู้ดูแลสมมุติ กิ่งไผ่"
}
```
**public_contact_id — unknown**
```json
null
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
  "en": "Fictional host for Software installation",
  "th": "ผู้ดูแลสมมุติเรื่อง ติดตั้งโปรแกรม"
}
```
**team — known**
```json
{
  "en": "Demo Bamboo team",
  "th": "ทีมทดสอบ กิ่งไผ่"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/person/demo20_person_15.json)

### คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`)

รหัส `demo20_faq_15`

คำถามตัวอย่าง:

- คำถามตัวอย่าง กิ่งไผ่ คำตอบคืออะไร
- Demo enquiry Bamboo What is the answer?
- คำถามตัวอย่าง กิ่งไผ่ คำตอบคืออะไรและใช้กับกรณีไหน

**answer — known**
```json
{
  "en": "Example answer: Fictional rule for Software installation: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องติดตั้งโปรแกรม: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
}
```
**question — known**
```json
{
  "en": "Demo enquiry Bamboo",
  "th": "คำถามตัวอย่าง กิ่งไผ่"
}
```
**related_ids — known**
```json
[
  "demo20_policy_15",
  "demo20_procedure_15"
]
```
**scope_note — known**
```json
{
  "en": "Only applies to fictional Bamboo scenario",
  "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ กิ่งไผ่"
}
```
**topic — known**
```json
"DEMO Software installation"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_15.json)

### การเชื่อมสถานะสด (`live_binding`)

รหัส `demo20_live_binding_15`

คำถามตัวอย่าง:

- ตัวเชื่อมทดลอง กิ่งไผ่ จับคู่สถานะยังไง
- Demo binding Bamboo How are statuses mapped?
- ตัวเชื่อมทดลอง กิ่งไผ่ จับคู่สถานะแบบไหนและเก็บข้อมูลนานเท่าไหร่

**external_resource_key — known**
```json
"DEMO20_EXTERNAL_15"
```
**freshness_policy — known**
```json
{
  "en": "Synthetic TTL 90 seconds; no API call or live status claim",
  "th": "ค่าจำลอง TTL 90 วินาที; ไม่เรียก API และไม่ยืนยันสถานะสด"
}
```
**physical_pool_key — known**
```json
"demo20_pool_15"
```
**provider — known**
```json
"wordpress_booking"
```
**service_id — known**
```json
"demo20_service_15"
```
**status_mapping — known**
```json
[
  {
    "normalized": "free",
    "raw": "DEMO_EMPTY_15"
  },
  {
    "normalized": "occupied",
    "raw": "DEMO_BUSY_15"
  },
  {
    "normalized": "unknown",
    "raw": "DEMO_UNKNOWN_15"
  }
]
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/live_binding/demo20_live_binding_15.json)

