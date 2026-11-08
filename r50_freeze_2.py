import json,shutil,hashlib
from datetime import datetime,timezone
from pathlib import Path
import r50_probe as r
old=Path((r.OUT/'release_r50_1_path.txt').read_text());new=r.OUT/'release_r50_2/PSU_Esports_Chatbot_Local';assert not new.exists()
shutil.copytree(old,new,ignore=shutil.ignore_patterns('logs','state','__pycache__','*.pyc','.git'))
for folder in ('app','web_chat','data/curated','data/rules'):shutil.copytree(r.old.old.p.ROOT/folder,new/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
m=json.loads((new/'package_manifest.json').read_text(encoding='utf-8-sig'));m.update(runtime_version='2026.10.09-flow-r50.2',parent_runtime_version='2026.10.09-flow-r50.1',built_at=datetime.now(timezone.utc).isoformat());(new/'package_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(r.OUT/'release_r50_2_path.txt').write_text(str(new))
with (r.OUT/'release_r50_2_hashes.json').open('x') as stream:json.dump({p.relative_to(new).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in new.rglob('*') if p.is_file()},stream,indent=2)
ps=(r.BASE/'r50_restart.ps1').read_text();lines=ps.splitlines()
lines=["$r48OldRoot=(Get-Content -LiteralPath (Join-Path (Get-Content -LiteralPath (Join-Path $PSScriptRoot 'r50_current_path.txt') -Raw).Trim() 'release_r50_1_path.txt') -Raw).Trim()" if line.startswith('$r48OldRoot=') else line for line in lines]
ps='\n'.join(lines).replace('2026.10.09-service-dialogue-r49.2','2026.10.09-flow-r50.1').replace('STOP_OWN_R49_2_PROCESSES','STOP_OWN_R50_1_PROCESSES').replace("Join-Path $r50Out 'release_r50_1_path.txt'","Join-Path $r50Out 'release_r50_2_path.txt'")
(r.BASE/'r50_restart_2.ps1').write_text(ps+'\n',encoding='utf-8')
print(new)
