"""Shared admission, deadline, stage/profile and transport receipts."""
import hashlib,json,os,time,urllib.request
import io

class ModelBudgetExhausted(OSError):pass

def digest(value):return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def call(client,payload):
 from app.pipeline.llm_health import llm_call_allowed,record_llm_success,record_llm_failure,release_llm_slot
 from app.pipeline.request_deadline import timeout_for_call
 from ..flow_context import CURRENT
 stage=payload.get('stage') or 'evidence_selection';requested_profile=os.getenv('PSU_PLANNER_PROFILE','retained') if stage=='context_understanding' else 'base'
 ctx=CURRENT.get()
 from ..bounded_time import timeout as analysis_timeout
 if analysis_timeout(client.timeout)<=0:raise ModelBudgetExhausted('analysis_time_budget_exhausted')
 payload={**payload,'stage':stage,'planner_profile':requested_profile}
 allowed,client.admission=llm_call_allowed('r129_'+stage,client.model)
 if not allowed:
  if ctx:ctx.event('model_admission_denied',model_stage=stage,admission=client.admission,http_attempted=False,reservation_consumed=False)
  raise OSError('model_admission_unavailable')
 if ctx and not ctx.reserve_model(stage):
  release_llm_slot()
  raise ModelBudgetExhausted('request_model_budget_exhausted')
 ctx=CURRENT.get();started=time.monotonic();receipt={'stage':'R129_model_gateway','model_stage':stage,'profile':requested_profile,'wire_messages_sha256':digest(payload['messages']),'schema_sha256':digest(payload.get('format')),'model':client.model,'transport_ok':False}
 try:
  timeout=analysis_timeout(timeout_for_call(client.timeout))
  if timeout<=0:raise TimeoutError('request_deadline_exhausted')
  margin=2.0 if stage in {'model_first_plan','context_understanding'} else 0.0
  if margin and timeout<=margin+1:raise ModelBudgetExhausted('server_finalizer_budget_unavailable')
  payload['request_timeout_sec']=timeout-margin
  req=urllib.request.Request(os.environ.get('OLLAMA_URL','http://127.0.0.1:11434').rstrip('/')+'/api/chat',data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
  client.http_attempted=True
  if ctx:ctx.model_calls_attempted+=1
  with urllib.request.urlopen(req,timeout=timeout) as response:result=json.load(response)
  receipt['returned_model']=result.get('model')
  if result.get('model')!=client.model:raise ValueError('model_identity_mismatch')
  provenance=result.get('provenance',{});receipt['returned_provenance']=provenance
  if provenance.get('serving_protocol')=='r129-multi-profile-v2':
   if provenance.get('effective_messages_sha256')!=digest(payload['messages']):raise ValueError('effective_messages_mismatch')
   if provenance.get('effective_schema_sha256')!=digest(payload.get('format')):raise ValueError('effective_schema_mismatch')
   if provenance.get('effective_profile')!=requested_profile:raise ValueError('effective_profile_mismatch')
  receipt['transport_ok']=True
  if ctx:ctx.model_calls_transport_completed+=1
  record_llm_success('r129_'+stage,client.model,elapsed_ms=(time.monotonic()-started)*1000,detail='HTTP/identity verified; content assessed separately')
  return result
 except (OSError,ValueError) as exc:
  receipt['error']=type(exc).__name__+': '+str(exc)
  record_llm_failure('r129_'+stage,client.model,elapsed_ms=(time.monotonic()-started)*1000,error_type=type(exc).__name__,error=str(exc));raise
 finally:
  receipt['elapsed_seconds']=time.monotonic()-started
  if ctx:ctx.event(**receipt)
  release_llm_slot()

def legacy_open(request,timeout=60,stage='compatibility_base'):
 """Adapt existing bounded generate callers after their admission gate.

 Their parsers and schema checks stay in place. Every such call is base-only;
 context adapters cannot silently contaminate selector/renderer stages.
 """
 from ..flow_context import CURRENT
 from app.pipeline.request_deadline import timeout_for_call
 from app.pipeline.llm_health import has_llm_admission,llm_call_allowed,release_llm_slot,record_llm_success,record_llm_failure
 payload=json.loads(request.data);stage=payload.pop('_gateway_stage',stage)
 ctx=CURRENT.get()
 owned_admission=False
 from ..bounded_time import timeout as analysis_timeout
 if analysis_timeout(timeout)<=0:raise ModelBudgetExhausted('analysis_time_budget_exhausted')
 if not has_llm_admission():
  allowed,admission=llm_call_allowed('gateway_'+stage,payload['model'])
  if not allowed:
   if ctx:ctx.event('model_admission_denied',model_stage=stage,admission=admission,http_attempted=False,reservation_consumed=False)
   raise OSError('model_admission_unavailable')
  owned_admission=True
 if ctx and not ctx.reserve_model(stage):
  if owned_admission:release_llm_slot()
  raise ModelBudgetExhausted('request_model_budget_exhausted')
 wire=payload.get('messages') or ([{'role':'system','content':payload['system']}] if payload.get('system') else [])+[{'role':'user','content':payload.get('prompt','')}]
 envelope={**payload,'stage':stage,'planner_profile':'base','messages':wire,'stream':False,'request_timeout_sec':analysis_timeout(timeout_for_call(timeout))}
 receipt={'model_stage':stage,'profile':'base','requested_model':payload['model'],'wire_messages_sha256':digest(wire),'schema_sha256':digest(envelope.get('format')),'transport_ok':False,'admission':'gateway_owned_gate' if owned_admission else 'existing_caller_gate'};start=time.monotonic()
 try:
  if envelope['request_timeout_sec']<=0:raise TimeoutError('request_deadline_exhausted')
  from urllib.parse import urlsplit,urlunsplit
  endpoint=urlsplit(request.full_url)
  req=urllib.request.Request(urlunsplit((endpoint.scheme,endpoint.netloc,'/api/chat','','')),data=json.dumps(envelope).encode(),headers={'Content-Type':'application/json'})
  if ctx:ctx.model_calls_attempted+=1
  with urllib.request.urlopen(req,timeout=envelope['request_timeout_sec']) as response:result=json.load(response)
  receipt['returned_model']=result.get('model')
  if result.get('model')!=payload['model']:raise ValueError('model_identity_mismatch')
  prov=result.get('provenance',{});receipt['returned_provenance']=prov
  if prov.get('serving_protocol')=='r129-multi-profile-v2' and (prov.get('effective_profile')!='base' or prov.get('effective_messages_sha256')!=digest(wire) or prov.get('effective_schema_sha256')!=digest(envelope.get('format'))):raise ValueError('effective_base_wire_mismatch')
  result['response']=result.get('message',{}).get('content',result.get('response',''));receipt['transport_ok']=True
  if ctx:ctx.model_calls_transport_completed+=1
  if owned_admission:record_llm_success('gateway_'+stage,payload['model'],elapsed_ms=(time.monotonic()-start)*1000,detail='HTTP/model/base wire identity verified; content assessed separately')
  return io.BytesIO(json.dumps(result,ensure_ascii=False).encode()+b'\n')
 except (ValueError,OSError) as exc:
  receipt['error']=repr(exc)
  if owned_admission:record_llm_failure('gateway_'+stage,payload['model'],elapsed_ms=(time.monotonic()-start)*1000,error_type=type(exc).__name__,error=str(exc))
  raise
 finally:
  receipt['elapsed_seconds']=time.monotonic()-start
  if ctx:ctx.event('R129_model_gateway',**receipt)
  if owned_admission:release_llm_slot()
