import collections,hashlib,json,math,statistics
from pathlib import Path
R=Path(__file__).resolve().parent;ROOT=R.parent;config=json.loads((R/'PROCESS.json').read_text('utf8'))
def readrows(p):return [json.loads(l) for l in p.read_text('utf8').splitlines() if l.strip()]
def link(p,label):return '['+label+'](<'+str(p.resolve()).replace('\\','/')+'>)'
def stats(rows):
 vals=sorted(r['wall_sec'] for r in rows)
 return {'requests':len(vals),'median_sec':statistics.median(vals),'p95_nearest_rank_sec':vals[math.ceil(.95*len(vals))-1],'max_sec':max(vals),'http_errors':sum(bool(r.get('error')) for r in rows)}
old=readrows(Path(config['legacy']['output'])/'HTTP_RESULTS.jsonl');new=readrows(Path(config['current']['output'])/'HTTP_RESULTS.jsonl')
oldsingle=[x for x in old if x['kind']=='single'];oldtalk=[x for x in old if x['kind']=='conversation'];retained=readrows(ROOT/'r126_latency_audit_20261023/run_1792765098897050300/HTTP_RESULTS.jsonl')
assert len(oldsingle)==len(retained)==34 and len(oldtalk)==len(new)==19
assert all(a['question']==b['question'] for a,b in zip(oldsingle,retained))
assert all(x.get('response',{}).get('ok') for x in [*old,*new,*retained])
notes={
'date_explicit':'ทั้งคู่ได้วันจันทร์ 26 ต.ค. / 13–16 ใหม่สรุปเฉพาะวันที่กระชับกว่า เดิมใส่ปฏิทินและทั้งสัปดาห์ นับ cold start แยกจาก warm',
'date_english':'เดิมตอบตารางรายสัปดาห์ ไม่ resolve October 26; ใหม่ unconfirmed หลัง model ทั้งคู่ยังตอบวันที่เฉพาะไม่ครบ',
'date_paraphrase':'ทั้งคู่พูดช่วงวันจันทร์ได้ แต่ยังไม่ได้ยืนยัน date ของคำว่าจันทร์หน้าและ exception ของวันนั้น; ใหม่เสีย context call',
'date_relative':'อีกสามวันไม่ถูก resolve เฉพาะวัน เดิมให้ตารางทั่วไป ใหม่ unconfirmed; date parser gap ทั้งคู่',
'catalog_direct':'ทั้งคู่ให้ catalogue ตาม source เดิม 42 games; ต้องแยก unique game จาก offered service relations ไม่ใช้จำนวน label แทนกัน',
'catalog_paraphrase':'เดิมเลือก equipment PS5 แทนรายชื่อเกม ใหม่ให้ PS5 catalogue ถูกประเภทคำตอบ แต่เสีย model ประมาณ 28 วินาที',
'catalog_filter':'เดิมให้ 42 games ทั้งหมดไม่กรองสี่คน ใหม่แจ้ง unsupported/data limitation ทั้งคู่ยังไม่ให้รายการที่ตรวจ player mode แล้ว',
'equipment_direct':'เดิมมี definition/quantity/location/uses ใหม่เป็น usage list จึงขาดจำนวน/ที่ตั้ง และแหล่งใน side panel ว่าง แม้ internal refs มี',
'equipment_paraphrase':'เดิมคืน PC เครื่องเดียว ใหม่เลือก inventory subset ยังไม่พิสูจน์อุปกรณ์เตรียมไว้ครบทุกชนิด ทั้งคู่ต้อง inventory scope ตามคำถาม',
'hardware':'ทั้งคู่มี RTX 5060 ในข้อมูลเดิมก็มีอยู่แล้ว ใหม่เลือก GPU เฉพาะส่วนจึงกระชับกว่า แต่ต้องคงขอบเขตการตรวจยืนยันเครื่องจริง',
'price_digits':'ทั้งคู่ 70 บาทสำหรับหนึ่งชั่วโมงบุคคลทั่วไป เดิม package formula ใหม่ซ้ำตาม service record สองกลุ่มเครื่อง',
'price_words':'เดิมรักษา external_unspecified แสดง 50/140 ตามสองกลุ่ม ใหม่สมมติคนนอก=General Adult 140; semantic ambiguity กับ latency ไม่ใช่ arithmetic failure อย่างเดียว',
'price_compare':'ตัวเลขสองบริการสำหรับ PSU เป็นศูนย์ตามอัตรา แต่เดิม PC แสดงแพ็กเกจโดยไม่คูณสองชั่วโมง ใหม่ใช้ price_calculate ไม่ใช่ compare และยาวซ้ำ; validity คนละ source revision',
'price_multi_audience':'เดิมลดเหลือ general adult 1 คน ตอบ140 ไม่ใช่ยอดรวมโจทย์ ใหม่ถามจำนวนซ้ำแม้ผู้ใช้บอกครบ; ghost audience + rate cardinality เป็นสาเหตุยืนยัน R126',
'booking_direct':'เดิมสรุปขั้นตอนเป็น bullet ใหม่คงข้อความสอง source ที่สาระคล้ายกันแล้ว partial; canonicalization และ procedure formatter ยังขาด',
'booking_paraphrase':'เดิมตอบที่ตั้งผิดงาน ใหม่ตี booking ถูกแต่ reader entity_not_bound ไม่มีคำตอบ; task-to-reader interface ขาด',
'booking_compound':'ทั้งคู่แยกจองกับตารางได้ เดิม heading Question 1/2 และ steps ชัด ใหม่รักษา source variants แต่ verbose/model call',
'cancel':'ทั้งคู่ตอบยกเลิกล่วงหน้า1ชั่วโมงสำหรับ wording ที่ระบุ booking ชัด แต่ follow-up ไทยในบทสนทนายังไม่ทำงาน',
'policy_direct':'ทั้งคู่รักษาความต่างนำเข้ากับกินได้ แสดงว่าตัวป้องกัน negation เฉพาะ intent นี้ใช้งานได้',
'policy_paraphrase':'เดิม user_service_facts ตอบให้ดูเพื่อนได้ ใหม่ missing_source ทั้งที่ migrated owner FAQ มี จัดเป็น confirmed retrieval regression',
'policy_personal_device':'คำตอบตรงข้าม: เดิมไม่อนุญาตจาก owner answers 8ต.ค. ใหม่อนุญาตแต่ให้แจ้งตามข้อมูล owner รุ่นใหม่; แยก data revision ไม่ตัดสินว่าใหม่ผิดเพราะไม่เหมือนเดิม',
'documents':'ทั้งคู่ให้เอกสารได้ แต่ใหม่ใช้ selector หลายวินาที เดิม owner fact ตรง ไม่มีเหตุจำเป็นต้อง generation ทุกครั้ง',
'controls_direct':'ทั้งคู่ให้ชุดปุ่มตาม source พร้อม caveat secondary mapping ต้องแยกครบชุดในแหล่งจากยืนยันตรงเครื่องศูนย์',
'controls_paraphrase':'เดิมตอบเกม summary ใหม่ตอบเล็งL2แทน heavyR2 ทั้งคู่ผิดงาน; R126พิสูจน์ R2ถูกตัดจาก top8 candidate',
'compound_controls_price':'เดิมตกส่วนปุ่ม ใหม่ส่งรายการปุ่มพร้อมราคาพร้อมแจ้ง12 entriesไม่ระบุsubset8; ใหม่ coverage ดีกว่าแต่ยังไม่ควรเรียก8ปุ่มครบ',
'rules':'เดิมได้แค่ Round Loss/Map Forfeit ใหม่ได้ Intent/Impact principle ทั้งคู่ไม่ครบ penalty types',
'ambiguous':'ไม่มีประวัติจริงทั้งคู่ควรถามเพิ่ม การขอความชัดไม่ใช่ content failure แต่ใหม่เสียmodelcallก่อนถาม',
'unknown_game':'ไม่มี source ยืนยัน HadesII การไม่เดาเป็นพฤติกรรมเหมาะสม แต่ดู latency/clarification scope แยกจาก accuracy',
'live_current':'ทั้งคู่ live WordPress จริงพร้อมtimestamp ขณะทดสอบอยู่นอกเวลา; คนละเวลาจึงไม่เทียบ occupancyเป็นgoldเดียวกัน',
'live_day':'เดิมใช้วันนี้23ทั้งที่ถาม27 ใหม่ใช้27และPC02ถูก scope เป็นข้อดีของ date/live R125',
'live_missing_scope':'ใหม่ถามชื่อเครื่องเฉพาะช่องที่ขาด ชัดกว่า generic clarification หรือเดารายเครื่อง',
'repeat_fast':'ถามซ้ำ native date ยังเร็ว warm ห้ามเอาครั้งcoldเปรียบเทียบเป็นsteady-state',
'repeat_slow':'ถามซ้ำ English date ยังเสียmodelและunconfirmed ไม่มีผลแก้ parser จากการถามซ้ำ',
'repeat_compound':'ยืนยันคำตอบแบบเดียวกับ booking_compound เดิมแยกงานโดยไม่ generation ใหม่ยังใช้contextgeneration; ไม่ใช่ข้อใหม่อิสระ'
}
talknotes={
'game_reference':'ยืนยัน context regression: เดิมเติมเกมรอบ2/3 ใหม่มีรหัสเกมในstateแต่ไม่ผูกtaskแล้วคืนunconfirmedทั้งสองรอบ ข้อมูลความสัมพันธ์และR2มีจริง',
'booking_reference':'รอบแรกใหม่ตอบ procedure ได้ตรงกว่าเดิมที่ตอบเลือกโซน แต่คำยกเลิกแบบไม่มีคำว่าจองทำให้ทั้งคู่หาไม่เจอ เดิม topic_shift และ fallback มี embed404/generate client timeout จึงไม่จัดผลเดิมข้อนี้เป็น pure content/Flow failure; ใหม่ entity_not_bound โดย model transportสำเร็จ',
'price_reference':'ยืนยัน slot regression: เดิมเก็บaudience/service/duration เปลี่ยนสองชั่วโมงและPS5ได้ ใหม่ถามบริการซ้ำแล้วตอบจำนวนจอยPS5 ความต่อเนื่องงานราคาหาย',
'date_clarification':'ใหม่ทำได้ดีกว่า: ขอเดือนแล้วresume15พ.ย.2026ได้ เดิมให้ตารางทั่วไปแล้วไม่เข้าใจคำตอบพฤศจิกายน',
'live_clarification':'ใหม่ทำได้ดีกว่า: ขอเครื่องแล้วใช้วันที่27เดิมกับPC2เรียกproviderถูกscope เดิมไม่resumeและคำตอบก่อนหน้าละวัน',
'topic_shift':'ใหม่วันพรุ่งนี้ถูกและกระชับ แต่ BeatSaberคืออะไร ถูก equipment frameแย่งแล้วตอบservice_capacity; เดิมdefinitionถูก แต่รอบถามกี่คนเดิมก็คืนsummary ไม่ตอบจำนวน จึงไม่ผ่านทั้งคู่',
'multi_target':'เดิมรอบแรกให้ทั้งPS5และPC ใหม่มีplatformconstraintsทั้งคู่แต่เลือกPS5อย่างเดียวแล้วบอกsupported (binding longest alias); รอบอันที่สองกำกวมจากลำดับคำถาม/ลำดับแสดงต่างกัน ทั้งคู่ไม่ได้resolve ต้องเก็บordered optionsและถามclarifyเมื่ออ้างอิงไม่ชัด',
'game_controls':'เดิมTekken definitionและต่อปุ่ม12entriesได้ ใหม่definitionถูกC03equipmentแย่งตอบcapacity แล้วรอบปุ่มถามชื่อเกมใหม่ เป็นทั้งcross-domain alias precedenceและstate/taskresumption failure'
}
def evidence(b):
 art=b.get('decision_artifact',{});d=art.get('domain_flow',{});needs=art.get('need_results',[])
 return {'mode':b.get('mode'),'resolved_question':b.get('resolved_question'),'context_resolution':b.get('context_resolution'),'request_plan':b.get('request_plan'),'common_read_state':b.get('common_read_state'),'understanding':art.get('understanding'),'query_plan':art.get('query_plan'),'need_results':needs,'claims':d.get('typed_claims'),'sources':b.get('sources'),'trace':b.get('trace'),'execution_contract':art.get('execution_contract'),'conversation_state':b.get('conversation_state')}
pairs=[]
for a,b in zip(oldsingle,retained):
 pairs.append({'kind':'single','key':a['key'],'question':a['question'],'review':notes[a['key']],'legacy':a,'current':b,'legacy_evidence':evidence(a['response']),'current_evidence':evidence(b['response'])})
for name,questions in json.loads((R/'CONVERSATIONS.json').read_text('utf8')):
 aa=[x for x in oldtalk if x['key']==name];bb=[x for x in new if x['key']==name]
 assert len(aa)==len(bb)==len(questions)
 for a,b in zip(aa,bb):
  assert a['question']==b['question']
  pairs.append({'kind':'conversation','key':name,'turn':a['turn'],'question':a['question'],'review':talknotes[name],'legacy':a,'current':b,'legacy_evidence':evidence(a['response']),'current_evidence':evidence(b['response'])})
summary={'matched_single':34,'unique_single_questions':len({x['question'] for x in oldsingle}),'conversations':8,'turns_per_arm':19,'retained_current_single':34,'fresh_http_requests':len(old)+len(new),'legacy_single':stats(oldsingle),'current_retained_single':stats(retained),'legacy_conversation':stats(oldtalk),'current_conversation':stats(new),'full_test':False,'overall_accuracy_estimated':False}
summary['client_model_transport']={}
for arm,c in config.items():
 timing=readrows(Path(c['output'])/'TIMINGS.jsonl');events=[(row['question'],e) for row in timing for e in row.get('http',[]) if e['kind']=='model']
 summary['client_model_transport'][arm]={'pipeline_calls':len(timing),'attempts':len(events),'completed':sum(bool(e.get('transport_ok')) for _,e in events),'failures':[{'question':q,**e} for q,e in events if not e.get('transport_ok')]}
# Retain actual model wire for this audit window; no replay or synthetic inference.
start=min(x['started_at'] for x in [*old,*new]);end=max(x['started_at']+x['wall_sec'] for x in [*old,*new])
wirepath=ROOT/'r124_legacy_guided_parity_20261023/inference_1792743193162376900/REQUESTS.jsonl'
wire=[]
with wirepath.open(encoding='utf8') as f:
 for line in f:
  x=json.loads(line)
  if start<=x.get('started_at',0)<=end:wire.append(x)
(R/'MODEL_WIRE_EVIDENCE.json').write_text(json.dumps({'source':str(wirepath),'window':[start,end],'note':'Timestamp window; may include concurrent user requests. Use question/profile and per-request TIMINGS for attribution.','events':wire},ensure_ascii=False,indent=2),'utf8')
verification={}
for arm,c in config.items():
 before=json.loads((Path(c['output'])/'SOURCE_BEFORE.json').read_text('utf8'));S=Path(c['system']);missing=[];changed=[]
 for rel,sha in before.items():
  p=S/rel
  if not p.exists():missing.append(rel)
  elif hashlib.sha256(p.read_bytes()).hexdigest()!=sha:changed.append(rel)
 verification[arm]={'files_checked':len(before),'missing':missing,'changed':changed,'source_unchanged':not missing and not changed}
for name,p in [('r125_frozen',ROOT/'r125_date_context_presentation_20261023/FINAL_SOURCE_FREEZE.json'),('legacy_original',ROOT/'r124_legacy_guided_parity_20261023/TEACHER_FREEZE.json')]:
 h=json.loads(p.read_text('utf8'));missing=[];changed=[]
 for path,sha in h.items():
  f=Path(path)
  if not f.exists():missing.append(path)
  elif hashlib.sha256(f.read_bytes()).hexdigest()!=sha:changed.append(path)
 verification[name]={'files_checked':len(h),'missing':missing,'changed':changed,'source_unchanged':not missing and not changed}
summary['verification']=verification
(R/'COMPARISON.json').write_text(json.dumps({'summary':summary,'pairs':pairs},ensure_ascii=False,indent=2),'utf8')
(R/'VERIFICATION.json').write_text(json.dumps(verification,ensure_ascii=False,indent=2),'utf8')
(R/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8')
md=['# คำถามเดียวกัน: คำตอบเดิม / R125 และ log จริง','','อ่านข้อสรุป สาเหตุ โค้ด และ Flow ทั้งสองที่ '+link(R/'REVIEW_TH.md','REVIEW_TH.md'),'','## หลักฐานและขอบเขต','',f"34 paired single requests ({summary['unique_single_questions']} unique wordings รวมข้อซ้ำ) และ 8 บทสนทนา / 19 turns ต่อระบบ; รอบนี้ HTTP ใหม่ 72 requests รวม legacy34+38conversation; R125 single ใช้ผล HTTP จริง R126 34 ที่เก็บแล้ว ไม่ใช่ full test และไม่คำนวณ accuracy ทั้งระบบ",'','| เวลา HTTP | เดิม | ใหม่ |','|---|---:|---:|',f"| median คำถามเดี่ยว | {summary['legacy_single']['median_sec']:.3f}s | {summary['current_retained_single']['median_sec']:.3f}s |",f"| median turn บทสนทนา | {summary['legacy_conversation']['median_sec']:.3f}s | {summary['current_conversation']['median_sec']:.3f}s |",'','ข้อมูลและ model profile คนละรุ่น จึงไม่ใช่ causal Flow-only benchmark; latency เป็นเวลาทดสอบเครื่องนี้ ไม่ใช่ SLA','', '**ข้อจำกัด transport ที่ต้องแยก:** legacy follow-up ยกเลิกมี /api/embed HTTP404 และ /api/generate client timeout จึงไม่จัดผลสุดท้ายข้อนี้เป็น pure Flow/content failure; R125 conversation 11 model requests สำเร็จทั้งหมด คำตอบผิดงานยังเกิดได้แม้ model transport สำเร็จ','',link(R/'COMPARISON.json','HTTP responses + trace/decision artifact เต็ม'),link(R/'MODEL_WIRE_EVIDENCE.json','model wire ที่ backend ใช้จริง'),link(R/'SOURCE_COUNTERFACTUALS.json','readonly source binding controls'),link(R/'VERIFICATION.json','hash verification'),'','## คำถามเดี่ยว','']
for i,p in enumerate(pairs,1):
 if p['kind']=='conversation' and (i==35 or p['turn']==1):md.extend(['',f"## บทสนทนา: {p['key']}",'',talknotes[p['key']],''])
 md.extend([f"### {i}. {p['key']}"+(f" / turn {p['turn']}" if p['kind']=='conversation' else ''),'',p['question'],'',f"**วิเคราะห์:** {p['review']}",''])
 for arm,label in [('legacy','เดิม'),('current','ใหม่ R125')]:
  row=p[arm];b=row['response'];ev=p[arm+'_evidence'];md.extend([f"**{label} — {row['wall_sec']:.3f} วินาที / {b.get('mode')}**",'','```text',b.get('answer',''),'```',''])
  excerpt={'resolved_question':ev['resolved_question'],'context_resolution':ev['context_resolution'],'request_plan':ev['request_plan'],'common_read_state':ev['common_read_state'],'query_plan':ev['query_plan'],'meaning_tasks':(ev.get('understanding') or {}).get('tasks'),'reason_codes':[(n.get('need_id'),n.get('status'),n.get('reason_codes')) for n in ev.get('need_results') or []],'source_ids':[s.get('id') for s in ev.get('sources') or []]}
  md.extend(['<details><summary>Log: ข้อความที่เข้า executor / state / source ที่เลือก</summary>','','```json',json.dumps(excerpt,ensure_ascii=False,indent=2),'```','','</details>',''])
(R/'COMPARISON_TH.md').write_text('\n'.join(md),'utf8')
# Link directly to source lines, retaining excerpts for review even when code moves.
specs=[('r125_date_context_presentation_20261023/system/app/web_api/server.py',650,680),('r124_legacy_guided_parity_20261023/teacher/app/session/context_resolver.py',872,925),('r125_date_context_presentation_20261023/system/app/knowledge/common/answer.py',199,213),('r125_date_context_presentation_20261023/system/app/knowledge/common/domain_flow/integration.py',49,118),('r125_date_context_presentation_20261023/system/app/knowledge/common/domain_flow/understanding.py',159,177),('r124_legacy_guided_parity_20261023/serve_model.py',58,83),('r124_legacy_guided_parity_20261023/context_contract.py',32,36),('r125_date_context_presentation_20261023/system/app/knowledge/common/domain_flow/meaning_review.py',72,97),('r125_date_context_presentation_20261023/system/app/knowledge/common/domain_flow/index.py',47,62),('r125_date_context_presentation_20261023/system/app/knowledge/common/domain_flow/model.py',59,78),('r125_date_context_presentation_20261023/system/app/knowledge/common/domain_flow/meaning_reader.py',109,120),('r125_date_context_presentation_20261023/system/app/web_api/server.py',215,256)]
code=['# Source evidence ที่ใช้วิเคราะห์','','อ่านประกอบ response และ trace ใน COMPARISON.json ไม่ถือ code path ที่มีอยู่เท่ากับ path ที่ถูกใช้ทุกครั้ง','']
for path,a,b in specs:
 p=ROOT/path;lines=p.read_text('utf8').splitlines();code.extend([f'## {path}:{a}','',link(Path(str(p)+':'+str(a)),'เปิด source บรรทัดเริ่มต้น'),'','```python',* [f'{n}: {lines[n-1]}' for n in range(a,min(b,len(lines))+1)],'```',''])
(R/'CODE_EVIDENCE.md').write_text('\n'.join(code),'utf8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
