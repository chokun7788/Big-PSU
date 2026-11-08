"""Actual owner HTTP + published chat HTTP in isolated synthetic processes."""
import os,sys,json,threading,subprocess,socket,time,urllib.request,uuid,contextlib
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';T=R/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False);sys.path[:0]=[str(S),str(R)]
os.environ.update(PSU_COMMON_ALLOW_DEMO='1',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_ESPORTS_NOW='2026-10-20T12:00:00+07:00')
from scenario_support import Fixture,bi
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import make_handler
from http.server import ThreadingHTTPServer
f=Fixture.clone(T/'SYNTHETIC_ONLY.sqlite',R/'fixtures/BASE_SYNTHETIC.sqlite');checks=[];exchanges=[]
def port():
 with socket.socket() as s:s.bind(('127.0.0.1',0));return s.getsockname()[1]
def check(name,ok,detail=None):checks.append({'case':name,'passed':bool(ok),'detail':detail});print(name,bool(ok),flush=True)
owner_port=port();token=uuid.uuid4().hex;server=ThreadingHTTPServer(('127.0.0.1',owner_port),make_handler(f.store,token,'isolated-http-fixture',owner_port));threading.Thread(target=server.serve_forever,daemon=True).start()
proc=None;log=(T/'PUBLIC_SERVER.log').open('x',encoding='utf8')
def owner(path,body=None):
 req=urllib.request.Request('http://127.0.0.1:'+str(owner_port)+path,data=json.dumps(body,ensure_ascii=False).encode() if body is not None else None,
   headers={'Content-Type':'application/json','Authorization':'Bearer '+token})
 with urllib.request.urlopen(req,timeout=35) as h:x=json.load(h)
 exchanges.append({'surface':'owner','path':path,'response':x});return x
try:
 registry=owner('/api/registry');check('HTTP owner exposes schema 3.1 and guided mapping schema',registry['version']=='studio-content-3.1' and bool(registry.get('claim_schema')))
 game=template('game');game['record_id']='fx_http_aurora';game['localization']['en_status']='agent_translated'
 for k,v in {'title':bi('ออโรร่าผ่านฟอร์ม','Aurora HTTP Fixture'),'summary':bi('ภาพรวม HTTP_NEW','Overview HTTP_NEW'),'how_to_play':bi('เดิน HTTP_PLAY','Move HTTP_PLAY')}.items():game['fields'][k].update(status='known',value=v)
 saved=owner('/api/save',{'record':game,'expected_version':0,'attest':True,'change_note':'Synthetic HTTP addition'})
 check('new data saved through actual owner API',saved['record']['revision']==1)
 draft=owner('/api/preview',{'question':'What is Aurora HTTP Fixture?','locale':'en','draft':True});check('same dispatcher reads HTTP-added draft', 'HTTP_NEW' in draft['answer'])
 for rid in ['fx_http_aurora']:
  x=f.store.get(rid);owner('/api/approve',{'id':rid,'version':x['version'],'hash':x['hash'],'confirm':True})
 owner('/api/publish',{'ids':['fx_http_aurora'],'expected_active':f.store.snapshot()['active'],'request_key':'http-first-release'})
 public_port=port();env=os.environ.copy();env.update(PYTHONPATH=str(S),PSU_COMMON_CHAT_PROFILE='common-r102-published',PSU_KNOWLEDGE_DB=str(f.path),
  PSU_CHAT_LOG_DIR=str(T/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(T/'logs/transcripts.sqlite'),PSU_CONVERSATION_STATE_PATH=str(T/'conversation.sqlite'),PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_BILINGUAL_EN_ENABLED='1')
 proc=subprocess.Popen([sys.executable,'-B','-X','utf8','-m','app.web_api.server','--host','127.0.0.1','--port',str(public_port)],cwd=S,env=env,stdout=log,stderr=subprocess.STDOUT,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
 url='http://127.0.0.1:'+str(public_port);health=None
 for _ in range(90):
  if proc.poll() is not None:raise RuntimeError('Public candidate server exited; inspect PUBLIC_SERVER.log')
  try:
   with urllib.request.urlopen(url+'/health',timeout=1) as h:health=json.load(h)
   break
  except (OSError,ValueError):time.sleep(.5)
 if not health:raise RuntimeError('Public server startup unavailable')
 check('actual public process loaded R102',health.get('common_loaded_build',{}).get('build_id')=='common-r102-complete-contract-flow')
 def chat(question,session=None):
  payload={'question':question,'locale':'en','debug':True,'client_session_id':session or 'r102-http-'+uuid.uuid4().hex,'client_turn_id':'turn-'+uuid.uuid4().hex,'experimental_allow_llm':True}
  with urllib.request.urlopen(urllib.request.Request(url+'/api/chat',data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'}),timeout=45) as h:x=json.load(h)
  exchanges.append({'surface':'public','question':question,'response':x});return x
 first=chat('What is Aurora HTTP Fixture?');check('published chat reads owner-added approved data','HTTP_NEW' in first.get('answer',''))
 check('published response carries actual R102 per-need audit',first.get('decision_artifact',{}).get('flow_audit',{}).get('version')=='r102')
 changed=saved['record'];changed['fields']['summary']['value']=bi('ฉบับใหม่ HTTP_EDIT','Revised HTTP_EDIT')
 owner('/api/save',{'record':changed,'expected_version':1,'attest':True,'change_note':'Synthetic edit'})
 unpublished=chat('What is Aurora HTTP Fixture?');check('draft changes do not leak to published chat','HTTP_NEW' in unpublished.get('answer','') and 'HTTP_EDIT' not in unpublished.get('answer',''))
 x=f.store.get('fx_http_aurora');owner('/api/approve',{'id':'fx_http_aurora','version':x['version'],'hash':x['hash'],'confirm':True})
 owner('/api/publish',{'ids':['fx_http_aurora'],'expected_active':f.store.snapshot()['active'],'request_key':'http-second-release'})
 edited=chat('What is Aurora HTTP Fixture?');check('published edit updates public answers','HTTP_EDIT' in edited.get('answer','') and 'HTTP_NEW' not in edited.get('answer',''))
 owner('/api/withdraw',{'id':'fx_http_aurora'});withdrawn=chat('What is Aurora HTTP Fixture?');check('HTTP withdrawal cannot resurrect old facts','HTTP_NEW' not in withdrawn.get('answer','') and 'HTTP_EDIT' not in withdrawn.get('answer',''))
except Exception as e:
 import traceback
 check('HTTP lane completed',False,{'error':str(e),'traceback':traceback.format_exc()})
finally:
 server.shutdown();server.server_close()
 if proc is not None:
  proc.terminate()
  try:proc.wait(timeout=15)
  except subprocess.TimeoutExpired:proc.kill();proc.wait(timeout=10)
 log.close()
 (T/'EXCHANGES.json').write_text(json.dumps(exchanges,ensure_ascii=False,indent=2,default=str),'utf8')
 summary={'count':len(checks),'passed':sum(c['passed'] for c in checks),'failed':[c['case'] for c in checks if not c['passed']],'checks':checks,'actual_http':True,'data':'isolated synthetic only','servers_stopped':True}
 (T/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(summary)
sys.exit(bool(summary['failed']))
