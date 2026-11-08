import json,sys
from pathlib import Path
project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
sys.path.insert(0,str(project))
from app.knowledge.localization import approved_localization
rows=[json.loads(line) for line in (project/'data/competition_rules/competition_rule_chunks.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
for row in rows:
 if row['id'].endswith(('valorant_psu_phuket_2026_s10_c01','valorant_psu_phuket_2026_s14_c01','valorant_psu_phuket_2026_s25_c01','tekken8_psu_esports_s02_c01')):
  print(json.dumps({'id':row['id'],'th':row['text'],'en':approved_localization(row,'text')},ensure_ascii=False),flush=True)
