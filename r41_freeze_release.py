import json,shutil,hashlib,sys
from datetime import datetime,timezone
from pathlib import Path
BASE=Path(__file__).resolve().parent
OUT=Path((BASE/'r41_current_path.txt').read_text(encoding='utf-8'))
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OLD=BASE/'r40_targeted_flow_20261006_022135_9e5ad7/release_r40_3/PSU_Esports_Chatbot_Local'
minor=int(sys.argv[1])
NEW=OUT/f'release_r41_{minor}/PSU_Esports_Chatbot_Local'
assert not NEW.exists(),'Never replace an existing release'
shutil.copytree(OLD,NEW,ignore=shutil.ignore_patterns('logs','__pycache__','.git','*.pyc'))
for folder in ('app','web_chat'):
    shutil.copytree(ROOT/folder,NEW/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
for name in ('Open-PSU-Esports-Background.ps1','Start-PSU-Esports-Chatbot.ps1','README_TH.md','LOCAL_OPERATION_AND_DATA_POLICY_TH.md'):
    shutil.copy2(ROOT/'deployment_templates'/name,NEW/name)
manifest=json.loads((NEW/'package_manifest.json').read_text(encoding='utf-8-sig'))
manifest.update(runtime_version=f'2026.10.06-task-memory-r41.{minor}',built_at=datetime.now(timezone.utc).isoformat(),
    release_scope='Targeted task memory and execution coverage; local-machine candidate. Model weights excluded.',
    parent_runtime_version='2026.10.06-targeted-flow-r40.3')
manifest['local_runtime_features']+=['acknowledged_cross_topic_request_memory','bounded_scope_selectors','per_task_execution_contract']
(NEW/'package_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
hashes={p.relative_to(NEW).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in NEW.rglob('*') if p.is_file()}
with (OUT/f'release_r41_{minor}_hashes.json').open('x',encoding='utf-8') as f:json.dump(hashes,f,indent=2)
with (OUT/f'release_r41_{minor}_path.txt').open('x',encoding='utf-8') as f:f.write(str(NEW))
print(NEW,len(hashes))
