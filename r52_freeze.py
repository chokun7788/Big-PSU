import json,shutil,hashlib
from pathlib import Path
BASE=Path(__file__).resolve().parent; OUT=Path((BASE/'r52_current_path.txt').read_text())
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
old=BASE/'r50_flow_load_20261009_66d96bb7/release_r50_2/PSU_Esports_Chatbot_Local'
new=OUT/'candidate/PSU_Esports_Chatbot_Local'
assert not new.exists()
shutil.copytree(old,new,ignore=shutil.ignore_patterns('logs','state','__pycache__','*.pyc','.git'))
for folder in ('app','web_chat','tests'):
    shutil.copytree(ROOT/folder,new/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
p=new/'Start-PSU-Esports-Chatbot.ps1'; text=p.read_text(encoding='utf-8-sig')
text=text.replace('$env:PSU_PIPELINE_WORKERS = "1"','$env:PSU_PIPELINE_WORKERS = "2"')
text=text.replace('$env:PSU_PIPELINE_WORKER_WARMUP_LLM = "1"','$env:PSU_PIPELINE_WORKER_WARMUP_LLM = "0"')
text += '\n'
text=text.replace('$env:PSU_PIPELINE_WORKER_SUPERVISOR = "1"','$env:PSU_PIPELINE_WORKER_SUPERVISOR = "1"\n$env:PSU_CHAT_JOBS_ENABLED = "1"\n$env:PSU_LLM_MAX_CONCURRENCY = "1"')
p.write_text(text,encoding='utf-8')
m=json.loads((new/'package_manifest.json').read_text(encoding='utf-8-sig'));m.update(runtime_version='2026.10.09-research-flow-r52.1',parent_runtime_version='2026.10.09-flow-r50.2')
(new/'package_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'candidate_path.txt').write_text(str(new),encoding='utf-8')
print(new)
