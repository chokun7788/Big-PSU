"""Isolated real-provider API; no fixture substitution or startup booking read."""
import dataclasses,json,os,sys,threading,time,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';sys.path.insert(0,str(S));OUT=Path(os.environ['R124_RUN_DIR'])
from app.web_api import server
lock=threading.Lock();native=server.answer_question_pipeline_debug
def observed(*args,**kwargs):
 result=native(*args,**kwargs)
 with lock:
  with (OUT/'PIPELINE_CAPTURE.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps({'question':args[0] if args else kwargs.get('question'),'pipeline':dataclasses.asdict(result)},ensure_ascii=False,default=str)+'\n')
 return result
server.answer_question_pipeline_debug=observed
original=urllib.request.urlopen
def transport(req,*args,**kwargs):
 url=getattr(req,'full_url',str(req));event={'url':url,'transport_ok':False};started=time.monotonic()
 try:
  result=original(req,*args,**kwargs);event['transport_ok']=True;return result
 except Exception as exc:event.update(error_type=type(exc).__name__,error=str(exc));raise
 finally:
  if url.startswith(os.environ['OLLAMA_URL']):
   event['elapsed_to_headers_sec']=time.monotonic()-started
   with lock:
    with (OUT/'MODEL_TRANSPORT.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(event,ensure_ascii=False)+'\n')
urllib.request.urlopen=transport
if __name__=='__main__':
    # Warm only the local source index, never fetch provider occupancy or run
    # model inference before a customer request.
    from app.knowledge.common.migrated_view import MigratedView
    from app.knowledge.common.domain_flow.engine import Engine
    store=MigratedView(S/'data/knowledge/common.sqlite')
    Engine.from_snapshot(store.snapshot(),cache_key=store.path.resolve())
    print('R125 local source index ready; no provider/model warmup',flush=True)
    raise SystemExit(server.main())
