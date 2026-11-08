"""Apply reviewed behavior transfer after preserving the measured baseline."""
import hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';D=S/'app/knowledge/common/domain_flow'
done=json.loads((R/'baseline01/TEST_COMPLETE.json').read_text('utf8'));assert done['complete']
freeze=json.loads((R/'baseline01/RUN_FREEZE.json').read_text('utf8'))['files'];assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in freeze.items())
shutil.copytree(S,R/'baseline01/FROZEN_SYSTEM',ignore=shutil.ignore_patterns('__pycache__','*.pyc','*-wal','*-shm'))
changes=[]
def patch(name,a,b):
 p=D/name;src=p.read_text('utf8');assert src.count(a)==1,(name,a[:80],src.count(a));before=hashlib.sha256(p.read_bytes()).hexdigest();p.write_text(src.replace(a,b),'utf8');changes.append({'path':str(p),'before':before,'after':hashlib.sha256(p.read_bytes()).hexdigest()})
shutil.copy2(R/'staged/distilled_policy.py',D/'distilled_policy.py')
lessons=json.loads((R/'TEACHER_LESSONS.json').read_text('utf8'))
runtime={k:v for k,v in lessons.items() if k!='examples'};runtime['examples']=[{k:e[k] for k in ['id','question','plan','technique']} for e in lessons['examples']]
(D/'teacher_lessons.json').write_text(json.dumps(runtime,ensure_ascii=False,indent=2),'utf8')
patch('understanding.py',"    tasks=[];seen=set();legacy=[]\n","    from .distilled_policy import normalize_tasks\n    raw=normalize_tasks(raw)\n    tasks=[];seen=set();legacy=[]\n")
patch('understanding.py',"    audience_ids=[r['record_id'] for r in directory];contrast=legacy_contrast(question)\n","    audience_ids=[r['record_id'] for r in directory];contrast=legacy_contrast(question)\n    from .distilled_policy import demonstrations\n    teaching=demonstrations(question)\n")
patch('understanding.py',"'independent_legacy_interpretation':contrast}","'independent_legacy_interpretation':contrast,'reviewed_teacher_task_examples':teaching}")
patch('understanding.py',"      'Interpret the WHOLE customer request before routing. Do not answer it. Return JSON tasks only. '","      'Interpret the WHOLE customer request before routing. Do not answer it. Return JSON tasks only. '\n      'Teacher task examples illustrate operations and complete source-quoted needs, not facts. Never reuse their entity, quote, numbers or constraints in a new request. '")
patch('understanding.py',"    result.event=event;result=review(question,index,result)\n","    from .distilled_policy import retain_context\n    result.event=event;result=retain_context(question,result,index);result=review(question,index,result)\n    event['teaching_example_ids']=[e['example_id'] for e in teaching]\n    event['distillation_method']='reviewed_behavior_examples_and_source_contracts_no_weight_update'\n")
patch('meaning_review.py',"    from .precision import equipment\n    if re.search", "    from .precision import equipment\n    from .distilled_policy import requested_frame\n    taught_frame=requested_frame(question,index)\n    if taught_frame is not None:\n        frame=taught_frame;basis='distilled_price_operation_with_current_native_rate_relation'\n    elif re.search")
patch('projection.py',"                cat=next((c for t,c in topics.items() if intent.startswith(t)),None)\n","                cat=next((c for t,c in topics.items() if intent.startswith(t)),None)\n                # Legacy topic and declared query scope are native metadata,\n                # not an inferred fact from an opaque record ID.\n                declared=(value(r,'legacy_search') or {}).get('route_category') or value(r,'topic')\n                if cat is None:cat={'penalty':'C10','rules':'C10','overview':'C01','contact':'C01'}.get(declared)\n")
patch('readers.py',"    fieldq=q\n    for s in sorted({s for f in pool for s in f['subject'].values()},key=len,reverse=True):fieldq=fieldq.replace(norm(s),' ')\n    labels=[]\n", "    from .distilled_policy import broad_rule_family\n    family=broad_rule_family(index,q,pool)\n    if family is not None:return family\n    fieldq=q\n    for s in sorted({s for f in pool for s in f['subject'].values()},key=len,reverse=True):fieldq=fieldq.replace(norm(s),' ')\n    labels=[]\n")
patch('scope.py',"    if not m:return None\n    number=float(m[1]);return number*60 if m[2] in {'ชั่วโมง','hour','hours','hr','hrs'} else number\n", "    if not m:\n        if re.search(r'อย่างน้อย|ไม่เกิน|น้อยกว่า|มากกว่า|\\b(?:at least|less than|more than|up to|under|over)\\b',q):return None\n        words={'one and a half':1.5,'half an':.5,'half a':.5,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'a':1,'an':1}\n        names='|'.join(re.escape(s) for s in sorted(words,key=len,reverse=True))\n        verbal=re.search(r'(?<![a-z])('+names+r')\\s+(hours?|hrs?|minutes?)\\b',q)\n        if not verbal:return None\n        n=words[verbal[1]];return n*60 if verbal[2] in {'hour','hours','hr','hrs'} else n\n    number=float(m[1]);return number*60 if m[2] in {'ชั่วโมง','hour','hours','hr','hrs'} else number\n")
# Keep arithmetic enums in audit metadata, not the customer answer sentence.
patch('engine.py'," ตามกฎ {calc[\"rule\"]}","")
patch('engine.py'," under the declared {calc[\"rule\"]} rule","")
(R/'IMPLEMENTED_CHANGES.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),'utf8')
base=(R/'run_baseline.py').read_text('utf8')
student=base.replace("OUT=R/'baseline01'","OUT=R/'student01'").replace("'run_baseline.py']]","'run_baseline.py','run_student.py']]")
student=student.replace('R120 baseline R119 revision03','R120 distilled student').replace('r120-baseline','r120-student').replace('R120-baseline-R119','R120-distilled-student')
(R/'run_student.py').write_text(student,'utf8')
# Same known development keys, with a separate immutable manifest.
dev=list(map(json.loads,(R/'DEVELOPMENT_JOBS.jsonl').open(encoding='utf8')))
(R/'DEV_MANIFEST.json').write_text(json.dumps({'requests':len(dev),'grades':sum(len(j['entries']) for j in dev),'default_reference_clock':'2026-10-21T12:00:00+07:00'},indent=2),'utf8')
reg=student.replace("OUT=R/'student01'","OUT=R/'regression01'").replace("R/'SELECTED_JOBS.jsonl'","R/'DEVELOPMENT_JOBS.jsonl'").replace("R/'SELECTION_MANIFEST.json'","R/'DEV_MANIFEST.json'")
reg=reg.replace("'SELECTED_JOBS.jsonl','SELECTION_MANIFEST.json'","'DEVELOPMENT_JOBS.jsonl','DEV_MANIFEST.json'").replace("'run_baseline.py','run_student.py']]","'run_baseline.py','run_student.py','run_regression.py']]")
(R/'run_regression.py').write_text(reg,'utf8')
print('Prepared student from',len(runtime['examples']),'reviewed teacher examples; weights and native data unchanged.')
