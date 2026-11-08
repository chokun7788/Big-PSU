import os,sys,json,time,hashlib
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
B=Path(__file__).resolve().parent
source=Path(sys.argv[1]).resolve();tag=sys.argv[2];suite=sys.argv[3] if len(sys.argv)>3 else 'target';holdout=suite=='holdout'
T=B/'results'/tag;T.mkdir(parents=True,exist_ok=False)
os.environ.update(PYTHONDONTWRITEBYTECODE='1',PYTHONUTF8='1',PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(source/'system/data/knowledge/common.sqlite'),PSU_CHAT_LOG_DIR=str(T/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(T/'logs/transcripts.sqlite'),PSU_CONVERSATION_STATE_PATH=str(T/'state.sqlite'),PSU_BILINGUAL_EN_ENABLED='1',PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_CHAT_LOG_WEBHOOK_URL='',PSU_CHAT_LOG_POSTGRES='0')
sys.path.insert(0,str(source/'system'))
from app.calendar import service_calendar
service_calendar.now_bangkok=lambda:datetime(2026,10,16,12,tzinfo=ZoneInfo('Asia/Bangkok'))
from app.pipeline.migrated_chat import answer
from app.core.locale import LocaleDecision
from target_cases import CASES,HOLDOUT
if suite=='risk':
 from risk_cases import CASES
if suite=='exploratory':
 from exploratory_cases import CASES
if suite=='scope':
 from scope_cases import CASES
if suite=='ownership':
 from ownership_cases import CASES
if suite=='unseen':
 from holdout_cases import CASES
if suite=='payment_boundary':
 from payment_boundary_cases import CASES
if suite=='semantic_acceptance':
 from semantic_acceptance_cases import CASES
db=source/'system/data/knowledge/common.sqlite';before=hashlib.sha256(db.read_bytes()).hexdigest()
rows=[]
with (T/'ANSWERS.jsonl').open('x',encoding='utf8') as f:
 for i,c in enumerate(HOLDOUT if holdout else CASES):
  start=time.perf_counter();loc=LocaleDecision(c['locale'],c['locale'],c['locale'],1,'explicit_test_locale')
  r=answer(c['question'],locale=loc,history=[],allow_llm=True);a=r.answer;artifact=r.decision_artifact or {};errors=[]
  for s in c['need']:
   if s.casefold() not in a.casefold():errors.append('missing:'+s)
  for s in c['forbid']:
   if s.casefold() in a.casefold():errors.append('forbidden:'+s)
  if not r.validation.ok:errors.append('validation_rejected')
  if not a.strip():errors.append('empty_answer')
  if c.get('expected_mode') and r.mode!=c['expected_mode']:errors.append('mode:'+r.mode)
  if c.get('expected_source'):
   expected=c['expected_source'];sources={h.get('record_id') for h in r.hits}
   if expected.startswith('!'):
    if expected[1:] in sources:errors.append('wrong_source:'+expected[1:])
   elif expected not in sources:errors.append('missing_source:'+expected)
  if c.get('expected_sources_any') and not ({h.get('record_id') for h in r.hits}&set(c['expected_sources_any'])):errors.append('missing_any_expected_source')
  if c.get('expected_topic') and artifact.get('query_plan',{}).get('unconfirmed_topic')!=c['expected_topic']:errors.append('wrong_unconfirmed_topic')
  if artifact.get('migration',{}).get('legacy_fallback_used') is not False:errors.append('legacy_fallback_status')
  row={'index':i,**c,'passed':not errors,'errors':errors,'answer':a,'mode':r.mode,'seconds':time.perf_counter()-start,'artifact':artifact,'hits':r.hits}
  rows.append(row);f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush()
  print(json.dumps({'i':i,'passed':not errors,'errors':errors},ensure_ascii=False),flush=True)
after=hashlib.sha256(db.read_bytes()).hexdigest()
from app.pipeline.llm_health import llm_health_snapshot
(T/'MODEL_HEALTH.json').write_text(json.dumps(llm_health_snapshot(),ensure_ascii=False,indent=2),encoding='utf8')
summary={'source':str(source),'llm_enabled':True,'format':'common','suite':suite,'holdout':holdout,'count':len(rows),'passed':sum(x['passed'] for x in rows),'data_unchanged':before==after,'database_sha256':after,'method':'real dispatcher, frozen clock, no network/browser certification; source content contracts, not legacy route protocol'}
(T/'SUMMARY.json').write_text(json.dumps(summary,indent=2),encoding='utf8');print(json.dumps(summary))
