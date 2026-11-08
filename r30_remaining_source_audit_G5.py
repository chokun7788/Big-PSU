import json,sys,re,hashlib
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(p));r=Path(Path('r30_report_path.txt').read_text().strip())
from app.pipeline.retrieval import load_curated_rows
from app.pipeline.competition_presentation import source_clause_lines
proof=[]
for row in load_curated_rows():
    id=row.get('id','');text=row.get('text','')
    if not id.startswith('competition_rules_cs2_psu_phuket_2026') or row.get('_canonical_projection'):continue
    lines=[l for l in source_clause_lines(text) if re.search(r'1\s*วัน|สถานที่|ระยะเวลา|PSU Esports Studio',l,re.I)]
    if lines:proof.append({'id':id,'source_url':row.get('source_url'),'clauses':lines,'text_sha256':hashlib.sha256(text.encode()).hexdigest()})
examples=[]
for line in (r/'FINAL_G5_EXTRA_CORPUS_RESULTS.jsonl').open(encoding='utf-8'):
    x=json.loads(line)
    if x['question'] in ['CS2 แข่งกี่วันและแข่งที่ไหน','CS2 แข่งกี่วันแล้วจัดที่ไหน แบบสรุป']:
        examples.append(x)
with (r/'REMAINING_EVENT_DETAILS_G5.json').open('x',encoding='utf-8') as out:json.dump({'source_proof':proof,'actual_cases':examples,'scope':'recorded rulebook event duration and venue; not current event schedule or owner confirmation'},out,ensure_ascii=False,indent=2)
print(json.dumps({'source_proof':proof,'cases':len(examples)},ensure_ascii=False)[:4600])
