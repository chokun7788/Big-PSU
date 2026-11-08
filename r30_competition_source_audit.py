import json,re,sys
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r30_report_path.txt').read_text().strip());rows=[]
for line in (p/'data/competition_rules/competition_rule_chunks.jsonl').read_text(encoding='utf-8').splitlines():
    row=json.loads(line);text=row.get('text','')
    if re.search(r'ไม่มีการเปลี่ยนแปลงสมาชิก|Blood|Bodies|ผู้เล่นหลัก|มาสาย|สายเกิน',text,re.I):rows.append(row)
with (r/'competition_extra_source_audit.json').open('x',encoding='utf-8') as f:json.dump(rows,f,ensure_ascii=False,indent=2)
for row in rows:print(json.dumps({k:row.get(k) for k in ['id','game','heading','text']},ensure_ascii=False)[:2000])
examples=json.loads((r/'EXTRA_CORPUS_ANALYSIS.json').read_text(encoding='utf-8'))['examples']
for v in examples.values():
    print(json.dumps({'q':v['question'],'trace':[x for x in v['trace'] if any(k in x['stage'] for k in ['competition','route','intent']) and not x['stage'].startswith('timing:')][-8:]},ensure_ascii=False)[:3500])
