import hashlib,json,shutil
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r56_current_path.txt').read_text());READY=BASE.parents[1]/'PSU_Esports_Share_R56_20261010';rows=[]
for variant in ('01_Download_Models','02_With_Models'):
 p=READY/variant/'system/PSU_Esports_Chatbot_Local/Start-PSU-Esports-Chatbot.ps1';t=p.read_text(encoding='utf-8-sig');backup=OUT/(variant+'_launcher_before_worker_fix.ps1');shutil.copy2(p,backup)
 assert t.count('$env:PSU_PIPELINE_WORKERS = "2"')==1 and t.count('$env:PSU_PIPELINE_WORKERS = "1"')==1
 t=t.replace('$env:PSU_PIPELINE_WORKERS = "2"\n','',1).replace('$env:PSU_PIPELINE_WORKERS = "1"','$env:PSU_PIPELINE_WORKERS = "2"',1)
 p.write_text(t,encoding='utf-8-sig');rows.append(dict(variant=variant,before_sha256=hashlib.sha256(backup.read_bytes()).hexdigest(),after_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),effective_pipeline_workers=2,root_source_changed=False))
with (OUT/'package_launcher_worker_fix.json').open('x',encoding='utf-8') as f:json.dump(rows,f,indent=2)
print('new package launchers fixed, old R50 intact')
