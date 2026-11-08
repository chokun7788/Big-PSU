# ชุด 13 — จันทร์เสี้ยว / Crescent

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

เกม สถานที่ ราคา กฎ บุคคล และสถานะทั้งหมดในชุดใหม่นี้แต่งขึ้นเพื่อทดสอบ ไม่ได้เป็นข้อมูล PSU หรือเกมที่มีจำหน่ายจริง คำแปลยังไม่ผ่านมนุษย์

แพลตฟอร์มตัวอย่าง: Cockpit • จำนวนผู้เล่น 1–1 • เวลาเล่น 60 นาที / กินช่องจอง 60 นาที

## ข้อมูลครบ 24 หมวด

### ข้อมูลศูนย์ (`center`)

รหัส `demo20_center_13`

คำถามตัวอย่าง:

- ศูนย์ทดลอง จันทร์เสี้ยว อยู่ตรงไหน
- Demo venue Crescent Where is it located?
- ศูนย์ทดลอง จันทร์เสี้ยว อยู่ตึกอะไร ชั้นไหน

**address — known**
```json
{
  "en": "Fictional address 91, Example Road, Test District",
  "th": "เลขที่สมมุติ 91 ถนนตัวอย่าง แขวงทดลอง"
}
```
**building — known**
```json
"DEMO Tower D"
```
**description — known**
```json
{
  "en": "Synthetic scenario 13: Tiny Convoy, not a real venue",
  "th": "สถานการณ์ทดลอง 13: ขบวนรถจิ๋ว ไม่ใช่สถานที่จริง"
}
```
**floor — known**
```json
"4"
```
**map_url — known**
```json
"https://example.invalid/demo20/map/13"
```
**name — known**
```json
{
  "en": "Demo venue Crescent",
  "th": "ศูนย์ทดลอง จันทร์เสี้ยว"
}
```
**operator — known**
```json
{
  "en": "Fictional Crescent operator",
  "th": "ผู้ประกอบการสมมุติ จันทร์เสี้ยว"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/center/demo20_center_13.json)

### โซนบริการ (`zone`)

รหัส `demo20_zone_13`

คำถามตัวอย่าง:

- โซนทดลอง จันทร์เสี้ยว มีที่นั่งกี่ที่
- Demo zone Crescent How many seats are there?
- โซนทดลอง จันทร์เสี้ยว โซนนี้อยู่ตรงไหนและมีที่นั่งกี่ที่

**description — known**
```json
{
  "en": "Synthetic Cockpit zone for Tiny Convoy",
  "th": "โซนจำลอง Cockpit สำหรับขบวนรถจิ๋ว"
}
```
**location — known**
```json
{
  "en": "Test building, floor 4, room 113",
  "th": "อาคารทดสอบ ชั้น 4 ห้อง 113"
}
```
**name — known**
```json
{
  "en": "Demo zone Crescent",
  "th": "โซนทดลอง จันทร์เสี้ยว"
}
```
**room_seats — known**
```json
4
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_13.json)

### รุ่นและสเปกอุปกรณ์ (`equipment_model`)

รหัส `demo20_equipment_model_13`

คำถามตัวอย่าง:

- รุ่นอุปกรณ์ จันทร์เสี้ยว สเปกมีอะไรบ้าง
- Demo model Crescent What are its specifications?
- รุ่นอุปกรณ์ จันทร์เสี้ยว เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง

**device_type — known**
```json
"wheel"
```
**name — known**
```json
{
  "en": "Demo model Crescent",
  "th": "รุ่นอุปกรณ์ จันทร์เสี้ยว"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_13.json)

### เครื่องหรือทรัพยากรจริง (`resource`)

รหัส `demo20_resource_13`

คำถามตัวอย่าง:

- เครื่องทดลอง จันทร์เสี้ยว เล่นพร้อมกันได้กี่คน
- Demo station Crescent How many people can play at once?
- เครื่องทดลอง จันทร์เสี้ยว เครื่องยังใช้งานได้ไหมและรองรับกี่คน

**capacity_persons — known**
```json
1
```
**equipment_model_ids — known**
```json
[
  "demo20_equipment_model_13"
]
```
**name — known**
```json
{
  "en": "Demo station Crescent",
  "th": "เครื่องทดลอง จันทร์เสี้ยว"
}
```
**operational_status — known**
```json
"in_service"
```
**physical_pool_key — known**
```json
"demo20_pool_13"
```
**zone_id — known**
```json
"demo20_zone_13"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/resource/demo20_resource_13.json)

### รายการที่เลือกในระบบจอง (`service`)

รหัส `demo20_service_13`

คำถามตัวอย่าง:

- รอบทดลอง จันทร์เสี้ยว หนึ่งรอบเล่นได้กี่นาที
- Demo session Crescent How many minutes does one session last?
- รอบทดลอง จันทร์เสี้ยว เวลาเล่นกับเวลาที่กินช่องจองกี่นาที

**booking_product_key — known**
```json
"DEMO20_BOOKING_13"
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
  "en": "Demo session Crescent",
  "th": "รอบทดลอง จันทร์เสี้ยว"
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
  "demo20_resource_13"
]
```
**session_minutes — known**
```json
60
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_13.json)

### ข้อมูลเกม (`game`)

รหัส `demo20_game_13`

คำถามตัวอย่าง:

- เกมสมมุติ จันทร์เสี้ยว เล่นยังไง
- Fictional game Crescent How do I play it?
- เกมสมมุติ จันทร์เสี้ยว เกมเกี่ยวกับอะไรและเล่นยังไง

**age_rating — known**
```json
{
  "en": "Synthetic DEMO rating 6",
  "th": "เรตอายุสมมุติ DEMO 6"
}
```
**edition — known**
```json
"DEMO fiction revision 13"
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
  "en": "Steer a convoy to its destination; follow the demonstration controls",
  "th": "ควบคุมรถหลายคันให้วิ่งถึงปลายทาง; ใช้คำสั่งตามชุดควบคุมทดลอง"
}
```
**publisher_url — known**
```json
"https://example.invalid/demo20/fictional-game/13"
```
**summary — known**
```json
{
  "en": "Fictional test game: Steer a convoy to its destination",
  "th": "เกมแต่งขึ้นเพื่อทดสอบ: ควบคุมรถหลายคันให้วิ่งถึงปลายทาง"
}
```
**supported_platforms — known**
```json
[
  "Cockpit"
]
```
**title — known**
```json
{
  "en": "Fictional Tiny Convoy",
  "th": "เกมสมมุติ ขบวนรถจิ๋ว"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_13.json)

### กลุ่มผู้ใช้ (`audience`)

รหัส `demo20_audience_13`

คำถามตัวอย่าง:

- กลุ่มผู้ใช้ จันทร์เสี้ยว ต้องใช้หลักฐานอะไร
- Demo visitors Crescent What proof is required?
- กลุ่มผู้ใช้ จันทร์เสี้ยว ใครใช้สิทธิ์กลุ่มนี้ได้และต้องแสดงหลักฐานอะไร

**eligibility — known**
```json
{
  "en": "Fictional group 13: demo sessions only",
  "th": "ผู้ใช้สมมุติกลุ่ม 13: ใช้บริการตามรอบทดลอง"
}
```
**name — known**
```json
{
  "en": "Demo visitors Crescent",
  "th": "กลุ่มผู้ใช้ จันทร์เสี้ยว"
}
```
**required_proofs — known**
```json
[
  "DEMO pass Crescent"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/audience/demo20_audience_13.json)

### ติดต่อ (`contact`)

รหัส `demo20_contact_13`

คำถามตัวอย่าง:

- ช่องทางช่วยเหลือ จันทร์เสี้ยว ติดต่อทางไหน
- Demo help channel Crescent How can I contact them?
- ช่องทางช่วยเหลือ จันทร์เสี้ยว ติดต่อที่ไหนและติดต่อได้ช่วงไหน

**channel — known**
```json
"website"
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
  "en": "Fictional support for Practice before starting",
  "th": "สอบถามสมมุติเรื่อง ฝึกก่อนเริ่ม"
}
```
**value — known**
```json
"https://example.invalid/demo20/contact/13"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_13.json)

### ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`)

รหัส `demo20_procedure_13`

คำถามตัวอย่าง:

- ขั้นตอนทดลอง จันทร์เสี้ยว ต้องทำยังไงบ้าง
- Demo procedure Crescent What steps should I follow?
- ขั้นตอนทดลอง จันทร์เสี้ยว มีขั้นตอนอะไรและต้องใช้เอกสารอะไร

**deadline_minutes — known**
```json
30
```
**outcome — known**
```json
{
  "en": "Demo outcome: Practice before starting checked",
  "th": "ผลทดสอบ: ตรวจสอบ ฝึกก่อนเริ่ม เสร็จ"
}
```
**preconditions — known**
```json
[]
```
**required_documents — known**
```json
[
  "DEMO pass Crescent"
]
```
**steps — known**
```json
[
  {
    "contact_id": null,
    "instruction": {
      "en": "Select the fictional Crescent service",
      "th": "เลือกบริการสมมุติ จันทร์เสี้ยว"
    },
    "order": 1
  },
  {
    "contact_id": "demo20_contact_13",
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
"DEMO Practice before starting"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_13.json)

### นโยบายและกฎศูนย์ (`policy`)

รหัส `demo20_policy_13`

คำถามตัวอย่าง:

- ข้อกำหนดทดลอง จันทร์เสี้ยว กฎเป็นยังไง
- Demo policy Crescent What are the rules?
- ข้อกำหนดทดลอง จันทร์เสี้ยว อนุญาตไหมและมีข้อยกเว้นอะไร

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
  "en": "Fictional rule for Practice before starting: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "กติกาสมมุติเรื่องฝึกก่อนเริ่ม: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
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
"demo20_procedure_13"
```
**subject — known**
```json
{
  "en": "Demo policy Crescent",
  "th": "ข้อกำหนดทดลอง จันทร์เสี้ยว"
}
```
**topic — known**
```json
"DEMO Practice before starting"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/policy/demo20_policy_13.json)

### สิ่งอำนวยความสะดวก (`facility`)

รหัส `demo20_facility_13`

คำถามตัวอย่าง:

- พื้นที่พัก จันทร์เสี้ยว อยู่ตรงไหนในร้าน
- Demo amenity Crescent Where in the venue is it?
- พื้นที่พัก จันทร์เสี้ยว อยู่ตรงไหนและคนที่ต้องการความช่วยเหลือเข้าใช้ยังไง

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
  "en": "Driving practice board in demo room 113",
  "th": "ป้ายฝึกขับ อยู่ห้องทดสอบ 113"
}
```
**name — known**
```json
{
  "en": "Demo amenity Crescent",
  "th": "พื้นที่พัก จันทร์เสี้ยว"
}
```
**usage_conditions — known**
```json
{
  "en": "Demo sessions only; ask the operator first",
  "th": "ใช้ตามรอบทดลอง; ต้องขอผู้ดูแลก่อน"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/facility/demo20_facility_13.json)

### เกมที่ศูนย์มีให้เล่นจริง (`game_service`)

รหัส `demo20_game_service_13`

คำถามตัวอย่าง:

- การติดตั้งทดลอง จันทร์เสี้ยว มีให้เล่นหรือยัง
- Demo installation Crescent Is this game offered?
- การติดตั้งทดลอง จันทร์เสี้ยว มีให้เล่นไหมและติดตั้งรุ่นไหน

**account_policy_id — known**
```json
"demo20_policy_13"
```
**game_id — known**
```json
"demo20_game_13"
```
**game_version — known**
```json
"DEMO BUILD 13"
```
**installed_resource_ids — known**
```json
[
  "demo20_resource_13"
]
```
**offered — known**
```json
true
```
**service_id — known**
```json
"demo20_service_13"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_service/demo20_game_service_13.json)

### รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`)

รหัส `demo20_game_mode_13`

คำถามตัวอย่าง:

- โหมดทดลอง จันทร์เสี้ยว เล่นพร้อมกันได้สูงสุดกี่คน
- Demo mode Crescent How many people can play together at most?
- โหมดทดลอง จันทร์เสี้ยว ต้องมีขั้นต่ำกี่คนและเล่นได้สูงสุดกี่คน

**game_id — known**
```json
"demo20_game_13"
```
**mode_name — known**
```json
{
  "en": "Demo mode Crescent",
  "th": "โหมดทดลอง จันทร์เสี้ยว"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_mode/demo20_game_mode_13.json)

### วิธีเล่นและปุ่ม (`control_set`)

รหัส `demo20_control_set_13`

คำถามตัวอย่าง:

- ชุดควบคุมทดลอง จันทร์เสี้ยว ปุ่มอะไรบ้าง
- Demo controls Crescent What are the controls?
- ชุดควบคุมทดลอง จันทร์เสี้ยว ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร

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
      "en": "Fictional input for Tiny Convoy",
      "th": "คำสั่งสมมุติของ ขบวนรถจิ๋ว"
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
      "en": "Fictional input for Tiny Convoy",
      "th": "คำสั่งสมมุติของ ขบวนรถจิ๋ว"
    },
    "gesture": "press"
  }
]
```
**game_id — known**
```json
"demo20_game_13"
```
**game_version — known**
```json
"DEMO BUILD 13"
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
"DEMO_LAYOUT_13"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_13.json)

### ราคาต่อบริการ (`rate`)

รหัส `demo20_rate_13`

คำถามตัวอย่าง:

- อัตราทดลอง จันทร์เสี้ยว ราคาเท่าไหร่
- Demo tariff Crescent How much does it cost?
- อัตราทดลอง จันทร์เสี้ยว ราคาเท่าไหร่และได้กี่นาที

**amount_minor — known**
```json
11000
```
**audience_id — known**
```json
"demo20_audience_13"
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
"demo20_service_13"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rate/demo20_rate_13.json)

### ราคาเหมาโซน/ห้อง (`rental_package`)

รหัส `demo20_rental_package_13`

คำถามตัวอย่าง:

- แพ็กเกจทดลอง จันทร์เสี้ยว เหมาเท่าไหร่
- Demo package Crescent How much is the rental?
- แพ็กเกจทดลอง จันทร์เสี้ยว ราคาเหมาเท่าไหร่และรวมอุปกรณ์อะไร

**amount_minor — known**
```json
34250
```
**audience_id — known**
```json
"demo20_audience_13"
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
  "en": "Fictional Crescent station and Cockpit inputs",
  "th": "เครื่องสมมุติ จันทร์เสี้ยว พร้อมอุปกรณ์ Cockpit"
}
```
**name — known**
```json
{
  "en": "Demo package Crescent",
  "th": "แพ็กเกจทดลอง จันทร์เสี้ยว"
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
  "demo20_zone_13"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rental_package/demo20_rental_package_13.json)

### ตารางบริการ (`schedule`)

รหัส `demo20_schedule_13`

คำถามตัวอย่าง:

- ตารางทดลอง จันทร์เสี้ยว จองช่วงไหนได้บ้าง
- Demo timetable Crescent What are the booking hours?
- ตารางทดลอง จันทร์เสี้ยว เปิดช่วงไหนและพักบำรุงรักษาตอนไหน

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
  "en": "Synthetic Crescent schedule with maintenance",
  "th": "ตารางสมมุติ จันทร์เสี้ยว มีพักบำรุงรักษา"
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
  "demo20_zone_13"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_13.json)

### วันปิด/ข้อยกเว้น (`closure`)

รหัส `demo20_closure_13`

คำถามตัวอย่าง:

- ประกาศวันทดลอง จันทร์เสี้ยว วันนั้นปิดไหม
- Demo date notice Crescent Is it closed on that date?
- ประกาศวันทดลอง จันทร์เสี้ยว วันนั้นเปิดปิดยังไงและเพราะอะไร

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
"2026-12-13"
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
  "en": "Synthetic Crescent date notice: modified_hours",
  "th": "ประกาศสมมุติ จันทร์เสี้ยว: modified_hours"
}
```
**resolution_policy_id — known**
```json
"demo20_policy_13"
```
**state — known**
```json
"modified_hours"
```
**zone_ids — known**
```json
[
  "demo20_zone_13"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/closure/demo20_closure_13.json)

### รายการแข่งขันและฉบับกติกา (`competition`)

รหัส `demo20_competition_13`

คำถามตัวอย่าง:

- รายการฝึก จันทร์เสี้ยว ใช้กติกาฉบับไหน
- Demo event Crescent Which rulebook release applies?
- รายการฝึก จันทร์เสี้ยว ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่

**competition_dates — known**
```json
[
  "2026-12-13"
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
  "en": "Demo event Crescent",
  "th": "รายการฝึก จันทร์เสี้ยว"
}
```
**game_id — known**
```json
"demo20_game_13"
```
**rulebook_release — known**
```json
"DEMO20_REV_13"
```
**supersedes_id — not_applicable**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_13.json)

### ข้อกติกาการแข่งขัน (`competition_rule`)

รหัส `demo20_competition_rule_13`

คำถามตัวอย่าง:

- ข้อการแข่งขันทดลอง จันทร์เสี้ยว ข้อนี้กำหนดอะไร
- Demo rule Crescent What does this rule require?
- ข้อการแข่งขันทดลอง จันทร์เสี้ยว กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม

**competition_id — known**
```json
"demo20_competition_13"
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
"competition_format"
```
**heading — known**
```json
{
  "en": "Demo rule Crescent",
  "th": "ข้อการแข่งขันทดลอง จันทร์เสี้ยว"
}
```
**section_number — known**
```json
"4.13"
```
**text — known**
```json
{
  "en": "Fictional clause 13: for Practice before starting, follow decision allowed; exception requires written demo operator approval; not actual rules",
  "th": "ข้อสมมุติ 13: ฝึกก่อนเริ่ม ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_13.json)

### ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`)

รหัส `demo20_news_13`

คำถามตัวอย่าง:

- ข่าวทดลอง จันทร์เสี้ยว ประกาศว่าอะไร
- Demo bulletin Crescent What does the announcement say?
- ข่าวทดลอง จันทร์เสี้ยว ประกาศอะไรและกิจกรรมเริ่มจบเมื่อไหร่

**audience_ids — known**
```json
[
  "demo20_audience_13"
]
```
**body — known**
```json
{
  "en": "Synthetic bulletin: Tiny Convoy activity for 1–1 people; no actual payment",
  "th": "ข่าวสมมุติ: กิจกรรมขบวนรถจิ๋ว สำหรับกลุ่ม 1–1 คน; ไม่มีรับเงินจริง"
}
```
**contact_id — known**
```json
"demo20_contact_13"
```
**event_end — known**
```json
"2026-12-13T12:00:00+07:00"
```
**event_start — known**
```json
"2026-12-13T10:00:00+07:00"
```
**registration_url — known**
```json
"https://example.invalid/demo20/register/13"
```
**title — known**
```json
{
  "en": "Demo bulletin Crescent",
  "th": "ข่าวทดลอง จันทร์เสี้ยว"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/news/demo20_news_13.json)

### บุคลากร/ทีมที่เปิดเผยได้ (`person`)

รหัส `demo20_person_13`

คำถามตัวอย่าง:

- ผู้ดูแลสมมุติ จันทร์เสี้ยว รับผิดชอบอะไร
- Fictional host Crescent What is their role?
- ผู้ดูแลสมมุติ จันทร์เสี้ยว รับผิดชอบเรื่องอะไรและติดต่อทางไหน

**display_name — known**
```json
{
  "en": "Fictional host Crescent",
  "th": "ผู้ดูแลสมมุติ จันทร์เสี้ยว"
}
```
**public_contact_id — known**
```json
"demo20_contact_13"
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
  "en": "Fictional host for Practice before starting",
  "th": "ผู้ดูแลสมมุติเรื่อง ฝึกก่อนเริ่ม"
}
```
**team — known**
```json
{
  "en": "Demo Crescent team",
  "th": "ทีมทดสอบ จันทร์เสี้ยว"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/person/demo20_person_13.json)

### คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`)

รหัส `demo20_faq_13`

คำถามตัวอย่าง:

- คำถามตัวอย่าง จันทร์เสี้ยว คำตอบคืออะไร
- Demo enquiry Crescent What is the answer?
- คำถามตัวอย่าง จันทร์เสี้ยว คำตอบคืออะไรและใช้กับกรณีไหน

**answer — known**
```json
{
  "en": "Example answer: Fictional rule for Practice before starting: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องฝึกก่อนเริ่ม: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
}
```
**question — known**
```json
{
  "en": "Demo enquiry Crescent",
  "th": "คำถามตัวอย่าง จันทร์เสี้ยว"
}
```
**related_ids — known**
```json
[
  "demo20_policy_13",
  "demo20_procedure_13"
]
```
**scope_note — known**
```json
{
  "en": "Only applies to fictional Crescent scenario",
  "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ จันทร์เสี้ยว"
}
```
**topic — known**
```json
"DEMO Practice before starting"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_13.json)

### การเชื่อมสถานะสด (`live_binding`)

รหัส `demo20_live_binding_13`

คำถามตัวอย่าง:

- ตัวเชื่อมทดลอง จันทร์เสี้ยว จับคู่สถานะยังไง
- Demo binding Crescent How are statuses mapped?
- ตัวเชื่อมทดลอง จันทร์เสี้ยว จับคู่สถานะแบบไหนและเก็บข้อมูลนานเท่าไหร่

**external_resource_key — known**
```json
"DEMO20_EXTERNAL_13"
```
**freshness_policy — known**
```json
{
  "en": "Synthetic TTL 80 seconds; no API call or live status claim",
  "th": "ค่าจำลอง TTL 80 วินาที; ไม่เรียก API และไม่ยืนยันสถานะสด"
}
```
**physical_pool_key — known**
```json
"demo20_pool_13"
```
**provider — known**
```json
"wordpress_booking"
```
**service_id — known**
```json
"demo20_service_13"
```
**status_mapping — known**
```json
[
  {
    "normalized": "free",
    "raw": "DEMO_EMPTY_13"
  },
  {
    "normalized": "occupied",
    "raw": "DEMO_BUSY_13"
  },
  {
    "normalized": "unknown",
    "raw": "DEMO_UNKNOWN_13"
  }
]
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/live_binding/demo20_live_binding_13.json)

