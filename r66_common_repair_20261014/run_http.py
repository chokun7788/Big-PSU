"""Correct ACK/session protocol on an isolated server; captures error bodies."""
import sys,os,json,time,subprocess,socket,urllib.request,urllib.error
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path[:0]=[str(B),str(B/'system')]
from harness import STAGE
tag=sys.argv[1];llm=sys.argv[2]=='1';out=B/('http_'+tag);out.mkdir(exist_ok=False)
with socket.socket() as sock:sock.bind(('127.0.0.1',0));port=sock.getsockname()[1]
env=os.environ.copy();env.update(PYTHONPATH=str(STAGE),PSU_R66_LLM='1' if llm else '0',PSU_ESPORTS_NOW='2026-10-14T12:00:00+07:00',PSU_PIPELINE_WORKER_SUPERVISOR='0',PSU_CHAT_JOBS_ENABLED='0',PSU_SESSION_CONTEXT_SQLITE_PATH=str(out/'sessions.sqlite'),PSU_CHAT_LOG_DIR=str(out/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(out/'logs/transcripts.sqlite'))
if tag.endswith('_slow'):env['PSU_R66_TEST_DELIVERY_DELAY']='0.35'
log=(out/'server.log').open('x',encoding='utf-8');proc=subprocess.Popen([sys.executable,'-B',str(B/'http_server.py'),'--host','127.0.0.1','--port',str(port)],cwd=STAGE,env=env,stdout=log,stderr=subprocess.STDOUT,creationflags=subprocess.CREATE_NO_WINDOW)
def request(path,data=None):
 req=urllib.request.Request('http://127.0.0.1:'+str(port)+path,data=json.dumps(data,ensure_ascii=False).encode() if data else None,headers={'Content-Type':'application/json'})
 with urllib.request.urlopen(req,timeout=30) as response:return json.load(response)
rows=[]
try:
 for _ in range(180):
  if proc.poll() is not None:raise RuntimeError('owned test server exited')
  try:request('/health');break
  except OSError:time.sleep(.25)
 sessions=json.loads((B.parent/'r64_full_comparison_20261013/SESSIONS.json').read_text(encoding='utf-8'))
 for n,entry in enumerate(sessions):
  session='r66-'+tag+'-session-'+str(n)+'-verified';ack=''
  for i,turn in enumerate(entry['case']['turns']):
   body={'question':turn.get('question') or turn.get('query'),'locale':turn.get('locale',entry['case'].get('locale','auto')),'client_session_id':session,'client_turn_id':'r66-'+tag+'-turn-'+str(n)+'-'+str(i),'last_seen_response_id':ack,'debug':True,'experimental_allow_llm':llm};start=time.perf_counter()
   try:
    response=request('/api/chat',body);session=response.get('session_id',session);ack=response.get('request_id','')
    from tools.eval_contract_v2 import contract_matches
    _,fail=contract_matches(response.get('answer',''),turn.get('answer_contract') or turn)
    if not response.get('ok') or response.get('timed_out'):fail.append('execution_or_deadline_failure')
    row={'session':n,'turn':i,'question':body['question'],'passed':not fail,'failures':fail,'response':response,'elapsed':time.perf_counter()-start}
   except urllib.error.HTTPError as e:row={'session':n,'turn':i,'question':body['question'],'passed':False,'failures':['HTTP:'+str(e.code)],'error_body':e.read(30000).decode('utf-8',errors='replace')}
   except Exception as e:row={'session':n,'turn':i,'question':body['question'],'passed':False,'failures':['transport:'+repr(e)]}
   rows.append(row)
   with (out/'RESULTS.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
 summary={'turns':len(rows),'passed_literal_contract':sum(x['passed'] for x in rows),'llm_enabled':llm,'actual_http':True,'error_bodies_preserved':True,'common_draft_only':True,'public_booking_verified':False,'delivery_delay_fixture_ms':350 if tag.endswith('_slow') else 0}
 (out/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(summary),flush=True)
 if summary['passed_literal_contract']!=summary['turns']:raise RuntimeError('HTTP dialogue contracts failed; see preserved responses')
finally:
 proc.terminate();proc.wait(10);log.close()
