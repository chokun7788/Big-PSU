import json,os,socket,subprocess,time,urllib.request,urllib.parse,sqlite3,sys
from pathlib import Path
OUT=Path(__file__).resolve().parent
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');target=ROOT/'data/knowledge/migration_r63_20261013'
runtime=OUT.parent/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/runtime/python/python.exe'
with socket.socket() as sock:sock.bind(('127.0.0.1',0));port=sock.getsockname()[1]
env=os.environ.copy();env['PSU_LOCAL_LLM_ASSIST_ENABLED']='0';env['PSU_KNOWLEDGE_DB']=str(target/'approved.sqlite')
tag=sys.argv[1] if len(sys.argv)>1 else 'initial'
out=(OUT/('installed_owner_'+tag+'.out.log')).open('x',encoding='utf-8');err=(OUT/('installed_owner_'+tag+'.err.log')).open('x',encoding='utf-8')
proc=subprocess.Popen([str(runtime),'-B','-m','app.knowledge.common.owner_server','--port',str(port),'--db',str(target/'approved.sqlite'),'--no-browser'],cwd=ROOT,env=env,stdout=out,stderr=err,creationflags=subprocess.CREATE_NO_WINDOW)
checks=[]
try:
 session=None
 for _ in range(60):
  if proc.poll() is not None:raise RuntimeError('Owner server exited')
  if (target/'owner-session.json').exists():
   candidate=json.loads((target/'owner-session.json').read_text(encoding='utf-8'))
   if candidate['pid']==proc.pid:session=candidate;break
  time.sleep(.25)
 if not session:raise RuntimeError('No owner session')
 token=session['url'].split('#token=')[1]
 def get(path):
  req=urllib.request.Request('http://127.0.0.1:'+str(port)+path,headers={'Authorization':'Bearer '+token})
  with urllib.request.urlopen(req,timeout=15) as r:return json.load(r)
 status=get('/api/status');checks.append({'name':'installed owner serves 582 draft heads','passed':len(status['records'])==582 and status['active']=='' and not status['published_ids']})
 kinds={r['kind']:r['record_id'] for r in status['records']}
 for kind,rid in kinds.items():
  row=get('/api/record?id='+urllib.parse.quote(rid));checks.append({'name':'installed edit form data:'+kind,'passed':row['record']['record_id']==rid and row['record']['kind']==kind})
 result={'passed':sum(c['passed'] for c in checks),'total':len(checks),'checks':checks,'server_code':str(ROOT),'separate_db':True,'llm_preview_not_tested':True,'process_stopped':False}
finally:
 proc.terminate();proc.wait(timeout=10);out.close();err.close()
 # The owned server cannot run its finally on TerminateProcess; remove only
 # its capability file after matching its exact PID. No other files touched.
 session_path=target/'owner-session.json'
 if session_path.exists() and json.loads(session_path.read_text(encoding='utf-8'))['pid']==proc.pid:session_path.unlink()
if 'result' in globals():
 result['process_stopped']=True;(OUT/'INSTALLED_OWNER_CHECK.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in result.items() if k!='checks'}))
 if not all(c['passed'] for c in checks):raise SystemExit(1)
