import json,re,statistics,urllib.request
from pathlib import Path
import r47_probe as r
out=r.OUT
def latest(pattern):return json.loads(max(out.glob(pattern),key=lambda p:p.stat().st_mtime).read_text(encoding='utf-8'))
initial=latest('R47_INITIAL_WEB*summary.json');final=latest('R47_FINAL_WEB*summary.json');focused=latest('R47_FIFTH_SOURCE*summary.json')
assert final['passed']==final['executed_cases']==206
assert focused['passed']==focused['executed_cases']==25
units=latest('source_regression_*.json');assert len(units)==4 and all(x['returncode']==0 for x in units)
unit_count=sum(int(re.search(r'Ran (\d+) tests',(out/x['evidence']).read_text(encoding='utf-8'))[1]) for x in units);assert unit_count==50
audit=json.loads((out/'SOURCE_AND_RELEASE_AUDIT_R47.json').read_text())
with urllib.request.urlopen('http://127.0.0.1:8091/health',timeout=6) as response:health=json.load(response)
assert health['runtime']['version']=='2026.10.07-answer-content-r47.1'
with (out/'FINAL_HEALTH_R47.json').open('x',encoding='utf-8') as f:json.dump(health,f,ensure_ascii=False,indent=2)
lookup={x['id']:x for x in final['results']};final_location=[lookup[c['id']] for c in r.cases() if c['kind']=='location']
latencies=[x['records'][-1]['elapsed_sec'] for x in final_location]
gates=dict(initial_focused_passed=initial['passed'],initial_focused_total=initial['executed_cases'],final_focused_passed=25,final_focused_total=25,final_combined_passed=206,final_combined_total=206,http_requests=final['requests'],unit_tests_passed=unit_count,source_release_hashes_passed=audit['passed_file_checks'],address_http_median_sec=statistics.median(latencies),address_http_max_sec=max(latencies),owner_facts_changed=False,limitations=['targeted tests only','legacy existing English address reused, no new human approval','cancel acknowledgement still not resolved','live WordPress occupancy correctness not checked','portable distributions not rebuilt'])
with (out/'FINAL_AUTOMATED_GATES_R47.json').open('x',encoding='utf-8') as f:json.dump(gates,f,indent=2)
old={x['id']:x for x in initial['results']}
old_source=latest('R47_FOURTH_SOURCE*summary.json')
for x in old_source['results']:old.setdefault(x['id'],x)
lines=['# วิเคราะห์คำตอบและเกณฑ์เนื้อหา r47','',
 '## ผลก่อน/หลัง','',f'ชุด HTTP ก่อนแก้ {initial["passed"]}/{initial["executed_cases"]}; หลังแก้ชุดเฉพาะ 25/25 และชุดรวม HTTP 206/206 ({final["requests"]} requests). Unit tests 50/50. ผลนี้ไม่ใช่ความแม่นยำของทุกคำถามที่เป็นไปได้','',
 '## สาเหตุจาก trace','',
 '### 1. อังกฤษมีคำตอบ แต่รูปประโยคไม่ตรงตัวรับคำถาม','',
 'Where is the venue? ไม่มี location/address และไม่ได้ใช้ studio/PSU Esports ที่ legacy regex กำหนด RuleMatcher ไม่พบผล และ English path ห้ามตกไปตอบไทย จึงคืน english_no_answer. r46 นับเคสนี้ผ่านเพราะเช็คเพียงว่า mode ไม่ใช่ราคาเหมา ไม่ได้เช็คว่าคำตอบมีที่อยู่จริง','',
 'แก้: ตีความคำถามสถานที่ของศูนย์แล้วใช้ bilingual contact_location rule เดิม ส่ง source ID curated_contact_location และ URL เดิม เกณฑ์ใหม่บังคับ category contact + เนื้อหาที่อยู่ตรง record + URL + ไม่ใช่ no_answer','',
 '### 2. ภาษาไทยหาเจอข้อมูล แต่ frame บังคับประเภทคำตอบผิด','',
 'ศูนย์อยู่ที่ไหน: route contact/contact_lookup → Local LLM contact/detail confidence 0.9 → question_frame equipment/equipment_lookup confidence 0.92 เพราะ looks_like_equipment_query มีคำว่าอยู่ที่ไหนโดยไม่ต้องมีชื่ออุปกรณ์ → decision_candidates เลือก structured.equipment score 0.789 → category_rule_base พบ rule_contact_location → validation ปฏิเสธ answer_contract_type_mismatch expected equipment,list actual fact,summary และ answer_contract_source_domain_mismatch expected equipment actual contact → curated retrieval ก็ถูกปฏิเสธด้วยกรอบเดิม → no_answer แม้มีข้อมูลจริง','',
 'แก้: รักษา frame หมวด contact ก่อน generic equipment-location cue และใช้ resolver ที่ผูกคำถามที่ตั้งภาษาไทยกับ curated fact เดิมก่อน late ambiguity gate สำหรับขอที่อยู่ศูนย์/ที่ตั้ง PSU Esports Studio','',
 '### 3. ชื่อสถานที่อื่นถูกแทนด้วยที่อยู่ PSU','',
 'Where is the Xbox studio in Bangkok? เดิม matched regex where is ... studio ซึ่งอนุญาตคำใดก็ได้ระหว่าง is กับ studio จึงตอบที่อยู่ PSU ทั้งที่ subject ไม่ตรง แก้ตรวจ noun/คำที่ยังไม่ resolve และถามยืนยัน ไม่ใช้ที่อยู่ PSU เป็นคำตอบของสถานที่นั้น','',
 '### 4. จุดที่พบขณะพัฒนาและข้อผิดพลาดของเทส','',
 '- Resolver ไทยรอบแรกใช้ row.id เป็น key แต่ canonical projection มี id curated_contact_location::th::text และ content_id curated_contact_location ทำให้หา record ไม่เจอ แก้ใช้ content_id ตามตัวระบุหลัก ตรวจ unit และ HTTP ซ้ำ','',
 '- เกณฑ์ catalog_source รอบแรกกำหนด URL our-games ให้ทั้งไทยและอังกฤษ แต่คำตอบไทยเป็นรายการเกมแยกเลขเครื่องจาก service_game_availability ซึ่งอ้าง esports.computing.psu.ac.th/ จริง แก้ oracle ให้ตรงแหล่งข้อมูลต้นฉบับของแต่ละชุด โดยไม่แก้คำตอบที่ถูกอยู่แล้ว','',
 '## การอ่านคะแนน','',
 'Confidence ของ routing/intent/frame เป็นคะแนนของแต่ละขั้น ไม่ได้ยืนยันว่ามีเนื้อหาที่ตอบคำถามได้ Candidate score 0.789 เป็นคะแนนการเลือก capability ไม่ใช่ความถูกต้องของที่อยู่ ส่วน English location handler 0.98 เป็นค่าที่กำหนดในโค้ด การผ่านจึงต้องใช้เกณฑ์เนื้อหาและแหล่งข้อมูลร่วมด้วย','',
 '## เกณฑ์เดิมที่เพิ่มความเข้ม','',
 '- en-venue-location: ต้องตอบที่อยู่จริงและอ้าง record','- en-venue-hours: ต้องมีช่วงเปิด/พัก/maintenance ตามวัน','- การเปลี่ยนจากเหมาเป็น PC รายชั่วโมง: ต้องมี 25/70 และ source local update ที่มีหลักฐาน','- เปลี่ยนเป็น PC games: ต้องมีรายชื่อ PC และไม่แทรกโซนอื่น พร้อม URL ของแหล่งรายการจริง','- เปลี่ยนเป็น CS2 rules: ต้องมีเนื้อหา format/team จาก rulebook CS2 ไม่ใช่แค่หลุดจากราคาเหมา','',
 '## ขอบเขตที่ยังไม่ใช่ผลยืนยัน','',
 'คำถามยกเลิก th-cancel-rental-prices ยังเป็น ambiguity_clarification; เกณฑ์เดิมตรวจเฉพาะไม่ส่งราคาเหมาเดิมซ้ำ ยังไม่ได้แก้ข้อความรับทราบการยกเลิก. ข้อมูลขั้นตอน/ชั่วโมงเช่าเหมาที่ไม่มีใน workbook ยังคงขาด. ไม่มีการยืนยันข้อมูลจองสดกับ oracle จริงหรือทดสอบ UI render. ที่อยู่ภาษาอังกฤษนำจาก record เดิม ไม่ได้อ้างว่าผ่านมนุษย์ตรวจเพิ่มในรอบนี้','',
 '## ทุกเคสเฉพาะที่ตรวจ','']
for c in r.cases():
    b=old[c['id']]['records'][-1]['response'];n=lookup[c['id']]
    lines+=['### '+c['id'],'','คำถาม: '+' → '.join(c['turns']),'',
      'ก่อนแก้: '+old[c['id']]['mode']+'; failed checks: '+', '.join(k for k,v in old[c['id']]['checks'].items() if not v),'',b.get('answer',''),'','หลังแก้: '+n['mode']+'; checks: `'+json.dumps(n['checks'],ensure_ascii=False)+'`','',n['answer'],'']
with (out/'CASE_ANALYSIS_R47_TH.md').open('x',encoding='utf-8') as f:f.write('\n'.join(lines)+'\n')
report=f'''# สรุป r47: แก้เคสมีข้อมูลแต่ตอบไม่ได้ และเพิ่มเกณฑ์ตรวจเนื้อหา

## ทำเสร็จ
- Where is the venue?/studio/centre และสำนวนสถานที่อังกฤษตอบจากที่อยู่ที่มีอยู่แล้ว
- ศูนย์อยู่ที่ไหน/ขอที่อยู่ศูนย์/ที่ตั้ง PSU Esports Studio ตอบข้อมูลเดิมได้
- คำถาม Xbox studio in Bangkok ไม่ได้ถูกแทนด้วยที่อยู่ PSU; ถามยืนยันชื่อสถานที่
- อุปกรณ์ เกม สมาชิก และสถานที่แข่งขันมีขอบเขตของตัวเอง; คำถามเดินทางให้ที่อยู่และแจ้งว่าข้อมูลเส้นทางไม่มี
- เพิ่มเกณฑ์เนื้อหาให้เคสเก่าที่เคยตรวจเพียงไม่ตอบราคาเหมา

## ผล
- ก่อนแก้ HTTP ชุดแรก **{initial['passed']}/{initial['executed_cases']}**
- ชุดเฉพาะสุดท้าย **25/25** ผ่าน source และ HTTP
- รวมไทย/อังกฤษที่เกี่ยวข้อง **206/206** ผ่าน HTTP **{final['requests']} requests** ด้วย Local LLM เปิดใช้งาน
- Unit tests สุดท้าย **50/50** ผ่าน 4 ไฟล์
- Source/release **{audit['passed_file_checks']}/{audit['total_file_checks']}** hashes ตรง; Git diff --check exit 0
- คำถามที่อยู่ HTTP median {statistics.median(latencies):.4f}s; max {max(latencies):.4f}s ไม่รวมการ render หน้าเว็บ

## เปลี่ยนไฟล์ใด
แก้ app/pipeline/bilingual_english.py, app/pipeline/question_frame.py, app/pipeline/closed_query_improvements.py และเพิ่ม tests/test_studio_location_r47.py
ข้อมูล data/rules และ data/curated ทุกไฟล์ใน snapshot ไม่เปลี่ยน; address/translation ใช้ record เดิม ไม่มีการเพิ่มนโยบายหรือสถานที่โดยเดา
เก็บ before snapshot, ทุก run/raw/trace, diff และ Git status แยกไฟล์; ไม่ reset/stash/commit หรือทับ log เดิม

## ยังเหลือ
- คำถามยกเลิกยังต้องปรับข้อความตอบรับและการปิดบริบท (งานถัดไปข้อ 2); เคสนี้ยังผ่านเฉพาะเกณฑ์ไม่ส่งราคาเดิมซ้ำ
- ไม่ได้ยืนยันสถานะจองสดจากข้อมูลจริง ไม่ได้รัน full 20k และไม่ได้ปรับแพ็กแจกทั้งสองแบบ
- ชั่วโมง/วิธีจอง/วันที่มีผล/ค่าเจ้าหน้าที่เช่าเหมายังรอหลักฐานเจ้าของ
- นำคำแปลที่อยู่เดิมมาใช้ ไม่อ้างว่าได้รับ human approval ใหม่; ผลผ่านเป็นชุดคำถามจำกัด ไม่ใช่ทุกสำนวน

## ใช้งาน
http://127.0.0.1:8091/ — รุ่น **2026.10.07-answer-content-r47.1**
release local: {out/'release_r47_1/PSU_Esports_Chatbot_Local'}
ชุดนี้อ้าง runtime Python/Ollama เดิมบนเครื่อง ไม่ใช่แพ็ก portable ที่แจกคนอื่นได้ทันที

## หลักฐาน
FLOW_R47_CONTENT.md, CASE_ANALYSIS_R47_TH.md, FINAL_AUTOMATED_GATES_R47.json, FINAL_HEALTH_R47.json, SOURCE_AND_RELEASE_AUDIT_R47.json, SOURCE_CHANGE_R47.diff และ raw/summary R47_* ทุก run
'''
with (out/'REPORT_R47_FINAL_TH.md').open('x',encoding='utf-8') as f:f.write(report)
with (out/'FLOW_R47_FINAL.md').open('x',encoding='utf-8') as f:f.write((out/'FLOW_R47_CONTENT.md').read_text(encoding='utf-8')+'\n## Reviewed outcome\n- Address content and domain/source checks are mandatory; non-rental mode alone is insufficient.\n- Thai contact frame guard and explicit source-bound Thai resolver were added after trace analysis.\n- Canonical source lookup uses content_id; catalog URL checks follow the actual source dataset.\n- Focused 25/25, final HTTP 206/206, unit 50/50; no owner data changes.\n- Cancel acknowledgment, live occupancy oracle and portable package update remain distinct follow-up work.\n')
print(json.dumps(gates,ensure_ascii=False))
