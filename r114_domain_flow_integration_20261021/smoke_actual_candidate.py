"""Small recorded HTTP inspection of the imported candidate, no data writes."""
import json,sys,urllib.request,uuid
from pathlib import Path
R=Path(__file__).resolve().parent;out=R/'verification'/sys.argv[1];out.mkdir(exist_ok=False,parents=True)
with urllib.request.urlopen('http://127.0.0.1:8134/health',timeout=3) as h:health=json.load(h)
assert health.get('common_loaded_build',{}).get('build_id')=='common-r114-domain-flow'
assert health['runtime']['knowledge_draft_preview']
(out/'HEALTH.json').write_text(json.dumps(health,ensure_ascii=False,indent=2),'utf8')
questions=[('วันนี้เปิดไหม','th',None),('ศูนย์อยู่ตึกอะไร ชั้นไหน','th',None),('มีเกมอะไรเล่นบน PS5 บ้าง','th',None),
 ('ราคา VR สำหรับบุคคลภายนอก 2 คน 2 รอบ รวมเท่าไร','th',None),('ราคาเหมา PC Zone สำหรับหน่วยงานภายนอกครึ่งวัน','th',None),
 ('เครดิตเงินโอนเกินหมดอายุกี่วัน','th',None),('Is the studio open today?','auto',None),
 ('ราคา VR สำหรับ General Adult รวม 2 คน 2 รอบ รอบละ 30 นาที','th',None),
 ('ราคา VR สำหรับ General Adult รวม 2 คน 2 รอบ','th','vr-period'),('รอบละ 30 นาที','th','vr-period')]
rows=[]
sessions={}
with (out/'RESULTS.jsonl').open('x',encoding='utf8') as f:
    for q,locale,shared in questions:
        session=sessions.setdefault(shared,'r114-review-'+uuid.uuid4().hex) if shared else 'r114-review-'+uuid.uuid4().hex
        payload={'question':q,'locale':locale,'debug':True,'client_session_id':session,'client_turn_id':uuid.uuid4().hex,'experimental_allow_llm':True}
        req=urllib.request.Request('http://127.0.0.1:8134/api/chat',data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
        with urllib.request.urlopen(req,timeout=45) as h:r=json.load(h)
        row={'question':q,'locale':locale,'response':r};rows.append(row);f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush()
        print(json.dumps({'q':q,'answer':r.get('answer'),'response_type':r.get('decision_artifact',{}).get('response_type')},ensure_ascii=False),flush=True)
(out/'COMPLETE.json').write_text(json.dumps({'completed':len(rows),'expected':len(questions),'actual_candidate_http':True,'read_only_questions':True,
 'published_to_production':False,'semantic_score_claimed':False},indent=2),'utf8')
