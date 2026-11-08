import json,collections
from pathlib import Path
r=Path(Path('r30_report_path.txt').read_text().strip());baseline={};current={};changes=[];counts=collections.Counter()
for run in ['final_G2','final_G3']:
    dest=baseline if run=='final_G2' else current
    for l in (r/(run+'_all_results.jsonl')).open(encoding='utf-8'):
        x=json.loads(l)
        dest[x['key']]={'question':x['question'],'locale':x['locale'],'answer':x.get('result',{}).get('answer',''),'mode':x.get('result',{}).get('mode'),'language':x.get('result',{}).get('language'),'grades':{(g['corpus'],g['id'],g['variant']):g for g in x['grades']}}
assert baseline.keys()==current.keys()
with (r/'FINAL_G2_TO_G3_DIFFERENCES.jsonl').open('x',encoding='utf-8') as out:
    for key,b in baseline.items():
        a=current[key];delta=[]
        for gid,g in a['grades'].items():
            old=b['grades'][gid]
            if old['passed']!=g['passed']:
                counts['newly_passed_case_grades' if g['passed'] else 'newly_failed_case_grades']+=1
                delta.append({'corpus':gid[0],'id':gid[1],'variant':gid[2],'previous_passed':old['passed'],'current_passed':g['passed'],'old_failures':old['failures'],'new_failures':g['failures'],'expected':g['expected']})
        answer_changed=b['answer']!=a['answer'] or b['mode']!=a['mode']
        counts['changed_answer_or_mode_requests']+=answer_changed
        if delta or answer_changed:
            out.write(json.dumps({'key':key,'question':a['question'],'locale':a['locale'],'before':{k:b[k] for k in ('answer','mode','language')},'after':{k:a[k] for k in ('answer','mode','language')},'grade_changes':delta,'scope':'grade changes need content/source review; no combined accuracy'},ensure_ascii=False)+'\n')
counts['unique_requests_compared']=len(current)
with (r/'FINAL_G2_TO_G3_COMPARISON.json').open('x',encoding='utf-8') as f:json.dump(counts,f,ensure_ascii=False,indent=2)
print(json.dumps(counts))
