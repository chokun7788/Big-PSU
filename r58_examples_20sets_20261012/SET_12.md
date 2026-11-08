# ชุด 12 — ทองทราย / Sand Gold

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

เกม สถานที่ ราคา กฎ บุคคล และสถานะทั้งหมดในชุดใหม่นี้แต่งขึ้นเพื่อทดสอบ ไม่ได้เป็นข้อมูล PSU หรือเกมที่มีจำหน่ายจริง คำแปลยังไม่ผ่านมนุษย์

แพลตฟอร์มตัวอย่าง: VR • จำนวนผู้เล่น 1–1 • เวลาเล่น 20 นาที / กินช่องจอง 60 นาที

## ข้อมูลครบ 24 หมวด

### ข้อมูลศูนย์ (`center`)

รหัส `demo20_center_12`

คำถามตัวอย่าง:

- ศูนย์ทดลอง ทองทราย อยู่ตรงไหน
- Demo venue Sand Gold Where is it located?
- ศูนย์ทดลอง ทองทราย อยู่ตึกอะไร ชั้นไหน

**address — known**
```json
{
  "en": "Fictional address 84, Example Road, Test District",
  "th": "เลขที่สมมุติ 84 ถนนตัวอย่าง แขวงทดลอง"
}
```
**building — known**
```json
"DEMO Tower C"
```
**description — known**
```json
{
  "en": "Synthetic scenario 12: Sky Laboratory, not a real venue",
  "th": "สถานการณ์ทดลอง 12: ห้องทดลองลอยฟ้า ไม่ใช่สถานที่จริง"
}
```
**floor — known**
```json
"3"
```
**map_url — known**
```json
"https://example.invalid/demo20/map/12"
```
**name — known**
```json
{
  "en": "Demo venue Sand Gold",
  "th": "ศูนย์ทดลอง ทองทราย"
}
```
**operator — known**
```json
{
  "en": "Fictional Sand Gold operator",
  "th": "ผู้ประกอบการสมมุติ ทองทราย"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/center/demo20_center_12.json)

### โซนบริการ (`zone`)

รหัส `demo20_zone_12`

คำถามตัวอย่าง:

- โซนทดลอง ทองทราย มีที่นั่งกี่ที่
- Demo zone Sand Gold How many seats are there?
- โซนทดลอง ทองทราย โซนนี้อยู่ตรงไหนและมีที่นั่งกี่ที่

**description — known**
```json
{
  "en": "Synthetic VR zone for Sky Laboratory",
  "th": "โซนจำลอง VR สำหรับห้องทดลองลอยฟ้า"
}
```
**location — known**
```json
{
  "en": "Test building, floor 3, room 112",
  "th": "อาคารทดสอบ ชั้น 3 ห้อง 112"
}
```
**name — known**
```json
{
  "en": "Demo zone Sand Gold",
  "th": "โซนทดลอง ทองทราย"
}
```
**room_seats — known**
```json
3
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_12.json)

### รุ่นและสเปกอุปกรณ์ (`equipment_model`)

รหัส `demo20_equipment_model_12`

คำถามตัวอย่าง:

- รุ่นอุปกรณ์ ทองทราย สเปกมีอะไรบ้าง
- Demo model Sand Gold What are its specifications?
- รุ่นอุปกรณ์ ทองทราย เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง

**device_type — known**
```json
"vr"
```
**name — known**
```json
{
  "en": "Demo model Sand Gold",
  "th": "รุ่นอุปกรณ์ ทองทราย"
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
    "value": "vr_motion"
  }
]
```
**usage — known**
```json
{
  "en": "Fictional equipment for VR; not a PSU specification",
  "th": "เครื่องสมมุติใช้กับ VR; ห้ามอ้างเป็นสเปกศูนย์"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_12.json)

### เครื่องหรือทรัพยากรจริง (`resource`)

รหัส `demo20_resource_12`

คำถามตัวอย่าง:

- เครื่องทดลอง ทองทราย เล่นพร้อมกันได้กี่คน
- Demo station Sand Gold How many people can play at once?
- เครื่องทดลอง ทองทราย เครื่องยังใช้งานได้ไหมและรองรับกี่คน

**capacity_persons — known**
```json
1
```
**equipment_model_ids — known**
```json
[
  "demo20_equipment_model_12"
]
```
**name — known**
```json
{
  "en": "Demo station Sand Gold",
  "th": "เครื่องทดลอง ทองทราย"
}
```
**operational_status — known**
```json
"in_service"
```
**physical_pool_key — known**
```json
"demo20_pool_12"
```
**zone_id — known**
```json
"demo20_zone_12"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/resource/demo20_resource_12.json)

### รายการที่เลือกในระบบจอง (`service`)

รหัส `demo20_service_12`

คำถามตัวอย่าง:

- รอบทดลอง ทองทราย หนึ่งรอบเล่นได้กี่นาที
- Demo session Sand Gold How many minutes does one session last?
- รอบทดลอง ทองทราย เวลาเล่นกับเวลาที่กินช่องจองกี่นาที

**booking_product_key — known**
```json
"DEMO20_BOOKING_12"
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
  "en": "Demo session Sand Gold",
  "th": "รอบทดลอง ทองทราย"
}
```
**occupancy_minutes — known**
```json
60
```
**platform — known**
```json
"VR"
```
**resource_ids — known**
```json
[
  "demo20_resource_12"
]
```
**session_minutes — known**
```json
20
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_12.json)

### ข้อมูลเกม (`game`)

รหัส `demo20_game_12`

คำถามตัวอย่าง:

- เกมสมมุติ ทองทราย เล่นยังไง
- Fictional game Sand Gold How do I play it?
- เกมสมมุติ ทองทราย เกมเกี่ยวกับอะไรและเล่นยังไง

**age_rating — known**
```json
{
  "en": "Synthetic DEMO rating 3",
  "th": "เรตอายุสมมุติ DEMO 3"
}
```
**edition — known**
```json
"DEMO fiction revision 12"
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
  "en": "Assemble virtual machines using motion inputs; follow the demonstration controls",
  "th": "หยิบวัตถุเสมือนประกอบเครื่องจักร; ใช้คำสั่งตามชุดควบคุมทดลอง"
}
```
**publisher_url — known**
```json
"https://example.invalid/demo20/fictional-game/12"
```
**summary — known**
```json
{
  "en": "Fictional test game: Assemble virtual machines using motion inputs",
  "th": "เกมแต่งขึ้นเพื่อทดสอบ: หยิบวัตถุเสมือนประกอบเครื่องจักร"
}
```
**supported_platforms — known**
```json
[
  "VR",
  "PC"
]
```
**title — known**
```json
{
  "en": "Fictional Sky Laboratory",
  "th": "เกมสมมุติ ห้องทดลองลอยฟ้า"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_12.json)

### กลุ่มผู้ใช้ (`audience`)

รหัส `demo20_audience_12`

คำถามตัวอย่าง:

- กลุ่มผู้ใช้ ทองทราย ต้องใช้หลักฐานอะไร
- Demo visitors Sand Gold What proof is required?
- กลุ่มผู้ใช้ ทองทราย ใครใช้สิทธิ์กลุ่มนี้ได้และต้องแสดงหลักฐานอะไร

**eligibility — known**
```json
{
  "en": "Fictional group 12: demo sessions only",
  "th": "ผู้ใช้สมมุติกลุ่ม 12: ใช้บริการตามรอบทดลอง"
}
```
**name — known**
```json
{
  "en": "Demo visitors Sand Gold",
  "th": "กลุ่มผู้ใช้ ทองทราย"
}
```
**required_proofs — known**
```json
[]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/audience/demo20_audience_12.json)

### ติดต่อ (`contact`)

รหัส `demo20_contact_12`

คำถามตัวอย่าง:

- ช่องทางช่วยเหลือ ทองทราย ติดต่อทางไหน
- Demo help channel Sand Gold How can I contact them?
- ช่องทางช่วยเหลือ ทองทราย ติดต่อที่ไหนและติดต่อได้ช่วงไหน

**channel — known**
```json
"facebook"
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
  "en": "Fictional support for Safety boundary",
  "th": "สอบถามสมมุติเรื่อง พื้นที่ปลอดภัย"
}
```
**value — known**
```json
"https://example.invalid/demo20/social/12"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_12.json)

### ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`)

รหัส `demo20_procedure_12`

คำถามตัวอย่าง:

- ขั้นตอนทดลอง ทองทราย ต้องทำยังไงบ้าง
- Demo procedure Sand Gold What steps should I follow?
- ขั้นตอนทดลอง ทองทราย มีขั้นตอนอะไรและต้องใช้เอกสารอะไร

**deadline_minutes — known**
```json
15
```
**outcome — known**
```json
{
  "en": "Demo outcome: Safety boundary checked",
  "th": "ผลทดสอบ: ตรวจสอบ พื้นที่ปลอดภัย เสร็จ"
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
      "en": "Select the fictional Sand Gold service",
      "th": "เลือกบริการสมมุติ ทองทราย"
    },
    "order": 1
  },
  {
    "contact_id": "demo20_contact_12",
    "instruction": {
      "en": "Check names and conditions before confirming",
      "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
    },
    "order": 2
  },
  {
    "contact_id": "demo20_contact_12",
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
"DEMO Safety boundary"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_12.json)

### นโยบายและกฎศูนย์ (`policy`)

รหัส `demo20_policy_12`

คำถามตัวอย่าง:

- ข้อกำหนดทดลอง ทองทราย กฎเป็นยังไง
- Demo policy Sand Gold What are the rules?
- ข้อกำหนดทดลอง ทองทราย อนุญาตไหมและมีข้อยกเว้นอะไร

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
  "en": "Fictional rule for Safety boundary: required; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "กติกาสมมุติเรื่องพื้นที่ปลอดภัย: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
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
"demo20_procedure_12"
```
**subject — known**
```json
{
  "en": "Demo policy Sand Gold",
  "th": "ข้อกำหนดทดลอง ทองทราย"
}
```
**topic — known**
```json
"DEMO Safety boundary"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/policy/demo20_policy_12.json)

### สิ่งอำนวยความสะดวก (`facility`)

รหัส `demo20_facility_12`

คำถามตัวอย่าง:

- พื้นที่พัก ทองทราย อยู่ตรงไหนในร้าน
- Demo amenity Sand Gold Where in the venue is it?
- พื้นที่พัก ทองทราย อยู่ตรงไหนและคนที่ต้องการความช่วยเหลือเข้าใช้ยังไง

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
  "en": "Headset fitting point in demo room 112",
  "th": "จุดสวมอุปกรณ์ อยู่ห้องทดสอบ 112"
}
```
**name — known**
```json
{
  "en": "Demo amenity Sand Gold",
  "th": "พื้นที่พัก ทองทราย"
}
```
**usage_conditions — known**
```json
{
  "en": "Demo sessions only; may use while waiting",
  "th": "ใช้ตามรอบทดลอง; ใช้ได้ระหว่างรอ"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/facility/demo20_facility_12.json)

### เกมที่ศูนย์มีให้เล่นจริง (`game_service`)

รหัส `demo20_game_service_12`

คำถามตัวอย่าง:

- การติดตั้งทดลอง ทองทราย มีให้เล่นหรือยัง
- Demo installation Sand Gold Is this game offered?
- การติดตั้งทดลอง ทองทราย มีให้เล่นไหมและติดตั้งรุ่นไหน

**account_policy_id — known**
```json
"demo20_policy_12"
```
**game_id — known**
```json
"demo20_game_12"
```
**game_version — known**
```json
"DEMO BUILD 12"
```
**installed_resource_ids — known**
```json
[
  "demo20_resource_12"
]
```
**offered — known**
```json
true
```
**service_id — known**
```json
"demo20_service_12"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_service/demo20_game_service_12.json)

### รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`)

รหัส `demo20_game_mode_12`

คำถามตัวอย่าง:

- โหมดทดลอง ทองทราย เล่นพร้อมกันได้สูงสุดกี่คน
- Demo mode Sand Gold How many people can play together at most?
- โหมดทดลอง ทองทราย ต้องมีขั้นต่ำกี่คนและเล่นได้สูงสุดกี่คน

**game_id — known**
```json
"demo20_game_12"
```
**mode_name — known**
```json
{
  "en": "Demo mode Sand Gold",
  "th": "โหมดทดลอง ทองทราย"
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
"VR"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_mode/demo20_game_mode_12.json)

### วิธีเล่นและปุ่ม (`control_set`)

รหัส `demo20_control_set_12`

คำถามตัวอย่าง:

- ชุดควบคุมทดลอง ทองทราย ปุ่มอะไรบ้าง
- Demo controls Sand Gold What are the controls?
- ชุดควบคุมทดลอง ทองทราย ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร

**bindings — known**
```json
[
  {
    "action": {
      "en": "Confirm",
      "th": "ยืนยัน"
    },
    "buttons": [
      "DEMO_vr_motion_1"
    ],
    "context": {
      "en": "Fictional input for Sky Laboratory",
      "th": "คำสั่งสมมุติของ ห้องทดลองลอยฟ้า"
    },
    "gesture": "press"
  }
]
```
**game_id — known**
```json
"demo20_game_12"
```
**game_version — known**
```json
"DEMO BUILD 12"
```
**input_device — known**
```json
"vr_motion"
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
"VR"
```
**preset — known**
```json
"DEMO_LAYOUT_12"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_12.json)

### ราคาต่อบริการ (`rate`)

รหัส `demo20_rate_12`

คำถามตัวอย่าง:

- อัตราทดลอง ทองทราย ราคาเท่าไหร่
- Demo tariff Sand Gold How much does it cost?
- อัตราทดลอง ทองทราย ราคาเท่าไหร่และได้กี่นาที

**amount_minor — known**
```json
5000
```
**audience_id — known**
```json
"demo20_audience_12"
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
20
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
"demo20_service_12"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rate/demo20_rate_12.json)

### ราคาเหมาโซน/ห้อง (`rental_package`)

รหัส `demo20_rental_package_12`

คำถามตัวอย่าง:

- แพ็กเกจทดลอง ทองทราย เหมาเท่าไหร่
- Demo package Sand Gold How much is the rental?
- แพ็กเกจทดลอง ทองทราย ราคาเหมาเท่าไหร่และรวมอุปกรณ์อะไร

**amount_minor — known**
```json
16250
```
**audience_id — known**
```json
"demo20_audience_12"
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
  "en": "Fictional Sand Gold station and VR inputs",
  "th": "เครื่องสมมุติ ทองทราย พร้อมอุปกรณ์ VR"
}
```
**name — known**
```json
{
  "en": "Demo package Sand Gold",
  "th": "แพ็กเกจทดลอง ทองทราย"
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
  "demo20_zone_12"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rental_package/demo20_rental_package_12.json)

### ตารางบริการ (`schedule`)

รหัส `demo20_schedule_12`

คำถามตัวอย่าง:

- ตารางทดลอง ทองทราย จองช่วงไหนได้บ้าง
- Demo timetable Sand Gold What are the booking hours?
- ตารางทดลอง ทองทราย เปิดช่วงไหนและพักบำรุงรักษาตอนไหน

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
  "en": "Synthetic Sand Gold schedule without maintenance",
  "th": "ตารางสมมุติ ทองทราย ไม่มีพักบำรุงรักษา"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```
**weekday — known**
```json
5
```
**zone_ids — known**
```json
[
  "demo20_zone_12"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_12.json)

### วันปิด/ข้อยกเว้น (`closure`)

รหัส `demo20_closure_12`

คำถามตัวอย่าง:

- ประกาศวันทดลอง ทองทราย วันนั้นปิดไหม
- Demo date notice Sand Gold Is it closed on that date?
- ประกาศวันทดลอง ทองทราย วันนั้นเปิดปิดยังไงและเพราะอะไร

**bookable_periods — known**
```json
[]
```
**local_date — known**
```json
"2026-12-12"
```
**open_periods — known**
```json
[]
```
**reason — known**
```json
{
  "en": "Synthetic Sand Gold date notice: closed",
  "th": "ประกาศสมมุติ ทองทราย: closed"
}
```
**resolution_policy_id — known**
```json
"demo20_policy_12"
```
**state — known**
```json
"closed"
```
**zone_ids — known**
```json
[
  "demo20_zone_12"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/closure/demo20_closure_12.json)

### รายการแข่งขันและฉบับกติกา (`competition`)

รหัส `demo20_competition_12`

คำถามตัวอย่าง:

- รายการฝึก ทองทราย ใช้กติกาฉบับไหน
- Demo event Sand Gold Which rulebook release applies?
- รายการฝึก ทองทราย ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่

**competition_dates — known**
```json
[
  "2026-12-12"
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
  "en": "Demo event Sand Gold",
  "th": "รายการฝึก ทองทราย"
}
```
**game_id — known**
```json
"demo20_game_12"
```
**rulebook_release — known**
```json
"DEMO20_REV_12"
```
**supersedes_id — not_applicable**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_12.json)

### ข้อกติกาการแข่งขัน (`competition_rule`)

รหัส `demo20_competition_rule_12`

คำถามตัวอย่าง:

- ข้อการแข่งขันทดลอง ทองทราย ข้อนี้กำหนดอะไร
- Demo rule Sand Gold What does this rule require?
- ข้อการแข่งขันทดลอง ทองทราย กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม

**competition_id — known**
```json
"demo20_competition_12"
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
  "en": "Demo rule Sand Gold",
  "th": "ข้อการแข่งขันทดลอง ทองทราย"
}
```
**section_number — known**
```json
"3.12"
```
**text — known**
```json
{
  "en": "Fictional clause 12: for Safety boundary, follow decision required; exception requires written demo operator approval; not actual rules",
  "th": "ข้อสมมุติ 12: พื้นที่ปลอดภัย ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_12.json)

### ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`)

รหัส `demo20_news_12`

คำถามตัวอย่าง:

- ข่าวทดลอง ทองทราย ประกาศว่าอะไร
- Demo bulletin Sand Gold What does the announcement say?
- ข่าวทดลอง ทองทราย ประกาศอะไรและกิจกรรมเริ่มจบเมื่อไหร่

**audience_ids — known**
```json
[
  "demo20_audience_12"
]
```
**body — known**
```json
{
  "en": "Synthetic bulletin: Sky Laboratory activity for 1–1 people; no actual payment",
  "th": "ข่าวสมมุติ: กิจกรรมห้องทดลองลอยฟ้า สำหรับกลุ่ม 1–1 คน; ไม่มีรับเงินจริง"
}
```
**contact_id — known**
```json
"demo20_contact_12"
```
**event_end — known**
```json
"2026-12-12T12:00:00+07:00"
```
**event_start — known**
```json
"2026-12-12T10:00:00+07:00"
```
**registration_url — known**
```json
"https://example.invalid/demo20/register/12"
```
**title — known**
```json
{
  "en": "Demo bulletin Sand Gold",
  "th": "ข่าวทดลอง ทองทราย"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/news/demo20_news_12.json)

### บุคลากร/ทีมที่เปิดเผยได้ (`person`)

รหัส `demo20_person_12`

คำถามตัวอย่าง:

- ผู้ดูแลสมมุติ ทองทราย รับผิดชอบอะไร
- Fictional host Sand Gold What is their role?
- ผู้ดูแลสมมุติ ทองทราย รับผิดชอบเรื่องอะไรและติดต่อทางไหน

**display_name — known**
```json
{
  "en": "Fictional host Sand Gold",
  "th": "ผู้ดูแลสมมุติ ทองทราย"
}
```
**public_contact_id — known**
```json
"demo20_contact_12"
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
  "en": "Fictional host for Safety boundary",
  "th": "ผู้ดูแลสมมุติเรื่อง พื้นที่ปลอดภัย"
}
```
**team — known**
```json
{
  "en": "Demo Sand Gold team",
  "th": "ทีมทดสอบ ทองทราย"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/person/demo20_person_12.json)

### คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`)

รหัส `demo20_faq_12`

คำถามตัวอย่าง:

- คำถามตัวอย่าง ทองทราย คำตอบคืออะไร
- Demo enquiry Sand Gold What is the answer?
- คำถามตัวอย่าง ทองทราย คำตอบคืออะไรและใช้กับกรณีไหน

**answer — known**
```json
{
  "en": "Example answer: Fictional rule for Safety boundary: required; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องพื้นที่ปลอดภัย: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
}
```
**question — known**
```json
{
  "en": "Demo enquiry Sand Gold",
  "th": "คำถามตัวอย่าง ทองทราย"
}
```
**related_ids — known**
```json
[
  "demo20_policy_12",
  "demo20_procedure_12"
]
```
**scope_note — known**
```json
{
  "en": "Only applies to fictional Sand Gold scenario",
  "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ทองทราย"
}
```
**topic — known**
```json
"DEMO Safety boundary"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_12.json)

### การเชื่อมสถานะสด (`live_binding`)

รหัส `demo20_live_binding_12`

คำถามตัวอย่าง:

- ตัวเชื่อมทดลอง ทองทราย จับคู่สถานะยังไง
- Demo binding Sand Gold How are statuses mapped?
- ตัวเชื่อมทดลอง ทองทราย จับคู่สถานะแบบไหนและเก็บข้อมูลนานเท่าไหร่

**external_resource_key — known**
```json
"DEMO20_EXTERNAL_12"
```
**freshness_policy — known**
```json
{
  "en": "Synthetic TTL 75 seconds; no API call or live status claim",
  "th": "ค่าจำลอง TTL 75 วินาที; ไม่เรียก API และไม่ยืนยันสถานะสด"
}
```
**physical_pool_key — known**
```json
"demo20_pool_12"
```
**provider — known**
```json
"wordpress_booking"
```
**service_id — known**
```json
"demo20_service_12"
```
**status_mapping — known**
```json
[
  {
    "normalized": "free",
    "raw": "DEMO_EMPTY_12"
  },
  {
    "normalized": "occupied",
    "raw": "DEMO_BUSY_12"
  },
  {
    "normalized": "unknown",
    "raw": "DEMO_UNKNOWN_12"
  }
]
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/live_binding/demo20_live_binding_12.json)

