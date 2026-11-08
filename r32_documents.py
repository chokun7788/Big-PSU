import json,collections,hashlib
from pathlib import Path
ROOT=Path(__file__).parent;R=Path((ROOT/'r32_report_path.txt').read_text().strip());P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
load=lambda n:json.loads((R/n).read_text(encoding='utf-8'))
summary=load('final13_SUMMARY.json');a=load('FINAL_ANALYSIS_METRICS.json');u=load('final13_unit_all.json')
flow=f'''# Flow ฉบับตรวจหลังลงมือ — PSU Esports Chatbot r32

วันที่ 2 ตุลาคม 2026 เวลาไทย • รุ่นแพ็กเกจ final13 • Runtime `2026.10.02-source-content-reliability-r32`

## 1. เป้าหมายและขอบเขต

แก้รายการที่เหลือในระบบจริง: คำพิมพ์ผิดที่ทำให้ข้อมูลสดหลุดเส้นทาง, เกมถูกแต่หัวข้อผิด, คำถามหลายประเด็นตอบขาด, คำตอบมีแต่หัวข้อ, คำจริงกำกวม, เงื่อนไขตรวจเนื้อหา, การสร้างชุดภาษาอังกฤษ, ข้อมูลขาด/ขัดกัน/ผิดปี และคิวเว็บ พร้อมเก็บผลทดสอบที่ตรวจย้อนกลับได้

ผลการทดสอบอัตโนมัติเป็นหลักฐานเฉพาะเคสและเงื่อนไขที่ตรวจ ไม่ใช่การรับรองทุกคำถามหรือการอนุมัตินโยบายของเจ้าของ งานเก็บสถานะจองจริงยังพักตามคำสั่งเดิม เตรียมเครื่องมือตรวจไว้แล้วโดยไม่สร้างการจอง

## 2. Flow รับคำถามถึงตอบ

```mermaid
flowchart TD
 A[รับข้อความ ภาษา และประวัติ] --> B[ตรวจแป้นพิมพ์และข้อความเบิ้ล]
 B --> C[กู้คำสำคัญตามบริบทและขอบเขต]
 C --> D[ล็อกชื่อเกม อุปกรณ์ และชนิดคำถาม]
 D --> E{{ต้องใช้สถานะจองสดหรือไม่}}
 E -- ใช่ --> F[ดึงสถานะตามวันที่และช่วงเวลาที่ถาม]
 F --> G{{ข้อมูลสดพร้อมและครอบคลุมหรือไม่}}
 G -- ไม่ --> H[บอกว่ายังยืนยันไม่ได้]
 G -- ใช่ --> I[คัดเฉพาะเครื่องและ Slot ที่ถาม]
 I --> J[แสดงจำนวนว่างและรายการตามคำถาม]
 E -- ไม่ --> K{{เป็นกฎการแข่งขันหรือไม่}}
 K -- ใช่ --> L[ล็อกเกม รายการ และปีเอกสาร]
 L --> M{{ตรงฉบับที่มีหรือไม่}}
 M -- ไม่ --> N[บอกฉบับที่มีและฉบับที่ยังขาด]
 M -- ใช่ --> O[แยกทุกประเด็นที่ผู้ใช้ถาม]
 O --> P[อ่านข้อกฎจริงพร้อมเงื่อนไขและตัวเลข]
 P --> Q{{ครบทุกประเด็นหรือไม่}}
 Q -- มีส่วนขาด --> R[ตอบส่วนที่ยืนยันได้ พร้อมระบุส่วนที่ขาด]
 Q -- ข้อกฎขัดกัน --> S[แสดงความขัดกันและคำถามถึงผู้จัด]
 Q -- ครบ --> T[จัดคำตอบจากข้อกฎครบถ้วน]
 K -- ไม่ --> U[เส้นทางข้อมูลบริการ เกม ราคา สมาชิก หรือความรู้]
 H --> V[ตรวจภาษา เนื้อหา แหล่งข้อมูล และความสด]
 J --> V
 N --> V
 R --> V
 S --> V
 T --> V
 U --> V
 V --> W{{ผ่านสัญญาคำตอบหรือไม่}}
 W -- ไม่ --> X[ถามเพิ่มหรือแจ้งว่าไม่พบข้อมูลที่ยืนยันได้]
 W -- ผ่าน --> Y[ส่งคำตอบพร้อมแหล่งข้อมูลและบันทึก trace]
```

## 3. การกู้คำผิด

1. เก็บข้อความดิบและข้อความหลังแก้ใน trace ทุกขั้น ไม่ทับ input เดิม
2. ใช้ชื่อที่ลงทะเบียนและศัพท์หัวข้อของระบบ เป็นขอบเขตการเปรียบเทียบ ใช้ OSA/edit distance รองรับเพิ่ม ขาด เบิ้ล และสลับอักษร
3. กู้คำที่มีบริบทสนับสนุน เช่น อุปกรณ์ + เวลา + รูปคำถามสถานะว่าง หรือชื่อเกม + คำถามการแข่งขัน
4. จำกัดจำนวน span และ edit ตามตัวกู้คำเดิม (intent preflight 3 span / 4 edits รวม); ไม่ขยายทั้งพจนานุกรมเพื่อให้ตัวอย่างผ่าน
5. รักษาเลขเครื่อง วันที่ เวลา เวอร์ชันเกม คำปฏิเสธ และคำเชื่อม `และ/กับ/and` ให้ครบ
6. เมื่อ candidate กินคำเชื่อม ให้คำนวณ candidate หัวข้อเดิมซ้ำโดยใช้คำเชื่อมเป็นขอบเขตแข็ง หากไม่มีคำเดียวที่ผ่าน ให้คงข้อความเดิม
7. คำจริงเช่น pay/play ต้องถามกลับเมื่อกำกวม ชื่อบุคคลต้องมีหลักฐานชื่อเดียวกันก่อนเชื่อมข้อมูล
8. candidate ของชื่อเกมและหัวข้อใช้ solver ร่วมกัน แต่การยอมให้ prefix ทับกันใช้เฉพาะหัวข้อเดียวกัน ไม่ผ่อนข้อจำกัดชื่อเกม/เลขรุ่น

ข้อจำกัด: วิธีนี้ยังไม่แก้ทุกคำทั่วไปและทุกประโยคใหม่ การเพิ่มศัพท์ต้องผ่านเคสคำจริงและคำปฏิเสธด้วย

## 4. สถานะจองและเวลาบริการ

- คำถาม “PC1 ตอน 10:00 วางหรือเปล่า” ต้องเข้าเส้นทางสถานะสด เมื่อบริบทครบ จึงไม่ใช้ตารางเปิดบริการแทนการว่าง
- ชื่อหมวดกว้างให้รวบรวมเครื่องของหมวดนั้นและแสดงจำนวนว่าง/ทั้งหมด คำถามหาอุปกรณ์ว่างทุกหมวดให้แสดงเฉพาะรายการว่างตาม Slot ที่ถาม ตาม Flow เดิม
- รักษานโยบาย 12:00–13:00 ไม่เปิดจอง และ VR 30 นาทีครอบคลุมชั่วโมงเต็มตามที่ผู้ใช้ยืนยันไว้ก่อนหน้า; รอบนี้ไม่เปลี่ยนไฟล์ตารางเจ้าของ
- fixture ต้องมีขอบเวลา, approved/cancelled/no-show, VR, Maintenance และวันปิดพิเศษทั้งไทย/อังกฤษ
- หากข้อมูลสดไม่พร้อม ให้ตอบว่ายังยืนยันไม่ได้ แม้รู้ตารางเปิดบริการ
- แยก `transport_http_ok` จาก `occupancy_verified`; ค่า HTTP 200 ไม่ใช่หลักฐานว่าว่างจริง

เครื่องมือตรวจที่เตรียม: `tools/check_saved_booking_oracle_r32.py` อ่าน snapshot ที่บันทึกไว้กับ oracle ที่เจ้าหน้าที่รู้ผลจริง โดยผูก SHA256, วันที่, +07 timestamp, ผู้ยืนยัน, เครื่อง และ Slot ตรวจเฉพาะรายการที่ยืนยัน ไม่รับรองอนาคตหรือเครื่องที่ไม่ตรวจ ใช้ template รุ่น V2 ที่มี `source_snapshot_sha256`

## 5. กฎการแข่งขันและคำถามหลายประเด็น

1. ระบุเกมเดียวหรือหลายเกมให้ชัด อย่าใช้กฎ VALORANT แทน CS2/RoV/Tekken
2. ตรวจปีจากตัวตนเอกสารที่ลงทะเบียน ไม่ใช้วันที่อัปเดตเป็นฉบับกฎ และไม่อนุมานปีของ Tekken ที่เอกสารไม่ระบุ
3. ปีเกิดและยอดเงินสี่หลักไม่ใช่ปีฉบับกฎ; เลขข้อที่มีจุดไม่ถูกดึงเป็นปี
4. สร้างรายการประเด็นจากคำถามก่อนเลือกแหล่งข้อมูล: eligibility, roster, registration, settings, equipment, scope/event information, pause/timeout และ team size ที่มีข้อรองรับ
5. อ่านข้อกฎจริงทั้งเงื่อนไขและตัวเลข ไม่ยอมให้ชื่อหัวข้อ “การตั้งค่าในเกม” เป็นคำตอบรายละเอียด
6. เมื่อมีคำถามขาดข้อมูล เช่นอายุขั้นต่ำ/ค่าสมัคร ให้แยกส่วนที่ขาดออกจากคำถามย่อยที่มีหลักฐาน ตอบข้อคุณสมบัติที่มีและแจ้งว่าข้อมูลอายุยังไม่พบ
7. ถ้าถามอายุอย่างเดียว ไม่แสดงคุณสมบัติทั่วไปแทนเกณฑ์อายุ; ไม่มีแหล่งยืนยันอายุให้ตอบว่ายังไม่พบ
8. RoV 5v5 คือผู้เล่นในเกมฝ่ายละ 5 ไม่ได้ยืนยันจำนวนรายชื่อรวมสำรอง
9. ข้อ Tekken เรื่อง pause ขัดกัน ให้แสดงความขัดกัน ไม่เลือกนโยบายเอง
10. ข้อ RoV ที่ต้นฉบับจบกลางประโยค ให้ขอข้อเต็ม ไม่เติมข้อความด้วยการเดาหรือแปลส่วนที่ขาด

## 6. การตรวจเนื้อหาต้องปรากฏคืออะไร

การได้หมวด `competition_rules` หรือมี source ID ของ CS2 ยังไม่พอ ตัวอย่างคำถาม pause + timeout ต้องมีทั้งข้อ pause พร้อมจำนวน/ระยะเวลา และข้อ timeout พร้อมจำนวน/ระยะเวลา/Freeze time ข้อใดหายต้องไม่ผ่าน

ตัวตรวจอ่านคำถามเองก่อน retrieval แล้วตรวจ source ที่เลือกและข้อความข้อกฎครบถ้วนในคำตอบ ตัวตรวจใหม่ไม่ใช้ประโยคที่ระบบตอบมาสร้างคำตอบคาดหวัง

- positive oracle ใหม่ 30 เคสมีข้อ source ที่ระบุไว้ล่วงหน้าทั้งไทย/อังกฤษ
- oracle partial ใหม่ 8 เคสตรวจข้อ eligibility เต็ม + ข้อความบอกอายุ/ค่าสมัครที่ขาด
- mutation ลบข้อใดข้อหนึ่ง หรือเหลือเพียงหัวข้อ ต้องถูกปฏิเสธ แม้มี source ID ที่ถูก
- คำแปลอังกฤษต้องตรง source hash; ถ้าแปลเก่าหรือไม่มีแปล ให้แจ้ง pending ตามขอบเขต ไม่แปลสดโดยเดาค่านโยบาย
- frozen Gold เดิมคงไว้ การเปลี่ยนสถานะจาก no_answer เป็น partial ทำให้เกณฑ์เก่าบางข้อไม่ผ่าน ซึ่งต้องแสดงแยกจากการตอบข้อเท็จจริงผิด

## 7. ภาษาอังกฤษและการสร้างชุดทดสอบ

ตัวสร้างต้องสร้าง metadata ของ frozen v2 ได้เหมือนเดิม เก็บ English reference ปัจจุบันเป็น sidecar ใหม่ ไม่เขียนทับ Gold แก้ความต่าง reference 6 แถวที่พบ และแยกความเข้ากันได้ย้อนหลังออกจากเนื้อหาปัจจุบัน

Audit กฎพบ 104 แถว มี English text ตรง hash 103 แถว อีกแถวเป็นส่วนที่ต้นฉบับไม่ครบ การมี registry status approved ในโค้ดไม่ยืนยันว่าเจ้าของหรือผู้จัดตรวจเนื้อหาหรือเห็นชอบปีฉบับแล้ว

## 8. คิวเว็บและการรอ

1. คิวรับ TCP ขนาด 16 รองรับ burst สั้น เพื่อให้คำขอไปถึง admission gate ได้ ไม่เพิ่มจำนวนงานประมวลผลหรือ worker
2. เมื่อคิวเต็ม ส่ง HTTP 503 + `retryable:true` + Retry-After เฉพาะกรณีที่ลองซ้ำได้
3. หน้าเว็บลองไม่เกิน 3 ครั้ง เว้น 250–1500 ms และหยุดเริ่ม retry เพิ่มเมื่อเวลาสะสมเกิน 12 วินาที เงื่อนไขนี้ไม่รับรองว่าทุก HTTP call จะจบภายใน 12 วินาที
4. payload/history/session เดิมทุกครั้ง ไม่เพิ่มข้อความผู้ใช้ซ้ำ ขณะรอแสดงสถานะไทย/อังกฤษและปิดปุ่มส่งชั่วคราว
5. network error, JSON เสีย, HTTP 500 และ error ที่ไม่ retryable ไม่ส่งซ้ำอัตโนมัติ
6. เก็บผล idle, cold/loaded และ protocol แยกกัน การทดลอง 10 คำถามไม่ใช่ SLA ของ WordPress หรือจำนวนผู้ใช้สูงสุด

## 9. รอบแก้และข้อที่พบจากการตรวจซ้ำ

| รอบ | สิ่งที่ตรวจพบ | สิ่งที่ปรับ |
|---|---|---|
| 1 | intent และ source requirements ยังไม่ครบ | baseline/snapshot และเพิ่มตัวกู้หัวข้อ/สัญญาเนื้อหา |
| 2 | source oracle ผ่าน 26/30 | เติมการแยกหัวข้อและขอบเขต source |
| 3–5 | แก้คำกิน prefix/คำถูก และแยก RoV team size ไม่สำเร็จบางแบบ | จำกัด overlap ในหัวข้อเดียว รักษาคำจริง และอ่านข้อ 5v5 |
| 6 | source oracle ผ่าน 30/30 | รันชุดใหญ่ทุก corpus ที่ inventoried |
| 7 | หยุดเกิน/การแข่งขันไหน/เครื่องหมายวรรคตอน ถูกแก้เป็นหัวข้อผิด | รักษาคำ threshold, identity และขอบเขต punctuation; API 937/937 ในรุ่นนี้ |
| 8 | กฎผิดปีผ่านการทดสอบ direct แต่เว็บยังตอบ overview ต่อ | เพิ่ม guard ปี source แล้วตรวจ actual HTTP; เก็บผลล้มเหลว 6/24 |
| 9 | answer contract ไม่รู้จัก no_answer mode ของ guard | จำแนก mode ให้ตรงผลจริง; actual HTTP ปี 24/24 |
| 10 | ปีเกิด/ยอดเงินอาจสับสนกับปีฉบับ | เพิ่ม negative bounds และทดสอบเดิมทั้งหมด |
| 11 | burst บางคำขอไม่ถึง HTTP gate | ทดลอง Windows backlog 5 ได้ 6/10 เทียบ 16 ได้ 10/10; ปรับ intake และตรวจ cold helper 10/10 |
| 12 | อายุขั้นต่ำที่ขาดทำให้ eligibility ที่มีหายไป | แยก partial; เคสใหม่ 7/8 พบคำเชื่อมถูกกิน |
| 13 | คุณสมบัตและ ถูกแก้เป็น คุณสมบัติละ | ใช้คำเชื่อมเป็นขอบเขต; partial 8/8 และ source 30/30 ผ่านเว็บ |

ผลแต่ละรอบเก็บแยก ไม่เปลี่ยนคำตอบคาดหวังเดิมเพื่อให้คะแนนผ่าน

## 10. วิธีประเมินและที่มาผล

- ครบ 20,327 requests ไม่ซ้ำ / 55,583 grades; รัน C6 เต็ม แล้ว replay C7 8,526 queries, C10 17 source-abstention queries, C12 17 source-gap queries, C13 3 queries ที่ recovery ทับคำเชื่อม
- C8 พบว่า corpus ชุดใหญ่ไม่มี explicit Gregorian year ในคำถาม จึงเพิ่มชุด HTTP ปี 24 เคสแยก แทนการอ้างว่าชุดใหญ่ครอบคลุมปีแล้ว
- ไม่เรียกผลรวมนี้ว่ารันสดทุกข้อบน final13; ทุกรายการมี execution provenance และเก็บ raw ของรอบที่รันจริง
- คู่พิมพ์ผิด 2,000 ใช้ grader v2 เดียวกันเปรียบเทียบก่อน/หลัง; มี positive content contract 894 คู่เท่านั้น
- รุ่นสุดท้ายทดสอบ unit {u['tests']}/{u['tests']} แยกจาก smoke เดิม 71/85, extra 970 requests และ native guard 500
- Human review 120 แถวเป็น observations ไม่มี oracle ที่เจ้าของยืนยัน ห้ามนับเป็นความถูกต้อง 120/120
- ชุด slot จริง 4 HTTP cases ถูก defer เพราะงานเก็บ occupancy พัก; known synthetic booking fixture 31/31 เป็นคนละหลักฐาน

## 11. งานที่ยังต้องพัฒนาและวิธีเดินต่อ

1. **P1: 42 คู่ที่มีเงื่อนไขเนื้อหาบวกยังตก** — ตรวจ source/target/ทุก proposition รายข้อจาก appendix ก่อนแก้ route หรือ renderer แล้วเพิ่ม mutation ที่ลบเนื้อหาจริง
2. **P1: คำสำคัญ/หัวข้อทั่วไปและสมาชิก** — กลุ่ม trace 71 และ 19 คู่ ตามลำดับ ต้องแยกคำผิดออกจากคำจริงและชื่อคนที่ไม่ตรง source; เพิ่ม syntax frames/ศัพท์งานและ target lock โดยไม่เพิ่ม alias ทั้งประโยค
3. **P1: อีก 65 คู่ที่ยังไม่มี positive oracle** — สร้างคำตอบคาดหวังจาก source อย่างอิสระก่อนเรียกว่าคำตอบใดถูก ไม่ใช้ clean answer เป็น Gold อัตโนมัติ
4. **P2: repeat guard** — 500 เคส layout ถูก 500 แต่ repeat ยังมี FN 27 / FP 2; เก็บชุด negative คำจริงและปรับ model/threshold ร่วมกับ downstream recovery ไม่ลด threshold อย่างเดียว
5. **P2: load ที่เกิน burst ที่ทดสอบ** — เพิ่มสถานการณ์ overload ต่อเนื่อง/คำถามที่เรียก LLM และวัดคิวกับ deadline หากนำไปใช้งานหลายคน; คงการจำกัดงานเดิมจนมีหลักฐาน
6. **เจ้าของ/ผู้จัด** — ยืนยันกฎขัดกัน ฉบับปีที่ใช้งานจริง ข้อ RoV เต็ม อายุ/ค่าสมัคร/จำนวนรายชื่อรวมสำรอง และนโยบายถ่ายภาพ; มีคำถามพร้อมใน OWNER_QUESTIONS_TH.md
7. **พักตามผู้ใช้** — real booking occupancy; เมื่อผู้ใช้พร้อมจึงใช้ template V2 และ checker ที่ผูก snapshot แยก transport จาก correctness

การเดินต่อทุกกลุ่ม: หลักฐานต้นฉบับ → oracle อิสระ → baseline/trace → เปลี่ยนเฉพาะจุด → positive/negative/mutation → affected replay → package/hash → actual HTTP → รายงานข้อจำกัด ถ้า source ขาดให้ตอบส่วนที่มีและขอข้อมูลที่ขาด ไม่ใช้การเดา

## 12. การรักษาไฟล์และเปิดใช้งาน

ก่อนแก้ snapshot 423 ไฟล์; ข้อมูลเจ้าของ/Gold 584 hashes ต้องเหมือนเดิม; tests ที่มีเดิม 140 ไฟล์ต้องเหมือนเดิม เก็บแพ็กเกจและ log ทุกรุ่น ไม่มี reset/stash/commit หรือเขียนทับผลทดสอบเดิม

แพ็กเกจส่งมอบคือ `owner_local_delivery_20261002_source_content_reliability_r32_final13/PSU_Esports_Chatbot_Local`; เปิดเว็บจาก launcher ของแพ็กเกจ และตรวจ `/health` + hash ของไฟล์ UI หลังเปิด ใช้พอร์ต 8090 สำหรับลองจริง พอร์ต 8091 ใช้ทดสอบแล้วปิดเฉพาะ process ที่พิสูจน์ว่าเป็นของงานนี้

รายงานและ raw อยู่ที่ `{R}`. ดู FINAL_RESULTS_TH.md และ REMAINING_107_ANALYSIS_TH.md เพื่ออ่านข้อที่ผ่าน ข้อที่ยังตก และ trace รายข้อ
'''
path=P/'docs/133_all_remaining_r32_verified_flow_20261002.md'
with path.open('x',encoding='utf-8') as f:f.write(flow)
with (R/'FLOW_FINAL.md').open('x',encoding='utf-8') as f:f.write(flow)
# Detailed analysis of the two intentional frozen-status differences.
new=[json.loads(l) for l in (R/'final13_NEW_FAILED.jsonl').open(encoding='utf-8')]
with (R/'FROZEN_STATUS_DIFFERENCES_REVIEW.json').open('x',encoding='utf-8') as f:json.dump(dict(total=len(new),interpretation='Frozen cases expected no_answer. New source-bound partial answer retains CS2 eligibility and explicitly discloses missing age. Original scores are preserved; independent partial HTTP oracle validates this changed behavior. This is not a claim that every legacy failure is a stale test.',cases=new),f,ensure_ascii=False,indent=2)
counts=summary['counts'];pair=summary['paired'];metrics='\n'.join(f'- {k}: {v}' for k,v in a['remaining_trace_hypothesis_groups'].items())
report=f'''# ผลพัฒนาและทดสอบ PSU Esports Chatbot — r32 final13

## ผลที่ได้

ทำ Flow และลงมือแก้ครบกลุ่มที่มีหลักฐานในรายการเดิม พร้อมตรวจซ้ำ 13 รอบของ candidate แต่ยังไม่ใช่ระบบที่ตอบทุกคำถามถูก 100% งาน source ที่ต้องให้ผู้จัดยืนยันและงานเก็บสถานะจองจริงยังมีข้อจำกัดเดิม

- กู้คำสถานะว่างจากบริบทอุปกรณ์/เวลา โดยไม่ใช้ตารางเปิดบริการแทนสถานะจอง
- กู้หัวข้อกฎด้วยศัพท์งานและ edit distance รักษาเกม เลขรุ่น ตัวเลข คำจริงและคำเชื่อม
- ตอบข้อกฎเต็มและทุกประเด็นที่มีหลักฐาน ตรวจข้อความจริง ไม่รับเพียง source ID หรือหัวข้อ
- ตอบส่วนที่มีหลักฐานพร้อมแจ้งส่วนอายุ/ค่าสมัครที่ยังขาด; ถ้าถามอายุอย่างเดียวไม่ใช้ eligibility แทน
- ปฏิเสธฉบับกฎผิดปี; ไม่นับปีเกิด/ยอดเงินเป็นปีฉบับ
- แก้ English builder metadata drift 6 แถวและทำ current-reference sidecar โดยคง frozen Gold
- เพิ่มข้อความรอและ bounded retry เฉพาะ 503 ที่ retryable; ปรับ TCP backlog 16 หลังทดลองบน Windows โดยไม่เพิ่ม worker
- เตรียม template/checker ของสถานะจองจริงที่ตรวจแยก transport และ occupancy

## หลักฐานทดสอบ

| ชุด | ผล | ขอบเขต |
|---|---|---|
| Unit final13 | {u['tests']}/{u['tests']} | tests เดิม + tests ใหม่; ไม่มี skip |
| Full corpus รวม affected replay | {counts['grade_passed']:,}/{counts['grades']:,} grades; {summary['requests_seen']:,} inputs | ผล legacy ไม่ใช่ factual accuracy; provenance C6/C7/C10/C12/C13 |
| Bilingual typo pairs | clean {pair['clean_passed']}/2000; noisy {pair['noisy_passed']}/2000 | scorer v2 เดียวกัน; ก่อน r32 noisy 1672, regression 111; ตอนนี้ 1676, regression {pair['clean_pass_noisy_fail']} |
| Independent source clauses actual HTTP final13 | 30/30 | clause เต็ม + source + ภาษา |
| Independent partial/source-gap actual HTTP final13 | 8/8 | eligibility พร้อมบอกส่วน age/fee ที่ขาด; clean/noisy/age-only |
| Explicit source year HTTP | 24/24 ใน C9–C12 | TH/EN 3 เกม; หลัง deploy รุ่นสุดท้ายตรวจซ้ำและเก็บผลแยก |
| Existing actual HTTP regression | C9 937/937; C13 รันซ้ำเก็บผลแยก | 4 live occupancy questions defer; รุ่นล่าสุดมี frozen-status differences ที่อธิบายด้านล่าง |
| Synthetic known booking | 31/31 | approved/cancelled/no-show, boundary, lunch, Maintenance, special closure, VR; ไม่ใช่ oracle ของจริง |
| Session context | 12/12 sessions, 24/24 turns | offline original wording/contents; ไม่ยืนยันทุก session ภาษาอังกฤษ |
| Existing smoke scripts | 71/85 บน C7 | 14 ชื่อไฟล์ที่ตกเหมือน baseline; เก็บ log และสาเหตุด้านล่าง |
| Extra corpora | 970 requests / 981 grades | รุ่น C7, subset aliases แยก; human observations ไม่ใช่ accuracy |
| Native input guard | exact flags {a['native_guard']['exact_flags']}/500 | layout 500/500; repeat FN 27 / FP 2; ไม่ใช่คะแนนคำตอบ |
| Retry protocol | 9 scenarios + HTTP 503 TH/EN 2/2 | จำกัดรอบ/payload ไม่ซ้ำ ไม่ retry network/500/JSON เสีย |
| Windows pending TCP probe | backlog 5: 6/10; 16: 10/10 | delayed accept fixture; สนับสนุน intake fix ไม่ใช่ proof root cause ของ network failure ทุกครั้ง |
| Cold actual retry-helper C11 | 10/10, retry รวม 8 | 3.20–5.07 วินาทีบนเครื่องนี้; ไม่ใช่ WordPress SLA |

**เกณฑ์เดิมที่ผ่านแล้วตกเพิ่ม {counts.get('new_failed_grades',0)} grades:** สองคำถาม eligibility + minimum age เคยคาด no_answer ทั้งคำถาม แต่ source มี eligibility จึงตอบ partial พร้อมแจ้งอายุที่ขาด การตอบแบบใหม่ผ่าน oracle อิสระ 8/8 ไม่เปลี่ยน Gold เดิมเพื่อให้ผ่าน ดู FROZEN_STATUS_DIFFERENCES_REVIEW.json ส่วนก่อนเปลี่ยน partial (C10) ไม่มี new failed grades

## สิ่งที่ยังผิด/ยังพิสูจน์ไม่ได้

ยังมี {counts['failed_unique']} unique inputs ที่ไม่ผ่านอย่างน้อยหนึ่ง legacy grade; จำนวนนี้รวม route/intent labels, ข้อความเก่า, source IDs, status, ข้อมูลขาด และคำตอบที่ต้องตรวจเนื้อหา ไม่ใช่ {counts['failed_unique']} คำตอบที่ยืนยันว่าผิดข้อเท็จจริง

คู่ clean ผ่าน/noisy ตก {pair['clean_pass_noisy_fail']} คู่: ไทย 54 อังกฤษ 53 มี positive content contract 42 อีก 65 คู่ยังไม่มีเงื่อนไขเนื้อหาบวก การแบ่งกลุ่มต่อไปนี้อิง trace และเป็นข้อสันนิษฐานเชิงวิเคราะห์ มิใช่การ adjudicate โดยเจ้าของ:

{metrics}

รายละเอียดทุกคู่มี input ปกติ/ผิด, output, expected route/status/content, recovery ที่ใช้, resolver score/margin, mode, validation errors และข้อจำกัดการสรุปที่ REMAINING_107_ANALYSIS_TH.md / JSONL คำตอบ clean เป็น baseline ไม่ใช่คำตอบจริงที่ยืนยันแล้ว ตัวอย่างชื่อบุคคลอังกฤษบางคำถามได้รายชื่อรวมที่ผ่าน route/status จึงยังใช้ยืนยันบทบาทบุคคลนั้นไม่ได้

Priority ต่อไป: ตรวจ 42 positive failures รายข้อ → เพิ่ม syntax/task cues และล็อกชื่อบุคคลจาก source → เพิ่ม positive oracle 65 เคสที่ยังขาด → ปรับ repeat guard พร้อม negative คำจริง → ทดสอบโหลดต่อเนื่องเมื่อจะเปิดหลายผู้ใช้ อย่าลด threshold หรือเพิ่ม alias ทั้งประโยคเพื่อให้ได้คะแนนสูง

## วิเคราะห์ smoke เดิม 14 รายการ

- answer_pipeline / english_draft_preview / llm_health_circuit_breaker / pipeline_fixes_20260823 / game_catalog: บาง assertion บังคับชื่อ mode หรือ LLM path เก่า ทั้งที่มี source path/fast path ใหม่ ต้องแยกตรวจเนื้อหาก่อนปรับ oracle
- bilingual_pipeline: บังคับ clarification ราคาแบบเดิม; ต้องตรวจว่าคำถามขาดข้อมูลจริงหรือแสดงทางเลือกมีหลักฐานแล้ว
- availability_policy_regressions: bare Call of Duty ต้องแยก edition; ไม่ยืนยันเกมผิดฉบับเพื่อให้ผ่าน
- bilingual_web_api: เจอ 503 ขณะรันชุดอื่น; actual retry helper และ cold test แยกไว้ ผลนี้ไม่ได้เป็นหลักฐานตอบข้อเท็จจริงผิด
- boundary_guard: เกณฑ์คาด boundary mode แต่ระบบผ่าน freshness gate; ต้องตรวจไม่มีการอ้างสถานะสดเทียม
- correctness_control_flow_v1: บางเคสคาด no_controls ในขณะที่ source ปุ่มมีแล้ว
- english_format_parity_fixes: บังคับ literal label เดิม ขณะที่ระบุ official Thai source และแปล role แล้ว
- genre_alias_formatting: คาด Dota2/Mobile Legends ที่ไม่อยู่ใน verified catalog; ไม่เพิ่มเกมที่เจ้าของยังไม่ยืนยัน
- real_usage_golden: 23/24; Naruto how-to ต่าง mode/intent แต่มีคำตอบและ source PS5
- update: คาดคำ มหาลัยอื่น แต่ตอบ นักศึกษา-นักเรียนต่างสถาบัน และราคาเดิม; source/semantic check ต้องแยกจาก literal

ไม่เรียกว่า 14 ข้อนี้เป็นปัญหา oracle ทั้งหมดโดยอัตโนมัติ ต้องเก็บ assertion และหลักฐาน source ที่รองรับการจัดประเภทไว้

## เจ้าของยังต้องยืนยัน / สิ่งที่พักไว้

ดู OWNER_QUESTIONS_TH.md: ข้อยกเว้นและโทษ Tekken pause, ข้อ RoV 6.1.1 ฉบับเต็ม (แถว s08_c01), ฉบับปีของแต่ละรายการ, ค่าสมัคร/อายุ/รายชื่อรวมสำรอง, นโยบายถ่ายภาพ และการตรวจคำแปลเชิงนโยบาย Audit English hash 103/104 ไม่ใช่ owner approval

สถานะจองจริงยังไม่เก็บตามคำสั่งเดิม ไม่มีการสร้างการจองหรือยืนยัน occupancy จริง ใช้ REAL_BOOKING_ORACLE_PENDING_TEMPLATE_V2.json และ tools/check_saved_booking_oracle_r32.py เมื่อพร้อม

## การรักษางานและ provenance

- snapshot ก่อนแก้ 423 files; owner/Gold 584 hashes คงเดิม; tests เดิม 140 files คงเดิม; ไม่ reset/stash/commit
- เก็บ raw ทุก candidate; สร้างผลด้วย exclusive file mode; ไม่มี initial hash ของ historical logs ทั้งหมด จึงไม่อ้าง cryptographic verification ทุก log
- summary ของ HTTP runner ที่คัดจาก r31 บางไฟล์มี label runtime ค้าง แก้ provenance เป็น sidecar API_EXECUTION_PROVENANCE_CORRECTION.json โดยใช้ health/package/hash ของจริง ไม่เขียนทับผลเก่า; runner final13 ใช้ health version โดยตรงแล้ว
- C12 merge เขียน full results และ summary ครบก่อนชนชื่อ changes sidecar เดิม จึงยังเทียบครบ 20,327/55,583 ได้; เก็บความผิดพลาดและทำ execution sidecar ชื่อใหม่ ไม่เขียนทับ raw
- บาง retained provenance labels ของ replay ถูกคัดมาเป็น source-abstention แม้ C13 เป็น conjunction fix ให้ยึด FINAL_EXECUTION_SCOPE.json ที่บันทึก scope/keys/code hash แยกอย่างชัดเจน
- full offline runner ปิด LLM/semantic และใช้ controlled booking unavailable; legacy fast-answer alias บางข้อเรียก local 8091 แล้วได้ 404 ซึ่งไม่ใช่การเก็บ occupancy WordPress จริง ส่วน actual API ใช้ owner profile LLM/semantic เปิด

Flow ฉบับสุดท้าย: docs/133_all_remaining_r32_verified_flow_20261002.md

เว็บสำหรับลองใช้: http://127.0.0.1:8090/ — แพ็กเกจ final13; ตรวจผล postrelease ใน RELEASE_FINAL13_VERIFICATION.json
'''
with (R/'FINAL_RESULTS_TH.md').open('x',encoding='utf-8') as f:f.write(report)
print(json.dumps({'flow':str(path),'report':str(R/'FINAL_RESULTS_TH.md')}),flush=True)
