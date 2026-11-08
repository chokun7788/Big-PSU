import hashlib,json,shutil
from pathlib import Path
B=Path(__file__).resolve().parent/'r84_correction_scope_rental_20261017'
S=B.parent/'r78_web_session_check_20261016/system'
B.mkdir(exist_ok=False)
files=['app/knowledge/common/profile_confirmation.py','app/knowledge/common/question_profiles.py','app/knowledge/common/unconfirmed_request.py','app/knowledge/common/entity_search.py']
manifest={}
for name in files:
 for folder in ['before','candidate']:
  p=B/folder/name;p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(S/name,p)
 manifest[name]=hashlib.sha256((S/name).read_bytes()).hexdigest()
for name in ['data/knowledge/common.sqlite','app/knowledge/common/semantic_profile.py','app/knowledge/common/open_day.py','app/knowledge/common/answer.py','app/pipeline/migrated_chat.py']:
 manifest[name]=hashlib.sha256((S/name).read_bytes()).hexdigest()
(B/'BASELINE_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf8')
for name in ['run_existing.py','live_candidate.py','web_focused.py']:
 shutil.copy2(B.parent/'r83_selector_topic_repair_20261017'/name,B/name)
print(str(B))
