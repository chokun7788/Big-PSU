"""Isolated evaluation adapters. Draft view never writes approvals/releases."""
from __future__ import annotations
import copy,dataclasses,json,os,sys,time,tempfile
from pathlib import Path
B=Path(__file__).resolve().parent;STAGE=B/'system'
sys.path.insert(0,str(STAGE));sys.path.insert(0,str(B))
def test_temp(tag):
 p=(B/'temp'/tag).resolve();p.mkdir(parents=True,exist_ok=True)
 assert p.is_relative_to(B.resolve())
 os.environ.update(TEMP=str(p),TMP=str(p),TMPDIR=str(p),PSU_TEST_STATE_DIR=str(p/'state'))
 (p/'state').mkdir(exist_ok=True);tempfile.tempdir=str(p)

def configure(mode,llm=False,db=None):
 os.environ.update(PYTHONUTF8='1',PYTHONDONTWRITEBYTECODE='1',PSU_KNOWLEDGE_DB=str(B/(mode+'.sqlite')),PSU_BILINGUAL_EN_ENABLED='1',PSU_LOCAL_LLM_ASSIST_ENABLED='1' if llm else '0',PSU_SEMANTIC_RETRIEVAL='1' if llm else '0',PSU_LLM_PREFLIGHT='0',PSU_PIPELINE_WARMUP='0',PSU_INPUT_QUALITY_GUARD_MODE='enforce',PSU_INPUT_QUALITY_REPEAT_POLICY='warn_and_continue',PSU_PRODUCT_BACKEND_TIMEOUT_SEC='20',PSU_PIPELINE_GLOBAL_TIMEOUT_SEC='19',PSU_INTENT_LLM_TIMEOUT_SEC='14',PSU_INTENT_LLM_NUM_CTX='1536',PSU_INTENT_LLM_NUM_PREDICT='18',PSU_CHAT_LOG_DIR=str(B/'runtime_logs'/mode),PSU_CHAT_LOG_SQLITE_PATH=str(B/'runtime_logs'/mode/'transcripts.sqlite'),OLLAMA_URL='http://127.0.0.1:11434',PSU_OLLAMA_KEEP_ALIVE='30m',PSU_EMBEDDING_KEEP_ALIVE='30m',PSU_LLM_MAX_CONCURRENCY='1')
 if db:os.environ['PSU_KNOWLEDGE_DB']=str(db)
 if mode=='common':activate_draft_view()

def activate_draft_view():
 from app.knowledge.common.store import CommonStore
 from app.knowledge.common.answer import title
 from app.knowledge.common.registry import CATALOG,value
 target=Path(os.environ['PSU_KNOWLEDGE_DB']).resolve();store=CommonStore(target)
 original_snapshot=CommonStore.snapshot;original_current=CommonStore.still_current
 snap=original_snapshot(store)
 with store.connect() as c:records=store.heads(c);sources={sid:pair[0] for sid,pair in store.sources(c).items()}
 names={rid:list(dict.fromkeys(r['aliases']['th']+r['aliases']['en']+[title(r,'th'),title(r,'en')])) for rid,r in records.items()}
 refs={};index=[]
 for rid,r in records.items():
  for spec in CATALOG[r['kind']]['fields']:
   v=value(r,spec['key'])
   if v is not None:index.append({'id':rid+':'+spec['key'],'record_id':rid,'field':spec['key'],'text':json.dumps(v,ensure_ascii=False)})
   if v is not None and spec['reference_kind']:
    for key in v if isinstance(v,list) else [v]:refs.setdefault(key,[]).append(rid)
 frozen={**snap,'active':'EVAL_DRAFT_ONLY','release':{'records':records,'names':names,'reverse_refs':refs,'text_index':index,'sources':sources},'allow_demo':False,'evaluation_draft_only':True}
 def snapshot(self):return frozen if self.path.resolve()==target else original_snapshot(self)
 def current(self,s):return original_snapshot(self)['epoch']==s['epoch'] if self.path.resolve()==target else original_current(self,s)
 CommonStore.snapshot=snapshot;CommonStore.still_current=current

def offline_booking():
 from app.booking import live_status
 from app.runtime import fast_answer
 from app.pipeline import bilingual_english
 def unavailable(d):return live_status._unavailable(d,'controlled full evaluation; no actual booking oracle',error_code='fixture_offline')
 live_status.get_live_booking_status=unavailable;fast_answer.get_live_booking_status=unavailable;bilingual_english.get_live_booking_status=unavailable

MODE='';LLM=False;GUARD=None
def init(mode,llm):
 global MODE,LLM,GUARD
 test_temp('backend_shared')
 MODE=mode;LLM=llm;configure(mode,llm);offline_booking()
 if mode=='common':equivalent_name_pruning()
 from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
 GUARD=RuntimeInputQualityGuard.from_environment()

def equivalent_name_pruning():
 """Exact candidate equivalence for named(): only ratios >= .88 are used.

 SequenceMatcher.quick_ratio() is an upper bound. Returning zero when the
 bound is below .88 cannot change acceptance, score, ordering or margin.
 Applies only to this evaluator's module binding, never production files.
 """
 from app.knowledge.common import answer as module
 from functools import lru_cache
 if not getattr(module.normal,'cache_info',None):module.normal=lru_cache(maxsize=32768)(module.normal)
 original=module.SequenceMatcher
 if getattr(original,'evaluation_pruning',False):return
 class Pruned(original):
  evaluation_pruning=True
  def ratio(self):
   if self.real_quick_ratio()<.88:return 0.0
   if self.quick_ratio()<.88:return 0.0
   return super().ratio()
 module.SequenceMatcher=Pruned
 original_named=module.named
 @lru_cache(maxsize=1024)
 def memo_named(q,fingerprint,allow_fuzzy):
  return uncached_named(q,dict(fingerprint),allow_fuzzy=allow_fuzzy)
 import re,collections
 def uncached_named(q,names,*,allow_fuzzy=True):
  ids,method=original_named(q,names,allow_fuzzy=False)
  if ids or not allow_fuzzy:return ids,method
  q=module.normal(q);candidates=[];qcounts=collections.Counter(q);windows={}
  for rid,aliases in names.items():
   score=0
   for alias in aliases:
    a=module.normal(alias)
    if len(a)<5:continue
    digits=re.findall(r'\d+',a);matcher=Pruned(None,'',a)
    acounts=collections.Counter(a);max_matches=sum(min(n,qcounts[c]) for c,n in acounts.items())
    if 2.0*max_matches/(2*len(a)-1)<.88:continue
    for size in (len(a)-1,len(a),len(a)+1):
     if size not in windows:
      grouped={}
      for i in range(max(0,len(q)-size+1)):
       span=q[i:i+size]
       if (i>0 and q[i-1].isdigit() and span[:1].isdigit()) or (i+size<len(q) and q[i+size].isdigit() and span[-1:].isdigit()):continue
       grouped.setdefault(tuple(re.findall(r'\d+',span)),[]).append((i,span))
      windows[size]=grouped
     for i,span in windows[size].get(tuple(digits),[]):
      if re.search('[a-z]',a):
       if i and q[i-1].isascii() and q[i-1].isalnum():continue
       if i+size<len(q) and q[i+size].isascii() and q[i+size].isalnum():continue
      matcher.set_seq1(span);s=matcher.ratio()
      if s>=.88:score=max(score,s)
   if score:candidates.append((score,rid))
  candidates.sort(reverse=True)
  if candidates and (len(candidates)==1 or candidates[0][0]-candidates[1][0]>=.06):return [candidates[0][1]],'bounded_fuzzy'
  return [],'none'
 def cached_named(q,names,*,allow_fuzzy=True):
  fingerprint=tuple((rid,tuple(aliases)) for rid,aliases in names.items())
  ids,method=memo_named(q,fingerprint,allow_fuzzy)
  return list(ids),method
 module.named=cached_named

def run(job,history=None):
 from app.pipeline.engine import answer_question_pipeline_debug
 from app.core.locale import resolve_locale
 from app.pipeline.input_recovery import inspect_surface_input
 from app.pipeline.schemas import PipelineAnswer,PipelineRoute,EntityBundle,ValidationResult
 from app.pipeline.request_deadline import request_deadline
 from unittest.mock import patch
 from datetime import date
 q=job['question'];start=time.perf_counter();quality=GUARD.inspect(q);surface=inspect_surface_input(q)
 locale=resolve_locale(q,requested=job['locale'],keyboard_layout_direction=quality.locale_layout_direction,surface_language=surface.language if surface.should_review_intent else None)
 if quality.should_short_circuit:
  answer=('The keyboard layout may not match the language you intended. Please check the keyboard language and type the question again.' if locale.effective=='en' else quality.message)
  result=PipelineAnswer(answer=answer,hits=[],elapsed=time.perf_counter()-start,mode=quality.mode,confidence=0.0,route=PipelineRoute('input_guard',quality.flags[0] if quality.flags else 'input_quality',0.0,'clarification','low','input guard'),entities=EntityBundle(),validation=ValidationResult(True))
 else:
  kwargs=dict(locale=job['locale'],locale_decision=locale,experimental_allow_llm=LLM,experimental_rag_fallback=True,global_timeout_sec=19,recent_history=history or [])
  if job.get('reference_date'):
   with patch('app.booking.live_status.today_bangkok',return_value=date.fromisoformat(job['reference_date'])):result=answer_question_pipeline_debug(q,**kwargs)
  else:result=answer_question_pipeline_debug(q,**kwargs)
 return result,quality,locale,time.perf_counter()-start

def execute(job):
 from grade_legacy import grade,plain
 start=time.perf_counter()
 try:
  result,quality,locale,elapsed=run(job)
  grades=[]
  for entry in job['entries']:
   try:g=grade(entry['case'],result,Path(entry['file']).name)
   except Exception as error:g={'passed':False,'failures':['grader_exception:'+type(error).__name__+':'+str(error)],'evidence_level':'grader_error'}
   protocol=[];content=[];performance=[]
   for e in g['failures']:
    if e.startswith(('route:','intent:','legacy_mode_prefix:','status:','forbidden_category')):protocol.append(e)
    elif e=='latency_ceiling':performance.append(e)
    else:content.append(e)
   asserted=g['evidence_level'] not in {'route_outcome_only','grader_error'}
   grades.append({'file':entry['file'],'row':entry['row'],'variant':entry['variant'],'id':entry['case'].get('id'),**g,'protocol_failures':protocol,'content_failures':content,'performance_failures':performance,'content_asserted':asserted,'content_checks_passed':not content if asserted else None})
  response=plain(result)
  response['evaluation']={'mode':MODE,'llm_enabled':LLM,'common_draft_only':MODE=='common','no_actual_publication':True,'booking_fixture':'unavailable','worker_supervisor':False}
  return {'key':job['key'],'question':job['question'],'requested_locale':job['locale'],'effective_locale':locale.effective,'elapsed_wall':elapsed,'result':response,'input_quality':quality.to_public_dict(),'grades':grades}
 except Exception as e:
  return {'key':job['key'],'question':job['question'],'requested_locale':job['locale'],'elapsed_wall':time.perf_counter()-start,'exception':type(e).__name__+':'+str(e),'grades':[{'file':x['file'],'row':x['row'],'variant':x['variant'],'passed':False,'failures':['pipeline_exception'],'content_checks_passed':False,'content_asserted':False} for x in job['entries']]}
