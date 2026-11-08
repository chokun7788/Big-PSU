# บันทึกตรวจทานและปรับปรุง Flow

วันที่: 5 ตุลาคม 2026  
ขอบเขต: ตรวจการออกแบบและเอกสาร ไม่ใช่การรัน chatbot หรือการรับรองข้อมูลศูนย์

## รอบ 1 — ตรวจร่างกับปัญหาที่พบจริง

อ่านร่าง v1 เทียบรายงานสาเหตุและ code hooks ที่ตรวจในรอบนี้ พบว่าร่างยังระบุเพียงขั้นตอนโดยไม่มี ownership/lifecycle และไม่แยกความหมายของ all/coverage เพียงพอ

| จุดที่ยังไม่พอ | สิ่งที่เติมในฉบับสุดท้าย |
|---|---|
| State มีแต่รายการ field ไม่มีผู้ถือ state | parent HTTP process ถือ state ภายใต้ session lock ส่ง plan ให้ worker |
| pending อาจหายเมื่อ timeout | transition table เก็บ target ที่เติมแล้ว แยกจาก delivered |
| all ไม่ระบุมิติ | services/packages/facets/task scope และกรณีขาดหลายช่องต้องถาม |
| external อาจเป็นอัตราเดียวโดยเดา | external scope แสดงกลุ่มที่เกี่ยวข้องโดยไม่รับรอง entitlement |
| coverage อาจคำนวณจาก retrieval hits | requested/documented/usable แยก และ expected IDs มาก่อน retrieval |
| summary ถือว่ารายละเอียดครบ | ledger แยก summary/detail/source release |
| หลายงานหรือหลายระยะเวลาไม่ชัด | task list และ per-target filters; partial outcomes |
| วิธีโมเดลและ general classification กว้างเกิน | structured patch + schema/IDs/negation guard และ general policy เดิม |
| ขอบการแก้โค้ดไม่ระบุ | A/B/C implementation stages พร้อมไฟล์และหลักฐานเสร็จ |
| test มีแต่ประโยคตัวอย่าง | 32 scenario families และ semantics/source/locale/time criteria |

ผล: ขยายร่างเป็น Flow ที่มี schema, decision tables, integration mapping และ acceptance specification ยังไม่ได้อ้างว่าโค้ดรองรับ schema แล้ว

## รอบ 2 — ตรวจ failure ระหว่างงานและผลที่ผู้ใช้เห็น

อ่านฉบับละเอียดและไล่กรณี partial send, retry, model timeout, source change และงานเปรียบเทียบ พบจุดที่ยังทำให้ผลลัพธ์ผิดได้ แล้วแก้ในเอกสารดังนี้:

| จุดเสี่ยง | การปรับที่ทำแล้ว |
|---|---|
| server เขียน response แล้วถือว่าคนเห็นครบ | prepared/server_written/client_acknowledged/uncertain, last_seen_response_id และ legacy fallback |
| retry ใช้ turn ID เดิมแต่ข้อความคนละคำถาม | session + turn ID + fingerprint conflict check |
| parent เรียกโมเดลแล้ว worker เริ่ม quota ใหม่ | shared request call budget และ remaining time ข้าม supervisor |
| ไม่ทราบจำนวนส่วนแต่บอกส่วน 1/3 | ระบุจำนวนส่วนเฉพาะเมื่อคำนวณได้จริง |
| เก็บว่าเครื่องเคยว่างแล้วใช้ต่อใน turn ใหม่ | static ledger แยกจาก fresh snapshot ที่ต้อง fetch ใหม่ |
| บาง task ผ่านแล้วสรุปเปรียบเทียบโดยอีก task ล่ม | dependency/snapshot constraints และแยก facts จาก comparison conclusion |
| warning typo ทำให้ context หาย | warn-and-continue ไม่ล้าง accepted state เมื่อ plan ผ่าน guard |

ผล: เพิ่มข้อกำหนดในหัวข้อ 5, 6, 7, 9, 14 และรายการปรับปรุงท้าย Flow ไม่มีการเปลี่ยน source data หรือ runtime

## รอบ 3 — ตรวจความครบ ความสอดคล้อง และโครงสร้างเอกสาร

รายการตรวจ:

- รูปแบบ state เป็นข้อเสนอ ไม่เรียกว่าพัฒนาหรือผ่านแล้ว
- PC/all เติม pending ตามหมวดเดิม; ไม่มี state หรือมีหลายมิติยังถามได้ตรงจุด
- offered options ไม่กลายเป็น explicit selection
- topical shift ไม่ติดราคา และ corrected/negated filters ชนะบริบทเก่า
- external group set ไม่กลายเป็นสิทธิ์รายบุคคล; stale price ไม่เป็น current price
- live fetch ใช้ configuration ปัจจุบัน ไม่บังคับ Dashboard จากเอกสารเก่า
- continuation รักษา target, detail level, source release และยืนยันสิ่งที่ส่ง ไม่ใช้ static status อ้างสด
- worker restart/late response/retry ไม่ commit state ผิด revision
- model interpretation/composition ใช้ deadline และ budget ร่วมกัน
- legacy API ยังมีทางใช้งานระหว่าง migration; competition guards เดิมมี adapter ไม่ถูกลบทิ้ง
- tests แยก paired TH/EN, development/holdout, auto checks/human review/owner sign-off
- เพิ่ม temporal anchor/reference clock ให้ relative date และคำถามข้ามเที่ยงคืน ไม่สืบทอด timestamp ว่าเป็นสถานะสด
- ลิงก์ไฟล์อ้างอิงอยู่จริง code fences ปิดครบ JSON ตัวอย่างอ่านได้ และ scenario IDs C01–C32 ไม่ซ้ำ

ผลตรวจโครงสร้างบันทึกใน `DOCUMENT_CHECKS.json` แล้ว: ลิงก์อ้างอิง 4 จุดอยู่จริง, code fences ปิดครบ, JSON ตัวอย่างอ่านได้, C01–C32 ครบและไม่ซ้ำ, หัวข้อ 0–20 ครบ และ hash ของไฟล์โค้ดที่ตรวจ 6 ไฟล์ยังตรงเดิม ผลนี้ยืนยันเฉพาะเอกสาร ไม่ใช่ผลระบบตอบคำถามผ่าน

## ข้อจำกัดที่คงไว้โดยตั้งใจ

- ยังต้องพัฒนา state store, pending schema, plan adapters, filtering และ contracts จริง
- ยังต้องวัด threshold/TTL/budget consumption จากเคสและ holdout ก่อนกำหนดค่าใช้งาน
- ราคาปัจจุบันยังต้องมีหลักฐานต่ออายุ/อัปเดตจากเจ้าของ; การพัฒนา context ทำต่อได้
- ยังไม่มี actual trace ที่ตรงภาพ จึงไม่อ้างคะแนนจริงหรือ stage timings ของคำขอในภาพ
- ชุด 32 scenarios เป็นข้อกำหนดตรวจหลังพัฒนา ยังไม่ใช่ 32/32 ผ่าน
- หาก manifest ข้อมูลไม่ครบ ต้องบอกว่า completeness ยังตรวจไม่ได้ ห้ามลด denominator เพื่ออ้างครบ

ฉบับส่งมอบ: [FLOW_CONVERSATION_RELIABILITY_FINAL.md](FLOW_CONVERSATION_RELIABILITY_FINAL.md)
