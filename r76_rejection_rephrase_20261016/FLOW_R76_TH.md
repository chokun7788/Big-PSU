# Flow R76 — ปฏิเสธหัวข้อเก่าและถามใหม่ในข้อความเดียว

## เป้าหมาย

ต่อจาก R75 ที่ `No, I mean how do I pay?` และ `ไม่ใช่ครับ หมายถึงจ่ายค่าจองยังไง` ถูกปิดเป็น cancel แล้วขอให้ถามใหม่ ทั้งที่ข้อความมีคำถามใหม่ครบอยู่แล้ว

ทำในสำเนา R76 ไม่แก้ facts/schema/query_profile/approvals/validity ของข้อมูลเดิม ไม่เขียนทับ log เก่า ทดสอบ common format เปิด LLM เฉพาะส่วนเกี่ยวข้อง ไม่รัน full/legacy/OFF

## ขั้นตอน

1. เก็บสำเนา code/DB และ source manifest จาก R75 ใช้ SQLite backup เพื่ออ่านฐานที่สอดคล้องกัน
2. รับการแก้คำถามเฉพาะเมื่อมี pending topic ล่าสุดจาก server history ที่ส่งแล้ว ไม่ใช้ assistant text หรือ client-supplied state เป็นข้อเท็จจริง
3. ตรวจ rejection ที่ต้นข้อความ เช่น no/nope/not that/ไม่ใช่/ไม่มีในนี้ ถ้าเป็น no ภายใน proposition เช่น `No refund is needed` หรือ `ไม่ใช่แค่ราคา` ต้องไม่ตัดทิ้งเป็น acknowledgement
4. แยกคำเชื่อม `I mean`, `I meant`, `I'm asking about`, `หมายถึง`, `ขอถาม` ออกจาก replacement query โดยใช้ raw substring ไม่ normalize แล้วเขียนประโยคใหม่ ห้ามลบ not/ไม่/ตัวเลข/วัน/เวลา/ชื่ออุปกรณ์ในเนื้อหาใหม่
5. ถ้าไม่มีเนื้อหาใหม่ ให้ cancel ตามปกติ ถ้าข้อความมี replacement ให้ตั้ง declined IDs จากหัวข้อที่แสดงอยู่ และสร้าง context barrier ที่ไม่มี factual answer text
6. ส่ง replacement ผ่าน dispatcher ปกติอีกครั้ง ด้วย locale และ LLM flag เดิม เพื่อให้ทั้ง static knowledge/live adapter/validation ทำงานกับคำถามใหม่
7. ตรวจ product scope ของ replacement ซ้ำ เพราะข้อความต้นทางเริ่มด้วย no อาจทำให้ตัวตรวจ write/translate/out-of-scope ที่ต้นประโยคเดิมไม่เห็น ห้ามตอบเรื่องนอกข้อมูลร้านเกมด้วย general generation
8. ไม่ใช้ pending/ราคา/อุปกรณ์จากหัวข้อเก่ามาเติมคำถามใหม่เอง กรณี replacement เป็น fragment ที่ยังไม่ชัดให้ถามเฉพาะที่ขาด ไม่แต่งเป็นคำถามเต็มจากความจำ
9. กรอง declined profile IDs ออกจาก semantic candidates และเมนูหัวข้อใหม่ ไม่ถือว่าเป็นการถอนข้อมูลจริง หากผู้ใช้ระบุคำถามใหม่ด้วย task/subject ชัดแบบ direct จะใช้ source ได้ตามปกติ
10. หากยังตอบไม่ได้ ให้เก็บ declined-topic barrier ต่อใน server state เพื่อไม่วนเสนอเรื่องเดิมหลัง generic fallback หากได้ source answer ใหม่สำเร็จให้ใช้ context ใหม่สำหรับข้อความสั้นถัดไป เช่น `And when?`
11. เก็บ trace `dialogue_repair`: original_input, active_query, rejected IDs และยืนยันว่าไม่ใช้ previous answer facts/old context ส่วน facts ยังอ่านจาก DB ฉบับปัจจุบันทุกครั้ง
12. ทดสอบ raw parser, paired conversations ไทย/อังกฤษ, negation, short follow-up, repeated unknown, source update/withdraw, scope, live fixture และ actual HTTP handler แบบ memory แยกจาก model accuracy/TCP/WordPress สด
13. เปรียบเทียบ baseline ของคำถามเดิมก่อนแก้ เก็บทุก round และตรวจ source manifest/logical tables ก่อนส่งรายงาน

## การทบทวนสามรอบและสิ่งที่ปรับ

### รอบ 1 — ไม่ทำคำปฏิเสธในประโยคใหม่หาย

ไม่ใช้การลบคำว่า no/ไม่ ทุกตำแหน่ง จำกัด acknowledgement ที่ต้นข้อความและมีรูปแบบแยกชัด `No refund is needed` และ `ไม่เอาเลขบัญชี` ต้องคงเดิม ส่วนคำปฏิเสธหลัง I mean ต้องอยู่ครบใน active_query

### รอบ 2 — ไม่ตัดเส้นทาง live หรือขอบเขตผลิตภัณฑ์

การเรียกเฉพาะ CommonAnswerer ซ้ำจะไม่ถึง live adapter และข้อความนอกเรื่องอาจข้าม scope guard จึงให้ replacement ผ่าน dispatcher ปกติ พร้อมตรวจ product scope ซ้ำ และเก็บ trace ของตัวอ่านข้อมูลภายใน ไม่เขียนทับด้วย trace ว่างจาก wrapper

### รอบ 3 — ไม่ลืมสิ่งที่ปฏิเสธเมื่อยังไม่มีคำตอบใหม่

รอบแรกของ harness หยุดเมื่อ fallback ไม่มี common_read_state การตรวจนี้พบด้วยว่าถ้าไม่เก็บ declined IDs ต่อ fallback จะทำให้วงจรคำถามถัดไปวนกลับหัวข้อเดิมได้ เพิ่ม state barrier ที่ไม่มี answer facts สำหรับกรณี unresolved และ clear เมื่อมี context ใหม่ที่ตอบจาก source แล้ว

## เกณฑ์ผ่านและสิ่งที่ไม่อ้าง

- คำถามใหม่ที่มีข้อมูลต้องได้เนื้อหาที่ควรตอบ ไม่ผ่านเพียงเพราะห้ามมีข้อความเก่า
- Unknown policy ต้องแจ้งเรื่องที่ยังยืนยันไม่ได้ ไม่รับปากกฎใหม่
- Source revision ใหม่ต้องถูกอ่านและข้อมูลที่ถอนแล้วต้องไม่กลับมา
- การเชื่อมต่อ live fixture หรือ HTTP handler ใน memory ไม่ใช่สถานะ WordPress/TCP/browser จริง
- การเปิด LLM และใช้ controlled transport ไม่ใช่การรับรองความแม่นของโมเดลหรือเวลาตอบจริง
