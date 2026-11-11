# ผลรอบ200หลังแก้ข้อมูลเว็บ — 11 พฤศจิกายน 2026

ทดสอบครบ200คำถามเดิม แบบทีละข้อ ไม่มีkeyซ้ำ และkeysตรงmanifestทั้งหมด HTTPสำเร็จ200/200 ไม่มีtransport error สำเนาcode/registry/DBไม่เปลี่ยนระหว่างวัด ตรวจใน `COMPLETION_INTEGRITY.json`

## ผลที่วัด

| รายการ | หลังแก้เว็บ/เป้าหมาย | bounded200ก่อนแก้ |
|---|---:|---:|
| Literal matched / supported grade identities |196/255|202/255|
| Literal not matched |59|53|
| Literal unassessed ในส่วนที่รองรับ |0|0|
| Grade identities ที่ไม่มีเกณฑ์literalรองรับ |250|250|
| unavailable |36|35|
| เวลารวมทั้งรอบรวมpreflight |6นาที24วินาที|7นาที30วินาที|
| มัธยฐานเวลาต่อคำถาม |0.922วินาที|1.072วินาที|
| คำถามที่ใช้เวลาเกิน20วินาที |0|0|
| เวลาต่อคำถามสูงสุด |15.242วินาที|17.108วินาที|

ผลR134ที่บันทึกไว้สำหรับ200keysเดียวกัน197/255literal ไม่เรียกโมเดลR134หรือregradeR132 ตัวหาร255เป็นgrade identities ไม่ใช่255คำถาม คะแนนนี้ไม่ใช่semantic accuracy

## ผลต่างมีเพียง2คำถาม

จับคู่เกณฑ์เดียวกัน:ผ่านทั้งคู่196,เฉพาะก่อนแก้6,เฉพาะใหม่0,ไม่ผ่านทั้งคู่53

1. **จำนวนsessions:**5grade identitiesเดิมคาดข้อความ `3 sessions` แต่หน้าเว็บจองปัจจุบันบอก6 คำตอบใหม่ตอบ6พร้อมลิงก์และไม่ใส่หัวข้อคำถามเดิมที่อ่านผิดธรรมชาติ ตรวจแยกใน `SOURCE_ALIGNED_CHECK.json` ไม่แก้เกณฑ์เก่า ไม่หัก5ออกจากตัวหารเพื่อปรับคะแนน
2. **Driving Force Shifter อยู่ซนไหน:**1grade identity เปลี่ยนจากตอบCockpit Zoneเป็นunavailable Traceบันทึกmodel_transport_failure แต่ไม่พิสูจน์ว่าตัวโมเดลล่มหรือtimeoutจริง พบว่ารู้จักอุปกรณ์แล้วแต่คำว่า“อยู่ซนไหน”ยังไม่อยู่ในpredicateตรง จึงแก้หลังรอบวัดในworking candidate แยก

## สิ่งที่แก้และตรวจหลังรอบวัด

- เพิ่ม“อยู่ซนไหน”เป็นคำถามlocationเฉพาะเมื่อมีอุปกรณ์ที่ผูกได้ ไม่แก้ชื่ออุปกรณ์/ตัวเลข และอ่านตำแหน่งจากsourceเดิม
- แก้ทั้งnative intentกับfield vocabularyให้สอดคล้องกัน หลังแก้เพียงชั้นแรกพบGaming Mouseยังไปlegacyprofileผิดfield ถูกverifierระงับไว้ เก็บผลล้ม `post_eval_delivery_1794394148724110600` แล้วแก้ชั้นfieldร่วม
- รักษาชื่อหน้า/sectionที่ตรวจแล้วไม่ให้migration wrapperเปลี่ยนเป็นชื่ออ้างอิงทั่วไป
- `r135_bounded_response_20261111/post_eval_delivery_1794394237162105600/RESULT.json` ผ่าน8checks source-onlyผ่านshared chat dispatcher รวมShifterคำปกติ/คำพิมพ์ตก,อุปกรณ์อีกชนิด,unknowndeviceไม่ยืมข้อมูล,เก็บrawquestion,ชื่อsourceและ6sessions
- `r135_bounded_response_20261111/post_eval_http_1794394299299618100/RESULT.json` ผ่านHTTP3คำถามตามลำดับ/6assertions:ShifterตอบCockpit Zone,กฎ6sessionsพร้อมชื่อsource,โรงแรมอื่นไม่ยืมกฎของศูนย์
- working previewล่าสุด `http://127.0.0.1:8141/` version `R135-Verified-working` อ่านฐานสำเนาverified_sources.sqlite ส่วน8140เป็นสำเนาวัดที่ตรึงไว้

การแก้หลังวัดไม่อยู่ในคะแนน196/255 ไม่คำนวณคะแนนทั้งชุดใหม่จากผลเฉพาะจุด และไม่รัน200ซ้ำเพียงเพื่อเปลี่ยนคะแนนหนึ่งข้อ

## ข้อจำกัดและงานต่อ

ยังมี36unavailableในรอบที่วัด ไม่สรุปว่าแก้ครบทั้งหมดจากการแก้Shifterหนึ่งข้อ ต้องจัดกลุ่มจากtraceจริงต่อ ปัญหาauthority/ช่วงมีผล ขอบเขตเกม/บริการ ภาพคู่มือและกติกาที่อ่านไม่ได้ยังเปิดอยู่

จัดกลุ่มtraceไว้ใน `UNAVAILABLE_GROUPS.json`:12 unresolved,5 competition_rules,3 game_overview,3 equipment,7 game_detail,4 game_controls,2 schedule ส่วนreason codesพบstore_or_snapshot_unavailable15และmodel_transport_failure21 (ก่อนแก้ข้อมูลพบ15และ20ตามลำดับ) มีconstraint_application_unverifiedซ้อน1กรณี รหัสเหล่านี้ยังไม่พิสูจน์rootcause ต้องตรวจexception/เส้นทางจริง ไม่กล่าวว่าโมเดลล่มหรือDBเสียทั้งหมด

ตัวตรวจสถานที่เป็นbounded explicit-location rejectionร่วมกับsource relationship ใช้กับFAQที่ประกาศcenter binding ไม่ใช่general semantic proof ไม่อ้างครบ48/76หรือพร้อมproduction

ชุด200นี้เคยเปิดดูแล้ว เป็นregressionไม่ใช่unseen evaluation มีC07เพียง1ตัวอย่าง เวลา/source/backendต่างจากผลย้อนหลัง จึงไม่อ้างว่าFlowเป็นเหตุของเวลาหรือคะแนนทั้งหมด ไม่ฝึกweightsจากชุดนี้

เปิด `RESULTS_VIEW.html` เพื่ออ่านคำถาม คำตอบ3รุ่น เวลา และลิงก์ที่แต่ละรุ่นส่งจริง ส่วน `PAIRED_LITERAL_DIFFERENCES.json` เก็บ2กรณีที่คะแนนต่าง
