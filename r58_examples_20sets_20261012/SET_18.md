# ชุด 18 — กระเบน / Ray

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

เกม สถานที่ ราคา กฎ บุคคล และสถานะทั้งหมดในชุดใหม่นี้แต่งขึ้นเพื่อทดสอบ ไม่ได้เป็นข้อมูล PSU หรือเกมที่มีจำหน่ายจริง คำแปลยังไม่ผ่านมนุษย์

แพลตฟอร์มตัวอย่าง: PC • จำนวนผู้เล่น 1–1 • เวลาเล่น 60 นาที / กินช่องจอง 60 นาที

## ข้อมูลครบ 24 หมวด

### ข้อมูลศูนย์ (`center`)

รหัส `demo20_center_18`

คำถามตัวอย่าง:

- ศูนย์ทดลอง กระเบน อยู่ตรงไหน
- Demo venue Ray Where is it located?
- ศูนย์ทดลอง กระเบน อยู่ตึกอะไร ชั้นไหน

**address — known**
```json
{
  "en": "Fictional address 126, Example Road, Test District",
  "th": "เลขที่สมมุติ 126 ถนนตัวอย่าง แขวงทดลอง"
}
```
**building — known**
```json
"DEMO Tower D"
```
**description — known**
```json
{
  "en": "Synthetic scenario 18: Lost Satellite, not a real venue",
  "th": "สถานการณ์ทดลอง 18: ดาวเทียมหลงทาง ไม่ใช่สถานที่จริง"
}
```
**floor — known**
```json
"4"
```
**map_url — known**
```json
"https://example.invalid/demo20/map/18"
```
**name — known**
```json
{
  "en": "Demo venue Ray",
  "th": "ศูนย์ทดลอง กระเบน"
}
```
**operator — known**
```json
{
  "en": "Fictional Ray operator",
  "th": "ผู้ประกอบการสมมุติ กระเบน"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/center/demo20_center_18.json)

### โซนบริการ (`zone`)

รหัส `demo20_zone_18`

คำถามตัวอย่าง:

- โซนทดลอง กระเบน มีที่นั่งกี่ที่
- Demo zone Ray How many seats are there?
- โซนทดลอง กระเบน โซนนี้อยู่ตรงไหนและมีที่นั่งกี่ที่

**description — known**
```json
{
  "en": "Synthetic PC zone for Lost Satellite",
  "th": "โซนจำลอง PC สำหรับดาวเทียมหลงทาง"
}
```
**location — known**
```json
{
  "en": "Test building, floor 4, room 118",
  "th": "อาคารทดสอบ ชั้น 4 ห้อง 118"
}
```
**name — known**
```json
{
  "en": "Demo zone Ray",
  "th": "โซนทดลอง กระเบน"
}
```
**room_seats — known**
```json
3
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_18.json)

### รุ่นและสเปกอุปกรณ์ (`equipment_model`)

รหัส `demo20_equipment_model_18`

คำถามตัวอย่าง:

- รุ่นอุปกรณ์ กระเบน สเปกมีอะไรบ้าง
- Demo model Ray What are its specifications?
- รุ่นอุปกรณ์ กระเบน เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง

**device_type — known**
```json
"pc"
```
**name — known**
```json
{
  "en": "Demo model Ray",
  "th": "รุ่นอุปกรณ์ กระเบน"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_18.json)

### เครื่องหรือทรัพยากรจริง (`resource`)

รหัส `demo20_resource_18`

คำถามตัวอย่าง:

- เครื่องทดลอง กระเบน เล่นพร้อมกันได้กี่คน
- Demo station Ray How many people can play at once?
- เครื่องทดลอง กระเบน เครื่องยังใช้งานได้ไหมและรองรับกี่คน

**capacity_persons — known**
```json
1
```
**equipment_model_ids — known**
```json
[
  "demo20_equipment_model_18"
]
```
**name — known**
```json
{
  "en": "Demo station Ray",
  "th": "เครื่องทดลอง กระเบน"
}
```
**operational_status — known**
```json
"in_service"
```
**physical_pool_key — known**
```json
"demo20_pool_18"
```
**zone_id — known**
```json
"demo20_zone_18"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/resource/demo20_resource_18.json)

### รายการที่เลือกในระบบจอง (`service`)

รหัส `demo20_service_18`

คำถามตัวอย่าง:

- รอบทดลอง กระเบน หนึ่งรอบเล่นได้กี่นาที
- Demo session Ray How many minutes does one session last?
- รอบทดลอง กระเบน เวลาเล่นกับเวลาที่กินช่องจองกี่นาที

**booking_product_key — known**
```json
"DEMO20_BOOKING_18"
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
  "en": "Demo session Ray",
  "th": "รอบทดลอง กระเบน"
}
```
**occupancy_minutes — known**
```json
60
```
**platform — known**
```json
"PC"
```
**resource_ids — known**
```json
[
  "demo20_resource_18"
]
```
**session_minutes — known**
```json
60
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_18.json)

### ข้อมูลเกม (`game`)

รหัส `demo20_game_18`

คำถามตัวอย่าง:

- เกมสมมุติ กระเบน เล่นยังไง
- Fictional game Ray How do I play it?
- เกมสมมุติ กระเบน เกมเกี่ยวกับอะไรและเล่นยังไง

**age_rating — known**
```json
{
  "en": "Synthetic DEMO rating 9",
  "th": "เรตอายุสมมุติ DEMO 9"
}
```
**edition — known**
```json
"DEMO fiction revision 18"
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
  "en": "Choose commands to guide a satellite back; follow the demonstration controls",
  "th": "เลือกคำสั่งนำดาวเทียมกลับสถานี; ใช้คำสั่งตามชุดควบคุมทดลอง"
}
```
**publisher_url — known**
```json
"https://example.invalid/demo20/fictional-game/18"
```
**summary — known**
```json
{
  "en": "Fictional test game: Choose commands to guide a satellite back",
  "th": "เกมแต่งขึ้นเพื่อทดสอบ: เลือกคำสั่งนำดาวเทียมกลับสถานี"
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
  "en": "Fictional Lost Satellite",
  "th": "เกมสมมุติ ดาวเทียมหลงทาง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_18.json)

### กลุ่มผู้ใช้ (`audience`)

รหัส `demo20_audience_18`

คำถามตัวอย่าง:

- กลุ่มผู้ใช้ กระเบน ต้องใช้หลักฐานอะไร
- Demo visitors Ray What proof is required?
- กลุ่มผู้ใช้ กระเบน ใครใช้สิทธิ์กลุ่มนี้ได้และต้องแสดงหลักฐานอะไร

**eligibility — known**
```json
{
  "en": "Fictional group 18: demo sessions only",
  "th": "ผู้ใช้สมมุติกลุ่ม 18: ใช้บริการตามรอบทดลอง"
}
```
**name — known**
```json
{
  "en": "Demo visitors Ray",
  "th": "กลุ่มผู้ใช้ กระเบน"
}
```
**required_proofs — known**
```json
[
  "DEMO pass Ray"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/audience/demo20_audience_18.json)

### ติดต่อ (`contact`)

รหัส `demo20_contact_18`

คำถามตัวอย่าง:

- ช่องทางช่วยเหลือ กระเบน ติดต่อทางไหน
- Demo help channel Ray How can I contact them?
- ช่องทางช่วยเหลือ กระเบน ติดต่อที่ไหนและติดต่อได้ช่วงไหน

**channel — known**
```json
"website"
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
  "en": "Fictional support for Refund requests",
  "th": "สอบถามสมมุติเรื่อง คืนเงิน"
}
```
**value — known**
```json
"https://example.invalid/demo20/contact/18"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_18.json)

### ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`)

รหัส `demo20_procedure_18`

คำถามตัวอย่าง:

- ขั้นตอนทดลอง กระเบน ต้องทำยังไงบ้าง
- Demo procedure Ray What steps should I follow?
- ขั้นตอนทดลอง กระเบน มีขั้นตอนอะไรและต้องใช้เอกสารอะไร

**deadline_minutes — known**
```json
30
```
**outcome — known**
```json
{
  "en": "Demo outcome: Refund requests checked",
  "th": "ผลทดสอบ: ตรวจสอบ คืนเงิน เสร็จ"
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
  "DEMO pass Ray"
]
```
**steps — known**
```json
[
  {
    "contact_id": null,
    "instruction": {
      "en": "Select the fictional Ray service",
      "th": "เลือกบริการสมมุติ กระเบน"
    },
    "order": 1
  },
  {
    "contact_id": "demo20_contact_18",
    "instruction": {
      "en": "Check names and conditions before confirming",
      "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
    },
    "order": 2
  },
  {
    "contact_id": "demo20_contact_18",
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
"DEMO Refund requests"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_18.json)

### นโยบายและกฎศูนย์ (`policy`)

รหัส `demo20_policy_18`

คำถามตัวอย่าง:

- ข้อกำหนดทดลอง กระเบน กฎเป็นยังไง
- Demo policy Ray What are the rules?
- ข้อกำหนดทดลอง กระเบน อนุญาตไหมและมีข้อยกเว้นอะไร

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
  "en": "Fictional rule for Refund requests: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "กติกาสมมุติเรื่องคืนเงิน: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
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
"demo20_procedure_18"
```
**subject — known**
```json
{
  "en": "Demo policy Ray",
  "th": "ข้อกำหนดทดลอง กระเบน"
}
```
**topic — known**
```json
"DEMO Refund requests"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/policy/demo20_policy_18.json)

### สิ่งอำนวยความสะดวก (`facility`)

รหัส `demo20_facility_18`

คำถามตัวอย่าง:

- พื้นที่พัก กระเบน อยู่ตรงไหนในร้าน
- Demo amenity Ray Where in the venue is it?
- พื้นที่พัก กระเบน อยู่ตรงไหนและคนที่ต้องการความช่วยเหลือเข้าใช้ยังไง

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
  "en": "Payment help point in demo room 118",
  "th": "จุดสอบถามเงิน อยู่ห้องทดสอบ 118"
}
```
**name — known**
```json
{
  "en": "Demo amenity Ray",
  "th": "พื้นที่พัก กระเบน"
}
```
**usage_conditions — known**
```json
{
  "en": "Demo sessions only; may use while waiting",
  "th": "ใช้ตามรอบทดลอง; ใช้ได้ระหว่างรอ"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/facility/demo20_facility_18.json)

### เกมที่ศูนย์มีให้เล่นจริง (`game_service`)

รหัส `demo20_game_service_18`

คำถามตัวอย่าง:

- การติดตั้งทดลอง กระเบน มีให้เล่นหรือยัง
- Demo installation Ray Is this game offered?
- การติดตั้งทดลอง กระเบน มีให้เล่นไหมและติดตั้งรุ่นไหน

**account_policy_id — known**
```json
"demo20_policy_18"
```
**game_id — known**
```json
"demo20_game_18"
```
**game_version — known**
```json
"DEMO BUILD 18"
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
"demo20_service_18"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_service/demo20_game_service_18.json)

### รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`)

รหัส `demo20_game_mode_18`

คำถามตัวอย่าง:

- โหมดทดลอง กระเบน เล่นพร้อมกันได้สูงสุดกี่คน
- Demo mode Ray How many people can play together at most?
- โหมดทดลอง กระเบน ต้องมีขั้นต่ำกี่คนและเล่นได้สูงสุดกี่คน

**game_id — known**
```json
"demo20_game_18"
```
**mode_name — known**
```json
{
  "en": "Demo mode Ray",
  "th": "โหมดทดลอง กระเบน"
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
"PC"
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
false
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_mode/demo20_game_mode_18.json)

### วิธีเล่นและปุ่ม (`control_set`)

รหัส `demo20_control_set_18`

คำถามตัวอย่าง:

- ชุดควบคุมทดลอง กระเบน ปุ่มอะไรบ้าง
- Demo controls Ray What are the controls?
- ชุดควบคุมทดลอง กระเบน ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร

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
      "en": "Fictional input for Lost Satellite",
      "th": "คำสั่งสมมุติของ ดาวเทียมหลงทาง"
    },
    "gesture": "press"
  }
]
```
**game_id — known**
```json
"demo20_game_18"
```
**game_version — known**
```json
"DEMO BUILD 18"
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
"DEMO_LAYOUT_18"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_18.json)

### ราคาต่อบริการ (`rate`)

รหัส `demo20_rate_18`

คำถามตัวอย่าง:

- อัตราทดลอง กระเบน ราคาเท่าไหร่
- Demo tariff Ray How much does it cost?
- อัตราทดลอง กระเบน ราคาเท่าไหร่และได้กี่นาที

**amount_minor — known**
```json
3000
```
**audience_id — known**
```json
"demo20_audience_18"
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
1
```
**persons_min — known**
```json
1
```
**service_id — known**
```json
"demo20_service_18"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rate/demo20_rate_18.json)

### ราคาเหมาโซน/ห้อง (`rental_package`)

รหัส `demo20_rental_package_18`

คำถามตัวอย่าง:

- แพ็กเกจทดลอง กระเบน เหมาเท่าไหร่
- Demo package Ray How much is the rental?
- แพ็กเกจทดลอง กระเบน ราคาเหมาเท่าไหร่และรวมอุปกรณ์อะไร

**amount_minor — known**
```json
10250
```
**audience_id — known**
```json
"demo20_audience_18"
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
  "en": "Fictional Ray station and PC inputs",
  "th": "เครื่องสมมุติ กระเบน พร้อมอุปกรณ์ PC"
}
```
**name — known**
```json
{
  "en": "Demo package Ray",
  "th": "แพ็กเกจทดลอง กระเบน"
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
  "demo20_zone_18"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rental_package/demo20_rental_package_18.json)

### ตารางบริการ (`schedule`)

รหัส `demo20_schedule_18`

คำถามตัวอย่าง:

- ตารางทดลอง กระเบน จองช่วงไหนได้บ้าง
- Demo timetable Ray What are the booking hours?
- ตารางทดลอง กระเบน เปิดช่วงไหนและพักบำรุงรักษาตอนไหน

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
  "en": "Synthetic Ray schedule with maintenance",
  "th": "ตารางสมมุติ กระเบน มีพักบำรุงรักษา"
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
  "demo20_zone_18"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_18.json)

### วันปิด/ข้อยกเว้น (`closure`)

รหัส `demo20_closure_18`

คำถามตัวอย่าง:

- ประกาศวันทดลอง กระเบน วันนั้นปิดไหม
- Demo date notice Ray Is it closed on that date?
- ประกาศวันทดลอง กระเบน วันนั้นเปิดปิดยังไงและเพราะอะไร

**bookable_periods — known**
```json
[]
```
**local_date — known**
```json
"2026-12-18"
```
**open_periods — known**
```json
[]
```
**reason — known**
```json
{
  "en": "Synthetic Ray date notice: closed",
  "th": "ประกาศสมมุติ กระเบน: closed"
}
```
**resolution_policy_id — known**
```json
"demo20_policy_18"
```
**state — known**
```json
"closed"
```
**zone_ids — known**
```json
[
  "demo20_zone_18"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/closure/demo20_closure_18.json)

### รายการแข่งขันและฉบับกติกา (`competition`)

รหัส `demo20_competition_18`

คำถามตัวอย่าง:

- รายการฝึก กระเบน ใช้กติกาฉบับไหน
- Demo event Ray Which rulebook release applies?
- รายการฝึก กระเบน ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่

**competition_dates — known**
```json
[
  "2026-12-18"
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
  "en": "Demo event Ray",
  "th": "รายการฝึก กระเบน"
}
```
**game_id — known**
```json
"demo20_game_18"
```
**rulebook_release — known**
```json
"DEMO20_REV_18"
```
**supersedes_id — not_applicable**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_18.json)

### ข้อกติกาการแข่งขัน (`competition_rule`)

รหัส `demo20_competition_rule_18`

คำถามตัวอย่าง:

- ข้อการแข่งขันทดลอง กระเบน ข้อนี้กำหนดอะไร
- Demo rule Ray What does this rule require?
- ข้อการแข่งขันทดลอง กระเบน กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม

**competition_id — known**
```json
"demo20_competition_18"
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
  "en": "Demo rule Ray",
  "th": "ข้อการแข่งขันทดลอง กระเบน"
}
```
**section_number — known**
```json
"4.18"
```
**text — known**
```json
{
  "en": "Fictional clause 18: for Refund requests, follow decision prohibited; exception requires written demo operator approval; not actual rules",
  "th": "ข้อสมมุติ 18: คืนเงิน ให้ปฏิบัติตามคำตัดสิน prohibited; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_18.json)

### ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`)

รหัส `demo20_news_18`

คำถามตัวอย่าง:

- ข่าวทดลอง กระเบน ประกาศว่าอะไร
- Demo bulletin Ray What does the announcement say?
- ข่าวทดลอง กระเบน ประกาศอะไรและกิจกรรมเริ่มจบเมื่อไหร่

**audience_ids — known**
```json
[
  "demo20_audience_18"
]
```
**body — known**
```json
{
  "en": "Synthetic bulletin: Lost Satellite activity for 1–1 people; no actual payment",
  "th": "ข่าวสมมุติ: กิจกรรมดาวเทียมหลงทาง สำหรับกลุ่ม 1–1 คน; ไม่มีรับเงินจริง"
}
```
**contact_id — known**
```json
"demo20_contact_18"
```
**event_end — known**
```json
"2026-12-18T12:00:00+07:00"
```
**event_start — known**
```json
"2026-12-18T10:00:00+07:00"
```
**registration_url — known**
```json
"https://example.invalid/demo20/register/18"
```
**title — known**
```json
{
  "en": "Demo bulletin Ray",
  "th": "ข่าวทดลอง กระเบน"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/news/demo20_news_18.json)

### บุคลากร/ทีมที่เปิดเผยได้ (`person`)

รหัส `demo20_person_18`

คำถามตัวอย่าง:

- ผู้ดูแลสมมุติ กระเบน รับผิดชอบอะไร
- Fictional host Ray What is their role?
- ผู้ดูแลสมมุติ กระเบน รับผิดชอบเรื่องอะไรและติดต่อทางไหน

**display_name — known**
```json
{
  "en": "Fictional host Ray",
  "th": "ผู้ดูแลสมมุติ กระเบน"
}
```
**public_contact_id — known**
```json
"demo20_contact_18"
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
  "en": "Fictional host for Refund requests",
  "th": "ผู้ดูแลสมมุติเรื่อง คืนเงิน"
}
```
**team — known**
```json
{
  "en": "Demo Ray team",
  "th": "ทีมทดสอบ กระเบน"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/person/demo20_person_18.json)

### คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`)

รหัส `demo20_faq_18`

คำถามตัวอย่าง:

- คำถามตัวอย่าง กระเบน คำตอบคืออะไร
- Demo enquiry Ray What is the answer?
- คำถามตัวอย่าง กระเบน คำตอบคืออะไรและใช้กับกรณีไหน

**answer — known**
```json
{
  "en": "Example answer: Fictional rule for Refund requests: prohibited; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องคืนเงิน: prohibited; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
}
```
**question — known**
```json
{
  "en": "Demo enquiry Ray",
  "th": "คำถามตัวอย่าง กระเบน"
}
```
**related_ids — known**
```json
[
  "demo20_policy_18",
  "demo20_procedure_18"
]
```
**scope_note — known**
```json
{
  "en": "Only applies to fictional Ray scenario",
  "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ กระเบน"
}
```
**topic — known**
```json
"DEMO Refund requests"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_18.json)

### การเชื่อมสถานะสด (`live_binding`)

รหัส `demo20_live_binding_18`

คำถามตัวอย่าง:

- ตัวเชื่อมทดลอง กระเบน จับคู่สถานะยังไง
- Demo binding Ray How are statuses mapped?
- ตัวเชื่อมทดลอง กระเบน จับคู่สถานะแบบไหนและเก็บข้อมูลนานเท่าไหร่

**external_resource_key — known**
```json
"DEMO20_EXTERNAL_18"
```
**freshness_policy — known**
```json
{
  "en": "Synthetic TTL 105 seconds; no API call or live status claim",
  "th": "ค่าจำลอง TTL 105 วินาที; ไม่เรียก API และไม่ยืนยันสถานะสด"
}
```
**physical_pool_key — known**
```json
"demo20_pool_18"
```
**provider — known**
```json
"wordpress_booking"
```
**service_id — known**
```json
"demo20_service_18"
```
**status_mapping — known**
```json
[
  {
    "normalized": "free",
    "raw": "DEMO_EMPTY_18"
  },
  {
    "normalized": "occupied",
    "raw": "DEMO_BUSY_18"
  },
  {
    "normalized": "unknown",
    "raw": "DEMO_UNKNOWN_18"
  }
]
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/live_binding/demo20_live_binding_18.json)

