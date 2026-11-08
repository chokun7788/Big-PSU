import ast,hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'revision02_system'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
freeze=json.loads((R/'api01/RUN_FREEZE.json').read_text('utf8'));assert all(sha(Path(p))==h for p,h in freeze.items())
shutil.copytree(R/'system',S,ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.log','*-wal','*-shm'))
p=S/'app/knowledge/common/domain_flow/context_guard.py';x=p.read_text('utf8')
x=x.replace("if anaphor and not task.target and not named_targets(index,local):", "if anaphor and task.category in {'C03','C04','C05','C06','C07','C08','C12'} and not task.target and not named_targets(index,local):")
x=x.replace("len(set(durations))>1 and not re.search", "len(set(durations))>1 and task.operation!='compare' and not re.search")
x=x.replace("เปรียบเทียบ|compare|หรือ", "เปรียบเทียบ|compare|different|ต่างจาก|ต่างกัน|หรือ")
ast.parse(x);p.write_text(x,'utf8')
for name,new in [('serve_candidate.py','serve_candidate02.py'),('run_api.py','run_api02.py'),('run_execution.py','run_execution02.py'),('verify_context.py','verify_context02.py'),('prepare_scoped_labels.py','prepare_scoped_labels02.py')]:
 x=(R/name).read_text('utf8').replace("R/'system'","R/'revision02_system'")
 if name=='run_api.py':x=x.replace("OUT=R/'api01'","OUT=R/'api02'").replace('serve_candidate.py','serve_candidate02.py')
 if name=='run_execution.py':
  x=x.replace("OUT=R/'execution01'","OUT=R/'execution02'").replace("'inference01'","'inference02'").replace('run_api.py','run_api02.py').replace("R/'api01/TEST_COMPLETE.json'","R/'api02/TEST_COMPLETE.json'")
 if name=='verify_context.py':x=x.replace('OFFLINE_CONTEXT_VERIFICATION.json','OFFLINE_CONTEXT_VERIFICATION02.json')
 if name=='prepare_scoped_labels.py':x=x.replace("R/'annotation_draft01'","R/'annotation_draft02'")
 ast.parse(x);(R/new).write_text(x,'utf8')
assert all(sha(Path(p))==h for p,h in freeze.items())
(R/'REVISION02_BUILD.json').write_text(json.dumps({'parent_frozen_unchanged':True,'change':'Limit unresolved pronoun clarification to entity-specific domains, preserve implicit studio opening and style phrases; distinguish explicit duration comparison','data_unchanged':sha(S/'data/knowledge/common.sqlite')==sha(R/'system/data/knowledge/common.sqlite'),'production_installed':False},indent=2),'utf8')
print('Revision02 built without modifying prior frozen source')
