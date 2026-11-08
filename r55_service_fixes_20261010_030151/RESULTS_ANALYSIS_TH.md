# ผลการแก้ r55 และข้อจำกัดที่เหลือ · 10 ตุลาคม 2026

## สถานะ

แก้โปรเจกต์จริงแล้ว เปิด candidate 2026.10.10-service-r55.7 ที่ http://127.0.0.1:8093/ ใช้ Python/โมเดลที่มีบนเครื่องนี้ ไม่ได้อัปเดตแพ็กเกจแบบแจกสองชนิดจากรอบเก่าโดยอัตโนมัติ

## ผลตรวจ แยกประเภทหลักฐาน

| หลักฐาน | ผล | ความหมาย |
|---|---|---|
| unit + fixture 8 modules บน source ล่าสุด | 92 tests, 0 failures, 0 errors | parser/slot/context/queue/timeout/calendar/known booking fixture; ไม่ใช่ทุก legacy test |
| ร้านเกม 156 HTTP requests บน r55.6 | 0 failed checks; 109 CHECKED, 47 REVIEW | transport ครบ; CHECKED ผ่านเฉพาะ owner-answer/contains/forbid/route ที่แต่ละเคสมี |
| follow-up / paraphrase / full-rule pages บน r55.7 | 44 requests, 25 checks, 0 failed checks | ตรวจสองรอบ 7 บทสนทนา + 16 คำใหม่ + pagination 2 ภาษา |
| controls และกฎที่ได้รับผลจากการแก้ล่าสุด r55.7 | 10 requests, 0 failed checks | ตรวจซ้ำส่วนเปลี่ยนจาก r55.6; ไม่เรียกว่า rerun 156 ทั้งชุดบน r55.7 |
| CS2 full sections | TH 56/56, EN 56/56 ไม่ซ้ำ | ความครบตาม rulebook ในระบบ ไม่ยืนยันกติกาปีอื่น/รายการใหม่ |
| owner hash | 38/38 ไม่เปลี่ยน | ข้อมูลเจ้าของคงเดิม; candidate app hash ตรง ROOT |

REVIEW 47 ข้อบางข้อถูกอ่านตรวจแล้วว่าเข้ากับ source เช่น unknown policy และ catalog แต่ยังไม่มี oracle เนื้อหาครบของทุกข้อ จึงไม่แปลงเป็น accuracy 100% จาก HTTP 200 หรือจากคำที่ตรงบางคำ

ผล unit เดิมที่ผิดยังอยู่ในไฟล์ loop* / final*: มีข้อผิดจริงเรื่อง VR ที่แก้แล้ว, environment tmpdir ของ runner ที่แก้แล้ว และ calendar assertion ที่แยก A/a/Thai/ thai การแก้ assertion รอบท้าย casefold ทั้ง expected และ actual รักษาข้อความเงื่อนไขนโยบายเดิม ไม่ลดเกณฑ์ข้อเท็จจริง

## ทำไมข้อมูลครบแต่เลือกตอบผิด และสิ่งที่แก้

| ลำดับ | สาเหตุที่พบ | การแก้ | สิ่งที่ควรตอบ / หลักฐาน |
|---|---|---|---|
| P0 | เลขเวลาถูกอ่านเป็นเลขเครื่อง; นาทีใน 9:00-9:30 ถูกอ่านเป็นช่วง 00-9 | boundary/unit guards และ parse date ก่อน time | VR 09–09:30 ตรวจ 09–10; fixture ครึ่งหลัง busy ต้องไม่บอกว่าว่าง |
| P0 | semantic handler ชนะก่อนตรวจข้อมูลเจ้าของ; subject ผิดสลิป/เปลี่ยนรอบ/รายชื่อไม่ครบไม่เข้า claim | bounded owner claims ก่อน generic retrieval; subject+operation+negation | ผิดสลิปส่งเพจ; เปลี่ยนรอบยกเลิกทางอีเมลแล้วจองใหม่; เช็กอินรายคน |
| P0 | typed plan ทำ customer group/คำระยะเวลา/จำนวนคนหาย | retain group, number words, people count | PC บุคคลทั่วไป 2h = 140 บาท; Nintendo 4 คนใช้ package 3–4 คน |
| P1 | server early price rewrite ลบส่วนเกม/คำถามอื่น | split operations ก่อน server price plan และก่อน early return | ต้องได้รายการเกม PC และราคาในคำตอบเดียว |
| P1 | คำตอบสั้น ทั้งหมด/PC ไม่ผูก pending task; PC2 ไม่เก็บเวลาเดิม | task memory/eligible context + scope/date/time ที่ยืนยัน | หลังถามราคาแล้วตอบ PC ต้องได้ราคา; PC2 ต้องคงวันที่/เวลาเดิม |
| P1 | Continue with the remaining rules ไม่ตรง grammar ทำ cursor ไม่เดิน | bounded continuation grammar + ACK IDs | TH/EN ต่อจนได้ครบ 56 ส่วนไม่ซ้ำ |
| P1 | งบถูกตีความเป็น price question; ราคา 0 เสี่ยงตีความเป็นไม่จำกัด | integer affordability จาก package เดิม + capacity/group/expiry caveats | 100 บาท PC adult ได้ 1h เหลือ 30; missing group ถามกลับ |
| P1 | คำถามเกม/permission/identity/hours/control ใกล้กันถูกเลือกคนละหมวด | scoped catalog/hours/control/spec adapters และ pending installation guard | ขอ install Minecraft ต้องไม่ตอบว่าเกมมี/ไม่มีแทนสิทธิ์ติดตั้ง |
| P1 | broad กฎแข่ง ROV ล่ะ ถูกตอบ clause 4.1.1 ข้อเดียว | เติม discourse particle ใน broad-rule grammar; ปี/facet เฉพาะยังอยู่; เพิ่ม overview oracle | ตอบภาพรวมหลายหัวข้อ RoV พร้อมชื่อรายการ/source ไม่ใช่ clause เดียว |
| P2 | control preflight ใช้ session alias registry ที่หา CS2 ไม่เจอ และนับ Tekken variants เป็น 2 เกม | ใช้ existing control catalog resolver เฉพาะเกมเดียว; guards หลายเกม | คำถามปุ่มตรง source ลดการเรียก LLM; warning แหล่งรองยังอยู่ |
| P2 | ข้อความแถว Tekken มีคำอาหรับปน | cleanup ตอน render เฉพาะแถวที่รู้ provenance; raw source ไม่เปลี่ยน | ข้อความไทยอ่านได้; ไม่อ้างตรวจ controller จริงแล้ว |
| P2 | timeout สูญเสีย trace ตอน worker replacement | bounded partial progress แนบ timeout response/log ก่อนเปลี่ยน worker | รู้ขั้นตอนล่าสุด แต่ cause_confirmed=false จนพิสูจน์สาเหตุ |

คะแนน routing/candidate confidence เป็น heuristic ไม่ใช่ค่าความถูกต้องของคำตอบ การเลือก game target ถูกยังไม่พิสูจน์ว่า facet/coverage/ปีถูกทั้งหมด

## Loop และการปรับเกณฑ์จากผลจริง

1. web_loop1: 156 requests พบ failed checks 5 ข้อ (เปลี่ยนรอบ, Steam policy, catalog continuation timeout, multi-clause TH/EN)
2. web_loop2: 34 requests พบ 1 timeout ของคำถามนับเกม; partial trace ยืนยันขั้นตอนล่าสุด แต่ไม่พิสูจน์ root cause เดียว
3. near_loop3: full-rule TH/EN ครบแล้ว แต่พบ 3 checks ผิดจากราคา group-only, เกม+กี่บาท, install ชื่อเกมโดยไม่มีคำว่า game
4. web_final / near_final: แก้ 3 จุดจนผ่าน checks เดิม อ่านคำตอบเพิ่มแล้วพบ c124 ยังตอบไม่ครบ แม้ชื่อเกมตรง
5. web_final6: เพิ่ม broad_rules_need_overview แล้วผ่านทั้ง 156; กฎ ROV ล่ะจากประมาณ 14s เหลือประมาณ 0.9s
6. controls_final7 / near_final7 + units_final8: แก้ตัวค้นชื่อเกมใน control preflight และตรวจ subset ที่ได้รับผล พร้อม 92 unit/fixture tests

ทุก raw result คงชื่อเดิมไว้ ไม่มีการ rescore ไฟล์เก่าให้ดูเหมือนระบบรันใหม่

controls_semantic_audit.json รอบแรกกำหนด heading “ข้อห้าม” ให้ภาพรวม RoV โดยไม่มีเหตุผลจาก formatter จึงเกิด false failure เพิ่ม รอบ v2 ตรวจ format/equipment/pause/penalty และ metadata หลาย source sections แทน เก็บผลรอบแรกไว้ ชี้แจง oracle_revision และไม่เรียก offline audit ว่ารัน pipeline ใหม่

## เวลาในเครื่องนี้

- 156 เคส sequential r55.6: median 0.571s, P95 1.729s, max 13.144s
- subset ปุ่ม/กฎ r55.7: median 0.801s, max 2.262s
- followups/pages r55.7: median 0.397s, P95 0.746s, max 3.022s

เป็นเวลาบนเครื่องนี้หลัง warmup แบบ sequential และ query set เฉพาะ ไม่ใช่ SLA หรือผลใช้พร้อมกันหลายคน กฎที่ต้อง retrieval/LLM จริงและ WordPress network ยังมี latency เปลี่ยนตามภาระ

## สิ่งที่ยังยืนยันเองไม่ได้ และคำถามที่ต้องถามเจ้าของ

1. **ราคา non-PC:** ตารางเดิมมีผลถึง 31 มีนาคม 2026 อัตราปัจจุบันเหมือนเดิมหรือไม่? มีผลเริ่ม/สิ้นสุดเมื่อใด และอนุมัติข้อความราคาใด?
2. **เปลี่ยนวันเมื่อจ่ายแล้ว:** ข้อ 45 อนุญาตเปลี่ยนวันเมื่อจองผิดวัน แต่ข้อ 46 ไม่อนุญาตเลื่อนแทนคืนเงิน แยกสองกรณีอย่างไร? ติดต่อช่องทางใด ต้องแจ้งล่วงหน้ากี่ชั่วโมง?
3. **เงินสด/ค่าจอดรถ/คนดู:** รับเงินสดหรือไม่? ที่จอดรถและนั่งดูเพื่อนมีค่าใช้จ่ายหรือไม่? เงื่อนไขเป็นอย่างไร?
4. **บัญชีเกม/ติดตั้ง:** ต้องใช้ Steam/บัญชีส่วนตัวหรือมีบัญชีศูนย์? ขอเพิ่มเกม/ติดตั้งเอง/mod/โปรแกรมได้ไหม ใครเป็นผู้ทำ?
5. **เด็ก/อุปกรณ์ส่วนตัว/สตรีม:** อายุขั้นต่ำและผู้ปกครอง? จอยส่วนตัว/กล้อง/การสตรีมและถ่ายภาพอนุญาตในกรณีใด? (keyboard/mouse มีคำตอบว่าไม่อนุญาตแล้ว ไม่ถามซ้ำ)
6. **เวลาเสียไป/สาย:** เกมอัปเดตหรือเครื่องค้างเริ่มนับเวลาเมื่อใด ชดเชยอย่างไร? มี grace period หรือข้อยกเว้นสาย 15 นาทีจากกฎเดิมหรือไม่?
7. **เช่าเหมา:** ครึ่งวัน/เต็มวันเป็นกี่ชั่วโมง เริ่ม/จบเวลาใด? ใช้วิธีจอง/ชำระเงินเดียวกับรายเครื่องหรือไม่? ราคาใน workbook มี validity เมื่อใด?
8. **กฎและปุ่ม:** เอกสาร rulebook ที่ใช้เป็นฉบับที่จะให้ตอบในการแข่งขันครั้งถัดไปหรือไม่? ข้อยกเว้น pause ของ Tekken ใช้อย่างไร? ปุ่มแหล่งรองตรงกับเกม/เครื่องที่ศูนย์ตั้งค่าจริงไหม?

ระบบตอบส่วนที่มีหลักฐานก่อน และระบุเฉพาะ field ที่ยังไม่ยืนยัน ไม่สร้างนโยบายจากการอนุมาน คำถาม owner pending ไม่ได้ขัดขวางการใช้ส่วนที่แก้แล้ว

## งานเทคนิคที่ยังติดตามได้โดยไม่ต้องให้เจ้าของตอบ

- ขยาย semantic oracles ของ REVIEW 47 ข้อจาก source ไม่ใช้ชื่อเกม/เลขเพียงอย่างเดียว; r55 เพิ่ม regression สำคัญแล้ว แต่ชุดนี้ยังไม่ได้พิสูจน์ทุก wording
- คำถามหลายส่วนเกิน 3 ส่วนและการปฏิเสธ/เปรียบเทียบซับซ้อนยังไม่ได้ตรวจครบ ไม่ควรแก้ grammar กว้างจากตัวอย่างเดียว
- ตรวจใหม่เมื่อเปลี่ยน corpus/models/worker policy; รอบนี้ไม่ได้เพิ่ม model concurrency หรือทำ load test r55
- อัปเดต portable packages สองชนิดด้วย version/hash ใหม่เมื่อจะนำแจก; candidate นี้อาศัย runtime/model ที่มีในเครื่อง จึงไม่ใช่แพ็กเกจแจกใหม่
- Git checkout ยังขึ้น fatal ที่ path Learn-LLM; เก็บ snapshot/diff แล้ว ไม่ reset/clean หรือซ่อม metadata ของ Git โดยเดา

## ไฟล์หลักฐาน

FLOW_FINAL.md, SUMMARY.json, ALL_QUESTIONS_ANSWERS_TH.md, web_final6.json/raw.jsonl, controls_final7.json/raw.jsonl, near_final7.json/raw.jsonl, units_final8.txt/json, final7_PRESERVATION_AUDIT.json, final7_SOURCE_CHANGES.patch และ HANDOFF_R55.md
