# บันทึกตรวจทาน 10 มิติ r50

วันที่ 2026-10-09; นี่คือ 10 มิติที่ตรวจพร้อม feedback iterations จริง ไม่ใช่การอ้าง 10 cycles แก้โค้ด/ทดสอบเต็มชุด

| รอบตรวจ | สิ่งที่ตรวจ / สิ่งที่พบ | การปรับและหลักฐาน | ขอบเขตที่เหลือ |
|---|---|---|---|
| 1 Evidence | ข้อมูลจริง/อังกฤษผู้ใช้ยืนยันแล้ว; ห้ามนับเป็น test ใหม่ | USER_CONFIRMATIONS แยก human/auto | ยืนยันเฉพาะขอบเขตที่ผู้ใช้แจ้ง |
| 2 Source/locale | CS2 source มี 5; VAL roster ไม่มี; timeout TH ไม่ติด facet | source V1 15/22 → V2 22/22 | VAL team_size ยัง missing |
| 3 Scope | สมาชิกทีมติด guard; member groups ติด membership answer; Bangkok ติด Phuket parking | game/team count delegation, member directory delegation, location guard; r42 17/18→18/18 | ไม่ใช่ universal place resolver |
| 4 Completeness | API200/validationok อาจตอบคนละเรื่อง; unknown fields ห้ามเดา | assertion ตัวเลข/หมวด/source/required text; unknown typed answers | Oracle lexical+route ไม่เท่ากับ human audit ทุกข้อความ |
| 5 Context/ACK | ต้องกลับเรื่องชัดและใช้ ACK server history; compound คลุมเครือ | bounded return marker + polite followup; HTTP focused; parallel4 content/resolved/session ผ่าน | หลายหัวข้ออาจถามเพิ่มตาม ambiguity |
| 6 Persistence/TTL | memory เดิมไม่อยู่หลัง reboot; pending/live ห้าม replay | SQLite WAL/snapshot/TTL; unit12 ผ่าน | session เดิม/TTL1800/pathเดิม |
| 7 Restart/failure | sandbox temp test ใช้ไม่ได้; concurrent10 restart harness หยุด503 | fixture dirใหม่เก็บไว้; real reboot sequential10+fresh1=11/11; failed evidence เก็บ | ไม่อ้าง10 simultaneous restorationผ่าน |
| 8 Load/recycle | fast16 latestผ่าน; mixed8final PIDเปลี่ยน; threshold250 | เก็บ worker event; mixedconfirm ไม่มี PIDเปลี่ยน แยกcapacity/recycle | sustained/public/livebooking/unseenLLMยังไม่ได้วัด |
| 9 Package/preserve | long path/share hardlink sandbox buildแรกไม่สำเร็จ; READMEเก่าอ้างr37 | short pathใหม่, hashes+full data equality, READMEรุ่นใหม่; audit9existing+2new,data unchanged | coldmachinebootยังไม่ได้ทำ; partialfolderห้ามส่ง |
| 10 Acceptance | ทดสอบครบเฉพาะเกี่ยวข้อง; debugfalse contextfieldไม่ได้คืน | public oracle regrade, final docsแสดงทั้งfail/pass/limits | 6mixedเป็นhighesttestedไม่ใช่universalmaximum |

## ข้อผิดพลาดของเครื่องมือวัดที่เก็บไว้

- HTTP_PARALLEL_CONTEXT_R50.json ประเมิน 0/4 เพราะ oracle เรียก context_resolution ซึ่งไม่มีใน debug=false; คำตอบทั้ง4ถูกและ session/หัวข้อ resolved ถูก
- HTTP_PARALLEL_CONTEXT_REGRADED_R50.json ตรวจ evidence เดิมด้วย public contract: 4/4 ไม่มี rerun หรือแก้ network response
- ข้อมูล first restart concurrent ใช้ retrospective committed state เท่านั้น เพราะ harness แรกไม่มี HTTP error log ครบ; ไม่แต่งจำนวน/เวลา failed requests
- Package build แรกในโฟลเดอร์ลึกไม่สำเร็จ เก็บ partial folder; buildสำเร็จอยู่ short pathที่รายงานเท่านั้น
