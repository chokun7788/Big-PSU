# R115 — ทำครบขั้น 1–3 และตรวจผ่านแชทจริง

## สรุป

ตรวจ source เดิม → แก้โค้ดตามสาเหตุ → ตรวจคำถามเดิมผ่าน `/api/chat` จริง เปิด LLM และเลือกหมวดอัตโนมัติ ครบ 1,400 ข้อทั้งก่อนและหลังแก้ ไม่เพิ่มคำถาม ไม่รัน full 20,554 ไม่ติดตั้งทับ R78

- Positive ที่มี source จริงผ่าน strict: **902/960 (93.96%) → 926/960 (96.46%)**
- Positive ที่คืน goal claims ครบหลังแก้: 960/960 ข้อ เป็น source-claim coverage ไม่ใช่ human semantic accuracy
- Negative: 280/280 ผ่าน strict; 280/280 ไม่มี factual claim และตอบแบบไม่ยืนยัน
- Fixture positive 160 ข้อไม่มี fake live/news source ใน native: ยังตอบเนื้อหาเหล่านั้นไม่ได้ แต่คำตอบที่แทนด้วยข้อมูลผิดเรื่องลดจาก 27 ข้อเหลือ 0 ข้อ
- Strict ทั้ง corpus: 1141/1,400 (81.50%) → 1206/1,400 (86.14%) รวมข้อ fixture ที่ไม่มีข้อมูลไว้ ไม่ซ่อน coverage
- Strict เมื่อแยก 160 fixture goals ที่ไม่มี native source: 1141/1,240 (92.02%) → 1206/1,240 (97.26%)
- Strict ดีขึ้น 85 ข้อ; ถอยลง 20 ข้อ
- ในข้อที่ strict ลด มี 20 ข้อตารางเวลาที่คืน claims ครบแต่เปลี่ยนจาก answer เป็น partial ตามช่องว่างของ source; อีก 0 ข้อต้อง review แยก ไม่ซ่อนการลดคะแนนไว้

ตัวเลขทั้งหมดเป็นการตรวจ source identity/value/state กับ expected ที่ freeze ก่อน HTTP ใช้ projection ร่วมในการจัด identity ไม่ใช่คะแนนความถูกต้องจากผู้ประเมินมนุษย์อิสระ และไม่ใช่หลักฐานว่าระบบพร้อม production ครบทุกเงื่อนไข

## วิธีทดสอบและ lineage

- R113 เป็นแหล่งคำถามเดิมและ expected เดิม; R114 shared-engine เคยได้ 99.14% บน frozen read model จึงเทียบตรงกับ native API รอบนี้ไม่ได้ เพราะ source/fixture/adapter และเส้นทางการทำงานต่างกัน
- Before = R114 candidate ที่คัดลอกแยกมาทดสอบใน R115, runs/http01; After = candidate R115, runs/http03 ใช้ DB เดิมที่ hash ตรงกัน
- ไม่ใช้ category hint; ทุกข้อแยก session; เวลาอ้างอิงเดิม 2026-10-21T12:00:00+07:00; ไม่เรียก baseline เก่ามารันใหม่ด้วยข้อมูลคนละรุ่น
- http02 หยุดโดยตั้งใจหลังวิเคราะห์ log พบช่องโหว่เพิ่ม ไม่ใช่ full run และไม่เอามาปนเป็นผลสำเร็จ เก็บ ABORTED.json, original raw log และสำเนาโค้ดที่ hash ตรงกับ RUN_FREEZE ครบ
- 301 code checks ผ่าน โดยใช้ข้อความเดิม/ค่าคงที่เดิม และตรวจ source extension ใน memory ไม่มี HTTP/model เพิ่มในชุดนี้ ผลตรวจที่ไม่ผ่านระหว่างพัฒนาเก็บไว้ด้วย
- review_v2 อ่านทั้ง domain fact_id packets และ compatibility record/field packets ตรวจ raw response เดิมทั้งสองรอบด้วยเกณฑ์เดียวกัน ไม่เขียนทับ original grades

## ผลรายหมวด

| หมวด | Strict ก่อน /100 | Strict หลัง /100 | Positive มี source หลัง |
|---|---:|---:|---:|
| C01 ศูนย์/สถานที่/ติดต่อ | 100 | 100 | 80/80 |
| C02 บุคลากร | 95 | 100 | 80/80 |
| C03 อุปกรณ์ | 99 | 100 | 80/80 |
| C04 เกมและแค็ตตาล็อก | 100 | 100 | 80/80 |
| C05 วิธีควบคุมเกม | 100 | 100 | 80/80 |
| C06 ราคาปกติ | 61 | 100 | 80/80 |
| C07 ราคาเหมา | 100 | 100 | 80/80 |
| C08 การจองและขั้นตอน | 93 | 100 | 80/80 |
| C09 ชำระเงิน/เอกสาร | 93 | 100 | 80/80 |
| C10 กฎการใช้บริการ | 94 | 100 | 80/80 |
| C11 ตารางเวลา | 89 | 69 | 49/80 |
| C12 สถานะจองสด | 14 | 20 | 0/0 |
| C13 กติกาการแข่งขัน | 97 | 97 | 77/80 |
| C14 ข่าว/กิจกรรม | 6 | 20 | 0/0 |

C12/C14 มี positive fixture หมวดละ 80 ข้อและ negative หมวดละ 20 ข้อ การได้ strict เฉพาะ negative ไม่ใช่ความสามารถตอบ live/news positive ได้แล้ว

## จุดที่แก้และความหมายของผล

1. **Identity แย่งคำถามชื่อบุคลากร**: จำกัดคำกว้างชื่ออะไรและแก้ regex ชื่อไทย ไม่ hardcode ชื่อคน
2. **รหัส rate ถูกแยกเป็น staff/availability**: ผูก ID ทั้งรหัสกับ record ปัจจุบันก่อน route และจำกัด rate pool ตาม ID จริง แยก duration จาก money amount เมื่อถามเวลาเท่าไหร่
3. **Predicate guard ถูกข้าม**: router และ reader ใช้ predicate frames ร่วมกัน ถามสิทธิ์บริษัท การถ่ายบุคคล คริปโต ประกัน ฯลฯ ต้องมี source ของ predicate นั้น ไม่ใช้ขั้นตอนจองหรือกฎใกล้เคียงแทน
4. **FAQ ตารางกว้างกว่า field ที่ถาม**: อ่าน recorded period รายวันก่อน แสดงข้อจำกัดโซน/ช่วงมีผล/เวลาเปิดที่ขัดแย้ง ใช้ partial แทนการยืนยันสิทธิ์จองจริงเมื่อ source ยังไม่ครบ
5. **Live request ถูกตอบด้วยข้อมูลเครื่อง**: ตรวจชื่อเครื่องพร้อมวันเวลาและการถามว่าจองได้หรือยังเป็น live task อ่าน resource binding จริงก่อน provider ไม่ใช้ static location/capacity แทนสถานะ
6. **Unknown booking reference**: แยก missing source ของเลขจองจาก provider unavailable ไม่เลือกเครื่องหรือเลขจองข้างเคียง
7. **Unknown event หลุดไปกติกาคนละงาน/เพจติดต่อ**: เมื่อ news reader ผูกกิจกรรมไม่ได้ ให้ปิดทาง fallback ข้ามเรื่อง พร้อม guard จำนวนทีมและข่าวสดที่ไม่มีหลักฐาน
8. **คำแปลไม่ครบ**: แจ้งชัดก่อนแสดงย่อหน้าไทยในคำตอบอังกฤษ ไม่เรียกว่าคำแปลอังกฤษครบ
9. **เครื่องมือตรวจมองไม่เห็น compatibility packets**: แก้ตัววิเคราะห์ offline แยก original grade จาก review_v2 และอ่านเนื้อหาจริงประกอบทุกกลุ่ม

มีคำถามรหัสเทคนิค 39 ข้อ: strict 0/39 → 39/39 ต้องแยกจากการตอบภาษาธรรมชาติ ไม่อ้างว่าเป็น generalization กับคำถามใหม่

## สิ่งที่ยังไม่ถือว่าแก้ครบ

- **ตารางเวลา**: owner ยืนยันปิดวันธรรมดา 16:00–18:00 เท่านั้น; open_periods บางวัน conflicted, zone_ids และ effective dates ยัง unknown ไม่แก้ข้อมูลให้เป็นเปิดช่วงอื่นเอง คำตอบช่วงจองที่ partial จงใจคงความไม่แน่นอน แม้ oracle เก่าคาด answer
- **VR**: คำยืนยันต่อคนถูกผูกกับ rates เดิมแล้ว แต่ไม่เพิ่มจำนวนคนที่ใช้ได้จริง ส่วนลด การปัดเศษ หรือเงื่อนไข eligibility โดยไม่มี source ไม่เปลี่ยนข้อมูลเพื่อให้เทสผ่าน
- **C13 extra clauses 3 ข้อ**: มี summary และย่อหน้าหัวข้อเดียวกันจาก source ที่มีจริง คืน goal clauses ครบและมี source เพิ่ม เป็น granularity/overlap ของ oracle กับข้อมูล native ไม่ใช่หลักฐานว่าแต่งกฎ คง strict fail และตัวอย่างไว้
- **ภาษาอังกฤษ**: 20 คำถามอังกฤษยังมีบางย่อหน้าไทยที่ไม่มีคำแปลยืนยัน แม้ source claims ตรง expected จึงไม่ใช่คะแนนคุณภาพภาษาอังกฤษครบถ้วน
- **สถานะจองจริง/ข่าวสด**: workload ไม่มี snapshot fixture เดิมใน native และ provider/binding ที่ใช้ได้จริงยังไม่ถูกยืนยัน ห้ามใช้ผล unavailable/missing_source มาสรุปว่ารู้สถานะว่างหรือข่าวล่าสุดจริง
- **ข้อมูลเป็น draft**: ยังไม่มี approvals/release สำหรับ production; ใช้ migration preview เท่านั้น การเผยแพร่จริงต้องยืนยันข้อมูลและผ่านขั้นตอน owner ที่มีอยู่
- **ความละเอียดของสเปก**: บาง equipment specifications มีเพียง zone/quantity; คืนค่าตาม source ได้ไม่ได้หมายความว่ามี CPU/RAM/ความละเอียดจอครบ ตัวอักษร boilerplate ในค่า structured ถูกย่อในการแสดงผล จึงมี literal-body flags ที่ต้องแยกจากข้อมูลผิด ทั้งหมดเก็บใน raw และรายละเอียดด้านล่าง

## LLM และ transport

```json
{
  "before": {
    "selector_events": 53,
    "http_attempted": 53,
    "transport_ok": 51,
    "schema_ok": 51,
    "identity_verified": 51
  },
  "after": {
    "selector_events": 9,
    "http_attempted": 9,
    "transport_ok": 9,
    "schema_ok": 9,
    "identity_verified": 9
  }
}
```

ข้างบนเป็น domain evidence-selector events ที่มี id/transport/schema ใน log ไม่ใช่การอนุมานจำนวนเรียกโมเดลจากการเปิด toggle ทุกรอบเปิด LLM แต่ typed reader ตอบเองได้ก็ไม่จำเป็นต้องเรียก การส่ง HTTP สำเร็จ รูปแบบ model ถูก และคำตอบถูกต้องเป็นคนละเกณฑ์
- Actual chat HTTP หลังแก้: 1400/1,400; delivery validation 1400/1,400
- Latency ก่อน: median 0.453s, p95 6.406s; หลัง: median 0.469s, p95 0.796s ไม่แยก causal effect จาก cache/สภาพเครื่องด้วย

## ความครบถ้วนและไฟล์

- Original references 1131 ไฟล์ hash เดิมครบ; DB เดิม; input/expected ไม่เปลี่ยน; build/model identity ตรวจทั้งก่อนและหลัง
- source facts nonfixture 1,164 จับคู่ native ครบใน scope ที่ตรวจ ไม่ได้หมายความว่าครอบคลุมข้อมูลธุรกิจทุกหัวข้อที่อาจมีคนถาม
```json
{
  "approvals": 0,
  "draft_records": 806,
  "withdrawn_records": 24,
  "active_release": "",
  "published_releases": 0
}
```

- [แผน Flow และเหตุผล](02_IMPLEMENTATION_FLOW_TH.md)
- [ตรวจ source ก่อนรัน](01_SOURCE_REVIEW_TH.md)
- [รายละเอียดข้อที่เคยไม่ผ่านและหลักฐานก่อน/หลัง](ROOT_CAUSE_REVIEW_TH.md)
- [คะแนนเปรียบเทียบและรายชื่อเปลี่ยนแปลง](COMPARISON_FINAL.json)
- [หลักฐานความครบถ้วน](INTEGRITY_FINAL.json)
- [ผลตรวจหลังแก้ครบชุด](runs/http03/TEST_COMPLETE.json)
- [Raw response หลังแก้](runs/http03/RESULTS.jsonl)

## ขั้นถัดไปที่จำเป็นก่อนใช้จริง

ยืนยันขอบเขต/วันมีผลของตารางและเงื่อนไข VR จากเจ้าของ จัดคำแปลอังกฤษที่ขาด ตรวจ live bindings/provider ด้วยขั้นตอนที่เจ้าของอนุญาต แล้วเผยแพร่ draft ตามระบบ approvals ปัจจุบัน ผลรอบนี้เพียงพอสำหรับยืนยันการแก้ช่องโหว่ในชุดคำถามเดิม ไม่ใช่เหตุให้ประกาศว่าทุกหมวดพร้อมจริงหรือเปลี่ยน production อัตโนมัติ
