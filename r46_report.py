import json,re,hashlib,statistics,urllib.request
import r46_probe as r
out=r.OUT
def latest(pattern):
    return json.loads(max(out.glob(pattern),key=lambda p:p.stat().st_mtime).read_text(encoding='utf-8'))
initial=latest('R46_INITIAL_WEB*summary.json');source=latest('R46_SOURCE_REGRESSION*summary.json');final=latest('R46_FINAL_WEB*summary.json')
assert final['passed']==final['executed_cases']==181
unit=latest('source_regression_*.json');assert all(x['returncode']==0 for x in unit)
unit_count=sum(int(re.search(r'Ran (\d+) tests', (out/x['evidence']).read_text(encoding='utf-8'))[1]) for x in unit)
assert unit_count==86
with urllib.request.urlopen('http://127.0.0.1:8091/health',timeout=6) as response:health=json.load(response)
assert health['runtime']['version']=='2026.10.07-english-rental-r46.1'
workbook_sha=hashlib.sha256((r.prior.r.p.ROOT/'data/sources/zone_rental_fees_20261006.xlsx').read_bytes()).hexdigest()
assert workbook_sha==r.prior.r.x['sha256']
with (out/'FINAL_HEALTH_R46.json').open('x',encoding='utf-8') as f:json.dump(health,f,ensure_ascii=False,indent=2)
audit=json.loads((out/'SOURCE_AND_RELEASE_AUDIT_R46.json').read_text())
lookup={x['id']:x for x in final['results']}
english=[lookup[x['id']] for x in initial['results']]
assert len(english)==33 and all(x['passed'] for x in english)
latencies=[rec['elapsed_sec'] for x in english for rec in x['records'] if rec['response'].get('mode')=='pipeline:zone_rental_fee']
counts=dict(initial_english_passed=initial['passed'],initial_english_total=33,final_english_passed=33,final_english_total=33,final_combined_passed=181,final_combined_total=181,http_requests=final['requests'],unit_tests_passed=unit_count,source_release_hashes_passed=audit['passed_file_checks'],rental_http_median_sec=statistics.median(latencies),rental_http_max_sec=max(latencies),source_workbook_sha256=workbook_sha)
with (out/'FINAL_AUTOMATED_GATES_R46.json').open('x',encoding='utf-8') as f:json.dump(counts,f,indent=2)
causes={
 'en-whole-day':'FULL regex รองรับ whole day แต่ไม่รองรับ whole-day จึงคงค่าเริ่มต้นสองช่วง แก้ให้เป็นเต็มวันเท่านั้น',
 'en-people':'ตัวตรวจ follow-up ไม่รวม how many people แม้ตัวแยก field รู้จัก capacity ทำให้หลุดไปถามยืนยัน แก้ให้ใช้ผลแยก field ร่วมกัน',
 'en-duration':'ตัวตรวจ follow-up ไม่รวม how long แม้ตัวแยก field รู้จัก duration จึงเห็นแค่ full day และตอบราคา ต้องตอบว่าไฟล์ไม่ระบุจำนวนชั่วโมง',
 'en-reserve':'รู้จัก reserve ในตัวแยก field แต่ตัวตรวจบริบทรับเฉพาะ how do I book it ต้องรักษาบริบทเช่าเหมาและแจ้งว่าไฟล์ไม่ระบุขั้นตอน',
 'en-booking-procedure':'booking เป็นคำถามข้อมูลที่ไม่มีชื่อโซน ตัวตรวจ follow-up เดิมพลาด จึงหลุด retrieval ต้องใช้ rental context ที่ client รับแล้ว',
 'en-effective':'prices ทำให้เป็น generic_price แต่ take effect ไม่อยู่ใน effective_date จึงส่งราคาเดิม ต้องตอบว่าไม่ระบุวันที่มีผล',
 'en-typo-cockpit':'service_mentions ปิด fuzzy เมื่อทั้งประโยคยาวเกิน 50 ตัว ขณะที่ตัวสกัด unknown ลบ token ที่ fuzzy รู้จักออก ทำให้ไม่มี target/unknown แล้วใช้ทุกโซน แก้ใช้ fuzzy token เดิมกับประโยคยาวในขอบเขตเช่าเหมา',
 'en-generic-exclusion':'พบ VR แล้วตัดออกจน targets ว่าง ตัวสร้าง plan ใช้ทุกโซนค่าเริ่มต้นทำให้ VR กลับมา แก้ให้ค่าเริ่มต้นถูกกรองตั้งแต่ต้น',
 'en-per-machine':'per machine ถูกจับเป็น field และ noun ที่ไม่รู้จักพร้อมกัน ต้องเป็นคำขอราคาต่อเครื่องที่ไฟล์ไม่มี ไม่ใช่สินค้าใหม่',
 'en-compound-versus':'แยก clause เฉพาะ and/และ/semicolon ทำให้ versus ตกเป็น unknown และ union เงื่อนไขกลายเป็น Cartesian product แก้แยกตาม versus',
 'en-compound-with':'compare...with ไม่แยก clause และ compare/with กลายเป็น unknown แก้แยก with เฉพาะประโยค compare แล้วเก็บเงื่อนไขราย clause',
}
lines=['# วิเคราะห์เคสอังกฤษ r46','',f'ก่อนแก้ {initial["passed"]}/33; หลังแก้ 33/33 ในชุดอังกฤษใหม่; ชุดรวมผ่าน 181/181','',
 '## การอ่านคะแนน','', 'confidence 0.99 ของ route เช่าเหมาเป็นค่าที่กำหนดในโค้ด ไม่ใช่ความแม่นยำจากการประเมิน ตัว builder ตอบตาม plan: ถ้า parser ขยาย target/period ผิด คำตอบจากเซลล์จริงก็ยังผิดความต้องการได้ เกณฑ์ทดสอบจึงตรวจ ID ราคา + ค่า + source hash + missing fields + คำตอบที่แสดง แยกจาก HTTP 200 และ validation_ok','',
 '## แต่ละเคส','']
for old in initial['results']:
    new=lookup[old['id']];b=old['records'][-1]['response'];n=new['records'][-1]['response']
    meta=b.get('zone_rental_contract') or {};nm=n.get('zone_rental_contract') or {}
    lines+=['### '+old['id'],'','คำถาม/ลำดับ: '+' → '.join(x['payload']['question'] for x in old['records']),'',
      'ผลก่อนแก้: '+('ผ่าน' if old['passed'] else 'ไม่ผ่าน')+'; เกณฑ์ที่พลาด: '+', '.join(k for k,v in old['checks'].items() if not v),'',
      causes.get(old['id'],'เคสนี้ผ่านอยู่แล้ว เก็บไว้ตรวจว่าแก้เคสอื่นแล้วไม่กระทบเงื่อนไขเดิม'),'','Expected rates: `'+json.dumps(next(c for c in r.cases() if c['id']==old['id']).get('expected',{}))+'`','',
      'Plan ก่อนแก้: `'+json.dumps(meta.get('request_plan',{}),ensure_ascii=False)+'`','',
      'คำตอบก่อนแก้:','',b.get('answer',''),'','ผลหลังแก้: '+str(new['passed'])+'; rates: `'+json.dumps(nm.get('returned_rates',[]))+'`; missing fields: `'+json.dumps(nm.get('missing_fields',[]))+'`','','คำตอบหลังแก้:','',n.get('answer',''),'']
with (out/'CASE_ANALYSIS_R46_ENGLISH_TH.md').open('x',encoding='utf-8') as f:f.write('\n'.join(lines)+'\n')
report=f'''# สรุป r46: รองรับคำถามเช่าเหมาเป็นภาษาอังกฤษ

## ทำแล้ว
- เพิ่ม 33 เคสอังกฤษ: คำถามสุภาพ สำนวนหลายแบบ พิมพ์ผิด follow-up การเลือกช่วง/กลุ่ม การตัดรายการ และการเปรียบเทียบราคาเงื่อนไขต่างกัน
- รอบแรกผ่าน 22/33; วิเคราะห์และแก้ 11 จุดที่พบ โดยแก้ไฟล์เดิมเฉพาะ app/pipeline/zone_rental.py และเพิ่ม tests/test_english_rental_r46.py
- whole-day จับเป็นเต็มวัน; คำถาม how many people/how long/reserve/booking procedure/take effect ใช้บริบทและ field ถูกต้อง
- typo token ในประโยคยาวใช้ fuzzy service matcher เดิม; PS55/Xbox ยังไม่ถูกเดาเป็นเครื่องที่มี
- versus และ compare...with รักษา target/group/period ของแต่ละ clause ราคาคนละเงื่อนไขไม่ปนกัน
- ยกเว้น VR ไม่กลับเข้ามาตอนใช้ defaults; per machine เป็น field ที่ไม่มีราคายืนยัน

## ผลอัตโนมัติ
- อังกฤษใหม่: **33/33** ผ่าน HTTP จริงหลังแก้ (ก่อนแก้ **22/33**)
- Regression ไทย+อังกฤษเกี่ยวข้องรวม: **181/181** ผ่าน ทั้ง source และ HTTP; HTTP **{final['requests']} requests**
- Unit tests: **86/86** ผ่านใน 5 ไฟล์
- Source/release: **155/155** ไฟล์ตรงกัน; Git diff --check exit 0
- ราคาตรวจ ID/ค่าโดยเทียบเซลล์จาก workbook เดิมและ SHA256 ไม่ใช่แค่ API เชื่อมสำเร็จ
- HTTP rental ในชุดอังกฤษ median {statistics.median(latencies):.4f}s, max {max(latencies):.4f}s; ไม่รวมการวาดหน้าเว็บ/การดึง WordPress
- Source workbook hash ยังเดิม: {workbook_sha}

## เกณฑ์ผ่านมีขอบเขต
- เคสเปลี่ยนหัวข้อบางข้อเช็คเพียงว่าไม่ตอบราคาเหมา เช่น en-venue-location ยังเป็น english_no_answer ไม่ใช่ผ่านความถูกต้องเรื่องสถานที่
- เคส missing เช่นขั้นตอนจอง/ชั่วโมง/วันที่มีผล ผ่านเมื่อแจ้งว่าไฟล์ไม่ระบุ ไม่ได้หมายถึงข้อมูลนั้นได้รับการยืนยันแล้ว
- ไม่ได้รัน full suite 20k หรือยืนยันสถานะว่างจริงจาก WordPress ในรอบนี้
- ตัวเลข confidence 0.99 เป็น route constant ไม่ใช่ความน่าจะเป็นว่าคำตอบถูกทุกประโยค

## เจ้าของยังต้องยืนยัน
จำนวนชั่วโมง/ช่วงเวลาเช่าครึ่งวันและเต็มวัน; วันที่มีผล; วิธีจองเหมา; ค่าเจ้าหน้าที่และการรวมราคา; สิทธิ์บุคคล; รายชั่วโมง/หลายวัน/ส่วนลด/แพ็กเกจตัดโซน ยังไม่มีใน workbook และไม่เดาเพิ่ม

## ใช้งาน
เว็บ http://127.0.0.1:8091/ ใช้ **2026.10.07-english-rental-r46.1**; เปิดภาษาอังกฤษก่อนถาม
release: {(out/'release_r46_1/PSU_Esports_Chatbot_Local')}
release นี้เป็น local runtime อ้าง Python/Ollama บนเครื่องเดิม ยังไม่ได้ปรับแพ็กแจกจ่ายพร้อม/ไม่พร้อมโมเดลสองแบบ

## หลักฐาน
- FLOW_R46_ENGLISH.md: flow และเกณฑ์ตรวจ
- CASE_ANALYSIS_R46_ENGLISH_TH.md: ทุกคำถาม expected/plan/คำตอบก่อนและหลัง
- R46_INITIAL_WEB*, R46_SECOND_SOURCE*, R46_SOURCE_REGRESSION*, R46_FINAL_WEB*: raw responses/trace/checks ทุก run ไม่ทับผลเดิม
- FINAL_AUTOMATED_GATES_R46.json, FINAL_HEALTH_R46.json, SOURCE_AND_RELEASE_AUDIT_R46.json, SOURCE_CHANGE_R46.diff
- before/: snapshot งานเดิม; GIT_STATUS_R46.txt และ GIT_DIFF_CHECK_R46.txt เก็บสถานะ
'''
with (out/'REPORT_R46_FINAL_TH.md').open('x',encoding='utf-8') as f:f.write(report)
print(json.dumps(counts,ensure_ascii=False))
