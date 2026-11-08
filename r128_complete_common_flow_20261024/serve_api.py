"""Runtime timing hooks around the R128 common candidate."""
import contextvars,dataclasses,functools,json,os,sys,threading,time,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';sys.path.insert(0,str(S));OUT=Path(os.environ['R124_RUN_DIR'])
CTX=contextvars.ContextVar('latency_audit',default=None);PARENT=contextvars.ContextVar('latency_span',default=None);guard=threading.Lock()
def instrument(fn,name):
 @functools.wraps(fn)
 def wrapped(*a,**k):
  ctx=CTX.get()
  if ctx is None:return fn(*a,**k)
  span={'id':len(ctx['events'])+1,'name':name,'parent':PARENT.get(),'start_sec':time.perf_counter()-ctx['started']};ctx['events'].append(span);token=PARENT.set(span['id']);before=time.perf_counter()
  try:return fn(*a,**k)
  except Exception as e:span['error']=type(e).__name__+': '+str(e);raise
  finally:span['duration_sec']=time.perf_counter()-before;PARENT.reset(token)
 return wrapped
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow import understanding,meaning_review,date_context,native_contract,obligation_verifier,projection
from app.knowledge.common.domain_flow.model import EvidenceSelector
from app.booking import live_status
from app.web_api import server
MigratedView.snapshot=instrument(MigratedView.snapshot,'source.snapshot')
MigratedView.still_current=instrument(MigratedView.still_current,'source.epoch_check')
Engine.from_snapshot=classmethod(instrument(Engine.from_snapshot.__func__,'index.from_snapshot'))
Engine.plan=instrument(Engine.plan,'reader.plan')
Engine._render_one=instrument(Engine._render_one,'answer.render_one')
CommonAnswerer.finish=instrument(CommonAnswerer.finish,'answer.finish')
for mod,fn,name in [(understanding,'interpret','context.interpret'),(meaning_review,'review','context.independent_review'),(date_context,'resolve','date.resolve'),(native_contract,'prepare','request.compile'),(obligation_verifier,'assess','answer.obligation_check'),(live_status,'get_live_booking_status','provider.fetch')]:setattr(mod,fn,instrument(getattr(mod,fn),name))
EvidenceSelector.select=instrument(EvidenceSelector.select,'evidence.select')
original_urlopen=urllib.request.urlopen
class Response:
 def __init__(self,r,event):self.r=r;self.event=event;self.start=time.perf_counter();self.data=[]
 def __getattr__(self,k):return getattr(self.r,k)
 def __enter__(self):self.r.__enter__();return self
 def read(self,*a,**k):
  result=self.r.read(*a,**k)
  if isinstance(result,bytes):self.data.append(result)
  return result
 def __exit__(self,*a):
  try:return self.r.__exit__(*a)
  finally:
   self.event['total_sec']=time.perf_counter()-self.event['_start'];self.event.pop('_start',None)
   body=b''.join(self.data);self.event['response_bytes']=len(body)
   if self.event['kind']=='model':
    try:
     value=json.loads(body);self.event.update(eval_count=value.get('eval_count'),stage=value.get('provenance',{}).get('stage'),response_model=value.get('model'))
    except (ValueError,UnicodeError):pass
def observed_http(req,*a,**k):
 ctx=CTX.get();url=getattr(req,'full_url',str(req))
 if ctx is None:return original_urlopen(req,*a,**k)
 model=url.startswith(os.environ['OLLAMA_URL']);event={'kind':'model' if model else 'provider_http','url':url,'_start':time.perf_counter(),'start_sec':time.perf_counter()-ctx['started'],'parent':PARENT.get()};ctx['http'].append(event)
 if model and getattr(req,'data',None):
  payload=json.loads(req.data);event.update(request_bytes=len(req.data),options=payload.get('options'),requested_model=payload.get('model'),message_characters=sum(len(m.get('content','')) for m in payload.get('messages',[])))
 try:
  response=original_urlopen(req,*a,**k);event.update(headers_sec=time.perf_counter()-event['_start'],transport_ok=True);return Response(response,event)
 except Exception as e:event.update(total_sec=time.perf_counter()-event.pop('_start'),transport_ok=False,error=type(e).__name__+': '+str(e));raise
urllib.request.urlopen=observed_http
native=server.answer_question_pipeline_debug
def observed(*a,**k):
 ctx={'started':time.perf_counter(),'events':[],'http':[]};token=CTX.set(ctx);cpu=time.process_time()
 try:
  result=native(*a,**k)
  row={'question':a[0] if a else k.get('question'),'wall_sec':time.perf_counter()-ctx['started'],'local_cpu_sec':time.process_time()-cpu,'events':ctx['events'],'http':ctx['http'],'pipeline':dataclasses.asdict(result)}
  with guard:
   with (OUT/'TIMINGS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
  return result
 finally:CTX.reset(token)
server.answer_question_pipeline_debug=observed
if __name__=='__main__':
 store=MigratedView(S/'data/knowledge/common.sqlite');Engine.from_snapshot(store.snapshot(),cache_key=store.path.resolve())
 print('R128 common candidate timing server ready',flush=True);raise SystemExit(server.main())
