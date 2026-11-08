"""Frozen same-source comparison plus automatic routing and reserved questions.

Saved R113 winner rows are read, never re-executed. Each new arm executes the
shared R114 answer implementation independently; no cross-arm answer cache.
"""
import collections,hashlib,importlib.util,json,os,sys,time,traceback,urllib.request
from datetime import datetime
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent/'r113_multi_flow_benchmark_20261021';sys.path.insert(0,str(R/'system'))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.model import MODEL
from app.pipeline.request_deadline import request_deadline
spec=importlib.util.spec_from_file_location('retained_r113_grader',B/'benchmark.py');g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)

def read(p):return json.loads(p.read_text('utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8')
out=R/'verification'/sys.argv[1];out.mkdir(parents=True,exist_ok=False)
def control(name,value):
    raw=json.dumps(value,ensure_ascii=False,indent=2);p=out/name;tmp=p.with_suffix('.control.tmp')
    for attempt in range(7):
        try:tmp.write_text(raw,'utf8');os.replace(tmp,p);return
        except PermissionError:
            if attempt==6:write(out/(p.stem+'_IO_'+str(time.time_ns())+'.json'),value);return
            time.sleep(min(.05*2**attempt,.5))

def main():
    jobs=[json.loads(x) for x in (B/'EFFECTIVE_QUESTIONS_1400.jsonl').read_text('utf8').splitlines()]
    reserved=[json.loads(x) for x in (R/'RESERVED_QUESTIONS_140.jsonl').read_text('utf8').splitlines()]
    assert len(jobs)==1400 and len(reserved)==140
    assert not any('หน่วยโทษ' in x['question'] for x in jobs+reserved)
    files=[*sorted((R/'system/app').rglob('*.py')),R/'system/app/knowledge/common/ui/owner.js',R/'system/data/knowledge/common.sqlite',
      R/'RESERVED_QUESTIONS_140.jsonl',B/'COMMON_READ_MODEL.json',B/'EFFECTIVE_QUESTIONS_1400.jsonl',B/'main_natural/RESULTS.jsonl',B/'WINNER_CANDIDATE_CONFIG.json',Path(__file__)]
    frozen={str(p.resolve()):sha(p) for p in files};write(out/'RUN_FREEZE.json',{'files':frozen,'source_same_as_R113':True,'comparison_baseline':'saved category winner rows; not rerun','model':MODEL,'started_at':datetime.now().astimezone().isoformat()})
    with urllib.request.urlopen('http://127.0.0.1:11434/api/tags',timeout=5) as response:tags=json.load(response)
    digest=next(x['digest'] for x in tags['models'] if x['name']==MODEL);assert digest=='b1f251ef835962b270ba48266d4e32e6f90b29f10930d0712ef5eaabec773a05'
    winners=read(B/'WINNER_CANDIDATE_CONFIG.json')['category_to_flow'];baseline={}
    for line in (B/'main_natural/RESULTS.jsonl').read_text('utf8').splitlines():
        row=json.loads(line)
        if row['flow_id']==winners[row['category']]:baseline[row['question_id']]=row
    assert len(baseline)==1400
    data=read(B/'COMMON_READ_MODEL.json');engine=Engine(data);started=time.monotonic();count=0;seen=set();stats=collections.defaultdict(lambda:collections.defaultdict(collections.Counter))
    total=2940
    with (out/'RESULTS.jsonl').open('x',encoding='utf8') as f,(out/'MODEL_EVENTS.jsonl').open('x',encoding='utf8') as ef:
        for arm,cases,hinted in [('same_source_hinted',jobs,True),('automatic_routing',jobs,False),('reserved_automatic',reserved,False)]:
            for j in cases:
                with request_deadline(30):result=engine.answer(j['question'],j['locale'],category=j['category'] if hinted else None,at=j['reference_time'],allow_llm=True)
                grade=g.grade(j,result);key=(arm,j['id']);assert key not in seen;seen.add(key)
                base=baseline.get(j['id']);bpass=base['grade']['passed'] if base else None
                row={'arm':arm,'question_id':j['id'],'category':j['category'],'question':j['question'],'locale':j['locale'],'stratum':j['stratum'],
                  'fixture':j['fixture'],'result':result,'grade':grade,'saved_baseline_pass':bpass,'saved_baseline_flow':base['flow_id'] if base else None}
                f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush()
                for e in result['model_events']:ef.write(json.dumps({**e,'arm':arm,'question_id':j['id']},ensure_ascii=False)+'\n');ef.flush()
                c=stats[arm][j['category']];c['questions']+=1;c['passed']+=grade['passed'];c['saved_baseline_passed']+=bool(bpass)
                c['improved']+=bpass is False and grade['passed'];c['regressed']+=bpass is True and not grade['passed'];c['model_calls']+=len(result['model_events'])
                c['wrong_scope_or_extra']+=bool(grade['unrequested_claims']);c['missing_claims']+=bool(grade['missing_claims'])
                c['status_only_fail']+=not grade['passed'] and not any(grade[k] for k in ['missing_claims','unrequested_claims','wrong_values','evidence_mismatches'])
                c['routing_exact']+=all(n['category']==j['category'] for n in result['needs'])
                count+=1
                if count%20==0:
                    control('PROGRESS.json',{'completed':count,'total':total,'arm':arm,'category':j['category'],'elapsed_sec':round(time.monotonic()-started,2),
                      'pid':os.getpid(),'running':True,'updated_at':datetime.now().astimezone().isoformat(),'scores':{a:{c:dict(v) for c,v in group.items()} for a,group in stats.items()}})
                if c['questions']==100 or arm=='reserved_automatic' and c['questions']==10:print(json.dumps({'arm':arm,'category':j['category'],**dict(c)},ensure_ascii=False),flush=True)
    assert count==2940 and len(seen)==2940
    assert all(sha(Path(p))==h for p,h in frozen.items())
    with urllib.request.urlopen('http://127.0.0.1:11434/api/tags',timeout=5) as response:tags=json.load(response)
    assert next(x['digest'] for x in tags['models'] if x['name']==MODEL)==digest
    summary={'complete':True,'executions':count,'unique_arm_question_pairs':len(seen),'source_and_code_unchanged':True,'model_identity_verified':True,
      'model_digest':digest,'elapsed_sec':round(time.monotonic()-started,2),'same_source':True,'saved_baseline_executions_rerun':0,
      'scores':{a:{c:dict(v) for c,v in group.items()} for a,group in stats.items()},'scope':'shared domain engine, not full retained 20,554-question HTTP corpus','completed_at':datetime.now().astimezone().isoformat()}
    write(out/'TEST_COMPLETE.json',summary);control('PROGRESS.json',{'completed':count,'total':total,'running':False,'complete':True})

if __name__=='__main__':
    try:main()
    except BaseException as exc:write(out/'FAILED.json',{'error':repr(exc),'traceback':traceback.format_exc(),'pid':os.getpid()});raise
