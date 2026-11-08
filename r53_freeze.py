import json,shutil
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r53_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OLD=Path((BASE/'r52_current_path.txt').read_text())/'candidate_r52_5/PSU_Esports_Chatbot_Local'
NEW=OUT/'candidate/PSU_Esports_Chatbot_Local';assert not NEW.exists()
shutil.copytree(OLD,NEW,ignore=shutil.ignore_patterns('logs','state','__pycache__','*.pyc','.git'))
for folder in ('app','web_chat','tests','data/general_evidence'):
 shutil.copytree(ROOT/folder,NEW/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
m=json.loads((NEW/'package_manifest.json').read_text(encoding='utf-8-sig'));m['runtime_version']='2026.10.09-semantic-r53.1'
(NEW/'package_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'candidate_path.txt').write_text(str(NEW),encoding='utf-8');print(NEW)
old_launcher=str(OLD/'Open-PSU-Esports-Chatbot.ps1');new_launcher=str(NEW/'Open-PSU-Esports-Chatbot.ps1')
script=(BASE/'r52_swap_4_to_5.ps1').read_text(encoding='utf-8')
script=script.replace("$out=Join-Path $PSScriptRoot 'r52_research_flow_20261009_191123'",f"$out='{OUT}'")
script=script.replace("'2026.10.09-research-flow-r52.4'","'2026.10.09-research-flow-r52.5'")
script=script.replace("$expected=Join-Path $out 'candidate_r52_4\\PSU_Esports_Chatbot_Local\\Open-PSU-Esports-Chatbot.ps1'",f"$expected='{old_launcher}'")
script=script.replace("$launcher=Join-Path $out 'candidate_r52_5\\PSU_Esports_Chatbot_Local\\Open-PSU-Esports-Chatbot.ps1'",f"$launcher='{new_launcher}'")
script=script.replace('STOP_OWN_R52_4','STOP_OWN_R52_5').replace('r52_5_start','r53_1_start').replace('Started r52.5','Started r53.1')
(OUT/'swap_to_r53_1.ps1').write_text(script,encoding='utf-8')
