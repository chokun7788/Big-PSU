"""Analyze ALL selected saved output against the SAME retained oracle rows."""
import collections,gzip,hashlib,json,re,sqlite3,statistics
from datetime import datetime
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent;RUN=R/'full01'
def read(p):return json.loads(p.read_text('utf8'))
def lines(p):return map(json.loads,p.open(encoding='utf8'))
def pct(n,d):return f'{100*n/d:.2f}%' if d else 'N/A'
def ratio(n,d):return f'{n:,}/{d:,} ({pct(n,d)})'
def norm(x):return re.sub(r'\s+',' ',str(x)).casefold().strip()
def title(r):
 for k in ['title','name','display_name','event_name','question']:
  f=r.get('fields',{}).get(k,{})
  if f.get('status')=='known':return f['value'] if isinstance(f['value'],dict) else {'th':str(f['value']),'en':str(f['value'])}
 return {'th':r.get('record_id',''),'en':r.get('record_id','')}
def value(r,k):
 f=r.get('fields',{}).get(k,{})
 return f.get('value') if f.get('status')=='known' else None
native=read(B/'r115_native_http_validation_20261021/NATIVE_SOURCE_REFERENCE.json');records=native['records']
allowed={(p['source_id'],p['locator']) for r in records.values() for f in r['fields'].values() for p in f.get('evidence_refs',[])}
def source_review(row):
 raw=row['result'];art=raw.get('decision_artifact') or {};packets=list((art.get('domain_flow') or {}).get('typed_claims') or [])+list(art.get('claim_packets') or [])
 for n in art.get('need_results',[]):packets+=n.get('claim_packets') or []
 packets=list({json.dumps(c,ensure_ascii=False,sort_keys=True):c for c in packets if isinstance(c,dict)}.values())
 unknown=[{'record_id':c.get('record_id'),'ref':p} for c in packets for p in c.get('evidence_refs',[]) if (p.get('source_id'),p.get('locator')) not in allowed]
 reasons=collections.Counter(str(s) for n in art.get('need_results',[]) for s in n.get('reason_codes',[]))
 states=collections.Counter(str(n.get('status')) for n in art.get('need_results',[]))
 body=raw.get('answer','');q=row['question'];zone_evidence=[];control_set_gap=None
 # Additional source-set diagnostic; it never changes the retained oracle.
 if (art.get('domain_flow') or {}).get('path')=='domain_readers' and re.search(r'ปุ่มอะไรบ้าง|ปุ่ม.*ทั้งหมด|all (?:the )?(?:buttons|controls)|(?:buttons|controls).*ทั้งหมด',q,re.I):
  fs=[f for f in native['facts'] if f['category']=='C05']
  targets={f['subject']['en'].split(' / ')[0] for f in fs if norm(f['subject']['en'].split(' / ')[0]) in norm(q)}
  targets={s for s in targets if not any(s!=t and s in t for t in targets)}
  pool=[f for f in fs if f['subject']['en'].split(' / ')[0] in targets]
  explicit=None
  for platform,pattern in [('ps5',r'ps5|playstation'),('pc',r'\bpc\b|keyboard'),('switch',r'switch|nintendo')]:
   if re.search(pattern,q,re.I):explicit=platform;break
  if explicit:pool=[f for f in pool if explicit in norm(f['subject']['en'])]
  scopes={f['subject']['en'] for f in pool}
  expected={f['id'] for f in pool};got={c.get('fact_id') for c in packets if c.get('fact_id') in expected}
  if len(scopes)==1 and got and expected-got:
   control_set_gap={'requested':'all controls, single source platform scope','scope':next(iter(scopes)),
       'available_binding_count':len(expected),'returned_binding_count':len(got),'missing_fact_ids':sorted(expected-got),
       'top_k_truncation_possible':len(expected)>8 and len(got)<=8,'source_record_ids':sorted({f['record_id'] for f in pool})}
 if re.search(r'โซน|\bzone\b',q,re.I):
  for c in packets:
   if c.get('facet')!='studio_services':continue
   gid=c.get('record_id');paths=[]
   for offer in records.values():
    if offer['kind']!='game_service' or value(offer,'game_id')!=gid or value(offer,'offered') is not True:continue
    sid=value(offer,'service_id');service=records.get(sid,{})
    for resource_id in value(service,'resource_ids') or []:
     resource=records.get(resource_id,{});zone=records.get(value(resource,'zone_id'),{})
     if zone:paths.append({'game_id':gid,'offer_id':offer['record_id'],'service_id':sid,'resource_id':resource_id,'zone_id':zone['record_id'],'zone_title':title(zone)})
   labels={s for p in paths for s in p['zone_title'].values() if s}
   if paths and not any(norm(s) in norm(body) for s in labels):zone_evidence+=paths
 return {'returned_claim_packets':len(packets),'unrecognized_source_refs':unknown,'need_reason_codes':dict(reasons),'need_statuses':dict(states),
  'response_type':art.get('response_type'),'domain_flow':{k:(art.get('domain_flow') or {}).get(k) for k in ['path','categories','category','english_translation_missing']},
  'internal_metadata_visible':any(x in body for x in ['"r114_fact"','"query_profile"','"source_record_id"']),
  'service_instead_of_explicit_zone_source_paths':zone_evidence,'all_controls_source_set_gap':control_set_gap,
  'claims':[{'record_id':c.get('record_id'),'facet':c.get('facet') or c.get('field'),'value':c.get('value'),'evidence_refs':c.get('evidence_refs',[])} for c in packets]}

def main():
 done=read(RUN/'TEST_COMPLETE.json');assert done['complete'] and done['unique_request_keys']==2108 and done['grades']==5643
 assert all(done[k] is True for k in ['all_selected_keys_recorded','source_code_inputs_unchanged','original_sources_and_results_unchanged','model_identity_verified'])
 out=R/'analysis';out.mkdir(exist_ok=False)
 jobs={j['key']:j for j in lines(R/'SELECTED_JOBS.jsonl')};old={x['key']:x for x in lines(R/'BASELINE_SCORED_V2.jsonl')}
 allocation={x['domain']:x for x in read(R/'SAMPLE_ALLOCATION.json')};seen=set();counts=collections.defaultdict(collections.Counter)
 issues=collections.Counter();regressions=[];improvements=[];failure_rows=[];durations=[];same_grade_ids=set();audits=collections.Counter()
 audit_file=(out/'PER_REQUEST_REVIEW.jsonl').open('x',encoding='utf8');grade_file=gzip.open(out/'GRADE_COMPARISON.jsonl.gz','xt',encoding='utf8')
 for row in lines(RUN/'RESULTS.jsonl'):
  key=row['key'];assert key not in seen and key in jobs;seen.add(key);j=jobs[key];b=old[key]
  assert row['question']==j['question']==b['question'] and row['requested_locale']==j['locale']==b['locale']
  assert len(row['grades'])==len(b['grades'])==len(j['entries']);durations.append(row['elapsed_sec'])
  source=source_review(row)
  audits['response_type:'+str(source['response_type'])]+=1
  audits['requests_with_unknown_refs']+=bool(source['unrecognized_source_refs']);audits['internal_metadata_visible']+=source['internal_metadata_visible']
  audits['service_zone_projection_gap_requests']+=bool(source['service_instead_of_explicit_zone_source_paths'])
  audits['all_controls_source_set_gap_requests']+=bool(source['all_controls_source_set_gap'])
  for reason,n in source['need_reason_codes'].items():audits['need_reason:'+reason]+=n
  positive_old=[];positive_new=[];current_issues=set();allstrictold=[];allstrictnew=[]
  target_groups=[('TOTAL','all'),('LOCALE',j['locale']),('DOMAIN',row['domain'])]
  for a,g,e in zip(row['grades'],b['grades'],j['entries']):
   identity=(key,e['file'],e['row'],e['variant']);assert identity not in same_grade_ids;same_grade_ids.add(identity)
   assert all(a[k]==g[k]==e[k] for k in ['file','row','variant']);assert a['positive_literal']==g['positive_literal']
   allstrictold.append(g['passed']);allstrictnew.append(a['passed'])
   for group in target_groups:
    c=counts[group];c['grades']+=1;c['old_strict_pass']+=g['passed'];c['new_strict_pass']+=a['passed']
    c['positive_grades']+=a['positive_literal']
    if a['positive_literal']:
     c['old_positive_pass']+=g['literal_passed'];c['new_positive_pass']+=a['literal_passed']
     c['both_positive_pass']+=g['literal_passed'] and a['literal_passed'];c['old_only_positive_pass']+=g['literal_passed'] and not a['literal_passed'];c['new_only_positive_pass']+=a['literal_passed'] and not g['literal_passed'];c['both_positive_fail']+=not a['literal_passed'] and not g['literal_passed']
   if a['positive_literal']:positive_old.append(g['literal_passed']);positive_new.append(a['literal_passed'])
   for category in a['partitions']:issues[category]+=1;current_issues.add(category)
   grade_file.write(json.dumps({'key':key,'grade_identity':identity[1:],'old':g,'new':a},ensure_ascii=False)+'\n')
  for group in target_groups:
   c=counts[group];c['requests']+=1;c['positive_requests']+=bool(positive_new)
   c['old_positive_requests_pass']+=bool(positive_old) and all(positive_old);c['new_positive_requests_pass']+=bool(positive_new) and all(positive_new)
   c['old_all_strict_requests_pass']+=all(allstrictold);c['new_all_strict_requests_pass']+=all(allstrictnew)
   c['http_ok']+=200<=row['http_status']<300;c['validation_ok']+=row['response'].get('validation_ok') is True
  isreg=bool(positive_new) and all(positive_old) and not all(positive_new);isgain=bool(positive_new) and not all(positive_old) and all(positive_new)
  if isreg:regressions.append(key)
  if isgain:improvements.append(key)
  review={'key':key,'question':j['question'],'locale':j['locale'],'domain':row['domain'],'old_positive_all':bool(positive_old) and all(positive_old),
      'new_positive_all':bool(positive_new) and all(positive_new),'positive_contracts':len(positive_new),'old_positive_pass':sum(positive_old),'new_positive_pass':sum(positive_new),
      'failure_groups':sorted(current_issues),'source_review':source,'actual_http_response':row['response'].get('answer',''),'old_saved_answer':b['result'].get('answer','')}
  audit_file.write(json.dumps(review,ensure_ascii=False)+'\n')
  if any(not g['passed'] for g in row['grades']) or source['internal_metadata_visible'] or source['all_controls_source_set_gap'] or source['unrecognized_source_refs'] or source['service_instead_of_explicit_zone_source_paths']:failure_rows.append((row,review))
 audit_file.close();grade_file.close();assert seen==set(jobs) and len(same_grade_ids)==5643
 # A domain containing only negative contracts has a real zero positive denominator.
 # Emit explicit zeros so it remains in the report as N/A, never as omitted coverage.
 for c in counts.values():
  for k in ['old_positive_pass','new_positive_pass','positive_grades','old_positive_requests_pass','new_positive_requests_pass','positive_requests']:
   c.setdefault(k,0)
 domain_rows=[{**allocation[d],**dict(counts[('DOMAIN',d)])} for d in sorted(allocation)]
 assert all(x['requests']==x['selected'] for x in domain_rows)
 transport=collections.Counter();raw_model=[]
 for e in lines(RUN/'MODEL_TRANSPORT.jsonl'):
  transport['attempts']+=1;transport['transport_ok']+=e['transport_ok'];transport['transport_failure']+=not e['transport_ok'];transport['endpoint:'+e['url'].rsplit('/',1)[-1]]+=1
  if not e['transport_ok']:raw_model.append(e)
 model_events={e['id']:e for e in lines(RUN/'MODEL_EVENTS.jsonl')};model_schema=collections.Counter()
 for e in model_events.values():
  model_schema['domain_selector_events']+=1;model_schema['transport_ok']+=e['transport_ok'];model_schema['schema_ok']+=e['schema_ok'];model_schema['identity_verified']+=bool(e.get('identity_verified'))
 total=dict(counts[('TOTAL','all')]);loc={l:dict(counts[('LOCALE',l)]) for l in ['th','en','auto']}
 delta=100*(total['new_positive_pass']-total['old_positive_pass'])/total['positive_grades']
 result={'complete':True,'population':20554,'sample_requests':2108,'sample_grades':5643,'new_questions':0,'sample_domains':104,'totals':total,
  'by_requested_locale':loc,'by_original_domain':domain_rows,'strict_failure_groups_grade_events':dict(issues),'source_audits':dict(audits),
  'model_transport':dict(transport),'domain_selector_schema':dict(model_schema),'model_transport_failures':raw_model,
  'positive_request_regressions_vs_saved_legacy':regressions,'positive_request_improvements_vs_saved_legacy':improvements,
  'latency':{'median_sec':statistics.median(durations),'p95_sec':sorted(durations)[int(len(durations)*.95)],'max_sec':max(durations)},
  'positive_literal_delta_percentage_points':delta,'semantic_accuracy_claimed':False,'source_versions_differ':True,'original_logs_unchanged':done['original_sources_and_results_unchanged']}
 (out/'COMPARISON.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8')
 report=['# R116 — 10% ของแต่ละหมวดใน Full เดิม เทียบ Legacy กับ R115','',
  'ใช้คำถามจากชุด Full เดิม R64 ที่เคยทดสอบจริง ครบ 2,108 request keys (5,643 oracle rows) จากประชากร 20,554 คำขอ สุ่มตาม seed โดยหมวดเดิม 104 กลุ่มได้ ceil(10% × จำนวนกลุ่ม) ทุกกลุ่ม ไม่เลือกจากผลผ่าน/ไม่ผ่าน ไม่สร้างคำถามแทนชุด Full',
  '', '## สรุปคะแนนบนคำถามและเกณฑ์เดียวกัน','', '| เกณฑ์ | Legacy R64 ผลที่เก็บไว้ | R115 ผ่าน API จริง LLM ON |','|---|---:|---:|',
  f"| Positive literal/clause grades | {ratio(total['old_positive_pass'],total['positive_grades'])} | {ratio(total['new_positive_pass'],total['positive_grades'])} |",
  f"| คำขอที่ผ่าน positive ทุกแถวที่ผูกไว้ | {ratio(total['old_positive_requests_pass'],total['positive_requests'])} | {ratio(total['new_positive_requests_pass'],total['positive_requests'])} |",
  f"| Strict รวม route/mode/status/evidence/เวลา | {ratio(total['old_strict_pass'],total['grades'])} | {ratio(total['new_strict_pass'],total['grades'])} |",'',
  'Strict เป็น compatibility ตาม Flow เดิม ไม่ใช่คะแนนเนื้อหาล้วน ส่วน positive literal/clause เป็นคำ/ข้อความที่ oracle กำหนด ไม่ใช่ semantic accuracy จากมนุษย์ คำตอบที่ไม่ตรงคำอาจถูกความหมาย และการผ่านคำไม่รับรองว่าตอบครบทั้งเรื่อง',
  '',f"**ผลบน benchmark นี้:** R115 {'ยังต่ำกว่า' if delta<0 else 'สูงกว่าหรือเท่ากับ'} Legacy ใน positive literal/clause {abs(delta):.2f} จุดเปอร์เซ็นต์บนเกณฑ์ชุดเดียวกัน ความต่างจึงไม่ได้มีแค่ชื่อ route แต่ยังต้องแยก literal/ภาษา/source-version gaps ออกจาก actual content failure รายกรณี",
  '', 'คะแนน 96.46% ใน R115 รอบก่อนเป็น source identity/value/state ของ 960 ข้อที่มี source ในชุดรายหมวด 1,400 ข้อ ไม่ใช่ metric หรือประชากรเดียวกับ Full sample รอบนี้ จึงใช้ตัวเลขนั้นแทนความสามารถบน Full เดิมไม่ได้ แม้ candidate code จะเป็นรุ่นเดียวกัน',
  '', '## ภาษา requested — cohort คงที่','', '| ภาษา | คำขอ | Legacy positive grades | R115 positive grades |','|---|---:|---:|---:|']
 for l,c in loc.items():report.append(f"| {l} | {c['requests']} | {ratio(c['old_positive_pass'],c['positive_grades'])} | {ratio(c['new_positive_pass'],c['positive_grades'])} |")
 report+=['','## Sampling และข้อจำกัดการเปรียบเทียบ','',
  '- ดึงจาก R88 SELECTED_JOBS ซึ่งตรวจแล้วว่าข้อความ/locale/reference_date/entries ตรงกับ R64 JOBS ทุก key ก่อนสุ่ม หมวดใช้ชื่อดั้งเดิม r70_stratum.domain รวม compound/noise/unclassified ไม่ย้ายชื่อหมวดให้คะแนนดูดี',
  '- จำนวนเกิน 2,055 เล็กน้อยเพราะปัดขึ้นทุกหมวดเล็ก ไม่อ้างว่าเป็น 10.000% หรือผล Full ครบ 20,554 และไม่อ้าง blind holdout เพราะเป็น corpus ที่เคยใช้พัฒนาในโครงการ',
  '- เป็น Full เดิมที่เคยใช้ทดสอบจริง แต่ตัวคลังรวมคำถามที่สร้าง/แปลง/ทำคำสะกดผิดสำหรับทดสอบ และบาง oracle มี review_status เป็น candidate ไม่ได้หมายความว่าทุกข้อเป็นคำถามลูกค้าจริงหรือเจ้าของตรวจยืนยันทุก expected แล้ว',
  '- กระจาย locale ภายในแต่ละหมวดตามสัดส่วนด้วย largest remainder; ข้อความ/การสะกดผิด/เกณฑ์ทุกแถวคงเดิม เก็บ SAMPLE_ALLOCATION.json และ SELECTED_JOBS.jsonl',
  '- Legacy อ่านผลจริงเดิมจาก evidence.sqlite แบบ read-only ไม่รัน Flow เดิมใหม่ ตรวจ definition positive กับผล R89 ครบทั้ง sample และ native strict บน saved output ตรงคะแนนเก่าก่อนเริ่มใหม่',
  '- R115 ใช้ source รุ่นใหม่ จึงเปรียบเทียบผลการตอบภายใต้คนละ source/runtime ได้ แต่ความต่างไม่ใช่ causal effect ของ Flow ล้วน ๆ วันที่ปกติของรอบนี้ 2026-10-21; job ที่ระบุวันอ้างอิงเดิมเก็บ override เดิมครบ ส่วน baseline มีวันที่เดิมของรอบเก่า',
  '- รัน serial ผ่าน /api/chat จริง เปิด LLM, session ใหม่ทุก key, ไม่มี category hint ไม่แก้ R115 ระหว่างทดสอบ จับ actual PipelineAnswer ตาม request_id เพื่อไม่เอาการซ่อน private source ใน HTTP มาปนเป็น source failure',
  '- Booking เป็น controlled unavailable เช่น Full เดิม ไม่มีการยืนยัน occupancy ลูกค้าจริง และไม่ใส่ fake live/news data ลง native DB',
  '- จำนวน grades ให้น้ำหนักคำถามที่มีหลาย oracle/หลายคลังมากกว่า จึงแสดงทั้งระดับ grade และระดับ request และไม่ตีความ missing-source/no-answer ว่าตอบเนื้อหาสำเร็จ',
  '', '## หมวดเดิมทุกกลุ่ม — ตรวจ coverage 10%','', '| หมวดเดิม | ประชากร | สุ่ม | สัดส่วน | Legacy positive | R115 positive |','|---|---:|---:|---:|---:|---:|']
 for c in domain_rows:report.append(f"| {c['domain'].replace('|','/')} | {c['population']} | {c['requests']} | {pct(c['requests'],c['population'])} | {ratio(c['old_positive_pass'],c['positive_grades'])} | {ratio(c['new_positive_pass'],c['positive_grades'])} |")
 report+=['','## กลุ่มไม่ผ่าน strict','', '```json',json.dumps(dict(issues),ensure_ascii=False,indent=2),'```','',
  'หนึ่ง grade มีได้หลาย failure group จึงห้ามรวม event counts เป็นจำนวนคำถามผิดจริง Protocol/ชื่อ route/ชื่อ evidence, outcome, literal/complete-clause, validity/source gaps, performance และ grader errors ต้องอ่านแยก',
  '', '## ตรวจ source และ projection เพิ่ม','', '```json',json.dumps(dict(audits),ensure_ascii=False,indent=2),'```','',
  'source refs ที่พบใน snapshot แสดงว่ามีหลักฐานของค่าที่พูด ไม่ได้พิสูจน์ว่าค่านั้นตอบ predicate ของคำถาม ตัวอย่าง service-vs-zone เก็บเส้นทาง game→offer→service→resource→zone ที่มีจริงใน PER_REQUEST_REVIEW และแยกเป็น projection gap ที่ต้องตรวจ ไม่เหมารวมว่าข้อมูลอยู่ผิดโซน',
  'Literal ที่ไม่ผ่านและยังตัดสินความหมายไม่ได้ต้อง review ต่อ ไม่ถือเป็น actual content failure ทั้งหมด รายละเอียดกรณีและคำตอบก่อน/หลังอยู่ CASEBOOK_TH.md',
  '', '## โมเดล การส่งคำขอ และเวลา','', '```json',json.dumps({'observed_model_http':dict(transport),'domain_selector_schema':dict(model_schema),'latency':result['latency']},ensure_ascii=False,indent=2),'```','',
  'Transport success คือได้รับ HTTP response ไม่รับรอง schema หรือเนื้อหาถูก Domain selector schema เป็นเฉพาะ events ที่มีหลักฐานใน artifact ไม่ใช่จำนวน generation สำเร็จทั้งหมด Model identity ตรวจ tag/digest ก่อนและหลังรัน ไฟล์ MODEL_TRANSPORT เก็บ endpoint และข้อผิดพลาดจริง',
  f"- Chat HTTP สำเร็จ {total['http_ok']}/2,108; validation {total['validation_ok']}/2,108; ไม่มีการ retry ซ่อนคำตอบแรก",
  '- เป็น correctness benchmark serial บนเครื่องนี้ ไม่ใช่ load/capacity certification และมี cold-start รวมในรอบ',
  '', '## หลักฐาน','', '- [สรุปสาเหตุที่ตรวจยืนยันและลำดับแก้หลังทดสอบ](ROOT_CAUSE_REVIEW_TH.md)','- [คะแนน JSON](COMPARISON.json)','- [ทุกคำขอ: คำตอบเดิม/ใหม่และ source review](PER_REQUEST_REVIEW.jsonl)',
  '- [ทุก grade คู่เดิม/ใหม่](GRADE_COMPARISON.jsonl.gz)','- [กรณีไม่ผ่านและโจทย์เดิม](CASEBOOK_TH.md)',
  '- [Manifest การเลือก](../SELECTION_MANIFEST.json)','- [ยืนยันจบรอบและ hash](../full01/TEST_COMPLETE.json)',
  '- [Raw HTTP และ PipelineAnswer](../full01/RESULTS.jsonl)',
  '- [กรณีที่ตรวจ source/code ระหว่างรัน](../PRELIMINARY_FINDINGS_TH.md)',
  '', 'R115 ยังเป็น candidate ไม่ติดตั้งทับ R78 ไม่เปลี่ยน source/approvals/oracle/log เก่า และไม่แก้ Flow จากผลระหว่าง benchmark นี้','']
 (out/'REPORT_TH.md').write_text('\n'.join(report),'utf8')
 casebook=['# R116 — ทุกกรณีไม่ผ่าน strict และข้อสังเกต source เพิ่มเติม พร้อมคำตอบเดิม/ใหม่','','ผล literal/strict ไม่ใช่ semantic adjudication; อ่าน REPORT_TH.md ก่อน','']
 for row,v in failure_rows:
  j=jobs[row['key']]
  casebook += [f"## {row['key']} — {row['domain']} / {row['requested_locale']}",'',j['question'],'','### Legacy ที่เก็บไว้','','```text',v['old_saved_answer'],'```','',
      '### R115 API จริง','','```text',v['actual_http_response'],'```','', '### เกณฑ์และ source evidence','','```json',json.dumps({'grades':row['grades'],'source_review':v['source_review']},ensure_ascii=False,indent=2),'```','']
 (out/'CASEBOOK_TH.md').write_text('\n'.join(casebook),'utf8')
 (R/'STATUS.json').write_text(json.dumps({'phase':'complete','complete':True,'requests':2108,'grades':5643,'new_questions':0,'production_installed':False,'report':'analysis/REPORT_TH.md','completed_at':datetime.now().astimezone().isoformat()},ensure_ascii=False,indent=2),'utf8')
 print(json.dumps({'totals':total,'model':dict(transport),'source_audits':dict(audits),'regressions':len(regressions),'improvements':len(improvements),'report':str(out/'REPORT_TH.md')},ensure_ascii=False))
if __name__=='__main__':main()
