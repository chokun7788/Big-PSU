import hashlib,json,shutil
from pathlib import Path
B=Path(__file__).resolve().parent;R=B/'r91_common_task_flow_20261018';S=B/'r78_web_session_check_20261016/system'
R.mkdir(exist_ok=False)
manifest={}
for p in (S/'app').rglob('*.py'):
 if 'vendor' not in p.parts:manifest[p.relative_to(S).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
manifest['data/knowledge/common.sqlite']=hashlib.sha256((S/'data/knowledge/common.sqlite').read_bytes()).hexdigest()
for name in ['app/knowledge/common/answer.py','app/knowledge/common/equipment_bridge.py']:
 for folder in ['before','candidate']:
  p=R/folder/name;p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(S/name,p)
(R/'BASELINE_MANIFEST.json').write_text(json.dumps(manifest,indent=2),'utf8')
print(R)
