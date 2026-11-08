# R97 — Flow กลาง V2 หลังทบทวน R96

วันที่: 19 ตุลาคม 2026 เวลาไทย

**สถานะ: ออกแบบและตรวจความสอดคล้องของเอกสาร ยังไม่ติดตั้ง runtime หรือทดสอบคำตอบรุ่นใหม่**

## เริ่มอ่าน

1. [จุดบกพร่อง R96 และการปรับ 18 จุด](01_R96_GAP_REVIEW_TH.md)
2. [Flow กลาง V2 ฉบับละเอียด](02_FLOW_V2_TH.md)
3. [ลำดับลงโค้ดและเกณฑ์ตรวจรับ](03_IMPLEMENTATION_AND_ACCEPTANCE_TH.md)
4. [สัญญา Flow และ 37 review scenarios](FLOW_SPEC.json)
5. [ผลตรวจความสอดคล้องของเอกสาร](DOCUMENT_QA.json)

## สิ่งที่พัฒนาจาก R96

- เพิ่ม candidate discovery ก่อนให้ planner เลือก task/record
- ให้ทุกหมวดใช้ RequestPlan และ NeedResult เดียวกัน พร้อม slots/qualifiers ที่มี origin
- รองรับคำถามหลาย subject แม้เป็น task เดียว และคำถามผสม rules/live ผ่านแผนร่วม
- แยก required claims, optional context และ alternative read branches
- ให้ “ทั้งหมด” ใช้ exhaustive scope query พร้อมหลักฐานความครบ
- รักษา pending task เมื่อผู้ใช้ตอบสั้น และอ่าน facts revision ใหม่โดยไม่ถาม slot เดิมโดยไม่จำเป็น
- แยก known empty, unknown, opening, bookability และ live occupancy
- เพิ่ม claim-level authority, dependency checks และแผนเปลี่ยน early-return ownership

## ใช้หลักฐานเดิมอย่างไร

ใช้ผลและการค้น paper ของ R96 กับโค้ด R95 ที่อ่านเพิ่ม ไม่มีการค้น paper ใหม่ ไม่มีการรัน chatbot/LLM/full test และไม่มีคะแนนใหม่

สิ่งที่ runtime มีอยู่แล้ว เช่น schema/source checks, pinned snapshots, request budget และบาง follow-up guards ถูกระบุให้ใช้ต่อ ไม่กล่าวว่าไม่มีอยู่ทั้งหมด

ไฟล์ `READ_ONLY_SOURCE_MANIFEST.json` เก็บ hash ของเอกสาร/โค้ดอ้างอิง; `prepare_design_spec.py` สร้าง design JSON และตรวจ IDs, graph reachability, kind coverage และ local links เท่านั้น ผล PASS ไม่หมายความว่า chatbot ตอบ 37 scenarios ผ่านแล้ว
