import io,json,os,sys,time
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
from app.knowledge.common.domain_flow.model_gateway import call,legacy_open,digest,ModelBudgetExhausted
from app.knowledge.common.flow_context import request_context
from app.pipeline.llm_health import record_llm_failure
import urllib.request
OUT=R/('gateway_verification_'+str(time.time_ns()));OUT.mkdir();checks={};requests=[]
def http(req,timeout):
 p=json.loads(req.data);requests.append(p);profile=p['planner_profile']
 return io.BytesIO(json.dumps({'model':p['model'],'message':{'content':'{"ok":true}'},'provenance':{'serving_protocol':'r129-multi-profile-v2','effective_profile':profile,'effective_messages_sha256':digest(p['messages']),'effective_schema_sha256':digest(p.get('format'))}}).encode())
with request_context() as ctx,patch('urllib.request.urlopen',http),patch('app.pipeline.llm_health.llm_call_allowed',return_value=(True,{})),patch('app.pipeline.llm_health.record_llm_success'),patch('app.pipeline.llm_health.release_llm_slot'):
 os.environ['PSU_PLANNER_PROFILE']='new';client=SimpleNamespace(model='fixture:latest',timeout=10,admission={},http_attempted=False)
 payload={'model':client.model,'stage':'context_understanding','messages':[{'role':'user','content':'test quotation only'}],'format':{'type':'object'}}
 r=call(client,payload);checks['context_uses_explicit_selected_profile']=r['provenance']['effective_profile']=='new'
 data={'model':client.model,'system':'source selection only','prompt':'input quotation','format':'json','stream':True}
 req=urllib.request.Request('http://127.0.0.1:12921/api/generate',data=json.dumps(data).encode())
 r=json.loads(legacy_open(req,timeout=10,stage='source_selector').readline());checks['legacy_stream_envelope_preserved']=r['response']=='{"ok":true}'
 checks['non_context_always_base']=requests[-1]['planner_profile']=='base' and requests[-1]['stage']=='source_selector'
 try:call(client,payload);checks['third_call_rejected_before_http']=False
 except ModelBudgetExhausted:checks['third_call_rejected_before_http']=len(requests)==2
 checks['shared_budget_records_two_calls']=ctx.model_calls_reserved==2
 checks['actual_messages_and_schema_receipts']=all(e.get('wire_messages_sha256') for e in ctx.events if e['stage']=='R129_model_gateway')
 h=record_llm_failure('test','fixture:latest',error_type='ModelBudgetExhausted',error='request_model_budget_exhausted',elapsed_ms=0)
 checks['budget_exhaustion_does_not_poison_transport_health']=h.get('model_health_updated') is False
with request_context(),patch('urllib.request.urlopen',lambda *a,**k:io.BytesIO(b'{"model":"wrong","message":{"content":"{}"}}')),patch('app.pipeline.llm_health.llm_call_allowed',return_value=(True,{})),patch('app.pipeline.llm_health.record_llm_failure'),patch('app.pipeline.llm_health.release_llm_slot'):
 try:call(client,payload);checks['forged_model_identity_rejected']=False
 except ValueError:checks['forged_model_identity_rejected']=True
result={'all_passed':all(checks.values()),'checks':checks,'actual_network_calls':0,'actual_model_inferences':0};(OUT/'RESULT.json').write_text(json.dumps(result,indent=2),'utf8');print(json.dumps(result));assert result['all_passed']
