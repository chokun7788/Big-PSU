# ชุด 08 — ฟ้าหลังฝน / After Rain

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

เกม สถานที่ ราคา กฎ บุคคล และสถานะทั้งหมดในชุดใหม่นี้แต่งขึ้นเพื่อทดสอบ ไม่ได้เป็นข้อมูล PSU หรือเกมที่มีจำหน่ายจริง คำแปลยังไม่ผ่านมนุษย์

แพลตฟอร์มตัวอย่าง: PS5 • จำนวนผู้เล่น 1–2 • เวลาเล่น 30 นาที / กินช่องจอง 30 นาที

## ข้อมูลครบ 24 หมวด

### ข้อมูลศูนย์ (`center`)

รหัส `demo20_center_08`

คำถามตัวอย่าง:

- ศูนย์ทดลอง ฟ้าหลังฝน อยู่ตรงไหน
- Demo venue After Rain Where is it located?
- ศูนย์ทดลอง ฟ้าหลังฝน อยู่ตึกอะไร ชั้นไหน

**address — known**
```json
{
  "en": "Fictional address 56, Example Road, Test District",
  "th": "เลขที่สมมุติ 56 ถนนตัวอย่าง แขวงทดลอง"
}
```
**building — known**
```json
"DEMO Tower D"
```
**description — known**
```json
{
  "en": "Synthetic scenario 8: Letter Runner, not a real venue",
  "th": "สถานการณ์ทดลอง 8: ผู้ส่งจดหมาย ไม่ใช่สถานที่จริง"
}
```
**floor — known**
```json
"4"
```
**map_url — known**
```json
"https://example.invalid/demo20/map/8"
```
**name — known**
```json
{
  "en": "Demo venue After Rain",
  "th": "ศูนย์ทดลอง ฟ้าหลังฝน"
}
```
**operator — known**
```json
{
  "en": "Fictional After Rain operator",
  "th": "ผู้ประกอบการสมมุติ ฟ้าหลังฝน"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/center/demo20_center_08.json)

### โซนบริการ (`zone`)

รหัส `demo20_zone_08`

คำถามตัวอย่าง:

- โซนทดลอง ฟ้าหลังฝน มีที่นั่งกี่ที่
- Demo zone After Rain How many seats are there?
- โซนทดลอง ฟ้าหลังฝน โซนนี้อยู่ตรงไหนและมีที่นั่งกี่ที่

**description — known**
```json
{
  "en": "Synthetic PS5 zone for Letter Runner",
  "th": "โซนจำลอง PS5 สำหรับผู้ส่งจดหมาย"
}
```
**location — known**
```json
{
  "en": "Test building, floor 4, room 108",
  "th": "อาคารทดสอบ ชั้น 4 ห้อง 108"
}
```
**name — known**
```json
{
  "en": "Demo zone After Rain",
  "th": "โซนทดลอง ฟ้าหลังฝน"
}
```
**room_seats — known**
```json
6
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_08.json)

### รุ่นและสเปกอุปกรณ์ (`equipment_model`)

รหัส `demo20_equipment_model_08`

คำถามตัวอย่าง:

- รุ่นอุปกรณ์ ฟ้าหลังฝน สเปกมีอะไรบ้าง
- Demo model After Rain What are its specifications?
- รุ่นอุปกรณ์ ฟ้าหลังฝน เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง

**device_type — known**
```json
"console"
```
**name — known**
```json
{
  "en": "Demo model After Rain",
  "th": "รุ่นอุปกรณ์ ฟ้าหลังฝน"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_08.json)

### เครื่องหรือทรัพยากรจริง (`resource`)

รหัส `demo20_resource_08`

คำถามตัวอย่าง:

- เครื่องทดลอง ฟ้าหลังฝน เล่นพร้อมกันได้กี่คน
- Demo station After Rain How many people can play at once?
- เครื่องทดลอง ฟ้าหลังฝน เครื่องยังใช้งานได้ไหมและรองรับกี่คน

**capacity_persons — known**
```json
2
```
**equipment_model_ids — known**
```json
[
  "demo20_equipment_model_08"
]
```
**name — known**
```json
{
  "en": "Demo station After Rain",
  "th": "เครื่องทดลอง ฟ้าหลังฝน"
}
```
**operational_status — known**
```json
"in_service"
```
**physical_pool_key — known**
```json
"demo20_pool_08"
```
**zone_id — known**
```json
"demo20_zone_08"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/resource/demo20_resource_08.json)

### รายการที่เลือกในระบบจอง (`service`)

รหัส `demo20_service_08`

คำถามตัวอย่าง:

- รอบทดลอง ฟ้าหลังฝน หนึ่งรอบเล่นได้กี่นาที
- Demo session After Rain How many minutes does one session last?
- รอบทดลอง ฟ้าหลังฝน เวลาเล่นกับเวลาที่กินช่องจองกี่นาที

**booking_product_key — known**
```json
"DEMO20_BOOKING_08"
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
  "en": "Demo session After Rain",
  "th": "รอบทดลอง ฟ้าหลังฝน"
}
```
**occupancy_minutes — known**
```json
30
```
**platform — known**
```json
"PS5"
```
**resource_ids — known**
```json
[
  "demo20_resource_08"
]
```
**session_minutes — known**
```json
30
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_08.json)

### ข้อมูลเกม (`game`)

รหัส `demo20_game_08`

คำถามตัวอย่าง:

- เกมสมมุติ ฟ้าหลังฝน เล่นยังไง
- Fictional game After Rain How do I play it?
- เกมสมมุติ ฟ้าหลังฝน เกมเกี่ยวกับอะไรและเล่นยังไง

**age_rating — known**
```json
{
  "en": "Synthetic DEMO rating 3",
  "th": "เรตอายุสมมุติ DEMO 3"
}
```
**edition — known**
```json
"DEMO fiction revision 8"
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
  "en": "Deliver letters by selecting short routes; follow the demonstration controls",
  "th": "ส่งจดหมายให้ครบโดยเลือกเส้นทางสั้น; ใช้คำสั่งตามชุดควบคุมทดลอง"
}
```
**publisher_url — known**
```json
"https://example.invalid/demo20/fictional-game/8"
```
**summary — known**
```json
{
  "en": "Fictional test game: Deliver letters by selecting short routes",
  "th": "เกมแต่งขึ้นเพื่อทดสอบ: ส่งจดหมายให้ครบโดยเลือกเส้นทางสั้น"
}
```
**supported_platforms — known**
```json
[
  "PS5",
  "PC"
]
```
**title — known**
```json
{
  "en": "Fictional Letter Runner",
  "th": "เกมสมมุติ ผู้ส่งจดหมาย"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_08.json)

### กลุ่มผู้ใช้ (`audience`)

รหัส `demo20_audience_08`

คำถามตัวอย่าง:

- กลุ่มผู้ใช้ ฟ้าหลังฝน ต้องใช้หลักฐานอะไร
- Demo visitors After Rain What proof is required?
- กลุ่มผู้ใช้ ฟ้าหลังฝน ใครใช้สิทธิ์กลุ่มนี้ได้และต้องแสดงหลักฐานอะไร

**eligibility — known**
```json
{
  "en": "Fictional group 8: demo sessions only",
  "th": "ผู้ใช้สมมุติกลุ่ม 8: ใช้บริการตามรอบทดลอง"
}
```
**name — known**
```json
{
  "en": "Demo visitors After Rain",
  "th": "กลุ่มผู้ใช้ ฟ้าหลังฝน"
}
```
**required_proofs — known**
```json
[]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/audience/demo20_audience_08.json)

### ติดต่อ (`contact`)

รหัส `demo20_contact_08`

คำถามตัวอย่าง:

- ช่องทางช่วยเหลือ ฟ้าหลังฝน ติดต่อทางไหน
- Demo help channel After Rain How can I contact them?
- ช่องทางช่วยเหลือ ฟ้าหลังฝน ติดต่อที่ไหนและติดต่อได้ช่วงไหน

**channel — known**
```json
"website"
```
**office_hours — known**
```json
{
  "en": "Demo hours 08:00–17:00",
  "th": "ช่วงทดลอง 08:00–17:00"
}
```
**purpose — known**
```json
{
  "en": "Fictional support for Player accounts",
  "th": "สอบถามสมมุติเรื่อง บัญชีผู้เล่น"
}
```
**value — known**
```json
"https://example.invalid/demo20/contact/8"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_08.json)

### ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`)

รหัส `demo20_procedure_08`

คำถามตัวอย่าง:

- ขั้นตอนทดลอง ฟ้าหลังฝน ต้องทำยังไงบ้าง
- Demo procedure After Rain What steps should I follow?
- ขั้นตอนทดลอง ฟ้าหลังฝน มีขั้นตอนอะไรและต้องใช้เอกสารอะไร

**deadline_minutes — known**
```json
30
```
**outcome — known**
```json
{
  "en": "Demo outcome: Player accounts checked",
  "th": "ผลทดสอบ: ตรวจสอบ บัญชีผู้เล่น เสร็จ"
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
[]
```
**steps — known**
```json
[
  {
    "contact_id": null,
    "instruction": {
      "en": "Select the fictional After Rain service",
      "th": "เลือกบริการสมมุติ ฟ้าหลังฝน"
    },
    "order": 1
  },
  {
    "contact_id": "demo20_contact_08",
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
"DEMO Player accounts"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_08.json)

### นโยบายและกฎศูนย์ (`policy`)

รหัส `demo20_policy_08`

คำถามตัวอย่าง:

- ข้อกำหนดทดลอง ฟ้าหลังฝน กฎเป็นยังไง
- Demo policy After Rain What are the rules?
- ข้อกำหนดทดลอง ฟ้าหลังฝน อนุญาตไหมและมีข้อยกเว้นอะไร

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
  "en": "Fictional rule for Player accounts: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "กติกาสมมุติเรื่องบัญชีผู้เล่น: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
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
"demo20_procedure_08"
```
**subject — known**
```json
{
  "en": "Demo policy After Rain",
  "th": "ข้อกำหนดทดลอง ฟ้าหลังฝน"
}
```
**topic — known**
```json
"DEMO Player accounts"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/policy/demo20_policy_08.json)

### สิ่งอำนวยความสะดวก (`facility`)

รหัส `demo20_facility_08`

คำถามตัวอย่าง:

- พื้นที่พัก ฟ้าหลังฝน อยู่ตรงไหนในร้าน
- Demo amenity After Rain Where in the venue is it?
- พื้นที่พัก ฟ้าหลังฝน อยู่ตรงไหนและคนที่ต้องการความช่วยเหลือเข้าใช้ยังไง

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
  "en": "Account help counter in demo room 108",
  "th": "เคาน์เตอร์บัญชี อยู่ห้องทดสอบ 108"
}
```
**name — known**
```json
{
  "en": "Demo amenity After Rain",
  "th": "พื้นที่พัก ฟ้าหลังฝน"
}
```
**usage_conditions — known**
```json
{
  "en": "Demo sessions only; may use while waiting",
  "th": "ใช้ตามรอบทดลอง; ใช้ได้ระหว่างรอ"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/facility/demo20_facility_08.json)

### เกมที่ศูนย์มีให้เล่นจริง (`game_service`)

รหัส `demo20_game_service_08`

คำถามตัวอย่าง:

- การติดตั้งทดลอง ฟ้าหลังฝน มีให้เล่นหรือยัง
- Demo installation After Rain Is this game offered?
- การติดตั้งทดลอง ฟ้าหลังฝน มีให้เล่นไหมและติดตั้งรุ่นไหน

**account_policy_id — known**
```json
"demo20_policy_08"
```
**game_id — known**
```json
"demo20_game_08"
```
**game_version — known**
```json
"DEMO BUILD 8"
```
**installed_resource_ids — known**
```json
[]
```
**offered — known**
```json
false
```
**service_id — known**
```json
"demo20_service_08"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_service/demo20_game_service_08.json)

### รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`)

รหัส `demo20_game_mode_08`

คำถามตัวอย่าง:

- โหมดทดลอง ฟ้าหลังฝน เล่นพร้อมกันได้สูงสุดกี่คน
- Demo mode After Rain How many people can play together at most?
- โหมดทดลอง ฟ้าหลังฝน ต้องมีขั้นต่ำกี่คนและเล่นได้สูงสุดกี่คน

**game_id — known**
```json
"demo20_game_08"
```
**mode_name — known**
```json
{
  "en": "Demo mode After Rain",
  "th": "โหมดทดลอง ฟ้าหลังฝน"
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
1
```
**studio_supported — known**
```json
false
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_mode/demo20_game_mode_08.json)

### วิธีเล่นและปุ่ม (`control_set`)

รหัส `demo20_control_set_08`

คำถามตัวอย่าง:

- ชุดควบคุมทดลอง ฟ้าหลังฝน ปุ่มอะไรบ้าง
- Demo controls After Rain What are the controls?
- ชุดควบคุมทดลอง ฟ้าหลังฝน ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร

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
      "en": "Fictional input for Letter Runner",
      "th": "คำสั่งสมมุติของ ผู้ส่งจดหมาย"
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
      "en": "Fictional input for Letter Runner",
      "th": "คำสั่งสมมุติของ ผู้ส่งจดหมาย"
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
      "en": "Fictional input for Letter Runner",
      "th": "คำสั่งสมมุติของ ผู้ส่งจดหมาย"
    },
    "gesture": "press"
  }
]
```
**game_id — known**
```json
"demo20_game_08"
```
**game_version — known**
```json
"DEMO BUILD 8"
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
"DEMO_LAYOUT_8"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_08.json)

### ราคาต่อบริการ (`rate`)

รหัส `demo20_rate_08`

คำถามตัวอย่าง:

- อัตราทดลอง ฟ้าหลังฝน ราคาเท่าไหร่
- Demo tariff After Rain How much does it cost?
- อัตราทดลอง ฟ้าหลังฝน ราคาเท่าไหร่และได้กี่นาที

**amount_minor — known**
```json
3500
```
**audience_id — known**
```json
"demo20_audience_08"
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
2
```
**persons_min — known**
```json
1
```
**service_id — known**
```json
"demo20_service_08"
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
"per_session"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rate/demo20_rate_08.json)

### ราคาเหมาโซน/ห้อง (`rental_package`)

รหัส `demo20_rental_package_08`

คำถามตัวอย่าง:

- แพ็กเกจทดลอง ฟ้าหลังฝน เหมาเท่าไหร่
- Demo package After Rain How much is the rental?
- แพ็กเกจทดลอง ฟ้าหลังฝน ราคาเหมาเท่าไหร่และรวมอุปกรณ์อะไร

**amount_minor — known**
```json
11750
```
**audience_id — known**
```json
"demo20_audience_08"
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
  "en": "Fictional After Rain station and PS5 inputs",
  "th": "เครื่องสมมุติ ฟ้าหลังฝน พร้อมอุปกรณ์ PS5"
}
```
**name — known**
```json
{
  "en": "Demo package After Rain",
  "th": "แพ็กเกจทดลอง ฟ้าหลังฝน"
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
  "en": "Synthetic package excludes extensions; 1–2 people per session",
  "th": "แพ็กเกจสมมุติไม่รวมค่าต่อเวลา; รอบละ 1–2 คน"
}
```
**zone_ids — known**
```json
[
  "demo20_zone_08"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rental_package/demo20_rental_package_08.json)

### ตารางบริการ (`schedule`)

รหัส `demo20_schedule_08`

คำถามตัวอย่าง:

- ตารางทดลอง ฟ้าหลังฝน จองช่วงไหนได้บ้าง
- Demo timetable After Rain What are the booking hours?
- ตารางทดลอง ฟ้าหลังฝน เปิดช่วงไหนและพักบำรุงรักษาตอนไหน

**bookable_periods — known**
```json
[
  {
    "end": "17:00",
    "start": "08:00"
  }
]
```
**maintenance_periods — known**
```json
[]
```
**open_periods — known**
```json
[
  {
    "end": "17:00",
    "start": "08:00"
  }
]
```
**reason — known**
```json
{
  "en": "Synthetic After Rain schedule without maintenance",
  "th": "ตารางสมมุติ ฟ้าหลังฝน ไม่มีพักบำรุงรักษา"
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
  "demo20_zone_08"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_08.json)

### วันปิด/ข้อยกเว้น (`closure`)

รหัส `demo20_closure_08`

คำถามตัวอย่าง:

- ประกาศวันทดลอง ฟ้าหลังฝน วันนั้นปิดไหม
- Demo date notice After Rain Is it closed on that date?
- ประกาศวันทดลอง ฟ้าหลังฝน วันนั้นเปิดปิดยังไงและเพราะอะไร

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
"2026-12-08"
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
  "en": "Synthetic After Rain date notice: open_override",
  "th": "ประกาศสมมุติ ฟ้าหลังฝน: open_override"
}
```
**resolution_policy_id — known**
```json
"demo20_policy_08"
```
**state — known**
```json
"open_override"
```
**zone_ids — known**
```json
[
  "demo20_zone_08"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/closure/demo20_closure_08.json)

### รายการแข่งขันและฉบับกติกา (`competition`)

รหัส `demo20_competition_08`

คำถามตัวอย่าง:

- รายการฝึก ฟ้าหลังฝน ใช้กติกาฉบับไหน
- Demo event After Rain Which rulebook release applies?
- รายการฝึก ฟ้าหลังฝน ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่

**competition_dates — known**
```json
[
  "2026-12-08"
]
```
**coverage — known**
```json
"complete"
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
  "en": "Demo event After Rain",
  "th": "รายการฝึก ฟ้าหลังฝน"
}
```
**game_id — known**
```json
"demo20_game_08"
```
**rulebook_release — known**
```json
"DEMO20_REV_8"
```
**supersedes_id — not_applicable**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_08.json)

### ข้อกติกาการแข่งขัน (`competition_rule`)

รหัส `demo20_competition_rule_08`

คำถามตัวอย่าง:

- ข้อการแข่งขันทดลอง ฟ้าหลังฝน ข้อนี้กำหนดอะไร
- Demo rule After Rain What does this rule require?
- ข้อการแข่งขันทดลอง ฟ้าหลังฝน กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม

**competition_id — known**
```json
"demo20_competition_08"
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
"penalty_matrix"
```
**heading — known**
```json
{
  "en": "Demo rule After Rain",
  "th": "ข้อการแข่งขันทดลอง ฟ้าหลังฝน"
}
```
**section_number — known**
```json
"4.8"
```
**text — known**
```json
{
  "en": "Fictional clause 8: for Player accounts, follow decision conditional; exception requires written demo operator approval; not actual rules",
  "th": "ข้อสมมุติ 8: บัญชีผู้เล่น ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_08.json)

### ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`)

รหัส `demo20_news_08`

คำถามตัวอย่าง:

- ข่าวทดลอง ฟ้าหลังฝน ประกาศว่าอะไร
- Demo bulletin After Rain What does the announcement say?
- ข่าวทดลอง ฟ้าหลังฝน ประกาศอะไรและกิจกรรมเริ่มจบเมื่อไหร่

**audience_ids — known**
```json
[
  "demo20_audience_08"
]
```
**body — known**
```json
{
  "en": "Synthetic bulletin: Letter Runner activity for 1–2 people; no actual payment",
  "th": "ข่าวสมมุติ: กิจกรรมผู้ส่งจดหมาย สำหรับกลุ่ม 1–2 คน; ไม่มีรับเงินจริง"
}
```
**contact_id — known**
```json
"demo20_contact_08"
```
**event_end — known**
```json
"2026-12-08T12:00:00+07:00"
```
**event_start — known**
```json
"2026-12-08T10:00:00+07:00"
```
**registration_url — known**
```json
"https://example.invalid/demo20/register/8"
```
**title — known**
```json
{
  "en": "Demo bulletin After Rain",
  "th": "ข่าวทดลอง ฟ้าหลังฝน"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/news/demo20_news_08.json)

### บุคลากร/ทีมที่เปิดเผยได้ (`person`)

รหัส `demo20_person_08`

คำถามตัวอย่าง:

- ผู้ดูแลสมมุติ ฟ้าหลังฝน รับผิดชอบอะไร
- Fictional host After Rain What is their role?
- ผู้ดูแลสมมุติ ฟ้าหลังฝน รับผิดชอบเรื่องอะไรและติดต่อทางไหน

**display_name — known**
```json
{
  "en": "Fictional host After Rain",
  "th": "ผู้ดูแลสมมุติ ฟ้าหลังฝน"
}
```
**public_contact_id — known**
```json
"demo20_contact_08"
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
  "en": "Fictional host for Player accounts",
  "th": "ผู้ดูแลสมมุติเรื่อง บัญชีผู้เล่น"
}
```
**team — known**
```json
{
  "en": "Demo After Rain team",
  "th": "ทีมทดสอบ ฟ้าหลังฝน"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/person/demo20_person_08.json)

### คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`)

รหัส `demo20_faq_08`

คำถามตัวอย่าง:

- คำถามตัวอย่าง ฟ้าหลังฝน คำตอบคืออะไร
- Demo enquiry After Rain What is the answer?
- คำถามตัวอย่าง ฟ้าหลังฝน คำตอบคืออะไรและใช้กับกรณีไหน

**answer — known**
```json
{
  "en": "Example answer: Fictional rule for Player accounts: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องบัญชีผู้เล่น: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
}
```
**question — known**
```json
{
  "en": "Demo enquiry After Rain",
  "th": "คำถามตัวอย่าง ฟ้าหลังฝน"
}
```
**related_ids — known**
```json
[
  "demo20_policy_08",
  "demo20_procedure_08"
]
```
**scope_note — known**
```json
{
  "en": "Only applies to fictional After Rain scenario",
  "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ฟ้าหลังฝน"
}
```
**topic — known**
```json
"DEMO Player accounts"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_08.json)

### การเชื่อมสถานะสด (`live_binding`)

รหัส `demo20_live_binding_08`

คำถามตัวอย่าง:

- ตัวเชื่อมทดลอง ฟ้าหลังฝน จับคู่สถานะยังไง
- Demo binding After Rain How are statuses mapped?
- ตัวเชื่อมทดลอง ฟ้าหลังฝน จับคู่สถานะแบบไหนและเก็บข้อมูลนานเท่าไหร่

**external_resource_key — known**
```json
"DEMO20_EXTERNAL_8"
```
**freshness_policy — known**
```json
{
  "en": "Synthetic TTL 55 seconds; no API call or live status claim",
  "th": "ค่าจำลอง TTL 55 วินาที; ไม่เรียก API และไม่ยืนยันสถานะสด"
}
```
**physical_pool_key — known**
```json
"demo20_pool_08"
```
**provider — known**
```json
"wordpress_booking"
```
**service_id — known**
```json
"demo20_service_08"
```
**status_mapping — known**
```json
[
  {
    "normalized": "free",
    "raw": "DEMO_EMPTY_8"
  },
  {
    "normalized": "occupied",
    "raw": "DEMO_BUSY_8"
  },
  {
    "normalized": "unknown",
    "raw": "DEMO_UNKNOWN_8"
  }
]
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/live_binding/demo20_live_binding_08.json)

