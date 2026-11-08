"""Bounded LLM-on smoke with actual local inference and full saved responses."""
import dataclasses,json,os,sys,time,urllib.request
from pathlib import Path
from unittest.mock import patch
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system';T=B/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False)
os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(S/'data/knowledge/common.sqlite'),PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_CHAT_LOG_DIR=str(T/'logs'))
sys.path.insert(0,str(S));import app.knowledge.common as pkg;pkg.__path__.insert(0,str(B/'candidate/app/knowledge/common'))
if True:
 import app.pipeline as pipeline_pkg;pipeline_pkg.__path__.insert(0,str(B/'candidate/app/pipeline'))
from app.pipeline.migrated_chat import answer
from app.core.locale import LocaleDecision
from app.knowledge.common.dialogue import state_from_answer
from app.pipeline.request_deadline import request_deadline
payload={'model':'scb10x/typhoon2.5-qwen3-4b','stream':False,'think':False,'prompt':'Return exactly READY','options':{'temperature':0,'num_predict':12,'num_ctx':3072}}
with urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:11434/api/generate',data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'}),timeout=45) as f:preflight=json.load(f)
(T/'MODEL_PREFLIGHT.json').write_text(json.dumps(preflight,ensure_ascii=False,indent=2),'utf8');assert preflight.get('done'),preflight
cases=[('th','The Legend of Zelda: Breath of the Wild คือกมอะๆร','summary'),('en','Beat Saber how do you play?','how_to_play'),('en','What is the studio policy for friday maintenance','answer'),('th','PC มีอะไรบ้าง',None),('th','อุปกรณ์','equipment'),('en','Could you give me a beginner-friendly introduction to Beat Saber?','summary')]
original=urllib.request.urlopen;calls=[];rows=[];history=[]
def observed(req,*args,**kwargs):
 start=time.perf_counter();url=req.full_url if hasattr(req,'full_url') else str(req)
 if not url.startswith('http://127.0.0.1:11434/'):raise AssertionError('Unexpected external call in local smoke: '+url)
 try:
  response=original(req,*args,**kwargs);calls.append({'url':url,'response_opened':True,'seconds_until_headers':time.perf_counter()-start});return response
 except Exception as e:
  calls.append({'url':url,'response_opened':False,'error_type':type(e).__name__});raise
for i,(lang,q,expected) in enumerate(cases):
 before=len(calls);start=time.perf_counter()
 with patch('urllib.request.urlopen',side_effect=observed),request_deadline(22):r=answer(q,locale=LocaleDecision(lang,lang,lang,1,'explicit'),history=history if i==4 else [],allow_llm=True)
 p=r.decision_artifact.get('query_plan') or {};ok=None if expected is None else (p.get('operation')=='equipment' and len(r.hits)>0 if expected=='equipment' else any(h.get('field')==expected for h in r.hits)) and r.validation.ok
 row={'index':i,'question':q,'language':lang,'passed':ok,'expectation':expected,'observational_only':expected is None,'seconds':time.perf_counter()-start,'model_http':calls[before:],'result':dataclasses.asdict(r)};rows.append(row)
 with (T/'RESULTS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
 if i==3:history=[{'role':'user','text':q},{'role':'assistant','text':r.answer,'common_read_state':state_from_answer(r) or {},'delivery_status':'server_written'}]
 print(json.dumps({'index':i,'passed':ok,'seconds':row['seconds'],'model_calls':len(row['model_http']),'answer':r.answer[:300]},ensure_ascii=False),flush=True)
summary={'requests':len(rows),'asserted':sum(r['passed'] is not None for r in rows),'passed':sum(r['passed'] is True for r in rows),'observational':sum(r['passed'] is None for r in rows),'actual_model_preflight_done':True,'chat_model_http_calls':len(calls),'transport_failure_calls':sum(not c['response_opened'] for c in calls),'llm_enabled':True,'full_test':False}
(T/'SUMMARY.json').write_text(json.dumps(summary,indent=2),'utf8');print(json.dumps(summary));sys.exit(any(r['passed'] is False for r in rows))
