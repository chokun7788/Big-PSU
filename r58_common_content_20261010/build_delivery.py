import json,shutil,hashlib
from pathlib import Path
OUT=Path(__file__).resolve().parent;CAND=OUT/'system/PSU_Esports_Chatbot_Local'
DOC=OUT/'docs';DOC.mkdir(exist_ok=True)
catalog=json.loads((CAND/'app/knowledge/common/catalog.json').read_text(encoding='utf-8'))
def write(name,s):
    (DOC/name).write_text(s.strip()+'\n',encoding='utf-8')
write('START_HERE_TH.md',r'''
# ชุดกรอกข้อมูลกลางและแชท r58 — เริ่มใช้งาน

## เปิดอย่างไร

1. เปิดโฟลเดอร์ `system/PSU_Esports_Chatbot_Local` ข้างรายงานนี้
2. ดับเบิลคลิก `Open-Owner-Content.cmd` เพื่อจัดการข้อมูล (ปกติพอร์ต 8097)
3. ดับเบิลคลิก `Open-PSU-Esports-Chatbot.cmd` เพื่อเปิดแชท (ปกติพอร์ต 8090)
4. หาก 8090 เป็นชุดเก่าที่เปิดอยู่ ใช้ PowerShell จากโฟลเดอร์นี้: `powershell -NoProfile -ExecutionPolicy Bypass -File .\Open-PSU-Esports-Chatbot.ps1 -Port 8098` อย่าหยุดโปรแกรมของผู้อื่น
5. หน้าเจ้าของต้องเปิดผ่าน launcher ซึ่งใส่สิทธิ์เฉพาะเครื่องให้ URL เปิดแค่ / โดยไม่มีสิทธิ์จะอ่านหรือแก้ข้อมูลไม่ได้
6. หยุดเฉพาะหน้าเจ้าของด้วย `Stop-Owner-Content.cmd` แชทใช้ launcher/ตัวหยุดเดิม

เครื่องนี้มี Ollama และโมเดลเดิมอยู่แล้ว ชุดนี้แนบ Python 3.12 x64 และ validator ไว้ ไม่ต้องติดตั้ง pip สำหรับแบบฟอร์ม ข้อมูลโมเดล Ollama ไม่ถูกคัดลอกเพิ่ม การเอาไปเครื่องอื่นยังต้องมี Ollama และดาวน์โหลดโมเดลผ่าน Setup-Local-Models.cmd ไม่ใช่แพ็กเกจแนบโมเดลทั้งหมด

## เพิ่มเกมแล้วตอบได้โดยไม่แก้โค้ด

- เลือก **ข้อมูลเกม** → สร้างใหม่ → ใส่ ID ถาวร เช่น `game_ocean_adventure`
- เลือก “มีข้อมูลยืนยัน” สำหรับชื่อ และกรอกชื่อไทย/อังกฤษตามจริง
- กรอกวิธีเล่น แนวเกม แพลตฟอร์มที่ทราบ ช่องที่ไม่ทราบใช้ unknown
- ข้อมูลปุ่มกรอกแยกใน **วิธีเล่นและปุ่ม** โดยเลือกเกมเดิม แพลตฟอร์ม อุปกรณ์ ชุดปุ่ม และแต่ละ action/button/context
- เกมเล่นกับกี่คนกรอกใน **โหมดเกม**; เกมอยู่บนเครื่องใดกรอก **เกมกับบริการ** เชื่อมเกม บริการ และเครื่องจริง
- ติ๊กยืนยันที่มาของข้อมูล → บันทึกร่าง → ตรวจและอนุมัติ → เผยแพร่ เกม/บริการ/เครื่องที่ถูกอ้างอิงต้องมีฉบับเผยแพร่ก่อน หรือใช้ API เผยแพร่เป็นชุดเดียวกัน
- ร่างไม่มีผลต่อคำตอบ การอนุมัติอย่างเดียวยังไม่มีผล ต้องเผยแพร่ด้วย
- ทดสอบ “<ชื่อเกม> เล่นยังไง”, “แล้วปุ่มล่ะ”, “<ชื่อเกม> PC controls”, “<ชื่อเกม> ทั้งหมด” ผ่าน preview และเว็บแชท
- การเผยแพร่ใช้ SQLite เดียวกับแชท คำถามถัดไปอ่าน release ใหม่ ไม่ต้อง restart เพื่อเพิ่มข้อมูล

## สถานะเริ่มต้นที่ต้องเข้าใจ

ฐานใช้งานเริ่มด้วยร่างจากข้อมูลจริง 41 รายการ **ยังไม่เผยแพร่** ระบบตอบเดิมจึงยังทำงานเหมือนก่อน ร่างไม่ใช่การอนุมัติข้อเท็จจริงของเจ้าของ และไม่ถูกแปลงเป็นนโยบายใหม่อัตโนมัติ ชุดทดสอบเกมสมมุติอยู่ใน fixtures แยกจากฐานใช้งาน

อ่านต่อ: OWNER_MANUAL_TH.md, FIELD_REFERENCE_TH.md, FLOW_IMPLEMENTATION_TH.md, TEST_AND_FAILURE_ANALYSIS_TH.md, REMAINING_AND_DECISIONS_TH.md
''')
write('FLOW_IMPLEMENTATION_TH.md',r'''
# Flow ข้อมูลกลางที่ลงมือทำแล้ว — studio-content-3.0

## 1. ขอบเขตและหลักการ

ตอบเฉพาะข้อมูลบริการศูนย์ เกม อุปกรณ์ ราคา การจอง นโยบาย การแข่งขัน และหมวดที่เกี่ยวข้อง เจ้าของเพิ่มรายการในชนิดข้อมูลเดิมได้โดยกรอกฟอร์ม ไม่ต้องเพิ่มชื่อเกมในโค้ด การเพิ่มชนิดข้อมูลหรือ operation ใหม่ เช่น สูตรคำนวณเฉพาะ ต้องเพิ่ม schema และ adapter แล้วทดสอบ

ใช้ 24 kinds / 155 fields จาก registry เดียว สำหรับฟอร์ม validator renderer และรายการ fields ที่ LLM เลือก ความหมายของช่องเป็นสัญญาที่เครื่องอ่านได้ ไม่ใช้การถามชื่อเกมทุกตัวอย่างเป็นกลไกหลัก

## 2. เจ้าของ → ข้อมูลที่เผยแพร่

```mermaid
flowchart TD
 A[เลือกหมวดและกรอกค่าที่ทราบ] --> B[ยืนยันที่มาและบันทึกร่าง]
 B --> C[ตรวจ JSON Schema / เงิน / เวลา / ความสัมพันธ์ / หลักฐาน]
 C -->|ผ่าน| D[revision ใหม่ + source snapshot + audit]
 C -->|ไม่ผ่าน| E[แสดงข้อผิดพลาด / เก็บ release เดิม]
 D --> F[คนตรวจฉบับปัจจุบันและอนุมัติ hash]
 F --> G[เลือกฉบับที่อนุมัติและเผยแพร่]
 G --> H[ตรวจ release ทั้งชุด / FK / cycles / rates / EN]
 H -->|ผ่าน| I[สร้าง index และสลับ active ใน transaction เดียว]
 H -->|ไม่ผ่าน| E
 I --> J[แชทอ่าน release ใหม่ในคำถามถัดไป]
```

save ใช้ expected_version เพื่อกันทับร่างคนละฉบับ approve ผูกกับ revision/hash; publish ผูก expected_active และ request_key การกดซ้ำคำขอเดิมได้ release เดิม แต่ reuse key กับอีก selection ถูกปฏิเสธ ร่างที่ไม่เกี่ยวข้องไม่ขัดขวาง release ที่ใช้ฉบับเผยแพร่เดิม

## 3. คำถาม → คำตอบ

1. scope/translation/creation guards เดิมทำงานก่อน
2. อ่าน snapshot ของ active release เฉพาะข้อมูลที่เผยแพร่ ไม่ค้น draft
3. resolve entity จากชื่อ/aliases ในข้อมูลเอง → bounded fuzzy เมื่อคะแนน ≥0.88 และห่างตัวเลือกถัดไป ≥0.06 ป้องกันเลขภาค/รุ่น ไม่ยุบชื่อเกมต่างรุ่น
4. ถ้าเป็นคำถามต่อ อ่าน user history ทั้ง text และ content พร้อม protocol acknowledge ของเว็บเดิม
5. เลือก fields จากคำถาม/คำอธิบาย registry; ถ้ายังตีความไม่ได้ LLM เลือก fields ภายใต้ schema เฉพาะ kinds ที่เกี่ยวข้อง จำกัด 4 วินาทีและไม่อนุญาตให้เขียน facts/SQL/ID ใหม่
6. plan ที่ผิดรูปแบบ field ต่างหมวด หรือแพลตฟอร์มที่ไม่ได้เผยแพร่ถูกปฏิเสธ ถ้าไม่เข้าใจให้ถามเพิ่ม ไม่ใช้เรื่องย่อเกมเป็นคำตอบแทน
7. join ด้วย stable IDs: game→game_service→service/resources, game→control_set/game_mode, service/audience→rate, zone→rental, competition→rules/dependencies
8. วันที่มีผลใช้ aware datetime และช่วง [เริ่ม,สิ้นสุด) รวมตรวจ parent references ก่อนแสดงข้อมูลลูก แพลตฟอร์มผิดไม่ดึงปุ่ม PC ไปตอบ
9. ทุก field ตอบตามสถานะ known/unknown/not_applicable/conflicted พร้อม obligations และ evidence locator; ราคาแสดง amount_minor เป็น THB โดยไม่ใช้ float คิดเงิน
10. “ทั้งหมด” ของรายการที่เลือกใช้ทุก field และ relations ที่รองรับ ไม่ top-k รายการทั้งหมดใน common catalog ใช้ ID count เต็ม แต่รายการเดิมที่ยังไม่ย้ายไม่รวมใน common list และระบุขอบเขตไว้
11. finalizer ตรวจ active/epoch อีกครั้งก่อนคืนคำตอบ ถ้าข้อมูลเปลี่ยนระหว่างตอบให้ retry
12. คำถาม occupancy สดส่งต่อ WordPress adapter เดิม; common live_binding เป็น configuration ไม่ใช่สถานะจองสด

## 4. วงรอบที่ทำจริงและเหตุผล

| รอบ | สิ่งที่พบ | การแก้ / หลักฐาน |
|---|---|---|
| 1 | temp directory/sandbox socket เข้าถึงไม่ได้ | แยก test temp ใน candidate และขอสิทธิ์ loopback ผ่านระบบ เก็บผลผิดพลาดเดิม |
| 2 | note=null แต่ schema เป็น string; SQL INSERT releases จำนวน placeholders ผิด | normalize note และแก้ INSERT ก่อนผ่านชุด 17 เคส |
| 3 | native confirm ทำ UI ค้างใน browser; form เพิ่มเกมใหม่ต้องพิสูจน์ | เปลี่ยนเป็น dialog ภายในหน้า กรอก→อนุมัติ→เผยแพร่→preview ผ่านจริง มีภาพ |
| 4 | เว็บถามต่อหลุด เพราะ history ใช้ text; negative oracle ไป match คำว่าอนุญาตในไม่อนุญาต | รองรับ text/content; แก้ oracle ตามความหมาย คงผลรอบแรกไว้ เว็บ 22/22 ผ่าน |
| 5 | withdrawn name หายหลัง release ใหม่; platform ไม่รองรับ; EN nested; timezone overlap | cc_names ถาวร, platform guard, recursive EN validation, compare actual instants ผ่าน 22 เคส |
| 6 | selector หมวดกว้างไปตอบคนละเลขภาค; parent หมดอายุยังตอบ child; uncertain phrasing | จำกัด category fallback, recursive effective checks, clarification+bounded planner ผ่าน final 26 เคส |
| 7 | first request เสียเวลา import validator | preload ใน worker ก่อน ready; ผล timing รอบเว็บสุดท้ายอยู่ในรายงาน ไม่อ้าง concurrency จาก sequential tests |

## 5. หลักฐานวิจัยที่นำมาใช้และข้อจำกัด

[SGD](https://arxiv.org/abs/1909.05855), [D3ST](https://arxiv.org/abs/2201.08904), [SGD-X](https://ojs.aaai.org/index.php/AAAI/article/view/21341) สนับสนุนการแยก descriptions/slots ออกจากชื่อรายการ แต่เป็นคนละ model/dataset จึงไม่รับรองว่าบอทไทยตัวนี้ zero-error ใช้ holdout title, paraphrase, history และ near-negative ตรวจจริง

[JSON Schema 2020-12](https://json-schema.org/draft/2020-12/json-schema-validation), [PROV-O](https://www.w3.org/TR/prov-o/), [Ollama structured outputs](https://docs.ollama.com/capabilities/structured-outputs) เป็นเอกสารทางการสำหรับ typed contract, provenance และ constrained plan การได้ JSON ถูก schema ไม่ได้หมายถึงตีความคำถามถูก หรือเจ้าของยืนยันข้อเท็จจริงแล้ว รายละเอียดการค้น/ระดับการอ่านอยู่ในรายงานวิจัยก่อนหน้า
''')
write('OWNER_MANUAL_TH.md',r'''
# คู่มือเจ้าของข้อมูลกลาง

## สิ่งที่ต้องเตรียม

ใช้เครื่อง Windows ที่เปิดระบบเดิมได้ Python 3.12 x64 รวมในชุดนี้ แบบฟอร์มใช้ port 8097 เฉพาะ 127.0.0.1 ไม่ต้องใช้โมเดลเพื่อกรอก ตรวจ อนุมัติ หรือ preview แบบดึงค่า ส่วนแชทและ optional query planner ใช้ Ollama เดิม

ฐานจริง: `data/knowledge/approved.sqlite` ภายในโฟลเดอร์เดียวกับ app ถ้ากำหนด PSU_KNOWLEDGE_DB ให้ owner และ chat ใช้ path เดียวกัน อย่าชี้ไป fixtures และอย่าตั้ง PSU_COMMON_ALLOW_DEMO=1 สำหรับการใช้งานจริง

## 1. ID / aliases / ภาษา

ID ต้องขึ้นต้น a-z และใช้ a-z, 0-9, _, :, - ยาว 3–100 ตัว ใช้ชื่อถาวรเช่น `game_coral_trail` ไม่เปลี่ยน ID เพื่อแก้สะกด ใช้ aliases สำหรับชื่อเรียกที่คนใช้จริง ไม่ต้องกรอกสะกดผิดทุกแบบ ชื่อใหม่มาจากข้อมูล ไม่อยู่ใน dictionary โค้ด

text มี {th,en} ใช้ null เมื่อไม่มีคำแปล ตัวเลข เงิน เวลา IDs ใช้ร่วมกันทั้งสองภาษา เก็บ English status: missing/draft/agent_translated/reviewed/stale ถ้าแปลด้วยระบบแต่ยังไม่มีคนตรวจใช้ agent_translated คำตอบ EN ระบุสถานะนี้ ถ้าข้อความไทยเปลี่ยน review hash เดิมไม่ valid ต้องตรวจใหม่ ช่องติ๊ก “ตรวจภาษาอังกฤษ” ถูก reset ทุกครั้งที่เปิดรายการ

## 2. ช่องข้อมูลและสถานะ

- known: มีค่าตรงตามหลักฐาน เจ้าของยืนยันเมื่อบันทึก และตรวจอีกครั้งก่อนเผยแพร่
- unknown: ยังไม่ยืนยัน ใช้ null ห้ามกรอก 0, false หรือ “ไม่มี” เพื่อแทนไม่ทราบ
- not_applicable: ช่องไม่เกี่ยวกับรายการนี้ ไม่ใช่ไม่มีข้อมูล
- conflicted: หลักฐานขัดกัน เก็บร่าง/หลักฐานแยกและตัดสินใจก่อนเผยแพร่ หน้าฟอร์มยังไม่รองรับการเพิ่มหลักฐานขัดกันสองชุด ใช้ importer JSON สำหรับงานขั้นสูง

ดาว ★ คือ core ที่ต้อง known ก่อน publish ไม่จำเป็นต้องรู้ทุก optional field จึงเพิ่มเกมแล้วตอบเฉพาะที่ทราบได้ ปุ่ม/แพลตฟอร์มที่ไม่ทราบจะตอบว่ายังไม่มีข้อมูล ไม่ยืมจากเกมอื่น

## 3. เวลาและเงิน

ฟอร์มวันเวลาเป็นเวลาไทยและบันทึก +07:00 ต้องระบุ timezone ราคาหรือ event/rules/schedule/closure/news ต้องมี validity ที่ยืนยัน effective_from; effective_until เว้นว่างได้เมื่อมีหลักฐานว่าไม่กำหนดวันหมดอายุ ขอบเวลาใช้ start inclusive / end exclusive

amount_minor คือสตางค์: 35 บาท=3500; 4000 บาท=400000 ค่า string “35 บาท”, จำนวนติดลบ หรือ unknown ที่ value=0 ถูกปฏิเสธ สกุลเงินและหน่วย/ระยะเวลา/กลุ่มคนต้องกรอกแยก ห้ามใช้ราคาหนึ่งกลุ่มแทนทุกคน แพ็กเกจเหมาไม่ใช่การคูณเรทรายชั่วโมงและไม่สับสนจำนวนเครื่องกับจำนวนที่นั่ง

schedule แยก open_periods, bookable_periods, maintenance_periods การเปิดห้องไม่เท่ากับเปิดจอง; maintenance ห้ามทับช่วง bookable วันปิดพิเศษมี closure แยก อย่าแก้ 12:00/13:00 โดยเดา

session_minutes และ occupancy_minutes แยกกัน เช่น VR ใช้ 30 นาทีแต่กันสถานะเครื่องเป็น 60 นาทีตามนโยบายที่ยืนยันไว้ live_binding เชื่อม physical pool ของบริการเข้ากับ API; ฟอร์มนี้ไม่ได้ดึงสถานะจองมาเป็นข้อมูลถาวร

## 4. ลำดับการกรอกสัมพันธ์

1. zone/equipment_model → resource → service
2. game และ policy ที่เกี่ยวข้อง → game_service / game_mode / control_set
3. audience + service → rate; audience + zone → rental_package
4. contact → procedure → policy (ถ้า policy อ้าง procedure)
5. game → competition → competition_rule; dependency rules ต้องครบ ไม่วงกลม ไม่ข้ามงานแข่งขัน
6. schedule/closure ผูก zone; resolution policy ต้องเผยแพร่ก่อนใช้
7. person/news เชื่อม public contacts/audience; ไม่ใส่ข้อมูลส่วนตัวหรือข้อมูลการจองของลูกค้าในเนื้อหาสาธารณะ

ถ้ามีหลาย records ที่ต้องอัปเดตพร้อมกัน approve ทุกฉบับก่อนแล้วส่ง /api/publish พร้อม ids หลายตัวและ expected_active เดียว ใช้สิทธิ์ local owner เดิม หากกดทีละรายการแล้ว dependency ยัง draft การเผยแพร่จะถูกปฏิเสธโดยไม่สลับ release

## 5. ค้นปัญหา / แก้ข้อมูล

preview ใช้ release ที่เผยแพร่ แสดง query_plan (เลือก record/field/platform/method), obligations (known/unknown/not_current/needs_clarification) และ release_id ถ้าร่างเปลี่ยนแต่คำตอบยังเก่า ให้ดูว่าอนุมัติ+publish แล้วหรือยัง ถ้าผิด platform ตรวจ control_set; ถ้าความสัมพันธ์หายตรวจ IDs; ถ้าราคาไม่ current ตรวจ validity; ถ้า English stale ตรวจการแปลผูก revision

history ใน preview เก็บเฉพาะหน้า เปิดหน้าใหม่เพื่อเริ่มบทสนทนาใหม่ เว็บแชทใช้ session/delivery acknowledgment ของระบบเดิม ความสำเร็จของ API แยกจากความถูกต้องของเนื้อหา คำตอบไม่ครบต้องดู obligations ไม่ใช้แค่ status=200

withdraw เก็บประวัติและกัน fallback ไปข้อมูลที่ถอน หากยังมี published records อ้างอยู่ต้องถอนลูกก่อน rollback ไม่อนุญาตให้ชุบชีวิตรายการที่ถอนแล้ว การแก้ร่างใหม่ยังคง release เก่าจนกว่าจะเผยแพร่

## 6. สำรอง / ตรวจ / import (ผู้ดูแล)

เปิด PowerShell ในโฟลเดอร์ชุดใช้งาน ใช้ runtime\python\python.exe -B -m app.knowledge.common.manage --db data\knowledge\approved.sqlite status

ตรวจ gate สำหรับทุก draft: `runtime\python\python.exe -B -m app.knowledge.common.manage check`

สำรองด้วย SQLite API: `runtime\python\python.exe -B -m app.knowledge.common.manage backup data\backups\content_20261010.sqlite` ใช้ชื่อใหม่ทุกครั้ง ไม่คัดลอก .sqlite ไฟล์เดียวขณะมี WAL

rollback: `runtime\python\python.exe -B -m app.knowledge.common.manage rollback RELEASE_ID --expected-active CURRENT_RELEASE_ID` ตรวจ release_id จาก trace/audit ก่อน ใช้ backup เดิมสำหรับการกู้ระดับไฟล์หลังหยุดผู้เขียนทั้งหมดเท่านั้น

import: `runtime\python\python.exe -B -m app.knowledge.common.importer BUNDLE.json --actor local-owner` bundle มี schema_version/sources/records importer นำเข้า drafts เท่านั้น รายงาน saved และ pending_errors โดยไม่ทำ full-bundle transaction; ID ซ้ำไม่ทับของเดิม ให้แก้ revision ผ่านฟอร์ม

## 7. การดูแลสิทธิ์

ตัว editor เป็น local single-operator ในบัญชี Windows นี้ เปิดหลายแท็บได้แต่ revision guard กันทับร่าง ไม่ใช่ระบบ shared-admin/LAN/public authentication เก็บ capability ใน owner-session.json เพื่อเปิดซ้ำ อย่าแชร์ไฟล์นี้หรือ URL ที่มี token ปิดด้วย Stop-Owner-Content.cmd เมื่อต้องการหยุด editor ไม่เปลี่ยน permission ของบัญชี Windows อื่น
''')
lines=['# รายละเอียดฟอร์มทุกหมวด — 24 kinds / 155 fields','',
'ทุก field มี status/value/evidence_refs/note ใช้ schema 2020-12 ค่าที่กรอกผิดชนิดหรือ key นอก schema ถูกปฏิเสธ','',
'ค่ากลาง: schema_version, record_id, kind, branch_id=psu_phuket, revision, lifecycle, validity, localization, aliases, review ตัวระบบบันทึก revision/hash/audit ส่วนเจ้าของยืนยันเนื้อหา','']
for spec in catalog:
    lines+=['## '+spec['owner_form']+' (`'+spec['kind']+'`)','','| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |','|---|---|---|---|']
    for f in spec['fields']:
        s=f['value_schema'];t=s.get('type','');t='/'.join(t) if isinstance(t,list) else t
        detail=str(t)+(' enum='+', '.join(map(str,s['enum'])) if 'enum' in s else '')+(' → '+f['reference_kind'] if f['reference_kind'] else '')
        if s.get('type')=='object':detail+=' {'+', '.join(s.get('properties',{}))+'}'
        if s.get('type')=='array' and s.get('items',{}).get('type')=='object':detail+=' rows{'+', '.join(s['items'].get('properties',{}))+'}'
        lines.append('| '+f['key']+' | '+f['meaning_th']+' | '+('★' if f['publish_core'] else 'optional')+' | '+detail+' |')
    lines+=['','ต้นแบบ JSON: `app/knowledge/common/templates/'+spec['kind']+'.draft.json`','schema: `app/knowledge/common/schemas/'+spec['kind']+'.schema.json`','']
write('FIELD_REFERENCE_TH.md','\n'.join(lines))
write('REMAINING_AND_DECISIONS_TH.md',r'''
# งานที่ยังเหลือและข้อมูลที่ต้องตัดสินใจ

## P0 — ข้อเท็จจริงก่อนเผยแพร่

1. ร่าง 41 รายการยังไม่อนุมัติจริง ต้องตรวจการ map, English, relations และ validity ไม่ให้เครื่องลงนามแทนคน ตารางเดิมยังทำงานผ่าน legacy adapter
2. ข้อมูลเดิม canonical 270 รายการ มี mapping games 36 รายการ และเพิ่มร่างอ้างหลักฐาน 5 รายการ คิว canonical อีก 234 รายการยังรอ typed migration (270−36) ไม่มีการเติมคำตอบจากการเดา ดู migration_queue.json ส่วน draft 41 ไม่ใช่ 41 จาก 270 ทั้งหมด
3. ราคา/เหมาไม่มีวันมีผลยืนยันในบาง source: ถามเจ้าของเจาะจงว่า “ราคาใน workbook รุ่นนี้เริ่มใช้วันที่เท่าไร มีวันสิ้นสุดหรือไม่ และใช้กับกลุ่มใด?” ห้ามใช้วันที่ไฟล์แก้ไขแทนวันมีผล
4. กฎ Tekken/ข้อมูล RoV ที่ขัดกันหรือไม่ครบ: ระบุไฟล์ รุ่นงานแข่งขัน และข้อความข้อที่ขัดกันในคิว review อย่า merge ต่างเกมเป็นชุดเดียว
5. นโยบายที่ยัง unknown ต้องถามเป็นรายข้อ เช่น เวลาที่หายเพราะเกมอัปเดตมีชดเชยหรือไม่/ขั้นตอนอย่างไร ไม่ใช้ schema เติมคำตอบ

## P1 — งานที่ระบบทำต่อเองได้

- Typed migration ที่เหลือพร้อม lineage จากไฟล์เดิม เขียน mapper ตามหมวดและตรวจ unknown/semantics แบบไม่ publish อัตโนมัติ
- ต่อ calculator กับ rate/calculation_rule/rental แบบ amount_minor รวม rounding, eligibility, duration, minimums ตอนนี้ V3 ตอบข้อมูลเรทที่ประกาศได้ แต่ยังไม่ได้แทนสูตรคิดค่าใช้บริการทุกแบบของ legacy
- ต่อ calendar engine ให้ใช้ schedule+closure precedence เดียว ตรวจวันพิเศษ/maintenance/all zones และช่วงขอบเวลา ตอนนี้ typed validator ตรวจข้อมูลได้ แต่ runtime calendar เดิมยังเป็น operational adapter
- ต่อ live_binding กับ WordPress physical pool/version/freshness adapter โดยไม่ใช้ static records เป็น occupancy; ความถูกต้องสดที่ผู้ใช้ยืนยันก่อนหน้าแยกจาก schema tests รอบนี้
- เพิ่ม semantic record retrieval เมื่อคำถามไม่กล่าวชื่อ/หมวดชัดเจน ตอนนี้ V3 เน้นชื่อจากข้อมูล, schema fields, generic location/contact/schedule selectors และ bounded planner ไม่อ้างว่า arbitrary wording ทุกแบบผ่านแล้ว
- เพิ่ม batch publish UI / migration comparison UI / conflict evidence editor ตอนนี้ API รองรับ batch แต่ปุ่มหน้าเว็บ publish รายการที่เลือกทีละตัว
- English labels ของ fields แสดง canonical key ที่อ่านได้ และ fallback Thai source เมื่อไม่มี EN; ยังควรทำ glossary และ review เฉพาะ policy semantics ก่อนเปลี่ยนข้อเท็จจริง
- ทดสอบ optional LLM field planner เพิ่มด้วย paraphrases ที่ held out; model format valid ไม่เท่ากับเลือก field ถูก ให้ดู method/obligations ใน log
- ทดสอบจำนวนคนใช้งานพร้อมกันและ isolation ของ admin ถ้าจะขยายเกิน local operator รอบนี้ไม่ได้รัน load/full GT test 2 หมื่นเคส

## ข้อจำกัดที่ไม่ควรถูกตีความว่าผ่านแล้ว

24 types validate/publish ได้ใน fixtures ไม่ได้หมายความว่าทุกหมวด migrate ข้อมูลจริงและมี operational adapter ครบ รายการ “ทั้งหมด” ใน V3 มีขอบเขต published common catalog และไม่รวม legacy ที่ยังรอย้าย ความพร้อมของ owner editor แยกจาก correctness ของข้อมูลจริง, การแปลเชิงนโยบาย, live occupancy และ concurrency

ชุดทดสอบใหม่ใช้ข้อมูลสมมุติที่ผลแน่นอน ฐานใช้งานไม่ได้เผยแพร่ชื่อ Starfish Quest/Coral Trail ไม่มีการทับข้อมูล owner JSON หรือ log เดิม
''')
# Pin installed dependencies and keep the original distribution licenses.
pins={'jsonschema':'4.26.0','attrs':'26.1.0','jsonschema-specifications':'2025.9.1','referencing':'0.37.0','rpds-py':'2026.9.1','typing_extensions':'4.16.0'}
(CAND/'app/knowledge/common/requirements-lock.txt').write_text('\n'.join(k+'=='+v for k,v in pins.items())+'\n',encoding='utf-8')
write('DEPENDENCIES_TH.md','''# Dependency/runtime lock

Validator: jsonschema 4.26.0; attrs 26.1.0; jsonschema-specifications 2025.9.1; referencing 0.37.0; rpds-py 2026.9.1; typing_extensions 4.16.0

Vendored distributions retain .dist-info/licenses. rpds wheel is CPython 3.12 Windows x64. Bundled runtime is Python 3.12.14 x64. Use this runtime for the owner editor and chat. Other Python versions need compatible wheels and a new verified package; do not assume that changing only python.exe makes the pinned native dependency portable.

No global pip installation, PATH edits, API credentials or new model weights were added. Models/Ollama are the existing installation on this machine.
''')
runtime=CAND/'runtime/python'
if not runtime.exists():shutil.copytree(Path(r'C:\Users\Chokhun\Documents\Codex\PSU Esports Chatbot Ready 20261003\runtime\python'),runtime,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
m=json.loads((CAND/'package_manifest.json').read_text(encoding='utf-8'))
m['runtime_version']='2026.10.10-common-r58.2';m['python_runtime']={'path':'runtime/python/python.exe','scope':'bundled-windows-x64','required':'3.12'}
m['common_content']={'version':'studio-content-3.0','kinds':24,'fields':155,'database':'data/knowledge/approved.sqlite','initial_active_release':'','migration_drafts':41,'mode':'local owner editor; legacy operational adapters retained'}
(CAND/'package_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
shutil.copytree(DOC,CAND/'owner_content_docs',dirs_exist_ok=True)
shutil.copy2(DOC/'START_HERE_TH.md',CAND/'OWNER_CONTENT_GUIDE_TH.md')
print('Detailed docs and bundled Python ready')
