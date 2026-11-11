# ผลลงโค้ดคำตอบบางส่วนและงบเวลาวิเคราะห์

เป็น candidate แยกจากรอบ 2,111 ข้อที่วัดแล้ว ห้ามใช้เอกสารนี้อ้างว่าติดตั้งหรือแก้สาเหตุ model_transport_failure ครบแล้ว

- เพิ่ม cooperative analysis budget ค่าเริ่มต้น 20 วินาทีจาก request context และจำกัด gateway calls ครั้งละไม่เกิน 5 วินาที ปรับได้ด้วย PSU_ANALYSIS_BUDGET_SEC/PSU_ANALYSIS_CALL_SEC
- ลด admission wait ไม่เกิน 1 วินาทีและไม่เกินงบวิเคราะห์ที่เหลือ
- ก่อนเริ่ม gateway/admission ถ้างบหมดให้คืน budget error โดยไม่ส่ง HTTP
- หลังอ่าน deterministic tasks แล้ว งาน fallback ที่ค้างจะถูกข้ามเมื่อหมดงบ พร้อมข้อความเฉพาะส่วนว่าวิเคราะห์ไม่ทันเวลา งานพี่น้องที่มี source ผ่านยังถูก render/verify ตามเดิม
- ไม่ใช้คำตอบใกล้เคียงจากบริการอื่นและไม่เลี่ยง source rejection ส่วน compatibility ที่มีอยู่ยังใช้ verifier เดิม

ผลตรวจ: bounded_response_1794379987418247400 ผ่าน6 (fake clock, gateway, legacy admission และ natural typed price/booking ภายใต้งบศูนย์); expired_partial_1794380051262759900 ผ่าน3 (จำลอง booking pending, ราคา400ยังส่งได้, มี budget event และ disclosure); currency regression price_currency_1794380072425334000 ผ่าน12

ข้อจำกัด: ยังเป็น source-only/forced pending/fake clock ไม่ใช่ live slow model หรือ HTTP acceptance, socket timeout ไม่รับรอง absolute wall deadline, model server ต้องร่วมรักษางบด้วย, legacy callers ที่ไม่ผ่าน gateway ยังต้องตรวจ ไม่มี streaming หรือการส่งข้อมูลระหว่างที่ request ยังทำงานอยู่ เป็นการส่ง partial response ตอนจบรอบ request ยังไม่ได้เปิดใช้แทนแชตจริง

งานต่อ: ตรวจ admission และ gateway ด้วย HTTP ที่ควบคุมได้, ทดสอบ retained model จริงทีละคำถาม, ตรวจ source/target constraints และ timeout ของ task พี่น้องต่างชนิด แล้วค่อยพิจารณารวม candidate ข้อเท็จจริงที่ตรวจผ่านยังต้องไม่หายเมื่อ task อื่นล้ม
