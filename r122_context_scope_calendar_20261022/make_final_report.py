"""Build Thai report from completed, immutable measurements only."""
import hashlib,json,statistics
from pathlib import Path
R=Path(__file__).resolve().parent;OLD=R.parent/'r121_context_planner_training_20261022'
def read(p):return json.loads(p.read_text('utf8'))
def rows(p):return [json.loads(s) for s in p.read_text('utf8').splitlines()]
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
assert read(R/'api02/TEST_COMPLETE.json')['complete']
assert read(R/'ellipsis01/TEST_COMPLETE.json')['complete']
assert read(R/'comparison01/TEST_COMPLETE.json')['complete']
summary=read(R/'API_COMPARISON.json');verification=read(R/'FINAL_VERIFICATION.json')
base=rows(R/'api02/base/RESULTS.jsonl');trained=rows(R/'api02/trained/RESULTS.jsonl');probes=rows(R/'ellipsis01/trained/RESULTS.jsonl');fixed_probe=rows(R/'comparison01/trained/RESULTS.jsonl')
assert len(base)==len(trained)==8 and len(probes)==2
freeze=read(R/'comparison01/RUN_FREEZE.json');assert all(sha(Path(p))==h for p,h in freeze.items())
prior=read(R/'ellipsis01/RUN_FREEZE.json');assert all(sha(Path(p))==h for p,h in prior.items())
for name in ['OFFLINE_CONTEXT_VERIFICATION04.json','CONTEXT_REGRESSION_VERIFICATION04.json','ELLIPSIS_VERIFICATION.json','COMPARISON_VERIFICATION.json']:assert read(R/name)['all_passed']
assert len(fixed_probe)==1 and all(x['http_status']==200 and x['capture_body_matches_api'] for x in base+trained+probes+fixed_probe)
calls=rows(R/'inference03/REQUESTS.jsonl');backend=summary['model_transport']
latest_calls=rows(R/'inference04/REQUESTS.jsonl')
assert all(x['transport_ok'] for x in calls+latest_calls)
assert all(x['provenance']['adapter_active']==(x['stage']=='context') for x in latest_calls)
evidence=[{'question':x['question'],'key':x['key'],'answer':x['response']['answer'],'sources':x['result'].get('hits',[]),'decision_artifact':x['response'].get('decision_artifact',{})} for x in trained+probes+fixed_probe]
(R/'ANSWER_SOURCE_EVIDENCE.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2),'utf8')
verification.update(latest_candidate='R122 revision04',latest_candidate_frozen_files_unchanged=len(freeze),latest_database_sha256=sha(R/'revision04_system/data/knowledge/common.sqlite'),probe_adapter_identity_verified=read(R/'comparison01/MODEL_IDENTITY.json')['digests']==read(R/'api02/MODEL_IDENTITY.json')['digests'])
(R/'FINAL_VERIFICATION.json').write_text(json.dumps(verification,ensure_ascii=False,indent=2),'utf8')
b=summary['scores']['base'];t=summary['scores']['trained']
body=['# R122 — ผลพัฒนาการเข้าใจบริบทและตัวอ่านข้อมูล','',
'## สรุปสถานะ','',
'ทำ candidate ล่าสุด `revision04_system` แล้ว ใช้ LoRA ที่ฝึกจริงใน R121 จำนวน 93 optimizer steps ไม่มีการฝึกน้ำหนักรอบใหม่ใน R122 และยังไม่ได้ติดตั้งทับ R78/production','',
'แก้การปนเงื่อนไขระหว่างคำถามย่อย การผูกคำอ้างอิง การถามกลับเมื่อยังตีความไม่ได้ ตารางให้บริการทั้งสัปดาห์ และชื่อโปรไฟล์โมเดลของ fallback พร้อมเสริม service→game ellipsis จากความสัมพันธ์ต้นทาง','',
'ทดสอบ API ครบ 16 คำตอบสำหรับคู่ base/trained บน revision02 เพิ่ม 2 คำตอบบน revision03 และตรวจแก้ VR อีก 1 คำตอบบน revision04 รวม 19 คำตอบที่วัดจบ คำถามทั้งหมดมาจากชุดเดิม ไม่มี Full Test ไม่มีการรัน Flow เดิมใหม่ และไม่มีเปอร์เซ็นต์ semantic accuracy รวมที่ยืนยันได้จากงานนี้','',
'## 1. ผลการเทียบแบบตั้งค่าเดียวกัน','',
'| ตัววัด | Base | Trained context adapter |','|---|---:|---:|',
f"| HTTP 200 / คำถาม | {b['http_200']}/8 | {t['http_200']}/8 |",
f"| Strict benchmark เดิม | {b['strict_pass']}/{b['grades']} | {t['strict_pass']}/{t['grades']} |",
f"| Positive literal checks | {b['positive_literal_pass']}/{b['positive_literal_checks']} | {t['positive_literal_pass']}/{t['positive_literal_checks']} |",
f"| Median API latency | {b['median_elapsed_sec']:.3f} วินาที | {t['median_elapsed_sec']:.3f} วินาที |",'',
'Positive literal checks มีอยู่เพียง 2 จาก 8 คำถาม: Nintendo 4 checks และ CS2 1 check ดังนั้น 4/5 ไม่ใช่ 80% ของคำถามทั้งหมด และไม่ใช่คะแนนความถูกต้องรวม','',
'### แยก locale','',
'| Locale | คำถามต่อแขน | Strict base → trained | Positive literal base → trained |','|---|---:|---:|---:|']
for loc in ['th','en','auto']:
 lb=summary['by_locale']['base'].get(loc);lt=summary['by_locale']['trained'].get(loc)
 if lb:body.append(f"| {loc} | {lb['requests']} | {lb['strict_pass']}/{lb['grades']} → {lt['strict_pass']}/{lt['grades']} | {lb['positive_literal_pass']}/{lb['positive_literal_checks']} → {lt['positive_literal_pass']}/{lt['positive_literal_checks']} |")
 else:body.append(f'| {loc} | 0 | ไม่มีในชุด API นี้ | ไม่มี |')
body+=['','8 ข้อนี้เคยใช้วิเคราะห์และพัฒนาแล้ว จึงเป็น development comparison ไม่ใช่ fresh holdout ผลจาก R121 raw model 30 ข้อเป็นการวัดอีกแบบและคนละชั้นของระบบ ต้องไม่เอามารวม denominator กัน','',
'## 2. วิเคราะห์รายกรณีจากคำตอบจริง','',
'| กรณี | Base รอบนี้ | Trained รอบนี้ | ข้อสรุปจาก source |','|---|---|---|---|',
'| CS2 ปรับ Brightness/Resolution/Crosshair | งดตอบเพราะหา clause ไม่ครบ | ดึง clause ของ CS2 2026 ได้ | แหล่งข้อมูลมีจริง ปัญหา base อยู่ที่แผน/เส้นทางอ่าน ไม่ใช่ไม่มี clause |',
'| Nintendo Zone มีอะไรให้ใช้ | ตอบรายชื่อเกม | ตอบ OLED, TV 86 นิ้ว, จอย และตัวอย่างเกม | เลือก equipment usage ตรงเจตนาขึ้น |',
'| Tekken 8 ปุ่ม + ราคา PC | ตอบเฉพาะราคา | ตอบ controls และราคา แยกสองงาน | source มี 12 control entries แต่ไม่ระบุชุด 8 ปุ่มที่ถาม จึงต้อง partial/ถามกลับ ไม่อ้างว่าตอบชุด 8 ปุ่มครบ |',
'| ไม่ใช่นักศึกษา PSU เข้าได้ไหม | ตอบ owner policy ได้ | ตอบ owner policy ได้ | ทั่วไปเข้าได้ตามข้อมูล draft; ไม่ขยายเป็นสิทธิ์ลงแข่ง |',
'| ถือขวดน้ำเข้า ไม่ได้ถามเรื่องกิน | ยังไม่ยืนยัน | ยังไม่ยืนยัน | source การบริโภคไม่ใช่หลักฐานสิทธิ์นำเข้าแยกต่างหาก |',
'| FF16 ต้องจองอะไร | PS5 #01–#02 | PS5 #01–#02 | ใช้ relation เกม→บริการที่มีอยู่ |',
'| จอง Cockpit และเปิดวันไหน | ตอบเฉพาะตาราง | ตอบขั้นตอนจองและตาราง 7 วัน | ตารางมีจริง; applicability ต่อ resource และช่วงมีผลยังไม่ยืนยัน จึงไม่ใช่คำตอบเปิดจริงแบบไร้เงื่อนไข |',
'| ผู้ใช้ภายนอกต้องแสดง ID อะไร | ดึง documents ได้ | ดึง documents ได้ | มี owner policy และ legacy document policy ซ้ำ ควรรวมให้อ่านง่ายขึ้น |','',
'คำว่า source ในตารางหมายถึงฐานข้อมูล migration/evaluation draft ที่ frozen ไว้ ไม่ใช่การยืนยันว่าเจ้าของเผยแพร่หรืออนุมัติใช้งานจริงแล้ว','',
'## 3. ทำไม strict ยังเป็นศูนย์','',
'1. Protocol: route ภายนอกของ format กลางเป็น `knowledge` แต่ evaluator เดิมคาด `equipment`, `multi_question`, `rules` ฯลฯ จึงผิด route แม้เนื้อหาบางข้อรองรับจาก source','',
'2. Complete-clause/keyword: CS2 evaluator ต้องการประโยคลงท้าย `computer monitor` ขณะที่ source ที่ดึงมี `computer screen` และข้อความไทยที่ความหมายสอดคล้อง ต้อง review ความหมายแยก ห้ามนับเป็นคำตอบผิดทั้งหมดจาก literal fail อย่างเดียว','',
'3. First-line: ประโยคแรก CS2 เป็นคำชี้แจงการแปล ก่อนเริ่มตอบ clause ทำให้ first_line_off_topic ซึ่งเป็นปัญหาการจัดคำตอบที่ยังแก้ได้','',
'4. Evidence identity: wrong_game_source ของ CS2 ต้องอ่านกับหลักฐานจริง โดย hit มี `common_game_id=game_detail_cs2`, game=Counter-Strike 2 และ rulebook=competition_rules_cs2_psu_phuket_2026 จึงยังไม่มีหลักฐานว่าไปดึงกติกาคนละเกม เพียงเพราะ checker อ้าง source ID เดิมไม่ตรง','',
'5. Performance: trained ยังมี latency_ceiling 10 occurrences ใน 15 grades; base มี 15 occurrences ตัวเลขเป็น occurrences ต่อ grade จึงซ้ำคำถามได้ และความเร็วดีขึ้นไม่ได้หมายความว่าผ่าน SLA แล้ว','',
'## 4. Model transport แยกจากคุณภาพคำตอบ','',
f"รอบเทียบ revision02 เรียก backend จริง {backend['actual_backend_requests']} ครั้ง สำเร็จ {backend['success']} ครั้ง: context 16, evidence selection 4 และ generic base inference 1 ไม่มี transport error ในรอบนี้ โปรไฟล์ที่ caller ขอและ adapter_active ถูกตรวจจาก log จริง",'',
f"รอบ probe revision03 เรียก backend {len(calls)} ครั้ง สำเร็จ {sum(x['transport_ok'] for x in calls)} ครั้ง รายละเอียด stage และ raw output เก็บใน inference03/REQUESTS.jsonl",'',
f"รอบแก้ revision04 เรียก backend {len(latest_calls)} ครั้ง สำเร็จทั้งหมด รวมรอบที่วัดครบทั้งสามชุด {backend['actual_backend_requests']+len(calls)+len(latest_calls)} backend calls ไม่มี transport failure",'',
'ก่อนหน้านี้ R121 API มี base fallback 3 ครั้งเรียกชื่อ default ที่ backend ทดลองไม่รองรับ รอบนี้กำหนด model environment ทั้งห้าตัวแล้ว จึงแก้สาเหตุด้านการตั้งค่าได้ อย่างไรก็ตาม HTTP 200 และ schema ผ่านไม่ใช่หลักฐานว่าคำตอบถูก semantic','',
'Context adapter ใช้เฉพาะ context stage ของ trained arm; selector และ generic inference ใช้ base weights ทั้งสองแขน รุ่น base HF NF4 นี้ไม่ใช่ไฟล์น้ำหนักแบบเดียวกับ Ollama GGUF ของ Flow เดิม จึงไม่อ้างผลนี้ว่าเทียบกับ Flow เดิมโดยตรง','',
'## 5. การเสริม revision03 หลังการเทียบ','',
'จับ implicit ellipsis แบบจำกัด: task แรกมีชื่อบริการเดียว task ถัดมาถาม game catalog โดยไม่มีชื่อใหม่ และมี source relation บริการ→เกม จึงสืบทอดเฉพาะชื่อบริการเป็น target พร้อม audit โดยไม่สืบทอด duration/audience/price ของอีก task','',
'ตรวจ 11 จุดจาก saved plans, 6 regression questions และ 5 เงื่อนไขจาก 2 compound questions กับ revision03 แล้ว ทั้งหมดผ่าน แต่ตัวเลขเหล่านี้เป็น gates เฉพาะจุด ไม่ใช่จำนวนคำตอบที่ถูกทั่วไป','',
'### คำตอบ probe ผ่าน API จริง','']
for x in probes:
 body+=['#### '+x['question'],'',x['response']['answer'],'',f"HTTP {x['http_status']}; {x['elapsed_sec']:.3f} วินาที; key `{x['key']}`",'']
body+=['### แก้ต่อเป็น revision04 จากผล VR ที่ยังผิด','',
'VR_SOURCE_REVIEW.json ยืนยันว่ามีทั้ง rates 30 และ 60 นาที และมีข้อความขั้นตอนจอง 3 records ซึ่งเป็น 2 ข้อความไม่ซ้ำ จึงไม่ใช่ข้อมูลหาย ผล revision03 ส่งแผน compare มาถูกแล้ว แต่ reader/selector เลือกเพียง 30 นาที และ task จองลงท้าย reason request_model_budget_exhausted ไม่ใช่ model transport ล้ม','',
'revision04 อ่านอัตราของแต่ละระยะเวลาที่ระบุจาก source แยกกัน ไม่รวมยอดทางเลือกเข้าด้วยกัน และนำเสนอขั้นตอนจองหลายฉบับแยกกันในสถานะ partial แทนการใช้โมเดลเลือกฉบับใดฉบับหนึ่งโดยไม่มี authority rule เพิ่ม','',
'ตรวจ source-level เพิ่ม 6 จุด: พบ 30/60 ครบ, มี booking claims, ไม่ temporary failure, ไม่เรียกโมเดลเพิ่มจาก saved plan, ไม่รวมยอดทางเลือก, และเปิดเผยหลายฉบับของ procedure ผลผ่านทั้งหมด','',
'ผล API จริงหลังแก้:', '',fixed_probe[0]['response']['answer'],'',
f"HTTP {fixed_probe[0]['http_status']}; {fixed_probe[0]['elapsed_sec']:.3f} วินาที; ผลก่อนแก้เก็บใน ellipsis01 ผลหลังแก้เก็บใน comparison01",'',
'## 6. สิ่งที่แก้และสิ่งที่ยังเหลือ','',
'### แก้แล้วใน candidate','',
'- ตรวจ local constraints ต่อ task และบันทึกสิ่งที่ถูกเอาออก','- ผูกชื่อจาก it/its/เครื่องนั้น ด้วยชื่อที่อ้างจากคำถามและ source index','- รองรับ PC/VR ซึ่งเป็นชื่อย่อสองตัวอักษร','- ถามกลับเมื่อ pronoun ไม่มีสิ่งอ้างอิง หรือระยะเวลาสองค่ายังไม่แยกบทบาท','- รักษาคำถามเปรียบเทียบระยะเวลาและข้อความกำกับรูปแบบ เพื่อไม่สร้างความกำกวมเกินจำเป็น','- อ่าน recorded play-service timetable ทั้ง 7 วัน','- แยก regular timetable ออกจาก live availability','- ตั้งค่า caller/fallback ให้ใช้โปรไฟล์ถูกแขน','- เสริมบริการ→เกมในคำถามที่ละชื่อบริการตามเงื่อนไขที่รองรับ','',
'### ยังเหลือ','',
'- Shared prefix, audience, เงื่อนไขซ้อน และหลาย entity ในหลายประโยคยังไม่ใช่ semantic parser ที่ครอบคลุมทุกแบบ','- แหล่งข้อมูลที่ยืนยันสิทธิ์ถือเครื่องดื่มเข้าแยกจากสิทธิ์บริโภคยังขาด','- ชุดย่อย 8 ปุ่มและจำนวน control entries ต้องระบุความหมายให้ชัด','- ตารางยังขาด applicability ต่อ resource และ effective interval ที่ยืนยัน จึงต้องรักษาคำชี้แจง partial','- Comparison reader ใหม่จำกัดที่ duration_minutes และระยะเวลาชัดเจน ไม่ครอบคลุมจำนวนคน/รอบร่วมใน comparison; การเขียนระยะเวลาเป็นคำและคำเปรียบเทียบรูปอื่นยังต้องตรวจ normalization ต่อ','- รูปแบบ first line, คำตอบซ้ำจากหลาย source และ taxonomy ของ public API ยังควรพัฒนาต่อ','- ความเร็วบน GPU 6GB ยังไม่ผ่านเกณฑ์เดิมหลายข้อ','- Native compatibility typed parsers/fallback ยังอยู่ และยังไม่มีการวัด Full ของ candidate นี้','',
'## 7. ข้อมูลสอน','',
'annotation_draft03 เก็บคำถามเดิม 244 train / 15 validation / 30 test พบ label แตกต่าง 11 ข้อจาก 289 ข้อ เป็น draft ของ task scope ที่ต้อง review semantic เพิ่ม ไม่ได้นำไป optimize น้ำหนัก ไม่ได้แทนที่ gold เก่า และไม่ได้เปลี่ยนคะแนน R121 ย้อนหลัง','',
'## 8. การเก็บหลักฐานและข้อจำกัดการเปรียบเทียบ','',
'- คู่ API 16 คำตอบใช้ revision02 ที่ frozen; probe 2 คำตอบใช้ revision03 ที่ frozen แยกกัน ไม่เอามาปนว่า 18 คำตอบรัน source รุ่นเดียวกัน','- R121 saved API ที่แสดงใน API_PER_REQUEST_TH.md เป็น initial system รอบ api02 ก่อน guard revisions รุ่นหลัง และมี config confound ที่ระบุไว้ จึงใช้ดูกรณี ไม่ใช่ causal comparison ของ revision04→R122','- Runtime label ใน paired harness คงชื่อ R121-context-lora เดิม แต่ source path/hash ของ R122 ถูกตรวจโดย RUN_FREEZE; manual launcher ใช้ชื่อ R122 revision03 แล้ว','- รันแรกใน execution01 ถูกยกเลิกเมื่อพบ pronoun guard กว้างเกินไป เก็บ partial results, CANCEL_REASON และ logs ไว้ ไม่เอามานับเป็นรอบครบ','- รักษาฐานข้อมูลจริง approvals logs เดิม น้ำหนักและชุดฝึกเดิม รวมถึงไฟล์ source ที่ป้องกันไว้','',
'```json',json.dumps(verification,ensure_ascii=False,indent=2),'```','',
'## 9. ไฟล์สำหรับตรวจต่อ','',
'- FLOW_R122_TH.md: Flow และขอบเขตของแต่ละ guard','- API_PER_REQUEST_TH.md: คู่คำตอบ base/trained และ R121 saved รายข้อ','- ANSWER_SOURCE_EVIDENCE.json: คำตอบ, source IDs, snapshot hash และ decision artifacts','- API_COMPARISON.json: คะแนนแยก strict/literal/locale/transport','- OFFLINE_CONTEXT_VERIFICATION03.json, CONTEXT_REGRESSION_VERIFICATION03.json, ELLIPSIS_VERIFICATION.json: จุดตรวจ source/context','- api02 และ ellipsis01: actual API captures กับ RUN_FREEZE','- inference02 และ inference03: backend requests/raw outputs/provenance','- annotation_draft03/REVIEW_REQUIRED.json: diff ป้ายสอนที่ต้อง review','',
'ขั้นถัดไปควรขยาย shared context/normalization ของ comparison ตรวจ authority ของ procedure variants และทำ contract mapping ของ public API โดยคงเกณฑ์ benchmark เดิมแยกไว้ จากนั้นค่อยขยายการวัดด้วยคำถามเดิมที่มีอยู่ ยังไม่ควรอ้างว่าทุกหมวดพร้อม production หรือเริ่ม Full Test โดยไม่มีการพิจารณาผลรอบนี้','']
(R/'FINAL_REPORT_TH.md').write_text('\n'.join(body),'utf8')
final={'complete':True,'candidate':'R122 revision04','paired_api_revision':'revision02','paired_requests':16,'revision03_probe_requests':2,'latest_revision_probe_requests':1,'new_questions':0,'new_weight_training':False,'same_r121_trained_adapter':True,'full_test':False,'production_installed':False,'scores':summary,'semantic_accuracy':None,'verification':verification,'reports':['FINAL_REPORT_TH.md','FLOW_R122_TH.md','API_PER_REQUEST_TH.md','ANSWER_SOURCE_EVIDENCE.json']}
(R/'ANALYSIS_FINAL.json').write_text(json.dumps(final,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'complete':True,'candidate':final['candidate'],'api_requests':19,'new_training':False,'report':str(R/'FINAL_REPORT_TH.md')},ensure_ascii=False))
