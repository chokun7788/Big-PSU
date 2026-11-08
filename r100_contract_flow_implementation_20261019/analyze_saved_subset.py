"""Compare same keys to retained R98 without rerunning baseline or changing GT."""
import collections,gzip,hashlib,json,sys
from pathlib import Path
R=Path(__file__).resolve().parent;tag=sys.argv[1]
def load(folder):
 result={}
 for p in folder.glob('RESULTS_*.jsonl.gz'):
  with gzip.open(p,'rt',encoding='utf8') as f:
   for line in f:
    row=json.loads(line);result[row['key']]=row
 return result
new=load(R/tag);keys=set(new);old={k:v for k,v in load(R.parent/'r98_flow_v2_implementation_20261019/subset02').items() if k in keys}
def scores(data):
 total=collections.Counter();locales=collections.defaultdict(collections.Counter);failures=collections.Counter();statuses=collections.Counter()
 for r in data.values():
  total['requests']+=1;total['exceptions']+=bool(r.get('exception'));total['empty_answers']+=not bool(r.get('result',{}).get('answer'))
  for n in r.get('result',{}).get('decision_artifact',{}).get('need_results',[]):statuses[n['status']]+=1
  for c in r.get('observed_model_http_calls',[]):total['model_attempts']+=1;total['model_response_opened']+=bool(c.get('transport_ok'))
  for g in r.get('grades',[]):
   total['grades']+=1;total['strict_passed']+=bool(g['passed'])
   for p,v in g.get('partitions',{}).items():failures[p]+=len(v)
   if g.get('positive_text_contract'):
    passed=not bool(g.get('partitions',{}).get('content'));total['positive_grades']+=1;total['positive_literal_passed']+=passed
    locales[r['requested_locale']]['total']+=1;locales[r['requested_locale']]['passed']+=passed
 return {'totals':dict(total),'locales':{k:dict(v) for k,v in locales.items()},'failure_reasons':dict(failures),'need_status_counts':dict(statuses)}
def grades(row):return {(g['file'],g['row'],g['variant']):g for g in row.get('grades',[])}
changes=[];review=[]
for k,r in new.items():
 if k not in old:continue
 before=grades(old[k]);improved=[];regressed=[]
 for gkey,g in grades(r).items():
  b=before.get(gkey)
  if not b or not g.get('positive_text_contract'):continue
  bfail=bool(b.get('partitions',{}).get('content'));nfail=bool(g.get('partitions',{}).get('content'))
  if bfail and not nfail:improved.append(gkey)
  if nfail and not bfail:regressed.append(gkey)
 if improved or regressed:changes.append({'question':r['question'],'locale':r['requested_locale'],'improved':improved,'regressed':regressed,'old_answer':old[k]['result']['answer'],'new_answer':r['result']['answer'],'artifact':r['result'].get('decision_artifact')})
 fails=[g for g in r.get('grades',[]) if g.get('partitions',{}).get('content')]
 if fails:review.append({'key':k,'question':r['question'],'locale':r['requested_locale'],'answer':r['result']['answer'],'failed_grades':fails,'artifact':r['result'].get('decision_artifact')})
report={'same_key_requests':len(keys&set(old)),'r98_retained':scores(old),'r100_candidate':scores(new),'changes':changes,'limits':['Development regression subset, not untouched holdout or full-corpus accuracy.','Literal/content mismatch is not independent semantic adjudication.','Booking controlled unavailable.','Baseline retained, not rerun.']}
(R/tag/'COMPARISON.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8');(R/tag/'CONTENT_REVIEW.json').write_text(json.dumps(review,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({k:v for k,v in report.items() if k!='changes'},ensure_ascii=False));print(json.dumps([{'question':c['question'],'improved':len(c['improved']),'regressed':len(c['regressed'])} for c in changes],ensure_ascii=False))
