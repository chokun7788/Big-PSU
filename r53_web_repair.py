import sys,json
from pathlib import Path
from r52_web_cases import run,request
from r53_web_cases import semantic_errors
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r53_current_path.txt').read_text())
assert request('/health')[1]['runtime']['version']=='2026.10.09-semantic-r53.3'
cases=[('Translate "Wait 15 minutes." into Thai.','en'),('Translate "Wait 30 minutes." into Thai.','en'),('Translate "Wait about 15 minutes." into Thai.','en'),('แปลประโยค Wait 15 minutes. เป็นภาษาไทย','th'),('Translate into Thai: "Use PC10 for 60 minutes. You cannot cancel."','en')]
rows=[]
for q,l in cases:
 r=run(q,l);errors,meta=semantic_errors(q,(r['job'].get('result') or {}).get('answer',''),'translation');r['quality_probe']={'errors':errors,**meta};rows.append(r)
 with (OUT/'web_repair_r53_3_raw.jsonl').open('a',encoding='utf-8') as s:s.write(json.dumps(r,ensure_ascii=False)+'\n')
with (OUT/'web_repair_r53_3.json').open('x',encoding='utf-8') as s:json.dump(rows,s,ensure_ascii=False,indent=2)
print('model',sum(r['model_answer_delivered'] for r in rows),'bounded clean',sum(r['model_answer_delivered'] and not r['quality_probe']['errors'] for r in rows),'/',len(rows))
