"""Isolated R121 integration. Never modifies the R120 source tree."""
import hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;OLD=R.parent/'r120_teacher_distillation_20261022';S=R/'system'
assert not S.exists(),'Do not overwrite a candidate'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
before={str(p.resolve()):sha(p) for p in (OLD/'system').rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.pyc','.log'} and not p.name.endswith(('-wal','-shm'))}
shutil.copytree(OLD/'system',S,ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.log','*-wal','*-shm'))
D=S/'app/knowledge/common/domain_flow'
shutil.copy2(R/'context_contract.py',D/'context_contract.py')
p=D/'understanding.py';x=p.read_text('utf8')
x=x.replace('client=EvidenceSelector(model=model,timeout=18)','client=EvidenceSelector(model=model,timeout=90)')
x=x.replace('teaching=demonstrations(question)','teaching=[] # R121: context examples are encoded in the trained adapter.')
x=x.replace("event['response_model']=response.get('model');", "event['model_provenance']=response.get('provenance',{});event['response_model']=response.get('model');")
x=x.replace("result=parse(content,question,audience_ids);event['schema_ok']=result.accepted", "result=parse(content,question,audience_ids);event['schema_ok']=result.accepted\n            if result.accepted:\n                observed=json.loads(content);event['context_focus']=observed['focus'];event['context_quotes']=observed['context_quotes']")
x=x.replace("event['distillation_method']='reviewed_behavior_examples_and_source_contracts_no_weight_update'", "event['distillation_method']='r121_profiled_context_planner_see_model_provenance'")
# Keep the native independent review and reader logic common to both arms.
x+='''

_native_schema=schema
_native_parse=parse
def schema(audience_ids=()):
    from .context_contract import FOCUS
    value=_native_schema(())
    value['properties']['focus']={'type':'string','enum':FOCUS}
    value['properties']['context_quotes']={'type':'array','maxItems':12,'items':{'type':'string'}}
    value['required']=['focus','context_quotes','tasks']
    return value

def parse(content,question,audience_ids=()):
    from .context_contract import validate
    try:value=json.loads(content)
    except (TypeError,ValueError):return Understanding(reason='invalid_context_json')
    valid,reason=validate(value,question)
    if not valid:return Understanding(reason='r121_'+reason)
    return _native_parse(content,question,audience_ids)
'''
p.write_text(x,'utf8')
p=D/'model.py';x=p.read_text('utf8').replace('import json,time,uuid,urllib.request','import json,time,uuid,urllib.request,os')
x=x.replace("MODEL='scb10x/typhoon2.5-qwen3-4b:latest'", "MODEL=os.environ.get('PSU_CHATBOT_OLLAMA_MODEL','scb10x/typhoon2.5-qwen3-4b:latest')")
x=x.replace("'http://127.0.0.1:11434/api/chat'", "os.environ.get('OLLAMA_URL','http://127.0.0.1:11434').rstrip('/')+'/api/chat'")
x=x.replace('model=MODEL,timeout=12','model=MODEL,timeout=60')
x=x.replace("event['response_model']=raw.get('model');", "event['model_provenance']=raw.get('provenance',{});event['response_model']=raw.get('model');")
p.write_text(x,'utf8')
for name in ['serve_frozen.py','evaluation.py','reference_grader.py','retained_literal.py']:shutil.copy2(OLD/name,R/name)
assert all(sha(Path(p))==h for p,h in before.items())
(R/'CANDIDATE_BUILD.json').write_text(json.dumps({'parent':'R120 revision03','production_installed':False,'parent_files_unchanged':True,'parent_files':before,'changes':['context-first contract before native parse','no retrieved teaching examples','dedicated profiled HF transport and provenance','same independent review and source readers','experimental context/selector time budgets 90/60 seconds']},ensure_ascii=False,indent=2),'utf8')
print('Candidate copied and parent verified',len(before))
