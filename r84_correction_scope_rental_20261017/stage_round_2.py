import hashlib,json,shutil
from pathlib import Path
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system'
manifest=json.loads((B/'BASELINE_MANIFEST.json').read_text(encoding='utf8'))
for name in ['app/knowledge/common/answer.py','app/knowledge/common/query_scope.py','app/knowledge/common/audience_scope.py']:
 for folder in ['before','candidate']:
  p=B/folder/name
  if not p.exists():p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(S/name,p)
 manifest[name]=hashlib.sha256((S/name).read_bytes()).hexdigest()
(B/'BASELINE_MANIFEST_ROUND_2.json').write_text(json.dumps(manifest,indent=2),encoding='utf8')
