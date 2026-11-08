import json,shutil,hashlib
from pathlib import Path
from datetime import datetime,timezone
import r49_probe as r
old=Path((r.OUT/'release_r49_1_path.txt').read_text())
new=r.OUT/'release_r49_2/PSU_Esports_Chatbot_Local';assert not new.exists()
shutil.copytree(old,new,ignore=shutil.ignore_patterns('logs','__pycache__','.git','*.pyc'))
for folder in ('app','web_chat','data/curated','data/rules'):
 shutil.copytree(r.old.p.ROOT/folder,new/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
m=json.loads((new/'package_manifest.json').read_text(encoding='utf-8-sig'))
m.update(runtime_version='2026.10.09-service-dialogue-r49.2',parent_runtime_version='2026.10.09-service-dialogue-r49.1',built_at=datetime.now(timezone.utc).isoformat())
(new/'package_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(r.OUT/'release_r49_2_path.txt').write_text(str(new))
with (r.OUT/'release_r49_2_hashes.json').open('x',encoding='utf-8') as f:json.dump({p.relative_to(new).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in new.rglob('*') if p.is_file()},f,indent=2)
ps=(r.BASE/'r49_restart.ps1').read_text()
ps=ps.replace("Join-Path $r48Out 'release_r48_2_path.txt'","Join-Path (Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r49_current_path.txt') -Raw).Trim() 'release_r49_1_path.txt'")
ps=ps.replace('2026.10.08-user-service-facts-r48.2','2026.10.09-service-dialogue-r49.1').replace('STOP_OWN_R48_2_PROCESSES','STOP_OWN_R49_1_PROCESSES').replace("Join-Path $r49Out 'release_r49_1_path.txt'","Join-Path $r49Out 'release_r49_2_path.txt'")
(r.BASE/'r49_restart_2.ps1').write_text(ps,encoding='utf-8')
audit=(r.BASE/'r49_audit.py').read_text().replace('release_r49_1_path','release_r49_2_path').replace('AUDIT_R49.json','AUDIT_R49_2.json').replace('CHANGE_R49.diff','CHANGE_R49_2.diff').replace('STATUS_R49.txt','STATUS_R49_2.txt').replace('CHECK_R49.txt','CHECK_R49_2.txt')
(r.BASE/'r49_audit_2.py').write_text(audit,encoding='utf-8')
print(new)
