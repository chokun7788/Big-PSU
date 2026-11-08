"""Actual chat HTTP and session store with a dedicated owner-created fixture."""
import os,sys,json,time,subprocess,urllib.request
from pathlib import Path
B=Path(__file__).resolve().parent;ROOT=B.parent/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local'
env=os.environ.copy();env.update(PSU_KNOWLEDGE_DB=str(B/'OWNER_HTTP_DEMO_ONLY_2.sqlite'),PSU_COMMON_ALLOW_DEMO='1',OLLAMA_URL='http://127.0.0.1:11436',PSU_EMBEDDING_OLLAMA_URL='http://127.0.0.1:11436',PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_PIPELINE_WORKER_SUPERVISOR='0',PSU_CHAT_JOBS_ENABLED='0',PSU_CHAT_LOG_DIR=str(B/'fixture_web_logs'),PSU_CHAT_LOG_SQLITE_PATH=str(B/'fixture_web_logs/transcripts.sqlite'))
out=(B/'fixture_web_server.out.log').open('x',encoding='utf-8');err=(B/'fixture_web_server.err.log').open('x',encoding='utf-8')
proc=subprocess.Popen([str(ROOT/'runtime/python/python.exe'),'-B','-m','app.web_api.server','--host','127.0.0.1','--port','18094'],cwd=ROOT,env=env,stdout=out,stderr=err,creationflags=subprocess.CREATE_NO_WINDOW)
(B/'FIXTURE_WEB_PROCESS.json').write_text(json.dumps({'pid':proc.pid,'python':str(ROOT/'runtime/python/python.exe'),'port':18094,'owned_this_turn':True,'database':env['PSU_KNOWLEDGE_DB']}),encoding='utf-8')
url='http://127.0.0.1:18094'
def get(path,data=None):
 req=urllib.request.Request(url+path,data=json.dumps(data).encode() if data else None,headers={'Content-Type':'application/json'})
 with urllib.request.urlopen(req,timeout=25) as response:return json.load(response)
try:
 for n in range(60):
  if proc.poll() is not None:raise RuntimeError('Fixture web server exited')
  try:get('/health');break
  except OSError:time.sleep(.5)
 results=[]
 with (B/'WEB_FIXTURE_RESULTS.jsonl').open('x',encoding='utf-8') as f:
  for n,line in enumerate((B/'OWNER_HTTP_RESULTS.jsonl').read_text(encoding='utf-8').splitlines()):
   c=json.loads(line);lang=c['lang'];kind=c['kind'];key=next(x['field'] for x in c['artifact']['obligations'])
   question=('เดโมใหม่ ' if lang=='th' else 'R62 demo ')+kind+' '+key
   start=time.perf_counter();a=get('/api/chat',{'question':question,'locale':lang,'client_session_id':'r62-fixture-'+lang,'client_turn_id':'canonical-'+str(n),'debug':True})
   ok=a.get('ok') is True and not a.get('timed_out') and a.get('mode')=='pipeline:common_content' and bool(a.get('answer'))
   # Route names are not guessed: actual common response mode must be inspected.
   if a.get('mode')=='pipeline:common_published':ok=a.get('ok') is True and not a.get('timed_out') and bool(a.get('answer'))
   obs=(a.get('decision_artifact') or a.get('decision') or {}).get('obligations',[])
   if obs:ok=ok and any(x['field']==key for x in obs)
   row={'kind':kind,'lang':lang,'key':key,'passed':ok,'seconds':time.perf_counter()-start,'response':a};results.append(row);f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush()
 summary={'cases':len(results),'passed':sum(x['passed'] for x in results),'modes':sorted({x['response'].get('mode','') for x in results}),'actual_chat_http_and_session':True,'worker_load_benchmark':False,'only_fixture_owner_facts':True}
 (B/'WEB_FIXTURE_SUMMARY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8');print(summary,flush=True)
 if '--serve' in sys.argv:
  while not (B/'STOP_WEB_FIXTURE').exists():time.sleep(.5)
finally:
 proc.terminate();proc.wait(timeout=10);out.close();err.close()
