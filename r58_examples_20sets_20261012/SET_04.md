# ชุด 04 — สายหมอก / Mist

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

เกม สถานที่ ราคา กฎ บุคคล และสถานะทั้งหมดในชุดใหม่นี้แต่งขึ้นเพื่อทดสอบ ไม่ได้เป็นข้อมูล PSU หรือเกมที่มีจำหน่ายจริง คำแปลยังไม่ผ่านมนุษย์

แพลตฟอร์มตัวอย่าง: Cockpit • จำนวนผู้เล่น 1–1 • เวลาเล่น 45 นาที / กินช่องจอง 60 นาที

## ข้อมูลครบ 24 หมวด

### ข้อมูลศูนย์ (`center`)

รหัส `demo20_center_04`

คำถามตัวอย่าง:

- ศูนย์ทดลอง สายหมอก อยู่ตรงไหน
- Demo venue Mist Where is it located?
- ศูนย์ทดลอง สายหมอก อยู่ตึกอะไร ชั้นไหน

**address — known**
```json
{
  "en": "Fictional address 28, Example Road, Test District",
  "th": "เลขที่สมมุติ 28 ถนนตัวอย่าง แขวงทดลอง"
}
```
**building — known**
```json
"DEMO Tower E"
```
**description — known**
```json
{
  "en": "Synthetic scenario 4: Silver Curve, not a real venue",
  "th": "สถานการณ์ทดลอง 4: ทางโค้งสีเงิน ไม่ใช่สถานที่จริง"
}
```
**floor — known**
```json
"5"
```
**map_url — known**
```json
"https://example.invalid/demo20/map/4"
```
**name — known**
```json
{
  "en": "Demo venue Mist",
  "th": "ศูนย์ทดลอง สายหมอก"
}
```
**operator — known**
```json
{
  "en": "Fictional Mist operator",
  "th": "ผู้ประกอบการสมมุติ สายหมอก"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/center/demo20_center_04.json)

### โซนบริการ (`zone`)

รหัส `demo20_zone_04`

คำถามตัวอย่าง:

- โซนทดลอง สายหมอก มีที่นั่งกี่ที่
- Demo zone Mist How many seats are there?
- โซนทดลอง สายหมอก โซนนี้อยู่ตรงไหนและมีที่นั่งกี่ที่

**description — known**
```json
{
  "en": "Synthetic Cockpit zone for Silver Curve",
  "th": "โซนจำลอง Cockpit สำหรับทางโค้งสีเงิน"
}
```
**location — known**
```json
{
  "en": "Test building, floor 5, room 104",
  "th": "อาคารทดสอบ ชั้น 5 ห้อง 104"
}
```
**name — known**
```json
{
  "en": "Demo zone Mist",
  "th": "โซนทดลอง สายหมอก"
}
```
**room_seats — known**
```json
4
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_04.json)

### รุ่นและสเปกอุปกรณ์ (`equipment_model`)

รหัส `demo20_equipment_model_04`

คำถามตัวอย่าง:

- รุ่นอุปกรณ์ สายหมอก สเปกมีอะไรบ้าง
- Demo model Mist What are its specifications?
- รุ่นอุปกรณ์ สายหมอก เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง

**device_type — known**
```json
"wheel"
```
**name — known**
```json
{
  "en": "Demo model Mist",
  "th": "รุ่นอุปกรณ์ สายหมอก"
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
    "value": "racing_wheel"
  }
]
```
**usage — known**
```json
{
  "en": "Fictional equipment for Cockpit; not a PSU specification",
  "th": "เครื่องสมมุติใช้กับ Cockpit; ห้ามอ้างเป็นสเปกศูนย์"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_04.json)

### เครื่องหรือทรัพยากรจริง (`resource`)

รหัส `demo20_resource_04`

คำถามตัวอย่าง:

- เครื่องทดลอง สายหมอก เล่นพร้อมกันได้กี่คน
- Demo station Mist How many people can play at once?
- เครื่องทดลอง สายหมอก เครื่องยังใช้งานได้ไหมและรองรับกี่คน

**capacity_persons — known**
```json
1
```
**equipment_model_ids — known**
```json
[
  "demo20_equipment_model_04"
]
```
**name — known**
```json
{
  "en": "Demo station Mist",
  "th": "เครื่องทดลอง สายหมอก"
}
```
**operational_status — known**
```json
"in_service"
```
**physical_pool_key — known**
```json
"demo20_pool_04"
```
**zone_id — known**
```json
"demo20_zone_04"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/resource/demo20_resource_04.json)

### รายการที่เลือกในระบบจอง (`service`)

รหัส `demo20_service_04`

คำถามตัวอย่าง:

- รอบทดลอง สายหมอก หนึ่งรอบเล่นได้กี่นาที
- Demo session Mist How many minutes does one session last?
- รอบทดลอง สายหมอก เวลาเล่นกับเวลาที่กินช่องจองกี่นาที

**booking_product_key — known**
```json
"DEMO20_BOOKING_04"
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
  "en": "Demo session Mist",
  "th": "รอบทดลอง สายหมอก"
}
```
**occupancy_minutes — known**
```json
60
```
**platform — known**
```json
"Cockpit"
```
**resource_ids — known**
```json
[
  "demo20_resource_04"
]
```
**session_minutes — known**
```json
45
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_04.json)

### ข้อมูลเกม (`game`)

รหัส `demo20_game_04`

คำถามตัวอย่าง:

- เกมสมมุติ สายหมอก เล่นยังไง
- Fictional game Mist How do I play it?
- เกมสมมุติ สายหมอก เกมเกี่ยวกับอะไรและเล่นยังไง

**age_rating — known**
```json
{
  "en": "Synthetic DEMO rating 3",
  "th": "เรตอายุสมมุติ DEMO 3"
}
```
**edition — known**
```json
"DEMO fiction revision 4"
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
  "en": "Practise braking and cornering with a wheel; follow the demonstration controls",
  "th": "ฝึกเบรกและเข้าโค้งด้วยพวงมาลัย; ใช้คำสั่งตามชุดควบคุมทดลอง"
}
```
**publisher_url — known**
```json
"https://example.invalid/demo20/fictional-game/4"
```
**summary — known**
```json
{
  "en": "Fictional test game: Practise braking and cornering with a wheel",
  "th": "เกมแต่งขึ้นเพื่อทดสอบ: ฝึกเบรกและเข้าโค้งด้วยพวงมาลัย"
}
```
**supported_platforms — known**
```json
[
  "Cockpit",
  "PC"
]
```
**title — known**
```json
{
  "en": "Fictional Silver Curve",
  "th": "เกมสมมุติ ทางโค้งสีเงิน"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_04.json)

### กลุ่มผู้ใช้ (`audience`)

รหัส `demo20_audience_04`

คำถามตัวอย่าง:

- กลุ่มผู้ใช้ สายหมอก ต้องใช้หลักฐานอะไร
- Demo visitors Mist What proof is required?
- กลุ่มผู้ใช้ สายหมอก ใครใช้สิทธิ์กลุ่มนี้ได้และต้องแสดงหลักฐานอะไร

**eligibility — known**
```json
{
  "en": "Fictional group 4: demo sessions only",
  "th": "ผู้ใช้สมมุติกลุ่ม 4: ใช้บริการตามรอบทดลอง"
}
```
**name — known**
```json
{
  "en": "Demo visitors Mist",
  "th": "กลุ่มผู้ใช้ สายหมอก"
}
```
**required_proofs — known**
```json
[]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/audience/demo20_audience_04.json)

### ติดต่อ (`contact`)

รหัส `demo20_contact_04`

คำถามตัวอย่าง:

- ช่องทางช่วยเหลือ สายหมอก ติดต่อทางไหน
- Demo help channel Mist How can I contact them?
- ช่องทางช่วยเหลือ สายหมอก ติดต่อที่ไหนและติดต่อได้ช่วงไหน

**channel — known**
```json
"phone"
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
  "en": "Fictional support for Seat adjustment",
  "th": "สอบถามสมมุติเรื่อง ปรับเบาะ"
}
```
**value — known**
```json
"DEMO-NON-DIALABLE-04"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_04.json)

### ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`)

รหัส `demo20_procedure_04`

คำถามตัวอย่าง:

- ขั้นตอนทดลอง สายหมอก ต้องทำยังไงบ้าง
- Demo procedure Mist What steps should I follow?
- ขั้นตอนทดลอง สายหมอก มีขั้นตอนอะไรและต้องใช้เอกสารอะไร

**deadline_minutes — known**
```json
60
```
**outcome — known**
```json
{
  "en": "Demo outcome: Seat adjustment checked",
  "th": "ผลทดสอบ: ตรวจสอบ ปรับเบาะ เสร็จ"
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
      "en": "Select the fictional Mist service",
      "th": "เลือกบริการสมมุติ สายหมอก"
    },
    "order": 1
  },
  {
    "contact_id": "demo20_contact_04",
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
"DEMO Seat adjustment"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_04.json)

### นโยบายและกฎศูนย์ (`policy`)

รหัส `demo20_policy_04`

คำถามตัวอย่าง:

- ข้อกำหนดทดลอง สายหมอก กฎเป็นยังไง
- Demo policy Mist What are the rules?
- ข้อกำหนดทดลอง สายหมอก อนุญาตไหมและมีข้อยกเว้นอะไร

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
  "en": "Fictional rule for Seat adjustment: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "กติกาสมมุติเรื่องปรับเบาะ: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
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
"demo20_procedure_04"
```
**subject — known**
```json
{
  "en": "Demo policy Mist",
  "th": "ข้อกำหนดทดลอง สายหมอก"
}
```
**topic — known**
```json
"DEMO Seat adjustment"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/policy/demo20_policy_04.json)

### สิ่งอำนวยความสะดวก (`facility`)

รหัส `demo20_facility_04`

คำถามตัวอย่าง:

- พื้นที่พัก สายหมอก อยู่ตรงไหนในร้าน
- Demo amenity Mist Where in the venue is it?
- พื้นที่พัก สายหมอก อยู่ตรงไหนและคนที่ต้องการความช่วยเหลือเข้าใช้ยังไง

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
  "en": "Seat adjustment point in demo room 104",
  "th": "จุดปรับเบาะ อยู่ห้องทดสอบ 104"
}
```
**name — known**
```json
{
  "en": "Demo amenity Mist",
  "th": "พื้นที่พัก สายหมอก"
}
```
**usage_conditions — known**
```json
{
  "en": "Demo sessions only; may use while waiting",
  "th": "ใช้ตามรอบทดลอง; ใช้ได้ระหว่างรอ"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/facility/demo20_facility_04.json)

### เกมที่ศูนย์มีให้เล่นจริง (`game_service`)

รหัส `demo20_game_service_04`

คำถามตัวอย่าง:

- การติดตั้งทดลอง สายหมอก มีให้เล่นหรือยัง
- Demo installation Mist Is this game offered?
- การติดตั้งทดลอง สายหมอก มีให้เล่นไหมและติดตั้งรุ่นไหน

**account_policy_id — known**
```json
"demo20_policy_04"
```
**game_id — known**
```json
"demo20_game_04"
```
**game_version — known**
```json
"DEMO BUILD 4"
```
**installed_resource_ids — known**
```json
[
  "demo20_resource_04"
]
```
**offered — known**
```json
true
```
**service_id — known**
```json
"demo20_service_04"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_service/demo20_game_service_04.json)

### รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`)

รหัส `demo20_game_mode_04`

คำถามตัวอย่าง:

- โหมดทดลอง สายหมอก เล่นพร้อมกันได้สูงสุดกี่คน
- Demo mode Mist How many people can play together at most?
- โหมดทดลอง สายหมอก ต้องมีขั้นต่ำกี่คนและเล่นได้สูงสุดกี่คน

**game_id — known**
```json
"demo20_game_04"
```
**mode_name — known**
```json
{
  "en": "Demo mode Mist",
  "th": "โหมดทดลอง สายหมอก"
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
"Cockpit"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_mode/demo20_game_mode_04.json)

### วิธีเล่นและปุ่ม (`control_set`)

รหัส `demo20_control_set_04`

คำถามตัวอย่าง:

- ชุดควบคุมทดลอง สายหมอก ปุ่มอะไรบ้าง
- Demo controls Mist What are the controls?
- ชุดควบคุมทดลอง สายหมอก ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร

**bindings — known**
```json
[
  {
    "action": {
      "en": "Confirm",
      "th": "ยืนยัน"
    },
    "buttons": [
      "DEMO_racing_wheel_1"
    ],
    "context": {
      "en": "Fictional input for Silver Curve",
      "th": "คำสั่งสมมุติของ ทางโค้งสีเงิน"
    },
    "gesture": "press"
  },
  {
    "action": {
      "en": "Move",
      "th": "เคลื่อนที่"
    },
    "buttons": [
      "DEMO_racing_wheel_2"
    ],
    "context": {
      "en": "Fictional input for Silver Curve",
      "th": "คำสั่งสมมุติของ ทางโค้งสีเงิน"
    },
    "gesture": "press"
  }
]
```
**game_id — known**
```json
"demo20_game_04"
```
**game_version — known**
```json
"DEMO BUILD 4"
```
**input_device — known**
```json
"racing_wheel"
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
"Cockpit"
```
**preset — known**
```json
"DEMO_LAYOUT_4"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_04.json)

### ราคาต่อบริการ (`rate`)

รหัส `demo20_rate_04`

คำถามตัวอย่าง:

- อัตราทดลอง สายหมอก ราคาเท่าไหร่
- Demo tariff Mist How much does it cost?
- อัตราทดลอง สายหมอก ราคาเท่าไหร่และได้กี่นาที

**amount_minor — known**
```json
9500
```
**audience_id — known**
```json
"demo20_audience_04"
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
1
```
**persons_min — known**
```json
1
```
**service_id — known**
```json
"demo20_service_04"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rate/demo20_rate_04.json)

### ราคาเหมาโซน/ห้อง (`rental_package`)

รหัส `demo20_rental_package_04`

คำถามตัวอย่าง:

- แพ็กเกจทดลอง สายหมอก เหมาเท่าไหร่
- Demo package Mist How much is the rental?
- แพ็กเกจทดลอง สายหมอก ราคาเหมาเท่าไหร่และรวมอุปกรณ์อะไร

**amount_minor — known**
```json
29750
```
**audience_id — known**
```json
"demo20_audience_04"
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
  "en": "Fictional Mist station and Cockpit inputs",
  "th": "เครื่องสมมุติ สายหมอก พร้อมอุปกรณ์ Cockpit"
}
```
**name — known**
```json
{
  "en": "Demo package Mist",
  "th": "แพ็กเกจทดลอง สายหมอก"
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
  "demo20_zone_04"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rental_package/demo20_rental_package_04.json)

### ตารางบริการ (`schedule`)

รหัส `demo20_schedule_04`

คำถามตัวอย่าง:

- ตารางทดลอง สายหมอก จองช่วงไหนได้บ้าง
- Demo timetable Mist What are the booking hours?
- ตารางทดลอง สายหมอก เปิดช่วงไหนและพักบำรุงรักษาตอนไหน

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
  "en": "Synthetic Mist schedule without maintenance",
  "th": "ตารางสมมุติ สายหมอก ไม่มีพักบำรุงรักษา"
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
  "demo20_zone_04"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_04.json)

### วันปิด/ข้อยกเว้น (`closure`)

รหัส `demo20_closure_04`

คำถามตัวอย่าง:

- ประกาศวันทดลอง สายหมอก วันนั้นปิดไหม
- Demo date notice Mist Is it closed on that date?
- ประกาศวันทดลอง สายหมอก วันนั้นเปิดปิดยังไงและเพราะอะไร

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
"2026-12-04"
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
  "en": "Synthetic Mist date notice: modified_hours",
  "th": "ประกาศสมมุติ สายหมอก: modified_hours"
}
```
**resolution_policy_id — known**
```json
"demo20_policy_04"
```
**state — known**
```json
"modified_hours"
```
**zone_ids — known**
```json
[
  "demo20_zone_04"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/closure/demo20_closure_04.json)

### รายการแข่งขันและฉบับกติกา (`competition`)

รหัส `demo20_competition_04`

คำถามตัวอย่าง:

- รายการฝึก สายหมอก ใช้กติกาฉบับไหน
- Demo event Mist Which rulebook release applies?
- รายการฝึก สายหมอก ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่

**competition_dates — known**
```json
[
  "2026-12-04"
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
  "en": "Demo event Mist",
  "th": "รายการฝึก สายหมอก"
}
```
**game_id — known**
```json
"demo20_game_04"
```
**rulebook_release — known**
```json
"DEMO20_REV_4"
```
**supersedes_id — not_applicable**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_04.json)

### ข้อกติกาการแข่งขัน (`competition_rule`)

รหัส `demo20_competition_rule_04`

คำถามตัวอย่าง:

- ข้อการแข่งขันทดลอง สายหมอก ข้อนี้กำหนดอะไร
- Demo rule Mist What does this rule require?
- ข้อการแข่งขันทดลอง สายหมอก กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม

**competition_id — known**
```json
"demo20_competition_04"
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
  "en": "Demo rule Mist",
  "th": "ข้อการแข่งขันทดลอง สายหมอก"
}
```
**section_number — known**
```json
"5.4"
```
**text — known**
```json
{
  "en": "Fictional clause 4: for Seat adjustment, follow decision conditional; exception requires written demo operator approval; not actual rules",
  "th": "ข้อสมมุติ 4: ปรับเบาะ ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_04.json)

### ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`)

รหัส `demo20_news_04`

คำถามตัวอย่าง:

- ข่าวทดลอง สายหมอก ประกาศว่าอะไร
- Demo bulletin Mist What does the announcement say?
- ข่าวทดลอง สายหมอก ประกาศอะไรและกิจกรรมเริ่มจบเมื่อไหร่

**audience_ids — known**
```json
[
  "demo20_audience_04"
]
```
**body — known**
```json
{
  "en": "Synthetic bulletin: Silver Curve activity for 1–1 people; no actual payment",
  "th": "ข่าวสมมุติ: กิจกรรมทางโค้งสีเงิน สำหรับกลุ่ม 1–1 คน; ไม่มีรับเงินจริง"
}
```
**contact_id — known**
```json
"demo20_contact_04"
```
**event_end — known**
```json
"2026-12-04T12:00:00+07:00"
```
**event_start — known**
```json
"2026-12-04T10:00:00+07:00"
```
**registration_url — known**
```json
"https://example.invalid/demo20/register/4"
```
**title — known**
```json
{
  "en": "Demo bulletin Mist",
  "th": "ข่าวทดลอง สายหมอก"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/news/demo20_news_04.json)

### บุคลากร/ทีมที่เปิดเผยได้ (`person`)

รหัส `demo20_person_04`

คำถามตัวอย่าง:

- ผู้ดูแลสมมุติ สายหมอก รับผิดชอบอะไร
- Fictional host Mist What is their role?
- ผู้ดูแลสมมุติ สายหมอก รับผิดชอบเรื่องอะไรและติดต่อทางไหน

**display_name — known**
```json
{
  "en": "Fictional host Mist",
  "th": "ผู้ดูแลสมมุติ สายหมอก"
}
```
**public_contact_id — known**
```json
"demo20_contact_04"
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
  "en": "Fictional host for Seat adjustment",
  "th": "ผู้ดูแลสมมุติเรื่อง ปรับเบาะ"
}
```
**team — known**
```json
{
  "en": "Demo Mist team",
  "th": "ทีมทดสอบ สายหมอก"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/person/demo20_person_04.json)

### คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`)

รหัส `demo20_faq_04`

คำถามตัวอย่าง:

- คำถามตัวอย่าง สายหมอก คำตอบคืออะไร
- Demo enquiry Mist What is the answer?
- คำถามตัวอย่าง สายหมอก คำตอบคืออะไรและใช้กับกรณีไหน

**answer — known**
```json
{
  "en": "Example answer: Fictional rule for Seat adjustment: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องปรับเบาะ: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
}
```
**question — known**
```json
{
  "en": "Demo enquiry Mist",
  "th": "คำถามตัวอย่าง สายหมอก"
}
```
**related_ids — known**
```json
[
  "demo20_policy_04",
  "demo20_procedure_04"
]
```
**scope_note — known**
```json
{
  "en": "Only applies to fictional Mist scenario",
  "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ สายหมอก"
}
```
**topic — known**
```json
"DEMO Seat adjustment"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_04.json)

### การเชื่อมสถานะสด (`live_binding`)

รหัส `demo20_live_binding_04`

คำถามตัวอย่าง:

- ตัวเชื่อมทดลอง สายหมอก จับคู่สถานะยังไง
- Demo binding Mist How are statuses mapped?
- ตัวเชื่อมทดลอง สายหมอก จับคู่สถานะแบบไหนและเก็บข้อมูลนานเท่าไหร่

**external_resource_key — known**
```json
"DEMO20_EXTERNAL_4"
```
**freshness_policy — known**
```json
{
  "en": "Synthetic TTL 35 seconds; no API call or live status claim",
  "th": "ค่าจำลอง TTL 35 วินาที; ไม่เรียก API และไม่ยืนยันสถานะสด"
}
```
**physical_pool_key — known**
```json
"demo20_pool_04"
```
**provider — known**
```json
"wordpress_booking"
```
**service_id — known**
```json
"demo20_service_04"
```
**status_mapping — known**
```json
[
  {
    "normalized": "free",
    "raw": "DEMO_EMPTY_4"
  },
  {
    "normalized": "occupied",
    "raw": "DEMO_BUSY_4"
  },
  {
    "normalized": "unknown",
    "raw": "DEMO_UNKNOWN_4"
  }
]
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/live_binding/demo20_live_binding_04.json)

