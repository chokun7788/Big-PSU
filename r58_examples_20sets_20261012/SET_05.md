# ชุด 05 — บัวสีคราม / Indigo Lotus

**ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION**

เกม สถานที่ ราคา กฎ บุคคล และสถานะทั้งหมดในชุดใหม่นี้แต่งขึ้นเพื่อทดสอบ ไม่ได้เป็นข้อมูล PSU หรือเกมที่มีจำหน่ายจริง คำแปลยังไม่ผ่านมนุษย์

แพลตฟอร์มตัวอย่าง: PC • จำนวนผู้เล่น 1–1 • เวลาเล่น 60 นาที / กินช่องจอง 60 นาที

## ข้อมูลครบ 24 หมวด

### ข้อมูลศูนย์ (`center`)

รหัส `demo20_center_05`

คำถามตัวอย่าง:

- ศูนย์ทดลอง บัวสีคราม อยู่ตรงไหน
- Demo venue Indigo Lotus Where is it located?
- ศูนย์ทดลอง บัวสีคราม อยู่ตึกอะไร ชั้นไหน

**address — known**
```json
{
  "en": "Fictional address 35, Example Road, Test District",
  "th": "เลขที่สมมุติ 35 ถนนตัวอย่าง แขวงทดลอง"
}
```
**building — known**
```json
"DEMO Tower A"
```
**description — known**
```json
{
  "en": "Synthetic scenario 5: Colour Blocks, not a real venue",
  "th": "สถานการณ์ทดลอง 5: ก้อนบล็อกสี ไม่ใช่สถานที่จริง"
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
  "en": "Demo venue Indigo Lotus",
  "th": "ศูนย์ทดลอง บัวสีคราม"
}
```
**operator — known**
```json
{
  "en": "Fictional Indigo Lotus operator",
  "th": "ผู้ประกอบการสมมุติ บัวสีคราม"
}
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/center/demo20_center_05.json)

### โซนบริการ (`zone`)

รหัส `demo20_zone_05`

คำถามตัวอย่าง:

- โซนทดลอง บัวสีคราม มีที่นั่งกี่ที่
- Demo zone Indigo Lotus How many seats are there?
- โซนทดลอง บัวสีคราม โซนนี้อยู่ตรงไหนและมีที่นั่งกี่ที่

**description — known**
```json
{
  "en": "Synthetic PC zone for Colour Blocks",
  "th": "โซนจำลอง PC สำหรับก้อนบล็อกสี"
}
```
**location — known**
```json
{
  "en": "Test building, floor 1, room 105",
  "th": "อาคารทดสอบ ชั้น 1 ห้อง 105"
}
```
**name — known**
```json
{
  "en": "Demo zone Indigo Lotus",
  "th": "โซนทดลอง บัวสีคราม"
}
```
**room_seats — known**
```json
5
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/zone/demo20_zone_05.json)

### รุ่นและสเปกอุปกรณ์ (`equipment_model`)

รหัส `demo20_equipment_model_05`

คำถามตัวอย่าง:

- รุ่นอุปกรณ์ บัวสีคราม สเปกมีอะไรบ้าง
- Demo model Indigo Lotus What are its specifications?
- รุ่นอุปกรณ์ บัวสีคราม เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง

**device_type — known**
```json
"pc"
```
**name — known**
```json
{
  "en": "Demo model Indigo Lotus",
  "th": "รุ่นอุปกรณ์ บัวสีคราม"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/equipment_model/demo20_equipment_model_05.json)

### เครื่องหรือทรัพยากรจริง (`resource`)

รหัส `demo20_resource_05`

คำถามตัวอย่าง:

- เครื่องทดลอง บัวสีคราม เล่นพร้อมกันได้กี่คน
- Demo station Indigo Lotus How many people can play at once?
- เครื่องทดลอง บัวสีคราม เครื่องยังใช้งานได้ไหมและรองรับกี่คน

**capacity_persons — known**
```json
1
```
**equipment_model_ids — known**
```json
[
  "demo20_equipment_model_05"
]
```
**name — known**
```json
{
  "en": "Demo station Indigo Lotus",
  "th": "เครื่องทดลอง บัวสีคราม"
}
```
**operational_status — known**
```json
"out_of_service"
```
**physical_pool_key — known**
```json
"demo20_pool_05"
```
**zone_id — known**
```json
"demo20_zone_05"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/resource/demo20_resource_05.json)

### รายการที่เลือกในระบบจอง (`service`)

รหัส `demo20_service_05`

คำถามตัวอย่าง:

- รอบทดลอง บัวสีคราม หนึ่งรอบเล่นได้กี่นาที
- Demo session Indigo Lotus How many minutes does one session last?
- รอบทดลอง บัวสีคราม เวลาเล่นกับเวลาที่กินช่องจองกี่นาที

**booking_product_key — unknown**
```json
null
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
  "en": "Demo session Indigo Lotus",
  "th": "รอบทดลอง บัวสีคราม"
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
  "demo20_resource_05"
]
```
**session_minutes — known**
```json
60
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/service/demo20_service_05.json)

### ข้อมูลเกม (`game`)

รหัส `demo20_game_05`

คำถามตัวอย่าง:

- เกมสมมุติ บัวสีคราม เล่นยังไง
- Fictional game Indigo Lotus How do I play it?
- เกมสมมุติ บัวสีคราม เกมเกี่ยวกับอะไรและเล่นยังไง

**age_rating — unknown**
```json
null
```
**edition — known**
```json
"DEMO fiction revision 5"
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
  "en": "Arrange blocks to match examples without competing; follow the demonstration controls",
  "th": "จัดบล็อกตามตัวอย่างโดยไม่มีการแข่งขัน; ใช้คำสั่งตามชุดควบคุมทดลอง"
}
```
**publisher_url — known**
```json
"https://example.invalid/demo20/fictional-game/5"
```
**summary — known**
```json
{
  "en": "Fictional test game: Arrange blocks to match examples without competing",
  "th": "เกมแต่งขึ้นเพื่อทดสอบ: จัดบล็อกตามตัวอย่างโดยไม่มีการแข่งขัน"
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
  "en": "Fictional Colour Blocks",
  "th": "เกมสมมุติ ก้อนบล็อกสี"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game/demo20_game_05.json)

### กลุ่มผู้ใช้ (`audience`)

รหัส `demo20_audience_05`

คำถามตัวอย่าง:

- กลุ่มผู้ใช้ บัวสีคราม ต้องใช้หลักฐานอะไร
- Demo visitors Indigo Lotus What proof is required?
- กลุ่มผู้ใช้ บัวสีคราม ใครใช้สิทธิ์กลุ่มนี้ได้และต้องแสดงหลักฐานอะไร

**eligibility — known**
```json
{
  "en": "Fictional group 5: free learning activity",
  "th": "ผู้ใช้สมมุติกลุ่ม 5: เข้าร่วมกิจกรรมฟรี"
}
```
**name — known**
```json
{
  "en": "Demo visitors Indigo Lotus",
  "th": "กลุ่มผู้ใช้ บัวสีคราม"
}
```
**required_proofs — unknown**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/audience/demo20_audience_05.json)

### ติดต่อ (`contact`)

รหัส `demo20_contact_05`

คำถามตัวอย่าง:

- ช่องทางช่วยเหลือ บัวสีคราม ติดต่อทางไหน
- Demo help channel Indigo Lotus How can I contact them?
- ช่องทางช่วยเหลือ บัวสีคราม ติดต่อที่ไหนและติดต่อได้ช่วงไหน

**channel — known**
```json
"onsite"
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
  "en": "Fictional support for Free learning activity",
  "th": "สอบถามสมมุติเรื่อง กิจกรรมเรียนรู้ฟรี"
}
```
**value — known**
```json
"DEMO desk Indigo Lotus"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/contact/demo20_contact_05.json)

### ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`)

รหัส `demo20_procedure_05`

คำถามตัวอย่าง:

- ขั้นตอนทดลอง บัวสีคราม ต้องทำยังไงบ้าง
- Demo procedure Indigo Lotus What steps should I follow?
- ขั้นตอนทดลอง บัวสีคราม มีขั้นตอนอะไรและต้องใช้เอกสารอะไร

**deadline_minutes — known**
```json
0
```
**outcome — known**
```json
{
  "en": "Demo outcome: Free learning activity checked",
  "th": "ผลทดสอบ: ตรวจสอบ กิจกรรมเรียนรู้ฟรี เสร็จ"
}
```
**preconditions — known**
```json
[]
```
**required_documents — known**
```json
[
  "DEMO pass Indigo Lotus"
]
```
**steps — known**
```json
[
  {
    "contact_id": null,
    "instruction": {
      "en": "Select the fictional Indigo Lotus service",
      "th": "เลือกบริการสมมุติ บัวสีคราม"
    },
    "order": 1
  },
  {
    "contact_id": "demo20_contact_05",
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
"DEMO Free learning activity"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/procedure/demo20_procedure_05.json)

### นโยบายและกฎศูนย์ (`policy`)

รหัส `demo20_policy_05`

คำถามตัวอย่าง:

- ข้อกำหนดทดลอง บัวสีคราม กฎเป็นยังไง
- Demo policy Indigo Lotus What are the rules?
- ข้อกำหนดทดลอง บัวสีคราม อนุญาตไหมและมีข้อยกเว้นอะไร

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
  "en": "Fictional rule for Free learning activity: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "กติกาสมมุติเรื่องกิจกรรมเรียนรู้ฟรี: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
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
"demo20_procedure_05"
```
**subject — known**
```json
{
  "en": "Demo policy Indigo Lotus",
  "th": "ข้อกำหนดทดลอง บัวสีคราม"
}
```
**topic — known**
```json
"DEMO Free learning activity"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/policy/demo20_policy_05.json)

### สิ่งอำนวยความสะดวก (`facility`)

รหัส `demo20_facility_05`

คำถามตัวอย่าง:

- พื้นที่พัก บัวสีคราม อยู่ตรงไหนในร้าน
- Demo amenity Indigo Lotus Where in the venue is it?
- พื้นที่พัก บัวสีคราม อยู่ตรงไหนและคนที่ต้องการความช่วยเหลือเข้าใช้ยังไง

**accessibility — unknown**
```json
null
```
**location — known**
```json
{
  "en": "Learning table in demo room 105",
  "th": "โต๊ะเรียนรู้ อยู่ห้องทดสอบ 105"
}
```
**name — known**
```json
{
  "en": "Demo amenity Indigo Lotus",
  "th": "พื้นที่พัก บัวสีคราม"
}
```
**usage_conditions — known**
```json
{
  "en": "Demo sessions only; ask the operator first",
  "th": "ใช้ตามรอบทดลอง; ต้องขอผู้ดูแลก่อน"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/facility/demo20_facility_05.json)

### เกมที่ศูนย์มีให้เล่นจริง (`game_service`)

รหัส `demo20_game_service_05`

คำถามตัวอย่าง:

- การติดตั้งทดลอง บัวสีคราม มีให้เล่นหรือยัง
- Demo installation Indigo Lotus Is this game offered?
- การติดตั้งทดลอง บัวสีคราม มีให้เล่นไหมและติดตั้งรุ่นไหน

**account_policy_id — known**
```json
"demo20_policy_05"
```
**game_id — known**
```json
"demo20_game_05"
```
**game_version — unknown**
```json
null
```
**installed_resource_ids — known**
```json
[
  "demo20_resource_05"
]
```
**offered — known**
```json
true
```
**service_id — known**
```json
"demo20_service_05"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_service/demo20_game_service_05.json)

### รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`)

รหัส `demo20_game_mode_05`

คำถามตัวอย่าง:

- โหมดทดลอง บัวสีคราม เล่นพร้อมกันได้สูงสุดกี่คน
- Demo mode Indigo Lotus How many people can play together at most?
- โหมดทดลอง บัวสีคราม ต้องมีขั้นต่ำกี่คนและเล่นได้สูงสุดกี่คน

**game_id — known**
```json
"demo20_game_05"
```
**mode_name — known**
```json
{
  "en": "Demo mode Indigo Lotus",
  "th": "โหมดทดลอง บัวสีคราม"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/game_mode/demo20_game_mode_05.json)

### วิธีเล่นและปุ่ม (`control_set`)

รหัส `demo20_control_set_05`

คำถามตัวอย่าง:

- ชุดควบคุมทดลอง บัวสีคราม ปุ่มอะไรบ้าง
- Demo controls Indigo Lotus What are the controls?
- ชุดควบคุมทดลอง บัวสีคราม ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร

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
      "en": "Fictional input for Colour Blocks",
      "th": "คำสั่งสมมุติของ ก้อนบล็อกสี"
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
      "en": "Fictional input for Colour Blocks",
      "th": "คำสั่งสมมุติของ ก้อนบล็อกสี"
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
      "en": "Fictional input for Colour Blocks",
      "th": "คำสั่งสมมุติของ ก้อนบล็อกสี"
    },
    "gesture": "press"
  }
]
```
**game_id — known**
```json
"demo20_game_05"
```
**game_version — known**
```json
"DEMO BUILD 5"
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
"DEMO_LAYOUT_5"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/control_set/demo20_control_set_05.json)

### ราคาต่อบริการ (`rate`)

รหัส `demo20_rate_05`

คำถามตัวอย่าง:

- อัตราทดลอง บัวสีคราม ราคาเท่าไหร่
- Demo tariff Indigo Lotus How much does it cost?
- อัตราทดลอง บัวสีคราม ราคาเท่าไหร่และได้กี่นาที

**amount_minor — known**
```json
0
```
**audience_id — known**
```json
"demo20_audience_05"
```
**calculation_rule — known**
```json
"fixed"
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
"demo20_service_05"
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

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rate/demo20_rate_05.json)

### ราคาเหมาโซน/ห้อง (`rental_package`)

รหัส `demo20_rental_package_05`

คำถามตัวอย่าง:

- แพ็กเกจทดลอง บัวสีคราม เหมาเท่าไหร่
- Demo package Indigo Lotus How much is the rental?
- แพ็กเกจทดลอง บัวสีคราม ราคาเหมาเท่าไหร่และรวมอุปกรณ์อะไร

**amount_minor — known**
```json
0
```
**audience_id — known**
```json
"demo20_audience_05"
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
  "en": "Fictional Indigo Lotus station and PC inputs",
  "th": "เครื่องสมมุติ บัวสีคราม พร้อมอุปกรณ์ PC"
}
```
**name — known**
```json
{
  "en": "Demo package Indigo Lotus",
  "th": "แพ็กเกจทดลอง บัวสีคราม"
}
```
**period_label — known**
```json
"custom"
```
**room_seats — known**
```json
5
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
  "demo20_zone_05"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/rental_package/demo20_rental_package_05.json)

### ตารางบริการ (`schedule`)

รหัส `demo20_schedule_05`

คำถามตัวอย่าง:

- ตารางทดลอง บัวสีคราม จองช่วงไหนได้บ้าง
- Demo timetable Indigo Lotus What are the booking hours?
- ตารางทดลอง บัวสีคราม เปิดช่วงไหนและพักบำรุงรักษาตอนไหน

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
  "en": "Synthetic Indigo Lotus schedule with maintenance",
  "th": "ตารางสมมุติ บัวสีคราม มีพักบำรุงรักษา"
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
  "demo20_zone_05"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/schedule/demo20_schedule_05.json)

### วันปิด/ข้อยกเว้น (`closure`)

รหัส `demo20_closure_05`

คำถามตัวอย่าง:

- ประกาศวันทดลอง บัวสีคราม วันนั้นปิดไหม
- Demo date notice Indigo Lotus Is it closed on that date?
- ประกาศวันทดลอง บัวสีคราม วันนั้นเปิดปิดยังไงและเพราะอะไร

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
"2026-12-05"
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
  "en": "Synthetic Indigo Lotus date notice: open_override",
  "th": "ประกาศสมมุติ บัวสีคราม: open_override"
}
```
**resolution_policy_id — known**
```json
"demo20_policy_05"
```
**state — known**
```json
"open_override"
```
**zone_ids — known**
```json
[
  "demo20_zone_05"
]
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/closure/demo20_closure_05.json)

### รายการแข่งขันและฉบับกติกา (`competition`)

รหัส `demo20_competition_05`

คำถามตัวอย่าง:

- รายการฝึก บัวสีคราม ใช้กติกาฉบับไหน
- Demo event Indigo Lotus Which rulebook release applies?
- รายการฝึก บัวสีคราม ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่

**competition_dates — known**
```json
[
  "2026-12-05"
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
  "en": "Demo event Indigo Lotus",
  "th": "รายการฝึก บัวสีคราม"
}
```
**game_id — known**
```json
"demo20_game_05"
```
**rulebook_release — known**
```json
"DEMO20_REV_5"
```
**supersedes_id — not_applicable**
```json
null
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition/demo20_competition_05.json)

### ข้อกติกาการแข่งขัน (`competition_rule`)

รหัส `demo20_competition_rule_05`

คำถามตัวอย่าง:

- ข้อการแข่งขันทดลอง บัวสีคราม ข้อนี้กำหนดอะไร
- Demo rule Indigo Lotus What does this rule require?
- ข้อการแข่งขันทดลอง บัวสีคราม กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม

**competition_id — known**
```json
"demo20_competition_05"
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
"pre_match_on_site"
```
**heading — known**
```json
{
  "en": "Demo rule Indigo Lotus",
  "th": "ข้อการแข่งขันทดลอง บัวสีคราม"
}
```
**section_number — known**
```json
"1.5"
```
**text — known**
```json
{
  "en": "Fictional clause 5: for Free learning activity, follow decision allowed; exception requires written demo operator approval; not actual rules",
  "th": "ข้อสมมุติ 5: กิจกรรมเรียนรู้ฟรี ให้ปฏิบัติตามคำตัดสิน allowed; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/competition_rule/demo20_competition_rule_05.json)

### ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`)

รหัส `demo20_news_05`

คำถามตัวอย่าง:

- ข่าวทดลอง บัวสีคราม ประกาศว่าอะไร
- Demo bulletin Indigo Lotus What does the announcement say?
- ข่าวทดลอง บัวสีคราม ประกาศอะไรและกิจกรรมเริ่มจบเมื่อไหร่

**audience_ids — known**
```json
[
  "demo20_audience_05"
]
```
**body — known**
```json
{
  "en": "Synthetic bulletin: Colour Blocks activity for 1–1 people; no actual payment",
  "th": "ข่าวสมมุติ: กิจกรรมก้อนบล็อกสี สำหรับกลุ่ม 1–1 คน; ไม่มีรับเงินจริง"
}
```
**contact_id — known**
```json
"demo20_contact_05"
```
**event_end — known**
```json
"2026-12-05T12:00:00+07:00"
```
**event_start — known**
```json
"2026-12-05T10:00:00+07:00"
```
**registration_url — known**
```json
"https://example.invalid/demo20/register/5"
```
**title — known**
```json
{
  "en": "Demo bulletin Indigo Lotus",
  "th": "ข่าวทดลอง บัวสีคราม"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/news/demo20_news_05.json)

### บุคลากร/ทีมที่เปิดเผยได้ (`person`)

รหัส `demo20_person_05`

คำถามตัวอย่าง:

- ผู้ดูแลสมมุติ บัวสีคราม รับผิดชอบอะไร
- Fictional host Indigo Lotus What is their role?
- ผู้ดูแลสมมุติ บัวสีคราม รับผิดชอบเรื่องอะไรและติดต่อทางไหน

**display_name — known**
```json
{
  "en": "Fictional host Indigo Lotus",
  "th": "ผู้ดูแลสมมุติ บัวสีคราม"
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
  "en": "Fictional host for Free learning activity",
  "th": "ผู้ดูแลสมมุติเรื่อง กิจกรรมเรียนรู้ฟรี"
}
```
**team — known**
```json
{
  "en": "Demo Indigo Lotus team",
  "th": "ทีมทดสอบ บัวสีคราม"
}
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/person/demo20_person_05.json)

### คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`)

รหัส `demo20_faq_05`

คำถามตัวอย่าง:

- คำถามตัวอย่าง บัวสีคราม คำตอบคืออะไร
- Demo enquiry Indigo Lotus What is the answer?
- คำถามตัวอย่าง บัวสีคราม คำตอบคืออะไรและใช้กับกรณีไหน

**answer — known**
```json
{
  "en": "Example answer: Fictional rule for Free learning activity: allowed; contact the demo operator if requirements are not met. Not PSU policy.",
  "th": "คำตอบตัวอย่าง: กติกาสมมุติเรื่องกิจกรรมเรียนรู้ฟรี: allowed; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU"
}
```
**question — known**
```json
{
  "en": "Demo enquiry Indigo Lotus",
  "th": "คำถามตัวอย่าง บัวสีคราม"
}
```
**related_ids — known**
```json
[
  "demo20_policy_05",
  "demo20_procedure_05"
]
```
**scope_note — known**
```json
{
  "en": "Only applies to fictional Indigo Lotus scenario",
  "th": "ใช้ได้เฉพาะสถานการณ์สมมุติ บัวสีคราม"
}
```
**topic — known**
```json
"DEMO Free learning activity"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/faq/demo20_faq_05.json)

### การเชื่อมสถานะสด (`live_binding`)

รหัส `demo20_live_binding_05`

คำถามตัวอย่าง:

- ตัวเชื่อมทดลอง บัวสีคราม จับคู่สถานะยังไง
- Demo binding Indigo Lotus How are statuses mapped?
- ตัวเชื่อมทดลอง บัวสีคราม จับคู่สถานะแบบไหนและเก็บข้อมูลนานเท่าไหร่

**external_resource_key — known**
```json
"DEMO20_EXTERNAL_5"
```
**freshness_policy — known**
```json
{
  "en": "Synthetic TTL 40 seconds; no API call or live status claim",
  "th": "ค่าจำลอง TTL 40 วินาที; ไม่เรียก API และไม่ยืนยันสถานะสด"
}
```
**physical_pool_key — known**
```json
"demo20_pool_05"
```
**provider — known**
```json
"wordpress_booking"
```
**service_id — known**
```json
"demo20_service_05"
```
**status_mapping — known**
```json
[
  {
    "normalized": "free",
    "raw": "DEMO_EMPTY_5"
  },
  {
    "normalized": "occupied",
    "raw": "DEMO_BUSY_5"
  },
  {
    "normalized": "unknown",
    "raw": "DEMO_UNKNOWN_5"
  }
]
```
**timezone — known**
```json
"Asia/Bangkok"
```

[JSON record](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r58_examples_20sets_20261012/records/live_binding/demo20_live_binding_05.json)

