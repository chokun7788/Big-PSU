# R119 การวิเคราะห์สาเหตุและปัญหาที่ยังพบหลังย้ายข้อมูล

## สรุปที่ควรใช้ตัดสินงาน

การตรวจพบทั้ง **ข้อมูล/ความสัมพันธ์/ชื่อเรียกที่ย้ายตกหล่นจริง** และ **ค่าที่อยู่ใน native แล้วแต่ขั้นตีความหรือ reader ใช้ไม่ถูก** รอบนี้ซ่อมกลุ่มแรกและ reader บางส่วน พร้อมเก็บหลักฐานรายข้อ ไม่ถือว่าคะแนน positive 62/62 เป็นหลักฐานว่า Flow สมบูรณ์

ไฟล์กติกา Word ต้นฉบับทั้ง 4 เอกสารตรวจแล้ว ข้อความ body/table paragraphs 373/373 ย่อหน้ามีใน native rule text การตอบบทลงโทษไม่ครบจึงไม่ควรแก้ด้วยการขอให้เจ้าของส่งเอกสารเดิมหรือเพิ่มข้อความเดิมซ้ำ

## 1 แยกคำว่า ข้อมูลครบ ออกเป็นอะไรบ้าง

| ชั้น | สิ่งที่ตรวจ | สิ่งที่ยังสรุปแทนไม่ได้ |
|---|---|---|
| ต้นฉบับ | ไฟล์/record/JSON leaves และ primary Word/Excel | ยังไม่บอกว่า parser เข้าใจชนิดข้อมูลถูกทุกค่า |
| Representation | typed fields, aliases, relations, provenance, status | ยังไม่บอกว่าทุก reader ถูกเรียกเมื่อควรเรียก |
| Retrieval/reader | compile/index/bind/facet/operator | ยังไม่บอกว่า LLM เก็บเงื่อนไขของคำถามครบ |
| คำตอบ | selected source, เงื่อนไข, ความครบของข้อที่ถาม | keyword pass หรือ JSON schema pass เพียงอย่างเดียวรับรองไม่ได้ |

`legacy_context` และ compressed archives ใช้ตรวจว่าไม่ทิ้งต้นฉบับ ไม่ได้เอา raw JSON มาเป็นทางลัดตอบทุกอย่าง ส่วน 1,875 typed-value checks และ 743 source/operator/alias contracts ตรวจการแปลงและการเข้าถึงที่ระบุไว้ต่างหาก

## 2 ปัญหาการย้ายที่แก้แล้ว

### 2.1 มี facts.zones แต่บังคับผ่านเครื่องจริง

**หลักฐานเดิม:** game profiles ของ New Super Mario Bros. U Deluxe และ Little Nightmares II มี `facts.zones: Nintendo Switch Zone` อยู่แล้ว ขณะที่ service บางรายการไม่มี machine_numbers

**สิ่งที่ผิด:** migration/reader เดิมใช้ game → service → resource → zone เท่านั้น จึงตีว่าไม่มีความสัมพันธ์ถึงโซน ทั้งที่มี direct zone ในต้นฉบับ

**การแก้:** ย้าย direct game/service zone IDs และอ่านทั้ง direct relation กับ resource chain โดยตรวจ FK และแหล่งอ้างอิง ไม่สร้าง resource ID ขึ้นเอง

**ผลที่ตรวจ:** คำถามเดิมทั้งสองข้อตอบ Nintendo Switch Zone ผ่าน API ล่าสุด นี่เป็น representation/reader omission ที่แก้ได้จากต้นฉบับที่มีอยู่

### 2.2 โปรไฟล์ published ถูก public_scope unknown บล็อก

**หลักฐานเดิม:** โปรไฟล์บุคลากร 25 คนระบุ lifecycle published และ official source URL แต่ public_scope ของ native ไม่เคยถ่ายมา

**การแก้:** ย้ายขอบเขตของข้อมูลสาธารณะที่บันทึกไว้ ใช้ข้อความกำกับว่าตอบตามโปรไฟล์ต้นทาง ไม่รับรอง current tenure ไม่ขยายไปยังเงินเดือน/ข้อมูลส่วนตัว และไม่สร้าง approval

**ผลที่ตรวจ:** ตำแหน่ง → คน และชื่ออังกฤษที่สะกดใกล้กับ source alias จับคู่ได้ เมื่อถอน public scope ในการตรวจแบบ in-memory คำถามเดิมถูกบล็อกตามเดิม

### 2.3 สูตรปัดรอบอยู่ใน calculator เดิม แต่ไม่มีใน native

**หลักฐานเดิม:** โค้ดราคาใช้ `math.ceil(duration/session)` ส่วน native 18 จาก 24 rates ไม่มีกฎคำนวณ

**การแก้:** ถ่าย `session_ceil` เฉพาะ service/group/amount/duration ที่ตรงกัน รักษาหน่วย/ข้อยืนยันเจ้าของที่ใหม่กว่าไว้

**ผลที่ตรวจ:** PS5 2 ชั่วโมงอ่านกฎจาก native คิดตามรอบได้ ไม่ต้องสร้างราคาใหม่หรือใช้ FAQ ราคาเก่าหลบการตรวจ rate

### 2.4 ปะปนเวลาเปิดพื้นที่กับเวลาที่เปิดให้เล่น

**หลักฐานเดิม:** regular_service_slots มีสถานะ open/maintenance แยกวันครบ แต่บาง open_periods ใน native ขัดกัน

**การแก้:** ถ่าย play-service slots ทั้งเจ็ดวันแยกจาก physical hours แล้วใช้ calendar reader ที่ระบุขอบเขตชัดเจน ไม่ล้าง conflict ของข้อมูลอีกชนิดหนึ่งทิ้ง

**ผลที่ตรวจ:** จันทร์เช้าและศุกร์บ่ายตอบไม่เปิดให้เล่นเพราะ maintenance จากตาราง ส่วน “ตอนนี้” ใช้ clock ของ test ซึ่งตรึงไว้ให้เทียบกับ R118 ได้ ไม่ใช่คำประกาศสถานะจริง ณ เวลาที่อ่านรายงาน

### 2.5 aliases ของอุปกรณ์ยังอยู่ใน code cache

**หลักฐานเดิม:** EQUIPMENT_ITEM_DETAILS มีคำว่า เมาส์/เม้า/เม้าส์ แต่ต้นฉบับ canonical บางรายการมี aliases อังกฤษเป็นหลัก

**การแก้รอบท้าย:** ย้าย search aliases เพิ่ม 128 รายการ ได้แก่ อุปกรณ์ 91, โซน 24 และเกม 13 โดยจับคู่กับ entity ที่มีอยู่ ไม่ย้ายข้อความคำตอบ cache มาทับ facts ไม่สร้าง Minecraft เป็นเกมที่ให้บริการ และไม่เติมอีก 12 aliases ที่ชนกับ entity อื่น

**ผลที่ตรวจ:** คำถามเดิม “มีเมาส์เกใมิ่งให้ไหม” จากเดิมตอบไม่มีข้อมูล เปลี่ยนเป็นอ่าน Gaming Mouse และการใช้งานจาก native ได้แล้ว ไม่ต้องถามเจ้าของใหม่ว่าเมาส์มีจริงหรือไม่

### 2.6 กฎค้นหากว้างแย่งช่องตรงคำถาม

**หลักฐานจาก HTTP revision01:** ถาม Gaming Chair อยู่โซนไหน ได้รายการอุปกรณ์ PC ทั้งโซน พร้อม subject ที่เป็น regex

**การแก้ revision02:** typed field/relation และ locked guard ทำงานก่อน query-profile fallback พร้อมซ่อน pattern-only titles จากข้อความที่ลูกค้าเห็น

**ผลที่ตรวจ:** API ล่าสุดตอบ `Gaming Chair — location: PC Zone` ไม่ใช่รายการอุปกรณ์ทั้งห้อง

### 2.7 มี native field แล้ว แต่ยังไม่ compile ให้ reader

ต่อ person.affiliation/period, game.official_description และ service_capacity เข้าการฉาย facts พร้อมขอบเขตของแต่ละชนิด:

- คำบรรยาย 31 เกมเป็นข้อความที่เก็บจาก source ณ วันที่ระบุ ไม่รับรอง patch/DLC/entitlement ปัจจุบัน
- service_capacity ของ 8 บริการเป็นช่วงผู้ใช้ตามรายการ ไม่ใช่หลักฐานว่าจำนวนดังกล่าวเล่นพร้อมกันได้
- สังกัด/period ที่ native มีอยู่แล้วคงค่าเดิมและคำแปลไว้ ไม่ลดกลับเป็นข้อความเก่าที่สั้นกว่า

การตรวจส่วนนี้มี source/operator contracts; ไม่ได้สร้าง benchmark questions ใหม่เพื่ออ้างคะแนนเพิ่ม

## 3 ปัญหาที่ผล API ล่าสุดยังยืนยันว่าต้องพัฒนาต่อ

### 3.1 ถามราคา Beat Saber แต่ตอบรายชื่อเกม VR

**คำถามเดิม:** `How much does Beat Saber cost`

**คำตอบล่าสุด:** `VR Station games include Beat Saber and Horizon Call of the Mountain.`

**หลักฐานจากแผน:** ถูกตีเป็น game_detail/C04 และเลือก `declared_legacy_query_profile` ของ `migrated_faq_rule_vr_specific_games`

**ข้อสรุป:** เป็นการตอบคนละ predicate ที่ตรวจยืนยันได้ ไม่ใช่ไม่มีราคาใน native ระบบมี game_service และ rates ของ VR แต่เข้า reader ผิดหมวด

**สิ่งที่ควรแก้ต่อ:**

1. ตรวจ requested operation จากถ้อยคำราคาในคำถามจริง ไม่ใช้เพียง schema-valid task ของโมเดล
2. เมื่อเป้าหมายเป็นเกมและงานคือราคา ให้ผ่าน game_service ไปหา service/rate ที่ยืนยัน
3. ตรวจ audience/session length ที่ยังไม่ทราบ ถาม slot ที่จำเป็นหรือแสดงตัวเลือกโดยไม่เลือกให้เอง
4. query profile ของ game catalogue ต้องไม่ใช้ตอบคำถามราคาเพียงเพราะมีชื่อเกมตรงกัน
5. ใช้คำถามเดิมข้อนี้ตรวจ regression; ไม่ต้องเพิ่มข้อมูลราคาเดิมซ้ำ

### 3.2 “ระงับสิทธิ์ชั่วคราว” ยังตอบเหมือนไม่มีข้อมูล

**คำถามเดิม:** ขอข้อมูลเรื่องระงับสิทธิ์ชั่วคราว

**หลักฐาน API:** C10 ได้ `missing_source / entity_not_bound`

**ข้อมูลที่มีจริง:** `migrated_faq_curated_penalty_temp_suspension` และ `migrated_faq_rule_penalty_temp_suspension` มีข้อความเรื่องละเมิดซ้ำ/รุนแรงและการระงับ 1–7 วัน พร้อมหลักฐานใน native

**ข้อสรุป:** เป็น lookup/subject binding failure และข้อความแสดงผลชวนให้เข้าใจว่าฐานไม่มีข้อมูล ทั้งที่ข้อมูลอยู่แล้ว ไม่ใช่คำตอบที่ต้องให้เจ้าของกรอกใหม่

**สิ่งที่ควรแก้ต่อ:** ตรวจ topic → query profile → หมวด C10 → facet ที่อ่านจริง ให้เข้าถึง canonical decision โดยไม่ต้องระบุ opaque ID; แยกสถานะยังจับเจตนาไม่ได้จากสถานะไม่มี source จริง และรักษาเงื่อนไขละเมิดซ้ำ/รุนแรงกับช่วงโทษไว้ครบ

### 3.3 VR one hour ยังแสดงทั้งอัตรา 30 และ 60 นาที

**คำถามเดิม:** `How much does it cost for an adult to play VR for one hour?`

**คำตอบล่าสุด:** แสดง 525 บาท/30 นาที และ 1,050 บาท/60 นาที แทนที่จะยึดเวลาที่ถามเป็นหลัก

**หลักฐานแผน:** `unbound_or_duplicate_quote`; ใน raw proposal มี task ราคาและ task general ที่ quote ว่าง ทำให้ไม่ยอมรับแผนทั้งชุด จากนั้น fallback ไม่รักษา one hour เป็น duration slot ได้ครบ

**ข้อสรุป:** อัตราที่แสดงไม่ใช่ตัวเลขแต่ง แต่การใช้เงื่อนไขและการโฟกัสคำตอบยังผิด/ไม่ครบ ไม่มีหลักฐานว่าข้อมูลระยะเวลาหรือราคา 60 นาทีหายจากฐาน

**สิ่งที่ควรแก้ต่อ:**

1. ตรวจ empty general task ที่ไม่มี target/constraint แยกจาก factual task โดยไม่ทิ้งเงื่อนไขจริง
2. ให้ parser เวลาภาษาอังกฤษทำงานจากคำถามต้นฉบับได้ แม้แผนโมเดลไม่ผ่าน
3. แยกเวลาที่จะเล่นรวมกับนาทีต่อรอบอย่างชัดเจน
4. ตรวจว่า explicit duration/audience ทุกตัวจากคำถามยังถึง calculator

### 3.4 บริบท AOV หลุดก่อนเข้า reader กติกา

**คำถามเดิม:** `I am preparing for a AOV match. What is the policy for competition equipment and devices`

**หลักฐาน API:** need ที่เข้า C13 เหลือ `what is the policy for competition equipment and devices` และ target/constraints ไม่เก็บ AOV จึงได้ `event_or_rule_not_bound`

**ข้อมูลที่มีจริง:** alias AOV ของเกมอยู่ใน native หลังย้ายรอบท้าย และเอกสาร RoV Blueket Games 2025 อยู่ครบจาก Word ต้นฉบับ

**ข้อสรุป:** ยืนยันได้ว่าบริบทเกมหลุดใน execution query ไม่ใช่เอกสาร RoV หาย ส่วนการถามว่าต้องการกติกาฉบับใดอาจเหมาะสมเมื่อผู้ใช้ไม่ระบุรายการ จึงไม่ควรนับการถามยืนยันทุกกรณีเป็น actual content error

**สิ่งที่ควรแก้ต่อ:** รักษา game/event context ที่ quote จากคำถามต้นฉบับไว้ แม้อยู่ในประโยคเกริ่น หากมีแต่เอกสารปี 2025 ให้บอกขอบเขตนั้นและถามฉบับที่ต้องการ ไม่สมมติว่าเป็นกติกาของรายการใหม่ปีอื่น

### 3.5 ถามบทลงโทษ VALORANT ได้เพียงประโยคพิจารณา intent/impact

**คำตอบล่าสุด:** เจ้าหน้าที่จะพิจารณาโทษตามเจตนาและผลกระทบ

**ข้อมูลที่มีจริง:** native clauses และ Word มีรายละเอียด warning/round rollback/round loss/map forfeit/match forfeit และเงื่อนไขอื่นอยู่ครบ

**ข้อสรุป:** ข้อความที่เลือกจริงมี source รองรับ แต่ยังไม่ครอบคลุมคำถามกว้างเรื่องบทลงโทษ ห้ามตีว่าทุกคำถามกติกาผ่านเพราะได้ citation หนึ่งตัว หรือเพราะทุก section ย้ายครบแล้ว

**สิ่งที่ควรแก้ต่อ:** เลือก clause family ภายใน event/edition เดียวกัน อาศัย facet/heading/parent-child/dependencies ที่ตรวจได้ รวมชนิดโทษและเงื่อนไขที่เกี่ยวข้องตามลำดับต้นฉบับ ถ้าตอบบางส่วนต้องระบุว่าเป็นสรุปบางส่วน ไม่อ้างว่ากติกาครบทั้งหมด

## 4 ข้อจำกัดที่ไม่ควรแก้ด้วยการแต่งข้อมูลเพิ่ม

### 4.1 Physical video กับ in-game capture

เจ้าของให้คำตอบเรื่อง capture ภาพ/วิดีโอในเกม แต่คำถาม `May I record video inside the studio` อาจหมายถึงถ่ายคน/สถานที่ สิทธิ์หนึ่งไม่ได้ยืนยันอีกสิทธิ์ การยังไม่อนุญาตแบบเหมารวมเป็น source-scope guard ที่มีเหตุผล

### 4.2 Part II ที่ไม่ระบุ edition

คำถามรวม The Last of Us Part I / Part II ยังตอบโซน Part I ได้ แต่ไม่ใช้ Part II Remastered แทน Part II โดยอัตโนมัติ แม้ keyword จะผ่านจากส่วน Part I คำตอบยังเป็น partial ต้องเก็บส่วนที่ยังไม่ยืนยันไว้

### 4.3 สถานะเครื่องจริง

คำถาม PC2 ตอน 3pm ใน workload ใช้ provider ที่ควบคุมให้ unavailable ผลนี้ตรวจได้เพียงว่าระบบไม่แต่ง occupancy เมื่อไม่มี provider ไม่ได้ตรวจว่าเครื่องจริงว่างหรือถูกจอง

### 4.4 ข้อมูลรุ่นปัจจุบัน

Published profile, source description และ regular calendar เป็นข้อมูลที่บันทึกไว้ ไม่ใช่หลักฐานอัตโนมัติว่าตำแหน่ง/เวอร์ชันเกม/ประกาศปิดพิเศษล่าสุดยังไม่เปลี่ยน

### 4.5 คำถามกำกวมจริง

เช่น “พบปัญหา เครื่อง”, “อยู่ที่ไหน” โดยไม่มีเป้าหมาย หรือ “ของหาย อุปกรณ์ เปียก” ที่รวมหลายเรื่อง อาจสมควรถามรายละเอียด ห้ามเติมสถานการณ์ที่ผู้ใช้ไม่ได้บอกเพื่อให้ผ่าน benchmark

## 5 Protocol keyword validity transport ต้องแยกกัน

| กลุ่ม | การตีความที่ถูก |
|---|---|
| Strict protocol mismatch | route/mode/contract ที่ grader ยังเทียบ Legacy; ไม่ใช่ content failure ทุกข้อ |
| Positive literal/clause | 62 checks ใน 18 คำถาม ไม่ครอบคลุมทุกคำถาม และอาจผ่านเมื่อคำตอบยัง partial |
| Legacy outcome flags | บางข้ออิงชนิดผลลัพธ์/คำตอบเต็มแบบเดิม ต้องอ่าน predicate จริง ไม่รวมเป็นจำนวนคำตอบผิดโดยอัตโนมัติ |
| Language/format | คำไทยในชื่อบริการภาษาอังกฤษอาจทำให้ old prose flag ติด ต้องแยกจากตัวเลขหรือเงื่อนไขผิด |
| Validity/source scope | แหล่งเก่า/ไม่มีช่วงที่มีผล/edition ไม่ตรง เป็นข้อจำกัดที่ต้องรักษา ไม่เติมข้อมูลให้ดูเหมือน current |
| Model transport | เชื่อมต่อถึงโมเดลสำเร็จหรือ timeout; ไม่ได้ยืนยันความหมายหรือความถูกต้องของคำตอบ |
| Model schema | แผน JSON ถูกโครงสร้างยังอาจเลือก game_detail ให้คำถามราคาได้ |
| Actual wrong predicate / false no-source | ยืนยันจากคำถาม คำตอบ และข้อมูลที่มี เช่น Beat Saber cost หรือ temporary suspension |

จึงไม่รวมทุก keyword fail/strict fail เป็น actual content failure และไม่รวมทุกคำถามที่ไม่มี positive contract เข้าเป็นคำตอบถูก

## 6 ลำดับพัฒนาต่อจากผลที่ตรวจได้

1. **รักษา requested operation และ explicit slots** — ราคา/เวลา/negation/audience ต้องไม่หลุด แม้โมเดลสร้าง extra task ว่าง
2. **รักษาบริบทที่ผู้ใช้ให้ไว้** — target จากประโยคเกริ่นต้องถึงงานย่อย โดยไม่มีการดึงข้อมูลจากคำตอบโมเดลมาเป็น fact
3. **ซ่อม binding ของ policy topics ที่มีอยู่จริง** — เช่น temporary suspension; ใช้ source identity ไม่พึ่งชื่อ opaque record
4. **เลือกกติกาเป็นกลุ่มที่มีเงื่อนไขครบ** — ไม่ใช้เพียง longest label หรือ top-k clause เดียวตอบคำถามกว้าง
5. **แยกข้อความไม่เข้าใจจากไม่มีข้อมูล** — แจ้งให้ตรงกับเหตุที่เกิด และไม่ขอข้อมูลเดิมจากเจ้าของซ้ำ
6. **ใช้ keys เดิมเป็น regression** — ทุกกรณีข้างบนมีคำถามเดิมอยู่แล้ว ไม่ต้องเพิ่มคำถามใหม่หรือรัน baseline ใหม่เพื่อเริ่มแก้

ลำดับนี้เป็นงานพัฒนาการตีความ/reader ต่อจากการตรวจย้ายข้อมูล ไม่ใช่หลักฐานว่า R119 ได้แก้คุณภาพคำตอบทุกหมวดแล้ว รายละเอียดคำตอบจริง แผน และ receipts ของทุกข้ออยู่ใน `http03/analysis/CASEBOOK_TH.md` และ `PER_REQUEST_REVIEW.jsonl`
