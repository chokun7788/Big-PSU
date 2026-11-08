"""Use identical classifier + unchanged overlay on both generations; retain old scores."""
import json,sys,collections
from pathlib import Path
r=Path(Path('r31_report_path.txt').read_text().strip());old=Path(Path('r30_report_path.txt').read_text().strip());p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(p))
from tools.eval_contract_v2 import rescore_pair
overlay={x['id']:x for x in map(json.loads,(p/'data/eval/typo_r16_contract_overlay_20260930.jsonl').read_text(encoding='utf-8').splitlines())};pairs={}
for line in (old/'final_G6_all_results.jsonl').open(encoding='utf-8'):
    row=json.loads(line);z=row['result']
    for g in row['grades']:
        if g['corpus']=='master_gt_bilingual_multi_error_2000_20260929_r15.jsonl':
            pair=pairs.setdefault(g['id'],{'expected':g['expected']});pair[g['variant']]=dict(actual_route=z['route']['category'],mode=z['mode'],answer=z['answer'],latency_ok=z['elapsed']<=g['expected'].get('latency_ceiling_sec',20),passed=g['passed'])
rows={}
with (r/'R30_G6_COMMON_CURRENT_V2.jsonl').open('x',encoding='utf-8') as out:
    for id,pair in pairs.items():
        x=rescore_pair(dict(**pair['expected'],clean=pair['clean'],noisy=pair['noisy'],regression=pair['clean']['passed'] and not pair['noisy']['passed']),overlay.get(id));rows[id]=x;out.write(json.dumps(x,ensure_ascii=False)+'\n')
new={x['id']:x for x in map(json.loads,(r/'R31_C_PAIRED_TYPO_V2.jsonl').read_text(encoding='utf-8').splitlines())};assert set(new)==set(rows)
def summary(records):return dict(pairs=len(records),clean_passed=sum(x['v2']['clean']['passed'] for x in records.values()),noisy_passed=sum(x['v2']['noisy']['passed'] for x in records.values()),clean_pass_noisy_fail=sum(x['v2']['regression'] for x in records.values()))
delta=[]
for id,x in new.items():
    for variant in ['clean','noisy']:
        b=rows[id]['v2'][variant];z=x['v2'][variant]
        if b['passed']!=z['passed']:delta.append(dict(id=id,variant=variant,old_passed=b['passed'],new_passed=z['passed'],old=b,new=z))
data=dict(baseline_G6_current_scoring=summary(rows),r31_C_current_scoring=summary(new),improved=sum(x['new_passed'] for x in delta),new_failed=sum(not x['new_passed'] for x in delta),delta=delta,scope='Identical recognized modes + unchanged frozen overlay. Classifier correction is not behavioral accuracy improvement. Positive content oracle is absent in some rows. Booking occupancy not verified.')
with (r/'R31_COMMON_SCORING_COMPARISON.json').open('x',encoding='utf-8') as out:json.dump(data,out,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in data.items() if k!='delta'},ensure_ascii=False),flush=True)
