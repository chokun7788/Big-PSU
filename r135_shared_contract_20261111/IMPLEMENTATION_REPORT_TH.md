# ทดลองรวมเทคนิค shared need contract — 11 พฤศจิกายน 2026

ทำใน candidate ใหม่ `r135_shared_contract_20261111` จาก `r135_bounded_response_20261111` ไม่แก้รุ่นเก่า/owner/live/frozen ไม่เปลี่ยนน้ำหนักหรือหยุด protected model

## ขอบเขตรอบแรก

นำหลัก shared typed contract/need coverage/minimal raw spans/behavioral tests จาก M05/M07/M10/M21 ใน RESEARCH_METHODS_FOR_ALL_ISSUES_TH.md มาทดลองกับ **คำถามหลายงานที่ใช้ตัวเชื่อมหลายแบบร่วมกัน** โดยคง source/receipt verifier เดิมและทดสอบว่าราคาที่ผ่านแล้วรอดเมื่ออีกงานไม่พร้อม ไม่ได้ implement ทั้ง26method families หรือรับรองครบ48/76

## สิ่งที่พบก่อนแก้

คำถาม `PC นักศึกษา PSU ราคาเท่าไหร่; จองยังไง แล้วมีเกมอะไรบ้าง` ถูก splitter เดิมแบ่งเป็น2ส่วน เพราะเมื่อเจอ semicolon แล้วไม่ใช้กติกา แล้ว ต่อ ขณะที่ independent request observer เห็น3needs กรณี English/mixed separators ก็แบ่งไม่ตรงกัน

ผลก่อนแก้ `shared_contract_1794411318426031400/RESULT.json` ล้มด้านboundary/offset contract แต่ **positive delivery ที่ทดสอบก่อนแก้ยังผ่าน** เพราะมีชั้นอื่นช่วยเพิ่ม corrective tasks จึงห้ามอ้างว่ารอบนี้เปลี่ยนจากตอบผิดทั้งหมดเป็นถูกทั้งหมด หรือว่าคะแนนsemanticสูงขึ้นแล้ว

## เปลี่ยนโค้ดจริง

1. `domain_flow/routing.py`: สร้าง `need_spans` เป็น shared lexical boundary function ค้นตัวแบ่งทุกกลุ่มในรอบเดียว รักษา exact raw offsets และ opaque source names/quoted strings/URLs ไม่ normalize ชื่อหรือตัวเลขก่อนตัดข้อความ
2. เก็บ `split_needs` เป็น adapter ที่คืนข้อความจาก spans เพื่อให้ callers เดิมใช้ต่อได้ เมื่อคำขยายอย่าง `I am not a PSU student` อยู่หลัง separator จะรวมกลับกับงานก่อนโดยคงข้อความต้นฉบับรวม separator ไม่สร้าง quote ใหม่ด้วยการต่อช่องว่าง
3. `domain_flow/request_verifier.py`: ใช้ lexical boundaries ชุดเดียวกับ router แต่ยังตรวจ predicates/needs/constraints จากข้อความและ source vocabulary โดยไม่ใช้ผล planner tasks เป็นคำตอบ ความเป็นอิสระด้านsemanticจึงยังต้องตรวจภายนอก ไม่อ้างว่า shared splitter เป็น independent semantic proof
4. `domain_flow/context_guard.py`: เมื่อรีวิวบริบทซ้ำ ให้บันทึก basis ที่คำนวณใหม่จาก antecedent/source ได้อีกครั้ง แม้ target นั้นมีอยู่แล้ว ไม่เชื่อ audit tag เก่าและไม่ผ่อน compiler target guard

## แนวทางที่ล้มและการแก้

- แพตช์แบ่ง spans ครั้งแรกทำให้ขั้นตอนจองในคำถามตัวแทนหนึ่งข้อถูก `unproven_cross_task_target` เก็บ `shared_contract_1794411396057905900` ไว้ ไม่รับแพตช์นั้นเป็นรุ่นผ่าน
- พบว่า context review รอบสองเก็บ target ไว้ แต่ลบ source-related-booking basis ที่เคยคำนวณได้ออก จึงทำให้ compiler ปฏิเสธ การแก้คือคำนวณและบันทึก basis ซ้ำ ไม่ยอมรับ shared platform prefix เป็น target proof โดยอัตโนมัติ
- การตรวจ context guard ครั้งถัดมาพบ `NameError` เพราะยังไม่ได้ import norm เก็บ `shared_contract_1794411575102338300/RUN_ERROR.json` แล้วแก้ import ก่อนผลรอบใหม่ ไม่ใช้ attempt ที่ไม่มี RESULT ปิดการตรวจรับ
- ช่วงเตรียมสำเนาครั้งแรก exclude directory ชื่อ runtime กว้างเกินไป ทำให้ code `app/runtime` หาย6ไฟล์ ตรวจพบก่อนวัดพฤติกรรม คืนเฉพาะไฟล์ที่หายและตรวจ hashes ตรง baseline ทั้ง415 Python files บันทึก PREPARATION_AMENDMENT.json และแก้ตัวเตรียมสำเนาแล้ว

## ผลที่ตรวจผ่าน

| หลักฐาน | ผล | ขอบเขต |
|---|---|---|
| shared_contract_1794411658610522100/RESULT.json |33 checks| mixed coordinators, raw spans, names, qualifiers, context recheck และ natural source-only ราคา+จอง+เกมที่ model budget=0 |
| context_recheck_1794411731748949300/RESULT.json |3 checks| forced stale audit/target ถูกลบ และ compiler ยังปฏิเสธ target ที่ไม่มีใน request |
| typo_controls_1794411680909375900/RESULT.json |35 checks| คำผิด/คำขาด/เบิ้ล/ปฏิเสธ/ชื่อ/ตัวเลข/derived execution ยังทำงาน |
| bounded_response_1794411718452983400/RESULT.json |6 checks| budget admission/transport mock และ typed ราคา+จองยังอยู่ |
| verified_sources_controls_1794411737853659400/RESULT.json |22 checks| source relationships, wrong platform/สถานที่, source edit/withdraw, citation invalidation |
| partial_siblings_1794411797055381100/RESULT.json |6 checks| 2คำถามที่อีกส่วนไม่ยืนยัน/อยู่นอกข้อมูล ราคายัง0บาท ไม่รายงานครบ และไม่ยืมที่อยู่ศูนย์ |
| shared_http_1794411816301405100/RESULT.json |3 HTTP requests /12 assertions| คำถามสามงานผ่านแชตจริงตามลำดับ |
| typo_http_1794411831620798800/RESULT.json |11 HTTP requests /21 assertions| regressionแชตคำผิด/ราคา0/ราคา400+จอง/English/negative |

รวม105focused/source/mock checks และ14HTTP requests ที่แสดงไว้ ไม่ใช่จำนวนคำถามที่ใช้วัดsemantic accuracy และ assertions ภายในคำถามหนึ่งไม่เป็นตัวอย่างอิสระทั้งหมด

HTTPสามคำถามใหม่ใช้ wall time ที่สังเกตได้ประมาณ9.66,2.77,2.34วินาที ไม่ใช้ค่านี้อ้าง p95/p99 หรือว่าเร็วกว่ารุ่นเดิม เพราะไม่มี paired timing experiment รอบนี้

## ทดลองเปิดใช้

- URL: http://127.0.0.1:8143/
- version: `R135-Shared-contract-working`
- launcher: `Start-Shared-Preview.ps1 -NoBrowser`
- DB ของตัวเอง: `system/data/knowledge/verified_sources.sqlite` สำรองผ่าน SQLite backup API ไม่คัดลอกไฟล์ DB เก่าทับของใหม่
- logs/state เป็นของcandidateนี้ ไม่แชร์กับ8142/8140; raw details/DB/tokens/logsเก็บlocalบนD ไม่ขึ้นGit

## ข้อจำกัดและสิ่งที่ยังเปิด

- shared spans เป็น bounded lexical analysis ไม่ใช่ general parser ของทุกภาษา/ประโยคเงื่อนไข จึงยังต้อง source binding และ whole-request review
- raw need spans แยกตำแหน่งข้อความซ้ำได้ แต่ compiler/observer บางจุดยังใช้ `.find(quote)` ในบริบทอื่น รอบนี้ไม่ได้รับรองการผูกทุก task ของข้อความซ้ำหลาย occurrence ว่าถูกทั้งหมด
- การใช้ boundary helper ร่วมทำให้จุดผิดทางlexicalอาจกระทบทั้งrouterและobserver ต้องมีhuman-reviewed/unseen/directional controlsภายนอก ไม่เรียก shared boundary agreement ว่าsemantic correctness
- unknown siblingยังมีข้อความยืนยันไม่ได้ซ้ำ/หลายหัวข้อในบางกรณี เช่น Andaman Hotel เป็นปัญหาoutputshapeที่พบจริง ยังไม่ได้ย่อในรอบนี้ เพื่อไม่ปะปนกับการแก้scope
- game catalogยังpartialตามsource collection proof;0บาทยังมีข้อจำกัดช่วงมีผลตามsourceเดิม ไม่ยกระดับเป็นpublished/currentแน่นอนจากผลทดสอบ
- ยังไม่แก้root causeของmodel context timeout/cooldown ไม่พิสูจน์hard wall-clock cancellation/ทุกmodel fallbackหรือหลายผู้ใช้ และไม่รับรองfullowner/editor lifecycleทุกkind
- ไม่มี200/2111รอบใหม่ คะแนน196/255เดิมไม่รวมแพตช์นี้ ไม่แก้คะแนนหรือfrozenresultsย้อนหลัง
- ไม่มีtraining/distillation/reranker/documentmodelใหม่ และไม่deployแทนproductionก่อนgates/backup/rollback

## งานถัดไป

ตรวจ quote occurrence → task/slot provenance ที่compilerยังค้นข้อความแรก, output shape ของ unknown siblings, และ context timeout/admissionจากreceiptจริงเป็นคนละกลุ่ม เลือกfailureจริงก่อนแก้และใช้positive/negative/affectedregressionรอบเดียวหลังแก้ ไม่รันชุดเดิมซ้ำเมื่อไม่มีการเปลี่ยน
