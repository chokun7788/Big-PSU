import json,shutil,hashlib
from datetime import datetime,timezone
import r47_probe as r
oldout=r.BASE/'r46_current_path.txt'
old=__import__('pathlib').Path((__import__('pathlib').Path(oldout.read_text())/'release_r46_1_path.txt').read_text())
new=r.OUT/'release_r47_1/PSU_Esports_Chatbot_Local';assert not new.exists()
shutil.copytree(old,new,ignore=shutil.ignore_patterns('logs','__pycache__','.git','*.pyc'))
for folder in ('app','web_chat'):shutil.copytree(r.ROOT/folder,new/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
m=json.loads((new/'package_manifest.json').read_text(encoding='utf-8-sig'))
m.update(runtime_version='2026.10.07-answer-content-r47.1',parent_runtime_version='2026.10.07-english-rental-r46.1',built_at=datetime.now(timezone.utc).isoformat())
m['local_runtime_features']=list(dict.fromkeys(m['local_runtime_features']+['studio_location_source_binding','contact_question_frame_protection']))
(new/'package_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(r.OUT/'release_r47_1_path.txt').write_text(str(new))
with (r.OUT/'release_r47_1_hashes.json').open('x',encoding='utf-8') as f:json.dump({p.relative_to(new).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in new.rglob('*') if p.is_file()},f,indent=2)
print(new)
