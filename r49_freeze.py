import json,shutil,hashlib
from pathlib import Path
from datetime import datetime,timezone
import r49_probe as r
oldout=Path((r.BASE/'r48_current_path.txt').read_text());old=Path((oldout/'release_r48_2_path.txt').read_text())
new=r.OUT/'release_r49_1/PSU_Esports_Chatbot_Local';assert not new.exists()
shutil.copytree(old,new,ignore=shutil.ignore_patterns('logs','__pycache__','.git','*.pyc'))
for folder in ('app','web_chat','data/curated','data/rules'):
 shutil.copytree(r.old.p.ROOT/folder,new/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
m=json.loads((new/'package_manifest.json').read_text(encoding='utf-8-sig'))
m.update(runtime_version='2026.10.09-service-dialogue-r49.1',parent_runtime_version='2026.10.08-user-service-facts-r48.2',built_at=datetime.now(timezone.utc).isoformat())
m['local_runtime_features']=list(dict.fromkeys(m['local_runtime_features']+['bounded_service_noun_typo_recovery','acknowledged_service_fact_context','service_fact_state_without_debug']))
(new/'package_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(r.OUT/'release_r49_1_path.txt').write_text(str(new))
with (r.OUT/'release_r49_1_hashes.json').open('x',encoding='utf-8') as f:json.dump({p.relative_to(new).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in new.rglob('*') if p.is_file()},f,indent=2)
ps=(r.BASE/'r48_restart_2.ps1').read_text()
ps=ps.replace("$r48OldRoot=(Get-Content -LiteralPath (Join-Path $r48Out 'release_r48_1_path.txt')","$r48OldRoot=(Get-Content -LiteralPath (Join-Path $r48Out 'release_r48_2_path.txt')")
ps=ps.replace('2026.10.08-user-service-facts-r48.1','2026.10.08-user-service-facts-r48.2').replace('STOP_OWN_R48_1_PROCESSES','STOP_OWN_R48_2_PROCESSES')
ps=ps.replace("$r48NewRoot=(Get-Content -LiteralPath (Join-Path $r48Out 'release_r48_2_path.txt')","$r49Out=(Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r49_current_path.txt') -Raw).Trim()\n$r48NewRoot=(Get-Content -LiteralPath (Join-Path $r49Out 'release_r49_1_path.txt')")
ps=ps.replace("(Join-Path $r48Out 'STOP_OWN_R48_2_PROCESSES.json')","(Join-Path (Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r49_current_path.txt') -Raw).Trim() 'STOP_OWN_R48_2_PROCESSES.json')")
(r.BASE/'r49_restart.ps1').write_text(ps,encoding='utf-8')
print(new)
