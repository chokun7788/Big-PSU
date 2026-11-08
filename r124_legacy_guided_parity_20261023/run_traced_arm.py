"""Run real legacy/common pipelines on retained questions and retain traces."""
import argparse,collections,dataclasses,json,os,sys,time,traceback,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--arm',choices=['teacher','candidate'],required=True);p.add_argument('--jobs',required=True);p.add_argument('--output',required=True);p.add_argument('--no-llm',action='store_true');p.add_argument('--system',default='system');args=p.parse_args()
S=R/('teacher' if args.arm=='teacher' else args.system);OUT=R/args.output;OUT.mkdir(exist_ok=False)
sys.path.insert(0,str(S));profile='psu-r121-base:latest' if args.arm=='teacher' else 'psu-r121-trained:latest'
os.environ.update(PYTHONDONTWRITEBYTECODE='1',PSU_COMMON_CHAT_PROFILE='' if args.arm=='teacher' else 'r69-migration-preview',
 PSU_KNOWLEDGE_DB=str(S/'data/knowledge/common.sqlite') if args.arm=='candidate' else str(OUT/'teacher_empty.sqlite'),
 PSU_LIVE_BOOKING_FETCH_MODE='wordpress',PSU_LIVE_BOOKING_ENABLED='1',OLLAMA_URL='http://127.0.0.1:12421',
 PSU_BILINGUAL_EN_ENABLED='1',PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_SEMANTIC_RETRIEVAL='1',
 PSU_LLM_PREFLIGHT='0',PSU_PIPELINE_WARMUP='0',PSU_PIPELINE_WORKER_SUPERVISOR='0',PSU_PIPELINE_GLOBAL_TIMEOUT_SEC='180',PSU_PRODUCT_BACKEND_TIMEOUT_SEC='190',
 PSU_CHAT_LOG_DIR=str(OUT/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(OUT/'logs/transcripts.sqlite'),PSU_CONVERSATION_STATE_PATH=str(OUT/'conversation.sqlite'),
 PSU_CHAT_LOG_WEBHOOK_URL='',PSU_CHAT_LOG_POSTGRES='0',PSU_INPUT_QUALITY_REPEAT_POLICY='warn_and_continue')
for key in ('PSU_CHATBOT_OLLAMA_MODEL','PSU_KNOWLEDGE_LLM_MODEL','PSU_QUERY_PLANNER_MODEL','PSU_TOOL_ROUTER_MODEL','PSU_INTENT_LLM_MODEL'):os.environ[key]=profile
from app.pipeline.engine import answer_question_pipeline_debug
jobs=[json.loads(line) for line in Path(args.jobs).read_text('utf8').splitlines()];counts=collections.Counter();transport=[]
native=urllib.request.urlopen
def observed(req,*a,**kw):
 url=getattr(req,'full_url',str(req));event=None
 if ':12421/' in url:event={'url':url,'profile':profile,'started':time.monotonic(),'transport_ok':False};transport.append(event)
 try:
  result=native(req,*a,**kw)
  if event:event['transport_ok']=True
  return result
 finally:
  if event:event['elapsed_to_headers_sec']=time.monotonic()-event.pop('started')
urllib.request.urlopen=observed
def trace(frame,event,arg):
 if event!='call':return
 name=frame.f_code.co_filename.replace('\\','/');marker='/app/'
 if marker not in name:return
 rel=name.split(marker)[-1]
 if rel.startswith(('knowledge/common/','calculator/','calendar/','booking/','runtime/fast_answer','pipeline/query_planner','pipeline/target_resolver','pipeline/structured_tools','pipeline/engine')):
  counts[rel+':'+frame.f_code.co_name]+=1
started=time.monotonic();completed=0
with (OUT/'RESULTS.jsonl').open('x',encoding='utf8') as output:
 for job in jobs:
  counts.clear();transport.clear();before=time.monotonic();os.environ['PSU_ESPORTS_NOW']=job.get('reference_clock') or '2026-10-21T12:00:00+07:00'
  try:
   sys.setprofile(trace)
   result=answer_question_pipeline_debug(job['question'],locale=job.get('locale','auto'),experimental_allow_llm=not args.no_llm,
        experimental_rag_fallback=True,global_timeout_sec=180,recent_history=[])
   sys.setprofile(None)
   row={'key':job['key'],'question':job['question'],'locale':job.get('locale','auto'),'result':dataclasses.asdict(result),'function_calls':dict(counts),
      'model_transport':list(transport),'arm':args.arm,'model_profile':profile,'llm_allowed':not args.no_llm,'elapsed_sec':time.monotonic()-before}
  except Exception as exc:
   sys.setprofile(None);row={'key':job['key'],'question':job['question'],'error':repr(exc),'traceback':traceback.format_exc(),'function_calls':dict(counts)}
  output.write(json.dumps(row,ensure_ascii=False,default=str)+'\n');output.flush();completed+=1
  progress={'running':True,'arm':args.arm,'completed':completed,'total':len(jobs),'elapsed_sec':time.monotonic()-started,'pid':os.getpid(),'last_key':job['key']}
  (OUT/'PROGRESS.json').write_text(json.dumps(progress,indent=2),'utf8')
  print(json.dumps({'arm':args.arm,'completed':completed,'total':len(jobs),'key':job['key'][:8],'elapsed':row.get('elapsed_sec'),'error':row.get('error')},ensure_ascii=False),flush=True)
(OUT/'COMPLETE.json').write_text(json.dumps({'complete':True,'questions':completed,'llm_allowed':not args.no_llm,'saved_answers_replayed':False,'actual_pipeline_calls':True,'model_profile':profile,'elapsed_sec':time.monotonic()-started},indent=2),'utf8')
