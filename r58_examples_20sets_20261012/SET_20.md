# ชุด 20 — รุ่งเรือง / Radiance

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

เกม สถานที่ ราคา กฎ บุคคล และสถานะทั้งหมดในชุดใหม่นี้แต่งขึ้นเพื่อทดสอบ ไม่ได้เป็นข้อมูล PSU หรือเกมที่มีจำหน่ายจริง คำแปลยังไม่ผ่านมนุษย์

แพลตฟอร์มตัวอย่าง: PC • จำนวนผู้เล่น 2–8 • เวลาเล่น 240 นาที / กินช่องจอง 240 นาที

## ข้อมูลครบ 24 หมวด

### ข้อมูลศูนย์ (`center`)

รหัส `demo20_center_20`

คำถามตัวอย่าง:

- ศูนย์ทดลอง รุ่งเรือง อยู่ตรงไหน
- Demo venue Radiance Where is it located?
- ศูนย์ทดลอง รุ่งเรือง อยู่ตึกอะไร ชั้นไหน

**address — known**
```json
{
  "en": "Fictional address 140, Example Road, Test District",
  "th": "เลขที่สมมุติ 140 ถนนตัวอย่าง แขวงทดลอง"
}
```
**building — known**
```json
"DEMO Tower A"
```
**description — known**
```json
{
  "en": "Synthetic scenario 20: Practice Arena, not a real venue",
  "th": "สถานการณ์ทดลอง 20: เวทีฝึกฝน ไม่ใช่สถานที่จริง"
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
  "en": "Demo venue Radiance",
  "th": "ศูนย์ทดลอง รุ่งเรือง"
}
```
**operator — known**
```json
{
  "en": "Fictional Radiance operator",
  "th": "ผู้ประกอบการสมมุติ รุ่งเรือง"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/center/demo20_center_20.json)

### โซนบริการ (`zone`)

รหัส `demo20_zone_20`

คำถามตัวอย่าง:

- โซนทดลอง รุ่งเรือง มีที่นั่งกี่ที่
- Demo zone Radiance How many seats are there?
- โซนทดลอง รุ่งเรือง โซนนี้อยู่ตรงไหนและมีที่นั่งกี่ที่

**description — known**
```json
{
  "en": "Synthetic PC zone for Practice Arena",
  "th": "โซนจำลอง PC สำหรับเวทีฝึกฝน"
}
```
**location — known**
```json
{
  "en": "Test building, floor 1, room 120",
  "th": "อาคารทดสอบ ชั้น 1 ห้อง 120"
}
```
**name — known**
```json
{
  "en": "Demo zone Radiance",
  "th": "โซนทดลอง รุ่งเรือง"
}
```
**room_seats — known**
```json
12
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_20.json)

### รุ่นและสเปกอุปกรณ์ (`equipment_model`)

รหัส `demo20_equipment_model_20`

คำถามตัวอย่าง:

- รุ่นอุปกรณ์ รุ่งเรือง สเปกมีอะไรบ้าง
- Demo model Radiance What are its specifications?
- รุ่นอุปกรณ์ รุ่งเรือง เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง

**device_type — known**
```json
"pc"
```
**name — known**
```json
{
  "en": "Demo model Radiance",
  "th": "รุ่นอุปกรณ์ รุ่งเรือง"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_20.json)

### เครื่องหรือทรัพยากรจริง (`resource`)

รหัส `demo20_resource_20`

คำถามตัวอย่าง:

- เครื่องทดลอง รุ่งเรือง เล่นพร้อมกันได้กี่คน
- Demo station Radiance How many people can play at once?
- เครื่องทดลอง รุ่งเรือง เครื่องยังใช้งานได้ไหมและรองรับกี่คน

**capacity_persons — known**
```json
8
```
**equipment_model_ids — known**
```json
[
  "demo20_equipment_model_20"
]
```
**name — known**
```json
{
  "en": "Demo station Radiance",
  "th": "เครื่องทดลอง รุ่งเรือง"
}
```
**operational_status — known**
```json
"retired"
```
**physical_pool_key — known**
```json
"demo20_pool_20"
```
**zone_id — known**
```json
"demo20_zone_20"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/resource/demo20_resource_20.json)

### รายการที่เลือกในระบบจอง (`service`)

รหัส `demo20_service_20`

คำถามตัวอย่าง:

- รอบทดลอง รุ่งเรือง หนึ่งรอบเล่นได้กี่นาที
- Demo session Radiance How many minutes does one session last?
- รอบทดลอง รุ่งเรือง เวลาเล่นกับเวลาที่กินช่องจองกี่นาที

**booking_product_key — unknown**
```json
null
```
**capacity_max — known**
```json
8
```
**capacity_min — known**
```json
2
```
**name — known**
```json
{
  "en": "Demo session Radiance",
  "th": "รอบทดลอง รุ่งเรือง"
}
```
**occupancy_minutes — known**
```json
240
```
**platform — known**
```json
"PC"
```
**resource_ids — known**
```json
[
  "demo20_resource_20"
]
```
**session_minutes — known**
```json
240
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_20.json)

### ข้อมูลเกม (`game`)

รหัส `demo20_game_20`

คำถามตัวอย่าง:

- เกมสมมุติ รุ่งเรือง เล่นยังไง
- Fictional game Radiance How do I play it?
- เกมสมมุติ รุ่งเรือง เกมเกี่ยวกับอะไรและเล่นยังไง

**age_rating — unknown**
```json
null
```
**edition — known**
```json
"DEMO fiction revision 20"
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
  "en": "Pair players for unranked strategy practice; follow the demonstration controls",
  "th": "จับคู่ผู้เล่นฝึกกลยุทธ์โดยไม่จัดอันดับ; ใช้คำสั่งตามชุดควบคุมทดลอง"
}
```
**publisher_url — known**
```json
"https://example.invalid/demo20/fictional-game/20"
```
**summary — known**
```json
{
  "en": "Fictional test game: Pair players for unranked strategy practice",
  "th": "เกมแต่งขึ้นเพื่อทดสอบ: จับคู่ผู้เล่นฝึกกลยุทธ์โดยไม่จัดอันดับ"
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
  "en": "Fictional Practice Arena",
  "th": "เกมสมมุติ เวทีฝึกฝน"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_20.json)

### กลุ่มผู้ใช้ (`audience`)

รหัส `demo20_audience_20`

คำถามตัวอย่าง:

- กลุ่มผู้ใช้ รุ่งเรือง ต้องใช้หลักฐานอะไร
- Demo visitors Radiance What proof is required?
- กลุ่มผู้ใช้ รุ่งเรือง ใครใช้สิทธิ์กลุ่มนี้ได้และต้องแสดงหลักฐานอะไร

**eligibility — known**
```json
{
  "en": "Fictional group 20: demo sessions only",
  "th": "ผู้ใช้สมมุติกลุ่ม 20: ใช้บริการตามรอบทดลอง"
}
```
**name — known**
```json
{
  "en": "Demo visitors Radiance",
  "th": "กลุ่มผู้ใช้ รุ่งเรือง"
}
```
**required_proofs — unknown**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/audience/demo20_audience_20.json)

### ติดต่อ (`contact`)

รหัส `demo20_contact_20`

คำถามตัวอย่าง:

- ช่องทางช่วยเหลือ รุ่งเรือง ติดต่อทางไหน
- Demo help channel Radiance How can I contact them?
- ช่องทางช่วยเหลือ รุ่งเรือง ติดต่อที่ไหนและติดต่อได้ช่วงไหน

**channel — known**
```json
"onsite"
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
  "en": "Fictional support for Result appeals",
  "th": "สอบถามสมมุติเรื่อง การประท้วงผล"
}
```
**value — known**
```json
"DEMO desk Radiance"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_20.json)

### ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`)

รหัส `demo20_procedure_20`

คำถามตัวอย่าง:

- ขั้นตอนทดลอง รุ่งเรือง ต้องทำยังไงบ้าง
- Demo procedure Radiance What steps should I follow?
- ขั้นตอนทดลอง รุ่งเรือง มีขั้นตอนอะไรและต้องใช้เอกสารอะไร

**deadline_minutes — known**
```json
0
```
**outcome — known**
```json
{
  "en": "Demo outcome: Result appeals checked",
  "th": "ผลทดสอบ: ตรวจสอบ การประท้วงผล เสร็จ"
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
      "en": "Select the fictional Radiance service",
      "th": "เลือกบริการสมมุติ รุ่งเรือง"
    },
    "order": 1
  },
  {
    "contact_id": "demo20_contact_20",
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
"DEMO Result appeals"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_20.json)

### นโยบายและกฎศูนย์ (`policy`)

รหัส `demo20_policy_20`

คำถามตัวอย่าง:

- ข้อกำหนดทดลอง รุ่งเรือง กฎเป็นยังไง
- Demo policy Radiance What are the rules?
- ข้อกำหนดทดลอง รุ่งเรือง อนุญาตไหมและมีข้อยกเว้นอะไร

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
  "en": "Fictional rule for Result appeals: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "กติกาสมมุติเรื่องการประท้วงผล: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
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
"demo20_procedure_20"
```
**subject — known**
```json
{
  "en": "Demo policy Radiance",
  "th": "ข้อกำหนดทดลอง รุ่งเรือง"
}
```
**topic — known**
```json
"DEMO Result appeals"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/policy/demo20_policy_20.json)

### สิ่งอำนวยความสะดวก (`facility`)

รหัส `demo20_facility_20`

คำถามตัวอย่าง:

- พื้นที่พัก รุ่งเรือง อยู่ตรงไหนในร้าน
- Demo amenity Radiance Where in the venue is it?
- พื้นที่พัก รุ่งเรือง อยู่ตรงไหนและคนที่ต้องการความช่วยเหลือเข้าใช้ยังไง

**accessibility — unknown**
```json
null
```
**location — known**
```json
{
  "en": "Official desk in demo room 120",
  "th": "โต๊ะกรรมการ อยู่ห้องทดสอบ 120"
}
```
**name — known**
```json
{
  "en": "Demo amenity Radiance",
  "th": "พื้นที่พัก รุ่งเรือง"
}
```
**usage_conditions — known**
```json
{
  "en": "Demo sessions only; may use while waiting",
  "th": "ใช้ตามรอบทดลอง; ใช้ได้ระหว่างรอ"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/facility/demo20_facility_20.json)

### เกมที่ศูนย์มีให้เล่นจริง (`game_service`)

รหัส `demo20_game_service_20`

คำถามตัวอย่าง:

- การติดตั้งทดลอง รุ่งเรือง มีให้เล่นหรือยัง
- Demo installation Radiance Is this game offered?
- การติดตั้งทดลอง รุ่งเรือง มีให้เล่นไหมและติดตั้งรุ่นไหน

**account_policy_id — known**
```json
"demo20_policy_20"
```
**game_id — known**
```json
"demo20_game_20"
```
**game_version — unknown**
```json
null
```
**installed_resource_ids — known**
```json
[
  "demo20_resource_20"
]
```
**offered — known**
```json
true
```
**service_id — known**
```json
"demo20_service_20"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_service/demo20_game_service_20.json)

### รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`)

รหัส `demo20_game_mode_20`

คำถามตัวอย่าง:

- โหมดทดลอง รุ่งเรือง เล่นพร้อมกันได้สูงสุดกี่คน
- Demo mode Radiance How many people can play together at most?
- โหมดทดลอง รุ่งเรือง ต้องมีขั้นต่ำกี่คนและเล่นได้สูงสุดกี่คน

**game_id — known**
```json
"demo20_game_20"
```
**mode_name — known**
```json
{
  "en": "Demo mode Radiance",
  "th": "โหมดทดลอง รุ่งเรือง"
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
8
```
**players_min — known**
```json
2
```
**studio_supported — known**
```json
true
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_mode/demo20_game_mode_20.json)

### วิธีเล่นและปุ่ม (`control_set`)

รหัส `demo20_control_set_20`

คำถามตัวอย่าง:

- ชุดควบคุมทดลอง รุ่งเรือง ปุ่มอะไรบ้าง
- Demo controls Radiance What are the controls?
- ชุดควบคุมทดลอง รุ่งเรือง ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร

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
      "en": "Fictional input for Practice Arena",
      "th": "คำสั่งสมมุติของ เวทีฝึกฝน"
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
      "en": "Fictional input for Practice Arena",
      "th": "คำสั่งสมมุติของ เวทีฝึกฝน"
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
      "en": "Fictional input for Practice Arena",
      "th": "คำสั่งสมมุติของ เวทีฝึกฝน"
    },
    "gesture": "press"
  }
]
```
**game_id — known**
```json
"demo20_game_20"
```
**game_version — known**
```json
"DEMO BUILD 20"
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
"DEMO_LAYOUT_20"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_20.json)

### ราคาต่อบริการ (`rate`)

รหัส `demo20_rate_20`

คำถามตัวอย่าง:

- อัตราทดลอง รุ่งเรือง ราคาเท่าไหร่
- Demo tariff Radiance How much does it cost?
- อัตราทดลอง รุ่งเรือง ราคาเท่าไหร่และได้กี่นาที

**amount_minor — known**
```json
72000
```
**audience_id — known**
```json
"demo20_audience_20"
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
240
```
**persons_max — known**
```json
8
```
**persons_min — known**
```json
2
```
**service_id — known**
```json
"demo20_service_20"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rate/demo20_rate_20.json)

### ราคาเหมาโซน/ห้อง (`rental_package`)

รหัส `demo20_rental_package_20`

คำถามตัวอย่าง:

- แพ็กเกจทดลอง รุ่งเรือง เหมาเท่าไหร่
- Demo package Radiance How much is the rental?
- แพ็กเกจทดลอง รุ่งเรือง ราคาเหมาเท่าไหร่และรวมอุปกรณ์อะไร

**amount_minor — known**
```json
217250
```
**audience_id — known**
```json
"demo20_audience_20"
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
  "en": "Fictional Radiance station and PC inputs",
  "th": "เครื่องสมมุติ รุ่งเรือง พร้อมอุปกรณ์ PC"
}
```
**name — known**
```json
{
  "en": "Demo package Radiance",
  "th": "แพ็กเกจทดลอง รุ่งเรือง"
}
```
**period_label — known**
```json
"custom"
```
**room_seats — known**
```json
12
```
**terms — known**
```json
{
  "en": "Synthetic package excludes extensions; 2–8 people per session",
  "th": "แพ็กเกจสมมุติไม่รวมค่าต่อเวลา; รอบละ 2–8 คน"
}
```
**zone_ids — known**
```json
[
  "demo20_zone_20"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rental_package/demo20_rental_package_20.json)

### ตารางบริการ (`schedule`)

รหัส `demo20_schedule_20`

คำถามตัวอย่าง:

- ตารางทดลอง รุ่งเรือง จองช่วงไหนได้บ้าง
- Demo timetable Radiance What are the booking hours?
- ตารางทดลอง รุ่งเรือง เปิดช่วงไหนและพักบำรุงรักษาตอนไหน

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
  "en": "Synthetic Radiance schedule without maintenance",
  "th": "ตารางสมมุติ รุ่งเรือง ไม่มีพักบำรุงรักษา"
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
  "demo20_zone_20"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_20.json)

### วันปิด/ข้อยกเว้น (`closure`)

รหัส `demo20_closure_20`

คำถามตัวอย่าง:

- ประกาศวันทดลอง รุ่งเรือง วันนั้นปิดไหม
- Demo date notice Radiance Is it closed on that date?
- ประกาศวันทดลอง รุ่งเรือง วันนั้นเปิดปิดยังไงและเพราะอะไร

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
"2026-12-20"
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
  "en": "Synthetic Radiance date notice: open_override",
  "th": "ประกาศสมมุติ รุ่งเรือง: open_override"
}
```
**resolution_policy_id — known**
```json
"demo20_policy_20"
```
**state — known**
```json
"open_override"
```
**zone_ids — known**
```json
[
  "demo20_zone_20"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/closure/demo20_closure_20.json)

### รายการแข่งขันและฉบับกติกา (`competition`)

รหัส `demo20_competition_20`

คำถามตัวอย่าง:

- รายการฝึก รุ่งเรือง ใช้กติกาฉบับไหน
- Demo event Radiance Which rulebook release applies?
- รายการฝึก รุ่งเรือง ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่

**competition_dates — known**
```json
[
  "2026-12-20"
]
```
**coverage — known**
```json
"complete"
```
**division — known**
```json
{
  "en": "Practice group 2–8 players",
  "th": "กลุ่มฝึก 2–8 คน"
}
```
**event_name — known**
```json
{
  "en": "Demo event Radiance",
  "th": "รายการฝึก รุ่งเรือง"
}
```
**game_id — known**
```json
"demo20_game_20"
```
**rulebook_release — known**
```json
"DEMO20_REV_20"
```
**supersedes_id — not_applicable**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_20.json)

### ข้อกติกาการแข่งขัน (`competition_rule`)

รหัส `demo20_competition_rule_20`

คำถามตัวอย่าง:

- ข้อการแข่งขันทดลอง รุ่งเรือง ข้อนี้กำหนดอะไร
- Demo rule Radiance What does this rule require?
- ข้อการแข่งขันทดลอง รุ่งเรือง กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม

**competition_id — known**
```json
"demo20_competition_20"
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
"identity"
```
**heading — known**
```json
{
  "en": "Demo rule Radiance",
  "th": "ข้อการแข่งขันทดลอง รุ่งเรือง"
}
```
**section_number — known**
```json
"1.20"
```
**text — known**
```json
{
  "en": "Fictional clause 20: for Result appeals, follow decision conditional; exception requires written demo operator approval; not actual rules",
  "th": "ข้อสมมุติ 20: การประท้วงผล ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_20.json)

### ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`)

รหัส `demo20_news_20`

คำถามตัวอย่าง:

- ข่าวทดลอง รุ่งเรือง ประกาศว่าอะไร
- Demo bulletin Radiance What does the announcement say?
- ข่าวทดลอง รุ่งเรือง ประกาศอะไรและกิจกรรมเริ่มจบเมื่อไหร่

**audience_ids — known**
```json
[
  "demo20_audience_20"
]
```
**body — known**
```json
{
  "en": "Synthetic bulletin: Practice Arena activity for 2–8 people; no actual payment",
  "th": "ข่าวสมมุติ: กิจกรรมเวทีฝึกฝน สำหรับกลุ่ม 2–8 คน; ไม่มีรับเงินจริง"
}
```
**contact_id — known**
```json
"demo20_contact_20"
```
**event_end — known**
```json
"2026-12-20T12:00:00+07:00"
```
**event_start — known**
```json
"2026-12-20T10:00:00+07:00"
```
**registration_url — known**
```json
"https://example.invalid/demo20/register/20"
```
**title — known**
```json
{
  "en": "Demo bulletin Radiance",
  "th": "ข่าวทดลอง รุ่งเรือง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/news/demo20_news_20.json)

### บุคลากร/ทีมที่เปิดเผยได้ (`person`)

รหัส `demo20_person_20`

คำถามตัวอย่าง:

- ผู้ดูแลสมมุติ รุ่งเรือง รับผิดชอบอะไร
- Fictional host Radiance What is their role?
- ผู้ดูแลสมมุติ รุ่งเรือง รับผิดชอบเรื่องอะไรและติดต่อทางไหน

**display_name — known**
```json
{
  "en": "Fictional host Radiance",
  "th": "ผู้ดูแลสมมุติ รุ่งเรือง"
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
  "en": "Fictional host for Result appeals",
  "th": "ผู้ดูแลสมมุติเรื่อง การประท้วงผล"
}
```
**team — known**
```json
{
  "en": "Demo Radiance team",
  "th": "ทีมทดสอบ รุ่งเรือง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/person/demo20_person_20.json)

### คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`)

รหัส `demo20_faq_20`

คำถามตัวอย่าง:

- คำถามตัวอย่าง รุ่งเรือง คำตอบคืออะไร
- Demo enquiry Radiance What is the answer?
- คำถามตัวอย่าง รุ่งเรือง คำตอบคืออะไรและใช้กับกรณีไหน

**answer — known**
```json
{
  "en": "Example answer: Fictional rule for Result appeals: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องการประท้วงผล: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
}
```
**question — known**
```json
{
  "en": "Demo enquiry Radiance",
  "th": "คำถามตัวอย่าง รุ่งเรือง"
}
```
**related_ids — known**
```json
[
  "demo20_policy_20",
  "demo20_procedure_20"
]
```
**scope_note — known**
```json
{
  "en": "Only applies to fictional Radiance scenario",
  "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ รุ่งเรือง"
}
```
**topic — known**
```json
"DEMO Result appeals"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_20.json)

### การเชื่อมสถานะสด (`live_binding`)

รหัส `demo20_live_binding_20`

คำถามตัวอย่าง:

- ตัวเชื่อมทดลอง รุ่งเรือง จับคู่สถานะยังไง
- Demo binding Radiance How are statuses mapped?
- ตัวเชื่อมทดลอง รุ่งเรือง จับคู่สถานะแบบไหนและเก็บข้อมูลนานเท่าไหร่

**external_resource_key — known**
```json
"DEMO20_EXTERNAL_20"
```
**freshness_policy — known**
```json
{
  "en": "Synthetic TTL 115 seconds; no API call or live status claim",
  "th": "ค่าจำลอง TTL 115 วินาที; ไม่เรียก API และไม่ยืนยันสถานะสด"
}
```
**physical_pool_key — known**
```json
"demo20_pool_20"
```
**provider — known**
```json
"wordpress_booking"
```
**service_id — known**
```json
"demo20_service_20"
```
**status_mapping — known**
```json
[
  {
    "normalized": "free",
    "raw": "DEMO_EMPTY_20"
  },
  {
    "normalized": "occupied",
    "raw": "DEMO_BUSY_20"
  },
  {
    "normalized": "unknown",
    "raw": "DEMO_UNKNOWN_20"
  }
]
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/live_binding/demo20_live_binding_20.json)

