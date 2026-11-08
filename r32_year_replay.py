import json,re,sys,concurrent.futures,time,collections
from pathlib import Path
from r32_full import execute
R=Path(Path(__file__).with_name('r32_report_path.txt').read_text().strip())
def main():
 mode=sys.argv[1]
 if mode=='replay':
  jobs=[]
  for line in (R/'candidate6_all_results.jsonl').open(encoding='utf-8'):
   x=json.loads(line)
   if re.search(r'(?<![\d.])(?:19|20)\d{2}(?![\d.])',x['question']):
    jobs.append(dict(key=x['key'],question=x['question'],locale=x['locale'],reference_date=x.get('reference_date',''),entries=[{k:v for k,v in g.items() if k in ('corpus','row_index','id','variant')}|{'case':g['expected']} for g in x['grades']]))
  with (R/'candidate8_year_replay_keys.json').open('x',encoding='utf-8') as f:json.dump([x['key'] for x in jobs],f)
  print(json.dumps({'selected':len(jobs),'scope':'Every corpus request containing a standalone Gregorian year; includes noncompetition negative controls'}),flush=True)
  start=time.perf_counter()
  with (R/'candidate8_year_replay_results.jsonl').open('x',encoding='utf-8') as f,concurrent.futures.ProcessPoolExecutor(max_workers=2) as pool:
   for n,x in enumerate(pool.map(execute,jobs),1):
    f.write(json.dumps(x,ensure_ascii=False)+'\n');f.flush()
    if n%100==0:print(json.dumps({'completed':n,'total':len(jobs),'elapsed':round(time.perf_counter()-start)}),flush=True)
 else:
  replacements={x['key']:x for x in map(json.loads,(R/'candidate8_year_replay_results.jsonl').read_text(encoding='utf-8').splitlines())}
  assert set(replacements)==set(json.loads((R/'candidate8_year_replay_keys.json').read_text()))
  counts=collections.defaultdict(collections.Counter);seen=set();changed=[]
  with (R/'final8_all_results.jsonl').open('x',encoding='utf-8') as f:
   for line in (R/'final7_all_results.jsonl').open(encoding='utf-8'):
    old=json.loads(line);key=old['key'];assert key not in seen;seen.add(key);x=replacements.get(key,old)
    if key in replacements:
     x['execution_provenance']='candidate8_explicit_year_scope_reexecuted'
     if x.get('result',{}).get('answer')!=old.get('result',{}).get('answer'):changed.append(dict(question=x['question'],locale=x['locale'],previous=old.get('result',{}).get('answer'),actual=x.get('result',{}).get('answer'),grades=x['grades']))
    f.write(json.dumps(x,ensure_ascii=False)+'\n')
    for g in x['grades']:counts[g['corpus']]['total']+=1;counts[g['corpus']]['passed']+=g['passed']
  assert len(seen)==20327 and sum(c['total'] for c in counts.values())==55583
  with (R/'final8_all_summary.json').open('x',encoding='utf-8') as f:json.dump(dict(unique_requests=len(seen),case_grades=55583,candidate8_year_replayed=len(replacements),by_corpus=counts,scope='C6 full sweep, C7 competition/game/all paired replay, C8 all standalone year queries replay; not a fresh full C8 sweep; actual booking collection paused'),f,ensure_ascii=False,indent=2)
  with (R/'C8_YEAR_CHANGES.json').open('x',encoding='utf-8') as f:json.dump(changed,f,ensure_ascii=False,indent=2)
  print(json.dumps({'full_inputs':len(seen),'replayed_years':len(replacements),'year_answer_changes':len(changed)}),flush=True)
if __name__=='__main__':main()
