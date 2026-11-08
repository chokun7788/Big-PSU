# ชุด 16 — เมฆขาว / White Cloud

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

เกม สถานที่ ราคา กฎ บุคคล และสถานะทั้งหมดในชุดใหม่นี้แต่งขึ้นเพื่อทดสอบ ไม่ได้เป็นข้อมูล PSU หรือเกมที่มีจำหน่ายจริง คำแปลยังไม่ผ่านมนุษย์

แพลตฟอร์มตัวอย่าง: PC • จำนวนผู้เล่น 1–1 • เวลาเล่น 60 นาที / กินช่องจอง 60 นาที

## ข้อมูลครบ 24 หมวด

### ข้อมูลศูนย์ (`center`)

รหัส `demo20_center_16`

คำถามตัวอย่าง:

- ศูนย์ทดลอง เมฆขาว อยู่ตรงไหน
- Demo venue White Cloud Where is it located?
- ศูนย์ทดลอง เมฆขาว อยู่ตึกอะไร ชั้นไหน

**address — known**
```json
{
  "en": "Fictional address 112, Example Road, Test District",
  "th": "เลขที่สมมุติ 112 ถนนตัวอย่าง แขวงทดลอง"
}
```
**building — known**
```json
"DEMO Tower B"
```
**description — known**
```json
{
  "en": "Synthetic scenario 16: Sound Ladder, not a real venue",
  "th": "สถานการณ์ทดลอง 16: บันไดเสียง ไม่ใช่สถานที่จริง"
}
```
**floor — known**
```json
"2"
```
**map_url — known**
```json
"https://example.invalid/demo20/map/16"
```
**name — known**
```json
{
  "en": "Demo venue White Cloud",
  "th": "ศูนย์ทดลอง เมฆขาว"
}
```
**operator — known**
```json
{
  "en": "Fictional White Cloud operator",
  "th": "ผู้ประกอบการสมมุติ เมฆขาว"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/center/demo20_center_16.json)

### โซนบริการ (`zone`)

รหัส `demo20_zone_16`

คำถามตัวอย่าง:

- โซนทดลอง เมฆขาว มีที่นั่งกี่ที่
- Demo zone White Cloud How many seats are there?
- โซนทดลอง เมฆขาว โซนนี้อยู่ตรงไหนและมีที่นั่งกี่ที่

**description — known**
```json
{
  "en": "Synthetic PC zone for Sound Ladder",
  "th": "โซนจำลอง PC สำหรับบันไดเสียง"
}
```
**location — known**
```json
{
  "en": "Test building, floor 2, room 116",
  "th": "อาคารทดสอบ ชั้น 2 ห้อง 116"
}
```
**name — known**
```json
{
  "en": "Demo zone White Cloud",
  "th": "โซนทดลอง เมฆขาว"
}
```
**room_seats — known**
```json
4
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_16.json)

### รุ่นและสเปกอุปกรณ์ (`equipment_model`)

รหัส `demo20_equipment_model_16`

คำถามตัวอย่าง:

- รุ่นอุปกรณ์ เมฆขาว สเปกมีอะไรบ้าง
- Demo model White Cloud What are its specifications?
- รุ่นอุปกรณ์ เมฆขาว เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง

**device_type — known**
```json
"pc"
```
**name — known**
```json
{
  "en": "Demo model White Cloud",
  "th": "รุ่นอุปกรณ์ เมฆขาว"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_16.json)

### เครื่องหรือทรัพยากรจริง (`resource`)

รหัส `demo20_resource_16`

คำถามตัวอย่าง:

- เครื่องทดลอง เมฆขาว เล่นพร้อมกันได้กี่คน
- Demo station White Cloud How many people can play at once?
- เครื่องทดลอง เมฆขาว เครื่องยังใช้งานได้ไหมและรองรับกี่คน

**capacity_persons — known**
```json
1
```
**equipment_model_ids — known**
```json
[
  "demo20_equipment_model_16"
]
```
**name — known**
```json
{
  "en": "Demo station White Cloud",
  "th": "เครื่องทดลอง เมฆขาว"
}
```
**operational_status — known**
```json
"in_service"
```
**physical_pool_key — known**
```json
"demo20_pool_16"
```
**zone_id — known**
```json
"demo20_zone_16"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/resource/demo20_resource_16.json)

### รายการที่เลือกในระบบจอง (`service`)

รหัส `demo20_service_16`

คำถามตัวอย่าง:

- รอบทดลอง เมฆขาว หนึ่งรอบเล่นได้กี่นาที
- Demo session White Cloud How many minutes does one session last?
- รอบทดลอง เมฆขาว เวลาเล่นกับเวลาที่กินช่องจองกี่นาที

**booking_product_key — known**
```json
"DEMO20_BOOKING_16"
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
  "en": "Demo session White Cloud",
  "th": "รอบทดลอง เมฆขาว"
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
  "demo20_resource_16"
]
```
**session_minutes — known**
```json
60
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_16.json)

### ข้อมูลเกม (`game`)

รหัส `demo20_game_16`

คำถามตัวอย่าง:

- เกมสมมุติ เมฆขาว เล่นยังไง
- Fictional game White Cloud How do I play it?
- เกมสมมุติ เมฆขาว เกมเกี่ยวกับอะไรและเล่นยังไง

**age_rating — known**
```json
{
  "en": "Synthetic DEMO rating 3",
  "th": "เรตอายุสมมุติ DEMO 3"
}
```
**edition — known**
```json
"DEMO fiction revision 16"
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
  "en": "Listen to audio cues and select ladder positions; follow the demonstration controls",
  "th": "ฟังสัญญาณเสียงและเลือกตำแหน่งบนบันได; ใช้คำสั่งตามชุดควบคุมทดลอง"
}
```
**publisher_url — known**
```json
"https://example.invalid/demo20/fictional-game/16"
```
**summary — known**
```json
{
  "en": "Fictional test game: Listen to audio cues and select ladder positions",
  "th": "เกมแต่งขึ้นเพื่อทดสอบ: ฟังสัญญาณเสียงและเลือกตำแหน่งบนบันได"
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
  "en": "Fictional Sound Ladder",
  "th": "เกมสมมุติ บันไดเสียง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_16.json)

### กลุ่มผู้ใช้ (`audience`)

รหัส `demo20_audience_16`

คำถามตัวอย่าง:

- กลุ่มผู้ใช้ เมฆขาว ต้องใช้หลักฐานอะไร
- Demo visitors White Cloud What proof is required?
- กลุ่มผู้ใช้ เมฆขาว ใครใช้สิทธิ์กลุ่มนี้ได้และต้องแสดงหลักฐานอะไร

**eligibility — known**
```json
{
  "en": "Fictional group 16: demo sessions only",
  "th": "ผู้ใช้สมมุติกลุ่ม 16: ใช้บริการตามรอบทดลอง"
}
```
**name — known**
```json
{
  "en": "Demo visitors White Cloud",
  "th": "กลุ่มผู้ใช้ เมฆขาว"
}
```
**required_proofs — known**
```json
[]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/audience/demo20_audience_16.json)

### ติดต่อ (`contact`)

รหัส `demo20_contact_16`

คำถามตัวอย่าง:

- ช่องทางช่วยเหลือ เมฆขาว ติดต่อทางไหน
- Demo help channel White Cloud How can I contact them?
- ช่องทางช่วยเหลือ เมฆขาว ติดต่อที่ไหนและติดต่อได้ช่วงไหน

**channel — known**
```json
"email"
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
  "en": "Fictional support for Accessibility assistance",
  "th": "สอบถามสมมุติเรื่อง การช่วยเข้าถึง"
}
```
**value — known**
```json
"fiction16@example.invalid"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_16.json)

### ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`)

รหัส `demo20_procedure_16`

คำถามตัวอย่าง:

- ขั้นตอนทดลอง เมฆขาว ต้องทำยังไงบ้าง
- Demo procedure White Cloud What steps should I follow?
- ขั้นตอนทดลอง เมฆขาว มีขั้นตอนอะไรและต้องใช้เอกสารอะไร

**deadline_minutes — known**
```json
10
```
**outcome — known**
```json
{
  "en": "Demo outcome: Accessibility assistance checked",
  "th": "ผลทดสอบ: ตรวจสอบ การช่วยเข้าถึง เสร็จ"
}
```
**preconditions — known**
```json
[]
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
      "en": "Select the fictional White Cloud service",
      "th": "เลือกบริการสมมุติ เมฆขาว"
    },
    "order": 1
  },
  {
    "contact_id": "demo20_contact_16",
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
"DEMO Accessibility assistance"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_16.json)

### นโยบายและกฎศูนย์ (`policy`)

รหัส `demo20_policy_16`

คำถามตัวอย่าง:

- ข้อกำหนดทดลอง เมฆขาว กฎเป็นยังไง
- Demo policy White Cloud What are the rules?
- ข้อกำหนดทดลอง เมฆขาว อนุญาตไหมและมีข้อยกเว้นอะไร

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
  "en": "Fictional rule for Accessibility assistance: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "กติกาสมมุติเรื่องการช่วยเข้าถึง: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
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
"demo20_procedure_16"
```
**subject — known**
```json
{
  "en": "Demo policy White Cloud",
  "th": "ข้อกำหนดทดลอง เมฆขาว"
}
```
**topic — known**
```json
"DEMO Accessibility assistance"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/policy/demo20_policy_16.json)

### สิ่งอำนวยความสะดวก (`facility`)

รหัส `demo20_facility_16`

คำถามตัวอย่าง:

- พื้นที่พัก เมฆขาว อยู่ตรงไหนในร้าน
- Demo amenity White Cloud Where in the venue is it?
- พื้นที่พัก เมฆขาว อยู่ตรงไหนและคนที่ต้องการความช่วยเหลือเข้าใช้ยังไง

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
  "en": "Step-free entry in demo room 116",
  "th": "ทางเข้าไร้ขั้น อยู่ห้องทดสอบ 116"
}
```
**name — known**
```json
{
  "en": "Demo amenity White Cloud",
  "th": "พื้นที่พัก เมฆขาว"
}
```
**usage_conditions — known**
```json
{
  "en": "Demo sessions only; may use while waiting",
  "th": "ใช้ตามรอบทดลอง; ใช้ได้ระหว่างรอ"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/facility/demo20_facility_16.json)

### เกมที่ศูนย์มีให้เล่นจริง (`game_service`)

รหัส `demo20_game_service_16`

คำถามตัวอย่าง:

- การติดตั้งทดลอง เมฆขาว มีให้เล่นหรือยัง
- Demo installation White Cloud Is this game offered?
- การติดตั้งทดลอง เมฆขาว มีให้เล่นไหมและติดตั้งรุ่นไหน

**account_policy_id — known**
```json
"demo20_policy_16"
```
**game_id — known**
```json
"demo20_game_16"
```
**game_version — known**
```json
"DEMO BUILD 16"
```
**installed_resource_ids — known**
```json
[
  "demo20_resource_16"
]
```
**offered — known**
```json
true
```
**service_id — known**
```json
"demo20_service_16"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_service/demo20_game_service_16.json)

### รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`)

รหัส `demo20_game_mode_16`

คำถามตัวอย่าง:

- โหมดทดลอง เมฆขาว เล่นพร้อมกันได้สูงสุดกี่คน
- Demo mode White Cloud How many people can play together at most?
- โหมดทดลอง เมฆขาว ต้องมีขั้นต่ำกี่คนและเล่นได้สูงสุดกี่คน

**game_id — known**
```json
"demo20_game_16"
```
**mode_name — known**
```json
{
  "en": "Demo mode White Cloud",
  "th": "โหมดทดลอง เมฆขาว"
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
true
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_mode/demo20_game_mode_16.json)

### วิธีเล่นและปุ่ม (`control_set`)

รหัส `demo20_control_set_16`

คำถามตัวอย่าง:

- ชุดควบคุมทดลอง เมฆขาว ปุ่มอะไรบ้าง
- Demo controls White Cloud What are the controls?
- ชุดควบคุมทดลอง เมฆขาว ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร

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
      "en": "Fictional input for Sound Ladder",
      "th": "คำสั่งสมมุติของ บันไดเสียง"
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
      "en": "Fictional input for Sound Ladder",
      "th": "คำสั่งสมมุติของ บันไดเสียง"
    },
    "gesture": "press"
  }
]
```
**game_id — known**
```json
"demo20_game_16"
```
**game_version — known**
```json
"DEMO BUILD 16"
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
"DEMO_LAYOUT_16"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_16.json)

### ราคาต่อบริการ (`rate`)

รหัส `demo20_rate_16`

คำถามตัวอย่าง:

- อัตราทดลอง เมฆขาว ราคาเท่าไหร่
- Demo tariff White Cloud How much does it cost?
- อัตราทดลอง เมฆขาว ราคาเท่าไหร่และได้กี่นาที

**amount_minor — known**
```json
4000
```
**audience_id — known**
```json
"demo20_audience_16"
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
"demo20_service_16"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rate/demo20_rate_16.json)

### ราคาเหมาโซน/ห้อง (`rental_package`)

รหัส `demo20_rental_package_16`

คำถามตัวอย่าง:

- แพ็กเกจทดลอง เมฆขาว เหมาเท่าไหร่
- Demo package White Cloud How much is the rental?
- แพ็กเกจทดลอง เมฆขาว ราคาเหมาเท่าไหร่และรวมอุปกรณ์อะไร

**amount_minor — known**
```json
13250
```
**audience_id — known**
```json
"demo20_audience_16"
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
  "en": "Fictional White Cloud station and PC inputs",
  "th": "เครื่องสมมุติ เมฆขาว พร้อมอุปกรณ์ PC"
}
```
**name — known**
```json
{
  "en": "Demo package White Cloud",
  "th": "แพ็กเกจทดลอง เมฆขาว"
}
```
**period_label — known**
```json
"full_day"
```
**room_seats — known**
```json
4
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
  "demo20_zone_16"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rental_package/demo20_rental_package_16.json)

### ตารางบริการ (`schedule`)

รหัส `demo20_schedule_16`

คำถามตัวอย่าง:

- ตารางทดลอง เมฆขาว จองช่วงไหนได้บ้าง
- Demo timetable White Cloud What are the booking hours?
- ตารางทดลอง เมฆขาว เปิดช่วงไหนและพักบำรุงรักษาตอนไหน

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
  "en": "Synthetic White Cloud schedule without maintenance",
  "th": "ตารางสมมุติ เมฆขาว ไม่มีพักบำรุงรักษา"
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
  "demo20_zone_16"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_16.json)

### วันปิด/ข้อยกเว้น (`closure`)

รหัส `demo20_closure_16`

คำถามตัวอย่าง:

- ประกาศวันทดลอง เมฆขาว วันนั้นปิดไหม
- Demo date notice White Cloud Is it closed on that date?
- ประกาศวันทดลอง เมฆขาว วันนั้นเปิดปิดยังไงและเพราะอะไร

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
"2026-12-16"
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
  "en": "Synthetic White Cloud date notice: modified_hours",
  "th": "ประกาศสมมุติ เมฆขาว: modified_hours"
}
```
**resolution_policy_id — known**
```json
"demo20_policy_16"
```
**state — known**
```json
"modified_hours"
```
**zone_ids — known**
```json
[
  "demo20_zone_16"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/closure/demo20_closure_16.json)

### รายการแข่งขันและฉบับกติกา (`competition`)

รหัส `demo20_competition_16`

คำถามตัวอย่าง:

- รายการฝึก เมฆขาว ใช้กติกาฉบับไหน
- Demo event White Cloud Which rulebook release applies?
- รายการฝึก เมฆขาว ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่

**competition_dates — known**
```json
[
  "2026-12-16"
]
```
**coverage — known**
```json
"complete"
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
  "en": "Demo event White Cloud",
  "th": "รายการฝึก เมฆขาว"
}
```
**game_id — known**
```json
"demo20_game_16"
```
**rulebook_release — known**
```json
"DEMO20_REV_16"
```
**supersedes_id — not_applicable**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_16.json)

### ข้อกติกาการแข่งขัน (`competition_rule`)

รหัส `demo20_competition_rule_16`

คำถามตัวอย่าง:

- ข้อการแข่งขันทดลอง เมฆขาว ข้อนี้กำหนดอะไร
- Demo rule White Cloud What does this rule require?
- ข้อการแข่งขันทดลอง เมฆขาว กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม

**competition_id — known**
```json
"demo20_competition_16"
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
  "en": "Demo rule White Cloud",
  "th": "ข้อการแข่งขันทดลอง เมฆขาว"
}
```
**section_number — known**
```json
"2.16"
```
**text — known**
```json
{
  "en": "Fictional clause 16: for Accessibility assistance, follow decision allowed; exception requires written demo operator approval; not actual rules",
  "th": "ข้อสมมุติ 16: การช่วยเข้าถึง ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_16.json)

### ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`)

รหัส `demo20_news_16`

คำถามตัวอย่าง:

- ข่าวทดลอง เมฆขาว ประกาศว่าอะไร
- Demo bulletin White Cloud What does the announcement say?
- ข่าวทดลอง เมฆขาว ประกาศอะไรและกิจกรรมเริ่มจบเมื่อไหร่

**audience_ids — known**
```json
[
  "demo20_audience_16"
]
```
**body — known**
```json
{
  "en": "Synthetic bulletin: Sound Ladder activity for 1–1 people; no actual payment",
  "th": "ข่าวสมมุติ: กิจกรรมบันไดเสียง สำหรับกลุ่ม 1–1 คน; ไม่มีรับเงินจริง"
}
```
**contact_id — known**
```json
"demo20_contact_16"
```
**event_end — known**
```json
"2026-12-16T12:00:00+07:00"
```
**event_start — known**
```json
"2026-12-16T10:00:00+07:00"
```
**registration_url — known**
```json
"https://example.invalid/demo20/register/16"
```
**title — known**
```json
{
  "en": "Demo bulletin White Cloud",
  "th": "ข่าวทดลอง เมฆขาว"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/news/demo20_news_16.json)

### บุคลากร/ทีมที่เปิดเผยได้ (`person`)

รหัส `demo20_person_16`

คำถามตัวอย่าง:

- ผู้ดูแลสมมุติ เมฆขาว รับผิดชอบอะไร
- Fictional host White Cloud What is their role?
- ผู้ดูแลสมมุติ เมฆขาว รับผิดชอบเรื่องอะไรและติดต่อทางไหน

**display_name — known**
```json
{
  "en": "Fictional host White Cloud",
  "th": "ผู้ดูแลสมมุติ เมฆขาว"
}
```
**public_contact_id — known**
```json
"demo20_contact_16"
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
  "en": "Fictional host for Accessibility assistance",
  "th": "ผู้ดูแลสมมุติเรื่อง การช่วยเข้าถึง"
}
```
**team — known**
```json
{
  "en": "Demo White Cloud team",
  "th": "ทีมทดสอบ เมฆขาว"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/person/demo20_person_16.json)

### คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`)

รหัส `demo20_faq_16`

คำถามตัวอย่าง:

- คำถามตัวอย่าง เมฆขาว คำตอบคืออะไร
- Demo enquiry White Cloud What is the answer?
- คำถามตัวอย่าง เมฆขาว คำตอบคืออะไรและใช้กับกรณีไหน

**answer — known**
```json
{
  "en": "Example answer: Fictional rule for Accessibility assistance: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องการช่วยเข้าถึง: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
}
```
**question — known**
```json
{
  "en": "Demo enquiry White Cloud",
  "th": "คำถามตัวอย่าง เมฆขาว"
}
```
**related_ids — known**
```json
[
  "demo20_policy_16",
  "demo20_procedure_16"
]
```
**scope_note — known**
```json
{
  "en": "Only applies to fictional White Cloud scenario",
  "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ เมฆขาว"
}
```
**topic — known**
```json
"DEMO Accessibility assistance"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_16.json)

### การเชื่อมสถานะสด (`live_binding`)

รหัส `demo20_live_binding_16`

คำถามตัวอย่าง:

- ตัวเชื่อมทดลอง เมฆขาว จับคู่สถานะยังไง
- Demo binding White Cloud How are statuses mapped?
- ตัวเชื่อมทดลอง เมฆขาว จับคู่สถานะแบบไหนและเก็บข้อมูลนานเท่าไหร่

**external_resource_key — known**
```json
"DEMO20_EXTERNAL_16"
```
**freshness_policy — known**
```json
{
  "en": "Synthetic TTL 95 seconds; no API call or live status claim",
  "th": "ค่าจำลอง TTL 95 วินาที; ไม่เรียก API และไม่ยืนยันสถานะสด"
}
```
**physical_pool_key — known**
```json
"demo20_pool_16"
```
**provider — known**
```json
"wordpress_booking"
```
**service_id — known**
```json
"demo20_service_16"
```
**status_mapping — known**
```json
[
  {
    "normalized": "free",
    "raw": "DEMO_EMPTY_16"
  },
  {
    "normalized": "occupied",
    "raw": "DEMO_BUSY_16"
  },
  {
    "normalized": "unknown",
    "raw": "DEMO_UNKNOWN_16"
  }
]
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/live_binding/demo20_live_binding_16.json)

