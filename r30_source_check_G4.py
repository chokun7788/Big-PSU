import json,re,sys
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(p))
from app.pipeline.competition_presentation import source_clause_lines
from app.knowledge.localization import approved_localization
from app.pipeline.retrieval import load_curated_rows
for row in load_curated_rows():
    id=row.get('id','')
    if row.get('_canonical_projection') or not id.startswith('competition_rules_'):continue
    text=row.get('text','')
    if re.search(r'ไม่อนุญาตให้ลงทะเบียน|เวอร์ชันล่าสุด.*Steam|จำนวนรอบต่อเกม|สกิน Default',text,re.I):
        lines=[l for l in source_clause_lines(text) if re.search(r'ไม่อนุญาตให้ลงทะเบียน|เวอร์ชันล่าสุด.*Steam|จำนวนรอบต่อเกม|สกิน Default',l,re.I)]
        print(json.dumps({'id':id,'clauses_th':lines,'clauses_en':source_clause_lines(approved_localization(row,'text') or '')},ensure_ascii=False)[:2600])
