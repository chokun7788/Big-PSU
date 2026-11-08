import json,hashlib,shutil
from pathlib import Path
from datetime import datetime,timezone
import r50_probe as r
oldout=Path((r.BASE/'r49_current_path.txt').read_text());old=Path((oldout/'release_r49_2_path.txt').read_text())
new=r.OUT/'release_r50_1/PSU_Esports_Chatbot_Local';assert not new.exists()
shutil.copytree(old,new,ignore=shutil.ignore_patterns('logs','state','__pycache__','*.pyc','.git'))
for folder in ('app','web_chat','data/curated','data/rules'):
 shutil.copytree(r.old.old.p.ROOT/folder,new/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
m=json.loads((new/'package_manifest.json').read_text(encoding='utf-8-sig'))
m.update(runtime_version='2026.10.09-flow-r50.1',parent_runtime_version='2026.10.09-service-dialogue-r49.2',built_at=datetime.now(timezone.utc).isoformat())
m['local_runtime_features']=list(dict.fromkeys(m['local_runtime_features']+['persistent_acknowledged_dialogue_state','explicit_service_subject_resume','bound_team_member_count_rulebook_route']))
(new/'package_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(r.OUT/'release_r50_1_path.txt').write_text(str(new))
with (r.OUT/'release_r50_1_hashes.json').open('x',encoding='utf-8') as f:json.dump({p.relative_to(new).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in new.rglob('*') if p.is_file()},f,indent=2)
ps=(r.BASE/'r49_restart_2.ps1').read_text()
ps=ps.replace("'release_r49_1_path.txt'","'release_r49_2_path.txt'").replace('2026.10.09-service-dialogue-r49.1','2026.10.09-service-dialogue-r49.2').replace('STOP_OWN_R49_1_PROCESSES','STOP_OWN_R49_2_PROCESSES')
ps=ps.replace("$r48NewRoot=(Get-Content -LiteralPath (Join-Path $r49Out 'release_r49_2_path.txt') -Raw).Trim()","$r50Out=(Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r50_current_path.txt') -Raw).Trim()\n$r48NewRoot=(Get-Content -LiteralPath (Join-Path $r50Out 'release_r50_1_path.txt') -Raw).Trim()")
ps=ps.replace("'STOP_OWN_R49_2_PROCESSES.json'","'STOP_OWN_R49_2_PROCESSES.json'")
ps=ps.replace("(Join-Path (Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r49_current_path.txt') -Raw).Trim() 'STOP_OWN_R49_2_PROCESSES.json')","(Join-Path (Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r50_current_path.txt') -Raw).Trim() 'STOP_OWN_R49_2_PROCESSES.json')")
(r.BASE/'r50_restart.ps1').write_text(ps,encoding='utf-8')
print(new)
