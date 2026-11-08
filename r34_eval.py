import sys,json,time,collections
from pathlib import Path
import r33_full as runner
W=Path(__file__).parent;R=Path((W/'r34_report_path.txt').read_text().strip())
run=sys.argv[1];fixture=sys.argv[2] if len(sys.argv)>2 else 'R34_FOUR_GROUP_SOURCE_FIXTURE.json'
cases=json.loads((R/fixture).read_text(encoding='utf-8'))['cases'];counts=collections.defaultdict(collections.Counter);start=time.perf_counter()
with (R/(run+'_results.jsonl')).open('x',encoding='utf-8') as out:
 for c in cases:
  x=runner.execute(dict(key=c['id'],question=c['question'],locale=c['locale'],reference_date='',entries=[]));z=x.get('result',{});a=z.get('answer','');errors=[]
  for group in c['required']:
   if not any(w.casefold() in a.casefold() for w in group):errors.append('missing:'+str(group))
  for w in c['forbidden']:
   if w.casefold() in a.casefold():errors.append('forbidden:'+w)
  hits=str(z.get('hits',[]))
  if c.get('source') and not any(w in hits for w in c['source']):errors.append('wrong_source')
  if not z.get('validation',{}).get('ok',False):errors.append('validation_or_exception')
  row=dict(case=c,response=z,exception=x.get('exception'),passed=not errors,failures=errors);out.write(json.dumps(row,ensure_ascii=False)+'\n');out.flush()
  counts[c['group']]['total']+=1;counts[c['group']]['passed']+=not errors
  if errors:print(json.dumps(dict(id=c['id'],errors=errors,question=c['question'],mode=z.get('mode'),answer=a[:300]),ensure_ascii=False),flush=True)
with (R/(run+'_summary.json')).open('x',encoding='utf-8') as f:json.dump(dict(total=len(cases),passed=sum(c['passed'] for c in counts.values()),groups=counts,elapsed=time.perf_counter()-start),f,ensure_ascii=False,indent=2)
print(json.dumps(dict(run=run,groups=counts,elapsed=time.perf_counter()-start),ensure_ascii=False),flush=True)
