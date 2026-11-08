import json,shutil,hashlib
from pathlib import Path
from datetime import datetime,timezone
import r48_probe as r
old=Path((r.OUT/'release_r48_1_path.txt').read_text())
new=r.OUT/'release_r48_2/PSU_Esports_Chatbot_Local';assert not new.exists()
shutil.copytree(old,new,ignore=shutil.ignore_patterns('logs','__pycache__','.git','*.pyc'))
for folder in ('app','web_chat','data/curated','data/rules'):
 shutil.copytree(r.p.ROOT/folder,new/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
source=r.p.ROOT/'data/sources/user_service_answers_20261008.json'
shutil.copy2(source,new/'data/sources'/source.name)
m=json.loads((new/'package_manifest.json').read_text(encoding='utf-8-sig'))
m.update(runtime_version='2026.10.08-user-service-facts-r48.2',parent_runtime_version='2026.10.08-user-service-facts-r48.1',built_at=datetime.now(timezone.utc).isoformat())
(new/'package_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(r.OUT/'release_r48_2_path.txt').write_text(str(new))
with (r.OUT/'release_r48_2_hashes.json').open('x',encoding='utf-8') as f:
 json.dump({p.relative_to(new).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in new.rglob('*') if p.is_file()},f,indent=2)
ps=(r.BASE/'r48_restart.ps1').read_text(encoding='utf-8')
ps=ps.replace("$r48OldRoot=(Get-Content -LiteralPath (Join-Path $r47Out 'release_r47_1_path.txt') -Raw).Trim()","$r48OldRoot=(Get-Content -LiteralPath (Join-Path $r48Out 'release_r48_1_path.txt') -Raw).Trim()")
ps=ps.replace('2026.10.07-answer-content-r47.1','2026.10.08-user-service-facts-r48.1').replace('STOP_OWN_R47_1_PROCESSES','STOP_OWN_R48_1_PROCESSES')
ps=ps.replace("$r48NewRoot=(Get-Content -LiteralPath (Join-Path $r48Out 'release_r48_1_path.txt')","$r48NewRoot=(Get-Content -LiteralPath (Join-Path $r48Out 'release_r48_2_path.txt')")
(r.BASE/'r48_restart_2.ps1').write_text(ps,encoding='utf-8')
audit=(r.BASE/'r48_audit.py').read_text().replace('release_r48_1_path.txt','release_r48_2_path.txt').replace('AUDIT_R48.json','AUDIT_R48_2.json').replace('CHANGE_R48.diff','CHANGE_R48_2.diff').replace('STATUS_R48.txt','STATUS_R48_2.txt').replace('CHECK_R48.txt','CHECK_R48_2.txt')
(r.BASE/'r48_audit_2.py').write_text(audit,encoding='utf-8')
print(new)
