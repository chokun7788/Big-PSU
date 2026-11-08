import hashlib,json,shutil
from pathlib import Path
B=Path(__file__).resolve().parent;S=B/'r78_web_session_check_20261016/system';T=B/'r83_selector_topic_repair_20261017';T.mkdir(exist_ok=False)
files=['app/knowledge/common/entity_search.py','app/knowledge/common/answer.py']
manifest={}
for name in files:
    manifest[name]=hashlib.sha256((S/name).read_bytes()).hexdigest()
    for folder in ('before','candidate'):
        p=T/folder/name;p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(S/name,p)
for name in ['app/knowledge/common/semantic_profile.py','app/knowledge/common/open_day.py','data/knowledge/common.sqlite']:
    manifest[name]=hashlib.sha256((S/name).read_bytes()).hexdigest()
(T/'BASELINE_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf8')
print(T)
