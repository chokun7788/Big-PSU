import hashlib,json,shutil
from pathlib import Path
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system';name='app/pipeline/migrated_chat.py'
manifest=json.loads((B/'BASELINE_MANIFEST.json').read_text(encoding='utf8'))
with (B/'BASELINE_MANIFEST_INITIAL.json').open('x',encoding='utf8') as f:json.dump(manifest,f,indent=2)
manifest[name]=hashlib.sha256((S/name).read_bytes()).hexdigest()
for folder in ('before','candidate'):
 p=B/folder/name;p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(S/name,p)
(B/'BASELINE_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf8')
