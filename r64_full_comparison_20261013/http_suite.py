import json,os,socket,subprocess,sys,time,urllib.request,collections
from pathlib import Path
import harness
B=Path(__file__).resolve().parent
def main():
 mode=sys.argv[1];tag=sys.argv[2] if len(sys.argv)>2 else '';out=B/(mode+'_http'+('_'+tag if tag else ''));out.mkdir(exist_ok=False)
 with socket.socket() as sock:sock.bind(('127.0.0.1',0));port=sock.getsockname()[1]
 env=os.environ.copy();env.update(PSU_EVAL_FORMAT=mode,PSU_LOCAL_LLM_ASSIST_ENABLED='0',PSU_KNOWLEDGE_DB=str(B/(mode+'.sqlite')),PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_PIPELINE_WORKER_SUPERVISOR='0',PSU_CHAT_JOBS_ENABLED='0',PSU_CHAT_LOG_DIR=str(out/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(out/'logs/transcripts.sqlite'),PSU_SESSION_CONTEXT_SQLITE_PATH=str(out/'sessions.sqlite'))
 log=(out/'server.log').open('x',encoding='utf-8');proc=subprocess.Popen([sys.executable,'-B',str(B/'http_server.py'),'--host','127.0.0.1','--port',str(port)],cwd=harness.STAGE,env=env,stdout=log,stderr=subprocess.STDOUT,creationflags=subprocess.CREATE_NO_WINDOW)
 def request(path,body=None):
  req=urllib.request.Request('http://127.0.0.1:'+str(port)+path,data=json.dumps(body,ensure_ascii=False).encode() if body else None,headers={'Content-Type':'application/json'})
  with urllib.request.urlopen(req,timeout=25) as response:return json.load(response)
 rows=[]
 try:
  for _ in range(120):
   if proc.poll() is not None:raise RuntimeError('HTTP evaluation server exited')
   try:request('/health');break
   except OSError:time.sleep(.25)
  smoke=subprocess.run([sys.executable,'-B',str(harness.STAGE/'tests/smoke_test_bilingual_web_api.py'),'--url','http://127.0.0.1:'+str(port)],cwd=harness.STAGE,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=150)
  for n,entry in enumerate(json.loads((B/'SESSIONS.json').read_text(encoding='utf-8'))):
   session='r64-evaluation-'+mode+'-session-'+str(n);last_seen=''
   for i,turn in enumerate(entry['case'].get('turns',[])):
    body={'question':turn.get('question') or turn.get('query'),'locale':turn.get('locale',entry['case'].get('locale','auto')),'client_session_id':session,'client_turn_id':'r64-evaluation-turn-'+str(n)+'-'+str(i),'last_seen_response_id':last_seen,'debug':True,'experimental_allow_llm':False}
    start=time.perf_counter()
    try:
     response=request('/api/chat',body)
     session=response.get('session_id',session);last_seen=response.get('request_id','')
     from tools.eval_contract_v2 import contract_matches
     _,fail=contract_matches(response.get('answer',''),turn.get('answer_contract') or turn)
     if not response.get('ok') or response.get('timed_out'):fail.append('http_request_or_deadline_failure')
     r={'session':n,'turn':i,'question':body['question'],'response':response,'passed':not fail,'failures':fail,'elapsed':time.perf_counter()-start}
    except Exception as e:r={'session':n,'turn':i,'question':body['question'],'passed':False,'failures':['transport:'+repr(e)]}
    rows.append(r)
    with (out/'RESULTS.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(r,ensure_ascii=False)+'\n')
  summary={'turns':len(rows),'passed':sum(r['passed'] for r in rows),'bilingual_concurrent_smoke_exit':smoke.returncode,'actual_http_sessions':True,'worker_supervisor_enabled':False,'llm_enabled':False,'draft_only':mode=='common'}
  (out/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(summary,ensure_ascii=False),flush=True)
 finally:proc.terminate();proc.wait(10);log.close()
if __name__=='__main__':main()
