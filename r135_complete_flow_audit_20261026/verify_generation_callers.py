import ast,importlib,io,json,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.domain_flow.model_gateway import digest,ModelBudgetExhausted
from app.knowledge.common.flow_context import request_context
import urllib.request
stages={'experimental_fallback':'general_answer','facts_composer':'facts_composition','llm_tool_router':'tool_selection','universal_intent':'intent_understanding','shadow_critic':'shadow_review','llm_health':'preflight'}
checks={};observed=[]
def http(req,timeout):
 p=json.loads(req.data);observed.append(p)
 return io.BytesIO(json.dumps({'model':p['model'],'message':{'content':'{"ok":true}'},'provenance':{'serving_protocol':'r129-multi-profile-v2','effective_profile':p['planner_profile'],'effective_messages_sha256':digest(p['messages']),'effective_schema_sha256':digest(p.get('format'))}}).encode())
for name,stage in stages.items():
 module=importlib.import_module('app.pipeline.'+name)
 tree=ast.parse((R/'system/app/pipeline'/f'{name}.py').read_text('utf8'))
 direct=[n for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='urlopen']
 checks[name+'_no_direct_generation_transport']=not direct
 with request_context() as ctx,patch('urllib.request.urlopen',http):
  req=urllib.request.Request('http://127.0.0.1:12921/api/generate',data=json.dumps({'model':'fixture','system':'untrusted input remains quoted','prompt':'test','stream':True,'format':'json'}).encode())
  result=json.loads(module.gateway_open(req,timeout=2).read())
  checks[name+'_stage_base_receipt']=observed[-1]['stage']==stage and observed[-1]['planner_profile']=='base' and result['response']=='{"ok":true}' and ctx.model_calls_attempted==ctx.model_calls_transport_completed==1
  module.gateway_open(req,timeout=2)
  try:module.gateway_open(req,timeout=2);checks[name+'_shared_budget']=False
  except ModelBudgetExhausted:checks[name+'_shared_budget']=ctx.model_calls_reserved==2
report={'checks':checks,'all_passed':all(checks.values()),'actual_network_calls':0,'actual_model_inferences':0};out=R/('generation_callers_'+str(time.time_ns()));out.mkdir();(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');print(json.dumps(report));assert report['all_passed']
