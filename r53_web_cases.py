import sys,json,time
from pathlib import Path
from r52_web_cases import run,request
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r53_current_path.txt').read_text())
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(ROOT))
from app.pipeline.semantic_quality import semantic_errors
CASES=[
 ('แปลประโยค Please check your network connection เป็นภาษาไทย','th','translation'),
 ('Translate "Please check your network connection." into Thai.','en','translation'),
 ('Translate "Wait 15 minutes." into Thai.','en','translation'),
 ('Translate "You cannot cancel the booking." into Thai.','en','translation'),
 ('Translate "Use PC1 for 60 minutes." into Thai.','en','translation'),
 ('Translate the Thai sentence กรุณาตรวจสอบการเชื่อมต่ออินเทอร์เน็ต into English.','en','translation'),
 ('Translate "Note: Check your network." into Thai.','en','translation'),
 ('Write a friendly two-sentence invitation to a group study session.','en','two_sentences'),
 ('อธิบายว่า ping ในเครือข่ายคืออะไรแบบสั้นๆ','th','concise_definition'),
 ('Explain what ping can and cannot measure.','en','general_concise'),
 ('Explain HTTP and TLS transport briefly.','en','general_concise'),
 ('อธิบายความแตกต่างระหว่าง RAM กับ SSD พร้อมข้อดีข้อเสีย ขอประมาณ 500 คำ','th','long_explanation'),
 ('Explain DNS, TCP, TLS, HTTP and latency in approximately 500 words.','en','long_explanation'),
 ('Explain latency briefly.','en','general_concise'),
]
if __name__=='__main__':
 label=sys.argv[1];expected=sys.argv[2]
 health=request('/health')[1];assert health['runtime']['version']==expected
 cases=CASES if 'before' not in label else [CASES[i] for i in (0,2,3,7,8,12)]
 rows=[]
 for q,l,p in cases:
  r=run(q,l);result=r['job'].get('result') or {};errors,meta=semantic_errors(q,result.get('answer',''),p)
  r['quality_probe']={'errors':errors,**meta,'expected_task':p,'model_answer_delivered':r['model_answer_delivered'],'all_claims_verified':False}
  rows.append(r)
  with (OUT/(label+'_raw.jsonl')).open('a',encoding='utf-8') as s:s.write(json.dumps(r,ensure_ascii=False)+'\n')
 with (OUT/(label+'.json')).open('x',encoding='utf-8') as s:json.dump(rows,s,ensure_ascii=False,indent=2)
 print('transport',sum(r['transport_completed'] for r in rows),'model answers',sum(r['model_answer_delivered'] for r in rows),'bounded clean',sum(r['model_answer_delivered'] and not r['quality_probe']['errors'] for r in rows),'/',len(rows))
