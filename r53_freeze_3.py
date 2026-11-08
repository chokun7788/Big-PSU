from pathlib import Path
import shutil,json
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r53_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OLD=OUT/'candidate_r53_2/PSU_Esports_Chatbot_Local';NEW=OUT/'candidate_r53_3/PSU_Esports_Chatbot_Local';assert not NEW.exists()
shutil.copytree(OLD,NEW,ignore=shutil.ignore_patterns('logs','state','__pycache__','*.pyc','.git'))
for folder in ('app','web_chat','tests','data/general_evidence'):
 shutil.copytree(ROOT/folder,NEW/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
m=json.loads((NEW/'package_manifest.json').read_text(encoding='utf-8-sig'));m['runtime_version']='2026.10.09-semantic-r53.3';(NEW/'package_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
s=(OUT/'swap_to_r53_2.ps1').read_text(encoding='utf-8')
s=s.replace('2026.10.09-semantic-r53.1','2026.10.09-semantic-r53.2').replace(str(OUT/'candidate/PSU_Esports_Chatbot_Local'),str(OLD)).replace("$launcher='"+str(OLD),"$launcher='"+str(NEW))
s=s.replace('STOP_OWN_R53_1','STOP_OWN_R53_2').replace('r53_2_start','r53_3_start').replace('Started r53.2','Started r53.3')
(OUT/'swap_to_r53_3.ps1').write_text(s,encoding='utf-8');(OUT/'candidate_r53_3_path.txt').write_text(str(NEW),encoding='utf-8')
print(NEW)
