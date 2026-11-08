import json,shutil
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r52_current_path.txt').read_text())
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
old=OUT/'candidate_r52_2/PSU_Esports_Chatbot_Local';new=OUT/'candidate_r52_3/PSU_Esports_Chatbot_Local'
assert not new.exists()
shutil.copytree(old,new,ignore=shutil.ignore_patterns('logs','state','__pycache__','*.pyc','.git'))
for folder in ('app','web_chat','tests'):
    shutil.copytree(ROOT/folder,new/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
m=json.loads((new/'package_manifest.json').read_text(encoding='utf-8-sig'));m['runtime_version']='2026.10.09-research-flow-r52.3'
(new/'package_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'candidate_r52_3_path.txt').write_text(str(new),encoding='utf-8')
print(new)
