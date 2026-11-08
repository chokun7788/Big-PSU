import json,sys,collections,statistics
from pathlib import Path
ROOT=Path(__file__).parent;R=Path((ROOT/'r33_report_path.txt').read_text().strip());OLD=Path((ROOT/'r32_report_path.txt').read_text().strip());P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(P));run=sys.argv[1];tag=sys.argv[2]
from tools.eval_contract_v2 import rescore_pair
def identity(g):return g['corpus'],g['id'],g['variant'],g['row_index']
def signature(x):
 z=x.get('result',{});return z.get('answer'),z.get('mode'),z.get('route',{}).get('category'),z.get('validation',{}).get('ok')
base={}
for line in (OLD/'final13_all_results.jsonl').open(encoding='utf-8'):
 x=json.loads(line);base[x['key']]=dict(signature=signature(x),grades={identity(g):g['passed'] for g in x['grades']})
counts=collections.Counter();new_types=collections.Counter();pairs={};failtypes=collections.Counter();changed=[];newfails=[];seen=set();positive=0;latencies=[];failures=[]
for line in (R/(run+'_all_results.jsonl')).open(encoding='utf-8'):
 try:x=json.loads(line)
 except json.JSONDecodeError:break
 key=x['key'];assert key not in seen;seen.add(key);z=x.get('result',{});before=base[key];actual=signature(x);counts['changed_answers']+=actual!=before['signature'];latencies.append(z.get('elapsed',0));failed=False
 for g in x['grades']:
  counts['grades']+=1;counts['grade_passed']+=g['passed'];previous=before['grades'][identity(g)];counts['grade_improved']+=g['passed'] and not previous
  if not g['passed']:failed=True;failtypes.update(g['failures'])
  if previous and not g['passed']:
   counts['new_failed_grades']+=1;new_types.update(g['failures']);newfails.append(dict(question=x['question'],locale=x['locale'],grade=g,result=z,answer_changed=actual!=before['signature']))
  if g['corpus']=='master_gt_bilingual_multi_error_2000_20260929_r15.jsonl':
   pair=pairs.setdefault(g['id'],dict(expected=g['expected']));pair[g['variant']]=dict(actual_route=z.get('route',{}).get('category',''),mode=z.get('mode',''),answer=z.get('answer',''),latency_ok=z.get('elapsed',0)<=g['expected'].get('latency_ceiling_sec',20),passed=g['passed'])
 counts['failed_unique']+=failed
 if failed:failures.append(x)
 if actual!=before['signature']:changed.append(dict(question=x['question'],locale=x['locale'],previous_signature=before['signature'],new_result=z,grades=x['grades']))
overlay={x['id']:x for x in map(json.loads,(P/'data/eval/typo_r16_contract_overlay_20260930.jsonl').read_text(encoding='utf-8').splitlines())};scored=[]
for id,pair in pairs.items():
 if not {'clean','noisy'}<=set(pair):continue
 scored.append(rescore_pair(dict(**pair['expected'],clean=pair['clean'],noisy=pair['noisy'],regression=pair['clean']['passed'] and not pair['noisy']['passed']),overlay.get(id)))
summary=dict(requests_seen=len(seen),full_expected=len(base),complete=len(seen)==len(base),counts=counts,new_failure_types=new_types,all_failure_types=failtypes,paired=dict(complete_pairs=len(scored),clean_passed=sum(x['v2']['clean']['passed'] for x in scored),noisy_passed=sum(x['v2']['noisy']['passed'] for x in scored),clean_pass_noisy_fail=sum(x['v2']['regression'] for x in scored),positive_contract=sum(x['v2']['noisy']['positive_contract_present'] for x in scored)),scope='Same frozen input contracts and current graders, source-aware cases separate; legacy pass counts are not factual accuracy; real occupancy paused')
for name,rows in [('CHANGED',changed),('NEW_FAILED',newfails),('FAILURES',failures),('PAIRED',scored)]:
 with (R/(tag+'_'+name+'.jsonl')).open('x',encoding='utf-8') as out:
  for x in rows:out.write(json.dumps(x,ensure_ascii=False)+'\n')
with (R/(tag+'_SUMMARY.json')).open('x',encoding='utf-8') as out:json.dump(summary,out,ensure_ascii=False,indent=2)
print(json.dumps(summary,ensure_ascii=False),flush=True)
