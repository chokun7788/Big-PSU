import json,shutil
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r53_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OLD=OUT/'candidate/PSU_Esports_Chatbot_Local';NEW=OUT/'candidate_r53_2/PSU_Esports_Chatbot_Local';assert not NEW.exists()
shutil.copytree(OLD,NEW,ignore=shutil.ignore_patterns('logs','state','__pycache__','*.pyc','.git'))
for folder in ('app','web_chat','tests','data/general_evidence'):
 shutil.copytree(ROOT/folder,NEW/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
m=json.loads((NEW/'package_manifest.json').read_text(encoding='utf-8-sig'));m['runtime_version']='2026.10.09-semantic-r53.2'
(NEW/'package_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'candidate_r53_2_path.txt').write_text(str(NEW),encoding='utf-8')
s=(OUT/'swap_to_r53_1.ps1').read_text(encoding='utf-8')
s=s.replace('2026.10.09-research-flow-r52.5','2026.10.09-semantic-r53.1')
import re
s=re.sub(r"\$expected='[^']+'",f"$expected='{OLD/'Open-PSU-Esports-Chatbot.ps1'}'".replace('\\','\\\\'),s)
s=s.replace(str(OLD/'Open-PSU-Esports-Chatbot.ps1'),str(NEW/'Open-PSU-Esports-Chatbot.ps1'),1) if False else s
s=re.sub(r"\$launcher='[^']+'",lambda _:f"$launcher='{NEW/'Open-PSU-Esports-Chatbot.ps1'}'",s)
s=s.replace('STOP_OWN_R52_5','STOP_OWN_R53_1').replace('r53_1_start','r53_2_start').replace('Started r53.1','Started r53.2')
(OUT/'swap_to_r53_2.ps1').write_text(s,encoding='utf-8')
print(NEW)
