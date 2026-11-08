"""Same-key comparison of saved outputs only; no network or new questions."""
import collections,json,statistics,sys
from pathlib import Path
R=Path(__file__).resolve().parent;run=R/(sys.argv[1] if len(sys.argv)>1 else 'http02');OUT=run/'analysis';OUT.mkdir(exist_ok=False)
load=lambda p:json.loads(p.read_text('utf8'))
lines=lambda p:list(map(json.loads,p.open(encoding='utf8')))
done=load(run/'TEST_COMPLETE.json');assert done['complete'] and done['model_identity_verified'] and done['source_code_inputs_unchanged']
versions={
 'Legacy_R64_saved':lines(R/'BASELINE_SCORED_V2.jsonl'),
 'R115_saved':lines(R/'SAVED_R115_RESULTS.jsonl'),
 'R118_revision02_saved':lines(R.parent/'r118_precision_readers_20261021/http02/RESULTS.jsonl'),
 'R119_revision01':lines(R/'http01/RESULTS.jsonl'),
}
if run.name in {'http02','http03'}:versions['R119_revision02']=lines(R/'http02/RESULTS.jsonl')
if run.name=='http03':versions['R119_revision03']=lines(run/'RESULTS.jsonl')
jobs={x['key']:x for x in lines(R/'SELECTED_JOBS.jsonl')};summary={};indexes={};reviews=[]
for name,rows in versions.items():
 assert len(rows)==len({x['key'] for x in rows})==48 and {x['key'] for x in rows}==set(jobs)
 indexes[name]={x['key']:x for x in rows};total=collections.Counter();loc=collections.defaultdict(collections.Counter);reasons=collections.Counter()
 for r in rows:
  key=r['key'];assert r['question']==jobs[key]['question'];positive=[g for g in r['grades'] if g['positive_literal']]
  assert len(r['grades'])==len(jobs[key]['entries'])
  for c in [total,loc[jobs[key]['locale']]]:
   c['requests']+=1;c['grades']+=len(r['grades']);c['strict_pass']+=sum(g['passed'] for g in r['grades'])
   c['positive_grades']+=len(positive);c['positive_pass']+=sum(g['literal_passed'] for g in positive)
   c['positive_requests']+=bool(positive);c['positive_all_pass']+=bool(positive) and all(g['literal_passed'] for g in positive)
  for g in r['grades']:
   for partition,failures in g.get('partitions',{}).items():reasons[partition]+=bool(failures)
 summary[name]={'total':dict(total),'by_locale':{k:dict(c) for k,c in loc.items()},'failure_partitions':dict(reasons)}
latest=list(versions)[-1];old=indexes['R118_revision02_saved'];new=indexes[latest]
def answer(r):return (r.get('response') or r.get('result') or {}).get('answer','')
for key,j in jobs.items():
 r=new[key];a=r['response'].get('decision_artifact') or {};needs=a.get('need_results',[])
 reviews.append({'key':key,'question':j['question'],'locale':j['locale'],'domain':j['r70_stratum']['domain'],
  'answers':{n:answer(ix[key]) for n,ix in indexes.items()},'grades':r['grades'],
  'understanding':a.get('understanding'), 'need_results':needs,'sources':r['response'].get('sources'),
  'source_semantic_review_status':'literal contracts and selected-source identities inspected; broad completeness still requires case review'})
transport=collections.Counter();transport_errors=[]
for e in lines(run/'MODEL_TRANSPORT.jsonl'):
 if '/api/chat' not in e['url'] and '/api/generate' not in e['url']:continue
 transport['attempts']+=1;transport['transport_to_headers_ok']+=e['transport_ok'];transport['transport_failures']+=not e['transport_ok']
 if not e['transport_ok']:transport_errors.append(e)
gains=[];losses=[]
for k in jobs:
 a=[g['literal_passed'] for g in old[k]['grades'] if g['positive_literal']];b=[g['literal_passed'] for g in new[k]['grades'] if g['positive_literal']]
 if a and all(a) and not all(b):losses.append(k)
 if b and all(b) and not all(a):gains.append(k)
result={'versions':summary,'latest':latest,'requests':48,'grades':164,'new_questions':0,'production_installed':False,'semantic_accuracy_claimed':False,
 'development_regression_not_holdout':True,'same_keys_and_grade_population_verified':True,'positive_request_gains_vs_R118':gains,'positive_request_regressions_vs_R118':losses,
 'transport':dict(transport),'transport_errors':transport_errors,'latency':{'median_sec':statistics.median(r['elapsed_sec'] for r in new.values()),'max_sec':max(r['elapsed_sec'] for r in new.values())}}
(OUT/'COMPARISON.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8')
(OUT/'PER_REQUEST_REVIEW.jsonl').write_text(''.join(json.dumps(v,ensure_ascii=False)+'\n' for v in reviews),'utf8')
def ratio(c,k,d):return f"{c.get(k,0)}/{c.get(d,0)} ({100*c.get(k,0)/c[d]:.2f}%)" if c.get(d) else 'N/A'
doc=['# คำถามเดิม 48 ข้อ — คำตอบและหลักฐานรายข้อ','',
 'เป็น development regression ที่เลือกจาก Full เดิม ไม่ใช่ Full ใหม่และใช้คำนวณความถูกต้องทั้งระบบไม่ได้ คะแนน positive ตรวจ literal/clause ตามโจทย์เดิม ส่วน strict รวม protocol และ performance จึงเป็นคนละเกณฑ์กับความถูกต้องเนื้อหา','',
 '| รุ่น | Positive literal/clause | ข้อผ่าน positive ทุกแถว | Strict |','|---|---:|---:|---:|']
for n,c in summary.items():
 t=c['total'];doc.append(f"| {n} | {ratio(t,'positive_pass','positive_grades')} | {ratio(t,'positive_all_pass','positive_requests')} | {ratio(t,'strict_pass','grades')} |")
for v in reviews:
 doc += ['',f"## {v['key']}",'',v['question'],'']
 for n,text in v['answers'].items():doc += [f'### {n}','','```text',text,'```','']
 doc += ['### แผนและหลักฐานที่เลือก','','```json',json.dumps({'understanding':v['understanding'],'need_results':v['need_results'],'grades':v['grades']},ensure_ascii=False,indent=2),'```','']
(OUT/'CASEBOOK_TH.md').write_text('\n'.join(doc),'utf8')
print(json.dumps({'summary':summary,'transport':dict(transport),'gains':len(gains),'regressions':len(losses)},ensure_ascii=False))
