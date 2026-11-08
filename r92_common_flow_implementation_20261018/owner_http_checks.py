"""Exercise owner API/UI assets against an isolated SQLite backup only."""
import hashlib,json,os,sys,sqlite3,threading,urllib.request,urllib.error
from pathlib import Path
from http.server import ThreadingHTTPServer
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system'
T=B/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False)
os.environ['PSU_LOCAL_LLM_ASSIST_ENABLED']='0'
sys.path.insert(0,str(S));import app.knowledge.common as pkg;pkg.__path__.insert(0,str(B/'candidate/app/knowledge/common'))
import app.pipeline as pipe;pipe.__path__.insert(0,str(B/'candidate/app/pipeline'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import make_handler
source=B/'verification/flow_2/ISOLATED_NOT_PRODUCTION.sqlite';db=T/'ISOLATED_OWNER_API.sqlite'
a=sqlite3.connect(source.resolve().as_uri()+'?mode=ro',uri=True);z=sqlite3.connect(db);a.backup(z);z.close();a.close()
store=CommonStore(db);before=hashlib.sha256(db.read_bytes()).hexdigest();token='isolated-api-test-not-a-production-capability'
server=ThreadingHTTPServer(('127.0.0.1',0),None);port=server.server_address[1];server.RequestHandlerClass=make_handler(store,token,'isolated_test_actor',port)
thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start();base='http://127.0.0.1:'+str(port)
checks=[]
def request(path,payload=None,auth=True):
 headers={'Content-Type':'application/json'}
 if auth:headers['Authorization']='Bearer '+token
 req=urllib.request.Request(base+path,data=json.dumps(payload).encode() if payload is not None else None,headers=headers)
 with urllib.request.urlopen(req,timeout=15) as response:
  raw=response.read().decode('utf-8');return json.loads(raw) if response.headers.get_content_type()=='application/json' else raw
def check(name,ok,detail=None):checks.append({'case':name,'passed':bool(ok),'detail':detail});print(name,bool(ok),flush=True)
try:
 record=store.get('fixture_lumen_circuit')['record']
 report=request('/api/readiness',{'record':record})
 check('readiness-route-reports-game-data-not-publish-approval',any(t['task']=='game_overview' and t['status']=='data_ready' for t in report['tasks']) and not report['publication_approval_created'],report)
 preview=request('/api/preview',{'question':'Could you give me a beginner-friendly introduction to Lumen Circuit Fixture?','locale':'en'})
 check('owner-http-uses-shared-dispatcher-and-current-content','LUMEN_V3' in preview['answer'] and preview['trace']['preview_dispatcher']=='shared_common_chat',preview)
 follow=request('/api/preview',{'question':'how to play','locale':'en','history':[{'role':'user','text':'Lumen Circuit Fixture game overview'},{'role':'assistant','text':preview['answer'],'common_read_state':preview['common_read_state']}]})
 check('owner-http-follow-up-retains-task-target','LUMEN_PLAY' in follow['answer'],follow)
 js=request('/owner.js',auth=False);html=request('/',auth=False)
 check('owner-ui-serves-task-readiness-display',"/api/readiness" in js and 'ข้อมูลพร้อมสำหรับคำถามใดบ้าง' in js)
 check('owner-ui-explains-draft-and-live-boundaries','เลือกทดลองด้วยฉบับเผยแพร่หรือร่าง' in html)
 try:request('/api/readiness',{'record':record},auth=False);blocked=False
 except urllib.error.HTTPError as e:blocked=e.code==401
 check('readiness-keeps-owner-capability-authentication',blocked)
 check('readiness-and-preview-do-not-write-owner-database',hashlib.sha256(db.read_bytes()).hexdigest()==before)
finally:server.shutdown();server.server_close();thread.join(timeout=3)
(T/'CHECKS.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),'utf-8')
summary={'count':len(checks),'passed':sum(c['passed'] for c in checks),'failed':[c['case'] for c in checks if not c['passed']],'isolated_owner_http':True,'model_calls':0,'full_test':False}
(T/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf-8');print(json.dumps(summary));sys.exit(bool(summary['failed']))
