"""Read completed append-only evidence; never rerun questions or alter raw logs."""
import collections,gzip,json,sys
from pathlib import Path
B=Path(__file__).resolve().parent.parent;R=B/'r106_complete_flow_20261020'

def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2,default=str),'utf8')
def stream(folder):
 for p in sorted(folder.glob('RESULTS_*.jsonl.gz')):
  with gzip.open(p,'rt',encoding='utf8') as f:
   for line in f:
    if line.strip():yield json.loads(line)

def grades(folder,details=None):
 buckets={};keys=set();exceptions=[];duplicates=[];bykey={}
 sink=gzip.open(details,'wt',encoding='utf8') if details else None
 try:
  for x in stream(folder):
   key=x['key']
   if key in keys:duplicates.append(key)
   keys.add(key)
   loc=x.get('requested_locale','unknown');r=x.get('result') or {};failed=[g for g in x.get('grades',[]) if not g.get('passed')]
   row=buckets.setdefault(loc,{'requests':0,'grades':0,'strict_pass':0,'positive_checks':0,'positive_content_checks_pass':0,'model_calls':0,'model_transport_success':0,'request_exceptions':0,'failure_partitions':collections.Counter()})
   row['requests']+=1;row['request_exceptions']+=bool(x.get('exception'));row['model_calls']+=len(x.get('observed_model_http_calls',[]));row['model_transport_success']+=sum(c.get('transport_ok',False) for c in x.get('observed_model_http_calls',[]))
   if x.get('exception'):exceptions.append({'key':key,'question':x['question'],'exception':x['exception'],'traceback':x.get('traceback')})
   signature=[]
   for g in x.get('grades',[]):
    row['grades']+=1;row['strict_pass']+=bool(g.get('passed'));part=g.get('partitions') or {}
    for cat,values in part.items():row['failure_partitions'][cat]+=bool(values)
    if g.get('positive_text_contract'):
     row['positive_checks']+=1
     row['positive_content_checks_pass']+=not any(part.get(c) for c in ('content','evidence','validation','grader'))
    signature.append({'id':g.get('id'),'file':g.get('file'),'row':g.get('row'),'variant':g.get('variant'),'passed':bool(g.get('passed')),'partitions':part})
   bykey[key]={'locale':loc,'grades':signature}
   if sink and failed:
    art=r.get('decision_artifact') or {}
    sink.write(json.dumps({'key':key,'question':x['question'],'requested_locale':loc,'stratum':x.get('stratum'),'answer':r.get('answer'),'mode':r.get('mode'),'validation':r.get('validation'),'grades':failed,'need_results':art.get('need_results'),'query_plan':art.get('query_plan'),'model_calls':x.get('observed_model_http_calls',[]),'exception':x.get('exception'),'raw_files':str(folder/'RESULTS_*.jsonl.gz')},ensure_ascii=False)+'\n')
 finally:
  if sink:sink.close()
 for row in buckets.values():
  row['strict_percent']=round(row['strict_pass']/max(1,row['grades'])*100,2)
  row['positive_content_check_percent']=round(row['positive_content_checks_pass']/max(1,row['positive_checks'])*100,2)
 return {'by_locale':buckets,'unique_keys':len(keys),'duplicates':duplicates,'request_exceptions':exceptions},bykey,keys

def comparison(now,old):
 changes=[];shared=set(now)&set(old)
 for key in sorted(shared):
  a=now[key];b=old[key]
  def index(x):return {(g['file'],g['row'],g['variant'],g['id']):g for g in x['grades']}
  aa=index(a);bb=index(b)
  for k in set(aa)&set(bb):
   if aa[k]['passed']!=bb[k]['passed']:changes.append({'key':key,'grade':k,'before':bb[k],'after':aa[k]})
 return {'same_request_keys':len(shared),'improved_strict_grades':sum(x['after']['passed'] for x in changes),'regressed_strict_grades':sum(not x['after']['passed'] for x in changes),'changes':changes}

def integrated(tag='integrated04'):
 out=R/'analysis_integrated04';out.mkdir(exist_ok=True)
 batch=json.loads((R/tag/'BATCH_COMPLETE.json').read_text('utf8'));summ=[];lines=['# ผลรวม R106: รอบตรวจ Flow ทุกส่วน','',f"สถานะ {batch['status']} — attempted lanes {batch['lanes_complete']}/{batch['lanes_total']}; source unchanged: {batch['source_unchanged']}",'','จำนวน checks ของแต่ละ lane มีหน่วยต่างกัน จึงไม่รวมเป็นความแม่นยำเดียว','']
 for lane in batch['lanes']:
  p=R/lane['summary_path'];d=json.loads(p.read_text('utf8')) if p.exists() else None
  summ.append({'lane':lane,'summary':d})
  lines+=['## '+lane['lane'],'',f"exit={lane['exit_code']}; checks={lane.get('count')}; passed={lane.get('passed')}; blocked={lane.get('integration_blocked')}",'',f"[log]({(R/tag/(lane['lane']+'.log')).resolve().as_posix()})",'']
  if not d:lines+=['ไม่มี summary: ต้องอ่าน traceback ไม่ตีเป็นคะแนนคำตอบ 0%','']
  elif isinstance(d.get('failed'),list):lines += ['- '+str(x) for x in d['failed']]+['']
 acceptance=R/'verification'/(tag+'_r97_acceptance')/'RESULTS.jsonl';rows=[json.loads(x) for x in acceptance.read_text('utf8').splitlines()]
 failures=[x for x in rows if not x['passed']];dump(out/'ACCEPTANCE_FAILURES.json',failures)
 grouped={}
 for x in rows:
  c=grouped.setdefault(x['scenario'],{'total':0,'passed':0,'by_locale':{}});c['total']+=1;c['passed']+=x['passed'];loc=c['by_locale'].setdefault(x['locale'],{'total':0,'passed':0});loc['total']+=1;loc['passed']+=x['passed']
 dump(out/'SCENARIO_SCORES.json',grouped)
 detail=['# ทุก acceptance variant ที่ไม่ผ่าน','', 'ข้อที่ C07 เปลี่ยน oracle ให้รายงานแยกจากการเทียบ R102; ห้ามอ้างว่าทุกคะแนนที่เพิ่มมาจาก runtime','']
 for x in failures:
  detail += ['## '+x['id'],'','คำถาม: '+x['question'],'','ไม่ผ่าน: '+', '.join(c['assertion'] for c in x['checks'] if not c['passed']),'']
  for t in x.get('turns',[]):
   r=t.get('result') or {};detail+=['```text',r.get('answer') or '(ไม่มีผลลัพธ์)','```','', 'validation: '+json.dumps(r.get('validation'),ensure_ascii=False),'']
 (out/'ACCEPTANCE_FAILURES_TH.md').write_text('\n'.join(detail),'utf8')
 previous=[json.loads(x) for x in (B/'r102_full_flow_plan_20261020/verification/integrated01_r97_acceptance/RESULTS.jsonl').read_text('utf8').splitlines()]
 old={x['id']:x for x in previous};matched=[x for x in rows if x['scenario']!='C07' and x['id'] in old]
 lines+=['## Acceptance','',f"ผ่าน {len(rows)-len(failures)}/{len(rows)} ({100*(len(rows)-len(failures))/max(1,len(rows)):.2f}%)",'',f"เทียบ oracle เดิมยกเว้น C07: R102 {sum(old[x['id']]['passed'] for x in matched)}/{len(matched)}; R106 {sum(x['passed'] for x in matched)}/{len(matched)}",'','| Scenario | ผ่าน/ทั้งหมด |','|---|---|']
 lines += [f"| {k} | {v['passed']}/{v['total']} |" for k,v in grouped.items()]
 for tagname,baseline in [('retained_91',B/'r101_complete_flow_20261019/release_subset09'),('retained_holdout192',None)]:
  score,bykey,_=grades(R/(tag+'_'+tagname),out/(tagname+'_FAILURES.jsonl.gz'));dump(out/(tagname+'_SCORES.json'),score)
  lines+=['','## '+tagname,'','```json',json.dumps(score['by_locale'],ensure_ascii=False,indent=2),'```','']
  if baseline:
   before,bkeys,_=grades(baseline);diff=comparison(bykey,bkeys);dump(out/'VS_R101_SAME_91.json',diff)
   lines += [f"เทียบ R101 คำถามเดิม {diff['same_request_keys']} keys: strict ดีขึ้น {diff['improved_strict_grades']} grades, ถอยลง {diff['regressed_strict_grades']} grades",'']
 lines += ['## วิธีอ่านคะแนน','','- Strict pass รวม route/intent/outcome/text checks; protocol mismatch ไม่ยืนยันว่าเนื้อหาผิด','- Positive content checks เป็น literal/keyword/clauses ตาม oracle เดิม ไม่ใช่ semantic accuracy ที่มนุษย์ตรวจทุกคำตอบ','- Model HTTP สำเร็จยืนยันเพียง transport ไม่ยืนยันว่าตีความถูก','- 192 saved questions เคยอยู่ในคลัง project ไม่ใช่ external unseen holdout','- Live simulated tests ไม่ยืนยันสถานะจริง; real provider blocked ต้องแยกรายงาน','- Candidate ไม่ได้ติดตั้งแทน production; approvals และ real knowledge DB ไม่เปลี่ยน','']
 dump(out/'ANALYSIS.json',{'batch':batch,'lanes':summ,'acceptance':grouped,'failed_variants':len(failures)})
 (out/'REPORT_TH.md').write_text('\n'.join(lines),'utf8')
 return batch

def full(tag='full01'):
 out=R/'full_analysis';out.mkdir(exist_ok=True);jobs=B/'r95_merged_flow_implementation_20261018/FULL_JOBS.jsonl'
 expected={};expected_grades=0
 for line in jobs.read_text('utf8').splitlines():
  j=json.loads(line);expected[j['key']]=len(j['entries']);expected_grades+=len(j['entries'])
 score,bykey,keys=grades(R/tag,out/'ALL_FAILURES.jsonl.gz');actual=sum(v['grades'] for v in score['by_locale'].values())
 progress=json.loads((R/tag/'RUN_FINISHED.json').read_text('utf8'))
 cover={'expected_unique_keys':len(expected),'actual_unique_keys':len(keys),'expected_grades':expected_grades,'actual_grades':actual,'missing_keys':sorted(set(expected)-keys),'unexpected_keys':sorted(keys-set(expected)),'duplicates':score['duplicates'],'grade_count_mismatches':[k for k in keys&set(expected) if len(bykey[k]['grades'])!=expected[k]],'database_unchanged':progress.get('test_database_unchanged')}
 cover['complete']=not any(cover[k] for k in ['missing_keys','unexpected_keys','duplicates','grade_count_mismatches']) and actual==expected_grades and len(keys)==20554 and actual==55811
 dump(out/'COVERAGE.json',cover);dump(out/'SCORES.json',score)
 retained,baseline,_=grades(B/'r95_merged_flow_implementation_20261018/full01');diff=comparison(bykey,baseline);dump(out/'VS_R95_STRICT_CHANGES.json',diff)
 lines=['# Full Test Flow กลาง R106 — LLM ON','',f"Coverage {'ครบ' if cover['complete'] else 'ยังไม่ครบ'}: {len(keys):,}/{len(expected):,} request keys; {actual:,}/{expected_grades:,} grades",'','ทดสอบเฉพาะ common candidate ไม่รัน legacy ระบบจริงไม่ได้ถูกติดตั้งทับ','', '## ผลแยกภาษา','','| ภาษา | Requests | Strict | Positive literal content checks | Model transport |','|---|---:|---:|---:|---:|']
 for loc,v in score['by_locale'].items():lines.append(f"| {loc} | {v['requests']} | {v['strict_pass']}/{v['grades']} ({v['strict_percent']}%) | {v['positive_content_checks_pass']}/{v['positive_checks']} ({v['positive_content_check_percent']}%) | {v['model_transport_success']}/{v['model_calls']} |")
 lines+=['','## ความผิดพลาดและข้อจำกัด','','```json',json.dumps({k:v['failure_partitions'] for k,v in score['by_locale'].items()},ensure_ascii=False,indent=2),'```','',f"Request exceptions: {len(score['request_exceptions'])}",'','Full failed grades, question, full answer, validation, need status, query plan และ transport แยกราย request ใน ALL_FAILURES.jsonl.gz; raw results เก็บ artifact ฉบับเต็ม ไม่ตัดคำตอบเพื่อเปลี่ยนผลตรวจ','',f"เทียบ retained R95 keys เดียวกัน {diff['same_request_keys']:,}: strict ดีขึ้น {diff['improved_strict_grades']:,} grades; ถอยลง {diff['regressed_strict_grades']:,} grades",'','R95 กับ R106 ใช้ข้อมูล migration ต่างรุ่นด้วย จึงไม่ใช่การแยก causal effect ของ Flow อย่างเดียว','', '## วิธีตีความ','','- protocol แยก route/intent ของ format เดิมออกจาก content checks','- keyword/phrase mismatch ต้องอ่านคู่คำตอบและแหล่งข้อมูลก่อนสรุป actual content failure','- validity/source missing ต่างจาก hallucination; unknown ต้องคง unknown','- request exception และ HTTP transport แยกจากคำตอบผิด','- provider ถูกควบคุม unavailable ใน workload นี้; ผล live จริงดู integrated real_live','- การครบ 55,811 grades ไม่ใช่ 55,811 independent questions','- ไม่อ้างแก้ทุกความหมายหรือ production-ready จาก literal grader','']
 (out/'FINAL_REPORT_TH.md').write_text('\n'.join(lines),'utf8')
 dump(out/'ANALYSIS_FINAL.json',{'coverage':cover,'scores':score,'strict_comparison':{k:v for k,v in diff.items() if k!='changes'},'human_semantic_adjudication':False})
 return cover

if __name__=='__main__':
 if sys.argv[1]=='integrated':integrated()
 else:full(sys.argv[2] if len(sys.argv)>2 else 'full01')
