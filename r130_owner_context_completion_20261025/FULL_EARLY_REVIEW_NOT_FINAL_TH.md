# บันทึกระหว่าง Full R130 — ไม่ใช่ผลครบหรือคะแนนสุดท้าย

อ่านเฉพาะ raw ที่เขียนเสร็จแล้วจากรอบเดียว ไม่รันคำถาม/โมเดลหรือ regrade baseline ใหม่ ไม่แก้ frozen runtime/inputs

## เหตุผลที่ strict ต่ำในช่วงต้น ต้องแยกก่อนอธิบาย

ตัวอย่าง raw ณ ประมาณ2,097requests พบ failure `route:knowledge expected:[...]` จำนวนมาก เพราะ routeของcommon previewเป็น `knowledge/common_read` แต่graderยังขอlegacycategories เช่นgames/service_fee/members/reservation/competition_rules แม้บางคำตอบมีข้อมูลที่ถามแล้ว ห้ามอธิบาย strict ที่ต่ำว่าเป็นsemanticผิดเท่ากันทั้งหมด และห้ามถือการแก้route labelว่าแก้content

## ตัวอย่างที่ต้องนำไปตรวจครบหลัง coverage

1. “Fortnite ราคาเท่าไหร่” — แสดงอัตราPS5แยกกลุ่มผู้ใช้พร้อมหน่วย60นาที แต่failทั้งrouteและmissing required Fortnite การไม่กล่าวชื่อเกมในคำตอบเป็นkeyword/presentation issue ต้องตรวจoffering relationและอัตราก่อนนับactualcontentfailure ไม่ตัดสินจากคำว่าmissingอย่างเดียว
2. “ใครเป็นประธาน” — มีชื่อ/ทีม/ตำแหน่งจากtypedpersonแต่routeเป็นknowledge จำแนกprotocol/category mismatchแยกจากความถูกต้องของคน/บทบาท/ช่วงเวลาpublic scope
3. “สอบถามครับ PC #10 มี TEKKEN 8 ไหม” — ตอบเพียงPC Zone/PS5 Zoneของเกม แต่ไม่ตอบresource PC#10 กรณีนี้มีปัญหาขอบเขตสถานี/ความสัมพันธ์ ไม่ใช่แค่keyword ต้องตรวจgame_service/resource_idsของPC01–02กับPC03–10 และsource fields แล้วระบุว่าเป็นconfirmed predicate omission/selection errorหรือยังreview ห้ามใช้zone-levelrelationยืนยันทุกเครื่องในโซน
4. “Alumni เล่น VR 1 ชั่วโมง 3 ชั่วโมง เสียกี่บาท” — ขอแยกระยะเวลาที่ขัดแย้งเป็นclarification แต่graderเดิมขอansweravailable ต้องตรวจว่าคำถามระบุเวลาต่อรอบกับเวลารวมชัดหรือไม่ ไม่บังคับเลือกเลขตัวแรกเพื่อให้graderผ่าน
5. “Is thr stdio open 24 hours” — อ่านsourceว่าไม่เปิด24ชั่วโมงและตารางได้ แต่routeผิดlegacycontract ตัวอย่างนี้ไม่ควรถูกนับactualwronganswerเพียงเพราะroute
6. “JSON คืออะไร ตอบแบบเด็กปีหนึ่งเข้าใจได้” — คำตอบระบบตีความไม่พร้อมเป็นgeneral-assistant/transport limitation ไม่ใช่ธุรกิจไม่มีข้อมูลให้ย้าย

## ข้อสังเกต model transport

ช่วงต้นมีtimeout12/60วินาทีหลายรายการที่clientเรียก/api/chatจริง ไม่พบWinError10013หรือHTTP404ในตัวอย่างที่อ่าน ต่อมามีtransport successesแล้ว จึงห้ามสรุปว่าทั้งFullปิดLLM/เรียกโมเดลไม่ได้จาก5callsแรก Serverlogที่บันทึกgeneration/provenanceเสร็จไม่เท่ากับclientได้รับresponseทันเวลา ต้องใช้clientobserved_model_http_callsและgateway eventแยกtimeout/schema/selection/content

## งานหลังจบที่ยังบังคับ

ตรวจทุกfailuregroupแบบstreaming พร้อมquery/response/gold-contract/source evidenceและproofของkey/gradeครบ ไม่ใช้บันทึกระหว่างรันนี้แทนROOT_CAUSE_REVIEW_TH.md หรือคะแนนfixeddenominatorขั้นสุดท้าย และไม่เปิดFullซ้ำเพื่อเปลี่ยนผลให้ดีขึ้น
