"""Preserve tested revision04; tighten native guard receipts in a new copy."""
import ast,hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;P=R/'revision04_system';S=R/'revision05_system'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
freeze={str(p.resolve()):sha(p) for p in P.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc'}
assert not S.exists()
shutil.copytree(P,S,ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.log','*-wal','*-shm'))
(R/'REVISION05_PARENT_FREEZE.json').write_text(json.dumps(freeze,indent=2),'utf8')
p=S/'app/knowledge/common/domain_flow/integration.py';x=p.read_text('utf8')
x=x.replace("from .contracts import Plan\n                    ","")
x=x.replace("art['execution_contract']=aggregate_contract(compiled,outputs)","art['execution_contract']=aggregate_contract(compiled,outputs)\n            art['need_results']=[{**row,'execution_contract':ledger} for row,ledger in zip(art.get('need_results',[]),art['execution_contract']['tasks'])]")
x=x.replace("engine.answer(question,locale,category='C12',at=at,allow_llm=False,budget=budget,understanding=understanding)","engine.answer(question,locale,at=at,allow_llm=False,budget=budget,understanding=understanding)")
needle="result['status']='missing_source';result['needs'][0]['status']='missing_source';result['needs'][0]['reason']='unknown_exact_resource'"
assert needle in x
x=x.replace(needle,needle+"\n            from .native_contract import guard_contract\n            guard_contract(result,compiled,'missing_source','unknown_exact_resource')")
needle="result['status']='unavailable';result['needs'][0]['status']='unavailable';result['needs'][0]['reason']='live_binding_or_provider_not_confirmed'"
assert needle in x
x=x.replace(needle,needle+"\n            from .native_contract import guard_contract\n            guard_contract(result,compiled,'missing_source','live_binding_not_confirmed_no_provider_read')")
ast.parse(x);p.write_text(x,'utf8')
for old,new in [('verify_foundation04.py','verify_foundation05.py'),('verify_packaging04.py','verify_packaging05.py'),('verify_native04b.py','verify_native05.py')]:
 text=(R/old).read_text('utf8').replace('revision04_system','revision05_system');ast.parse(text);(R/new).write_text(text,'utf8')
(R/'REVISION05_BUILD.json').write_text(json.dumps({'parent':str(P),'candidate':str(S),'changes':['native missing-binding/resource guards keep compiled plan and explicit no-provider-read reason','compound need ledgers use whole-question task IDs'],'new_model_calls':0,'production_install':False,'database_sha256':sha(S/'data/knowledge/common.sqlite')},indent=2),'utf8')
print(S)
