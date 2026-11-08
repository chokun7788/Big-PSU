# ชุด 09 — ลมทะเล / Sea Breeze

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

เกม สถานที่ ราคา กฎ บุคคล และสถานะทั้งหมดในชุดใหม่นี้แต่งขึ้นเพื่อทดสอบ ไม่ได้เป็นข้อมูล PSU หรือเกมที่มีจำหน่ายจริง คำแปลยังไม่ผ่านมนุษย์

แพลตฟอร์มตัวอย่าง: PC • จำนวนผู้เล่น 3–12 • เวลาเล่น 180 นาที / กินช่องจอง 180 นาที

## ข้อมูลครบ 24 หมวด

### ข้อมูลศูนย์ (`center`)

รหัส `demo20_center_09`

คำถามตัวอย่าง:

- ศูนย์ทดลอง ลมทะเล อยู่ตรงไหน
- Demo venue Sea Breeze Where is it located?
- ศูนย์ทดลอง ลมทะเล อยู่ตึกอะไร ชั้นไหน

**address — known**
```json
{
  "en": "Fictional address 63, Example Road, Test District",
  "th": "เลขที่สมมุติ 63 ถนนตัวอย่าง แขวงทดลอง"
}
```
**building — known**
```json
"DEMO Tower E"
```
**description — known**
```json
{
  "en": "Synthetic scenario 9: Digital Harbour, not a real venue",
  "th": "สถานการณ์ทดลอง 9: ท่าเรือดิจิทัล ไม่ใช่สถานที่จริง"
}
```
**floor — known**
```json
"5"
```
**map_url — known**
```json
"https://example.invalid/demo20/map/9"
```
**name — known**
```json
{
  "en": "Demo venue Sea Breeze",
  "th": "ศูนย์ทดลอง ลมทะเล"
}
```
**operator — known**
```json
{
  "en": "Fictional Sea Breeze operator",
  "th": "ผู้ประกอบการสมมุติ ลมทะเล"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/center/demo20_center_09.json)

### โซนบริการ (`zone`)

รหัส `demo20_zone_09`

คำถามตัวอย่าง:

- โซนทดลอง ลมทะเล มีที่นั่งกี่ที่
- Demo zone Sea Breeze How many seats are there?
- โซนทดลอง ลมทะเล โซนนี้อยู่ตรงไหนและมีที่นั่งกี่ที่

**description — known**
```json
{
  "en": "Synthetic PC zone for Digital Harbour",
  "th": "โซนจำลอง PC สำหรับท่าเรือดิจิทัล"
}
```
**location — known**
```json
{
  "en": "Test building, floor 5, room 109",
  "th": "อาคารทดสอบ ชั้น 5 ห้อง 109"
}
```
**name — known**
```json
{
  "en": "Demo zone Sea Breeze",
  "th": "โซนทดลอง ลมทะเล"
}
```
**room_seats — known**
```json
14
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_09.json)

### รุ่นและสเปกอุปกรณ์ (`equipment_model`)

รหัส `demo20_equipment_model_09`

คำถามตัวอย่าง:

- รุ่นอุปกรณ์ ลมทะเล สเปกมีอะไรบ้าง
- Demo model Sea Breeze What are its specifications?
- รุ่นอุปกรณ์ ลมทะเล เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง

**device_type — known**
```json
"pc"
```
**name — known**
```json
{
  "en": "Demo model Sea Breeze",
  "th": "รุ่นอุปกรณ์ ลมทะเล"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_09.json)

### เครื่องหรือทรัพยากรจริง (`resource`)

รหัส `demo20_resource_09`

คำถามตัวอย่าง:

- เครื่องทดลอง ลมทะเล เล่นพร้อมกันได้กี่คน
- Demo station Sea Breeze How many people can play at once?
- เครื่องทดลอง ลมทะเล เครื่องยังใช้งานได้ไหมและรองรับกี่คน

**capacity_persons — known**
```json
12
```
**equipment_model_ids — known**
```json
[
  "demo20_equipment_model_09"
]
```
**name — known**
```json
{
  "en": "Demo station Sea Breeze",
  "th": "เครื่องทดลอง ลมทะเล"
}
```
**operational_status — known**
```json
"in_service"
```
**physical_pool_key — known**
```json
"demo20_pool_09"
```
**zone_id — known**
```json
"demo20_zone_09"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/resource/demo20_resource_09.json)

### รายการที่เลือกในระบบจอง (`service`)

รหัส `demo20_service_09`

คำถามตัวอย่าง:

- รอบทดลอง ลมทะเล หนึ่งรอบเล่นได้กี่นาที
- Demo session Sea Breeze How many minutes does one session last?
- รอบทดลอง ลมทะเล เวลาเล่นกับเวลาที่กินช่องจองกี่นาที

**booking_product_key — known**
```json
"DEMO20_BOOKING_09"
```
**capacity_max — known**
```json
12
```
**capacity_min — known**
```json
3
```
**name — known**
```json
{
  "en": "Demo session Sea Breeze",
  "th": "รอบทดลอง ลมทะเล"
}
```
**occupancy_minutes — known**
```json
180
```
**platform — known**
```json
"PC"
```
**resource_ids — known**
```json
[
  "demo20_resource_09"
]
```
**session_minutes — known**
```json
180
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_09.json)

### ข้อมูลเกม (`game`)

รหัส `demo20_game_09`

คำถามตัวอย่าง:

- เกมสมมุติ ลมทะเล เล่นยังไง
- Fictional game Sea Breeze How do I play it?
- เกมสมมุติ ลมทะเล เกมเกี่ยวกับอะไรและเล่นยังไง

**age_rating — known**
```json
{
  "en": "Synthetic DEMO rating 6",
  "th": "เรตอายุสมมุติ DEMO 6"
}
```
**edition — known**
```json
"DEMO fiction revision 9"
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
  "en": "Arrange vessel queues as a large group; follow the demonstration controls",
  "th": "จัดคิวเรือโดยเล่นเป็นกลุ่มใหญ่; ใช้คำสั่งตามชุดควบคุมทดลอง"
}
```
**publisher_url — known**
```json
"https://example.invalid/demo20/fictional-game/9"
```
**summary — known**
```json
{
  "en": "Fictional test game: Arrange vessel queues as a large group",
  "th": "เกมแต่งขึ้นเพื่อทดสอบ: จัดคิวเรือโดยเล่นเป็นกลุ่มใหญ่"
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
  "en": "Fictional Digital Harbour",
  "th": "เกมสมมุติ ท่าเรือดิจิทัล"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_09.json)

### กลุ่มผู้ใช้ (`audience`)

รหัส `demo20_audience_09`

คำถามตัวอย่าง:

- กลุ่มผู้ใช้ ลมทะเล ต้องใช้หลักฐานอะไร
- Demo visitors Sea Breeze What proof is required?
- กลุ่มผู้ใช้ ลมทะเล ใครใช้สิทธิ์กลุ่มนี้ได้และต้องแสดงหลักฐานอะไร

**eligibility — known**
```json
{
  "en": "Fictional group 9: demo sessions only",
  "th": "ผู้ใช้สมมุติกลุ่ม 9: ใช้บริการตามรอบทดลอง"
}
```
**name — known**
```json
{
  "en": "Demo visitors Sea Breeze",
  "th": "กลุ่มผู้ใช้ ลมทะเล"
}
```
**required_proofs — known**
```json
[
  "DEMO pass Sea Breeze",
  "DEMO group list 9"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/audience/demo20_audience_09.json)

### ติดต่อ (`contact`)

รหัส `demo20_contact_09`

คำถามตัวอย่าง:

- ช่องทางช่วยเหลือ ลมทะเล ติดต่อทางไหน
- Demo help channel Sea Breeze How can I contact them?
- ช่องทางช่วยเหลือ ลมทะเล ติดต่อที่ไหนและติดต่อได้ช่วงไหน

**channel — known**
```json
"phone"
```
**office_hours — known**
```json
{
  "en": "Demo hours 09:00–18:00",
  "th": "ช่วงทดลอง 09:00–18:00"
}
```
**purpose — known**
```json
{
  "en": "Fictional support for Group reservations",
  "th": "สอบถามสมมุติเรื่อง การจองหมู่คณะ"
}
```
**value — known**
```json
"DEMO-NON-DIALABLE-09"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_09.json)

### ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`)

รหัส `demo20_procedure_09`

คำถามตัวอย่าง:

- ขั้นตอนทดลอง ลมทะเล ต้องทำยังไงบ้าง
- Demo procedure Sea Breeze What steps should I follow?
- ขั้นตอนทดลอง ลมทะเล มีขั้นตอนอะไรและต้องใช้เอกสารอะไร

**deadline_minutes — known**
```json
60
```
**outcome — known**
```json
{
  "en": "Demo outcome: Group reservations checked",
  "th": "ผลทดสอบ: ตรวจสอบ การจองหมู่คณะ เสร็จ"
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
  "DEMO pass Sea Breeze",
  "DEMO group list 9"
]
```
**steps — known**
```json
[
  {
    "contact_id": null,
    "instruction": {
      "en": "Select the fictional Sea Breeze service",
      "th": "เลือกบริการสมมุติ ลมทะเล"
    },
    "order": 1
  },
  {
    "contact_id": "demo20_contact_09",
    "instruction": {
      "en": "Check names and conditions before confirming",
      "th": "ตรวจชื่อและเงื่อนไขก่อนยืนยัน"
    },
    "order": 2
  },
  {
    "contact_id": "demo20_contact_09",
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
"DEMO Group reservations"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_09.json)

### นโยบายและกฎศูนย์ (`policy`)

รหัส `demo20_policy_09`

คำถามตัวอย่าง:

- ข้อกำหนดทดลอง ลมทะเล กฎเป็นยังไง
- Demo policy Sea Breeze What are the rules?
- ข้อกำหนดทดลอง ลมทะเล อนุญาตไหมและมีข้อยกเว้นอะไร

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
  "en": "Fictional rule for Group reservations: required; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "กติกาสมมุติเรื่องการจองหมู่คณะ: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
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
"demo20_procedure_09"
```
**subject — known**
```json
{
  "en": "Demo policy Sea Breeze",
  "th": "ข้อกำหนดทดลอง ลมทะเล"
}
```
**topic — known**
```json
"DEMO Group reservations"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/policy/demo20_policy_09.json)

### สิ่งอำนวยความสะดวก (`facility`)

รหัส `demo20_facility_09`

คำถามตัวอย่าง:

- พื้นที่พัก ลมทะเล อยู่ตรงไหนในร้าน
- Demo amenity Sea Breeze Where in the venue is it?
- พื้นที่พัก ลมทะเล อยู่ตรงไหนและคนที่ต้องการความช่วยเหลือเข้าใช้ยังไง

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
  "en": "Group meeting area in demo room 109",
  "th": "พื้นที่รวมกลุ่ม อยู่ห้องทดสอบ 109"
}
```
**name — known**
```json
{
  "en": "Demo amenity Sea Breeze",
  "th": "พื้นที่พัก ลมทะเล"
}
```
**usage_conditions — known**
```json
{
  "en": "Demo sessions only; ask the operator first",
  "th": "ใช้ตามรอบทดลอง; ต้องขอผู้ดูแลก่อน"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/facility/demo20_facility_09.json)

### เกมที่ศูนย์มีให้เล่นจริง (`game_service`)

รหัส `demo20_game_service_09`

คำถามตัวอย่าง:

- การติดตั้งทดลอง ลมทะเล มีให้เล่นหรือยัง
- Demo installation Sea Breeze Is this game offered?
- การติดตั้งทดลอง ลมทะเล มีให้เล่นไหมและติดตั้งรุ่นไหน

**account_policy_id — known**
```json
"demo20_policy_09"
```
**game_id — known**
```json
"demo20_game_09"
```
**game_version — known**
```json
"DEMO BUILD 9"
```
**installed_resource_ids — known**
```json
[
  "demo20_resource_09"
]
```
**offered — known**
```json
true
```
**service_id — known**
```json
"demo20_service_09"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_service/demo20_game_service_09.json)

### รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`)

รหัส `demo20_game_mode_09`

คำถามตัวอย่าง:

- โหมดทดลอง ลมทะเล เล่นพร้อมกันได้สูงสุดกี่คน
- Demo mode Sea Breeze How many people can play together at most?
- โหมดทดลอง ลมทะเล ต้องมีขั้นต่ำกี่คนและเล่นได้สูงสุดกี่คน

**game_id — known**
```json
"demo20_game_09"
```
**mode_name — known**
```json
{
  "en": "Demo mode Sea Breeze",
  "th": "โหมดทดลอง ลมทะเล"
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
12
```
**players_min — known**
```json
3
```
**studio_supported — known**
```json
true
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_mode/demo20_game_mode_09.json)

### วิธีเล่นและปุ่ม (`control_set`)

รหัส `demo20_control_set_09`

คำถามตัวอย่าง:

- ชุดควบคุมทดลอง ลมทะเล ปุ่มอะไรบ้าง
- Demo controls Sea Breeze What are the controls?
- ชุดควบคุมทดลอง ลมทะเล ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร

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
      "en": "Fictional input for Digital Harbour",
      "th": "คำสั่งสมมุติของ ท่าเรือดิจิทัล"
    },
    "gesture": "press"
  }
]
```
**game_id — known**
```json
"demo20_game_09"
```
**game_version — known**
```json
"DEMO BUILD 9"
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
"DEMO_LAYOUT_9"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_09.json)

### ราคาต่อบริการ (`rate`)

รหัส `demo20_rate_09`

คำถามตัวอย่าง:

- อัตราทดลอง ลมทะเล ราคาเท่าไหร่
- Demo tariff Sea Breeze How much does it cost?
- อัตราทดลอง ลมทะเล ราคาเท่าไหร่และได้กี่นาที

**amount_minor — known**
```json
90000
```
**audience_id — known**
```json
"demo20_audience_09"
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
180
```
**persons_max — known**
```json
12
```
**persons_min — known**
```json
3
```
**service_id — known**
```json
"demo20_service_09"
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
"per_hour"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rate/demo20_rate_09.json)

### ราคาเหมาโซน/ห้อง (`rental_package`)

รหัส `demo20_rental_package_09`

คำถามตัวอย่าง:

- แพ็กเกจทดลอง ลมทะเล เหมาเท่าไหร่
- Demo package Sea Breeze How much is the rental?
- แพ็กเกจทดลอง ลมทะเล ราคาเหมาเท่าไหร่และรวมอุปกรณ์อะไร

**amount_minor — known**
```json
271250
```
**audience_id — known**
```json
"demo20_audience_09"
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
  "en": "Fictional Sea Breeze station and PC inputs",
  "th": "เครื่องสมมุติ ลมทะเล พร้อมอุปกรณ์ PC"
}
```
**name — known**
```json
{
  "en": "Demo package Sea Breeze",
  "th": "แพ็กเกจทดลอง ลมทะเล"
}
```
**period_label — known**
```json
"half_day"
```
**room_seats — known**
```json
14
```
**terms — known**
```json
{
  "en": "Synthetic package excludes extensions; 3–12 people per session",
  "th": "แพ็กเกจสมมุติไม่รวมค่าต่อเวลา; รอบละ 3–12 คน"
}
```
**zone_ids — known**
```json
[
  "demo20_zone_09"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rental_package/demo20_rental_package_09.json)

### ตารางบริการ (`schedule`)

รหัส `demo20_schedule_09`

คำถามตัวอย่าง:

- ตารางทดลอง ลมทะเล จองช่วงไหนได้บ้าง
- Demo timetable Sea Breeze What are the booking hours?
- ตารางทดลอง ลมทะเล เปิดช่วงไหนและพักบำรุงรักษาตอนไหน

**bookable_periods — known**
```json
[
  {
    "end": "12:00",
    "start": "09:00"
  },
  {
    "end": "18:00",
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
    "end": "18:00",
    "start": "09:00"
  }
]
```
**reason — known**
```json
{
  "en": "Synthetic Sea Breeze schedule with maintenance",
  "th": "ตารางสมมุติ ลมทะเล มีพักบำรุงรักษา"
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
  "demo20_zone_09"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_09.json)

### วันปิด/ข้อยกเว้น (`closure`)

รหัส `demo20_closure_09`

คำถามตัวอย่าง:

- ประกาศวันทดลอง ลมทะเล วันนั้นปิดไหม
- Demo date notice Sea Breeze Is it closed on that date?
- ประกาศวันทดลอง ลมทะเล วันนั้นเปิดปิดยังไงและเพราะอะไร

**bookable_periods — known**
```json
[]
```
**local_date — known**
```json
"2026-12-09"
```
**open_periods — known**
```json
[]
```
**reason — known**
```json
{
  "en": "Synthetic Sea Breeze date notice: closed",
  "th": "ประกาศสมมุติ ลมทะเล: closed"
}
```
**resolution_policy_id — known**
```json
"demo20_policy_09"
```
**state — known**
```json
"closed"
```
**zone_ids — known**
```json
[
  "demo20_zone_09"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/closure/demo20_closure_09.json)

### รายการแข่งขันและฉบับกติกา (`competition`)

รหัส `demo20_competition_09`

คำถามตัวอย่าง:

- รายการฝึก ลมทะเล ใช้กติกาฉบับไหน
- Demo event Sea Breeze Which rulebook release applies?
- รายการฝึก ลมทะเล ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่

**competition_dates — known**
```json
[
  "2026-12-09"
]
```
**coverage — known**
```json
"partial"
```
**division — known**
```json
{
  "en": "Practice group 3–12 players",
  "th": "กลุ่มฝึก 3–12 คน"
}
```
**event_name — known**
```json
{
  "en": "Demo event Sea Breeze",
  "th": "รายการฝึก ลมทะเล"
}
```
**game_id — known**
```json
"demo20_game_09"
```
**rulebook_release — known**
```json
"DEMO20_REV_9"
```
**supersedes_id — not_applicable**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_09.json)

### ข้อกติกาการแข่งขัน (`competition_rule`)

รหัส `demo20_competition_rule_09`

คำถามตัวอย่าง:

- ข้อการแข่งขันทดลอง ลมทะเล ข้อนี้กำหนดอะไร
- Demo rule Sea Breeze What does this rule require?
- ข้อการแข่งขันทดลอง ลมทะเล กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม

**competition_id — known**
```json
"demo20_competition_09"
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
"protest_dispute"
```
**heading — known**
```json
{
  "en": "Demo rule Sea Breeze",
  "th": "ข้อการแข่งขันทดลอง ลมทะเล"
}
```
**section_number — known**
```json
"5.9"
```
**text — known**
```json
{
  "en": "Fictional clause 9: for Group reservations, follow decision required; exception requires written demo operator approval; not actual rules",
  "th": "ข้อสมมุติ 9: การจองหมู่คณะ ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_09.json)

### ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`)

รหัส `demo20_news_09`

คำถามตัวอย่าง:

- ข่าวทดลอง ลมทะเล ประกาศว่าอะไร
- Demo bulletin Sea Breeze What does the announcement say?
- ข่าวทดลอง ลมทะเล ประกาศอะไรและกิจกรรมเริ่มจบเมื่อไหร่

**audience_ids — known**
```json
[
  "demo20_audience_09"
]
```
**body — known**
```json
{
  "en": "Synthetic bulletin: Digital Harbour activity for 3–12 people; no actual payment",
  "th": "ข่าวสมมุติ: กิจกรรมท่าเรือดิจิทัล สำหรับกลุ่ม 3–12 คน; ไม่มีรับเงินจริง"
}
```
**contact_id — known**
```json
"demo20_contact_09"
```
**event_end — known**
```json
"2026-12-09T12:00:00+07:00"
```
**event_start — known**
```json
"2026-12-09T10:00:00+07:00"
```
**registration_url — known**
```json
"https://example.invalid/demo20/register/9"
```
**title — known**
```json
{
  "en": "Demo bulletin Sea Breeze",
  "th": "ข่าวทดลอง ลมทะเล"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/news/demo20_news_09.json)

### บุคลากร/ทีมที่เปิดเผยได้ (`person`)

รหัส `demo20_person_09`

คำถามตัวอย่าง:

- ผู้ดูแลสมมุติ ลมทะเล รับผิดชอบอะไร
- Fictional host Sea Breeze What is their role?
- ผู้ดูแลสมมุติ ลมทะเล รับผิดชอบเรื่องอะไรและติดต่อทางไหน

**display_name — known**
```json
{
  "en": "Fictional host Sea Breeze",
  "th": "ผู้ดูแลสมมุติ ลมทะเล"
}
```
**public_contact_id — known**
```json
"demo20_contact_09"
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
  "en": "Fictional host for Group reservations",
  "th": "ผู้ดูแลสมมุติเรื่อง การจองหมู่คณะ"
}
```
**team — known**
```json
{
  "en": "Demo Sea Breeze team",
  "th": "ทีมทดสอบ ลมทะเล"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/person/demo20_person_09.json)

### คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`)

รหัส `demo20_faq_09`

คำถามตัวอย่าง:

- คำถามตัวอย่าง ลมทะเล คำตอบคืออะไร
- Demo enquiry Sea Breeze What is the answer?
- คำถามตัวอย่าง ลมทะเล คำตอบคืออะไรและใช้กับกรณีไหน

**answer — known**
```json
{
  "en": "Example answer: Fictional rule for Group reservations: required; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องการจองหมู่คณะ: required; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
}
```
**question — known**
```json
{
  "en": "Demo enquiry Sea Breeze",
  "th": "คำถามตัวอย่าง ลมทะเล"
}
```
**related_ids — known**
```json
[
  "demo20_policy_09",
  "demo20_procedure_09"
]
```
**scope_note — known**
```json
{
  "en": "Only applies to fictional Sea Breeze scenario",
  "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ลมทะเล"
}
```
**topic — known**
```json
"DEMO Group reservations"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_09.json)

### การเชื่อมสถานะสด (`live_binding`)

รหัส `demo20_live_binding_09`

คำถามตัวอย่าง:

- ตัวเชื่อมทดลอง ลมทะเล จับคู่สถานะยังไง
- Demo binding Sea Breeze How are statuses mapped?
- ตัวเชื่อมทดลอง ลมทะเล จับคู่สถานะแบบไหนและเก็บข้อมูลนานเท่าไหร่

**external_resource_key — known**
```json
"DEMO20_EXTERNAL_9"
```
**freshness_policy — known**
```json
{
  "en": "Synthetic TTL 60 seconds; no API call or live status claim",
  "th": "ค่าจำลอง TTL 60 วินาที; ไม่เรียก API และไม่ยืนยันสถานะสด"
}
```
**physical_pool_key — known**
```json
"demo20_pool_09"
```
**provider — known**
```json
"wordpress_booking"
```
**service_id — known**
```json
"demo20_service_09"
```
**status_mapping — known**
```json
[
  {
    "normalized": "free",
    "raw": "DEMO_EMPTY_9"
  },
  {
    "normalized": "occupied",
    "raw": "DEMO_BUSY_9"
  },
  {
    "normalized": "unknown",
    "raw": "DEMO_UNKNOWN_9"
  }
]
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/live_binding/demo20_live_binding_09.json)

