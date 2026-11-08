import json,shutil,hashlib,sys
from pathlib import Path
from datetime import datetime,timezone
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r46_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OLD=Path((Path((BASE/'r45_current_path.txt').read_text())/'release_r45_2_path.txt').read_text())
minor=sys.argv[1] if len(sys.argv)>1 else '1'
NEW=OUT/f'release_r46_{minor}/PSU_Esports_Chatbot_Local';assert not NEW.exists()
shutil.copytree(OLD,NEW,ignore=shutil.ignore_patterns('logs','__pycache__','.git','*.pyc'))
for folder in ('app','web_chat'):shutil.copytree(ROOT/folder,NEW/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
m=json.loads((NEW/'package_manifest.json').read_text(encoding='utf-8-sig'))
m.update(runtime_version=f'2026.10.07-english-rental-r46.{minor}',parent_runtime_version='2026.10.07-rental-scope-r45.2',built_at=datetime.now(timezone.utc).isoformat())
m['local_runtime_features']+=['rental_child_scopes','rental_negative_filters','rental_context_field_followups']
(NEW/'package_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(OUT/f'release_r46_{minor}_path.txt').write_text(str(NEW))
with (OUT/f'release_r46_{minor}_hashes.json').open('x',encoding='utf-8') as f:json.dump({p.relative_to(NEW).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in NEW.rglob('*') if p.is_file()},f,indent=2)
print(NEW)
