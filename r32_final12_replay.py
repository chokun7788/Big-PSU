import json,re,sys,concurrent.futures,time,collections
from pathlib import Path
from r32_full import execute
R=Path(Path(__file__).with_name('r32_report_path.txt').read_text().strip())
def affected(x):
 z=x.get('result',{})
 return bool(re.search(r'(?<![\d.])(?:19|20)\d{2}(?![\d.])',x['question'])) or z.get('mode')=='pipeline:competition_rule_detail_no_answer' or any(t.get('stage')=='competition_detail' and t.get('metadata',{}).get('outcome')=='no_answer' for t in z.get('trace',[]))
def main():
 if sys.argv[1]=='replay':
  jobs=[]
  for line in (R/'final10_all_results.jsonl').open(encoding='utf-8'):
   x=json.loads(line)
   if affected(x):jobs.append(dict(key=x['key'],question=x['question'],locale=x['locale'],reference_date=x.get('reference_date',''),entries=[{k:v for k,v in g.items() if k in ('corpus','row_index','id','variant')}|{'case':g['expected']} for g in x['grades']]))
  with (R/'final12_replay_keys.json').open('x',encoding='utf-8') as f:json.dump([x['key'] for x in jobs],f)
  print(json.dumps({'selected':len(jobs),'scope':'All standalone-year queries and every source-detail no-answer/rejected no-answer trace in C7 results'}),flush=True);start=time.perf_counter()
  with (R/'final12_replay_results.jsonl').open('x',encoding='utf-8') as f,concurrent.futures.ProcessPoolExecutor(max_workers=2) as pool:
   for n,x in enumerate(pool.map(execute,jobs),1):
    f.write(json.dumps(x,ensure_ascii=False)+'\n');f.flush()
    if n%100==0:print(json.dumps({'completed':n,'total':len(jobs),'elapsed':round(time.perf_counter()-start)}),flush=True)
 else:
  replacements={x['key']:x for x in map(json.loads,(R/'final12_replay_results.jsonl').read_text(encoding='utf-8').splitlines())};assert set(replacements)==set(json.loads((R/'final12_replay_keys.json').read_text()))
  counts=collections.defaultdict(collections.Counter);seen=set();changes=[]
  with (R/'final12_all_results.jsonl').open('x',encoding='utf-8') as f:
   for line in (R/'final10_all_results.jsonl').open(encoding='utf-8'):
    old=json.loads(line);key=old['key'];assert key not in seen;seen.add(key);x=replacements.get(key,old)
    if key in replacements:
     x['execution_provenance']='final12_source_detail_abstention_scope_reexecuted'
     if x.get('result',{}).get('answer')!=old.get('result',{}).get('answer'):changes.append(dict(question=x['question'],locale=x['locale'],previous=old.get('result',{}).get('answer'),actual=x.get('result',{}).get('answer'),grades=x['grades']))
    f.write(json.dumps(x,ensure_ascii=False)+'\n')
    for g in x['grades']:counts[g['corpus']]['total']+=1;counts[g['corpus']]['passed']+=g['passed']
  assert len(seen)==20327 and sum(c['total'] for c in counts.values())==55583
  with (R/'final12_all_summary.json').open('x',encoding='utf-8') as f:json.dump(dict(unique_requests=len(seen),case_grades=55583,final12_abstention_replayed=len(replacements),by_corpus=counts,scope='C6 full sweep; C7 all bilingual pairs/competition/game-context replay; final12 every source-detail no-answer trace replay; explicit year corpus absent from old sweep and tested separately through 24 actual HTTP cases. Not a fresh full final12 sweep. Real booking collection paused.'),f,ensure_ascii=False,indent=2)
  with (R/'FINAL9_ABSTENTION_CHANGES.json').open('x',encoding='utf-8') as f:json.dump(changes,f,ensure_ascii=False,indent=2)
  print(json.dumps({'full_inputs':len(seen),'replayed':len(replacements),'answer_changes':len(changes)}),flush=True)
if __name__=='__main__':main()
