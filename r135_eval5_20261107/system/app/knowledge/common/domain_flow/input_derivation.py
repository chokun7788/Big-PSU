"""Executable raw-input boundary; an audit tag alone grants no authority."""
import copy,hashlib,re
from ..flow_context import CURRENT
from ..normalized_query import normalize_query

def fingerprint(raw):return hashlib.sha256(raw.encode('utf8')).hexdigest()

def check(question):
 ctx=CURRENT.get();raw=ctx.input.get('raw_question') if ctx else None
 if not isinstance(raw,str):return {'verified':False,'reason':'raw_input_not_bound'}
 if question==raw:return {'verified':True,'basis':'exact_current_raw'}
 if question==normalize_query(raw).text:return {'verified':True,'basis':'deterministic_input_normalization'}
 receipt=ctx.validated_derivations.get(question)
 if receipt and receipt.get('raw_sha256')==fingerprint(raw):
  source=receipt.get('source_snapshot')
  if source and any(source.get(k)!=ctx.snapshot.get(k) for k in ['release_id','epoch']):return {'verified':False,'reason':'derivation_source_snapshot_changed'}
  if receipt.get('source_manifest_sha256') and receipt['source_manifest_sha256']!=ctx.snapshot.get('manifest_sha256'):return {'verified':False,'reason':'derivation_source_manifest_changed'}
  return {'verified':True,'basis':receipt['kind'],'receipt':copy.deepcopy(receipt)}
 return {'verified':False,'reason':'execution_text_has_no_validated_derivation'}

def live_resume(index,question,history):
 from ..followup_scope import delivered_state
 from .scope import contains,norm,requested_resources,canonical_resource
 from .projection import title
 pending=(delivered_state(history) or {}).get('live_scope_pending')
 if not isinstance(pending,dict) or pending.get('version')!=1 or len(question)>=80 or not isinstance(pending.get('query'),str) or len(pending['query'])>2000:return None
 labels=[label for r in index.records.values() if r['kind'] in {'zone','resource','service'} for label in [*title(r).values(),*sum(r.get('aliases',{}).values(),[])] if contains(question,label)]
 reply=re.sub(r'\s*(?:ครับ|ค่ะ|[?!.,])+\s*$','',norm(question)).strip();resources=requested_resources(reply)
 native=any(r['kind']=='resource' and any(canonical_resource(asked)==canonical_resource(label) for asked in resources for label in [*title(r).values(),*sum(r.get('aliases',{}).values(),[])]) for r in index.records.values())
 if any(reply==norm(label) for label in labels) or native and len(resources)==1 and canonical_resource(reply)==canonical_resource(next(iter(resources))):return pending['query']+' '+question
 return None

def register(question,kind,segments,index=None,history=None,**detail):
 ctx=CURRENT.get();proof={'verified':False,'reason':'unregistered_or_unverified_transform','kind':kind}
 if ctx is None:return proof
 parent=detail.get('parent_question')
 try:
  valid=False
  if kind=='r128_delivered_task_resolution' and index is not None:
   resolution=ctx.input.get('dialogue_resolution') or {};parent=resolution.get('original_question')
   if isinstance(parent,str) and check(parent)['verified']:
    from .dialogue_task import resolve
    expected=resolve(index,parent,history,(ctx.snapshot or {}).get('release_id'),ctx.pin_reference_time())
    valid=expected['execution_question']==question
  elif kind=='calendar_date_resolution' and index is not None:
   parent=parent if isinstance(parent,str) else segments[0].get('text') if segments else None
   if isinstance(parent,str) and check(parent)['verified']:
    from .date_context import resolve
    expected=resolve(parent,ctx.pin_reference_time(),history)
    valid=bool(expected and expected.get('status')=='resolved' and expected.get('query')==question)
  elif kind=='delivered_financial_resume' and index is not None:
   parent=next((s.get('text') for s in segments if s.get('origin')=='current_user_reply'),None)
   if isinstance(parent,str) and check(parent)['verified']:
    from .financial import resume_financial
    valid=resume_financial(parent,history,index.records)==question
  elif kind=='delivered_live_resume' and index is not None:
   if isinstance(parent,str) and check(parent)['verified']:valid=live_resume(index,parent,history)==question
  elif kind in {'compiled_parent_task','native_typed_fallback_revisit'}:
   if isinstance(parent,str) and check(parent)['verified'] and segments:
    source=segments[0].get('source_span') or {};a,b=source.get('start'),source.get('end');text=source.get('text')
    valid=type(a) is int and type(b) is int and 0<=a<b<=len(parent) and parent[a:b]==text
    pieces=[]
    for segment in segments[1:]:
     binding=segment.get('binding') or {};span=binding.get('source_span') or {};a,b=span.get('start'),span.get('end');value=span.get('text')
     if type(a) is not int or type(b) is not int or not 0<=a<b<=len(parent) or parent[a:b]!=value or binding.get('validation_outcome','validated')!='validated':valid=False;break
     if value not in text and value not in pieces:pieces.append(value)
    valid=valid and question==(text+' '+ ' '.join(pieces)).strip()
  elif kind=='native_clause_split' and index is not None:
   if isinstance(parent,str) and check(parent)['verified']:
    from .routing import split_needs
    valid=question in split_needs(parent,index)
  elif kind=='explicit_request_focus':
   if isinstance(parent,str) and check(parent)['verified']:
    from app.pipeline.request_focus import explicit_request_focus
    valid=explicit_request_focus(parent)[0]==question
  elif kind in {'native_request_plan_query','native_surface_canonical'} and index is not None:
   if isinstance(parent,str) and check(parent)['verified']:
    from ..query_scope import derived_names
    from .projection import title
    names=derived_names({rid:[*title(r).values(),*sum(r.get('aliases',{}).values(),[])] for rid,r in index.records.items()},index.records)
    if kind=='native_surface_canonical':
     from ..interpret_surface import canonical
     valid=canonical(parent,index.records,names)==question
    else:
     from ..request_plan import make_plan
     plan=make_plan(parent,index.records,names,history,split=True)
     valid=any(n.query==question for n in plan.needs)
  if valid:
   proof={'verified':True,'kind':kind,'parent_question':parent,'raw_sha256':fingerprint(ctx.input['raw_question']),'semantic_correctness_claimed':False}
   if index is not None:proof.update(source_snapshot=copy.deepcopy(index.snapshot_identity),source_manifest_sha256=ctx.snapshot.get('manifest_sha256'))
   ctx.validated_derivations[question]=copy.deepcopy(proof)
 except (ValueError,TypeError,KeyError,AttributeError,IndexError) as exc:proof['validation_error_type']=type(exc).__name__
 return proof

def reject_for_reader(reader,question,locale,at=None,snapshot=None):
 """Return the same no-claims executor contract for normal/native callers."""
 import time
 from .engine import Engine
 from .integration import package
 from .task_execution import input_rejection
 snap=snapshot if snapshot is not None else reader.store.snapshot()
 if not snap.get('release'):
  from dataclasses import replace
  from .result_contract import attach_runtime
  from .engine import language
  result=reader.finish(snap,time.perf_counter(),'ยังยืนยันการตีความคำถามนี้ไม่ได้ กรุณาระบุคำถามอีกครั้งครับ' if language(question,locale)=='th' else 'The request interpretation could not be verified. Please restate the question.',[],{'record_ids':[],'requested_fields':[],'method':'invalid_compiled_input_derivation'},[],response='unconfirmed')
  result=replace(result,decision_artifact={**result.decision_artifact,'execution_contract':{'path':'invalid_compiled_plan','input_derivation_validation':check(question)}})
  result=attach_runtime(result,{'execution_question':question,'requested_locale':locale,'effective_locale':language(question,locale)},snap)
  result.decision_artifact['execution_contract']['path']='input_derivation_guard'
  return result
 engine=Engine.from_snapshot(snap,cache_key=reader.store.path)
 return package(reader,snap,time.perf_counter(),question,input_rejection(engine,question,locale,CURRENT.get().pin_reference_time(at),check(question)))
