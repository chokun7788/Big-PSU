# เริ่มอ่านและใช้ format กลาง

ชุดนี้เป็นแบบออกแบบพร้อมต้นแบบรับเข้า **ยังไม่ได้ติดตั้งในบอทจริง** ไฟล์version `studio-content-3.0-design` โหลดเข้าระบบเก่าตรงๆไม่ได้

## อ่านอะไรเป็นลำดับ

1. `FORMAT_AND_FLOW_COMPLETE_TH.md` — ข้อเสนอทั้งหมด, dataflow, เหตุผล, สิ่งที่พบในrepo, migrationและข้อที่เจ้าของยังต้องยืนยัน
2. `OWNER_FIELD_GUIDE_TH.md` — 24ชนิด/155ช่อง, แต่ละช่องต้องกรอกอะไร, อ้างถึงหมวดไหน และช่องไหนจำเป็นก่อนPublish
3. `RESEARCH_EVIDENCE_TH.md` — paper23งาน +มาตรฐาน5รายการ, ระดับอ่านและข้อจำกัด, สิ่งที่ใช้กับระบบนี้ได้
4. `FLOW_IMPLEMENTATION_TH.md` — ขั้นพัฒนา P0–P4, acceptancegatesและfocusedtestloop

เปิด `report.html` ดูหน้าสรุปและค้นรายชื่อpaperได้แบบoffline ลิงก์paperต้องใช้อินเทอร์เน็ต Bibliographyเป็นรายการขั้นต่ำtitle/year/URL ไม่มีการเดาauthors/DOI/citationcount ให้ตรวจmetadataต้นฉบับก่อนใช้ในเอกสารวิชาการทางการ

## ทดลองกรอกเป็นdraftในโฟลเดอร์ใหม่

1. คัดลอก `templates/game.draft.json` ตั้งชื่อrecord_idใหม่ แล้วกรอก fieldsที่ทราบพร้อมevidence_refs
2. ถ้าไม่ทราบให้คง `status:unknown,value:null` และเหตุผล อย่าใส่0/falseเพื่อให้ดูครบ
3. ใช้ `templates/game_service.draft.json` ผูกgame_idกับservice_idจากทะเบียนในbundle; service/resource/zoneต้องมีrecordร่วมเพื่อให้FKตรวจได้
4. `control_set.draft.json` ใช้สำหรับปุ่ม/platform/preset; ราคาจริงกรอก `rate` ตามserviceและaudience ไม่คัดลอกไปทุกเกม
5. รวบรวม recordsกับsourcesในรูป `examples/actual_source_drafts.bundle.json` แหล่งข้อมูลมีpathและhashตามbytesจริง; ข้อมูลที่ไม่verifiedคงdraft
6. ทดสอบตรวจรับเข้าต้นแบบด้วยคำสั่งด้านล่าง จะรายงานshapeerrorsและcorefieldsที่ยังunknown **ไม่มีการPublishหรือเรียกLLM**

```powershell
$designDir = 'C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\canonical_format_research_20261010_180226'
$researchPython = 'C:\Users\Chokhun\Documents\Codex\PSU Esports Chatbot Ready 20261003\runtime\python\python.exe'
$env:PYTHONIOENCODING = 'utf-8'
& $researchPython -B "$designDir\validate_design.py" --bundle "$designDir\examples\actual_source_drafts.bundle.json"
```

ถ้าใช้เอกสารใหม่ในโฟลเดอร์sourceของคุณเอง ให้ระบุ `--source-root 'C:\path\to\your\sources'` และsources[].pathเป็นrelativeที่อยู่ใต้โฟลเดอร์นั้น ตัวตรวจrejectpathที่หลุดroot

รัน `validate_design.py` โดยไม่มีargsจะรัน45checksเดิมแล้วเขียน `VALIDATION_RESULTS.json` ภายในresearchfolder ข้อมูล6draftต้นแบบยังขาดcorefieldsบางส่วนโดยตั้งใจ (เช่นวันเวลาที่ไม่ยืนยันและtimezoneที่ไม่ได้ผูกsource) การผ่านdraftvalidationจึงยังไม่ใช่พร้อมPublish

## ผลรอบนี้กับขั้นถัดไป

- ทำแล้ว: inventory270canonicalrecords/10categories, ตรวจ488files, แบบ24types/155fields, 24templates/25schemas,6draftexamples,45checks, reviewdesign10รอบ, researchและflow
- ยังไม่ทำ: ownerUI, productionvalidator/adapter, QueryPlanLLMintegration, release/indexmigration, newrecordchatbenchmark, deployment
- ลำดับถัดไป: ownergamewizard +genericread/list/controladapter +newrecordholdouttests จากนั้นราคา/นโยบาย/เวลา ตามFlow
- Source/log/codeเดิมไม่ได้ถูกแก้; preservationcheckยืนยันhash488ไฟล์ที่สำรวจ ส่วนlogไม่ได้อ่าน/แก้หรือhashในรอบนี้

ข้อเท็จจริง/นโยบายที่ไม่มีหลักฐานยังต้องเจ้าของยืนยัน ส่วนschema/adapter/test/analysisเป็นงานเทคนิคที่เริ่มทำต่อได้เอง
