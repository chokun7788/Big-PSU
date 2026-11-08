"""Write implementation and operator documentation; no business-data changes."""
import json,sys
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
from app.knowledge.common.task_contracts import TASKS
from app.knowledge.common.registry import CATALOG
from app.knowledge.common.read_graph import REQUIRED
from app.knowledge.common.store import CommonStore

flow='''# R101 — ลงมือพัฒนา Flow กลางจาก R97 Flow V2 ของ Astra

## 1. ขอบเขตและความหมายของความครบ

ใช้ R97 Flow V2 ตามที่ผู้ใช้ยืนยันเป็นข้อกำหนด เพิ่มแกนร่วมที่ใช้กับทุก task ใน registry และทุกหมวดฟอร์มทั้ง 24 หมวด ไม่เพิ่มชื่อเกมหรือราคาจริงลงในโค้ดเพื่อให้เคสเดียวผ่าน

ความครบของโค้ดไม่เท่ากับคำถามทุกภาษาและทุก paraphrase จะถูกตีความถูก 100% และไม่ใช่การรับรองข้อเท็จจริงที่ต้นฉบับไม่มี รายงานผลทดสอบแยกจากเอกสารนี้ใน [RESULTS_TH.md](RESULTS_TH.md)

ยังใช้ domain adapters ที่มีอยู่สำหรับการคำนวณราคา ราคาเหมา ข้อกติกาพ่วง การเลือกฉบับ และการติดต่อระบบจอง เพราะ R97 กำหนดให้นำ logic ที่พิสูจน์แล้วกลับมาใช้ผ่านสัญญาร่วม การมี adapter จึงไม่ใช่หลักฐานว่าใช้ข้อมูล Legacy ตอบแทน common ข้อมูลคำตอบทุกทางยังต้องอยู่ใน common snapshot หรือ provider สดที่อนุญาต

## 2. Flow ที่เชื่อมใน runtime

```mermaid
flowchart TD
 A[คำถามดิบ + delivered state] --> B[ตรึง release เวลา locale และงบคำขอ]
 B --> C[ตีความงานและเติม pending slot ที่ส่งถึงผู้ใช้จริง]
 C --> D[ค้น candidates จากชื่อ ชนิดข้อมูล และ FK]
 D --> E{typed task หรือ domain adapter เข้าใจแล้ว?}
 E -->|ใช่| F[RequestPlan + needs + qualifiers + origins]
 E -->|ยังไม่ชัด| G[LLM เสนอแผนทั้งคำขอ ไม่เกินหนึ่งครั้ง]
 G --> H[ตรวจ ID span ขอบเขต subject และส่วนคำถามที่ตกหล่น]
 H -->|ผ่าน| F
 H -->|ไม่ผ่าน| I[แยกขาดตัวเลือก ขาดข้อมูล และการตีความล้ม]
 F --> J[compile all_of any_of optional และ relation paths]
 J --> K[อ่าน static facts หรือ live observation ตาม need]
 K --> L[ตรวจ source validity authority และ dependencies]
 L --> M[typed calculators และ source renderer]
 M --> N[ตรวจ claims ที่ส่งจริง พร้อม receipts และสถานะราย need]
 I --> N
 N --> O[รวมส่วนที่ตอบได้และคำถามเฉพาะที่ยังขาด]
 O --> P[ตรวจ snapshot ยังเป็นรุ่นเดิม]
 P -->|เปลี่ยน| Q[อ่านใหม่ได้หนึ่งครั้งในงบเดิม]
 Q --> N
 P -->|ไม่เปลี่ยน| R[ส่งคำตอบและบันทึก intent state]
```

### จุดเชื่อมจริง

- `CommonAnswerer.answer` เข้า [complete_flow.py](system/app/knowledge/common/complete_flow.py)
- dispatcher และ owner preview ใช้ทางเดียวกัน ไม่แยกสมองตอบร่างอีกชุด
- `flow_context.py` เก็บ request ID, snapshot/time/locale, audit, semantic attempts, corrective reads และ provider cache
- `grounded_plan.py` ค้น candidates ก่อนขอแผน; โมเดลไม่สร้างราคา ปุ่ม กฎ หรือข้อความตอบ
- `read_graph.py` เป็น registry และ executor ของกราฟอ่านข้อมูล ไม่ได้มีเฉพาะภาพ diagram
- `request_plan.py` รวม needs โดยคง subject, slots, qualifiers และ dependency ของแต่ละส่วน
- `result_contract.py` แยก missing_source, needs_user_slot, not_current, broken_relation, temporary_failure และ live_unavailable

## 3. สัญญาของแผนและการตีความ

1. ชื่อและ IDs มาจาก release ปัจจุบัน ไม่มาจากรายชื่อเกมที่เขียนในโค้ด
2. Task IDs ใช้ registry เดียวกับ typed executors
3. คำถามปกติหนึ่ง proposition จำกัด output array ให้มีหนึ่ง need; เพิ่มจำนวนได้เมื่อพบ coordination นอกชื่อรายการ
4. Span binding รองรับความต่างของตัวพิมพ์และ Unicode แต่คืน span จากข้อความต้นฉบับ
5. หลาย needs ห้ามใช้ quote ช่วงเดียวกันซ้ำเพื่อสร้างงานที่ผู้ใช้ไม่ได้ถาม
6. ทุกช่วงคำถามต้องมี need หรือเป็นคำเชื่อมที่ตรวจได้ ห้ามทิ้งเงื่อนไขเพื่อให้แผนผ่าน
7. เกม อุปกรณ์ ฉบับ และขอบเขตราคาที่ระบุ ต้องผูกกับ named subject หรือ trusted context ไม่เลือกเกมสุ่มจาก retrieval
8. คำถามที่เข้าใจแล้วแต่ไม่มีแพ็กเกจตามชั่วโมงที่ขอ ไม่ส่ง LLM ไปเดาแพ็กเกจใหม่
9. Accepted semantic task เข้าตัว execute โดยตรง ไม่ถูก fullmatch ของประโยคเดิม veto อีกรอบ
10. Model JSON/transport failure เป็นปัญหาการตีความหรือการประมวลผล ไม่สรุปว่าฐานไม่มี facts

## 4. Read graph และหลักฐาน

`all_of` บังคับข้อมูลที่จำเป็นจริง, `any_of` เลือก proof branch ที่ครบ, `optional` ไม่ทำให้คำตอบหลักล้มเมื่อไม่มี context เสริม, `not_applicable` แยกจาก unknown

FK traversal ใช้ catalog และทิศทางที่ประกาศ มี inverse index และ cycle/depth bound ไม่เดินจาก service ร่วมไปเอาโหมดของอีกเกม จำนวนผู้เล่นมาจาก game_mode ไม่มาจากที่นั่งห้อง

Receipt มี need ID, subject/record/field, ค่าจริง, units เมื่อเกี่ยวข้อง, revision, validity, release/epoch และ source locator/hash/authority ไม่ใช้เพียงคำว่า citation ถูกเพื่อรับรองว่าตอบตรงโจทย์

Claim packet เป็น typed source claim ไม่ใช่เครื่องพิสูจน์ความหมายภาษาไทยทั่วไป จึงไม่ตั้ง semantic entailment=true ให้ prose ทุกประโยค การอนุญาตที่ยังไม่มี conditions จะไม่ถูกส่งเป็นคำอนุญาตแบบไม่มีเงื่อนไขแล้วตามด้วยคำเตือน

กรณีเกมอยู่โซนไหน มีสอง proof branches: game.venue_zone_ids → zone.name หรือ game_service → service.resource_ids → resource.zone_id → zone.name ไม่มีการสมมุติ FK เพื่อให้ได้ชื่อโซน

## 5. บริบทสนทนาและคำถามสองรอบ

ใช้เฉพาะ `common_read_state` ของ assistant turn ล่าสุดที่มี delivery_status ยืนยัน ไม่อ่าน assistant prose เป็นแหล่ง facts และไม่ขุด pending เก่าหลังเปลี่ยนหัวข้อ

- ราคา → “PC”/“ทั้งหมด”: ใช้ service binding เดิมพร้อม audience/duration origins
- ชื่อเกมหลายฉบับ → ชื่อฉบับ: ใช้ edition adapter ที่เก็บ original qualified query; generic selector ห้ามแย่ง slot นี้
- “ปุ่มยิงคืออะไร” → ชื่อเกม: เติม game slot และรักษางาน controls ถ้าไม่มีปุ่มจะบอก source gap ไม่เปลี่ยนเป็นเล่าเกม
- วันพรุ่งนี้ว่างไหม → “15:00”: เก็บ service/date แล้วเติมเวลาใหม่จากผู้ใช้
- ordinal หมายถึงลำดับที่แสดงจริง รายการที่ถูกถอนจะไม่เลื่อนหมายเลขไปเป็นอีกอัน
- intent/IDs อยู่ใน state ส่วนค่าราคา กฎ และสถานะสดอ่านใหม่ทุก request

## 6. เวลา ข้อมูลสด และราคา

เปิดบริการ, จองได้, maintenance และเครื่องว่างเป็นคนละ predicate การมี booking period ไม่พิสูจน์ physical opening; zone scope ที่ยัง unknown ไม่ถูกสมมุติเป็นทั้งศูนย์

ราคาคิดจากค่า/หน่วย/กฎ/กลุ่ม/ช่วงมีผลที่มีหลักฐาน ราคาเหมาคือ rental_package ไม่ใช่เอารายชั่วโมงคูณเป็นวัน Formula ที่ระบบไม่รองรับไม่ถูกโมเดลสร้างขึ้น

Live reader ใหม่อ่าน `live_binding` ของ common ได้โดยไม่ฝังชื่อเครื่อง: service/provider/external key/physical pool/status mapping/timezone/freshness policy และอายุข้อมูลสูงสุดเป็นตัวเลข `freshness_max_age_seconds`

- ฟิลด์ตัวเลขอายุข้อมูลเป็น optional schema extension สำหรับความเข้ากันได้ของ record เก่า แต่ต้องมีค่าจริงก่อนยืนยันสถานะผ่าน binding ใหม่นี้ ไม่มี TTL ธุรกิจที่สร้างให้เอง
- provider/date เดียวกันอ่านครั้งเดียวต่อ request; คำขอถัดไปมี context ใหม่
- ต้องตรง target date, timestamp ไม่อยู่อนาคตและไม่เก่าเกินที่อนุญาต
- at 15:00 อ่าน slot 15:00; ช่วงเวลาอ่านครอบคลุมทุก slot และห้ามมีช่องว่าง
- unknown mapping/ช่องว่าง/ข้อมูลหมดอายุไม่ใช่ free หรือ occupied
- ผลสดมี observation receipts แยกจาก static source receipts และไม่ดึงข้อมูลรายบุคคล

## 7. Owner workflow และ publication

```mermaid
flowchart LR
 A[เพิ่มหรือเปิดรายการเดิม] --> B[ฟอร์มจาก catalog/schema]
 B --> C[ตรวจชนิดข้อมูล ความสัมพันธ์ และ task readiness]
 C --> D[ทดสอบร่างด้วย runtime เดียวกับแชท]
 D --> E[บันทึก immutable source snapshot]
 E --> F[ผู้ดูแลตรวจและอนุมัติ revision นี้]
 F --> G[publish records + index + FK graph ใน transaction เดียว]
 G --> H[Published chat อ่าน release ใหม่]
 H --> I[แก้ร่างครั้งถัดไปยังไม่เปลี่ยนคำตอบที่เผยแพร่]
```

เพิ่ม `runtime_tasks` ใน readiness API และแผงฟอร์ม ใช้กราฟเดียวกับแชท ข้อมูลครบสำหรับ overview ไม่ได้แปลว่าครบสำหรับจำนวนผู้เล่นหรือ controls

แก้ index builder ให้ record เก่าที่ไม่มี optional field รุ่นหลังยังเผยแพร่ได้ โดยมอง cell ที่ไม่มีเป็น unknown ระหว่างสร้างดัชนี ไม่แก้ approved payload หรือ hash เดิม

Publish/withdraw/revision optimistic concurrency และ source approvals เดิมยังอยู่ การถอนต้องถอน referring records ก่อน ไม่ปิด FK guard เพื่อให้ทดสอบผ่าน

มี profile แยกชัดเจน: `r69-migration-preview` อ่านข้อมูลร่างชุดย้าย; `common-r101-published` อ่าน active release ที่อนุมัติแล้วและไม่ fallback Legacy ฐาน published ว่างตอบว่าไม่มีชุดเผยแพร่ ไม่รายงานผิดว่าฐานเสีย

## 8. Registry ของทุก task

ตารางนี้สร้างจาก executable registry จริง ไม่ใช่รายการที่วาดเพิ่มในเอกสาร Required alternatives แปลว่าเลือกหนึ่ง branch ที่ครบ ไม่บังคับทุก branch พร้อมกัน

| Task | Kinds | Required alternatives |
|---|---|---|
'''
for task,contract in TASKS.items():
 groups=REQUIRED[task];required=' OR '.join(' + '.join(group) for group in groups) or 'ตาม explicit attributes ที่ผู้ใช้เลือก'
 flow+=f"| `{task}` | {', '.join(contract.kinds)} | {required} |\n"
flow+='''
## 9. การตรวจทานสามรอบที่ทำจริง

### รอบ 1 — ขอบเขตสถาปัตยกรรมและ lifecycle

ตรวจ R97/R99/R100, ทำ shared request context/whole-request proposer/read graph, เพิ่ม readiness และ publication profile, ทดสอบ new/edit/withdraw ทุกหมวด พบแล้วแก้การเผยแพร่ old optional cells และ all-details ที่เคยหลุดไปเป็น policy.details

### รอบ 2 — ตรวจ counterexamples และคำตอบที่คะแนนหลอก

ตรวจคำตอบจริงใน saved subset พบ model เลือก Mario มาตอบ server/client ทั้งที่ไม่ได้ระบุเกม แม้ literal checker นับว่าดีขึ้น จึงเพิ่ม anchored subject และ non-overlapping spans ไม่เก็บ “คะแนนดีขึ้น” นั้นเป็นความสำเร็จ

ตรวจ generic pending แย่ง edition repair, custom rental ถูกส่งไป LLM และตอนถามปุ่มแล้วเลือกเกมกลายเป็น overview แก้ ownership ของ pending slot และไม่ใช้ semantic retry กลบ source gap ที่ typed parser เข้าใจแล้ว

### รอบ 3 — ตรวจ LLM จริงและ temporal live

ทดสอบกับเกมสมมุติที่เพิ่มใหม่ผ่าน owner form พบ JSON ไม่ครบจาก cardinality ที่กว้างเกิน และเลือก overview แทนกิจกรรมการเล่น ปรับ constrained output และความหมายของ task registry จากงานที่ผู้ใช้ต้องการ ไม่ใส่ชื่อเกมหรือคำตอบใน prompt

เพิ่ม live fixtures ที่ available_now เป็น free แต่ 15:00 occupied, ช่วงเวลามี gap, date ไม่ตรง และถามเวลาต่ออีกหนึ่งรอบ ป้องกันการตอบ now แทนเวลาที่ถาม

## 10. ข้อจำกัดที่รายงานอย่างตรงไปตรงมา

- ไม่มีการรับรองว่า LLM 4B ตีความ paraphrase ทุกแบบถูก; เก็บ proposal/rejection/transport/schema audit สำหรับวิเคราะห์
- Typed receipts ไม่ใช่ independent human adjudication ของทุกภาษา และ field-ready ไม่ใช่ source approval
- ราคาปัจจุบัน/eligibility/จำนวนผู้เล่น/นโยบายที่ไม่มีในต้นฉบับยังต้องได้ข้อมูลจริง ไม่ขยายวันมีผลหรือเพิ่มข้ออนุญาตให้ผ่าน test
- ชุดทดสอบ 91 requests เป็น development regression subset ไม่ใช่ full accuracy หรือ untouched holdout
- ยังไม่ได้ติดตั้งทับ R78; โค้ดและ launchers อยู่ใน candidate นี้ ข้อมูลและ approvals จริงไม่ถูกแก้
'''
(R/'IMPLEMENTED_FLOW_TH.md').write_text(flow,'utf8')

guide='''# วิธีใช้ R101 และเพิ่ม/แก้ข้อมูล

## เปิดใช้งาน

เก็บโฟลเดอร์ R101 ไว้ในโปรเจกต์นี้ เพราะ launcher ใช้ Python ที่มีอยู่แล้ว ไม่ได้คัดลอกโมเดลหรือ runtime ขนาดใหญ่เพิ่ม

1. เปิด Ollama ที่มีโมเดลเดิม
2. ใช้ `Open-Preview.cmd` เพื่อดูข้อมูลชุดย้ายบนโค้ดใหม่ที่พอร์ต 8121
3. ใช้ `Open-Owner.cmd` เพื่อกรอกและทดสอบข้อมูลที่พอร์ต 8122
4. ใช้ `Open-Published.cmd` เมื่อต้องการอ่านเฉพาะชุดที่อนุมัติและเผยแพร่แล้ว พอร์ต 8121 ต้องไม่ซ้ำกับ preview

ปิดหน้าต่าง server เดิมก่อนสลับโหมด หรือใช้ `Start-R101.ps1 -Mode Published -Port 8123` ไม่มีการเปิด server ค้างไว้โดยอัตโนมัติจากการพัฒนารอบนี้

**ฐานชุดย้ายที่คัดลอกมามี active release/approvals จริงเป็นศูนย์** โหมด Published จึงยังไม่แสดงข้อมูลร่าง การกรอกข้อมูลครบไม่ได้สร้างการอนุมัติให้เจ้าของอัตโนมัติ โหมด Preview ใช้ตรวจข้อมูลเดิมและข้อมูลใหม่ก่อนเผยแพร่ได้

## เพิ่มข้อมูลใหม่

1. เลือกหมวดจากสิ่งที่ต้องการให้แชทตอบ ไม่จำเป็นต้องเอาทุกเรื่องลง FAQ
2. ตั้งรหัสถาวรครั้งเดียว เช่น `game_aurora_paths` ชื่อแสดงและชื่อเรียกย่อเปลี่ยนภายหลังได้ รหัสใช้เชื่อมข้อมูล
3. กรอกเฉพาะสิ่งที่ยืนยันได้ ถ้ายังไม่ทราบเลือก unknown; confirmed empty list ใช้เมื่อยืนยันว่าไม่มีจริง
4. ดูความพร้อมรายงานที่ฟอร์มและหัวข้อ “ตรวจจากกราฟเดียวกับแชท” หากข้อมูลเกมครบแต่ปุ่มไม่มี ต้องเพิ่ม control_set ที่อ้าง game_id เดียวกัน
5. ทดสอบร่างด้วยคำถามไทย/อังกฤษและชื่อรายการนั้น แชทใช้ runtime เดียวกับโหมดเผยแพร่
6. บันทึก ตรวจแหล่งข้อมูล อนุมัติ revision แล้วเผยแพร่ ข้อมูลจริงจะเปลี่ยนเมื่อ publish

## ตัวอย่างสมมุติ — ไม่ใช่ข้อมูลบริการจริง

เพิ่มเกม “Aurora Paths”: game.title/summary/how_to_play และ aliases เป็นชื่อที่ลูกค้าเรียก → ตอบว่าเกมอะไร/เล่นยังไง

เพิ่ม game_mode ที่ game_id ชี้เกมเดียวกัน มี mode_name/platform/players_min/players_max → ตอบจำนวนคน ไม่ใช้ room_seats แทน

เพิ่ม game_service ที่ game_id ชี้เกม, service_id ชี้บริการ, offered มีหลักฐาน → ตอบศูนย์มีให้เล่นตรงไหน ส่วน installed_resource_ids ต้องมีหลักฐานการติดตั้งจริง

เพิ่ม control_set ที่ game_id/platform/preset/input_device/bindings ถูกต้อง → ตอบปุ่ม ไม่ต้องแก้โค้ดชื่อเกม

เพิ่ม rate สำหรับ service และ audience: ตัวอย่างสมมุติ 100 บาทคือ amount_minor=10000, currency=THB ระบุ unit/duration/calculation_rule และวันมีผลจริง การไม่มีวันมีผลไม่ใช่เหตุผลให้ใช้วันที่วันนี้แทน

เพิ่ม rental_package สำหรับเหมาครึ่งวัน/เต็มวัน พร้อม zone_ids/audience_id/period_label/duration_minutes/amount_minor/currency/terms ไม่คูณราคาชั่วโมงเอง

เพิ่ม live_binding ต้องทราบรหัส API/pool/status mapping และ freshness_max_age_seconds ที่อนุญาต เช่น ตัวเลขจากนโยบายจริง ไม่ใช่ค่าที่โมเดลเดา

## แก้ข้อมูลเดิม

- เปิดรหัสรายการเดิมแล้วแก้ค่า ไม่สร้าง ID ใหม่เพียงเพราะราคาเปลี่ยน
- ใส่ change note, ตั้งวันมีผลตามหลักฐาน ทดสอบร่างและอนุมัติ revision ใหม่
- draft edit ไม่เปลี่ยนคำตอบ Published จนกว่าจะ publish
- ถ้าเป็นคนละฉบับเกมหรือคนละรายการแข่งขันจริง ให้สร้างรายการใหม่และ aliases ที่แยกฉบับได้
- ถอนรายการเมื่อเลิกใช้งาน ระบบจะให้จัดการ referring records ก่อน เพื่อไม่ให้แชทเห็นข้อมูลอ้างอิงขาด
- คำถามต่อเนื่องจะอ่าน revision ใหม่; ไม่มีค่าราคาหรือข้อกฎจากคำตอบเก่าถูกเก็บเป็น facts

## เลือกหมวด

| หมวด | เหมาะกับ |
|---|---|
'''
for kind,row in CATALOG.items():guide+=f"| `{kind}` | {row['owner_form']} |\n"
guide+='''
## อะไรไม่ควรกรอกให้ดูครบ

ไม่เลือก “บุคคลทั่วไป” แทน “บุคคลภายนอก” โดยไม่มี eligibility ไม่เดาปุ่มจากเกมคล้ายกัน ไม่ใส่จำนวนผู้เล่นจากที่นั่ง ไม่ตั้ง open_periods จาก booking slots และไม่ยืดราคาเก่าที่หมดอายุ

ดูผลและขอบเขตการตรวจใน [RESULTS_TH.md](RESULTS_TH.md), ดู Flow และ registry ใน [IMPLEMENTED_FLOW_TH.md](IMPLEMENTED_FLOW_TH.md)
'''
(R/'README_TH.md').write_text(guide,'utf8')
print('Wrote detailed flow and operator guide; tasks=',len(TASKS),'kinds=',len(CATALOG))
