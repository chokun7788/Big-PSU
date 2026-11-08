"""Preserve the installed R78 sources and stage a narrow R81 overlay."""
import hashlib,json,shutil
from pathlib import Path

B=Path(__file__).resolve().parent
T=B/'r81_selector_latency_20261017'
S=B/'r78_web_session_check_20261016/system'
T.mkdir(exist_ok=False)
files=['app/knowledge/common/entity_search.py','app/knowledge/common/answer.py']
manifest={}
for name in files:
    p=S/name;manifest[name]=hashlib.sha256(p.read_bytes()).hexdigest()
    for folder in ('before','candidate'):
        target=T/folder/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,target)
for name in ['app/knowledge/common/open_day.py','data/knowledge/common.sqlite']:
    manifest[name]=hashlib.sha256((S/name).read_bytes()).hexdigest()
(T/'BASELINE_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf8')
print(T)
