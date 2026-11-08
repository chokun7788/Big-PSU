import json,re,hashlib,urllib.request,statistics
from pathlib import Path
from datetime import datetime,timezone
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r44_current_path.txt').read_text());RELEASE=Path((OUT/'release_r44_4_path.txt').read_text())
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
summary_path=next(OUT.glob('R44_FINAL_WEB*_summary.json'));summary=json.loads(summary_path.read_text(encoding='utf-8'))
assert summary['passed']==summary['executed_cases']==103
assert summary['health']['runtime']['version']=='2026.10.06-zone-rental-r44.4'
units={}
for path in sorted(OUT.glob('source_regression_*.json')):
    for row in json.loads(path.read_text(encoding='utf-8')):
        log=(OUT/row['evidence']).read_text(encoding='utf-8');count=re.search(r'Ran (\d+) tests',log)
        assert count and row['returncode']==0
        units[row['file']]=dict(methods=int(count[1]),evidence=row['evidence'],passed=True)
assert sum(r['methods'] for r in units.values())==111
with urllib.request.urlopen('http://127.0.0.1:8091/health',timeout=6) as r:health=json.load(r)
assert health['runtime']['version']=='2026.10.06-zone-rental-r44.4' and health['warmup']['ok']
with (OUT/'FINAL_HEALTH_R44_4.json').open('x',encoding='utf-8') as f:json.dump(health,f,ensure_ascii=False,indent=2)
frozen=json.loads((OUT/'release_r44_4_hashes.json').read_text())
unchanged=all((RELEASE/r).is_file() and hashlib.sha256((RELEASE/r).read_bytes()).hexdigest()==v for r,v in frozen.items());assert unchanged
audit=json.loads((OUT/'SOURCE_AUDIT_R44_4_FINAL.json').read_text())
records=[record for case in summary['results'] for record in case['records']]
rental=[r for r in records if r['response']['mode']=='pipeline:zone_rental_fee']
assert all(r['status']==200 and r['response']['ok'] and not r['response'].get('timed_out') for r in records)
assert all(r['response'].get('validation_ok') is True for r in rental)
assert all(r['response']['context_resolution']['context_domain']=='zone_rental' for r in rental)
latency=dict(count=len(rental),median_sec=round(statistics.median(r['elapsed_sec'] for r in rental),4),max_sec=max(r['elapsed_sec'] for r in rental))
gates=dict(runtime_version=health['runtime']['version'],unit_methods=units,unit_total=111,http_cases=103,http_requests=summary['requests'],http_passed=103,http_evidence=summary_path.name,rental_http_latency=latency,original_cells_verified=24,source_release_parity=len(audit['source_release_parity']),source_release_parity_all=all(audit['source_release_parity'].values()),protected_unchanged=all(audit['protected_unchanged'].values()),original_workbook_unchanged=all(audit['workbook_hashes'].values()),final_release_bytes_unchanged=unchanged,owner_missing_fields=['period_hours','effective_dates','rental_booking_procedure','overtime_cost_and_payer','individual_eligibility','hourly_per_unit_multi_day_rental_policy'],live_wordpress_booking_verified_by_this_price_test=False)
with (OUT/'FINAL_AUTOMATED_GATES_R44_4.json').open('x',encoding='utf-8') as f:json.dump(gates,f,ensure_ascii=False,indent=2)
data=json.loads((ROOT/'data/curated/zone_rental_fees_20261006.json').read_text(encoding='utf-8'))
table=['| โซน | ภายนอกครึ่งวัน | ภายนอกเต็มวัน | ภายในครึ่งวัน | ภายในเต็มวัน | ที่นั่ง | อุปกรณ์ |','|---|---:|---:|---:|---:|---:|---|']
for row in data['rows']:
    a=row['prices_thb'];table.append(f"| {row['label']} | {a['external']['half_day']:,} | {a['external']['full_day']:,} | {a['internal']['half_day']:,} | {a['internal']['full_day']:,} | {row['seats']} | {row['equipment_th']} |")
report=f'''# ผลนำเข้าราคาเช่าเหมา r44.4 — 6 ตุลาคม 2026

## ใช้งาน

- เว็บล่าสุด: http://127.0.0.1:8091/ รุ่น `{health['runtime']['version']}`
- โฟลเดอร์รุ่นล่าสุด: `{RELEASE}` เปิด `Open-PSU-Esports-Background.cmd` เมื่อจะใช้อีกครั้ง
- โฟลเดอร์นี้เป็นชุด local ที่ผูก Python ของเครื่องนี้และใช้ Ollama ที่ติดตั้งอยู่ ยังไม่ได้สร้างชุดแจกพร้อมโมเดล/โหลดโมเดลใหม่จาก r44
- เว็บรุ่นเก่า 8090 และโฟลเดอร์รุ่นก่อนยังเก็บไว้ รุ่นเก่าไม่มีข้อมูลราคาใหม่

## ข้อมูลจากไฟล์

ต้นฉบับ: `{data['source_original_filename']}`

Sheet: `{data['source_sheet']}`, ช่วง A1:H8; อ่านทุกเซลล์ที่มีข้อมูลและทุก sheet แล้ว มี 1 sheet ไม่มีสูตร/ภาพ/comment; dimension A1:Z990 รวมพื้นที่ที่จัดรูปแบบแต่ไม่มีข้อมูลจริง

หัวตาราง B:C คือหน่วยงานภายนอก D:E คือหน่วยงานภายใน; B/D ต่อวัน C/E ต่อครึ่งวัน จำนวนราคา 24 ช่องตาม B3:E8 ไม่ใช้การคูณราคาชั่วโมงเก่า

ราคาทั้งหมดหน่วยบาท:

{chr(10).join(table)}

จำนวนที่นั่งเป็นค่าความจุห้อง/โซนที่ไฟล์ระบุ ไม่ใช่จำนวนเครื่องหรือจำนวนผู้เล่นพร้อมกัน เช่น PC มี 43 ที่นั่งและ PC 10 เครื่อง ไม่มีหลักฐานให้แก้ตัวเลขเหล่านี้เอง

หมายเหตุ H3 ที่แถว All Zones: `{data['source_notes'][0]['text_th']}` ไม่ระบุจำนวนเงิน ผู้จ่าย หรือรวมค่าเช่าหรือไม่ ไม่ขยายข้อความนี้เป็นนโยบายที่อนุมัติครบทุกโซน

SHA256 ต้นฉบับและสำเนาทั้งหมด: `{data['source_sha256']}`

## สิ่งที่เปลี่ยน

1. เพิ่ม JSON ตารางเช่าเหมาจากไฟล์ผู้ใช้ และเก็บ Excel สำเนาแบบ byte-identical ใน data/sources; ไม่แก้ต้นฉบับ
2. เพิ่ม source registry และตัวตอบไทย/อังกฤษจากข้อมูลตารางโดยตรง แสดงโซน กลุ่มหน่วยงาน ช่วงราคา ที่นั่ง อุปกรณ์ และแหล่งข้อมูล
3. แยกชนิดแผน `zone_rental_v1` กับราคาเล่นรายชั่วโมงของบุคคล แยก memory key `zone_rental/zone_rental_fee` กับ `service_fee/price_lookup`
4. รับคำถามเฉพาะโซน/กลุ่ม/ช่วง และคำถามต่อเนื่องหลังผู้ใช้ได้รับคำตอบแล้ว; “ทั้งหมด” ขยายรายการโซนโดยคงกลุ่ม/ช่วงที่เลือก; กลับไปเรื่องราคาเหมาได้หลังเปลี่ยนเรื่อง
5. หมวดราคาไม่ผ่าน LLM ให้สร้างตัวเลข; คะแนน .99 เป็นค่าของเส้นทางตอบข้อมูลตรงจากไฟล์ ไม่ใช่ความน่าจะเป็นหรือคะแนนคุณภาพที่วัดจากมนุษย์
6. คำถามข้อมูลที่ไม่มี เช่น กี่ชั่วโมง ขั้นตอนจอง ค่าเจ้าหน้าที่ ต่อเครื่อง ว่างสำหรับเหมาตอนนี้ จะบอกข้อมูลที่ขาด คำตอบบางส่วนมี outcome แยกจากคำตอบครบ
7. ใส่ provenance ต่ออัตรา เช่น `pc:external:full_day` → B8 → 4000 พร้อม source hash ใน trace และ HTTP `zone_rental_contract`

## ผลอัตโนมัติ

| การตรวจ | ผล | ความหมาย |
|---|---:|---|
| Unit ใหม่เช่าเหมา | 19/19 | source cells, capacity/equipment, source limits, typed plans, session/ack, exclusions |
| Unit เดิมที่เกี่ยวข้อง | 92/92 | conversation, task memory, domain resume, schedule, live booking fixtures |
| HTTP เว็บรุ่นสุดท้าย | 103/103 เคส, {summary['requests']} requests | ราคาและคำตอบจริง ไม่ใช่แค่ HTTP เชื่อมต่อสำเร็จ |
| ราคาต้นฉบับ | 24/24 ช่อง | เทียบจาก XML ใน workbook โดยตรง ไม่เอา JSON ที่เพิ่งสร้างมาเป็น oracle ตัวเอง |
| source ↔ release | {len(audit['source_release_parity'])}/{len(audit['source_release_parity'])} ไฟล์ | app/web/curated data ตรงกัน |
| Excel/ข้อมูลเดิม | ผ่าน | ต้นฉบับ สำเนา ราคาเดิม ตารางบริการ และกฎเดิม hash ไม่เปลี่ยน |

ตัวอย่างทดสอบ: ราคาเหมา PC ภายนอกเต็มวัน → 4,000 บาททั้งโซน พร้อม 10 เครื่อง; All Zones ภายนอกเต็มวัน → 12,000 บาทตามแพ็กเกจ ไม่ใช่ผลรวมแยกโซน 16,000; Thai/English; cockpik; unknown Xbox; แพ็กเกจครึ่งวันและเต็มวัน; เรื่องใหม่รายชั่วโมง/เกม; คำถามต่อ “รวมอะไรบ้าง”; resume; หน่วยงานไม่ถูกแมปเป็นนักศึกษาฟรี

เวลาที่วัดเฉพาะคำตอบเช่าเหมาจากไฟล์บนเครื่องนี้ {latency['count']} requests: median {latency['median_sec']} วินาที, max {latency['max_sec']} วินาที เป็นเวลาถึง HTTP response ไม่รวมเวลาวาดหน้าเว็บ และไม่ได้ใช้ WordPress สำหรับราคาชุดนี้

การทดสอบราคาไม่ได้พิสูจน์ว่าตอนนี้ WordPress ตอบสถานะว่าง/ถูกจองถูกต้อง ไม่ได้เก็บสถานะจองจริงมาทำ oracle ในรอบนี้; unit สถานะจองเป็น fixture ที่มี expected outcome

ผลนี้จำกัดกับเคสที่บันทึกไว้ ไม่ใช่การรับรองว่าจะเข้าใจทุกคำถาม/คำสะกด/เงื่อนไขผสม; ไม่รัน full suite สองหมื่นกว่าเคส

## สาเหตุที่พบและแก้ระหว่างรอบ

| รอบหลักฐาน | ผล | สาเหตุ/การแก้ |
|---|---|---|
| R44_INITIAL source | 71/80 | ตัวแยกชื่อที่ไม่รู้จักกินคำส่วนขยาย เช่น ทุกแพ็กเกจ/ทั้งศูนย์/รองรับกี่คน; cockpik ถูก match แล้วแต่ยังคงเป็น unknown; PC1 เหลือเลข 1; Xbox ที่มาก่อน rental ไม่ถูกตรวจ; hourly English canonical query เผลอสืบบริบทเหมา |
| R44_SECOND source | 80/80 | แยก noun span กับข้อมูลที่ถาม ลบ known/fuzzy target อย่างมีขอบเขต รู้ unknown noun ทั้งก่อน/หลัง rental; existing typed hourly plan ต้องไม่ถูก rental resolver ทับ |
| R44_EXTRA_INITIAL source | 9/16 | คำถามรายชั่วโมง/เจ้าหน้าที่/ว่าง/ยกเว้นยังติด unknown และ “รวมอะไรบ้าง/What is included?” ไม่สืบ schema เหมา |
| R44_EXTRA_SECOND source | 16/16 | แยก requested fields; ไม่ยก half/full-day rates เป็นคำตอบราคาเหมารายชั่วโมง; ตอบ included equipment จากแผนที่รับแล้ว |
| ตรวจทานก่อนรุ่นสุดท้าย | แก้และ unit ผ่าน | venue อย่างเดียวต้องไม่สร้าง rental intent; rental price for Xbox และชื่อหลังกลุ่มหน่วยงานต้องไม่ fallback เป็นทุกโซน |
| R44_FINAL_WEB r44.4 | 103/103 | ตรวจ trace/output/ราคา/ภาษาที่แสดง/source hash และเทียบ original cell oracle |

Raw/failed logs และ candidate r44.1/.2/.3 เก็บไว้ทุกชุด ไม่มีการลบผลที่เคยไม่ผ่าน

เคส “Where is the venue?” ใช้เป็น negative test ว่าต้องไม่ตอบราคาเหมา; เว็บตอบ `english_no_answer` จึงไม่ได้ถือว่าทดสอบคำตอบเรื่องสถานที่ผ่าน เป็นจุดปรับการรับคำถามอังกฤษที่ยังทำเพิ่มได้ภายหลัง ส่วน “What are the venue opening hours?” ไป schedule ตามเดิม

## ต้องให้เจ้าของศูนย์ยืนยัน

1. “ครึ่งวัน” และ “เต็มวัน” นับกี่ชั่วโมง เริ่ม–สิ้นสุดกี่โมง? เลือกช่วงใดได้ และเกี่ยวกับพักกลางวัน/Maintenance/วันปิดพิเศษ/นอกเวลาปกติอย่างไร?
2. ตารางราคาเริ่มใช้วันที่ใดและมีวันสิ้นสุดหรือไม่? วันที่ 6 ต.ค. ใน registry เป็นวันที่รับข้อมูล ไม่ใช่วันมีผลของราคา
3. จองเหมาได้ช่องทางไหน ต้องยื่นอะไร ล่วงหน้ากี่วัน ชำระ/มัดจำ/ยกเลิกอย่างไร? ไม่เอากฎเล่นทั่วไปสูงสุด 3 sessions มากำหนดการเช่าเหมาเอง
4. ค่าเจ้าหน้าที่นอกเวลารวมในราคาไหม? ใครเป็นผู้จ่ายและคำนวณ/เบิกอย่างไร? หมายเหตุ H3 ใช้เฉพาะ All Zones หรือทุกโซน?
5. บุคคลทั่วไป/นักศึกษา/บุคลากรที่ไม่ได้จองในนามหน่วยงานใช้ราคาใด? นิยามหน่วยงานภายใน/ภายนอกเป็นอย่างไร?
6. มีราคาเหมาโซนรายชั่วโมง ต่อเครื่อง หลายวัน หรือส่วนลดไหม? ถ้ามีให้ส่งตารางอนุมัติแยก ไม่คำนวณอัตราขึ้นมาเอง

ข้อเหล่านี้ไม่ได้ขัดขวางการตอบ 24 อัตราที่อยู่ในไฟล์ แต่ระบบยังยืนยันเงื่อนไขที่ไม่ได้ส่งมาให้ไม่ได้

## หลักฐาน

- ผลสุดท้าย: `{summary_path.name}` + JSONL raw ที่ระบุใน summary
- `FINAL_AUTOMATED_GATES_R44_4.json`, `FINAL_HEALTH_R44_4.json`
- `SOURCE_AUDIT_R44_4_FINAL.json`, `SOURCE_CHANGE_R44_4_FINAL.diff`, Git status/diff-check
- `WORKBOOK_EXTRACTION.json`, `FLOW_R44_FINAL.md`
- ชุดทดสอบ: `{ROOT / 'tests/test_zone_rental_r44.py'}`
'''
with (OUT/'REPORT_R44_FINAL_TH.md').open('x',encoding='utf-8') as f:f.write(report)
flow='''# Flow r44 ฉบับปรับปรุง: ราคาเช่าเหมาโซนจาก workbook

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
'''
with (OUT/'FLOW_R44_FINAL.md').open('x',encoding='utf-8') as f:f.write(flow)
print('REPORT',OUT/'REPORT_R44_FINAL_TH.md','GATES',111,summary['passed'],summary['requests'],'rental latency',latency)
