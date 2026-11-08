# ชุด 10 — ห้องสมุดดาว / Star Library

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

เกม สถานที่ ราคา กฎ บุคคล และสถานะทั้งหมดในชุดใหม่นี้แต่งขึ้นเพื่อทดสอบ ไม่ได้เป็นข้อมูล PSU หรือเกมที่มีจำหน่ายจริง คำแปลยังไม่ผ่านมนุษย์

แพลตฟอร์มตัวอย่าง: PS5 • จำนวนผู้เล่น 1–4 • เวลาเล่น 60 นาที / กินช่องจอง 60 นาที

## ข้อมูลครบ 24 หมวด

### ข้อมูลศูนย์ (`center`)

รหัส `demo20_center_10`

คำถามตัวอย่าง:

- ศูนย์ทดลอง ห้องสมุดดาว อยู่ตรงไหน
- Demo venue Star Library Where is it located?
- ศูนย์ทดลอง ห้องสมุดดาว อยู่ตึกอะไร ชั้นไหน

**address — known**
```json
{
  "en": "Fictional address 70, Example Road, Test District",
  "th": "เลขที่สมมุติ 70 ถนนตัวอย่าง แขวงทดลอง"
}
```
**building — known**
```json
"DEMO Tower A"
```
**description — known**
```json
{
  "en": "Synthetic scenario 10: Cube Melody, not a real venue",
  "th": "สถานการณ์ทดลอง 10: บทเพลงลูกบาศก์ ไม่ใช่สถานที่จริง"
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
  "en": "Demo venue Star Library",
  "th": "ศูนย์ทดลอง ห้องสมุดดาว"
}
```
**operator — known**
```json
{
  "en": "Fictional Star Library operator",
  "th": "ผู้ประกอบการสมมุติ ห้องสมุดดาว"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/center/demo20_center_10.json)

### โซนบริการ (`zone`)

รหัส `demo20_zone_10`

คำถามตัวอย่าง:

- โซนทดลอง ห้องสมุดดาว มีที่นั่งกี่ที่
- Demo zone Star Library How many seats are there?
- โซนทดลอง ห้องสมุดดาว โซนนี้อยู่ตรงไหนและมีที่นั่งกี่ที่

**description — known**
```json
{
  "en": "Synthetic PS5 zone for Cube Melody",
  "th": "โซนจำลอง PS5 สำหรับบทเพลงลูกบาศก์"
}
```
**location — known**
```json
{
  "en": "Test building, floor 1, room 110",
  "th": "อาคารทดสอบ ชั้น 1 ห้อง 110"
}
```
**name — known**
```json
{
  "en": "Demo zone Star Library",
  "th": "โซนทดลอง ห้องสมุดดาว"
}
```
**room_seats — known**
```json
7
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_10.json)

### รุ่นและสเปกอุปกรณ์ (`equipment_model`)

รหัส `demo20_equipment_model_10`

คำถามตัวอย่าง:

- รุ่นอุปกรณ์ ห้องสมุดดาว สเปกมีอะไรบ้าง
- Demo model Star Library What are its specifications?
- รุ่นอุปกรณ์ ห้องสมุดดาว เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง

**device_type — known**
```json
"console"
```
**name — known**
```json
{
  "en": "Demo model Star Library",
  "th": "รุ่นอุปกรณ์ ห้องสมุดดาว"
}
```
**specifications — unknown**
```json
null
```
**usage — known**
```json
{
  "en": "Fictional equipment for PS5; not a PSU specification",
  "th": "เครื่องสมมุติใช้กับ PS5; ห้ามอ้างเป็นสเปกศูนย์"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_10.json)

### เครื่องหรือทรัพยากรจริง (`resource`)

รหัส `demo20_resource_10`

คำถามตัวอย่าง:

- เครื่องทดลอง ห้องสมุดดาว เล่นพร้อมกันได้กี่คน
- Demo station Star Library How many people can play at once?
- เครื่องทดลอง ห้องสมุดดาว เครื่องยังใช้งานได้ไหมและรองรับกี่คน

**capacity_persons — known**
```json
4
```
**equipment_model_ids — known**
```json
[
  "demo20_equipment_model_10"
]
```
**name — known**
```json
{
  "en": "Demo station Star Library",
  "th": "เครื่องทดลอง ห้องสมุดดาว"
}
```
**operational_status — known**
```json
"retired"
```
**physical_pool_key — known**
```json
"demo20_pool_10"
```
**zone_id — known**
```json
"demo20_zone_10"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/resource/demo20_resource_10.json)

### รายการที่เลือกในระบบจอง (`service`)

รหัส `demo20_service_10`

คำถามตัวอย่าง:

- รอบทดลอง ห้องสมุดดาว หนึ่งรอบเล่นได้กี่นาที
- Demo session Star Library How many minutes does one session last?
- รอบทดลอง ห้องสมุดดาว เวลาเล่นกับเวลาที่กินช่องจองกี่นาที

**booking_product_key — unknown**
```json
null
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
  "en": "Demo session Star Library",
  "th": "รอบทดลอง ห้องสมุดดาว"
}
```
**occupancy_minutes — known**
```json
60
```
**platform — known**
```json
"PS5"
```
**resource_ids — known**
```json
[
  "demo20_resource_10"
]
```
**session_minutes — known**
```json
60
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_10.json)

### ข้อมูลเกม (`game`)

รหัส `demo20_game_10`

คำถามตัวอย่าง:

- เกมสมมุติ ห้องสมุดดาว เล่นยังไง
- Fictional game Star Library How do I play it?
- เกมสมมุติ ห้องสมุดดาว เกมเกี่ยวกับอะไรและเล่นยังไง

**age_rating — unknown**
```json
null
```
**edition — known**
```json
"DEMO fiction revision 10"
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
  "en": "Press to match colours and rhythms and create music; follow the demonstration controls",
  "th": "กดปุ่มตามสีและจังหวะเพื่อสร้างเพลง; ใช้คำสั่งตามชุดควบคุมทดลอง"
}
```
**publisher_url — known**
```json
"https://example.invalid/demo20/fictional-game/10"
```
**summary — known**
```json
{
  "en": "Fictional test game: Press to match colours and rhythms and create music",
  "th": "เกมแต่งขึ้นเพื่อทดสอบ: กดปุ่มตามสีและจังหวะเพื่อสร้างเพลง"
}
```
**supported_platforms — known**
```json
[
  "PS5"
]
```
**title — known**
```json
{
  "en": "Fictional Cube Melody",
  "th": "เกมสมมุติ บทเพลงลูกบาศก์"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_10.json)

### กลุ่มผู้ใช้ (`audience`)

รหัส `demo20_audience_10`

คำถามตัวอย่าง:

- กลุ่มผู้ใช้ ห้องสมุดดาว ต้องใช้หลักฐานอะไร
- Demo visitors Star Library What proof is required?
- กลุ่มผู้ใช้ ห้องสมุดดาว ใครใช้สิทธิ์กลุ่มนี้ได้และต้องแสดงหลักฐานอะไร

**eligibility — known**
```json
{
  "en": "Fictional group 10: demo sessions only",
  "th": "ผู้ใช้สมมุติกลุ่ม 10: ใช้บริการตามรอบทดลอง"
}
```
**name — known**
```json
{
  "en": "Demo visitors Star Library",
  "th": "กลุ่มผู้ใช้ ห้องสมุดดาว"
}
```
**required_proofs — unknown**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/audience/demo20_audience_10.json)

### ติดต่อ (`contact`)

รหัส `demo20_contact_10`

คำถามตัวอย่าง:

- ช่องทางช่วยเหลือ ห้องสมุดดาว ติดต่อทางไหน
- Demo help channel Star Library How can I contact them?
- ช่องทางช่วยเหลือ ห้องสมุดดาว ติดต่อที่ไหนและติดต่อได้ช่วงไหน

**channel — known**
```json
"onsite"
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
  "en": "Fictional support for Volume adjustment",
  "th": "สอบถามสมมุติเรื่อง ปรับระดับเสียง"
}
```
**value — known**
```json
"DEMO desk Star Library"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_10.json)

### ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`)

รหัส `demo20_procedure_10`

คำถามตัวอย่าง:

- ขั้นตอนทดลอง ห้องสมุดดาว ต้องทำยังไงบ้าง
- Demo procedure Star Library What steps should I follow?
- ขั้นตอนทดลอง ห้องสมุดดาว มีขั้นตอนอะไรและต้องใช้เอกสารอะไร

**deadline_minutes — known**
```json
0
```
**outcome — known**
```json
{
  "en": "Demo outcome: Volume adjustment checked",
  "th": "ผลทดสอบ: ตรวจสอบ ปรับระดับเสียง เสร็จ"
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
  "DEMO pass Star Library"
]
```
**steps — known**
```json
[
  {
    "contact_id": null,
    "instruction": {
      "en": "Select the fictional Star Library service",
      "th": "เลือกบริการสมมุติ ห้องสมุดดาว"
    },
    "order": 1
  },
  {
    "contact_id": "demo20_contact_10",
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
"DEMO Volume adjustment"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_10.json)

### นโยบายและกฎศูนย์ (`policy`)

รหัส `demo20_policy_10`

คำถามตัวอย่าง:

- ข้อกำหนดทดลอง ห้องสมุดดาว กฎเป็นยังไง
- Demo policy Star Library What are the rules?
- ข้อกำหนดทดลอง ห้องสมุดดาว อนุญาตไหมและมีข้อยกเว้นอะไร

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
  "en": "Fictional rule for Volume adjustment: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "กติกาสมมุติเรื่องปรับระดับเสียง: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
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
"demo20_procedure_10"
```
**subject — known**
```json
{
  "en": "Demo policy Star Library",
  "th": "ข้อกำหนดทดลอง ห้องสมุดดาว"
}
```
**topic — known**
```json
"DEMO Volume adjustment"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/policy/demo20_policy_10.json)

### สิ่งอำนวยความสะดวก (`facility`)

รหัส `demo20_facility_10`

คำถามตัวอย่าง:

- พื้นที่พัก ห้องสมุดดาว อยู่ตรงไหนในร้าน
- Demo amenity Star Library Where in the venue is it?
- พื้นที่พัก ห้องสมุดดาว อยู่ตรงไหนและคนที่ต้องการความช่วยเหลือเข้าใช้ยังไง

**accessibility — unknown**
```json
null
```
**location — known**
```json
{
  "en": "Headphone collection in demo room 110",
  "th": "จุดยืมหูฟัง อยู่ห้องทดสอบ 110"
}
```
**name — known**
```json
{
  "en": "Demo amenity Star Library",
  "th": "พื้นที่พัก ห้องสมุดดาว"
}
```
**usage_conditions — known**
```json
{
  "en": "Demo sessions only; may use while waiting",
  "th": "ใช้ตามรอบทดลอง; ใช้ได้ระหว่างรอ"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/facility/demo20_facility_10.json)

### เกมที่ศูนย์มีให้เล่นจริง (`game_service`)

รหัส `demo20_game_service_10`

คำถามตัวอย่าง:

- การติดตั้งทดลอง ห้องสมุดดาว มีให้เล่นหรือยัง
- Demo installation Star Library Is this game offered?
- การติดตั้งทดลอง ห้องสมุดดาว มีให้เล่นไหมและติดตั้งรุ่นไหน

**account_policy_id — known**
```json
"demo20_policy_10"
```
**game_id — known**
```json
"demo20_game_10"
```
**game_version — unknown**
```json
null
```
**installed_resource_ids — known**
```json
[
  "demo20_resource_10"
]
```
**offered — known**
```json
true
```
**service_id — known**
```json
"demo20_service_10"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_service/demo20_game_service_10.json)

### รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`)

รหัส `demo20_game_mode_10`

คำถามตัวอย่าง:

- โหมดทดลอง ห้องสมุดดาว เล่นพร้อมกันได้สูงสุดกี่คน
- Demo mode Star Library How many people can play together at most?
- โหมดทดลอง ห้องสมุดดาว ต้องมีขั้นต่ำกี่คนและเล่นได้สูงสุดกี่คน

**game_id — known**
```json
"demo20_game_10"
```
**mode_name — known**
```json
{
  "en": "Demo mode Star Library",
  "th": "โหมดทดลอง ห้องสมุดดาว"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_mode/demo20_game_mode_10.json)

### วิธีเล่นและปุ่ม (`control_set`)

รหัส `demo20_control_set_10`

คำถามตัวอย่าง:

- ชุดควบคุมทดลอง ห้องสมุดดาว ปุ่มอะไรบ้าง
- Demo controls Star Library What are the controls?
- ชุดควบคุมทดลอง ห้องสมุดดาว ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร

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
      "en": "Fictional input for Cube Melody",
      "th": "คำสั่งสมมุติของ บทเพลงลูกบาศก์"
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
      "en": "Fictional input for Cube Melody",
      "th": "คำสั่งสมมุติของ บทเพลงลูกบาศก์"
    },
    "gesture": "press"
  }
]
```
**game_id — known**
```json
"demo20_game_10"
```
**game_version — known**
```json
"DEMO BUILD 10"
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
"DEMO_LAYOUT_10"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_10.json)

### ราคาต่อบริการ (`rate`)

รหัส `demo20_rate_10`

คำถามตัวอย่าง:

- อัตราทดลอง ห้องสมุดดาว ราคาเท่าไหร่
- Demo tariff Star Library How much does it cost?
- อัตราทดลอง ห้องสมุดดาว ราคาเท่าไหร่และได้กี่นาที

**amount_minor — known**
```json
6000
```
**audience_id — known**
```json
"demo20_audience_10"
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
4
```
**persons_min — known**
```json
1
```
**service_id — known**
```json
"demo20_service_10"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rate/demo20_rate_10.json)

### ราคาเหมาโซน/ห้อง (`rental_package`)

รหัส `demo20_rental_package_10`

คำถามตัวอย่าง:

- แพ็กเกจทดลอง ห้องสมุดดาว เหมาเท่าไหร่
- Demo package Star Library How much is the rental?
- แพ็กเกจทดลอง ห้องสมุดดาว ราคาเหมาเท่าไหร่และรวมอุปกรณ์อะไร

**amount_minor — known**
```json
19250
```
**audience_id — known**
```json
"demo20_audience_10"
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
  "en": "Fictional Star Library station and PS5 inputs",
  "th": "เครื่องสมมุติ ห้องสมุดดาว พร้อมอุปกรณ์ PS5"
}
```
**name — known**
```json
{
  "en": "Demo package Star Library",
  "th": "แพ็กเกจทดลอง ห้องสมุดดาว"
}
```
**period_label — known**
```json
"full_day"
```
**room_seats — known**
```json
7
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
  "demo20_zone_10"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rental_package/demo20_rental_package_10.json)

### ตารางบริการ (`schedule`)

รหัส `demo20_schedule_10`

คำถามตัวอย่าง:

- ตารางทดลอง ห้องสมุดดาว จองช่วงไหนได้บ้าง
- Demo timetable Star Library What are the booking hours?
- ตารางทดลอง ห้องสมุดดาว เปิดช่วงไหนและพักบำรุงรักษาตอนไหน

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
  "en": "Synthetic Star Library schedule with maintenance",
  "th": "ตารางสมมุติ ห้องสมุดดาว มีพักบำรุงรักษา"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```
**weekday — known**
```json
3
```
**zone_ids — known**
```json
[
  "demo20_zone_10"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_10.json)

### วันปิด/ข้อยกเว้น (`closure`)

รหัส `demo20_closure_10`

คำถามตัวอย่าง:

- ประกาศวันทดลอง ห้องสมุดดาว วันนั้นปิดไหม
- Demo date notice Star Library Is it closed on that date?
- ประกาศวันทดลอง ห้องสมุดดาว วันนั้นเปิดปิดยังไงและเพราะอะไร

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
"2026-12-10"
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
  "en": "Synthetic Star Library date notice: modified_hours",
  "th": "ประกาศสมมุติ ห้องสมุดดาว: modified_hours"
}
```
**resolution_policy_id — known**
```json
"demo20_policy_10"
```
**state — known**
```json
"modified_hours"
```
**zone_ids — known**
```json
[
  "demo20_zone_10"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/closure/demo20_closure_10.json)

### รายการแข่งขันและฉบับกติกา (`competition`)

รหัส `demo20_competition_10`

คำถามตัวอย่าง:

- รายการฝึก ห้องสมุดดาว ใช้กติกาฉบับไหน
- Demo event Star Library Which rulebook release applies?
- รายการฝึก ห้องสมุดดาว ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่

**competition_dates — known**
```json
[
  "2026-12-10"
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
  "en": "Demo event Star Library",
  "th": "รายการฝึก ห้องสมุดดาว"
}
```
**game_id — known**
```json
"demo20_game_10"
```
**rulebook_release — known**
```json
"DEMO20_REV_10"
```
**supersedes_id — not_applicable**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_10.json)

### ข้อกติกาการแข่งขัน (`competition_rule`)

รหัส `demo20_competition_rule_10`

คำถามตัวอย่าง:

- ข้อการแข่งขันทดลอง ห้องสมุดดาว ข้อนี้กำหนดอะไร
- Demo rule Star Library What does this rule require?
- ข้อการแข่งขันทดลอง ห้องสมุดดาว กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม

**competition_id — known**
```json
"demo20_competition_10"
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
  "en": "Demo rule Star Library",
  "th": "ข้อการแข่งขันทดลอง ห้องสมุดดาว"
}
```
**section_number — known**
```json
"1.10"
```
**text — known**
```json
{
  "en": "Fictional clause 10: for Volume adjustment, follow decision conditional; exception requires written demo operator approval; not actual rules",
  "th": "ข้อสมมุติ 10: ปรับระดับเสียง ให้ปฏิบัติตามคำตัดสิน conditional; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_10.json)

### ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`)

รหัส `demo20_news_10`

คำถามตัวอย่าง:

- ข่าวทดลอง ห้องสมุดดาว ประกาศว่าอะไร
- Demo bulletin Star Library What does the announcement say?
- ข่าวทดลอง ห้องสมุดดาว ประกาศอะไรและกิจกรรมเริ่มจบเมื่อไหร่

**audience_ids — known**
```json
[
  "demo20_audience_10"
]
```
**body — known**
```json
{
  "en": "Synthetic bulletin: Cube Melody activity for 1–4 people; no actual payment",
  "th": "ข่าวสมมุติ: กิจกรรมบทเพลงลูกบาศก์ สำหรับกลุ่ม 1–4 คน; ไม่มีรับเงินจริง"
}
```
**contact_id — known**
```json
"demo20_contact_10"
```
**event_end — known**
```json
"2026-12-10T12:00:00+07:00"
```
**event_start — known**
```json
"2026-12-10T10:00:00+07:00"
```
**registration_url — known**
```json
"https://example.invalid/demo20/register/10"
```
**title — known**
```json
{
  "en": "Demo bulletin Star Library",
  "th": "ข่าวทดลอง ห้องสมุดดาว"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/news/demo20_news_10.json)

### บุคลากร/ทีมที่เปิดเผยได้ (`person`)

รหัส `demo20_person_10`

คำถามตัวอย่าง:

- ผู้ดูแลสมมุติ ห้องสมุดดาว รับผิดชอบอะไร
- Fictional host Star Library What is their role?
- ผู้ดูแลสมมุติ ห้องสมุดดาว รับผิดชอบเรื่องอะไรและติดต่อทางไหน

**display_name — known**
```json
{
  "en": "Fictional host Star Library",
  "th": "ผู้ดูแลสมมุติ ห้องสมุดดาว"
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
  "en": "Fictional host for Volume adjustment",
  "th": "ผู้ดูแลสมมุติเรื่อง ปรับระดับเสียง"
}
```
**team — known**
```json
{
  "en": "Demo Star Library team",
  "th": "ทีมทดสอบ ห้องสมุดดาว"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/person/demo20_person_10.json)

### คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`)

รหัส `demo20_faq_10`

คำถามตัวอย่าง:

- คำถามตัวอย่าง ห้องสมุดดาว คำตอบคืออะไร
- Demo enquiry Star Library What is the answer?
- คำถามตัวอย่าง ห้องสมุดดาว คำตอบคืออะไรและใช้กับกรณีไหน

**answer — known**
```json
{
  "en": "Example answer: Fictional rule for Volume adjustment: conditional; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องปรับระดับเสียง: conditional; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
}
```
**question — known**
```json
{
  "en": "Demo enquiry Star Library",
  "th": "คำถามตัวอย่าง ห้องสมุดดาว"
}
```
**related_ids — known**
```json
[
  "demo20_policy_10",
  "demo20_procedure_10"
]
```
**scope_note — known**
```json
{
  "en": "Only applies to fictional Star Library scenario",
  "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ ห้องสมุดดาว"
}
```
**topic — known**
```json
"DEMO Volume adjustment"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_10.json)

### การเชื่อมสถานะสด (`live_binding`)

รหัส `demo20_live_binding_10`

คำถามตัวอย่าง:

- ตัวเชื่อมทดลอง ห้องสมุดดาว จับคู่สถานะยังไง
- Demo binding Star Library How are statuses mapped?
- ตัวเชื่อมทดลอง ห้องสมุดดาว จับคู่สถานะแบบไหนและเก็บข้อมูลนานเท่าไหร่

**external_resource_key — known**
```json
"DEMO20_EXTERNAL_10"
```
**freshness_policy — known**
```json
{
  "en": "Synthetic TTL 65 seconds; no API call or live status claim",
  "th": "ค่าจำลอง TTL 65 วินาที; ไม่เรียก API และไม่ยืนยันสถานะสด"
}
```
**physical_pool_key — known**
```json
"demo20_pool_10"
```
**provider — known**
```json
"wordpress_booking"
```
**service_id — known**
```json
"demo20_service_10"
```
**status_mapping — known**
```json
[
  {
    "normalized": "free",
    "raw": "DEMO_EMPTY_10"
  },
  {
    "normalized": "occupied",
    "raw": "DEMO_BUSY_10"
  },
  {
    "normalized": "unknown",
    "raw": "DEMO_UNKNOWN_10"
  }
]
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/live_binding/demo20_live_binding_10.json)

