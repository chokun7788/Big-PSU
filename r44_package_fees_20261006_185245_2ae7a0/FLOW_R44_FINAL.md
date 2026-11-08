# Flow r44 ฉบับปรับปรุง: ราคาเช่าเหมาโซนจาก workbook

## ลำดับการทำงานและจุดตัดสินใจ

1. อ่านและสำรอง Excel ทุก sheet → ตรวจ merged headers B:C/D:E และหน่วย → เก็บ raw cells/source SHA256 → แมป B3:E8 เป็น 24 อัตรา และ F3:G8 เป็น capacity/equipment
2. สร้าง dataset ใหม่แยกจาก hourly fees; เก็บ field ที่ source ไม่ให้เป็น null; H3 เป็นโน้ตแถว All Zones
3. Parent ConversationStore รับคำถามและ last_seen_response_id → อนุญาตเฉพาะบริบทที่ client ยืนยันได้รับแล้วใน session เดียว → แยก rental task memory จาก hourly price memory
4. ถ้าคำถามกล่าวถึงเช่า/เหมา/rent หรือราคา half/full day → สร้าง zone_rental_v1; คำถาม hourly ธรรมดาหรือเรื่องเกม/กฎ/เวลาเปิดออกไป pipeline เดิม; venue เฉย ๆ ไม่เป็น rental
5. แยก targets/groups/periods/asks และ unknown nouns; service resolver fuzzy ที่มีอยู่ใช้แก้ชื่อสะกด โดยไม่เพิ่ม alias cockpik; ทั้งศูนย์คือ All Zones package แต่ทุกแพ็กเกจคือรายการทั้งหก
6. ถ้าไม่ระบุกลุ่ม/ช่วง แสดงทั้งสองกลุ่ม/ทั้งสองช่วงจากตาราง ถ้ามี unknown target ชัดเจนไม่แปลงเป็นทุกโซน; unknown + known แสดงส่วนที่ตอบได้และส่วนที่ยังไม่มีราคา
7. “PC/VR/ภายนอก/เต็มวัน/ทั้งหมด/รวมอะไรบ้าง” ต่อจาก rental ที่รับแล้ว → แก้เฉพาะ scope/field ที่กล่าวถึง; คงส่วนอื่นตาม plan; explicit resume ใช้ key zone_rental/zone_rental_fee
8. Validate typed schema → โหลด source JSON → render ภาษาเลือกโดยตรงจากตัวเลขตาราง → คืน source cell/hash และ requested-fields outcome; ค่า .99 คือ route priority ไม่ใช่ empirical certainty
9. Hourly rental/per-machine/booking/live rental availability/day definition/overtime/effective date/individual eligibility/multi-day ที่ไม่มีใน source → แจ้ง missing field; ไม่หารหรือคูณเป็นนโยบายใหม่ ไม่ยืนยัน live booking จากตารางราคา
10. บันทึก trace/task contract/resolved context/request plan/output/session และรอ delivery acknowledgement; logs ไม่ถูกรีเซ็ต

## Gates และการปรับแก้ตามผล

- Unit oracle เปิด archived XLSX XML โดยตรงแล้วเทียบทั้ง cell mapping และค่า; ไม่ใช้ normalized JSON เป็น expected output
- Source probes แยก transport / chosen operation / returned rate IDs+values / missing fields / rendered amounts / TH-EN / source SHA / validation
- Negative cases hourly/topics/venue ใช้ตรวจไม่ให้ rental ยึดเส้นทางอื่น; ไม่ถือว่า non-rental อัตโนมัติเท่ากับคำตอบเดิมถูกต้องทุกด้าน
- แก้ unknown span false positives, ambiguous prefix/suffix, PC1, fuzzy leftovers, canonical hourly re-entry จากผล 71/80 → 80/80; เพิ่ม field followups จาก 9/16 → 16/16
- Freeze release ใหม่ทุกครั้ง .1/.2/.3/.4; ไม่แก้ bytes ใน candidate เดิม; หยุดเฉพาะ process รุ่นทดลองที่ตรวจ identity/parent แล้ว; รุ่นผู้ใช้เก่าและ logs เดิมเก็บไว้
- รุ่น .4 ผ่าน HTTP 103 cases/125 requests, unit 111 methods (19 ใหม่ + 92 เดิม); อัตรา source 24 ช่อง, parity 155 ไฟล์, hash source/protected/frozen ผ่าน
- ไม่ใช้ full 20k suite; ไม่รับรอง input ที่ยังไม่อยู่ในชุดทดสอบ; English venue location เป็น observed no-answer ที่ยังอยู่นอกการนำเข้าราคา

## ขอบเขตต่อไป

- เมื่อได้ข้อมูลจากเจ้าของ: เพิ่ม hours/effective dates/rental booking/overtime/eligibility ลง source ที่ยืนยันแล้ว และทดสอบ field-specific; ห้ามใช้ calendar มาคาดเดาการเช่าเหมา
- เมื่อแจกเครื่องอื่น: rebuild สอง distribution จาก source r44 พร้อม metadata/runtime/model compatibility และ verify บนเครื่องปลายทาง; ชุด local ปัจจุบันผูก interpreter เครื่องนี้
- คำถามหลายงานที่ใช้คนละโซน/ช่วง/กลุ่มในประโยคเดียวควรมี per-child rental task schema แทนการให้ dimensions ของหนึ่ง plan ขยายรายการแบบ Cartesian; เป็นการปรับต่อ ไม่ใช้ผล 103 cases มาอ้างว่ารองรับทุก compound scope แล้ว
