import sys,json,time
from pathlib import Path
from r52_web_cases import run,request
from r53_web_cases import semantic_errors
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r53_current_path.txt').read_text())
health=request('/health')[1];assert health['runtime']['version']=='2026.10.09-semantic-r53.2'
cases=[
 ('Translate "Please check your network connection." into Thai.','en','translation'),
 ('Translate "Wait 15 minutes." into Thai.','en','translation'),
 ('Translate "Wait about 15 minutes." into Thai.','en','translation'),
 ('Translate into Thai: "You cannot cancel the booking."','en','translation'),
 ('แปลเป็นไทย: "Use PC1 for 60 minutes."','th','translation'),
 ('Translate "Use PC10 for 15 minutes." into Thai.','en','translation'),
 ('Explain RAM and SSD briefly.','en','general_concise'),
 ('อธิบาย RAM และ SSD แบบสั้น ๆ','th','general_concise'),
 ('Explain what ping can and cannot measure.','en','general_concise'),
 ('ราคา PC บุคคลทั่วไป','th','control'),
 ('What identification should I show when I arrive?','en','control'),
]
rows=[]
for q,l,p in cases:
 r=run(q,l);result=r['job'].get('result') or {}
 errors,meta=semantic_errors(q,result.get('answer',''),p)
 r['quality_probe']={'errors':errors,**meta,'expected_task':p}
 rows.append(r)
 with (OUT/'web_final_r53_2_raw.jsonl').open('a',encoding='utf-8') as s:s.write(json.dumps(r,ensure_ascii=False)+'\n')
with (OUT/'web_final_r53_2.json').open('x',encoding='utf-8') as s:json.dump(rows,s,ensure_ascii=False,indent=2)
print('transport',sum(r['transport_completed'] for r in rows),'model',sum(r['model_answer_delivered'] for r in rows),'of',len(rows))
