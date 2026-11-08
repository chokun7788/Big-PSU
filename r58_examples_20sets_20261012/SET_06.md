# ชุด 06 — ปะการัง / Coral

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

เกม สถานที่ ราคา กฎ บุคคล และสถานะทั้งหมดในชุดใหม่นี้แต่งขึ้นเพื่อทดสอบ ไม่ได้เป็นข้อมูล PSU หรือเกมที่มีจำหน่ายจริง คำแปลยังไม่ผ่านมนุษย์

แพลตฟอร์มตัวอย่าง: Nintendo Switch • จำนวนผู้เล่น 2–4 • เวลาเล่น 120 นาที / กินช่องจอง 120 นาที

## ข้อมูลครบ 24 หมวด

### ข้อมูลศูนย์ (`center`)

รหัส `demo20_center_06`

คำถามตัวอย่าง:

- ศูนย์ทดลอง ปะการัง อยู่ตรงไหน
- Demo venue Coral Where is it located?
- ศูนย์ทดลอง ปะการัง อยู่ตึกอะไร ชั้นไหน

**address — known**
```json
{
  "en": "Fictional address 42, Example Road, Test District",
  "th": "เลขที่สมมุติ 42 ถนนตัวอย่าง แขวงทดลอง"
}
```
**building — known**
```json
"DEMO Tower B"
```
**description — known**
```json
{
  "en": "Synthetic scenario 6: Friend Bridge, not a real venue",
  "th": "สถานการณ์ทดลอง 6: สะพานเพื่อน ไม่ใช่สถานที่จริง"
}
```
**floor — known**
```json
"2"
```
**map_url — known**
```json
"https://example.invalid/demo20/map/6"
```
**name — known**
```json
{
  "en": "Demo venue Coral",
  "th": "ศูนย์ทดลอง ปะการัง"
}
```
**operator — known**
```json
{
  "en": "Fictional Coral operator",
  "th": "ผู้ประกอบการสมมุติ ปะการัง"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/center/demo20_center_06.json)

### โซนบริการ (`zone`)

รหัส `demo20_zone_06`

คำถามตัวอย่าง:

- โซนทดลอง ปะการัง มีที่นั่งกี่ที่
- Demo zone Coral How many seats are there?
- โซนทดลอง ปะการัง โซนนี้อยู่ตรงไหนและมีที่นั่งกี่ที่

**description — known**
```json
{
  "en": "Synthetic Nintendo Switch zone for Friend Bridge",
  "th": "โซนจำลอง Nintendo Switch สำหรับสะพานเพื่อน"
}
```
**location — known**
```json
{
  "en": "Test building, floor 2, room 106",
  "th": "อาคารทดสอบ ชั้น 2 ห้อง 106"
}
```
**name — known**
```json
{
  "en": "Demo zone Coral",
  "th": "โซนทดลอง ปะการัง"
}
```
**room_seats — known**
```json
6
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_06.json)

### รุ่นและสเปกอุปกรณ์ (`equipment_model`)

รหัส `demo20_equipment_model_06`

คำถามตัวอย่าง:

- รุ่นอุปกรณ์ ปะการัง สเปกมีอะไรบ้าง
- Demo model Coral What are its specifications?
- รุ่นอุปกรณ์ ปะการัง เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง

**device_type — known**
```json
"console"
```
**name — known**
```json
{
  "en": "Demo model Coral",
  "th": "รุ่นอุปกรณ์ ปะการัง"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_06.json)

### เครื่องหรือทรัพยากรจริง (`resource`)

รหัส `demo20_resource_06`

คำถามตัวอย่าง:

- เครื่องทดลอง ปะการัง เล่นพร้อมกันได้กี่คน
- Demo station Coral How many people can play at once?
- เครื่องทดลอง ปะการัง เครื่องยังใช้งานได้ไหมและรองรับกี่คน

**capacity_persons — known**
```json
4
```
**equipment_model_ids — known**
```json
[
  "demo20_equipment_model_06"
]
```
**name — known**
```json
{
  "en": "Demo station Coral",
  "th": "เครื่องทดลอง ปะการัง"
}
```
**operational_status — known**
```json
"in_service"
```
**physical_pool_key — known**
```json
"demo20_pool_06"
```
**zone_id — known**
```json
"demo20_zone_06"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/resource/demo20_resource_06.json)

### รายการที่เลือกในระบบจอง (`service`)

รหัส `demo20_service_06`

คำถามตัวอย่าง:

- รอบทดลอง ปะการัง หนึ่งรอบเล่นได้กี่นาที
- Demo session Coral How many minutes does one session last?
- รอบทดลอง ปะการัง เวลาเล่นกับเวลาที่กินช่องจองกี่นาที

**booking_product_key — known**
```json
"DEMO20_BOOKING_06"
```
**capacity_max — known**
```json
4
```
**capacity_min — known**
```json
2
```
**name — known**
```json
{
  "en": "Demo session Coral",
  "th": "รอบทดลอง ปะการัง"
}
```
**occupancy_minutes — known**
```json
120
```
**platform — known**
```json
"Nintendo Switch"
```
**resource_ids — known**
```json
[
  "demo20_resource_06"
]
```
**session_minutes — known**
```json
120
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_06.json)

### ข้อมูลเกม (`game`)

รหัส `demo20_game_06`

คำถามตัวอย่าง:

- เกมสมมุติ ปะการัง เล่นยังไง
- Fictional game Coral How do I play it?
- เกมสมมุติ ปะการัง เกมเกี่ยวกับอะไรและเล่นยังไง

**age_rating — known**
```json
{
  "en": "Synthetic DEMO rating 9",
  "th": "เรตอายุสมมุติ DEMO 9"
}
```
**edition — known**
```json
"DEMO fiction revision 6"
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
  "en": "Place bridges together to cross a river; follow the demonstration controls",
  "th": "ร่วมกันวางสะพานให้ตัวละครข้ามแม่น้ำ; ใช้คำสั่งตามชุดควบคุมทดลอง"
}
```
**publisher_url — known**
```json
"https://example.invalid/demo20/fictional-game/6"
```
**summary — known**
```json
{
  "en": "Fictional test game: Place bridges together to cross a river",
  "th": "เกมแต่งขึ้นเพื่อทดสอบ: ร่วมกันวางสะพานให้ตัวละครข้ามแม่น้ำ"
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
  "en": "Fictional Friend Bridge",
  "th": "เกมสมมุติ สะพานเพื่อน"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_06.json)

### กลุ่มผู้ใช้ (`audience`)

รหัส `demo20_audience_06`

คำถามตัวอย่าง:

- กลุ่มผู้ใช้ ปะการัง ต้องใช้หลักฐานอะไร
- Demo visitors Coral What proof is required?
- กลุ่มผู้ใช้ ปะการัง ใครใช้สิทธิ์กลุ่มนี้ได้และต้องแสดงหลักฐานอะไร

**eligibility — known**
```json
{
  "en": "Fictional group 6: demo sessions only",
  "th": "ผู้ใช้สมมุติกลุ่ม 6: ใช้บริการตามรอบทดลอง"
}
```
**name — known**
```json
{
  "en": "Demo visitors Coral",
  "th": "กลุ่มผู้ใช้ ปะการัง"
}
```
**required_proofs — known**
```json
[
  "DEMO pass Coral"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/audience/demo20_audience_06.json)

### ติดต่อ (`contact`)

รหัส `demo20_contact_06`

คำถามตัวอย่าง:

- ช่องทางช่วยเหลือ ปะการัง ติดต่อทางไหน
- Demo help channel Coral How can I contact them?
- ช่องทางช่วยเหลือ ปะการัง ติดต่อที่ไหนและติดต่อได้ช่วงไหน

**channel — known**
```json
"email"
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
  "en": "Fictional support for Food in the zone",
  "th": "สอบถามสมมุติเรื่อง อาหารในโซน"
}
```
**value — known**
```json
"fiction06@example.invalid"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_06.json)

### ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`)

รหัส `demo20_procedure_06`

คำถามตัวอย่าง:

- ขั้นตอนทดลอง ปะการัง ต้องทำยังไงบ้าง
- Demo procedure Coral What steps should I follow?
- ขั้นตอนทดลอง ปะการัง มีขั้นตอนอะไรและต้องใช้เอกสารอะไร

**deadline_minutes — known**
```json
10
```
**outcome — known**
```json
{
  "en": "Demo outcome: Food in the zone checked",
  "th": "ผลทดสอบ: ตรวจสอบ อาหารในโซน เสร็จ"
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
  "DEMO pass Coral"
]
```
**steps — known**
```json
[
  {
    "contact_id": null,
    "instruction": {
      "en": "Select the fictional Coral service",
      "th": "เลือกบริการสมมุติ ปะการัง"
    },
    "order": 1
  },
  {
    "contact_id": "demo20_contact_06",
    "instruction": {
      "en": "Check names and conditions before confirming",
      "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
    },
    "order": 2
  },
  {
    "contact_id": "demo20_contact_06",
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
"DEMO Food in the zone"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_06.json)

### นโยบายและกฎศูนย์ (`policy`)

รหัส `demo20_policy_06`

คำถามตัวอย่าง:

- ข้อกำหนดทดลอง ปะการัง กฎเป็นยังไง
- Demo policy Coral What are the rules?
- ข้อกำหนดทดลอง ปะการัง อนุญาตไหมและมีข้อยกเว้นอะไร

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
  "en": "Fictional rule for Food in the zone: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "กติกาสมมุติเรื่องอาหารในโซน: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
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
"demo20_procedure_06"
```
**subject — known**
```json
{
  "en": "Demo policy Coral",
  "th": "ข้อกำหนดทดลอง ปะการัง"
}
```
**topic — known**
```json
"DEMO Food in the zone"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/policy/demo20_policy_06.json)

### สิ่งอำนวยความสะดวก (`facility`)

รหัส `demo20_facility_06`

คำถามตัวอย่าง:

- พื้นที่พัก ปะการัง อยู่ตรงไหนในร้าน
- Demo amenity Coral Where in the venue is it?
- พื้นที่พัก ปะการัง อยู่ตรงไหนและคนที่ต้องการความช่วยเหลือเข้าใช้ยังไง

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
  "en": "Food storage point in demo room 106",
  "th": "จุดฝากอาหาร อยู่ห้องทดสอบ 106"
}
```
**name — known**
```json
{
  "en": "Demo amenity Coral",
  "th": "พื้นที่พัก ปะการัง"
}
```
**usage_conditions — known**
```json
{
  "en": "Demo sessions only; may use while waiting",
  "th": "ใช้ตามรอบทดลอง; ใช้ได้ระหว่างรอ"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/facility/demo20_facility_06.json)

### เกมที่ศูนย์มีให้เล่นจริง (`game_service`)

รหัส `demo20_game_service_06`

คำถามตัวอย่าง:

- การติดตั้งทดลอง ปะการัง มีให้เล่นหรือยัง
- Demo installation Coral Is this game offered?
- การติดตั้งทดลอง ปะการัง มีให้เล่นไหมและติดตั้งรุ่นไหน

**account_policy_id — known**
```json
"demo20_policy_06"
```
**game_id — known**
```json
"demo20_game_06"
```
**game_version — known**
```json
"DEMO BUILD 6"
```
**installed_resource_ids — known**
```json
[
  "demo20_resource_06"
]
```
**offered — known**
```json
true
```
**service_id — known**
```json
"demo20_service_06"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_service/demo20_game_service_06.json)

### รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`)

รหัส `demo20_game_mode_06`

คำถามตัวอย่าง:

- โหมดทดลอง ปะการัง เล่นพร้อมกันได้สูงสุดกี่คน
- Demo mode Coral How many people can play together at most?
- โหมดทดลอง ปะการัง ต้องมีขั้นต่ำกี่คนและเล่นได้สูงสุดกี่คน

**game_id — known**
```json
"demo20_game_06"
```
**mode_name — known**
```json
{
  "en": "Demo mode Coral",
  "th": "โหมดทดลอง ปะการัง"
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
"Nintendo Switch"
```
**players_max — known**
```json
4
```
**players_min — known**
```json
2
```
**studio_supported — known**
```json
true
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_mode/demo20_game_mode_06.json)

### วิธีเล่นและปุ่ม (`control_set`)

รหัส `demo20_control_set_06`

คำถามตัวอย่าง:

- ชุดควบคุมทดลอง ปะการัง ปุ่มอะไรบ้าง
- Demo controls Coral What are the controls?
- ชุดควบคุมทดลอง ปะการัง ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร

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
      "en": "Fictional input for Friend Bridge",
      "th": "คำสั่งสมมุติของ สะพานเพื่อน"
    },
    "gesture": "press"
  }
]
```
**game_id — known**
```json
"demo20_game_06"
```
**game_version — known**
```json
"DEMO BUILD 6"
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
"DEMO_LAYOUT_6"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_06.json)

### ราคาต่อบริการ (`rate`)

รหัส `demo20_rate_06`

คำถามตัวอย่าง:

- อัตราทดลอง ปะการัง ราคาเท่าไหร่
- Demo tariff Coral How much does it cost?
- อัตราทดลอง ปะการัง ราคาเท่าไหร่และได้กี่นาที

**amount_minor — known**
```json
18000
```
**audience_id — known**
```json
"demo20_audience_06"
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
2
```
**service_id — known**
```json
"demo20_service_06"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rate/demo20_rate_06.json)

### ราคาเหมาโซน/ห้อง (`rental_package`)

รหัส `demo20_rental_package_06`

คำถามตัวอย่าง:

- แพ็กเกจทดลอง ปะการัง เหมาเท่าไหร่
- Demo package Coral How much is the rental?
- แพ็กเกจทดลอง ปะการัง ราคาเหมาเท่าไหร่และรวมอุปกรณ์อะไร

**amount_minor — known**
```json
55250
```
**audience_id — known**
```json
"demo20_audience_06"
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
  "en": "Fictional Coral station and Nintendo Switch inputs",
  "th": "เครื่องสมมุติ ปะการัง พร้อมอุปกรณ์ Nintendo Switch"
}
```
**name — known**
```json
{
  "en": "Demo package Coral",
  "th": "แพ็กเกจทดลอง ปะการัง"
}
```
**period_label — known**
```json
"half_day"
```
**room_seats — known**
```json
6
```
**terms — known**
```json
{
  "en": "Synthetic package excludes extensions; 2–4 people per session",
  "th": "แพ็กเกจสมมุติไม่รวมค่าต่อเวลา; รอบละ 2–4 คน"
}
```
**zone_ids — known**
```json
[
  "demo20_zone_06"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rental_package/demo20_rental_package_06.json)

### ตารางบริการ (`schedule`)

รหัส `demo20_schedule_06`

คำถามตัวอย่าง:

- ตารางทดลอง ปะการัง จองช่วงไหนได้บ้าง
- Demo timetable Coral What are the booking hours?
- ตารางทดลอง ปะการัง เปิดช่วงไหนและพักบำรุงรักษาตอนไหน

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
  "en": "Synthetic Coral schedule with maintenance",
  "th": "ตารางสมมุติ ปะการัง มีพักบำรุงรักษา"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```
**weekday — known**
```json
6
```
**zone_ids — known**
```json
[
  "demo20_zone_06"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_06.json)

### วันปิด/ข้อยกเว้น (`closure`)

รหัส `demo20_closure_06`

คำถามตัวอย่าง:

- ประกาศวันทดลอง ปะการัง วันนั้นปิดไหม
- Demo date notice Coral Is it closed on that date?
- ประกาศวันทดลอง ปะการัง วันนั้นเปิดปิดยังไงและเพราะอะไร

**bookable_periods — known**
```json
[]
```
**local_date — known**
```json
"2026-12-06"
```
**open_periods — known**
```json
[]
```
**reason — known**
```json
{
  "en": "Synthetic Coral date notice: closed",
  "th": "ประกาศสมมุติ ปะการัง: closed"
}
```
**resolution_policy_id — known**
```json
"demo20_policy_06"
```
**state — known**
```json
"closed"
```
**zone_ids — known**
```json
[
  "demo20_zone_06"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/closure/demo20_closure_06.json)

### รายการแข่งขันและฉบับกติกา (`competition`)

รหัส `demo20_competition_06`

คำถามตัวอย่าง:

- รายการฝึก ปะการัง ใช้กติกาฉบับไหน
- Demo event Coral Which rulebook release applies?
- รายการฝึก ปะการัง ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่

**competition_dates — known**
```json
[
  "2026-12-06"
]
```
**coverage — known**
```json
"partial"
```
**division — known**
```json
{
  "en": "Practice group 2–4 players",
  "th": "กลุ่มฝึก 2–4 คน"
}
```
**event_name — known**
```json
{
  "en": "Demo event Coral",
  "th": "รายการฝึก ปะการัง"
}
```
**game_id — known**
```json
"demo20_game_06"
```
**rulebook_release — known**
```json
"DEMO20_REV_6"
```
**supersedes_id — not_applicable**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_06.json)

### ข้อกติกาการแข่งขัน (`competition_rule`)

รหัส `demo20_competition_rule_06`

คำถามตัวอย่าง:

- ข้อการแข่งขันทดลอง ปะการัง ข้อนี้กำหนดอะไร
- Demo rule Coral What does this rule require?
- ข้อการแข่งขันทดลอง ปะการัง กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม

**competition_id — known**
```json
"demo20_competition_06"
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
"in_match_operations"
```
**heading — known**
```json
{
  "en": "Demo rule Coral",
  "th": "ข้อการแข่งขันทดลอง ปะการัง"
}
```
**section_number — known**
```json
"2.6"
```
**text — known**
```json
{
  "en": "Fictional clause 6: for Food in the zone, follow decision prohibited; exception requires written demo operator approval; not actual rules",
  "th": "ข้อสมมุติ 6: อาหารในโซน ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_06.json)

### ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`)

รหัส `demo20_news_06`

คำถามตัวอย่าง:

- ข่าวทดลอง ปะการัง ประกาศว่าอะไร
- Demo bulletin Coral What does the announcement say?
- ข่าวทดลอง ปะการัง ประกาศอะไรและกิจกรรมเริ่มจบเมื่อไหร่

**audience_ids — known**
```json
[
  "demo20_audience_06"
]
```
**body — known**
```json
{
  "en": "Synthetic bulletin: Friend Bridge activity for 2–4 people; no actual payment",
  "th": "ข่าวสมมุติ: กิจกรรมสะพานเพื่อน สำหรับกลุ่ม 2–4 คน; ไม่มีรับเงินจริง"
}
```
**contact_id — known**
```json
"demo20_contact_06"
```
**event_end — known**
```json
"2026-12-06T12:00:00+07:00"
```
**event_start — known**
```json
"2026-12-06T10:00:00+07:00"
```
**registration_url — known**
```json
"https://example.invalid/demo20/register/6"
```
**title — known**
```json
{
  "en": "Demo bulletin Coral",
  "th": "ข่าวทดลอง ปะการัง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/news/demo20_news_06.json)

### บุคลากร/ทีมที่เปิดเผยได้ (`person`)

รหัส `demo20_person_06`

คำถามตัวอย่าง:

- ผู้ดูแลสมมุติ ปะการัง รับผิดชอบอะไร
- Fictional host Coral What is their role?
- ผู้ดูแลสมมุติ ปะการัง รับผิดชอบเรื่องอะไรและติดต่อทางไหน

**display_name — known**
```json
{
  "en": "Fictional host Coral",
  "th": "ผู้ดูแลสมมุติ ปะการัง"
}
```
**public_contact_id — known**
```json
"demo20_contact_06"
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
  "en": "Fictional host for Food in the zone",
  "th": "ผู้ดูแลสมมุติเรื่อง อาหารในโซน"
}
```
**team — known**
```json
{
  "en": "Demo Coral team",
  "th": "ทีมทดสอบ ปะการัง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/person/demo20_person_06.json)

### คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`)

รหัส `demo20_faq_06`

คำถามตัวอย่าง:

- คำถามตัวอย่าง ปะการัง คำตอบคืออะไร
- Demo enquiry Coral What is the answer?
- คำถามตัวอย่าง ปะการัง คำตอบคืออะไรและใช้กับกรณีไหน

**answer — known**
```json
{
  "en": "Example answer: Fictional rule for Food in the zone: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องอาหารในโซน: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
}
```
**question — known**
```json
{
  "en": "Demo enquiry Coral",
  "th": "คำถามตัวอย่าง ปะการัง"
}
```
**related_ids — known**
```json
[
  "demo20_policy_06",
  "demo20_procedure_06"
]
```
**scope_note — known**
```json
{
  "en": "Only applies to fictional Coral scenario",
  "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ปะการัง"
}
```
**topic — known**
```json
"DEMO Food in the zone"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_06.json)

### การเชื่อมสถานะสด (`live_binding`)

รหัส `demo20_live_binding_06`

คำถามตัวอย่าง:

- ตัวเชื่อมทดลอง ปะการัง จับคู่สถานะยังไง
- Demo binding Coral How are statuses mapped?
- ตัวเชื่อมทดลอง ปะการัง จับคู่สถานะแบบไหนและเก็บข้อมูลนานเท่าไหร่

**external_resource_key — known**
```json
"DEMO20_EXTERNAL_6"
```
**freshness_policy — known**
```json
{
  "en": "Synthetic TTL 45 seconds; no API call or live status claim",
  "th": "ค่าจำลอง TTL 45 วินาที; ไม่เรียก API และไม่ยืนยันสถานะสด"
}
```
**physical_pool_key — known**
```json
"demo20_pool_06"
```
**provider — known**
```json
"wordpress_booking"
```
**service_id — known**
```json
"demo20_service_06"
```
**status_mapping — known**
```json
[
  {
    "normalized": "free",
    "raw": "DEMO_EMPTY_6"
  },
  {
    "normalized": "occupied",
    "raw": "DEMO_BUSY_6"
  },
  {
    "normalized": "unknown",
    "raw": "DEMO_UNKNOWN_6"
  }
]
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/live_binding/demo20_live_binding_06.json)

