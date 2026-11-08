import os,sys,json,re,concurrent.futures,time,collections
from pathlib import Path
ROOT=Path(__file__).parent;R=Path((ROOT/'r32_report_path.txt').read_text().strip())
from r32_full import execute
PAIR='master_gt_bilingual_multi_error_2000_20260929_r15.jsonl'
def affected(row):
 if any(g['corpus']==PAIR or 'competition_rules' in (g['expected'].get('expected_route_categories') or []) for g in row['grades']):return True
 if row.get('result',{}).get('route',{}).get('category')=='competition_rules':return True
 if any(t.get('stage')=='intent_cue_preflight' and any('registered facet span' in c.get('reason','') for c in t.get('metadata',{}).get('recoveries',[])) for t in row.get('result',{}).get('trace',[])):return True
 return bool(re.search(r'cs2|counter|เคาน|rov|aov|arena|อารี|tekken|เทค|valorant|วาโล|rulebook|competition|tournament|rulse|rules|กติก|กฎ|กฏ|แข่ง|เวลานอก|protest|roster|หยุดเกม',row['question'],re.I))
def main():
 mode=sys.argv[1]
 if mode=='replay':
  jobs=[]
  for line in (R/'candidate6_all_results.jsonl').open(encoding='utf-8'):
   x=json.loads(line)
   if affected(x):jobs.append(dict(key=x['key'],question=x['question'],locale=x['locale'],reference_date=x.get('reference_date',''),entries=[{k:v for k,v in g.items() if k in ('corpus','row_index','id','variant')}|{'case':g['expected']} for g in x['grades']]))
  with (R/'candidate7_replay_keys.json').open('x',encoding='utf-8') as out:json.dump([j['key'] for j in jobs],out)
  print(json.dumps({'selected':len(jobs),'scope':'all 2000 clean/noisy pairs plus competition and named-game contexts'}),flush=True)
  started=time.perf_counter()
  with (R/'candidate7_replay_results.jsonl').open('x',encoding='utf-8') as out,concurrent.futures.ProcessPoolExecutor(max_workers=4) as pool:
   for n,x in enumerate(pool.map(execute,jobs),1):out.write(json.dumps(x,ensure_ascii=False)+'\n');out.flush();print(json.dumps({'completed':n,'total':len(jobs),'elapsed':round(time.perf_counter()-started)}),flush=True) if n%200==0 else None
 else:
  replacement={x['key']:x for x in map(json.loads,(R/'candidate7_replay_results.jsonl').read_text(encoding='utf-8').splitlines())};assert set(replacement)==set(json.loads((R/'candidate7_replay_keys.json').read_text()));seen=set();counts=collections.defaultdict(collections.Counter)
  with (R/'final7_all_results.jsonl').open('x',encoding='utf-8') as out:
   for line in (R/'candidate6_all_results.jsonl').open(encoding='utf-8'):
    x=json.loads(line);key=x['key'];assert key not in seen;seen.add(key);used=replacement.get(key,x);used['execution_provenance']='candidate7_reexecuted' if key in replacement else 'candidate6_retained_unaffected_by_facet_only_change';out.write(json.dumps(used,ensure_ascii=False)+'\n')
    for g in used['grades']:counts[g['corpus']]['total']+=1;counts[g['corpus']]['passed']+=g['passed']
  assert len(seen)==20327 and sum(x['total'] for x in counts.values())==55583
  summary=dict(unique_requests=len(seen),reexecuted_candidate7=len(replacement),retained_unaffected=len(seen)-len(replacement),case_grades=55583,by_corpus=counts,scope='Full candidate6 sweep, all bilingual pairs and competition/game contexts replayed on candidate7; not a new full candidate7 run; real booking occupancy remains paused')
  with (R/'final7_all_summary.json').open('x',encoding='utf-8') as out:json.dump(summary,out,ensure_ascii=False,indent=2)
  print(json.dumps({k:v for k,v in summary.items() if k!='by_corpus'}),flush=True)
if __name__=='__main__':main()
