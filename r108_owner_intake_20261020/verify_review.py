"""Focused checks against isolated form storage. Does not call chatbot/model endpoints."""
import hashlib,importlib.util,json,tempfile,threading,urllib.request,urllib.error
from pathlib import Path
R=Path(__file__).resolve().parent;F=R.parent/'r107_owner_questions_20261020'
checks=[]
def read(p):return json.loads(p.read_text('utf8'))
def check(name,value):checks.append({'check':name,'passed':bool(value)});assert value,name
before=read(R/'BEFORE_simple_questions.json');current=read(F/'simple_questions.json')
lookup={i+1:q['id'] for i,q in enumerate(before['questions'])}
check('explicit old numbers mapped correctly',[lookup[n] for n in [19,26,30,31]]==['Q023','Q031','Q035','Q036'])
check('10 separate remaining prompts',current['count']==10 and len({q['id'] for q in current['questions']})==10)
check('removed questions absent',not {'Q023','Q031','Q035','Q036'}&{q['id'] for q in current['questions']})
check('every old question reviewed',len(read(R/'QUESTION_REVIEW_ALL_56.json'))==56)
reviewed=read(R/'REPLIES_REVIEWED.json')
check('reviewed response file unchanged by reconciliation',hashlib.sha256((F/'responses/simple_answers.json').read_bytes()).hexdigest()==reviewed['file_sha256'])
check('all earlier answer texts preserved',all(reviewed['responses']['answers'].get(k,{}).get('text')==v.get('text') for k,v in read(R/'BEFORE_responses__simple_answers.json')['answers'].items()))
check('earlier events preserved as append-only prefix',(F/'responses/simple_events.jsonl').read_bytes().startswith((R/'BEFORE_responses__simple_events.jsonl').read_bytes()))
for name in ['responses/answers.json','QUESTION_UPDATES.json']:
 check('preserved '+name,(F/name).read_bytes()==(R/('BEFORE_'+name.replace('/','__'))).read_bytes())
for m in read(R/'SOURCE_MANIFEST.json'):
 check('original DOCX unchanged '+m['game'],hashlib.sha256(Path(m['original_path']).read_bytes()).hexdigest()==m['sha256'])
docs=read(R/'TOURNAMENT_SOURCE_UNITS.json')['documents']
check('CS2 penalty table preserves pair',any(row==['ดูสตรีมระหว่างแข่ง','ปรับแพ้ในแมตช์นั้น'] for t in next(d for d in docs if d['game']=='cs2')['tables'] for row in t))
check('source contradictions not filled',sum(bool(u['quality_hold']) for d in docs for u in d['units'])==6)
check('24 rental entries with unknown hours',len(read(R/'RENTAL_SOURCE_RECONCILIATION.json')['packages'])==24 and all(p['duration_minutes'] is None for p in read(R/'RENTAL_SOURCE_RECONCILIATION.json')['packages']))
db=R.parent/'r106_complete_flow_20261020/system/data/knowledge/common.sqlite'
check('frozen database unchanged',hashlib.sha256(db.read_bytes()).hexdigest()==read(F/'questions.json')['source_database_sha256'])
spec=importlib.util.spec_from_file_location('form_review',F/'server.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
with tempfile.TemporaryDirectory(prefix='psu-r108-verify-') as folder:
 m.D=Path(folder);m.STATE=m.D/'answers.json';m.EVENTS=m.D/'events.jsonl'
 m.STATE.write_text('{"answers":{"Q002":{"text":"old"}}}','utf8');saved=m.STATE.read_bytes()
 server=m.ThreadingHTTPServer(('127.0.0.1',0),m.H);threading.Thread(target=server.serve_forever,daemon=True).start()
 def req(path,body=None):
  request=urllib.request.Request('http://127.0.0.1:'+str(server.server_port)+path,data=json.dumps(body).encode() if body is not None else None,headers={'Content-Type':'application/json','X-Questionnaire-Token':m.TOKEN})
  try:
   with urllib.request.urlopen(request) as response:return response.status,json.load(response)
  except urllib.error.HTTPError as e:return e.code,json.load(e)
 _,state=req('/api/simple-state');key=state['questions']['questions'][0]['id']
 check('new narrow question starts blank',key not in state['responses']['answers'])
 check('draft saved in isolated storage',req('/api/simple-draft',{'id':key,'text':'คำตอบสำหรับตรวจระบบ'})[0]==200)
 code,out=req('/api/simple-submit',{'answers':{key:'คำตอบสำหรับตรวจระบบ'}})
 check('submit retains mapping',code==200 and out['submission']['answers'][0]['original_question_ids']==['Q039'])
 check('previous detailed answers unaffected',m.STATE.read_bytes()==saved)
 server.shutdown();server.server_close()
with urllib.request.urlopen('http://127.0.0.1:8120/api/simple-state',timeout=5) as response:live=json.load(response)
check('live HTTP serves new question set',len(live['questions']['questions'])==10 and live['questions']['review_id']=='r108_owner_intake_20261020')
check('live replies preserved',live['responses']==read(F/'responses/simple_answers.json'))
out={'passed':len(checks),'total':len(checks),'checks':checks,'llm_calls':0,'production_applied':False,'browser_visual_verified':False}
(R/'VERIFICATION.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'passed':len(checks),'total':len(checks)}))
