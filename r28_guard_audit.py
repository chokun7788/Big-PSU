import re,json,sys,os
from pathlib import Path
from collections import Counter
root=Path(__file__).parent;project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(project))
report=Path((root/'r28_report_path.txt').read_text(encoding='utf-8').strip())
import app.core.keyboard_input_anomaly as module
from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
os.environ['PSU_INPUT_QUALITY_GUARD_MODE']='enforce';os.environ['PSU_INPUT_QUALITY_REPEAT_POLICY']='warn_and_continue'
new_prior=module.GENERIC_ENGLISH_WORDS
old_text=(report/'before/app__core__keyboard_input_anomaly.py').read_text(encoding='utf-8')
old_prior=frozenset(re.search(r'GENERIC_ENGLISH_WORDS = frozenset\(\s*"""(.*?)"""\.split\(\)',old_text,re.S).group(1).split())
module.GENERIC_ENGLISH_WORDS=old_prior;old=RuntimeInputQualityGuard.from_environment()
module.GENERIC_ENGLISH_WORDS=new_prior;new=RuntimeInputQualityGuard.from_environment()
cases=[]
for name in ('competition_user_r24_2000_20261001.jsonl','master_gt_bilingual_multi_error_2000_20260929_r15.jsonl'):
    for r in (json.loads(x) for x in (project/'data/eval'/name).read_text(encoding='utf-8').splitlines() if x.strip()):
        cases.append({'id':r['id'],'question':r.get('question') or r.get('noisy_question') or r.get('input') or r.get('mutated_question'),'corpus':name})
cases+= [dict(c,corpus='r28_composition') for c in json.loads((report/'composition_fixture_v3.json').read_text(encoding='utf-8'))['cases']]
cases+=[{'id':'layout-'+str(i),'question':q,'corpus':'layout_diagnostic'} for i,q in enumerate(('g]jo','l;ylfu','อยากถามว่า g]jo ได้ไหม'))]
records=[]
for c in cases:
    assert c['question'],c
    a=old.inspect(c['question']);b=new.inspect(c['question'])
    records.append({'id':c['id'],'corpus':c['corpus'],'question':c['question'],'before_blocked':a.should_short_circuit,'after_blocked':b.should_short_circuit,'before':a.to_log_dict(),'after':b.to_log_dict()})
summary={'total':len(records),'before_blocked':sum(r['before_blocked'] for r in records),'after_blocked':sum(r['after_blocked'] for r in records),'newly_blocked':sum(not r['before_blocked'] and r['after_blocked'] for r in records),'no_longer_blocked':sum(r['before_blocked'] and not r['after_blocked'] for r in records),'new_profile':new.profile_version,'added_prior_words':sorted(new_prior-old_prior),'scope':'guard-only before/after check; no answer or route correctness grading; old prior with same unchanged detector/threshold; profile labels in before metadata use current hash implementation'}
with (report/'guard_prior_audit.json').open('x',encoding='utf-8') as f:json.dump({'summary':summary,'records':records},f,ensure_ascii=False,indent=2)
print(json.dumps(summary,ensure_ascii=False));print(json.dumps([r for r in records if r['corpus']=='layout_diagnostic' or not r['before_blocked'] and r['after_blocked']],ensure_ascii=False))
