# ผลวงรอบแก้ 01 — 12 พฤศจิกายน 2026

Parent: r135_shared_contract_20261111, commit99791918 ส่วนรายงานวิเคราะห์ log commit7341532b เก็บผลเดิมแยก ไม่แก้ owner/live/frozen/โมเดล

## สาเหตุร่วมและการแก้

กรณี `นักศึกษา PSU เล่น PC 30 นาที เสียกี่บาท` มีบริการ PC สอง record ของ audience เดียวกัน ทั้งสองบรรทัดตอบ0บาทสำหรับ30นาที แต่ตัวตรวจ duration เดิมรองรับเพียงหนึ่ง claim/หนึ่ง calculation จึงยังออกคำเตือนว่า30นาทีไม่ยืนยัน ทั้งไทย อังกฤษ และคำถามราคา+จอง ก่อนแก้ 3คำถาม/7checks มี3checksของ false notice ล้ม ขณะที่ราคาและขั้นตอนจองยังตอบได้

แก้ app เพียง `domain_flow/calculation_check.py`: สำหรับหลายบริการ audience เดียวและเป็น alternative unit rates ให้ตรวจ scope/audience จากคำถามและต้นทาง แล้วตรวจ claim/calculation/source arithmetic/revision/snapshot/receipts ของ **ทุกบรรทัด** ผ่านตัวตรวจ single-rate เดิม ก่อนประกอบเป็น duration proof ทั้งชุด หากบรรทัดที่สองผิดก็ไม่ให้ใช้บรรทัดแรกผ่านแทน

หลักการประยุกต์จาก PAL คือใช้ runtime/typed arithmetic ที่ตรวจกลับได้ แทนให้โมเดลรับรองตัวเลข; จาก selective QA คือรักษา normal positives พร้อม negatives ไม่แก้ด้วยการระงับทุกคำตอบ ข้อนี้เป็นข้อเสนอวิศวกรรมของเรา ไม่ใช่ implementation เต็มของ paper หรือผลที่ paper รับรองบน PSU

ไม่รวมราคาตัวเลือกเป็นยอดซื้อ ไม่เปิด multi-audience/multi-person total ด้วย proof นี้ ไม่ยกเลิกข้อจำกัดช่วงมีผล/authority และไม่เปลี่ยนตัวเลขราคาในข้อมูล

## ผลและตัวหาร

ดู LOOP01_MANIFEST.json สำหรับชื่อโฟลเดอร์และhashจริง:

- คำถามที่เคยล้ม 3คำถามหลังแก้ผ่าน7checks รวมไทย/อังกฤษ/booking sibling
- direct replay/mutation20checks ผ่าน: บรรทัดที่สองปลอมยอด/ราคา/ระยะเวลา/จำนวน/revision/scope/evidence, calculationหาย/ซ้ำ, claimเกิน, ผิดaudience/บริการ, total/multi-personที่proofนี้ไม่รองรับ, durationกำกวม, snapshotเก่า, rejected/fatal
- affected regression: matrix27คำถามเดิม, boundedbudget6checks, source/scope/edit/withdraw22checks, currency12checks ผ่าน
- แชตจริง candidate5คำขอเรียงทีละข้อผ่าน22assertions: ราคา0คงอยู่, false duration noticeหาย, วันที่ownerยืนยันยังแสดง, จองยังตอบ และunknown siblingไม่ถูกรายงานว่าครบ

67checks source/replay/regressionข้างต้น, matrix27คำถาม และHTTP5คำขอเป็นคนละตัวหาร มีการตรวจพฤติกรรมซ้ำ ไม่บวกเป็น accuracy หรือจำนวนข้อไม่ซ้ำ ไม่มี200/2111ใหม่

## ข้อจำกัดที่ยังอยู่

- ยังไม่แก้ root cause ของ timeout/cooldown และไม่พิสูจน์ hard cancellation
- partial notice ซ้ำและเกม/กฎ/ข้อมูลทุกชนิดยังไม่ได้ปิดครบจากแพตช์นี้
- proofหลายบริการใช้ scope/audience helpers ร่วมกับระบบเดิม จึงไม่ใช่ independently implemented semantic interpretation ทั้งชุด; ส่วนเลข Decimal/rate/rule ยังคงตรวจแยกจากselector
- ไม่ได้พิสูจน์ owner/editor HTTP lifecycle ของ multiple alternatives หรือการเปลี่ยนข้อมูลทุกชนิดจาก20mutations; source edit/withdraw22checksเป็น regression ของชุดเดิมตามขอบเขตของชุดนั้น
- ราคา alternative, หน่วยเรียกเก็บ, authority และช่วงมีผลต้องแยกจาก duration application ที่พิสูจน์ได้
- source-only checksห้ามเรียกโมเดล และ HTTPจริงไม่เท่ากับ semantic accuracy หรือ model availability acceptance
- รุ่นทดลองใช้port8144/versionR135-Recovery-loop01/DBของตัวเอง; parent8143และfrozenผลเก่ายังอยู่ ไม่ติดตั้งแทนproduction

ระหว่างเตรียมมีคำสั่งค้นไฟล์ใช้workdirผิดจึงไม่พบtestscript แก้pathก่อนใช้ ไม่ใช่Flowfailureและไม่รวมเป็นคะแนน การทดลองแก้appรอบนี้ไม่ได้เพิ่มnegativeหลังผ่านโดยไม่มีchange

งานถัดไป: audience typo/missing role กับ output completeness จากactual failure และ cooldown/deadline diagnostics ตาม RESEARCH_AND_LOOP_PLAN_TH.md
