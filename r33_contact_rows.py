import sys,json
from pathlib import Path
sys.path.insert(0,r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
from app.pipeline.retrieval import load_curated_rows,hit_from_curated
for row in load_curated_rows():
 if 'curated_contact_email' in str(row) or 'curated_contact_phone' in str(row):
  print(json.dumps(row,ensure_ascii=False));print(json.dumps(hit_from_curated(row),ensure_ascii=False))
