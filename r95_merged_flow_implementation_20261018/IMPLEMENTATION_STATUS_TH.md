# R95 — สถานะพัฒนาและการทดสอบ Flow รวม

18 ตุลาคม 2026 · เริ่ม full test เวลา 23:01 น. ไทย · **ยังไม่ถือว่าผลเต็มเสร็จจนมี FULL_TEST_COMPLETE.json และรายงานจากผลครบ**

## สิ่งที่ลงมือแล้ว

- Shared normalization ก่อน common routing: raw text, offsets, edits, protected spans, discourse/polite-prefix recovery ไทย/อังกฤษ
- Runtime task registry 32 contracts รวม explicit schema-attribute task ที่ใช้กับ kinds จาก catalog
- Task-first selection แยก entity/task/fields และ bounded semantic task proposal พร้อม raw quote checks และ typed qualifier gates
- แยก common `execute_task` จากตัวตีความ แล้วให้เส้นทางใหม่และ compatibility ใช้ evidence/projection/billing/controls/relations/validation เดียวกัน
- Explicit unknown/withdrawn handling ไม่คืน facts จาก state/ฐานเก่า
- กลุ่มนักศึกษามหาวิทยาลัยอื่นใช้ general-student concept จากชื่อกลุ่มที่มี ไม่เดาราคาใหม่หรือยืด expiry
- Projection คำถามโซนของอุปกรณ์เลือก source-declared zone โดยไม่แสดง specs ทุกช่องแทนโซน
- คง owner preview/published providers/revision/approval และ readiness เดิม ไม่อนุมัติข้อมูลจริงโดยอัตโนมัติ
- Trace แยก shared normalization, task acceptance, executor และ compatibility paths
- ตัววางแผนใช้ context 3072 เหมือนเส้นทางโมเดลเดิม ลดการเรียกโมเดลก่อนทราบว่าต้องใช้ typed qualifier path

ไฟล์แอปเดิมที่แก้ 4 ไฟล์ + โมดูลใหม่ 4 ไฟล์ อยู่ใน `system/` ของ R95 แยกจาก R78 ที่ผู้ใช้เปิดอยู่ รายการและ diff อยู่ IMPLEMENTATION_MANIFEST.json / CHANGESET.diff

## สิ่งที่ยังใช้ของกลางเดิมอย่างตั้งใจ

ราคา/เหมา/budget/กติกาและ qualified policies หลายส่วนยังใช้ domain parser เดิมที่มี business constraints ผ่าน compatibility routing และ executor ร่วม ไม่ได้อ้างว่าเปลี่ยนทุกหมวดเป็น generic LLM task interpreter ครบแล้ว

การนำตัวอ่านที่ดีมาใช้ตาม R94 rollout plan ไม่ได้ลบปัญหาที่ยังเหลือ เช่น expired rates, unsupported business qualifiers, rule compare presentation, source/GT wording differences หรือ semantic acceptance ที่ยัง conservative ต้องอ่านผลใหญ่และแยกสาเหตุอีกครั้ง

## ผลตรวจที่บันทึกก่อน full

| ชุด | ผล | ขอบเขต |
|---|---:|---|
| release_gate | 20/20 | engine จริง เปิด LLM รวม wrapper/typo/role/zone regressions และ follow-up บางแบบ |
| contracts02 | 65/65 | wording/negative task contracts, readiness, snapshot, preview; ไม่ใช่ 65 คำถามผู้ใช้ทั้งหมด |
| owner02 | 13/13 | synthetic isolated create/edit/publish/withdraw; ไม่ใช่ real owner approvals |
| existing01 | 19/19 | isolated rental/current-source/revision/no-legacy-fallback fixture; transport ถูกควบคุม |
| competition01 | 7/7 | isolated edited/new/withdrawn rule clauses ไทย/อังกฤษ; transport ถูกควบคุม |
| gate03 | 80 requests / 231 grades ครบ | 0 exceptions, 0 HTTP-open failures ใน 29 attempts; ไม่ใช่ full accuracy |

gate03 ผ่าน positive text/clause 87/120 (72.50%) และไม่พบ request ที่ R88 ผ่าน positive ทุกข้อแล้วมาตกในชุดนี้ ตัวเลขนี้เป็นเพียง gate cohort ไม่ใช้เทียบกับคะแนน full หรือ sample 1,000 โดยตรง

รอบที่พบข้อผิดพลาด focused01, owner01, gate02 และ timeout ใน gate01 เก็บไว้ ไม่ลบหรือเปลี่ยนผลแรก release_gate จึงไม่ใช่ผลครั้งแรกของทุกเคส

## Full ที่เริ่มแล้ว

- เฉพาะ common Flow ใหม่ R95 + LLM ON ไม่บังคับทุกคำถามให้เรียกโมเดล
- 20,554 unique request keys / 55,811 grades ครบ population เดิม
- ภาษาไทย อังกฤษ และ auto ตาม jobs เดิม
- 4 evaluator processes ใช้ shared model slot 1 ช่อง; ไม่ใช่ข้อสรุป load capacity ของเว็บ
- เวลาอ้างอิง 16 ต.ค. 2026 พร้อม per-job overrides ตาม baseline เพื่อเทียบผลที่เก็บไว้
- Booking ถูกควบคุม unavailable ตาม baseline ไม่มี live occupancy oracle
- ไม่มี histories ใน full population; owner/multi-turn fixtures แยกรายงาน
- เปรียบเทียบกับ R88 ที่เก็บไว้ และ cohort R93 เดียวกัน ไม่รันระบบเก่าซ้ำ

Supervisor รันแยกเบื้องหลัง ตรวจ coverage/hash และสั่งวิเคราะห์หลังจบโดยอัตโนมัติ:

- `SUPERVISOR_STATUS.json` — สถานะล่าสุด running/analyzing/completed/failed
- `full01/PROGRESS.json` — จำนวนเสร็จ/ทั้งหมดและเวลาโดยประมาณซึ่งยังเปลี่ยนได้
- `FULL_SOURCE_MANIFEST.json`, `FULL_CONFIG.json` — โค้ด/ข้อมูล/เวลา/ขอบเขตที่ตรึง
- `FULL_RUN_STDOUT.log`, `FULL_RUN_STDERR.log`, `SUPERVISOR_EVENTS.jsonl` — log รอบใหม่
- `FULL_TEST_COMPLETE.json` — สร้างเมื่อ coverage ครบ 20,554/55,811 และวิเคราะห์สำเร็จเท่านั้น ไม่แปลว่าคำตอบถูกทั้งหมด
- `full_analysis/FINAL_REPORT_TH.md`, `ANALYSIS_FINAL.json`, `PER_REQUEST_ANALYSIS.jsonl` — จะสร้างหลังรันครบ

ถ้า supervisor ล้ม ดู SUPERVISOR_FAILURE.log โดยไม่เริ่ม full ซ้ำทับผลเดิม หาก coverage ยังไม่ครบห้ามเรียกว่าทดสอบเสร็จ

## การรักษาของเดิมและสถานะติดตั้ง

ฐานข้อมูล facts ของ candidate ยังมี hash เท่า source เดิม ไม่แก้ราคา นโยบาย owner approvals หรือ archived results การเปลี่ยนแปลงอยู่ R95 เท่านั้น

**ยังไม่ได้ติดตั้ง R95 ทับ R78 หรือ rebuild portable package** เพราะกำลังประเมินรุ่นที่ตรึงไว้ การทดสอบเต็มวัด candidate นี้โดยตรง ไม่ใช่เว็บ R78 เดิมที่เปิดค้างอยู่

แผนปรับปรุงที่เติมหลังทบทวน R94 อยู่ FLOW_REVIEW_ADDENDUM_TH.md ส่วน R94 เดิมเก็บไว้ตามเดิม
