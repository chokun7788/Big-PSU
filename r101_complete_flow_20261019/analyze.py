import collections,gzip,json,sys
from pathlib import Path
R=Path(__file__).resolve().parent;tag=sys.argv[1]
def load(folder):
 rows={}
 for p in folder.glob('RESULTS_*.jsonl.gz'):
  with gzip.open(p,'rt',encoding='utf8') as f:
   for line in f:
    r=json.loads(line);rows[r['key']]=r
 return rows
new=load(R/tag);old=load(R.parent/'r100_contract_flow_implementation_20261019/subset05')
def score(rows):
 c=collections.Counter();locales=collections.defaultdict(collections.Counter)
 for r in rows.values():
  c['requests']+=1;c['exceptions']+=bool(r.get('exception'));c['empty']+=not r.get('result',{}).get('answer')
  for call in r.get('observed_model_http_calls',[]):c['model_attempts']+=1;c['model_transport_ok']+=bool(call.get('transport_ok'))
  for g in r.get('grades',[]):
   c['grades']+=1;c['strict_pass']+=bool(g['passed'])
   for kind,items in g.get('partitions',{}).items():c['failure_'+kind]+=len(items)
   if g.get('positive_text_contract'):
    passed=not bool(g.get('partitions',{}).get('content'));c['positive']+=1;c['positive_pass']+=passed
    locales[r['requested_locale']]['total']+=1;locales[r['requested_locale']]['pass']+=passed
 return {'totals':dict(c),'locales':{k:dict(v) for k,v in locales.items()}}
changes=[];failures=[];transport=[]
for k,r in new.items():
 b=old.get(k,{})
 def grades(r):return {(g['file'],g['row'],g['variant']):g for g in r.get('grades',[]) if g.get('positive_text_contract')}
 bg=grades(b);ng=grades(r);up=[];down=[]
 for key,g in ng.items():
  if key not in bg:continue
  fail=bool(g.get('partitions',{}).get('content'));before=bool(bg[key].get('partitions',{}).get('content'))
  if before and not fail:up.append(key)
  if fail and not before:down.append(key)
 if up or down:changes.append({'question':r['question'],'locale':r['requested_locale'],'improved':len(up),'regressed':len(down),'old_answer':b.get('result',{}).get('answer'),'new_answer':r.get('result',{}).get('answer')})
 if any(g.get('partitions',{}).get('content') for g in r.get('grades',[])):failures.append(r)
 if any(not c.get('transport_ok') for c in r.get('observed_model_http_calls',[])):transport.append({'question':r['question'],'calls':r['observed_model_http_calls'],'context':r.get('result',{}).get('decision_artifact',{}).get('request_context')})
report={'same_key_requests':len(set(new)&set(old)),'baseline_r100_retained':score({k:v for k,v in old.items() if k in new}),'candidate_r101':score(new),'changes':changes,'transport':transport,'scope':'development subset, not full accuracy or independent semantic adjudication'}
(R/tag/'ANALYSIS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8')
(R/tag/'FAILURES.json').write_text(json.dumps(failures,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({k:v for k,v in report.items() if k not in {'changes','transport'}},ensure_ascii=False));print(json.dumps(changes,ensure_ascii=False));print(json.dumps(transport,ensure_ascii=False))
