import json,shutil,hashlib
from pathlib import Path
from datetime import datetime,timezone
import r48_probe as r
out47=Path((r.BASE/'r47_current_path.txt').read_text())
old=Path((out47/'release_r47_1_path.txt').read_text())
new=r.OUT/'release_r48_1/PSU_Esports_Chatbot_Local';assert not new.exists()
shutil.copytree(old,new,ignore=shutil.ignore_patterns('logs','__pycache__','.git','*.pyc'))
for folder in ('app','web_chat','data/curated','data/rules'):
 shutil.copytree(r.p.ROOT/folder,new/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
source=r.p.ROOT/'data/sources/user_service_answers_20261008.json'
(new/'data/sources').mkdir(exist_ok=True)
shutil.copy2(source,new/'data/sources'/source.name)
m=json.loads((new/'package_manifest.json').read_text(encoding='utf-8-sig'))
m.update(runtime_version='2026.10.08-user-service-facts-r48.1',parent_runtime_version='2026.10.07-answer-content-r47.1',built_at=datetime.now(timezone.utc).isoformat())
m['local_runtime_features']=list(dict.fromkeys(m['local_runtime_features']+['user_confirmed_service_facts_th_en','unanswered_policy_boundaries']))
(new/'package_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(r.OUT/'release_r48_1_path.txt').write_text(str(new))
with (r.OUT/'release_r48_1_hashes.json').open('x',encoding='utf-8') as f:
 json.dump({p.relative_to(new).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in new.rglob('*') if p.is_file()},f,indent=2)
ps=(r.BASE/'r47_restart.ps1').read_text(encoding='utf-8')
ps=ps.replace('$r47','$r48').replace('$r46','$r47')
ps=ps.replace('r47_current_path.txt','r48_current_path.txt').replace('r46_current_path.txt','r47_current_path.txt')
ps=ps.replace('release_r46_1_path.txt','release_r47_1_path.txt').replace('release_r47_1_path.txt\') -Raw).Trim()\n&','release_r48_1_path.txt\') -Raw).Trim()\n&')
ps=ps.replace('2026.10.07-english-rental-r46.1','2026.10.07-answer-content-r47.1').replace('STOP_OWN_R46_1_PROCESSES','STOP_OWN_R47_1_PROCESSES')
(r.BASE/'r48_restart.ps1').write_text(ps,encoding='utf-8')
print(new)
