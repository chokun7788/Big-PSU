# ชุด 14 — แสงอรุณ / Dawn Light

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

เกม สถานที่ ราคา กฎ บุคคล และสถานะทั้งหมดในชุดใหม่นี้แต่งขึ้นเพื่อทดสอบ ไม่ได้เป็นข้อมูล PSU หรือเกมที่มีจำหน่ายจริง คำแปลยังไม่ผ่านมนุษย์

แพลตฟอร์มตัวอย่าง: Nintendo Switch • จำนวนผู้เล่น 1–4 • เวลาเล่น 45 นาที / กินช่องจอง 60 นาที

## ข้อมูลครบ 24 หมวด

### ข้อมูลศูนย์ (`center`)

รหัส `demo20_center_14`

คำถามตัวอย่าง:

- ศูนย์ทดลอง แสงอรุณ อยู่ตรงไหน
- Demo venue Dawn Light Where is it located?
- ศูนย์ทดลอง แสงอรุณ อยู่ตึกอะไร ชั้นไหน

**address — known**
```json
{
  "en": "Fictional address 98, Example Road, Test District",
  "th": "เลขที่สมมุติ 98 ถนนตัวอย่าง แขวงทดลอง"
}
```
**building — known**
```json
"DEMO Tower E"
```
**description — known**
```json
{
  "en": "Synthetic scenario 14: Rainbow Kitchen, not a real venue",
  "th": "สถานการณ์ทดลอง 14: ครัวสายรุ้ง ไม่ใช่สถานที่จริง"
}
```
**floor — known**
```json
"5"
```
**map_url — known**
```json
"https://example.invalid/demo20/map/14"
```
**name — known**
```json
{
  "en": "Demo venue Dawn Light",
  "th": "ศูนย์ทดลอง แสงอรุณ"
}
```
**operator — known**
```json
{
  "en": "Fictional Dawn Light operator",
  "th": "ผู้ประกอบการสมมุติ แสงอรุณ"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/center/demo20_center_14.json)

### โซนบริการ (`zone`)

รหัส `demo20_zone_14`

คำถามตัวอย่าง:

- โซนทดลอง แสงอรุณ มีที่นั่งกี่ที่
- Demo zone Dawn Light How many seats are there?
- โซนทดลอง แสงอรุณ โซนนี้อยู่ตรงไหนและมีที่นั่งกี่ที่

**description — known**
```json
{
  "en": "Synthetic Nintendo Switch zone for Rainbow Kitchen",
  "th": "โซนจำลอง Nintendo Switch สำหรับครัวสายรุ้ง"
}
```
**location — known**
```json
{
  "en": "Test building, floor 5, room 114",
  "th": "อาคารทดสอบ ชั้น 5 ห้อง 114"
}
```
**name — known**
```json
{
  "en": "Demo zone Dawn Light",
  "th": "โซนทดลอง แสงอรุณ"
}
```
**room_seats — known**
```json
8
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_14.json)

### รุ่นและสเปกอุปกรณ์ (`equipment_model`)

รหัส `demo20_equipment_model_14`

คำถามตัวอย่าง:

- รุ่นอุปกรณ์ แสงอรุณ สเปกมีอะไรบ้าง
- Demo model Dawn Light What are its specifications?
- รุ่นอุปกรณ์ แสงอรุณ เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง

**device_type — known**
```json
"console"
```
**name — known**
```json
{
  "en": "Demo model Dawn Light",
  "th": "รุ่นอุปกรณ์ แสงอรุณ"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_14.json)

### เครื่องหรือทรัพยากรจริง (`resource`)

รหัส `demo20_resource_14`

คำถามตัวอย่าง:

- เครื่องทดลอง แสงอรุณ เล่นพร้อมกันได้กี่คน
- Demo station Dawn Light How many people can play at once?
- เครื่องทดลอง แสงอรุณ เครื่องยังใช้งานได้ไหมและรองรับกี่คน

**capacity_persons — known**
```json
4
```
**equipment_model_ids — known**
```json
[
  "demo20_equipment_model_14"
]
```
**name — known**
```json
{
  "en": "Demo station Dawn Light",
  "th": "เครื่องทดลอง แสงอรุณ"
}
```
**operational_status — known**
```json
"in_service"
```
**physical_pool_key — known**
```json
"demo20_pool_14"
```
**zone_id — known**
```json
"demo20_zone_14"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/resource/demo20_resource_14.json)

### รายการที่เลือกในระบบจอง (`service`)

รหัส `demo20_service_14`

คำถามตัวอย่าง:

- รอบทดลอง แสงอรุณ หนึ่งรอบเล่นได้กี่นาที
- Demo session Dawn Light How many minutes does one session last?
- รอบทดลอง แสงอรุณ เวลาเล่นกับเวลาที่กินช่องจองกี่นาที

**booking_product_key — known**
```json
"DEMO20_BOOKING_14"
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
  "en": "Demo session Dawn Light",
  "th": "รอบทดลอง แสงอรุณ"
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
  "demo20_resource_14"
]
```
**session_minutes — known**
```json
45
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_14.json)

### ข้อมูลเกม (`game`)

รหัส `demo20_game_14`

คำถามตัวอย่าง:

- เกมสมมุติ แสงอรุณ เล่นยังไง
- Fictional game Dawn Light How do I play it?
- เกมสมมุติ แสงอรุณ เกมเกี่ยวกับอะไรและเล่นยังไง

**age_rating — known**
```json
{
  "en": "Synthetic DEMO rating 9",
  "th": "เรตอายุสมมุติ DEMO 9"
}
```
**edition — known**
```json
"DEMO fiction revision 14"
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
  "en": "Split tasks to prepare fictional meals on time; follow the demonstration controls",
  "th": "แบ่งหน้าที่ทำอาหารสมมุติให้ทันเวลา; ใช้คำสั่งตามชุดควบคุมทดลอง"
}
```
**publisher_url — known**
```json
"https://example.invalid/demo20/fictional-game/14"
```
**summary — known**
```json
{
  "en": "Fictional test game: Split tasks to prepare fictional meals on time",
  "th": "เกมแต่งขึ้นเพื่อทดสอบ: แบ่งหน้าที่ทำอาหารสมมุติให้ทันเวลา"
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
  "en": "Fictional Rainbow Kitchen",
  "th": "เกมสมมุติ ครัวสายรุ้ง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_14.json)

### กลุ่มผู้ใช้ (`audience`)

รหัส `demo20_audience_14`

คำถามตัวอย่าง:

- กลุ่มผู้ใช้ แสงอรุณ ต้องใช้หลักฐานอะไร
- Demo visitors Dawn Light What proof is required?
- กลุ่มผู้ใช้ แสงอรุณ ใครใช้สิทธิ์กลุ่มนี้ได้และต้องแสดงหลักฐานอะไร

**eligibility — known**
```json
{
  "en": "Fictional group 14: demo sessions only",
  "th": "ผู้ใช้สมมุติกลุ่ม 14: ใช้บริการตามรอบทดลอง"
}
```
**name — known**
```json
{
  "en": "Demo visitors Dawn Light",
  "th": "กลุ่มผู้ใช้ แสงอรุณ"
}
```
**required_proofs — known**
```json
[
  "DEMO pass Dawn Light"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/audience/demo20_audience_14.json)

### ติดต่อ (`contact`)

รหัส `demo20_contact_14`

คำถามตัวอย่าง:

- ช่องทางช่วยเหลือ แสงอรุณ ติดต่อทางไหน
- Demo help channel Dawn Light How can I contact them?
- ช่องทางช่วยเหลือ แสงอรุณ ติดต่อที่ไหนและติดต่อได้ช่วงไหน

**channel — known**
```json
"phone"
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
  "en": "Fictional support for Photography",
  "th": "สอบถามสมมุติเรื่อง ถ่ายภาพ"
}
```
**value — known**
```json
"DEMO-NON-DIALABLE-14"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_14.json)

### ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`)

รหัส `demo20_procedure_14`

คำถามตัวอย่าง:

- ขั้นตอนทดลอง แสงอรุณ ต้องทำยังไงบ้าง
- Demo procedure Dawn Light What steps should I follow?
- ขั้นตอนทดลอง แสงอรุณ มีขั้นตอนอะไรและต้องใช้เอกสารอะไร

**deadline_minutes — known**
```json
60
```
**outcome — known**
```json
{
  "en": "Demo outcome: Photography checked",
  "th": "ผลทดสอบ: ตรวจสอบ ถ่ายภาพ เสร็จ"
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
  "DEMO pass Dawn Light"
]
```
**steps — known**
```json
[
  {
    "contact_id": null,
    "instruction": {
      "en": "Select the fictional Dawn Light service",
      "th": "เลือกบริการสมมุติ แสงอรุณ"
    },
    "order": 1
  },
  {
    "contact_id": "demo20_contact_14",
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
"DEMO Photography"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_14.json)

### นโยบายและกฎศูนย์ (`policy`)

รหัส `demo20_policy_14`

คำถามตัวอย่าง:

- ข้อกำหนดทดลอง แสงอรุณ กฎเป็นยังไง
- Demo policy Dawn Light What are the rules?
- ข้อกำหนดทดลอง แสงอรุณ อนุญาตไหมและมีข้อยกเว้นอะไร

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
  "en": "Fictional rule for Photography: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "กติกาสมมุติเรื่องถ่ายภาพ: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
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
"demo20_procedure_14"
```
**subject — known**
```json
{
  "en": "Demo policy Dawn Light",
  "th": "ข้อกำหนดทดลอง แสงอรุณ"
}
```
**topic — known**
```json
"DEMO Photography"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/policy/demo20_policy_14.json)

### สิ่งอำนวยความสะดวก (`facility`)

รหัส `demo20_facility_14`

คำถามตัวอย่าง:

- พื้นที่พัก แสงอรุณ อยู่ตรงไหนในร้าน
- Demo amenity Dawn Light Where in the venue is it?
- พื้นที่พัก แสงอรุณ อยู่ตรงไหนและคนที่ต้องการความช่วยเหลือเข้าใช้ยังไง

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
  "en": "Photo backdrop in demo room 114",
  "th": "ฉากถ่ายภาพ อยู่ห้องทดสอบ 114"
}
```
**name — known**
```json
{
  "en": "Demo amenity Dawn Light",
  "th": "พื้นที่พัก แสงอรุณ"
}
```
**usage_conditions — known**
```json
{
  "en": "Demo sessions only; may use while waiting",
  "th": "ใช้ตามรอบทดลอง; ใช้ได้ระหว่างรอ"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/facility/demo20_facility_14.json)

### เกมที่ศูนย์มีให้เล่นจริง (`game_service`)

รหัส `demo20_game_service_14`

คำถามตัวอย่าง:

- การติดตั้งทดลอง แสงอรุณ มีให้เล่นหรือยัง
- Demo installation Dawn Light Is this game offered?
- การติดตั้งทดลอง แสงอรุณ มีให้เล่นไหมและติดตั้งรุ่นไหน

**account_policy_id — known**
```json
"demo20_policy_14"
```
**game_id — known**
```json
"demo20_game_14"
```
**game_version — known**
```json
"DEMO BUILD 14"
```
**installed_resource_ids — known**
```json
[
  "demo20_resource_14"
]
```
**offered — known**
```json
true
```
**service_id — known**
```json
"demo20_service_14"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_service/demo20_game_service_14.json)

### รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`)

รหัส `demo20_game_mode_14`

คำถามตัวอย่าง:

- โหมดทดลอง แสงอรุณ เล่นพร้อมกันได้สูงสุดกี่คน
- Demo mode Dawn Light How many people can play together at most?
- โหมดทดลอง แสงอรุณ ต้องมีขั้นต่ำกี่คนและเล่นได้สูงสุดกี่คน

**game_id — known**
```json
"demo20_game_14"
```
**mode_name — known**
```json
{
  "en": "Demo mode Dawn Light",
  "th": "โหมดทดลอง แสงอรุณ"
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
1
```
**studio_supported — known**
```json
true
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_mode/demo20_game_mode_14.json)

### วิธีเล่นและปุ่ม (`control_set`)

รหัส `demo20_control_set_14`

คำถามตัวอย่าง:

- ชุดควบคุมทดลอง แสงอรุณ ปุ่มอะไรบ้าง
- Demo controls Dawn Light What are the controls?
- ชุดควบคุมทดลอง แสงอรุณ ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร

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
      "en": "Fictional input for Rainbow Kitchen",
      "th": "คำสั่งสมมุติของ ครัวสายรุ้ง"
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
      "en": "Fictional input for Rainbow Kitchen",
      "th": "คำสั่งสมมุติของ ครัวสายรุ้ง"
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
      "en": "Fictional input for Rainbow Kitchen",
      "th": "คำสั่งสมมุติของ ครัวสายรุ้ง"
    },
    "gesture": "press"
  }
]
```
**game_id — known**
```json
"demo20_game_14"
```
**game_version — known**
```json
"DEMO BUILD 14"
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
"DEMO_LAYOUT_14"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_14.json)

### ราคาต่อบริการ (`rate`)

รหัส `demo20_rate_14`

คำถามตัวอย่าง:

- อัตราทดลอง แสงอรุณ ราคาเท่าไหร่
- Demo tariff Dawn Light How much does it cost?
- อัตราทดลอง แสงอรุณ ราคาเท่าไหร่และได้กี่นาที

**amount_minor — known**
```json
5500
```
**audience_id — known**
```json
"demo20_audience_14"
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
45
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
"demo20_service_14"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rate/demo20_rate_14.json)

### ราคาเหมาโซน/ห้อง (`rental_package`)

รหัส `demo20_rental_package_14`

คำถามตัวอย่าง:

- แพ็กเกจทดลอง แสงอรุณ เหมาเท่าไหร่
- Demo package Dawn Light How much is the rental?
- แพ็กเกจทดลอง แสงอรุณ ราคาเหมาเท่าไหร่และรวมอุปกรณ์อะไร

**amount_minor — known**
```json
17750
```
**audience_id — known**
```json
"demo20_audience_14"
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
  "en": "Fictional Dawn Light station and Nintendo Switch inputs",
  "th": "เครื่องสมมุติ แสงอรุณ พร้อมอุปกรณ์ Nintendo Switch"
}
```
**name — known**
```json
{
  "en": "Demo package Dawn Light",
  "th": "แพ็กเกจทดลอง แสงอรุณ"
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
  "demo20_zone_14"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rental_package/demo20_rental_package_14.json)

### ตารางบริการ (`schedule`)

รหัส `demo20_schedule_14`

คำถามตัวอย่าง:

- ตารางทดลอง แสงอรุณ จองช่วงไหนได้บ้าง
- Demo timetable Dawn Light What are the booking hours?
- ตารางทดลอง แสงอรุณ เปิดช่วงไหนและพักบำรุงรักษาตอนไหน

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
  "en": "Synthetic Dawn Light schedule with maintenance",
  "th": "ตารางสมมุติ แสงอรุณ มีพักบำรุงรักษา"
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
  "demo20_zone_14"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_14.json)

### วันปิด/ข้อยกเว้น (`closure`)

รหัส `demo20_closure_14`

คำถามตัวอย่าง:

- ประกาศวันทดลอง แสงอรุณ วันนั้นปิดไหม
- Demo date notice Dawn Light Is it closed on that date?
- ประกาศวันทดลอง แสงอรุณ วันนั้นเปิดปิดยังไงและเพราะอะไร

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
"2026-12-14"
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
  "en": "Synthetic Dawn Light date notice: open_override",
  "th": "ประกาศสมมุติ แสงอรุณ: open_override"
}
```
**resolution_policy_id — known**
```json
"demo20_policy_14"
```
**state — known**
```json
"open_override"
```
**zone_ids — known**
```json
[
  "demo20_zone_14"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/closure/demo20_closure_14.json)

### รายการแข่งขันและฉบับกติกา (`competition`)

รหัส `demo20_competition_14`

คำถามตัวอย่าง:

- รายการฝึก แสงอรุณ ใช้กติกาฉบับไหน
- Demo event Dawn Light Which rulebook release applies?
- รายการฝึก แสงอรุณ ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่

**competition_dates — known**
```json
[
  "2026-12-14"
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
  "en": "Demo event Dawn Light",
  "th": "รายการฝึก แสงอรุณ"
}
```
**game_id — known**
```json
"demo20_game_14"
```
**rulebook_release — known**
```json
"DEMO20_REV_14"
```
**supersedes_id — not_applicable**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_14.json)

### ข้อกติกาการแข่งขัน (`competition_rule`)

รหัส `demo20_competition_rule_14`

คำถามตัวอย่าง:

- ข้อการแข่งขันทดลอง แสงอรุณ ข้อนี้กำหนดอะไร
- Demo rule Dawn Light What does this rule require?
- ข้อการแข่งขันทดลอง แสงอรุณ กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม

**competition_id — known**
```json
"demo20_competition_14"
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
"match_configuration"
```
**heading — known**
```json
{
  "en": "Demo rule Dawn Light",
  "th": "ข้อการแข่งขันทดลอง แสงอรุณ"
}
```
**section_number — known**
```json
"5.14"
```
**text — known**
```json
{
  "en": "Fictional clause 14: for Photography, follow decision conditional; exception requires written demo operator approval; not actual rules",
  "th": "ข้อสมมุติ 14: ถ่ายภาพ ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_14.json)

### ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`)

รหัส `demo20_news_14`

คำถามตัวอย่าง:

- ข่าวทดลอง แสงอรุณ ประกาศว่าอะไร
- Demo bulletin Dawn Light What does the announcement say?
- ข่าวทดลอง แสงอรุณ ประกาศอะไรและกิจกรรมเริ่มจบเมื่อไหร่

**audience_ids — known**
```json
[
  "demo20_audience_14"
]
```
**body — known**
```json
{
  "en": "Synthetic bulletin: Rainbow Kitchen activity for 1–4 people; no actual payment",
  "th": "ข่าวสมมุติ: กิจกรรมครัวสายรุ้ง สำหรับกลุ่ม 1–4 คน; ไม่มีรับเงินจริง"
}
```
**contact_id — known**
```json
"demo20_contact_14"
```
**event_end — known**
```json
"2026-12-14T12:00:00+07:00"
```
**event_start — known**
```json
"2026-12-14T10:00:00+07:00"
```
**registration_url — known**
```json
"https://example.invalid/demo20/register/14"
```
**title — known**
```json
{
  "en": "Demo bulletin Dawn Light",
  "th": "ข่าวทดลอง แสงอรุณ"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/news/demo20_news_14.json)

### บุคลากร/ทีมที่เปิดเผยได้ (`person`)

รหัส `demo20_person_14`

คำถามตัวอย่าง:

- ผู้ดูแลสมมุติ แสงอรุณ รับผิดชอบอะไร
- Fictional host Dawn Light What is their role?
- ผู้ดูแลสมมุติ แสงอรุณ รับผิดชอบเรื่องอะไรและติดต่อทางไหน

**display_name — known**
```json
{
  "en": "Fictional host Dawn Light",
  "th": "ผู้ดูแลสมมุติ แสงอรุณ"
}
```
**public_contact_id — known**
```json
"demo20_contact_14"
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
  "en": "Fictional host for Photography",
  "th": "ผู้ดูแลสมมุติเรื่อง ถ่ายภาพ"
}
```
**team — known**
```json
{
  "en": "Demo Dawn Light team",
  "th": "ทีมทดสอบ แสงอรุณ"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/person/demo20_person_14.json)

### คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`)

รหัส `demo20_faq_14`

คำถามตัวอย่าง:

- คำถามตัวอย่าง แสงอรุณ คำตอบคืออะไร
- Demo enquiry Dawn Light What is the answer?
- คำถามตัวอย่าง แสงอรุณ คำตอบคืออะไรและใช้กับกรณีไหน

**answer — known**
```json
{
  "en": "Example answer: Fictional rule for Photography: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องถ่ายภาพ: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
}
```
**question — known**
```json
{
  "en": "Demo enquiry Dawn Light",
  "th": "คำถามตัวอย่าง แสงอรุณ"
}
```
**related_ids — known**
```json
[
  "demo20_policy_14",
  "demo20_procedure_14"
]
```
**scope_note — known**
```json
{
  "en": "Only applies to fictional Dawn Light scenario",
  "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ แสงอรุณ"
}
```
**topic — known**
```json
"DEMO Photography"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_14.json)

### การเชื่อมสถานะสด (`live_binding`)

รหัส `demo20_live_binding_14`

คำถามตัวอย่าง:

- ตัวเชื่อมทดลอง แสงอรุณ จับคู่สถานะยังไง
- Demo binding Dawn Light How are statuses mapped?
- ตัวเชื่อมทดลอง แสงอรุณ จับคู่สถานะแบบไหนและเก็บข้อมูลนานเท่าไหร่

**external_resource_key — known**
```json
"DEMO20_EXTERNAL_14"
```
**freshness_policy — known**
```json
{
  "en": "Synthetic TTL 85 seconds; no API call or live status claim",
  "th": "ค่าจำลอง TTL 85 วินาที; ไม่เรียก API และไม่ยืนยันสถานะสด"
}
```
**physical_pool_key — known**
```json
"demo20_pool_14"
```
**provider — known**
```json
"wordpress_booking"
```
**service_id — known**
```json
"demo20_service_14"
```
**status_mapping — known**
```json
[
  {
    "normalized": "free",
    "raw": "DEMO_EMPTY_14"
  },
  {
    "normalized": "occupied",
    "raw": "DEMO_BUSY_14"
  },
  {
    "normalized": "unknown",
    "raw": "DEMO_UNKNOWN_14"
  }
]
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/live_binding/demo20_live_binding_14.json)

