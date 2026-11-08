import hashlib,json,subprocess
from pathlib import Path
project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
root=Path(__file__).parent;report=Path((root/'r26_report_path.txt').read_text(encoding='utf-8').strip())
pkg=project/'owner_local_delivery_20261001_competition_content_speed_r26_ready/PSU_Esports_Chatbot_Local'
freeze=json.loads((report/'ready_code_manifest.json').read_text(encoding='utf-8'))
for relative,h in freeze.items():
 assert hashlib.sha256((project/relative).read_bytes()).hexdigest()==h,relative
 if not relative.startswith('tests/'):assert hashlib.sha256((pkg/relative).read_bytes()).hexdigest()==h,relative
before=json.loads((report/'before_manifest.json').read_text(encoding='utf-8'))
protected={relative:{'before':h,'after':hashlib.sha256((project/relative).read_bytes()).hexdigest()} for relative,h in before.items() if relative.startswith(('data/','booking_dashboard/','docs/')) or relative=='app/pipeline/bilingual_english.py'}
assert all(row['before']==row['after'] for row in protected.values())
unit=json.loads((report/'round_F_unit.json').read_text(encoding='utf-8'))
content=json.loads((report/'final_ready_live_8090_content.json').read_text(encoding='utf-8'))
http=json.loads((report/'http_final_ready.json').read_text(encoding='utf-8'))
large=json.loads((report/'full_r26_D_ready_summary.json').read_text(encoding='utf-8'))
review=json.loads((report/'full_r26_D_ready_source_presence_review.json').read_text(encoding='utf-8'))
assert unit['success'] and content['passed']==80 and http['passed']==36
assert not review['unresolved_ids']
summary={'runtime_version':'2026.10.01-competition-content-speed-r26','ready_package':str(pkg),'web':'http://127.0.0.1:8090/','unit_tests':unit['tests'],'unit_passed':unit['success'],'http_content_cases':80,'http_content_passed':content['passed'],'http_regression_cases':36,'http_regression_passed':http['passed'],'http_regression_range_sec':[min(r['elapsed_sec'] for r in http['cases']),max(r['elapsed_sec'] for r in http['cases'])],'large_total':large['total'],'large_raw_stats':large['stats'],'large_source_presence_resolved':review['source_presence_resolved'],'large_source_presence_after_review':review['source_presence_passed_after_review'],'large_semantic_accuracy':'not established for all 2000 cases; bounded 16-anchor content fixtures are separate','protected_files':protected,'ready_code_matches_snapshot':True,'package_runtime_files_match':7,'owner_approval':False,'prior_timeout':'R24-TH-tekken8-105 in B: 719.2584s; replay passed in 1.5759s; final D no latency failure; cause unconfirmed'}
with (report/'FINAL_VERIFICATION.json').open('x',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
ui={'method':'Cua browser DOM/accessibility plus visual inspection; synthetic requests; no Correct feedback buttons submitted','candidate_8092_th_penalty_types':{'question':'กติกกา VALORANT มีบทลงโทษประเภทไหนบ้าง','types':5,'sources':'s11-s15','latency_ms':180,'old_notice_requested_retype':True},'final_ui_th_penalty_types':{'types':5,'latency_ms':175,'notice':'พบตัวอักษรซ้ำ ระบบประมวลผลคำถามต่อแล้ว กรุณาตรวจว่าคำตอบตรงกับสิ่งที่ต้องการถาม'},'final_ui_en_penalty_types':{'question':'What do the VALORANT tournament ruules say about penalties?','types':5,'source':'s25','latency_ms':72,'notice':'Repeated characters detected. Your question was processed; please check whether the answer matches what you meant.'},'ready_en_format':{'question':'Hi, What is the Tekken 8 tournamment format?','first_line':'Answer: Singles (1v1) format','detail':'FT2: Winner is the first to win two games','source':'competition_rules_tekken8_psu_esports_s02_c01','latency_ms':570,'hardware_first_line':False},'created_test_tab_closed':True,'owner_validation':False}
with (report/'ui_verification.json').open('x',encoding='utf-8') as f:json.dump(ui,f,ensure_ascii=False,indent=2)
with (report/'git_status_final.txt').open('x',encoding='utf-8') as f:f.write(subprocess.run(['git','status','--short'],cwd=project,capture_output=True,text=True,encoding='utf-8').stdout)
flow=project/'docs/126_competition_content_speed_r26_flow_20261001.md'
with (report/'flow_initial.md').open('x',encoding='utf-8') as f:f.write(flow.read_text(encoding='utf-8'))
results=f'''## ผลการดำเนินงาน — รุ่นพร้อมใช้
แพ็กเกจ: `{pkg}`
เวอร์ชัน: `2026.10.01-competition-content-speed-r26`
เว็บ: http://127.0.0.1:8090/

| การตรวจ | ผล | ขอบเขต |
| --- | --- | --- |
| Unit/regression รอบ F | 113/113 | source scope, first line, negative controls, coverage, route, booking และ typo |
| เนื้อหาเว็บจริง | 80/80 | ไทย 40 อังกฤษ 40, 16 ประเด็น × 5 รูปคำถาม; ไม่ใช่ทุกความหมายที่ผู้ใช้อาจถาม |
| HTTP รุ่นพร้อมใช้ | 36/36 | คำถามเดิมของผู้ใช้, history เปลี่ยนเกม, source gap, catalog, booking, penalty, typo; LLM/semantic เปิด |
| HTTP เวลา | {summary['http_regression_range_sec'][0]}–{summary['http_regression_range_sec'][1]}s | 36 เคสที่วัด ไม่ใช่คำรับประกันทุกคำถาม |
| GT ใหญ่ รอบ D | 1953/2000 ดิบ | ไทย 1000 อังกฤษ 1000; LLM/semantic ปิด |
| review ของ 47 fails | พบ source clause เต็ม 47/47 | ยืนยัน source presence เพิ่ม ไม่ใช่ตรวจ semantic ครบทุกคำตอบ |
| hash ไฟล์ป้องกัน | {len(protected)}/{len(protected)} เหมือนก่อนแก้ | source, Gold, review queue, English CURRENT, ownerschedule, r25 flow, bilingual English |
| package/code snapshot | 7/7 runtime files ตรง | สำเนา ready_code 8 ไฟล์รวม test |

### การวนตรวจและแก้ที่ทำจริง
1. Baseline fixture v1: 68/80; แยก 5 oracle wording errors ออกจาก 7 response errors ด้วย source
2. รอบ A: content 80/80 แต่ unit พบ no_answer mode และ age detail guard ยังผิด
3. รอบ B/C: mode และ age guard ถูก; เพิ่ม positive/negative age-value tests, unit 112/112
4. ตรวจ UI จริง: notice ขอพิมพ์ใหม่หลังตอบสำเร็จ แก้ copy ไทย/อังกฤษ; ไม่เปลี่ยน guard/log
5. ตรวจคำตอบเต็ม HTTP: English tournament format ประโยคแรกเป็น hardware; เพิ่ม facet และ first-line assertions
6. Fixture v3 รอบ D: 75/80 แสดงว่าหัวข้อไทยยังแทนคำตอบตรงประเด็นอยู่
7. รอบ E: เริ่มด้วย 1v1/FT2 แต่ regression พบค่า 60 วินาทีหาย จึงคืน settings ที่ผูกกับส่วนรูปแบบเดียวกัน
8. รอบ F: unit 113/113 และ fixture 80/80; freeze โค้ดก่อน full GT รุ่นพร้อมใช้
9. full A=1953/2000; B=1952/2000 มี timeout หนึ่งเคส; replay เคสนั้นผ่าน; C=1953/2000; D รุ่นพร้อมใช้=1953/2000 ไม่มี timeout; ทุกผลดิบยังอยู่
10. ตรวจ package + เว็บ 8090 + DOM ของคำตอบอังกฤษ 1v1/FT2 + hash + ผลแยก source review ก่อนสรุป

### การปรับ flow หลังอ่านคำตอบเต็ม
- เพิ่ม gate ว่า first line ต้องเป็น clause ที่ตอบหัวข้อ ไม่ใช่แค่มีคำตอบจริงที่ส่วนรายละเอียด
- gate “หัวข้อเดียวกัน” ยังไม่พอ: age ต้องมีค่า/หน่วย และ pause ต้องมี proposition ที่ถามใน subtype นั้น
- completeness ของรายการต้องมี source ทุกข้อ; negative control ที่เอกสารขาดท้ายรายการต้องไม่เติมเอง
- source presence / bounded content acceptance / organizer policy confirmation เป็นหลักฐานคนละระดับ
- ไม่อ้างทุกคำถามเร็วจาก median: r25 มี cache hit; เก็บ cold/preface/repeated requests และ trace LLM attempts แยกกัน
- ไม่อ้าง source review แก้ timeout: รอบ B เหตุการณ์ 719.2584s ยังบันทึกเป็น timeout จริง ต้นเหตุยังยืนยันไม่ได้ รีเทสผ่าน 1.5759s และรอบสุดท้ายไม่พบซ้ำ

### ข้อจำกัดที่ยังเหลือ
- ตัวให้คะแนน GT ใหญ่ยังมีข้อจำกัดกับ clause อังกฤษสั้น/penalty; ใช้ review แยกและไม่แก้ Gold
- fixture ใหม่ตรวจ 16 ประเด็น ต้องขยายรายละเอียด/ข้อยกเว้นจากคำถามจริงเมื่อเก็บได้
- คำถามไม่ระบุเกมยังใช้การถามกลับ; เวลาอาจนานกว่าคำถาม game+facet ชัด
- กติกา Tekken pause ที่ขัดกันและ V2 104 รายการยังรอผู้จัด ไม่แก้นโยบายโดยเดา
- รอบ B มี timeout ที่รีเทสไม่เกิดซ้ำ ยังระบุต้นเหตุเครื่องหรือ preflight ไม่ได้ หากเกิดอีกต้องเก็บ timing ช่วงที่ยังไม่ถูกวัด

## เอกสารและหลักฐาน
- รายงานสรุป: `{report / 'FINAL_RESULTS_TH.md'}`
- วิเคราะห์เหตุและสิ่งที่ควรตอบ: `{report / 'CAUSE_ANALYSIS_TH.md'}`
- ผลดิบ GT: `full_r26_A/B/C/D_ready_*`; ผลรอบ D ใช้ชื่อ `full_r26_D_ready_*`
- คำตอบเว็บเต็มพร้อม trace: `http_final_ready.json`, `final_ready_live_8090_content.json`
- fixture v1/v2/v3 และผล baseline เก็บแยก ไม่เขียนทับ
- ผลยืนยัน snapshot / source review / owner pending: `FINAL_VERIFICATION.json`
'''
text=flow.read_text(encoding='utf-8')
text=text.replace('## ผลการดำเนินงาน\nจะเติมผลที่วัดจริงหลังทดสอบ โดยเก็บความแตกต่างระหว่างผลอัตโนมัติ, การตรวจโดยผู้ช่วย และการยืนยันจากเจ้าของให้ชัด\n',results)
flow.write_text(text,encoding='utf-8')
final=f'''# สรุปผล r26 — 2026-10-01

เปิดใช้รุ่นใหม่ที่ http://127.0.0.1:8090/ โดยใช้แพ็กเกจ `{pkg.name}` ใน `{pkg.parent.name}`

## สิ่งที่แก้
- VALORANT ประเภทบทลงโทษไทยครบ 5 ประเภท พร้อมเงื่อนไขและ source s11–s15
- typo อังกฤษ tournament แบบเบิ้ล/ขาด/สลับ อาศัย edit distance ที่มีเกมใน registry เป็นบริบท
- รูปแบบแข่งขันเริ่มด้วย 1v1/FT2 ทั้งไทย/อังกฤษ รักษารอบ/เวลาไทยที่มีในส่วนเดียวกัน
- age/pause รายละเอียดที่ไม่มี source ต้อง no_answer; ไม่หยิบข้อใกล้เคียงมาตอบ
- game+facet กติกาชัดข้าม semantic route / LLM intent ซ้ำ แต่ยังตรวจแหล่งข้อมูล
- notice ไทย/อังกฤษสำหรับตัวอักษรซ้ำบอกว่าประมวลผลต่อแล้ว

## ทดสอบและข้อจำกัด
Unit 113/113; เนื้อหา HTTP ไทย/อังกฤษ 80/80; HTTP regression 36/36 เวลา {summary['http_regression_range_sec'][0]}–{summary['http_regression_range_sec'][1]}s

GT รุ่นสุดท้าย ไทย 1000 อังกฤษ 1000 คะแนนดิบ 1953/2000; อีก 47 เป็นข้อจำกัด source-overlap grader (Tekken 30, VALORANT 17) พบ clause เต็มตรง source ใน review แยกครบ 47 จึงยืนยัน source presence 2000/2000 หลัง review แต่ไม่ใช่ semantic correctness ของทุกคำตอบหรือเจ้าของรับรอง

รอบ B เกิด timeout เคสหนึ่ง 719.2584s; replay ผ่าน 1.5759s และรอบสุดท้ายไม่พบ timeout นี้ ต้นเหตุยังยืนยันไม่ได้ เก็บผลเดิมและ trace ไว้ครบ

เวลาเทียบคำเกริ่นใหม่: RoV 7.2289 → 0.3664s, Tekken ประมาณ 2.8 → 0.3s ในชุด benchmark; cache/การเริ่มต้น/ประเภทคำถามมีผลต่อเวลา

## งานที่รอเจ้าของ
Tekken: s07 เป็นข้อยกเว้น s03 เรื่อง pause หรือไม่ ต้องอนุญาตกรรมการหรือไม่? แต่ละกรณีเสีย Round, Game หรือ FT2 Match? V2 104 รายการและคำแปลอังกฤษยังไม่ได้รับรองจากผู้จัด

## ไฟล์
Flow: `{flow}`
วิเคราะห์ละเอียด: `CAUSE_ANALYSIS_TH.md`
ผลครบพร้อม hash: `FINAL_VERIFICATION.json`

รักษาโค้ดที่ยังไม่บันทึก Git, logs, Gold, policy sources, review queue, ตารางเจ้าของ และแพ็กเกจเก่าทั้งหมด มีสำเนาก่อนแก้/หลังแก้ ไม่มี reset/clean/commit
'''
with (report/'FINAL_RESULTS_TH.md').open('x',encoding='utf-8') as f:f.write(final)
print(json.dumps({key:value for key,value in summary.items() if key!='protected_files'},ensure_ascii=False,indent=2))
