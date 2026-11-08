"""New isolated revision. Preserve every parent source/result and trained weight."""
import ast,hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;OLD=R.parent/'r121_context_planner_training_20261022';S=R/'system'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
assert not S.exists()
parent={str(p.resolve()):sha(p) for p in (OLD/'revision04_system').rglob('*') if p.is_file() and '__pycache__' not in p.parts}
shutil.copytree(OLD/'revision04_system',S,ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.log','*-wal','*-shm'))
for name in ['context_contract.py','evaluation.py','reference_grader.py','retained_literal.py','runtime_profile.py','API_SELECTED_JOBS.jsonl']:
 shutil.copy2(OLD/name,R/name)
x=(OLD/'serve_reader.py').read_text('utf8').replace("R/'revision04_system'","R/'system'")
(R/'serve_candidate.py').write_text(x,'utf8')
x=(OLD/'serve_planner.py').read_text('utf8').replace("RUN=R/'train02'","RUN=R.parent/'r121_context_planner_training_20261022/train02'")
x=x.replace("profile=data['model'];assert profile in profiles", "profile=data['model'];record['requested_profile']=profile\n   if profile not in profiles:\n    record['error']='unsupported_model_profile';self.send(400,{'error':'unsupported_model_profile','supported':list(profiles)});return")
ast.parse(x);(R/'serve_planner.py').write_text(x,'utf8')
x=(OLD/'run_api_comparison02.py').read_text('utf8').replace("OUT=R/'api02'","OUT=R/'api01'").replace("read(R/'train02/TRAINING_COMPLETE.json')","read(R.parent/'r121_context_planner_training_20261022/train02/TRAINING_COMPLETE.json')").replace('serve_frozen.py','serve_candidate.py')
x=x.replace('from evaluation import evaluate,from_http','from evaluation import evaluate,from_http\nfrom runtime_profile import profile_environment')
x=x.replace("log=(A/('SERVER_'", "env.update(profile_environment(profile,MODEL_URL))\n     write(A/('MODEL_ENV_'+str(time.time_ns())+'.json'),{k:env[k] for k in profile_environment(profile,MODEL_URL)})\n     log=(A/('SERVER_'")
x=x.replace("'retained_literal.py']","'retained_literal.py','runtime_profile.py','context_contract.py']")
ast.parse(x);(R/'run_api.py').write_text(x,'utf8')
x=(OLD/'run_reader_execution.py').read_text('utf8').replace("OUT=R/'execution06'","OUT=R/'execution01'")
x=x.replace("R/'train02/TRAINING_COMPLETE.json'","R.parent/'r121_context_planner_training_20261022/train02/TRAINING_COMPLETE.json'")
x=x.replace("'inference05'","'inference01'").replace("R/'inference01/SERVER.json'","R.parent/'r121_context_planner_training_20261022/inference01/SERVER.json'")
x=x.replace('run_reader_probe.py','run_api.py').replace("R/'reader01/TEST_COMPLETE.json'","R/'api01/TEST_COMPLETE.json'").replace('requests_per_arm=3','requests_per_arm=8')
ast.parse(x);(R/'run_execution.py').write_text(x,'utf8')
(R/'PARENT_FREEZE.json').write_text(json.dumps(parent,indent=2),'utf8')
assert all(sha(Path(p))==h for p,h in parent.items())
assert sha(S/'data/knowledge/common.sqlite')==sha(OLD/'revision04_system/data/knowledge/common.sqlite')
(R/'LINEAGE.json').write_text(json.dumps({'parent':'R121 revision04','same_database_sha256':sha(S/'data/knowledge/common.sqlite'),'same_adapter_sha256':sha(OLD/'train02/adapter/adapter_model.safetensors'),'new_training':False,'production_installed':False,'new_questions':0,'comparison':'same revised candidate with base / context-only trained adapter; eight previously inspected development questions, not fresh holdout'},indent=2),'utf8')
print('Isolated source and measurement harness prepared')
