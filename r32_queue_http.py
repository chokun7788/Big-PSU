"""Actual HTTP rejection protocol on an isolated handler with a full admission gate."""
import os,sys,json,threading,urllib.request,urllib.error
from pathlib import Path
from http.server import ThreadingHTTPServer
from unittest.mock import patch,Mock
ROOT=Path(__file__).parent;P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(P));sys.path.insert(0,str(ROOT/'work/r30_test_dependencies'));os.environ['PSU_BILINGUAL_EN_ENABLED']='1'
from app.web_api import server
R=Path((ROOT/'r32_report_path.txt').read_text().strip());rows=[]
gate=Mock();gate.acquire.return_value=False
with patch.object(server,'_ACTIVE_REQUESTS',gate):
 http=ThreadingHTTPServer(('127.0.0.1',0),server.ChatHandler);worker=threading.Thread(target=http.serve_forever,daemon=True);worker.start()
 try:
  for loc,q in [('th','มีเกมอะไรบ้าง'),('en','What games are available?')]:
   payload=dict(question=q,locale=loc,recent_history=[],client_session_id='r32-queue-protocol-'+loc)
   try:urllib.request.urlopen(urllib.request.Request(f'http://127.0.0.1:{http.server_port}/api/chat',json.dumps(payload).encode(),{'Content-Type':'application/json'}))
   except urllib.error.HTTPError as e:
    raw=json.loads(e.read());headers=dict(e.headers);errors=[]
    if e.code!=503:errors.append('wrong_http_status')
    if raw.get('retryable') is not True:errors.append('missing_explicit_retryable')
    if raw.get('error')!='server_busy':errors.append('wrong_queue_error')
    if e.headers.get('Retry-After')!='1':errors.append('missing_bounded_retry_header')
    if e.headers.get('Content-Language')!=loc:errors.append('wrong_response_locale')
    rows.append(dict(locale=loc,status=e.code,headers=headers,response=raw,passed=not errors,errors=errors))
 finally:http.shutdown();http.server_close();worker.join(timeout=5)
with (R/'R32_QUEUE_HTTP_PROTOCOL.json').open('x',encoding='utf-8') as out:json.dump(dict(scope='controlled HTTP admission rejection, not real WordPress peak-load SLA',rows=rows),out,ensure_ascii=False,indent=2)
print(json.dumps({'total':len(rows),'passed':sum(r['passed'] for r in rows),'errors':[r['errors'] for r in rows]},ensure_ascii=False));assert len(rows)==2 and all(r['passed'] for r in rows)
