"""Focused checks for draft/submit workflow using isolated temporary storage."""
import hashlib,importlib.util,json,tempfile,threading,urllib.error,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent;spec=importlib.util.spec_from_file_location('form',R/'server.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
checks=[]
def check(name,ok):checks.append({'check':name,'passed':bool(ok)});assert ok,name
with tempfile.TemporaryDirectory(prefix='psu-simple-form-') as folder:
 m.D=Path(folder);m.STATE=m.D/'answers.json';m.EVENTS=m.D/'events.jsonl';m.STATE.write_text(json.dumps({'answers':{'Q002':{'text':'existing owner answer','status':'answered'}}}),'utf8');old=m.STATE.read_bytes()
 server=m.ThreadingHTTPServer(('127.0.0.1',0),m.H);threading.Thread(target=server.serve_forever,daemon=True).start();base='http://127.0.0.1:'+str(server.server_port)
 def req(path,body=None):
  request=urllib.request.Request(base+path,data=json.dumps(body).encode() if body is not None else None,headers={'Content-Type':'application/json','X-Questionnaire-Token':m.TOKEN})
  try:
   with urllib.request.urlopen(request) as r:return r.status,json.load(r)
  except urllib.error.HTTPError as e:return e.code,json.load(e)
 status,data=req('/api/simple-state');prompts=data['questions']['questions'];id=prompts[0]['id'];check('only 56 grouped pending prompts',status==200 and len(prompts)==56 and all(q['id'] not in ['Q002','Q006','Q007','Q012','Q024'] for q in prompts))
 check('draft saved',req('/api/simple-draft',{'id':id,'text':'คำตอบเพิ่มทดสอบ'})[0]==200)
 _,data=req('/api/simple-state');check('draft restored without marking submitted',data['responses']['answers'][id]['text']=='คำตอบเพิ่มทดสอบ' and data['responses']['answers'][id]['submitted_at'] is None)
 check('blank submission rejected',req('/api/simple-submit',{'answers':{id:' '}})[0]==400)
 status,submitted=req('/api/simple-submit',{'answers':{id:'คำตอบเพิ่มทดสอบ'}});check('submission contains text and original question mapping',status==200 and submitted['count']==1 and submitted['submission']['answers'][0]['answer']=='คำตอบเพิ่มทดสอบ' and submitted['submission']['answers'][0]['original_question_ids'])
 check('submission stored as recoverable file',(m.D/'submissions'/submitted['filename']).exists())
 _,data=req('/api/simple-state');check('submitted marker restored on reload',bool(data['responses']['answers'][id]['submitted_at']))
 check('previous owner answers preserved exactly',m.STATE.read_bytes()==old)
 server.shutdown();server.server_close()
db=R.parent/'r106_complete_flow_20261020/system/data/knowledge/common.sqlite';frozen=json.loads((R/'questions.json').read_text('utf8'));check('chatbot database unchanged',hashlib.sha256(db.read_bytes()).hexdigest()==frozen['source_database_sha256'])
(R/'SIMPLE_VERIFICATION.json').write_text(json.dumps({'checks':checks,'passed':len(checks),'total':len(checks),'scope':'isolated simple draft and submission checks; no LLM calls','browser_visual_verified':False},ensure_ascii=False,indent=2),'utf8');print(json.dumps({'passed':len(checks),'total':len(checks)}))
