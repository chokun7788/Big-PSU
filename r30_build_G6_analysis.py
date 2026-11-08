"""Generate a reviewable failure inventory, retaining all original grades."""
import json,collections,statistics,sys,hashlib
from pathlib import Path
r=Path(Path('r30_report_path.txt').read_text().strip());run=sys.argv[1] if len(sys.argv)>1 else 'final_F';prefix='FINAL_G6_'
assert (r/(run+'_all_summary.json')).exists(),'Full sweep has not completed; do not claim it has.'
coverage=json.loads((r/'final_G6_verified_coverage.json').read_text(encoding='utf-8'));assert coverage['all_requests_reexecuted_in_G6']
inventory=json.loads((r/'final_G6_inventory.json').read_text(encoding='utf-8'));summary=json.loads((r/(run+'_all_summary.json')).read_text(encoding='utf-8'))
by_domain=collections.defaultdict(collections.Counter);by_locale=collections.defaultdict(collections.Counter);levels=collections.Counter();modes=collections.Counter();latencies=[];failed_unique=0;count=0;examples={};pairs={};reference_rows=[];triage=collections.Counter()
def hint(g,result):
    failures=' '.join(g['failures']);mode=result.get('mode','');answer=result.get('answer','')
    if 'grader_exception' in failures:return 'grader_implementation_review'
    if 'legacy_mode_prefix' in failures or failures.startswith('intent:'):return 'metadata_or_mode_assertion_review'
    if 'Verified game catalog' in failures:return 'legacy_heading_assertion'
    if 'retrieval evidence did not match' in failures:return 'allowed_evidence_ids_need_source_review'
    if 'live_booking_status_unavailable' in mode:return 'controlled_live_dependency_unavailable'
    if 'input_guard_layout_retype' in mode or 'keyboard_layout' in mode:return 'input_guard_decision_review'
    if 'missing_english_localization' in mode:return 'localization_or_missing_source_review'
    if 'legacy_english_thai_prose_flag' in failures:return 'proper_names_or_language_leak_review'
    if 'latency' in failures:return 'deadline_or_loaded_machine_latency'
    if any(v in mode for v in ('clarification','no_current_game','no_data','unsupported','no_source')):return 'safe_abstention_vs_gold_or_missing_data_review'
    return 'route_content_or_source_selection_review'
with (r/(prefix+'FAILURE_INVENTORY.jsonl')).open('x',encoding='utf-8') as failures_out,(r/(run+'_all_results.jsonl')).open(encoding='utf-8') as source:
    for lineno,line in enumerate(source,1):
        row=json.loads(line);count+=1;result=row.get('result',{});latencies.append(float(result.get('elapsed',0)));modes[result.get('mode','exception')]+=1
        failed=[g for g in row['grades'] if not g['passed']]
        for g in row['grades']:
            domain=g['expected'].get('domain') or g['expected'].get('group') or g['expected'].get('category') or g['corpus']
            by_domain[domain]['total']+=1;by_domain[domain]['passed']+=g['passed'];by_locale[g['expected'].get('locale','auto')]['total']+=1;by_locale[g['expected'].get('locale','auto')]['passed']+=g['passed']
            level=g.get('evidence_level','unknown')
            if not any(g['expected'].get(k) for k in ['expected_route_categories','expected_category','expected_categories','expected_answer_status','expected_intent','answer_contract','must_contain','must_contain_any','required_clauses','clauses']):level='observation_only_no_answer_oracle'
            levels[level]+=1
            if g['corpus']=='master_gt_bilingual_multi_error_2000_20260929_r15.jsonl':
                pair=pairs.setdefault(g['id'],{'expected':g['expected']});pair[g['variant']]={'actual_route':result.get('route',{}).get('category',''),'mode':result.get('mode',''),'answer':result.get('answer',''),'latency_ok':result.get('elapsed',0)<=g['expected'].get('latency_ceiling_sec',20),'passed':g['passed']}
            if 'english_reference_200' in g['corpus']:reference_rows.append({'question':row['question'],'expected_reference_record':g['expected'],'actual_answer':result.get('answer'),'mode':result.get('mode'),'scope':'reference comparison saved; semantic equivalence not automatically established'})
        if failed:
            failed_unique+=1
            grouped=[]
            for g in failed:
                bucket=hint(g,result);triage[bucket]+=1;grouped.append({'corpus':g['corpus'],'id':g['id'],'variant':g['variant'],'failures':g['failures'],'expected':g['expected'],'triage_hint':bucket,'cause_confirmation':'candidate, not a confirmed root cause for every row'})
                if bucket not in examples:examples[bucket]={'question':row['question'],'locale':row['locale'],'answer':result.get('answer',''),'mode':result.get('mode'),'route':result.get('route'),'confidence':result.get('confidence'),'hits':result.get('hits'),'expected':g['expected'],'failures':g['failures'],'trace':result.get('trace'),'raw_line':lineno}
            failures_out.write(json.dumps({'key':row['key'],'question':row['question'],'locale':row['locale'],'result':result,'grade_failures':grouped,'original_results_line':lineno},ensure_ascii=False)+'\n')
assert count==summary['unique_requests']==20327
for filename,content in [('ENGLISH_REFERENCE_COMPARISONS.json',reference_rows),('FAILURE_EXAMPLES.json',examples)]:
    with (r/(prefix+filename)).open('x',encoding='utf-8') as f:json.dump(content,f,ensure_ascii=False,indent=2)
sys.path.insert(0,r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
from tools.eval_contract_v2 import rescore_pair
overlay={x['id']:x for x in map(json.loads,Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\typo_r16_contract_overlay_20260930.jsonl').read_text(encoding='utf-8').splitlines())}
paired=[]
with (r/(prefix+'PAIRED_TYPO_V2.jsonl')).open('x',encoding='utf-8') as f:
    for id,pair in pairs.items():
        case=pair['expected'];row={**case,'clean':pair['clean'],'noisy':pair['noisy'],'regression':pair['clean']['passed'] and not pair['noisy']['passed']}
        record=rescore_pair(row,overlay.get(id));paired.append(record);f.write(json.dumps(record,ensure_ascii=False)+'\n')
paired_summary={'pairs':len(paired),'legacy_clean_passed':sum(x['legacy']['clean_passed'] for x in paired),'legacy_noisy_passed':sum(x['legacy']['noisy_passed'] for x in paired),'v2_clean_passed':sum(x['v2']['clean']['passed'] for x in paired),'v2_noisy_passed':sum(x['v2']['noisy']['passed'] for x in paired),'v2_regressions':sum(x['v2']['regression'] for x in paired),'scope':'strict outcome and content overlay, not owner approved and not a booking oracle'}
audit={'unique_requests':count,'failed_unique_requests':failed_unique,'by_domain':by_domain,'by_locale':by_locale,'grade_evidence_levels':levels,'triage_hints_case_grades':triage,'triage_hints_are_not_confirmed_cause_counts':True,'mode_counts':modes,'paired_typo':paired_summary,'latency_loaded_direct_sec':{'median':statistics.median(latencies),'p95':sorted(latencies)[int(.95*(len(latencies)-1))],'max':max(latencies)},'english_reference_observations':len(reference_rows),'scope':'All 20327 requests actually reexecuted in G6; verified key/grade/provenance audit saved separately. LLM/semantic disabled; server locale binding, direct pipeline, runtime guard short-circuit tested separately; controlled unavailable booking. No combined answer accuracy across duplicated/historical/weak corpora'}
with (r/(prefix+'FULL_ANALYSIS_SUMMARY.json')).open('x',encoding='utf-8') as f:json.dump(audit,f,ensure_ascii=False,indent=2)
headers=['# วิเคราะห์ผลชุดใหญ่ r30','', '## สิ่งที่แก้แล้วและสาเหตุที่พิสูจน์ได้','',
'1. ราคาแบบหลายระยะเวลา: parser เดิมเลือกตัวเลขชุดเดียว; เพิ่มรายการ duration พร้อมหน่วยและคำนวณแต่ละตัวเลือกตามตารางเดิม จำนวนรอบเดิมยังใช้เดิม',
'2. ปุ่มเฉพาะ: ชื่อปุ่มถูกชนกับคำในชื่อเกม/คำอธิบาย จึงได้รายการอื่น; เลือกชื่อปุ่มก่อนและรักษารหัสเลข ไม่เปลี่ยน R9 ให้เป็น R1',
'3. จองเพื่อเล่นเกม: booking steps ผ่านกฎทั่วไปก่อน game-to-service จึงขาดบริการที่ถาม; อ่าน catalog บริการตรงเกมแล้วแยกข้อความว่าไม่ได้ยืนยัน slot ว่าง',
'4. ไม่มีต้นฉบับนโยบาย: generic English fallback เหมารวมเป็น missing translation; ตรวจ source gap แยกและไม่แนบ homepage เป็นหลักฐานของกฎที่ไม่มี',
'5. การตรวจคำตอบปฏิเสธคำตอบที่ถูก: ชนิดงานคาด equipment/list หรือ generic fact แม้คำนวณราคาแล้ว และบังคับแหล่งราคา PC ในคำถามยืนยันกลุ่ม; เชื่อม operation ให้ถูก เพิ่มคำว่า ค่าเล่น และยกเว้น source-price gate เฉพาะ clarification ที่ไม่กล่าวราคา',
'6. ขอบที่พบเพิ่ม: สามตัวเลือกถูกตกหล่นตัวแรก กลุ่มที่ถูกปฏิเสธกลับถูกนับเป็น PSU นักศึกษา และรหัสปุ่ม Q9/Z9 หลุดไปแสดงทั้งหมด แก้และเพิ่ม negative controls แล้ว',
'7. กฎ implicit: ผู้เล่นหลัก/เปลี่ยนตัว/ปิดเลือดและศพหลุดไปเกมหรือหัวข้อหน้างาน; ผูก target และ proposition กับข้อ source เดียว พร้อม negative controls ไม่เปลี่ยนตัวละครเป็น roster', '8. Web ingress: layout_direction เป็น candidate ทุกข้อความ แม้ score ต่ำและไม่มี mismatch flag; ให้เฉพาะ decision ที่จำแนกแล้วมีผลต่อภาษา หยุดภาษาไทยถูกโยนไป EN โดย candidate ที่ไม่ผ่าน', '', '## หลักฐานก่อน/หลัง','', 'ชุด 69 ข้อเดิม: baseline 15 → A 40 → B/C/F 69 ข้อผ่าน; ชุดเพิ่มขอบเป็น 79 ข้อ: D 75 → E 78 → F 79 ทั้ง guard profile แบบเว็บ และ API จริง 79/79 การเพิ่มขอบทำให้พบข้อผิดพลาดที่ชุดเดิมไม่ตรวจ ไม่ใช่หลักฐานว่าทุกประโยคใหม่จะถูก',
'', '## ผลแต่ละชุด — ไม่รวมเป็นความแม่นยำเดียว','', '| ชุด | ผ่านเกณฑ์ที่ระบุ / ตรวจ | ข้อจำกัด |','|---|---:|---|']
for name,c in summary['by_corpus'].items():
    scope='เกณฑ์เดิม/route หรือข้อความ; ดู evidence level' if 'competition_content' not in name and 'competition_composition' not in name and 'competition_new_questions' not in name else 'complete clause และ first line; ไม่ใช่ผู้จัดรับรอง'
    if 'english_reference' in name or 'user_question_bank' in name:scope='observation/เกณฑ์สนับสนุนไม่พอพิสูจน์คำตอบถูก'
    headers.append(f"| {name} | {c['passed']}/{c['total']} | {scope} |")
headers+=['','## ข้อผิดเพิ่มเติมที่แก้ G4/G5/G6','', 'G4: CS2 platform/client clause, after-closed registration action, RoV Default skin, Tekken rounds และ bare franchise edition qualifier; G5: restored enumerated roster topic, generic booking-period available, CS2 event version ก่อน catalog target lock และ protest-language ลำดับคำสองทิศ ตรวจ source literals ไม่สร้างนโยบายใหม่ หลักฐานก่อน/หลังใน source fixtures และ Flow final; G6 เพิ่ม CS2 duration/venue จาก s08_c01', '', '## เปรียบเทียบคำตอบ clean/noisy 2,000 คู่','',json.dumps(paired_summary,ensure_ascii=False),'', '## ประเภทของข้อที่เหลือและแนวทาง','',
'### P1: งาน/ภาษา/เป้าหมายยังเสียความหมายในบางข้อความ','',
'Ingress/locale: F direct กับ API ใช้ surface binding ต่างกัน จากนั้น G2 แก้ candidate layout direction ที่ยังไม่จำแนก และ G3 แยก source game titles จากหลักฐานภาษา Full sweep G2/G3/G4/G6 ใช้ binding แบบ server แล้ว Mixed-title fixture ตรวจ 8 ข้อแยกภาษา การเทียบ G2→G3 พบ 45 grades ดีขึ้นและ 4 grades แย่ลงทั้งหมดเป็น latency ของ Minecraft ประโยคเดียวที่คำตอบไม่เปลี่ยน จึงไม่เหมารวมเป็น content regression',
'', 'คำถามราคาที่มีเกมอยู่หลายบริการ เช่น TEKKEN 8 สามารถถามเลือก PC/PS5 ได้อย่างปลอดภัย แต่ Gold บางรุ่นคาด answer_available จึงไม่ควรตีความทุก clarification ว่าตอบผิด ส่วนเกมที่มีบริการเดียวแต่ยังถามเลือกบริการโดยไม่เสนอข้อมูลที่รู้ เป็นจุดที่พัฒนาได้ ใช้ game→services แล้วให้ตัวเลือกเฉพาะและราคาแต่ละกลุ่ม',
'', '### P1: ข้อมูลเก่าและข้อกำหนดของเกณฑ์ตรวจ','',
'`What games are available?` ได้รายชื่อ 42 เกม แต่เกณฑ์ต้องมีหัวข้อ `Verified game catalog` จึง fail: เป็น assertion รูปแบบเก่าที่ไม่พิสูจน์ว่ารายชื่อผิด ต้องตรวจชื่อเกม/จำนวน/โซนจาก catalog แทน และเก็บคะแนนเดิมไว้',
'', 'กฎแข่งขัน expanded v2 มีข้อ allowed evidence IDs ไม่ตรงกับข้อย่อยที่ตอบ ตัวอย่างการใช้อุปกรณ์ส่วนตัว CS2 ตอบรายการอุปกรณ์จาก rulebook เดียวกัน ต้องเทียบเนื้อหาข้อจริงก่อนเปลี่ยน Gold หรือสรุปว่า retrieval ผิด การมี source ID อย่างเดียวก็ยังไม่พิสูจน์ว่าตอบเงื่อนไขครบ',
'', 'Gold builder ไม่ตรงไฟล์ frozen 6 แถวอังกฤษ เพราะ metadata reference_answer เรื่องค่าเสียหายฉบับใหม่เพิ่มเงื่อนไข/จำนวนเงิน ไม่ได้เกิดจากแก้ Gold ในรอบนี้ เก็บ drift แยก ไม่เขียนทับไฟล์เพื่อให้ test ผ่าน',
'', '### P1: แยก schedule policy ออกจาก live booking','',
'คำถาม Maintenance ทั่วไปแก้ G4 ให้ตอบ weekly policy จากตารางเดิม และแยก PC1/status เป็น live path G4 unit พบ available for generic days/time periods ถูกกันผิด จึงแก้ G5 พร้อม regression tests คำถามวัน/เวลา/เครื่องจริงตรวจ path แยกจาก occupancy oracle ห้ามแปลง controlled unavailable fixture เป็นหลักฐานว่าข้อมูลจองจริงผิด',
'', '### P2: คำถามที่กำกวมและประสบการณ์ใช้งาน','',
'Call of Duty ไม่ระบุภาค: ระบบใหม่ถามชื่อ/ภาคเพื่อไม่เลือกบริการผิด เกณฑ์เก่าที่บังคับ reservation ไม่ผ่าน เป็นการเปลี่ยนผลตอบแบบปลอดภัยตาม Flow ปัจจุบัน พัฒนาเพิ่มได้ด้วยรายการภาคที่มีและบริการแต่ละภาค แทนการถามแบบไม่มีตัวเลือก',
'', 'สิบคำถามพร้อมกันมี HTTP 503 ทั้งกรณีทดสอบร่วมกับการดึง WordPress และรอบ G2 smoke ขณะ full sweep ใช้เครื่องหนัก worker เดียวมี queue wait 3 วินาที จึงต้องแยกผล under-load จาก idle เมื่อรันแยกโดยไม่มีงาน API อื่น รุ่น r29 และ r30-F ผ่าน 10/10 ทั้งคู่ ไม่มีภาษาข้ามกัน ไม่สรุปว่า r30 ทำให้ concurrency เสีย การรองรับคิวช่วงที่มีคำถามช้าหลายคนยังเป็นงานเสริม: แสดงสถานะรอ/ลองใหม่และวัด SLA แยกจาก correctness ก่อนปรับ worker/RAM',
'', '### P2: ภาษาอังกฤษและแหล่งข้อมูลที่ยังขาด','',
'ต้นฉบับ shadow 1,600 แถวไม่มี question_en; ใช้ชุดแปลเครื่อง 1,600 แถวที่มีอยู่ตรวจแยก ไม่เรียกว่าคนตรวจแล้ว ชื่อบุคลากรภาษาไทยจาก source อาจเป็นการรักษาชื่อจริง ไม่ใช่ภาษาอังกฤษรั่วทุกกรณี แยก proper name จาก Thai prose และขอชื่ออังกฤษทางการตามแบบฟอร์มเดิม',
'', 'นโยบายวิดีโอ/ภาพ อายุ ค่าสมัคร controller รายละเอียดที่ไม่มี และ Tekken/RoV ที่ขัดแย้ง/ถูกตัด ต้องได้เอกสารเจ้าของ ไม่ใช้โมเดลแต่งเติม; real booking oracle ยังพักตามคำขอ',
'', '### P2: ตัวตรวจการพิมพ์และความครอบคลุมของการทดสอบ','',
'Native detector benchmark ตรวจ calibration 100/test 400 พร้อม disclosure ว่าไม่ใช่ untouched holdout; runtime profile ตรวจ 500 เคสด้วย published corpus/fixed thresholds G2/G3 บล็อกตาม policy ถูก 498/500; G5 ตรวจ accidental repeat ที่มีหลักฐานจาก corpus ก่อนประเมิน wrong layout ใน residual รอบชื่อเกม exact โดยไม่เปลี่ยนข้อความ และตรวจ corpus 500 อีกครั้ง ผลล่าสุดดู final_G5_runtime_guard500_summary.json; corpus นี้ยังไม่มี content oracle ครบ ตัวเลขนี้ไม่ใช่ answer accuracy; continued inputs 260 เคสตรวจ validation แต่ยังไม่มี content oracle ครบ',
'', 'ชุดที่ตรวจแค่ route/outcome/validation ยังมีช่องว่างเรื่องเนื้อหา ต้องเติม oracle เนื้อหาจาก source เป็นรายกลุ่ม มีเลข/เงื่อนไข/ข้อห้าม/source scope และตรวจ clean/noisy ด้วย oracle เดียวกัน คู่ 2,000 มีการ rescore V2/overlay โดยไม่แก้ชุด frozen; native detector 500 เคสใช้ training corpus/threshold ต่างจาก runtime ให้ดู final_G_guard500/summary.json แยกจาก final_G_runtime_guard500_summary.json',
'', '## ตัวอย่าง trace ที่ไม่ผ่าน — หมวดเหล่านี้เป็นการคัดแยกเพื่อทบทวน','']
for bucket,e in examples.items():
    headers += [f'### {bucket}','',f"คำถาม: {e['question']}",'',f"คำตอบจริง: {e['answer']}",'',f"Mode: `{e['mode']}`; route: `{json.dumps(e['route'],ensure_ascii=False)}`; confidence: {e['confidence']}",'',f"ไม่ผ่าน: {json.dumps(e['failures'],ensure_ascii=False)}",'',f"Trace เต็มและ expected contract: FINAL_G6_FAILURE_EXAMPLES.json; ข้อมูล raw แถว {e['raw_line']} ใน final_G6_all_results.jsonl",'']
headers+=['## วิธีอ่านคะแนนและเหตุผลเลือก','',
'Trace แสดง input recovery, route candidates, top score/margin, target lock, hits, validation errors และ fallback ตามที่แต่ละเส้นทางบันทึก การผ่าน confidence threshold แปลว่าเลือก candidate ตามกติกาคะแนนได้ ไม่ใช่พิสูจน์ว่าคำตอบครบหรือ source ยังใช้งานจริง ทุกข้อไม่ผ่านเก็บ result เต็มใน FINAL_G6_FAILURE_INVENTORY.jsonl แล้วเชื่อมกลับ raw line ได้ หมวด triage อัตโนมัติเป็นเพียงคำใบ้ในการทบทวน ไม่ใช่ยืนยันสาเหตุเดียวให้ทุกข้อ',
'', '## สิ่งที่ยังไม่สรุป','',
'ไม่มีการยืนยัน booked/free ของข้อมูลจริง ไม่มีการรับรองนโยบายจากเจ้าของใหม่ ไม่รวม historical versions/splits/aliases เป็นเปอร์เซ็นต์เดียว และไม่เรียก reference ที่ไม่มี content oracle ว่าคำตอบถูกแล้วทั้งหมด']
with (r/(prefix+'DETAILED_CAUSE_ANALYSIS_TH.md')).open('x',encoding='utf-8') as f:f.write('\n'.join(headers)+'\n')
print(json.dumps({'unique':count,'failed_unique':failed_unique,'paired':paired_summary,'evidence_levels':levels},ensure_ascii=False),flush=True)
