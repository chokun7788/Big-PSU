import hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;B=R/'r87_common_behavior_bridge_20261017';S=R/'r78_web_session_check_20261016/system';B.mkdir(exist_ok=False)
files=['app/knowledge/common/answer.py','app/knowledge/common/dialogue.py']
baseline={}
for name in files:
 for folder in ['before','candidate']:
  p=B/folder/name;p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(S/name,p)
for name in files+['app/knowledge/common/semantic_profile.py','app/knowledge/common/open_day.py','app/pipeline/migrated_chat.py','app/pipeline/zone_rental.py','app/rules/matcher.py','data/knowledge/common.sqlite']:
 baseline[name]=hashlib.sha256((S/name).read_bytes()).hexdigest()
(B/'BASELINE_MANIFEST.json').write_text(json.dumps(baseline,indent=2),encoding='utf8')
for name in ['run_existing.py','live_candidate.py','web_focused.py']:
 shutil.copy2(R/'r84_correction_scope_rental_20261017'/name,B/name)
print(B)
