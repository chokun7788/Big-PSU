# ตรวจทานแผนรวม R102 ก่อนเริ่มพัฒนา

วันที่ 20 ตุลาคม 2026 — เป็นการตรวจเอกสารและสัญญาที่ออกแบบ **ไม่ใช่ผล runtime หรือ chatbot tests**

## รอบ A — ความครอบคลุม

- เทียบ R97 stages/contracts กับ Flow หลัก: มี input/context/state/planning/read/evidence/dependencies/render/verification/snapshot/delivery/audit
- ดึง C01–C37 จาก spec เดิมมาใส่ matrix พร้อม preconditions/expected invariant และขั้นที่เกี่ยวข้อง ไม่เปลี่ยน executed flags เดิม
- ดึง task table จาก R101 ได้ 32 tasks และ catalog ได้ 24 kinds ระบุ acceptance ของ reader/render/lifecycle เพิ่ม ไม่ใช้การมีชื่อใน registry เป็นหลักฐานว่าทำแล้ว
- ปิดช่องว่างที่มีรายงานแล้ว: FAQ detail undercoverage, cross-source conflicts, targeted gaps, mixed whole-request planning, actual live lane และ final batch attribution

## รอบ B — Failure paths และขอบเขตความเชื่อถือ

พบทาง corrective read กับ coherent reread ที่อาจถูกอ่านเป็นสองโควตา แก้เอกสารให้ใช้ ledger เดียวรวมไม่เกินหนึ่งครั้ง

ตรวจว่าราคา unknown/expired ไม่ใช้ derive budget, conditions unknown ไม่กลายเป็น permission, booking empty ไม่กลายเป็น physical closed, unknown mapping ไม่กลายเป็น free, typed source gap ไม่เรียกโมเดลเปลี่ยนเรื่อง และ supported independent need ยังส่งได้เมื่ออีก need ล้ม

ตรวจว่าความขัดแย้งต้องมี overlapping applicability; ข้อความคนละ actor/date ไม่ใช่ conflict โดยอัตโนมัติ possible conflict ของ FAQ ที่ยังไม่มี mapping ไม่ถูกอ้างว่า contradiction confirmed และไม่ปิด unrelated needs

## รอบ C — Interfaces และวิธีตรวจรับ

เดิมร่างเปิดตัวเลือก optional extension หรือ companion sidecar ไว้ จึงปิด design decision เป็น record-level claim_bindings ที่ผูก revision/source/approval/release เดียวกัน รองรับ schema เก่าโดยไม่แก้ approved hash ไม่มีฐาน claim ที่เผยแพร่หลุดออกจาก release

ตรวจว่าการเพิ่มชื่อใหม่ใน kind เดิมไม่ต้องเพิ่ม regex และสูตรใหม่ที่ไม่รองรับต้องได้ capability error ตรวจว่าคำตอบภาษาอังกฤษใช้ claims เดียวกับไทยโดยคง critical slots

แยกจำนวน scenario variants, unique request keys, conversation turns, assertions และ model calls; ขนาด 444 variants เป็น design target ของ lane R97 ไม่ใช่ผลทดสอบหรือจำนวน jobs สุดท้าย การนับจริงและ oracle จะตรึงก่อน batch

Batch เดียวต้องตรวจ strict-grade changes ทุกประเภทด้วย เพราะ R101 เคยพบบั๊ก opening→lost-property เฉพาะเมื่ออ่าน strict regression ไม่ใช่อ่าน positive content score อย่างเดียว

## สถานะที่ยังไม่กล่าวอ้าง

แผนรวมถูกเขียนและตรวจทานเอกสารแล้ว แต่ implementation paths/case IDs ของ R102 ยังต้องใส่หลังพัฒนา runtime และ runner ไม่ยืนยัน exact acceptance 37 ข้อผ่าน ไม่ยืนยัน live connection จริง ไม่สร้าง approvals จริง และยังไม่เปิด full/integrated test

เอกสารหลัก: [FULL_FLOW_TH.md](FULL_FLOW_TH.md) · รายการครบ: [COVERAGE_MATRIX_TH.md](COVERAGE_MATRIX_TH.md) · สถานะเครื่องอ่าน: [FLOW_COVERAGE_PLAN.json](FLOW_COVERAGE_PLAN.json)
