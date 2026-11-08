# R101 — ผลการพัฒนาและตรวจรับจาก R97 Flow V2

## 1. สรุปสิ่งที่ส่งมอบ

เชื่อม Flow กลางที่พัฒนาจาก R97 เข้าทางตอบจริงของ candidate R101 แล้ว มี shared request context/plan, ตัวอ่านกราฟ 32 tasks, owner readiness และวงจรเพิ่ม–แก้–ถอนทั้ง 24 หมวด พร้อม semantic planner ทั้งคำขอที่ใช้ budget เดียวกัน โมเดลเลือกงานและรายการจาก common snapshot แต่ไม่สร้างราคาหรือข้อกฎเพื่อเป็น facts

นี่เป็นการพัฒนาโค้ดและการตรวจหลายหมวด ไม่ใช่เพียงนำข้อมูลทดลองไปย้ายให้เห็นหน้าตา การรับรองว่าคำถามธรรมชาติทุกแบบถูกและพร้อม production ยังไม่เกิดขึ้น ดูข้อจำกัดและ mapping ตาม R97 ใน [R97_CONFORMANCE_TH.md](R97_CONFORMANCE_TH.md)

ไฟล์ใช้งาน: [README_TH.md](README_TH.md) · Flow ที่เชื่อมจริง: [IMPLEMENTED_FLOW_TH.md](IMPLEMENTED_FLOW_TH.md) · สถานะเครื่องอ่าน: [IMPLEMENTATION_STATUS.json](IMPLEMENTATION_STATUS.json)

## 2. แยกหลักฐานแต่ละชนิด

### 2.1 ชุดตรวจเฉพาะส่วน

| ชุดตรวจ | ผ่าน/ทั้งหมด | โฟลเดอร์หลักฐาน |
|---|---:|---|
| test_contract_flow.py | 59/59 | gate_contracts05 |
| flow_contracts.py | 65/65 | gate_flow04 |
| test_all_categories.py | 154/154 | gate_categories03 |
| test_semantic_flow.py | 17/17 | gate_semantic04 |
| test_live_bindings.py | 10/10 | gate_live04 |
| test_published.py | 9/9 | gate_published03 |
| test_conflicts.py | 4/4 | gate_conflicts02 |
| test_existing_fixture.py | 19/19 | gate_rental03 |
| test_existing_competition_fixture.py | 7/7 | gate_rules02 |
| test_flow_v2.py | 17/17 | gate_v203 |

รวมชุดหลัก **361/361 assertions** โค้ดไม่เปลี่ยนระหว่างรัน: [SELECTED_GATES.json](SELECTED_GATES.json) จำนวนนี้รวม schema/guard/relation/lifecycle assertions ไม่ใช่ 361 คำถามลูกค้าอิสระ

หลังชุดหลัก พบรอบเปรียบเทียบให้โมเดลเปลี่ยน unknown game ไปเป็นนโยบายศูนย์ และคำถามเปิดตอนนี้ไปเป็นกฎของหาย จึงแก้ subject-gap terminal, ผูกชื่อกลับ raw input และสงวน live predicate ให้ provider fallback จากนั้นตรวจส่วนที่ได้รับผล **contracts 59/59 และ semantic 22/22** หลักฐาน [contracts ล่าสุด](verification/gate_contracts08/SUMMARY.json), [semantic ล่าสุด](verification/gate_semantic07/SUMMARY.json) ไม่บวกการรันซ้ำเป็นจำนวนเคสใหม่ และไม่อ้างว่าชุดหลักทั้งชุดถูกรันซ้ำหลัง patch นี้

ชุด 24 หมวดสร้างข้อมูลสมมุติผ่าน owner path ถาม all-details ไทยและอังกฤษรวม 48 คำขอ ตรวจ revision และถอนทุกหมวด ฐานต้นฉบับไม่ถูกแก้ [ผล 24 หมวด](verification/gate_categories03/SUMMARY.json) การผ่าน all-details ไม่รับรอง task ย่อยทุกแบบของทุกหมวด

### 2.2 LLM จริงกับข้อมูลเพิ่มใหม่

ใช้เกมสมมุติที่เพิ่มผ่านฟอร์มใหม่ ถาม 3 คำถามไทย/อังกฤษ โมเดลจริงตอบตรงฟิลด์ **3/3**; generation calls 10.865 วินาทีครั้งเย็น และ 1.442/1.752 วินาทีถัดมา [raw summary](verification/real_planner03/SUMMARY.json)

ก่อนแก้เคย 2/3 เพราะ JSON ไม่ครบและ overview ถูกเลือกแทน how-to-play มีผลเก็บใน real_planner01/02 ปรับ cardinality/output budget และนิยาม task แล้วจึงได้ 3/3 การทดสอบนี้ทำก่อน patch subject-gap ล่าสุด ไม่ใช่สถิติทั่วไปของโมเดลและไม่ใช่ผล holdout

semantic suite ใช้ model protocol จำลองเพื่อตรวจ invariants, rental/rules fixtures มี controlled transport และ live suite ใช้ provider จำลอง ต้องแยกจากโมเดลหรือสถานะจองจริง

## 3. ชุดเปรียบเทียบ 91 คำขอ เปิด LLM

รอบสุดท้าย `release_subset09` ใช้ **91 request keys เดียวกัน / 162 grades** เทียบ retained R100 subset05 ไม่รัน R100 ใหม่ ไม่เปลี่ยน GT; วันที่ฐาน 16 ตุลาคม 2026 ตาม workload เดิม ไม่ใช่สถานะศูนย์วันนี้

มี positive literal content contracts 72 grades ผลดังนี้:

| ภาษา | R100 เดิม | R101 ล่าสุด |
|---|---:|---:|
| ไทย | 25/29 (86.21%) | 25/29 (86.21%) |
| อังกฤษ | 21/26 (80.77%) | 23/26 (88.46%) |
| Auto | 17/17 (100.00%) | 17/17 (100.00%) |
| รวม | 63/72 (87.50%) | 65/72 (90.28%) |

นี่คือคะแนนตามคำ/วลีของ checker เดิมเฉพาะชุดพัฒนา ไม่ใช่ semantic accuracy จากผู้ตรวจอิสระ และไม่ควรนำไปเทียบ full 20,554 คำขอของ Legacy ตรง ๆ

| ตัวชี้วัด | retained R100 | R101 |
|---|---:|---:|
| Strict ผ่านทุกเกณฑ์รวม route/mode/outcome/content | 19/162 | 19/162 |
| Protocol failure reasons | 150 | 150 |
| Outcome failure reasons | 19 | 19 |
| Content failure reasons | 10 | 8 |
| Evidence / validation / performance failure reasons | 0 / 0 / 0 | 0 / 0 / 0 |
| Model HTTP attempts / transport opened | 37 / 37 | 23 / 23 |
| Exceptions / empty answers | 0 / 0 | 0 / 0 |

failure reasons เป็นจำนวนข้อความผิดใน grades ซึ่งซ้อนกันได้ ไม่ใช่จำนวนคำถาม และ HTTP opened ไม่ได้พิสูจน์ว่า model JSON/task ถูกต้อง

Protocol ตัวอย่างคือ route ใหม่ `knowledge/common_read` เทียบกับ route เดิม `games`, `competition_rules`, `schedule` หรือ intent `list` แม้ข้อความตอบอาจตรงเนื้อหา ส่วน outcome ต้องอ่านคำตอบประกอบ เพราะ checker เก่าจำแนก answer/clarification จาก mode และคำศัพท์ของ flow เดิม ห้ามนับทุก outcome mismatch ว่าเป็นรูปแบบอย่างเดียวโดยไม่อ่านคำตอบ

Model attempts ลดจาก 37 เป็น 23 เพราะ typed source gaps ไม่ถูกส่งให้โมเดลลองใหม่โดยไม่มีเหตุ ไม่ใช่การปิด LLM ใช้ได้ตาม need; policy ของ workload ยังคงเปิด LLM และจำกัดการใช้ฮาร์ดแวร์จริงตาม admission เดิม

เวลาคำขอใน workload 2 workers นี้: median 1.116 วินาที, p95 4.004 วินาที, สูงสุด 6.049 วินาที เป็นผลชุดผสม static/LLM, provider สดถูกตั้ง unavailable จึงไม่ใช่ load capacity หรือเวลาของ LLM ล้วน

หลักฐาน [ANALYSIS.json](release_subset09/ANALYSIS.json), [PROGRESS.json](release_subset09/PROGRESS.json), [คำตอบและ failure content ที่คัดจาก raw](REMAINING_CONTENT_CASES.json), [before/after source](release_subset09_INTEGRITY.json), [strict grade changes ทุกรายการ](release_subset09/STRICT_GRADE_CHANGES.json)

รอบสุดท้าย strict grades เปลี่ยนจาก retained R100: ดีขึ้น 0 รายการ, ลดลง 0 รายการ นับแยกจาก positive content เสมอ

## 4. วิเคราะห์สิ่งที่ดีขึ้นและ regression ที่พบ

### การตาม relation ไปยังโซน

คำถาม Super Mario Odyssey อยู่โซนไหน เคยตอบชื่อ service โดยไม่อ่าน zone.name ทั้งที่มี relation อยู่ เพิ่ม zone projection จาก venue_zone_ids หรือ game_service→service→resource→zone พร้อม receipts จึงตอบ Nintendo Switch Zone จาก source จริง ทำให้ positive grades ที่ใช้คำถามนี้ดีขึ้นสองรายการ

### เกมไม่อยู่ในฐานแต่โมเดลตอบกฎศูนย์

รอบ release_subset07 พบคำถามที่สะกด unknown/answer ผิดเล็กน้อย โมเดลเลือก FAQ กฎศูนย์ที่ retrieval พบ ทั้งที่เกม Example Quest ไม่อยู่ใน catalog เป็น content regression จริง ไม่ใช่ protocol mismatch

แก้ให้ unmatched named game เป็น subject gap ก่อน fallback โมเดล และคงชื่อจาก raw span ไม่ lower-case ชื่อที่แสดง เพิ่มตัวอย่างหลายชื่อ/ภาษา ใช้ assertion ป้องกัน model call และตรวจไม่มี hits จาก policy รอบก่อนแก้และผลที่ล้มยังเก็บไว้ ไม่ลบหรือแก้คะแนนเก่า

### การปรับปรุงที่ไม่ได้วัดได้ด้วย 91 คำขออย่างเดียว

อีก regression ที่ต้องอ่าน strict grades จึงพบคือ “is the studio open right now?” รอบ release_subset08 ถูกเลือกไปตอบ FAQ ของหาย ทั้งที่ workload ตั้ง live provider เป็น unavailable และ R100 ตอบข้อจำกัดสดอย่างถูกเรื่องแล้ว แก้ให้ predicate ที่ live recognizer ยืนยันได้ แต่ไม่มี common binding อ่านสำเร็จ กลับ dispatcher/provider adapter เดิมโดยไม่เรียกโมเดลหา FAQ แทน เก็บผลเสียในรอบ 08 และเพิ่ม checks ก่อนตรึงรอบสุดท้าย ไม่จัดความผิดนี้เป็น protocol mismatch อย่างเดียว

release lifecycle ครบ 24 หมวด, game-mode reverse joins, pending controls/edition ownership, future live time slots, stale observations, typed contradictions และ bounded whole-request planning ต้องดู fixture เฉพาะ ความก้าวหน้าของสถาปัตยกรรมไม่ได้แปลว่าคะแนนชุดคำถามเดิมทุกข้อจะเพิ่มทันที

## 5. ประเด็นที่ยังเหลือใน content failures

รายการจริงทั้งหมดที่ checker ยังนับผิดอยู่ใน [REMAINING_CONTENT_CASES.json](REMAINING_CONTENT_CASES.json) การจัดประเภทต่อไปนี้เป็นการอ่านคำตอบและหลักฐานของผู้พัฒนา ไม่ได้เปลี่ยน raw grade ให้ผ่าน:

| ประเด็น | สาเหตุ/ความหมาย | สิ่งที่ยังควรทำ |
|---|---|---|
| server/client ต่างกัน | fallback ไม่ให้คำอธิบายเมื่อยังไม่ผูกกับข้อมูลศูนย์; checker ต้องการคำ server/client | ถ้าต้องการอยู่ในขอบเขตศูนย์ ให้มี FAQ อธิบายพร้อม scope ไม่ให้เลือกเกมอื่นมาตอบเพื่อผ่านคำศัพท์ |
| food/noise/damage ขาด 100–500 THB | เลือก summary FAQ ซึ่งกล่าวค่าชดเชยแต่ไม่ให้ตัวเลขตาม clause ที่ checker ต้องการ | ยังเป็นประเด็น undercoverage/source projection ที่ควรแก้ด้วย claim-level policy links; ห้ามย้ายจำนวนเงินจากหัวข้ออื่นมาแนบโดยไม่ตรวจ scope |
| บุคคลภายนอกเล่นได้ทุกเกมหรือไม่ | ไม่มีหลักฐาน universal eligibility; fallback ยังถามกว้างและไม่ตอบตรงว่าข้อยืนยันใดขาด | ปรับ targeted missing-source explanation และให้เจ้าของระบุ eligibility ตามบริการเมื่อมีข้อมูลจริง |
| VR ไม่จองได้ไหม | ตอบจาก source ว่า walk-in ต้องจอง ถูกสาระการจอง แต่ checker ต้องการคำ No แบบตายตัวและ one hour ที่ไม่ได้ถาม | wording/extra-clause mismatch; ไม่เติมระยะเวลาบังคับโดยไม่มี source ที่ใช้กับ need นี้ |
| ขอข้อมูลที่ไม่ได้อยู่เว็บ | fallback จำกัด source แต่คำไม่ตรงกลุ่มวลีเก่า | ปรับคำอธิบาย source-scope ให้ตรงคำถามเมื่อมี intent ที่ยืนยันได้ |
| นำแอลกอฮอล์เข้าศูนย์ | source ยืนยันข้อห้ามบริโภค ไม่ยืนยันการนำเข้า คำตอบรักษาความต่างนี้ แต่ checker ต้องการ alcohol consumption ตรงตัว | มีทั้ง lexical mismatch และ source scope gap ไม่ควรยกข้อห้ามบริโภคเป็นข้อห้ามนำเข้าเอง |
| ราคาบุคคลทั่วไปของ PC | เลือกได้หลาย audience และราคาไม่มีช่วงมีผลยืนยันแล้ว ไม่ออกเลขปัจจุบัน; checker ต้องการบาท | ต้องมี eligibility/validity จริง และทำ clarification ให้เจาะจง ห้ามยืดอายุราคาหรือถือว่าทุก audience เท่ากัน |

จึงยังพูดไม่ได้ว่า “ไม่มี content failures” หรือ “ปัญหาที่เหลือมีแต่ checker” โดยเฉพาะ undercoverage และคำอธิบายช่องว่างข้อมูลที่ยังกว้างเกินไปเป็นงานพัฒนาจริง

## 6. ความสอดคล้องและสิ่งที่ไม่ถูกเปลี่ยน

- Final frozen run: source_unchanged=True, frozen_source_matched=True, exit_code=0
- [INTEGRITY.json](INTEGRITY.json) ตรวจ R100 frozen ต้นฉบับ, common.sqlite เดิม, AST และ candidate manifest
- production R78 ไม่ถูกติดตั้งทับ ไม่สร้าง approvals จริง ไม่แก้แหล่งข้อมูลเก่า/GT/log เดิม
- release_subset06 เคยแก้ runtime ระหว่างรัน: source_unchanged=false จึงไม่ใช้เป็นหลักฐาน frozen รุ่นสุดท้าย ผลและ receipt เดิมเก็บไว้
- release_subset07 เป็นผล frozen ก่อนแก้ regression unknown subject; รายงาน final ใช้ release_subset09 แยกจากรอบนั้น

## 7. สถานะการใช้งานจริง

เปิด Preview ผ่าน Open-Preview.cmd เพื่อตรวจชุดย้ายด้วยโค้ดใหม่ เปิด Owner เพื่อกรอก/แก้ข้อมูลได้ตามคู่มือ ส่วน Published อ่านเฉพาะ active approved release ซึ่งในฐานสำเนาจริงขณะส่งมอบยังมี **0 releases / 0 approvals** จึงยังไม่แสดง draft โดยอัตโนมัติ

launchers ใช้ runtime ของโปรเจกต์นี้และโมเดล Ollama เดิม ยังไม่ใช่การทำ portable bundle ใหม่ รอบนี้ไม่ได้เปิดเซิร์ฟเวอร์ค้างหรือสลับเว็บที่ผู้ใช้เปิดไปเป็น candidate อัตโนมัติ

สิ่งที่ยังไม่ยืนยัน: full accuracy, every paraphrase, exact C01–C37 ทั้งหมด, semantic contradiction ใน FAQ ทุกชนิด, real live oracle และ throughput production แยกไว้เพื่อไม่ให้เอาผล focused ไปอ้างเกินหลักฐาน
