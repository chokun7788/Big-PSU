# Flow ปรับการตอบคำถามต่อและความครบของคำตอบ — ร่างก่อนตรวจทาน

วันที่: 5 ตุลาคม 2026 / Asia Bangkok

## เป้าหมาย

รองรับรูปคำถามที่ต่างกันแต่มีเจตนาเดียวกัน เช่น ถามราคาภายนอกแล้วตอบ PC หรือทั้งหมด โดยรักษาหมวด บริการ กลุ่มผู้ใช้ และเงื่อนไขเดิม รวมถึงตอบหลายส่วนให้ครบและแยกคำถามทั่วไป

หลักฐานตั้งต้นคือ `analysis_20261005_screenshot_diagnosis/ANALYSIS_TH.md` และ `component_findings.json` เป็นผลอ่านโค้ดและตรวจแยกส่วน ไม่ใช่คะแนนจริงในภาพ

## Flow ตั้งต้น

1. รับข้อความ พร้อม session และประวัติที่มี
2. อ่าน active request และ pending slot
3. ระบุข้อความใหม่ว่าเป็น fill slot, expand scope, update filter, continue, new task หรือ topic shift
4. จับชื่อบริการ/เกมจาก catalog และใช้ local LLM ช่วยตีความเมื่อวิธีตรงยังไม่พอ
5. รวมเจตนาใหม่กับ request เดิม เก็บ provenance ของแต่ละ field
6. สร้าง Question Frame แล้วเลือกเครื่องมือ
7. ขยาย “ทั้งหมด” เป็นรายการ target/package/section ที่คาดหวัง
8. อ่านข้อมูลจาก source ที่ตรงเป้าหมายและมีวันที่
9. สร้างคำตอบแยกแต่ละส่วนตามคำขอ
10. ตรวจว่า returned IDs ครบ expected IDs และ filters ตรง
11. ส่งคำตอบพร้อมข้อจำกัด แหล่งข้อมูล และ coverage
12. บันทึก state หลังตอบและ trace แยกเหตุผิด แล้วตรวจชุดสนทนา TH/EN

## State ที่ต้องมี

- active domain และ operation
- targets / facets / scope
- filters: user group, duration, people, date, time
- pending slot และ offered option IDs
- source release
- answered IDs และ remaining IDs
- state revision / request ID

## ตัวอย่าง

| ประวัติ | ข้อความใหม่ | ผล |
|---|---|---|
| ราคา external, ขาดบริการ | PC | price_lookup external PC |
| ราคา external, ขาดบริการ | ทั้งหมด | price_catalog external all services |
| ราคา PC | แล้ว VR ล่ะ | price_lookup VR คงกลุ่มเดิม |
| ราคา PC | ไม่เอาราคาแล้ว จองยังไง | new reservation task |
| ไม่มีประวัติ | ทั้งหมด | ถามว่าทั้งหมดเรื่องใด |
| กติกา CS2 | ต่อ | ตอบส่วนที่ยังไม่ตอบของ CS2 |
| คำถามทั่วไปครบถ้วน | ไก่กับไข่อะไรเกิดก่อน | general policy ของระบบ |

## ลำดับพัฒนา

1. Session request state และตัวเติม pending slot
2. Scope/group filtering และ completeness contract
3. แยก general/unknown/ambiguous
4. Trace และ conversation regression
5. แพ็กเกจใหม่หลังตรวจเฉพาะจุดและ regression

## เงื่อนไขตรวจ

- ไม่ถามซ้ำหลังเลือก PC
- ทั้งหมดไม่หลุดจากราคาไปเกม
- ทุกแพ็กเกจและทุกส่วนที่ร้องขอมีคำตอบหรือบอกช่องว่าง
- ไม่ใช้ตัวเลือกในข้อความบอทเป็นการเลือกของผู้ใช้
- ไม่เลือกอัตรานักศึกษา PSU ให้บุคคลภายนอก
- ไม่รับรองราคาเก่าว่าเป็นปัจจุบัน
- ไม่ใช้คำตอบถามเพิ่ม/ไม่พบข้อมูลแทน semantic pass
- ไทยและอังกฤษมี target, numbers และ source เดียวกัน
- ไม่ปน session และไม่ทำให้ competition flow เดิมถอยหลัง

## จุดที่ต้องตรวจทานก่อนสรุป

- State อยู่ตรงไหนและใครเป็นผู้ commit เมื่อ worker มี timeout/restart?
- “ทั้งหมด” เติม service, group หรือ section อย่างไรเมื่อขาดหลาย field?
- จำนวน expected IDs มาจาก manifest หรือข้อมูลที่ retrieval หาเจอเท่านั้น?
- จะรองรับ legacy recent_history และคำตอบพร้อมหลายงานอย่างไร?
- LLM ตัดสินใจได้ขนาดไหน มี fallback และขอบเวลาหรือไม่?
- สถานะข้อมูลเก่า/ขาดคำแปล/แหล่งสดไม่พร้อมควรถูกนับอย่างไร?
- Cursor ต้องใช้ edition/release เดียวกันและชี้เฉพาะสิ่งที่ส่งสำเร็จหรือไม่?

ร่างนี้ยังไม่ใช่ฉบับพร้อมนำไปพัฒนา รายละเอียดข้างต้นต้องได้รับการแก้ในฉบับสุดท้าย
