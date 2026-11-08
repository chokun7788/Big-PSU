"""Read immutable benchmark outputs and report all domain comparisons."""
import collections,hashlib,json,statistics
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent;RUN=R/'main_natural'
def read(p):return json.loads(p.read_text('utf8'))
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8')
done=read(RUN/'TEST_COMPLETE.json');assert done['complete'] and done['completed_executions']==4200
rows=[json.loads(x) for x in (RUN/'RESULTS.jsonl').read_text('utf8').splitlines()];jobs=[json.loads(x) for x in (R/'EFFECTIVE_QUESTIONS_1400.jsonl').read_text('utf8').splitlines()]
addendum=read(R/'EXCLUSION_ADDENDUM.json')
assert hashlib.sha256((R/'EFFECTIVE_QUESTIONS_1400.jsonl').read_bytes()).hexdigest()==addendum['effective_workload_sha256']
assert not any('หน่วยโทษ' in x['question'] for x in rows)
expected_pairs={(c['id'],j['id']) for c in read(R/'SELECTED_42.json') for j in jobs if c['category']==j['category']}
assert {(x['flow_id'],x['question_id']) for x in rows}==expected_pairs
configs=read(R/'SELECTED_42.json');catdata=read(B/'r112_category_design_20261021/CATEGORY_AND_METHOD_SPEC.json')['categories'];cnames={c['id']:c['name'] for c in catdata}
assert len(rows)==4200 and len({(r['flow_id'],r['question_id']) for r in rows})==4200
events=[json.loads(x) for x in (RUN/'MODEL_EVENTS.jsonl').read_text('utf8').splitlines()] if (RUN/'MODEL_EVENTS.jsonl').exists() else []
stats=[];allfail=[]
for config in configs:
 group=[x for x in rows if x['flow_id']==config['id']];assert len(group)==100
 st={'flow_id':config['id'],'category':config['category'],'name':config['name'],'family':config['family'],'questions':100,'passed':sum(x['grade']['passed'] for x in group),'score_percent':sum(x['grade']['passed'] for x in group),'strata':{},'locales':{},'failure_patterns':{},'latency_batch_amortized_mean_sec':round(statistics.mean(x['result']['elapsed_sec'] for x in group),4),'english_source_missing_cases':sum(x['result']['english_translation_missing'] for x in group)}
 for key in ['single_need','multi_need','missing_source']:
  part=[x for x in group if x['stratum']==key];st['strata'][key]={'questions':len(part),'passed':sum(x['grade']['passed'] for x in part),'unrequested_claim_cases':sum(bool(x['grade']['unrequested_claims']) for x in part)}
 for lang in ['th','en','auto']:
  part=[x for x in group if x['locale']==lang];st['locales'][lang]={'questions':len(part),'passed':sum(x['grade']['passed'] for x in part)}
 ev=[e for e in events if e['flow_id']==config['id']];st['model']={'http_attempts':len(ev),'transport_success':sum(e['transport_ok'] for e in ev),'schema_success':sum(e['schema_ok'] for e in ev),'questions_sent':sum(e['question_count'] for e in ev),'generation_elapsed_sec':round(sum(e['elapsed_sec'] for e in ev),3)}
 patterns=collections.Counter()
 for x in group:
  g=x['grade']
  if g['missing_claims']:patterns['missing_requested_source_claims']+=1
  if g['unrequested_claims']:patterns['unrequested_or_wrong_scope_claims']+=1
  if g['wrong_values']:patterns['numeric_or_value_mismatch']+=1
  if g['evidence_mismatches']:patterns['evidence_mismatch']+=1
  if not g['status_ok']:patterns['answer_state_mismatch']+=1
  if x['model_event_id'] and x['result']['status']=='unavailable':patterns['model_protocol_or_transport_unavailable']+=1
  if not g['passed']:allfail.append(x)
 st['failure_patterns']=dict(patterns);stats.append(st)
rankings=[]
for cat in catdata:
 cid=cat['id'];group=[s for s in stats if s['category']==cid];top=max(s['passed'] for s in group);ties=[s for s in group if s['passed']==top]
 recommended=sorted(ties,key=lambda s:(s['failure_patterns'].get('unrequested_or_wrong_scope_claims',0),s['model']['questions_sent'],s['flow_id']))[0]
 q=[j for j in jobs if j['category']==cid];sigs={json.dumps({'claims':[(x['fact_id'],x['numeric']) for x in j['expected']['claims']],'status':j['expected']['status']},sort_keys=True) for j in q}
 rankings.append({'category':cid,'name':cat['name'],'best_score_percent':top,'winning_flows':[s['flow_id'] for s in ties],'recommended_flow':recommended['flow_id'],'recommendation_basis':'highest exact source-contract pass; ties prefer fewer unrequested claims then less model dependence. No forced winner on a score tie.','all_scores':{s['flow_id']:s['passed'] for s in group},'unique_oracle_claim_signatures':len(sigs),'fixture_category':cid in ['C12','C14'],'english_translation_available_not_guaranteed':cid=='C13'})
write(R/'SCORES_42.json',stats);write(R/'RANKING_BY_CATEGORY.json',rankings)
with (R/'ALL_FAILED_CASES.jsonl').open('w',encoding='utf8') as f:
 for x in allfail:f.write(json.dumps(x,ensure_ascii=False)+'\n')
write(R/'WINNER_CANDIDATE_CONFIG.json',{'status':'benchmark recommendation only; not installed into the chatbot','category_to_flow':{x['category']:x['recommended_flow'] for x in rankings},'ties':{x['category']:x['winning_flows'] for x in rankings if len(x['winning_flows'])>1},'global_domain_router_tested':False})

lines=['# R113 — ผลเปรียบเทียบ 3 Flow ต่อหมวด','',
'## 1. สิ่งที่ทำจริง','',
'- ออกแบบ 140 Flow = 14 หมวด × 10 ทางเลือก พร้อมคะแนนความเป็นไปได้ทางวิศวกรรม และคัด 42 configurations ก่อนรันผล',
'- พัฒนาตัวรัน 3 families: lexical scoped retrieval / typed subject–facet contracts / typed + bounded local-model evidence selection พร้อม source provider ร่วม. แต่ละหมวดมี configuration/ขอบเขตข้อมูลของตนเอง ไม่ใช่การติดตั้ง 42 full chatbot engines',
'- คำตอบใช้ experimental compiled read model จาก common 602 records และ owner overlays R108/R109 รวม 1,268 facts. เป็น candidate projection สำหรับทดลอง ไม่ใช่ import ลง schema common ที่เปิดใช้งานจริง',
'- ชุดหลักมี 100 คำถามต่อหมวด ใช้ชุดเดียวกันทั้งสาม Flow = 1,400 คำถาม / 4,200 executions ครบ ไม่มี key คู่ Flow–คำถามซ้ำหรือขาด',
'- ใช้ local model scb10x/typhoon2.5-qwen3-4b:latest เมื่อ hybrid ตีความแบบ typed ไม่ลงตัว ตรวจ digest ก่อน–หลัง ไม่บังคับเรียกโมเดลเมื่ออ่านตรงได้',
'- ไม่แก้ production R78, frozen R106, approvals หรือ logs เก่า; ผลพร้อมติดตามใน main_natural/TEST_COMPLETE.json','',
'## 2. คะแนนนี้หมายถึงอะไร','',
'คะแนนออกแบบในไฟล์ 01 เป็น heuristic สำหรับเลือกแนวทางล่วงหน้า โดยใช้ค่าประเมินร่วมตาม family และลำดับไอเดีย ไม่ได้มีผู้เชี่ยวชาญให้คะแนนอิสระทั้ง 140 แบบ จึงใช้เป็นสมมติฐานออกแบบเท่านั้น คะแนนที่ใช้เปรียบเทียบการตอบจริงคือตารางผล 4,200 executions ด้านล่าง','',
'ผ่านหนึ่งข้อเมื่อ source claim IDs ที่ตอบครบและไม่เกินขอบเขต ค่า/จำนวนที่ตรวจตรง evidence refs ตรง และ answer state ตรงกับ oracle ที่ตรึงจาก source ก่อนรัน. ตรวจโดยเครื่องจาก task/source contracts ไม่ใช่มนุษย์ตรวจความหมายคำตอบอิสระทั้งหมด','',
'โจทย์เป็น source-grounded natural paraphrases สำหรับการพัฒนา มี 60 single-need / 20 multi-need / 20 missing-or-unconfirmed ต่อหมวด บางข้อทดสอบ source claim เดียวกันด้วยสำนวนต่างกัน จึงไม่ใช่ 100 facts หรือ 100 semantic situations ที่เป็นอิสระต่อหมวด และยังไม่ใช่ representative holdout จากคำถามลูกค้าจริง','',
'แต่ละ adapter ได้รับหมวดที่เลือกไว้แล้ว จึงวัดคุณภาพตัวอ่านในหมวด ไม่วัดการเลือก 14 หมวดอัตโนมัติของ chatbot ทั้งระบบ. ไม่เอาคะแนนนี้ไปเทียบ 94.41% Legacy หรือผล full R106 ตรง ๆ','',
'## 3. ผลหลักรายหมวด','',
'| หมวด | ค้นข้อความ | Typed contract | Hybrid + LLM เมื่อจำเป็น | คะแนนสูงสุด | Flow คะแนนสูงสุด |','|---|---:|---:|---:|---:|---|']
for r in rankings:
 s={x['family']:x for x in stats if x['category']==r['category']}
 lines.append(f"| {r['category']} {r['name']} | {s['lexical']['passed']}% ({s['lexical']['flow_id']}) | {s['typed']['passed']}% ({s['typed']['flow_id']}) | {s['hybrid']['passed']}% ({s['hybrid']['flow_id']}) | {r['best_score_percent']}% | {', '.join(r['winning_flows'])} |")
lines+=['','### วิธีเลือกเมื่อคะแนนเท่ากัน','',
'รายงานทุก Flow ที่คะแนนสูงสุดร่วมกัน ไม่อ้างว่าตัวใดชนะด้าน accuracy เมื่อเท่ากัน. Candidate configuration เสนอเลือกตัวที่ตอบเกินขอบเขตน้อยกว่า แล้วจึงพึ่งโมเดลน้อยกว่า. เวลาในชุดนี้มี batch amortization ไม่ใช้เป็น production latency','',
'## 4. ผลละเอียดและจุดที่ยังพลาด','']
for r in rankings:
 lines += [f"### {r['category']} {r['name']}",'',f"คะแนนสูงสุด {r['best_score_percent']}% — {', '.join(r['winning_flows'])}; เสนอสำหรับประกอบ candidate: {r['recommended_flow']}",'',f"100 สำนวนในหมวดนี้ครอบคลุม oracle claim signatures ที่ต่างกัน {r['unique_oracle_claim_signatures']} แบบ ไม่ใช่ 100 facts อิสระ",'','| Flow | Single | Multi | ขาดข้อมูล/ยังไม่ยืนยัน | ส่งให้โมเดล | ปัญหาที่พบ |','|---|---:|---:|---:|---:|---|']
 for s in [x for x in stats if x['category']==r['category']]:
  v=s['strata'];lines.append(f"| {s['flow_id']} | {v['single_need']['passed']}/60 | {v['multi_need']['passed']}/20 | {v['missing_source']['passed']}/20 | {s['model']['questions_sent']} | {json.dumps(s['failure_patterns'],ensure_ascii=False)} |")
 fails=[x for x in allfail if x['category']==r['category']]
 # Preserve a small representative example from each tested strategy, not only the winner.
 for fam in ['lexical','typed','hybrid']:
  x=next((x for x in fails if x['family']==fam),None)
  if x:
   lines+=['',f"ตัวอย่าง {x['flow_id']} / {x['question_id']}: {x['question']}",'', '> '+x['result']['answer'][:900].replace('\n','\n> '),'', 'ผลตรวจ: '+json.dumps(x['grade'],ensure_ascii=False)]
 lines+=['']
modelstats={'attempts':len(events),'http_transport_success':sum(e['transport_ok'] for e in events),'schema_valid_batches':sum(e['schema_ok'] for e in events),'questions_sent':sum(e['question_count'] for e in events),'errors':dict(collections.Counter(e.get('error','none').split(':')[0] for e in events if not e['schema_ok']))}
lines+=['## 5. โมเดลและข้อผิดพลาดของ protocol','',json.dumps(modelstats,ensure_ascii=False,indent=2),'',
'HTTP สำเร็จไม่ได้แปลว่าโมเดลส่งแผนครบหรือเลือกหลักฐานถูก. Invalid/missing per-question plans เป็น model-schema/planning failure แยกจาก transport failure; กลุ่มนั้นยังนับไม่ผ่านในคะแนน end-to-end ของ adapter ไม่ตัดออกเพื่อเพิ่มเปอร์เซ็นต์','',
'แบบจำลองตอบหลายแผนในหนึ่ง HTTP call เพื่อประหยัดเวลา ถ้าชุด JSON ขาดแผนใด parser ปัจจุบันปฏิเสธ batch นั้นทั้งหมด ผลนี้เป็นข้อจำกัดของ implementation ที่ทดสอบ ไม่ใช่หลักฐานว่าโมเดลไม่เชื่อมต่อ. รุ่นต่อไปควรใช้จำนวน items ใน JSON schema และแยกผลที่ใช้ได้ต่อ item โดยเก็บ failed items ไว้ ไม่ต้องเลือก lexical เสมอเมื่อมี known source gap','',
'## 6. ข้อจำกัดเฉพาะข้อมูลและหมวด','',
'- C12 เป็น controlled provider snapshots รวม available/booked/unavailable/stale ไม่ได้เรียกหรือยืนยันสถานะจองลูกค้าจริง',
'- C14 ใช้ synthetic news fixtures เพราะฐานจริงไม่มี news records เพียงพอ และมีเคสถามข่าวจริงที่ต้องตอบว่าไม่มีแหล่งยืนยัน; ไม่อ้างว่ามีงานเหล่านั้นจริง',
'- C13 มี source excerpts ที่ยังไม่มีคำแปลอังกฤษ บันทึก flags แยก ไม่อ้างว่าคะแนน claim matching ยืนยันคุณภาพภาษาอังกฤษ',
'- C06 บางคำถามระยะเวลาใช้ชื่อ record ภายในแทนชื่อบริการที่ลูกค้าใช้ เพราะ projection ยังไม่มีชื่อแสดงผลครบ จึงยังไม่ใช่ชุดทดสอบภาษาลูกค้าจริงทั้งหมด',
'- คำถามแต่ละหมวดมี locale th 70 / en 20 / auto 10; เคส missing-source ทั้ง 20 ข้อต่อหมวดเป็นภาษาไทยทั้งหมด จึงยังไม่ได้ทดสอบ unknown handling ภาษาอังกฤษในชุดหลัก',
'- Required selected source claims ที่ใช้ oracle บางคำถามยังเป็น granularity ระดับ source clause/field; คำตอบที่เท่ากันทางความหมายแต่ไม่มี claim ID ตรงอาจไม่ผ่าน จึงไม่ใช้คะแนนนี้เป็น semantic accuracy โดยทั่วไป',
'- ตัวเลือก 140 แบบที่ไม่ถูกคัดมีเพียง design feasibility score ไม่ได้อ้างว่ารันทดสอบครบ 140 implementations',
'- Three shared algorithm families ถูกใช้ซ้ำตาม domain configurations ไม่ได้เขียน code engine คนละชุด 42 ชุด และยังไม่รองรับ task ย่อยทุกชนิดใน R112 อย่าง production-complete',
'- Source view รวม facts ที่เลือกและ owner statements ไม่ใช่การย้าย field/relations ทั้ง schema ลง chatbot runtime จึงยังต้อง integration และ data-only lifecycle checks ในระบบจริง','',
'## 7. การรักษาขอบเขตและการรันต่อ','',
'รอบหลักหยุดครั้งแรกจาก WinError 5 ขณะเปลี่ยนไฟล์สถานะ ไม่ใช่จากตัวอ่านตอบคำถาม มี recovery control แยกและใช้ผลที่บันทึกแล้วต่อโดยไม่ลบหรือเปลี่ยนคะแนน จากนั้นหยุด process ของ benchmark ที่ตรวจ command line แล้วที่ 2,945 ผล เพื่อตรวจคำสั่งเจ้าของก่อนเข้า C13 พบคำถามหน่วยโทษ Pause Tekken 7 ข้อที่เจ้าของเคยสั่งงด และยืนยัน C13 ยังมี 0 executions จึงแทนด้วยคำถามกติกางานอนาคตที่ไม่มี source ใน stratum เดียวกัน ก่อนรันทั้งสาม Flow ของหมวดนั้น ใช้ EFFECTIVE_QUESTIONS_1400.jsonl ร่วมกัน และเก็บ workload เดิมกับรายการเปลี่ยนใน EXCLUSION_ADDENDUM.json ไม่ถือข้อที่งดเป็นผ่าน','',
'ตอนหยุดไม่มี model event ที่บันทึกไว้แต่ขาดผลคำตอบ อาจมี HTTP request ที่ยังไม่บันทึกผลก่อนถูกหยุด จึงไม่อ้างว่าไม่มี HTTP attempt ซ้ำเลย หลักฐานยืนยันได้คือ persisted Flow–question results ครบและไม่ซ้ำ กับคำถามในขอบเขตที่งดไม่ได้ execute ใน main run','',
'## 8. ทำไมมีผล pilot แยก','',
'ชุดแรกใช้คำถามที่ตรงชื่อฟิลด์เกินไป ทำให้ typed/hybrid ส่วนใหญ่ผ่าน 100% โดยไม่เรียก LLM จึงไม่ใช้เป็นข้อสรุปเลือก Flow. เก็บผล 4,200 executions เดิมใน pilot_field_contract ครบ แล้วสร้างชุดภาษาธรรมชาติหลักก่อนตรึง implementation/expected ใหม่ ไม่แก้คะแนนเก่าหรือคัดผลที่ดีที่สุดจากสองชุด. รวมการตรวจทางเทคนิค pilot และชุดหลัก 8,400 executions แต่คะแนนตารางหลักใช้ main_natural เท่านั้น','',
'## 9. ข้อเสนอหลังเห็นผล','',
'1. ประกอบ candidate ด้วย winner/tie recommendation รายหมวดใน WINNER_CANDIDATE_CONFIG.json เป็นข้อเสนอ ไม่สลับ production อัตโนมัติ',
'2. แก้ช่องว่างที่เห็นจริง: unknown qualifier, facet/subject ambiguity, multi-need coverage และ structured model output. เก็บ successful typed reads เป็นทางหลักเมื่อเหมาะสม ไม่เพิ่ม LLM ให้ทุกคำถาม',
'3. ตรวจด้วยคำถามอิสระจากผู้ใช้และ retained full corpus ก่อนอ้างว่าใกล้ Legacy; ถ้าต้องการคะแนนคำตอบถูกทางความหมาย ต้องเพิ่ม semantic/source review ที่อิสระจากตัวอ่าน',
'4. หลัง integration owner fields, dispatcher และ lifecycle พร้อม จึงทำ full common LLM ON ตามแผนเดิม โดยยังแยก fixture/transport/protocol/source gap และข้อมูลต่างรุ่น','',
'## 10. ไฟล์ใช้งาน','',
'- 01_DESIGNS_AND_SELECTION_TH.md / DESIGNS_140.json: แนวคิด 140 แบบและคะแนนออกแบบ',
'- SELECTED_42.json / flows/: configuration ที่รันได้จริง 3 แบบต่อหมวด',
'- flow_engine.py: เรียก CLI ด้วย --flow <id> --question <ข้อความ> --locale th หรือ en',
'- EFFECTIVE_QUESTIONS_1400.jsonl: workload ที่ใช้จริงร่วมกันทุก Flow; NATURAL_QUESTIONS_1400.jsonl เก็บต้นฉบับก่อน owner exclusion addendum',
'- main_natural/RESULTS.jsonl และ MODEL_EVENTS.jsonl: คำถาม คำตอบ claim/evidence และ model trace ทุกครั้ง',
'- SCORES_42.json / RANKING_BY_CATEGORY.json / ALL_FAILED_CASES.jsonl: คะแนน ลำดับ และคำตอบที่ยังไม่ผ่านทั้งหมด',
'- main_natural/RUN_FREEZE.json / TEST_COMPLETE.json: coverage, code/data hashes และ identity ของโมเดล','',
'รายงานนี้เป็นผลทดลองเปรียบเทียบตัวอ่านในหมวด ไม่ใช่คำรับรองว่าระบบแชทจริงได้คะแนนดังตารางแล้ว',
]
(R/'02_BENCHMARK_REPORT_TH.md').write_text('\n'.join(lines)+'\n','utf8')
payload={'complete':True,'designs':140,'implemented_domain_configurations':42,'headline_executions':4200,'headline_questions_per_category':100,'pilot_executions_retained_separately':4200,'total_executions_including_pilot':8400,'rankings':rankings,'model':modelstats,'production_installed':False,'global_routing_tested':False}
write(R/'FINAL_SUMMARY.json',payload)
print(json.dumps({'rankings':[{k:r[k] for k in ['category','all_scores','winning_flows','recommended_flow']} for r in rankings],'model':modelstats},ensure_ascii=False))
