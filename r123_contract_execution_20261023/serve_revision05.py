"""Observe unchanged API/PipelineAnswer; controlled unavailable booking fixture.

No test question, category, expected value or answer is injected into the engine.
"""
import dataclasses,json,os,sys,threading,time,urllib.request,uuid
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'revision05_system'));OUT=Path(os.environ['R116_RUN_DIR'])
from app.booking import live_status
from app.runtime import fast_answer
from app.pipeline import bilingual_english
def unavailable(d):return live_status._unavailable(d,'R116 controlled unavailable, matching retained Full workload; no actual occupancy oracle',error_code='fixture_offline')
for module in [live_status,fast_answer,bilingual_english]:module.get_live_booking_status=unavailable
from app.web_api import server
local=threading.local();lock=threading.Lock();sequence=0;active_window=None
original_post=server.Handler.do_POST if hasattr(server,'Handler') else None
# Resolve the actual request handler class without assuming a class name.
handlers=[x for x in vars(server).values() if isinstance(x,type) and issubclass(x,server.BaseHTTPRequestHandler) and x is not server.BaseHTTPRequestHandler]
assert len(handlers)==1;Handler=handlers[0];native_post=Handler.do_POST
def observed_post(self):
 global sequence,active_window
 with lock:sequence+=1;window=sequence;active_window=window
 local.pipeline=None;local.window=window
 try:return native_post(self)
 finally:
  with lock:
   if active_window==window:active_window=None
  local.pipeline=None
Handler.do_POST=observed_post
native_answer=server.answer_question_pipeline_debug
def observed_answer(*args,**kwargs):
 result=native_answer(*args,**kwargs)
 local.pipeline={'input':args[0] if args else kwargs.get('question'), 'result':dataclasses.asdict(result)}
 return result
server.answer_question_pipeline_debug=observed_answer
native_json=server._json_bytes
def observed_json(payload,status=200):
 if isinstance(payload,dict) and payload.get('request_id') and 'answer' in payload:
  row={'request_id':payload['request_id'],'window':getattr(local,'window',None),'pipeline':getattr(local,'pipeline',None),
       'response_answer':payload['answer'],'response_mode':payload.get('mode'),'status':status}
  with lock:
   with (OUT/'PIPELINE_CAPTURE.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False,default=server._json_default)+'\n')
 return native_json(payload,status)
server._json_bytes=observed_json
native_urlopen=urllib.request.urlopen
def observed_urlopen(req,*args,**kwargs):
 url=getattr(req,'full_url',str(req));is_model=url.startswith(os.environ.get('OLLAMA_URL','http://127.0.0.1:11434').rstrip('/')+'/')
 if not is_model:return native_urlopen(req,*args,**kwargs)
 event={'id':uuid.uuid4().hex,'window':active_window,'thread':threading.get_ident(),'url':url,'transport_ok':False,'started':time.monotonic()}
 try:
  response=native_urlopen(req,*args,**kwargs);event['transport_ok']=True;return response
 except Exception as exc:event.update(error_type=type(exc).__name__,error=str(exc));raise
 finally:
  event['elapsed_to_headers_sec']=round(time.monotonic()-event.pop('started'),4)
  with lock:
   with (OUT/'MODEL_TRANSPORT.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(event,ensure_ascii=False)+'\n')
urllib.request.urlopen=observed_urlopen
if __name__=='__main__':raise SystemExit(server.main())
