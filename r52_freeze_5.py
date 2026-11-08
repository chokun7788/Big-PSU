import json,shutil
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r52_current_path.txt').read_text())
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
old=OUT/'candidate_r52_4/PSU_Esports_Chatbot_Local';new=OUT/'candidate_r52_5/PSU_Esports_Chatbot_Local'
assert not new.exists()
shutil.copytree(old,new,ignore=shutil.ignore_patterns('logs','state','__pycache__','*.pyc','.git'))
for folder in ('app','web_chat','tests'):
    shutil.copytree(ROOT/folder,new/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
m=json.loads((new/'package_manifest.json').read_text(encoding='utf-8-sig'));m['runtime_version']='2026.10.09-research-flow-r52.5'
(new/'package_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'candidate_r52_5_path.txt').write_text(str(new),encoding='utf-8')
# Derive a new checked swap script; leave every previous script/log in place.
s=(BASE/'r52_swap_3_to_4.ps1').read_text(encoding='utf-8')
s=s.replace('r52.3','OLD_VERSION').replace('r52.4','r52.5').replace('OLD_VERSION','r52.4')
s=s.replace('candidate_r52_3','OLD_PATH').replace('candidate_r52_4','candidate_r52_5').replace('OLD_PATH','candidate_r52_4')
s=s.replace('STOP_OWN_R52_3','STOP_OWN_R52_4').replace('r52_4_start','r52_5_start')
(BASE/'r52_swap_4_to_5.ps1').write_text(s,encoding='utf-8')
print(new)
