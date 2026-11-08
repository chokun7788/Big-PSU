# ข้อ2 — หลักฐานเพิ่มระหว่างการทดสอบย่อย

รายงานหลัก ITEM02_DETAILED_DIAGNOSIS_TH.md และ gate เสร็จก่อนยิงsample01แล้ว เอกสารนี้เป็นการอ่านหลักฐานเดิม/ทดลองเส้นทางโค้ดเฉพาะในหน่วยความจำเพิ่มระหว่างรันทดสอบ ไม่แก้candidateที่วัด ไม่เปลี่ยนprompt/data/weights และไม่รันbaselineใหม่

## การผูกGPU: แยกต้นเหตุได้ด้วยตัวแปรเดียว

ตรวจคำถามGPUทั้ง13keysที่พบในผลเดิม ทุกข้อมีสเปกใน equipment_gaming_pc แต่poolที่เลือกไม่มีrecordนี้ เมื่อเปลี่ยนเฉพาะผลของ FactIndex.bind ในprocessวินิจฉัยให้เป็นfactsของเครื่องPCเดิม ตัวreaderเดิมอ่านGPUได้ครบ13ข้อ โดยไม่เปลี่ยนsourceหรือreader จึงยืนยันเหตุที่bindingได้ชัดกว่าการเห็นterminal missing_source

คำว่า จอ ใน การ์ดจอ จับmonitor ส่วน เครื่องPC ที่ยาวกว่า pc ทำให้service-capacity aliasesกีดกันaliasที่รวมequipmentPC poolไม่ว่างจึงไม่เข้าทางสำรอง device_type ดู POST_GATE_GPU_CAUSAL_REFINEMENT.json

84keysได้รับการตรวจรายกรณีหรือlocalcausalprobeแล้ว (72ก่อนgate +GPUเพิ่ม12ที่ไม่ซ้ำ) ในนี้มีตัวอย่างcontent/scope/omissionfailureที่ยืนยัน41keys ไม่ใช่จำนวนผิดทั้งหมดของ20,554และไม่ใช่semanticaccuracy

## Admission: มีโมเดลทำงานอยู่ แต่คำขอไม่ได้ส่งถึงโมเดล

จำนวนจากtraceเดิมครบ20,554requests:

- all_requests: 20554
- requests_with_admission_denial: 8890
- requests_with_explicit_concurrency_busy: 3971
- admission_denied_without_any_http: 8857
- budget_fully_reserved_without_any_http: 2420
- nonanswer_or_partial_state_without_http_after_denial: 6374

ตัวเลขกลุ่มเหล่านี้ซ้อนทับกันและไม่ใช่จำนวนคำตอบผิดทั้งหมด บางrequestกู้คำตอบด้วยtypedreaderได้ การพบadmissiondenialอย่างเดียวไม่พิสูจน์ว่าเป็นต้นเหตุของคำตอบสุดท้ายทุกข้อ

มี3,971requestsที่metadataระบุconcurrency busyตรง ๆ และ8,857requestsมีadmissiondenialโดยไม่มีHTTPไปโมเดลเลย จึงไม่ควรตีความทุกข้อความว่าโมเดลขนาด4Bตีโจทย์ไม่ออกหรือbusinessdataไม่มี

model_gateway.reserve_modelทำก่อนadmission จึงมี2,420requestsที่reserveครบbudgetทั้งที่ไม่มีHTTP ต้องออกแบบและตรวจpolicyของreserved/attempted/spentให้ชัดในรอบแก้ ไม่ประกาศว่าการนับเช่นนี้ผิดทุกกรณีโดยยังไม่ตกลงbudgetcontract

## Parser: การสำรวจเดิมนับบางpathไม่ครบ

- ['context', 'r121_root_fields', None]: 196 unique events
- ['selector', None, 'plans_not_array']: 64 unique events

รอบนี้รวมunderstanding.eventที่อยู่บนcompatibilitypathและdeduplicateด้วยeventidด้วย ไม่อ้างJSON/HTTPsuccessว่าselectionสำเร็จ และไม่อ้างschemafailว่าโมเดลให้factผิดถึงผู้ใช้เสมอ

## ข้อจำกัดของการวัดเวลาในsample

มีoffline forensic parsingทำงานร่วมบางช่วงระหว่างsample และserverqueue/admissionขึ้นกับลำดับคำขอ จึงรายงานเวลาและการเกิดซ้ำตามสภาพรอบนี้ ไม่อ้างการเปลี่ยนlatencyหรือคะแนนว่าเป็นผลแก้Flow เพราะruntimeไม่เปลี่ยน
