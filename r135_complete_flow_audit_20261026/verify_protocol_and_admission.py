"""Contract and admission regression tests without inference or network."""
import copy,json,sys,time
from unittest.mock import patch
from verification_support import R
sys.path.insert(0,str(R.parent/'r132_flow_repairs_20261025/vendor')) # test-only grammar dependency; no server activation claimed
from lmformatenforcer import JsonSchemaParser
from lmformatenforcer.characterlevelparser import CharacterLevelParserConfig
from app.knowledge.common.domain_flow.understanding import schema,parse
from app.knowledge.common.domain_flow.model import output_schema
from app.knowledge.common.domain_flow.rule_semantics import substantive
from app.knowledge.common.flow_context import request_context
from app.knowledge.common.domain_flow.model_gateway import call
from app.knowledge.common.domain_flow.model import EvidenceSelector
from app.pipeline import llm_health

checks=[]
def check(name,result):
 checks.append({'name':name,'passed':bool(result)})
 assert result,name
def accepts(schema_value,value):
 config=CharacterLevelParserConfig()
 config.alphabet+=''.join(chr(c) for c in range(0x0e00,0x0e80))
 p=JsonSchemaParser(schema_value,config=config)
 try:
  encoded=json.dumps(value,ensure_ascii=False,separators=(',',':'))
  for pos,ch in enumerate(encoded):
   if ch not in p.get_allowed_characters():
    print(json.dumps({'grammar_reject_at':pos,'char':ch,'context':encoded[max(0,pos-35):pos+20],'allowed_prefix':p.get_allowed_characters()[:100]},ensure_ascii=False))
    return False
   p=p.add_character(ch)
  return p.can_end()
 except Exception:return False
q='เครื่อง PC ใช้การ์ดจอรุ่นอะไร'
wire={'version':'r129-plan-v2','focus':'hardware','context_quotes':[],'tasks':[{'id':'t1','quote':q,'domain':'equipment','operation':'detail','facet':'specifications','target':'PC','constraints':[],'ambiguous':False}],'shared_bindings':[]}
check('graph_schema_accepts_complete_bound_json',accepts(schema(),wire))
check('runtime_parser_accepts_same_valid_wire',parse(json.dumps(wire,ensure_ascii=False),q).accepted)
check('schema_rejects_wrong_version',not accepts(schema(),{**wire,'version':'wrong'}))
check('schema_rejects_hybrid_root',not accepts(schema(),{**wire,'answer':'invented'}))
invented=json.loads(json.dumps(wire));invented['tasks'][0]['quote']='not in the request'
check('semantic_quote_guard_still_rejects_valid_json',not parse(json.dumps(invented),q).accepted)
legacy_surface=copy.deepcopy(wire);legacy_surface['tasks'][0]['id']='1';legacy_surface['constraints']=[]
original=copy.deepcopy(legacy_surface);converted=parse(json.dumps(legacy_surface,ensure_ascii=False),q)
check('lossless_surface_bijection_accepts_without_changing_source_fields',converted.accepted and converted.tasks[0].quote==q and converted.tasks[0].target=='PC' and converted.event.get('semantic_fields_changed') is False)
check('surface_adapter_preserves_original_raw_object',legacy_surface==original)
scoped=copy.deepcopy(legacy_surface);scoped['constraints']=[{'slot':'audience','quote':'invented'}]
check('nonempty_root_constraints_cannot_be_silently_dropped',not parse(json.dumps(scoped),q).accepted)
extra=copy.deepcopy(legacy_surface);extra['answer']='invented'
check('other_unknown_root_fields_still_rejected',not parse(json.dumps(extra),q).accepted)
bad_target=copy.deepcopy(legacy_surface);bad_target['tasks'][0]['target']='local_date'
check('surface_adapter_does_not_repair_invented_target',not parse(json.dumps(bad_target,ensure_ascii=False),q).accepted)
duplicate=copy.deepcopy(legacy_surface);duplicate['tasks'].append(copy.deepcopy(duplicate['tasks'][0]))
check('surface_adapter_rejects_duplicate_task_ids',not parse(json.dumps(duplicate,ensure_ascii=False),q).accepted)
cycle=copy.deepcopy(legacy_surface);cycle['shared_bindings']=[{'source_task_id':'1','target_task_id':'1','slot':'target','quote':'PC','basis':'explicit_anaphor'}]
check('renamed_self_cycle_still_rejected',not parse(json.dumps(cycle,ensure_ascii=False),q).accepted)
check('selector_schema_accepts_only_indexed_choices',accepts(output_schema(1,24),{'plans':[{'i':0,'choices':[1]}]}))
check('selector_schema_rejects_input_echo',not accepts(output_schema(1,24),{'question':q}))
check('complete_rule_may_equal_heading',substantive('All software or hardware macros are strictly prohibited.',['All software or hardware macros are strictly prohibited.']))
check('allowed_equipment_heading_is_not_substantive',not substantive('Allowed equipment',['Allowed equipment']))
check('overview_title_is_not_substantive',not substantive('Competition rules and format for the event',['Overview of Documents']))
client=EvidenceSelector();payload={'messages':[{'role':'user','content':q}],'stage':'context_understanding'}
with request_context() as ctx,patch.object(llm_health,'llm_call_allowed',return_value=(False,{'llm_concurrency_allowed':False})),patch('urllib.request.urlopen') as network:
 try:call(client,payload)
 except OSError as e:check('busy_is_reported_as_admission_unavailable',str(e)=='model_admission_unavailable')
 check('busy_consumes_no_context_call_reservation',ctx.model_calls_reserved==0)
 check('busy_performs_no_http',not network.called)
with patch.object(llm_health,'llm_health_enabled',return_value=False),patch.object(llm_health,'_acquire_llm_slot',return_value=(False,{'llm_concurrency_allowed':False})),patch.object(llm_health,'reserve_llm_call') as reserve:
 check('health_gate_denies_busy',not llm_health.llm_call_allowed('test','test')[0])
 check('busy_consumes_no_pipeline_call_budget',not reserve.called)
with patch.object(llm_health,'llm_health_enabled',return_value=False),patch.object(llm_health,'_acquire_llm_slot',return_value=(True,{'llm_concurrency_allowed':True})),patch.object(llm_health,'reserve_llm_call',return_value=(False,{})),patch.object(llm_health,'release_llm_slot') as release:
 check('exhausted_budget_releases_acquired_slot',not llm_health.llm_call_allowed('test','test')[0] and release.call_count==1)
out={'checks':checks,'passed':all(x['passed'] for x in checks),'inferences':0,'network_calls':0,'completed_at':time.time()}
(R/'PROTOCOL_ADMISSION_VERIFICATION.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'passed':out['passed'],'checks':len(checks),'inferences':0}))
