# Format กลาง: ข้อมูล 24 หมวด → งานที่แชทควรตอบได้

วันที่ 18 ตุลาคม 2026 — รายชื่อ field และ publish_core ดึงจาก catalog.json ของ R78 แบบอ่านอย่างเดียว ส่วน task/readiness/UI เป็นข้อเสนอพัฒนา ไม่ใช่สิ่งที่ระบบรับรองครบแล้ว

[Catalog ปัจจุบัน](<C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r78_web_session_check_20261016/system/app/knowledge/common/catalog.json>)
 
## หลักในการกรอกและบอกความพร้อม

- ทุก record มี stable identity, revision, lifecycle, localization, evidence และ validity ตาม envelope นอก fields; ตารางนี้แสดง fields ภายใน kind
- `publish_core` เป็นเงื่อนไขปัจจุบันของ schema ไม่ใช่ required_for_task ครบทุกชนิดคำถาม; validation จริงยังมีเงื่อนไขอื่น
- known = มีค่าที่อ้างอิงได้; unknown = ยังไม่ทราบ; conflicted = หลักฐานขัดกัน; ห้ามใช้เลข 0, false หรือ list ว่างแทน unknown
- เจ้าของเห็นชื่อหมวด/คำอธิบายภาษาไทยและเลือกรายการอ้างอิงจาก UI ระบบจัดการ record IDs ให้
- ต้องมีสามสถานะแยก: record พร้อมเผยแพร่หรือไม่, task ใดตอบได้แล้ว, ภาษาใดมีข้อมูลและ review สถานะใด
- R88 มี 602 heads ใน 21 kinds; schema มี 24 kinds อีกสาม kind คือ game_mode, news, live_binding การไม่มี records ไม่ใช่หลักฐานว่าคำตอบทุกข้อในหมวดนั้นหาย และ live runtime อาจมาจาก adapter/config

## ตัวอย่างการใช้งานร่วมกัน

เกมใหม่ → game + game_service + service/resource ที่มีอยู่; เพิ่ม game_mode/control_set ตามข้อมูลจริง  
ราคาใหม่ → rate เดิมหรือ versioned rate ตามช่วงมีผล + audience/service ที่ถูกต้อง  
กฎใหม่ → competition edition + ordered competition_rule + depends_on_ids  
เครื่องใหม่ → resource + zone/equipment_model + service + live mapping ที่ตรวจได้

## center

**งานที่ต้องรองรับ:** ข้อมูลศูนย์/เจ้าของ/ที่อยู่/แผนที่

**Readiness ต่อคำถาม:** overview ใช้ description/operator; directions ต้อง address/building/floor/map ตามสิ่งที่ถาม

**ข้อระวังเฉพาะหมวด:** ไม่ต้องบังคับมีทุกช่องเพื่อบอกชื่อศูนย์ แต่ห้ามแต่งตำแหน่งที่ไม่ได้กรอก

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `name` | ชื่อศูนย์อย่างเป็นทางการ | ใช่ | — |
| `operator` | หน่วยงานเจ้าของ/ผู้ดำเนินการ | ใช่ | — |
| `description` | ศูนย์ทำอะไร/ขอบเขตบริการ | ไม่ | — |
| `address` | ที่อยู่เต็ม | ไม่ | — |
| `building` | อาคาร | ไม่ | — |
| `floor` | ชั้น | ไม่ | — |
| `map_url` | ลิงก์แผนที่ | ไม่ | — |
| `timezone` | เขตเวลา | ใช่ | — |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## contact

**งานที่ต้องรองรับ:** ติดต่อเรื่องใด/ทางไหน/เมื่อใด

**Readiness ต่อคำถาม:** purpose + channel/value; office_hours เมื่อถามช่วงตอบ

**ข้อระวังเฉพาะหมวด:** เก็บเป็นช่องติดต่อสาธารณะ ไม่ดึง private contact มาแทน

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `name` | ชื่อที่แสดงให้ผู้ใช้เห็น | ไม่ | — |
| `channel` | ประเภทช่องทาง | ใช่ | — |
| `value` | URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย | ใช่ | — |
| `purpose` | ติดต่อเรื่องอะไรได้บ้าง | ใช่ | — |
| `office_hours` | เวลาตอบของช่องทางนี้ | ไม่ | — |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## facility

**งานที่ต้องรองรับ:** ที่จอดรถ/ที่พัก/สิ่งอำนวยความสะดวก

**Readiness ต่อคำถาม:** name/location; usage_conditions/accessibility ตาม need

**ข้อระวังเฉพาะหมวด:** การมีที่จอดรถไม่ยืนยันค่าจอดหรือ accessibility ถ้าไม่ได้ระบุ

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `name` | เช่น ที่จอดรถ/ที่นั่งพัก | ใช่ | — |
| `location` | อยู่บริเวณไหน | ใช่ | — |
| `usage_conditions` | เงื่อนไขใช้บริการ | ไม่ | — |
| `accessibility` | การเข้าถึง/รถเข็น หากยังไม่มีข้อมูลให้ unknown | ไม่ | — |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## zone

**งานที่ต้องรองรับ:** หมวดพื้นที่/รายการในโซน/ตำแหน่ง

**Readiness ต่อคำถาม:** name/description/location และ reverse refs จาก resource/rental

**ข้อระวังเฉพาะหมวด:** room_seats ไม่ใช่จำนวนผู้เล่นพร้อมกัน

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `name` | PC/PS5/Switch/Cockpit/VR เป็นชื่อรายการ | ใช่ | — |
| `description` | โซนนี้ใช้ทำอะไร | ไม่ | — |
| `location` | ตำแหน่งในศูนย์ | ไม่ | — |
| `room_seats` | จำนวนที่นั่งในพื้นที่ ไม่ใช่จำนวนคนเล่นพร้อมกัน | ไม่ | — |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## equipment_model

**งานที่ต้องรองรับ:** รุ่น/สเปก/อุปกรณ์ที่ใช้

**Readiness ต่อคำถาม:** name/device_type/specifications/usage + resource references

**ข้อระวังเฉพาะหมวด:** อุปกรณ์ส่วนตัวกับอุปกรณ์ศูนย์เป็นคนละ policy

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `name` | ชื่อรุ่นอุปกรณ์ | ใช่ | — |
| `device_type` | ประเภทอุปกรณ์ | ใช่ | — |
| `specifications` | สเปกทีละค่า พร้อมหน่วย/รุ่น | ไม่ | — |
| `usage` | วิธีใช้อุปกรณ์/ข้อควรทราบจากแหล่งข้อมูล | ไม่ | — |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## resource

**งานที่ต้องรองรับ:** เครื่องรายตัว/จำนวนเครื่อง/ความสัมพันธ์

**Readiness ต่อคำถาม:** zone_id + equipment_model_ids + operational_status + physical_pool_key

**ข้อระวังเฉพาะหมวด:** operational_status ไม่ใช่ live booking occupancy

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `name` | ชื่อเครื่อง เช่น PC #01 | ใช่ | — |
| `zone_id` | โซนที่เครื่องตั้งอยู่ | ใช่ | zone |
| `equipment_model_ids` | รุ่นอุปกรณ์ที่ประกอบในเครื่องนี้ | ไม่ | equipment_model |
| `capacity_persons` | จำนวนคนเล่นพร้อมกันของเครื่อง ไม่ใช่ห้อง | ไม่ | — |
| `physical_pool_key` | รหัสทรัพยากรร่วม เช่น VR 30/60 นาทีใช้เครื่องเดียวกัน | ใช่ | — |
| `operational_status` | พร้อมให้บริการทางกายภาพ ไม่ใช่สถานะจอง | ใช่ | — |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## service

**งานที่ต้องรองรับ:** บริการ/รอบเล่น/ความจุ/ขอบเขตจอง

**Readiness ต่อคำถาม:** resource_ids/platform/session_minutes/occupancy_minutes; capacity ตามคำถาม

**ข้อระวังเฉพาะหมวด:** เวลาเล่นกับเวลาที่กินช่องจองไม่ใช่ค่าเดียวกันเสมอ

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `name` | ชื่อบริการตามหน้า WordPress | ใช่ | — |
| `resource_ids` | เครื่องจริงที่บริการใช้ | ใช่ | resource |
| `platform` | แพลตฟอร์มของบริการ | ใช่ | — |
| `session_minutes` | ระยะเวลาเล่นของบริการ | ใช่ | — |
| `occupancy_minutes` | เวลาที่กันทรัพยากร เช่น VR 30 นาทีอาจกัน 60 | ใช่ | — |
| `capacity_min` | ผู้เล่นขั้นต่ำ | ไม่ | — |
| `capacity_max` | ผู้เล่นสูงสุดตามบริการ | ไม่ | — |
| `booking_product_key` | รหัสผลิตภัณฑ์/API จาก WordPress ไม่ใช่เดาจากชื่อ | ไม่ | — |
| `notes` | หมายเหตุของบริการ | ไม่ | — |
| `inventory_verified_on` | วันที่รายการเกมและเครื่องถูกตรวจตามต้นฉบับ ไม่ใช่สถานะจองสด | ไม่ | — |
| `inventory_basis` | หลักฐานของรายการเกมและเครื่องตามต้นฉบับ | ไม่ | — |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## game

**งานที่ต้องรองรับ:** ภาพรวม/แนว/วิธีเล่น/คำบรรยาย

**Readiness ต่อคำถาม:** summary/genre สำหรับ overview; how_to_play สำหรับวิธีเล่น; edition เมื่อแยกรุ่น

**ข้อระวังเฉพาะหมวด:** supported_platforms ไม่ยืนยันว่าศูนย์มีเกม; ไม่สร้าง task profile รายชื่อเกม

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `title` | ชื่อเกมอย่างเป็นทางการ | ใช่ | — |
| `edition` | ภาค/edition ให้ตรง หากต้นทางไม่มีให้ unknown | ไม่ | — |
| `genre` | แนวเกม | ไม่ | — |
| `summary` | เกมเกี่ยวกับอะไร | ไม่ | — |
| `how_to_play` | เป้าหมาย/วงจรการเล่นโดยสรุป | ไม่ | — |
| `publisher_url` | แหล่งจากผู้พัฒนาเกม | ไม่ | — |
| `supported_platforms` | แพลตฟอร์มที่ตัวเกมรองรับ ไม่แปลว่าศูนย์มีให้เล่น | ไม่ | — |
| `age_rating` | เรตเกมจากต้นทาง ไม่ใช่นโยบายรับเด็กของศูนย์ | ไม่ | — |
| `official_description` | คำบรรยายจากหน้าเกมต้นฉบับ | ไม่ | — |
| `profile_role` | บทบาทของรายการข้อมูล (ไม่ใช่สถานะให้บริการ) | ไม่ | — |
| `source_listing_sections` | หมวดที่ระบุในหน้าเกมต้นฉบับ (ไม่ใช่สถานะติดตั้งสด) | ไม่ | — |
| `venue_zone_ids` | โซนที่ระบุในข้อมูลเกมของศูนย์ (ไม่ใช่ทุกแพลตฟอร์มที่เกมรองรับ) | ไม่ | zone |
| `description_captured_at` | เวลาที่เก็บคำบรรยายต้นฉบับ ไม่ใช่วันอัปเดตเกม | ไม่ | — |
| `description_scope_note` | ขอบเขตคำบรรยายจากต้นฉบับ | ไม่ | — |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## game_service

**งานที่ต้องรองรับ:** เกมอยู่บริการใด/มีติดตั้งที่เครื่องไหน

**Readiness ต่อคำถาม:** game_id/service_id/offered; installed_resource_ids เมื่อถามการติดตั้ง

**ข้อระวังเฉพาะหมวด:** offered=true ไม่ยืนยันว่าทุกเครื่องว่างหรือติดตั้งล่าสุด

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `game_id` | เลือกเกมจากทะเบียนเกม | ใช่ | game |
| `service_id` | เลือกบริการจากทะเบียนการจอง | ใช่ | service |
| `offered` | ศูนย์ยืนยันมี/ไม่มีเกมนี้ในบริการนี้ | ใช่ | — |
| `installed_resource_ids` | ถ้ายืนยันเฉพาะเครื่อง ให้ระบุเครื่อง ห้ามอนุมานทั้งโซน | ไม่ | resource |
| `game_version` | เวอร์ชันเกมที่ติดตั้ง ถ้าไม่ทราบให้ unknown | ไม่ | — |
| `account_policy_id` | นโยบายบัญชีของศูนย์ | ไม่ | policy |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## game_mode

**งานที่ต้องรองรับ:** เล่นกี่คน/โหมดไหน/ออนไลน์ไหม

**Readiness ต่อคำถาม:** mode_name/platform/players_min/players_max/network_requirement/studio_supported

**ข้อระวังเฉพาะหมวด:** schema มีหมวดนี้แต่ R88 inventory ไม่มี records; ห้ามรับรองความพร้อมจริงจาก schema

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `game_id` | เกมที่อ้างถึง | ใช่ | game |
| `mode_name` | เช่น local co-op/online multiplayer | ใช่ | — |
| `platform` | แพลตฟอร์มของโหมดนี้ | ใช่ | — |
| `players_min` | จำนวนผู้เล่นขั้นต่ำของโหมด | ไม่ | — |
| `players_max` | สูงสุดของโหมดเกม ไม่ใช่ความจุบริการ | ไม่ | — |
| `network_requirement` | ออนไลน์/อินเทอร์เน็ต/บัญชีที่ต้องใช้ | ไม่ | — |
| `studio_supported` | ศูนย์รองรับโหมดนี้จริงหรือยังไม่ยืนยัน | ไม่ | — |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## control_set

**งานที่ต้องรองรับ:** ปุ่ม action/ปุ่มทั้งหมด/อุปกรณ์ควบคุม

**Readiness ต่อคำถาม:** game_id/platform/input_device/preset/bindings; limitations/coverage/verification

**ข้อระวังเฉพาะหมวด:** all ต้องมี cardinality และแจ้ง source partial; ปุ่มอาจยังไม่ตรวจบนอุปกรณ์จริง

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `game_id` | เกม/edition ที่ตรงกัน | ใช่ | game |
| `platform` | PC/PS5/Nintendo Switch/VR | ใช่ | — |
| `input_device` | ชนิดอุปกรณ์ควบคุม | ใช่ | — |
| `preset` | default/custom profile ชื่อชุดปุ่ม | ใช่ | — |
| `game_version` | เวอร์ชันที่ตรวจชุดปุ่มนี้ | ไม่ | — |
| `bindings` | ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record | ใช่ | — |
| `limitations` | ข้อจำกัดหรือปุ่มที่ยังไม่ยืนยัน | ไม่ | — |
| `source_summary` | ภาพรวมชุดปุ่มตามต้นฉบับ | ไม่ | — |
| `verification_note` | ข้อจำกัดการตรวจชุดปุ่มจากต้นฉบับ | ไม่ | — |
| `source_coverage` | สถานะความครบของผังปุ่มตามต้นฉบับ | ไม่ | — |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## audience

**งานที่ต้องรองรับ:** กลุ่มผู้ใช้/สิทธิ์/หลักฐาน

**Readiness ต่อคำถาม:** name/eligibility/required_proofs; เชื่อม rate/package

**ข้อระวังเฉพาะหมวด:** นักศึกษาทั่วไปกับ PSU ห้ามรวมกลุ่มด้วยคำว่า student อย่างเดียว

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `name` | ชื่อกลุ่ม เช่น บุคคลทั่วไป/หน่วยงานภายนอก | ใช่ | — |
| `eligibility` | ใครอยู่ในกลุ่มนี้ ตามนโยบายจริง | ใช่ | — |
| `required_proofs` | หลักฐานสิทธิ์ หากไม่มีข้อมูลให้ unknown | ไม่ | — |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## rate

**งานที่ต้องรองรับ:** ราคาต่อหน่วย/รวมเวลา/งบประมาณ

**Readiness ต่อคำถาม:** service_id/audience_id/amount_minor/currency/unit/duration/calculation_rule + validity

**ข้อระวังเฉพาะหมวด:** current price ต้องตรวจช่วงมีผล; ห้ามใช้ expired เป็นปัจจุบัน

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `service_id` | บริการตามระบบจอง | ใช่ | service |
| `audience_id` | กลุ่มผู้ใช้ | ใช่ | audience |
| `amount_minor` | จำนวนสตางค์: 70 บาท = 7000; 0 คือฟรีเมื่อยืนยันจริง | ใช่ | — |
| `currency` | สกุลเงิน | ใช่ | — |
| `unit` | คิดต่ออะไร | ใช่ | — |
| `duration_minutes` | ช่วงเวลาที่ราคานี้ครอบคลุม | ใช่ | — |
| `persons_min` | ช่วงผู้ใช้ขั้นต่ำ | ไม่ | — |
| `persons_max` | ช่วงผู้ใช้สูงสุด | ไม่ | — |
| `calculation_rule` | อนุญาตคูณเวลาได้หรือคิดตายตัว ต้องมีหลักฐาน | ใช่ | — |
| `tax_note` | ภาษี/เงื่อนไข ถ้ายังไม่ระบุห้ามคิดรวมเอง | ไม่ | — |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## rental_package

**งานที่ต้องรองรับ:** ราคาเหมา/ครึ่งวัน/เต็มวัน/รวมอุปกรณ์

**Readiness ต่อคำถาม:** zone_ids/audience_id/period_label/amount_minor/currency; terms/duration เมื่อถาม

**ข้อระวังเฉพาะหมวด:** label เต็มวันไม่ใช่จำนวนชั่วโมงที่อนุมานได้

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `name` | ชื่อแพ็กเกจ | ใช่ | — |
| `zone_ids` | โซนที่รวมในแพ็กเกจ | ใช่ | zone |
| `audience_id` | หน่วยงานภายใน/ภายนอก ไม่ใช่กลุ่มราคาบุคคล | ใช่ | audience |
| `period_label` | ครึ่งวัน/เต็มวันเป็นชื่อแพ็กเกจ | ใช่ | — |
| `duration_minutes` | จำนวนจริงของนาที ต้องรอยืนยัน ไม่เดาว่า 4/8 ชั่วโมง | ไม่ | — |
| `amount_minor` | ราคาเป็นสตางค์ | ใช่ | — |
| `currency` | สกุลเงิน | ใช่ | — |
| `equipment_included` | จำนวนเครื่อง/อุปกรณ์ที่รวม | ไม่ | — |
| `room_seats` | จำนวนที่นั่งพื้นที่ตามชีต ไม่ใช่ผู้เล่นเครื่อง | ไม่ | — |
| `terms` | เช่น ค่าเจ้าหน้าที่นอกเวลา | ไม่ | — |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## schedule

**งานที่ต้องรองรับ:** วันเปิด/ช่วงเปิด/ช่วงจอง/Maintenance

**Readiness ต่อคำถาม:** timezone/zone_ids/weekday/open_periods/bookable_periods/maintenance_periods

**ข้อระวังเฉพาะหมวด:** แยก open กับ bookable; closure ที่มีผลมาก่อน weekly schedule

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `timezone` | เขตเวลา | ใช่ | — |
| `zone_ids` | ขอบเขตโซน; [] ที่ known หมายถึงทุกโซนตามประกาศ | ใช่ | zone |
| `weekday` | ISO weekday ในสเปกนี้ 0=จันทร์ ต้องแปลงจากต้นทางชัดเจน | ใช่ | — |
| `open_periods` | ช่วงเปิดพื้นที่ | ใช่ | — |
| `bookable_periods` | ช่วงที่จอง/เล่นได้ แยกจากเปิดพื้นที่ | ใช่ | — |
| `maintenance_periods` | ช่วง maintenance | ไม่ | — |
| `reason` | เหตุผล/ประกาศของตาราง | ไม่ | — |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## closure

**งานที่ต้องรองรับ:** วันปิดพิเศษ/เปลี่ยนเวลาบริการ

**Readiness ต่อคำถาม:** local_date/zone_ids/state/reason และช่วงเวลาที่ override

**ข้อระวังเฉพาะหมวด:** ถ้าถามจัดการรายการจองหลังปิดพิเศษต้องมี resolution policy ไม่เดาจาก state

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `local_date` | วันที่ ISO ค.ศ. ตามเวลาไทย | ใช่ | — |
| `zone_ids` | โซนที่ได้รับผล; [] = ทุกโซนเมื่อยืนยัน | ใช่ | zone |
| `state` | ประเภทข้อยกเว้น | ใช่ | — |
| `open_periods` | เวลาใหม่ กรณี modified/open override | ไม่ | — |
| `bookable_periods` | เวลาที่จองได้ในวันที่ยกเว้น | ไม่ | — |
| `reason` | เหตุผลปิด/เปิดพิเศษ | ใช่ | — |
| `resolution_policy_id` | นโยบายจัดการรายการจองเดิม หากไม่มีให้ unknown | ไม่ | policy |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## policy

**งานที่ต้องรองรับ:** อนุญาตไหม/เงื่อนไข/ข้อยกเว้น/ผลตามมา

**Readiness ต่อคำถาม:** topic/subject/decision/conditions_all/details + exceptions/consequence ตาม need

**ข้อระวังเฉพาะหมวด:** ต้อง preserve action/object/context/polarity; unknown ไม่ใช่ denied

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `topic` | หัวข้อเชิงความหมาย เช่น personal_peripherals | ใช่ | — |
| `subject` | สิ่งที่กฎใช้กับ เช่น คีย์บอร์ด/เมาส์ส่วนตัว | ใช่ | — |
| `decision` | อนุญาต/ห้าม/จำเป็น/มีเงื่อนไข | ใช่ | — |
| `conditions_all` | เงื่อนไขที่ต้องครบ เช่น booking_paid=true; ไม่มีเงื่อนไขต้องยืนยันจริง | ใช่ | — |
| `exceptions` | ข้อยกเว้น หากต้นทางไม่ได้ระบุให้ unknown | ไม่ | — |
| `consequence` | ผลเมื่อผิดกฎ/ค่าปรับ ห้ามเติมเอง | ไม่ | — |
| `details` | ข้อความกฎพร้อมเงื่อนไขจากต้นทาง | ใช่ | — |
| `procedure_id` | ขั้นตอนปฏิบัติที่เกี่ยวข้อง | ไม่ | procedure |
| `query_profile` | ช่วยเลือกคำตอบ: ประเภทคำถาม เรื่อง และขอบเขต | ไม่ | — |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## procedure

**งานที่ต้องรองรับ:** ทำอย่างไร/ต้องเตรียมอะไร/กำหนดเวลา

**Readiness ต่อคำถาม:** topic/preconditions/steps; required_documents/deadline/outcome ตาม need

**ข้อระวังเฉพาะหมวด:** ตอบตามลำดับจริง ไม่เอาขั้นตอนชำระเงินไปแทนการแก้ข้อมูลจอง

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `name` | ชื่อที่แสดงให้ผู้ใช้เห็น | ไม่ | — |
| `topic` | เรื่องที่ขั้นตอนนี้ใช้กับ | ใช่ | — |
| `preconditions` | สถานการณ์ก่อนทำ เช่น จองผิดเครื่อง | ใช่ | — |
| `steps` | ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production | ใช่ | — |
| `required_documents` | หลักฐาน/รายการที่ต้องเตรียม | ไม่ | — |
| `deadline_minutes` | กำหนดเวลา ถ้าไม่ทราบอย่าเติม | ไม่ | — |
| `outcome` | หลังทำแล้วได้อะไร ขอบเขตสิ่งที่ยืนยัน | ไม่ | — |
| `query_profile` | ช่วยเลือกคำตอบ: ประเภทคำถาม เรื่อง และขอบเขต | ไม่ | — |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## competition

**งานที่ต้องรองรับ:** รายการแข่ง/ปี/เล่ม/ขอบเขตกติกา

**Readiness ต่อคำถาม:** game_id/event_name/rulebook_release/coverage + competition_rule children

**ข้อระวังเฉพาะหมวด:** supersedes ไม่ลบการถามเล่มเก่า แต่ห้ามถือเล่มเก่าใช้กับปีใหม่โดยไม่มีหลักฐาน

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `game_id` | เกมที่แข่งขัน | ใช่ | game |
| `event_name` | ชื่อรายการ+ปี+ประเภทให้ตรง | ใช่ | — |
| `division` | เช่น ทีมชาย/ทีมผสม ถ้าไม่ระบุให้ unknown | ไม่ | — |
| `rulebook_release` | ฉบับและเวอร์ชันกติกา | ใช่ | — |
| `competition_dates` | วันที่การแข่งขันจากต้นทาง | ไม่ | — |
| `coverage` | ความครบของเอกสาร ตรวจจากสารบัญและต้นทาง ไม่ใช่มี JSON แล้วครบ | ใช่ | — |
| `supersedes_id` | ฉบับก่อนหน้าถ้าทราบ | ไม่ | competition |
| `source_title` | ชื่อหัวเอกสารต้นฉบับ | ไม่ | — |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## competition_rule

**งานที่ต้องรองรับ:** กฎเฉพาะข้อ/ทั้งหมด/บทลงโทษ

**Readiness ต่อคำถาม:** competition_id/section_number/facet/heading/text/completeness + dependencies/order

**ข้อระวังเฉพาะหมวด:** แม้ heading ตรง ต้องรวม condition/exception/penalty ที่ผูกกัน

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `competition_id` | ฉบับรายการที่กฎเป็นของมัน | ใช่ | competition |
| `section_number` | เลขข้อเดิม เช่น 6.1.5 | ใช่ | — |
| `facet` | หมวดกฎ | ใช่ | — |
| `heading` | หัวข้อข้อกติกา | ใช่ | — |
| `text` | ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ | ใช่ | — |
| `depends_on_ids` | ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม | ไม่ | competition_rule |
| `completeness` | สถานะความสมบูรณ์ของข้อนี้ | ใช่ | — |
| `facets` | หัวข้อย่อยที่ข้อความส่วนนี้รองรับ (จัดหมวดจากต้นฉบับ) | ไม่ | — |
| `source_order` | ลำดับข้อความในเอกสารต้นฉบับ | ไม่ | — |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## news

**งานที่ต้องรองรับ:** ข่าว/กิจกรรม/ลงทะเบียน/ช่วงจัด

**Readiness ต่อคำถาม:** title/body/event_start/event_end/audience/contact/URL

**ข้อระวังเฉพาะหมวด:** R88 inventory ไม่มี records หมวดนี้; ข่าวไม่ override policy ถาวรโดยอัตโนมัติ

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `title` | หัวข้อประกาศ | ใช่ | — |
| `body` | รายละเอียด | ใช่ | — |
| `event_start` | เวลาเริ่มกิจกรรม | ไม่ | — |
| `event_end` | เวลาจบกิจกรรม | ไม่ | — |
| `audience_ids` | ผู้เข้าร่วม/กลุ่มสิทธิ์ | ไม่ | audience |
| `contact_id` | ช่องทางเกี่ยวกับกิจกรรม | ไม่ | contact |
| `registration_url` | ลิงก์สมัคร ถ้ามี | ไม่ | — |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## person

**งานที่ต้องรองรับ:** บุคลากร/หน้าที่/ทีม/ติดต่อสาธารณะ

**Readiness ต่อคำถาม:** display_name/role/team/affiliation/period/public_scope

**ข้อระวังเฉพาะหมวด:** แสดงข้อมูลเฉพาะที่ public_scope อนุญาต

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `display_name` | ชื่อที่อนุญาตให้เผยแพร่ | ใช่ | — |
| `role` | ตำแหน่ง/หน้าที่ | ใช่ | — |
| `team` | ทีม/หน่วยงาน | ไม่ | — |
| `public_contact_id` | ช่องทางงานที่อนุญาตเผยแพร่ | ไม่ | contact |
| `public_scope` | รายละเอียดที่เผยแพร่ได้ ไม่ใส่ข้อมูลลูกค้าหรือสลิป | ใช่ | — |
| `affiliation` | สังกัดตามต้นฉบับ | ไม่ | — |
| `period` | วาระหรือช่วงเวลาตามต้นฉบับ | ไม่ | — |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## faq

**งานที่ต้องรองรับ:** คำตอบข้อสงสัยที่เป็นข้อความ

**Readiness ต่อคำถาม:** question/topic/query_profile ช่วยค้น; answer เป็นเนื้อหาคำตอบ; related_ids ช่วย scope

**ข้อระวังเฉพาะหมวด:** ไม่ให้ owner กรอกทุก paraphrase; FAQ ที่ขัด typed policy ต้องตรวจ authority

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `question` | คำถามตั้งต้น ไม่จำเป็นต้องเก็บทุก paraphrase | ใช่ | — |
| `answer` | คำตอบพร้อมหลักฐานของศูนย์ | ใช่ | — |
| `related_ids` | รายการที่เกี่ยวข้อง หากใช้ต้อง resolve ข้าม kind | ไม่ | * |
| `topic` | หัวข้อเชิงความหมาย | ใช่ | — |
| `scope_note` | ขอบเขตและข้อจำกัด ไม่ใช้ FAQ override ราคาหรือสถานะสด | ไม่ | — |
| `intent_key` | หัวข้อเชิงความหมายของคำถาม (ข้อมูลจัดหมวดจากต้นฉบับ) | ไม่ | — |
| `source_variants` | ข้อความต้นทางที่แตกต่างกันและยังไม่เลือกเป็นนโยบายเดียว | ไม่ | — |
| `query_profile` | ช่วยเลือกคำตอบ: ประเภทคำถาม เรื่อง และขอบเขต | ไม่ | — |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## live_binding

**งานที่ต้องรองรับ:** ผูกบริการกับ provider สถานะสด

**Readiness ต่อคำถาม:** service_id/provider/external_resource_key/physical_pool_key/status_mapping/timezone/freshness_policy

**ข้อระวังเฉพาะหมวด:** R88 inventory ไม่มี records หมวดนี้ ไม่ได้แปลว่าไม่มี live adapter: runtime มี config ภายนอก ต้อง reconcile ตอน cutover

| Field ปัจจุบัน | ความหมายที่ฟอร์มควรสื่อ | publish_core | อ้างอิงหมวด |
|---|---|---|---|
| `service_id` | บริการของศูนย์ | ใช่ | service |
| `provider` | ผู้ให้ข้อมูลสด | ใช่ | — |
| `external_resource_key` | รหัสที่ API ใช้จริง | ใช่ | — |
| `physical_pool_key` | ทรัพยากรร่วม ต้องตรง resource ที่ service ใช้ | ใช่ | — |
| `status_mapping` | ความหมายสถานะจาก API ต้องมี fixture ที่รู้ผล | ใช่ | — |
| `timezone` | เขตเวลาของการแปลงข้อมูล | ใช่ | — |
| `freshness_policy` | นโยบาย cache/TTL ที่อนุมัติ | ใช่ | — |

**เมื่อเพิ่ม/แก้:** เก็บ revision และ source ใหม่ ตรวจ references/ช่วงมีผล สร้าง names/text/reverse-reference indexes ใหม่ตาม release และ invalidate plan/evidence cache ที่เกี่ยว ไม่เพิ่ม handler รายชื่อรายการ

## ช่องว่าง schema/ข้อมูลที่ต้องสำรวจระหว่างทำ

1. equipment relations บางเส้นทางอาศัย source grouping: เมื่อไม่มี explicit resource reference ต้องแยก inferred mapping ออกจาก confirmed reference
2. query_profile มีอยู่บาง kinds แต่ task registry/need ledger ร่วมยังเป็นงานออกแบบ ไม่ให้ owner ต้องสร้าง profile ทางเทคนิคเอง
3. วันที่มีผลและ future release ต้องตรวจความสามารถ store จริง; ไม่ออกแบบฟอร์มที่บอกว่าจะสลับอัตโนมัติทั้งที่ยังไม่มี scheduler
4. derived readiness/index/cache ต้องผูก schema_version และ release epoch เพื่อไม่ใช้ field contract เก่ากับข้อมูลรูปใหม่
5. หากสร้าง schema ใหม่ ต้องมี migration/version/read executor/renderer/validation มากกว่าการเพิ่มชื่อ kind ใน dropdown

