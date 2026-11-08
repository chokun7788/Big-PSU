import json,collections,sys
from pathlib import Path
W=Path(__file__).parent;P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(P))
R=Path((W/'r34_report_path.txt').read_text().strip());OLD=Path((W/'r33_report_path.txt').read_text().strip());prefix=sys.argv[1] if len(sys.argv)>1 else 'LARGE_REPLAY'
from tools.eval_contract_v2 import rescore_pair
base={}
identity=lambda g:(g['corpus'],g['id'],g['variant'],g['row_index'])
for l in (OLD/'final_H_all_results.jsonl').open(encoding='utf-8'):
 x=json.loads(l);base[x['key']]={identity(g):g['passed'] for g in x['grades']}
counts=collections.Counter();pairs={};new=[];types=collections.Counter();exceptions=[]
with (R/(prefix+'_FAILED.jsonl')).open('x',encoding='utf-8') as f:
 for line in (R/(prefix+'_RESULTS.jsonl')).open(encoding='utf-8'):
  x=json.loads(line);counts['requests']+=1;z=x.get('result',{});failed=False
  if 'exception' in x:exceptions.append(x)
  for g in x['grades']:
   counts['grades']+=1;counts['passed']+=g['passed'];before=base[x['key']][identity(g)]
   counts['improved_grades']+=g['passed'] and not before
   if before and not g['passed']:new.append(dict(question=x['question'],grade=g,result=z));counts['new_failed_grades']+=1
   if not g['passed']:failed=True;types.update(g['failures'])
   if g['corpus']=='master_gt_bilingual_multi_error_2000_20260929_r15.jsonl':
    pair=pairs.setdefault(g['id'],dict(expected=g['expected']));pair[g['variant']]=dict(actual_route=z.get('route',{}).get('category',''),mode=z.get('mode',''),answer=z.get('answer',''),latency_ok=z.get('elapsed',0)<=g['expected'].get('latency_ceiling_sec',20),passed=g['passed'])
  counts['failed_unique']+=failed
  if failed:f.write(json.dumps(x,ensure_ascii=False)+'\n')
overlay={x['id']:x for x in map(json.loads,(P/'data/eval/typo_r16_contract_overlay_20260930.jsonl').read_text(encoding='utf-8').splitlines())};scored=[]
for id,p in pairs.items():
 if {'clean','noisy'}<=set(p):scored.append(rescore_pair(dict(**p['expected'],clean=p['clean'],noisy=p['noisy'],regression=p['clean']['passed'] and not p['noisy']['passed']),overlay.get(id)))
summary=dict(counts=counts,exceptions=len(exceptions),failure_types=types,paired=dict(total=len(scored),clean_passed=sum(x['v2']['clean']['passed'] for x in scored),noisy_passed=sum(x['v2']['noisy']['passed'] for x in scored),regressions=sum(x['v2']['regression'] for x in scored),positive_contracts=sum(x['v2']['noisy']['positive_contract_present'] for x in scored)),scope='Subset replay legacy grades and frozen typo v2 contracts; pass counts are not owner approval or universal answer correctness.')
for name,rows in [('NEW_FAILURES',new),('PAIRED',scored),('EXCEPTIONS',exceptions)]:
 with (R/(prefix+'_'+name+'.jsonl')).open('x',encoding='utf-8') as f:
  for row in rows:f.write(json.dumps(row,ensure_ascii=False)+'\n')
with (R/(prefix+'_SUMMARY.json')).open('x',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
print(json.dumps(summary,ensure_ascii=False),flush=True)
