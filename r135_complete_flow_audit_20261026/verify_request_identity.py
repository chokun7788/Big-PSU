"""One clock and explicit observed identities across nested request readers."""
import json,time,os
from datetime import datetime,timedelta
from unittest.mock import patch
from verification_support import R,snapshot
out=R/('request_identity_'+str(time.time_ns()));out.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'isolated_conversation.sqlite')
from app.knowledge.common.flow_context import request_context
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.request_provenance import capture
from app.knowledge.common.domain_flow.request_provenance import derived_input
snap=snapshot();checks={};results=[];ticks=[];start=datetime.fromisoformat('2026-10-26T23:59:59+07:00')
class View:
 path=R/'system/data/knowledge/common.sqlite'
 def snapshot(self):return snap
 def still_current(self,s):return s is snap
def clock():
 value=start+timedelta(seconds=len(ticks)*2);ticks.append(value);return value
with request_context() as ctx,patch('app.calendar.service_calendar.now_bangkok',clock),patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):
 ctx.input={'raw_question':'What is the studio address? Who operates the studio?','requested_locale':'en','effective_locale':'en'}
 first='What is the studio address?';second='Who operates the studio?';raw=ctx.input['raw_question']
 for text in [first,second]:derived_input(text,'compiled_parent_task',[{'origin':'current_question_task','source_span':{'start':raw.index(text),'end':raw.index(text)+len(text),'text':text}}],parent_question=raw)
 a=CommonAnswerer(View()).answer('What is the studio address?',locale='en',planner=None)
 b=CommonAnswerer(View()).answer('Who operates the studio?',locale='en',planner=None)
 results=[a,b];contexts=[r.decision_artifact['execution_contract']['request_context'] for r in results];times=[r.decision_artifact['execution_contract']['request_plan']['snapshot']['reference_time'] for r in results]
 checks['nested_readers_share_one_reference_timestamp']=len(set(times))==1
 public=ctx.public();identity=capture('Who operates the studio?')
 checks['request_id_exists_and_stays_same']=bool(ctx.request_id) and all(c['request_id']==ctx.request_id for c in contexts)
 checks['request_clock_includes_bangkok_timezone']=public.get('reference_time',{}).get('timezone')=='Asia/Bangkok' and public.get('reference_time',{}).get('pinned') is True
 checks['snapshot_manifest_names_actual_record_revisions']=public.get('snapshot',{}).get('record_revisions')=={rid:r['revision'] for rid,r in snap['release']['records'].items()}
 checks['snapshot_manifest_names_actual_source_digests']=public.get('snapshot',{}).get('source_revisions')=={sid:s.get('sha256') for sid,s in snap['release']['sources'].items()}
 checks['locale_is_explicit_in_bound_request_context']=identity.get('locale')=={'requested':'en','effective':'en'}
 checks['runtime_identity_recorded_without_model_name_inference']=bool(identity.get('runtime_identity',{}).get('build_id'))
 checks['typed_request_does_not_claim_observed_model_assets']=identity.get('model_profile',{}).get('state')=='not_called' and identity.get('model_profile',{}).get('observations')==[]
 for label,mutate in [('clock_rewrite',lambda:setattr(ctx,'reference_time_value',start+timedelta(days=1))),('request_id_rewrite',lambda:setattr(ctx,'request_id','changed'))]:
  try:mutate();checks[label+'_rejected']=False
  except ValueError:checks[label+'_rejected']=True
 try:ctx.pin_reference_time(start+timedelta(days=1));checks['different_nested_clock_not_silently_accepted']=False
 except ValueError:checks['different_nested_clock_not_silently_accepted']=True
with request_context() as utc:
 value=utc.pin_reference_time('2026-10-26T16:59:59Z');checks['explicit_utc_clock_converted_to_bangkok']=value.isoformat()==start.isoformat()
with request_context() as naive:
 try:naive.pin_reference_time(datetime(2026,10,26,12));checks['timezone_free_reference_rejected']=False
 except ValueError:checks['timezone_free_reference_rejected']=True
from dataclasses import dataclass
from app.pipeline.migrated_chat import answer as dispatch
from app.knowledge.common.flow_context import CURRENT
@dataclass
class EarlyResult:
 decision_artifact:dict
def early(*args,**kwargs):
 checks['dispatcher_pins_clock_before_any_subreader']=CURRENT.get().reference_time_value is not None
 return EarlyResult({'response_type':'unconfirmed'})
with patch('app.pipeline.migrated_chat._answer',early),patch('app.calendar.service_calendar.now_bangkok',clock):
 dispatched=dispatch('Controlled early return',locale=None,allow_llm=False,allow_live=False)
checks['early_return_still_has_pinned_request_clock']=dispatched.decision_artifact['request_context']['reference_time']['pinned']
import io
from types import SimpleNamespace
from app.knowledge.common.domain_flow.model_gateway import call,digest
def response(req,timeout):
 data=json.loads(req.data);provenance={'serving_protocol':'r129-multi-profile-v2','effective_profile':data['planner_profile'],'effective_messages_sha256':digest(data['messages']),'effective_schema_sha256':digest(data.get('format')),'base_revision':'controlled-base-revision','adapter_sha256':None,'quantization':'controlled-precision','profile_digest':'controlled-profile-digest'}
 return io.BytesIO(json.dumps({'model':data['model'],'message':{'content':'{}'},'provenance':provenance}).encode())
with request_context() as observed,patch('urllib.request.urlopen',response),patch('app.pipeline.llm_health.llm_call_allowed',return_value=(True,{})),patch('app.pipeline.llm_health.record_llm_success'),patch('app.pipeline.llm_health.record_llm_failure'),patch('app.pipeline.llm_health.release_llm_slot'):
 client=SimpleNamespace(model='controlled:latest',timeout=10,admission={},http_attempted=False);payload={'model':client.model,'stage':'evidence_selection','messages':[{'role':'user','content':'Controlled quote'}],'format':{'type':'object'}}
 call(client,payload);proof=observed.identity()['model_profile']['observations'][0]
 checks['actual_returned_name_and_asset_receipt_kept_separate_from_alias']=proof['returned_model']==client.model and proof['response_model_name_verified'] and proof['returned_provenance']['base_revision']=='controlled-base-revision' and proof['returned_provenance']['profile_digest']=='controlled-profile-digest'
 with patch('urllib.request.urlopen',lambda *a,**k:io.BytesIO(b'{"model":"controlled-wrong:latest","message":{"content":"{}"}}')):
  try:call(client,payload);checks['wrong_model_name_not_marked_verified']=False
  except ValueError:
   proof=observed.identity()['model_profile']['observations'][-1];checks['wrong_model_name_not_marked_verified']=proof['returned_model']=='controlled-wrong:latest' and not proof['response_model_name_verified'] and not proof['transport_ok']
report={'all_passed':all(checks.values()),'checks':checks,'observed_times':times,'actual_model_inferences':0,'user_data_modified':False,'final_model_asset_gate_claimed':False}
(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps({'public_context':public,'captured_context':identity,'contexts':contexts},ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
