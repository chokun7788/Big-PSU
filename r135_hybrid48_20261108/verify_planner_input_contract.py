"""Malformed planner proposals are rejected as data, never request errors."""
import copy,json,time
from verification_support import R
from app.knowledge.common.domain_flow.understanding import parse
out=R/('planner_input_contract_'+str(time.time_ns()));out.mkdir();q='ราคา PC 30 นาที';checks={};details={}
valid={'version':'r129-plan-v2','focus':'price','context_quotes':[],'tasks':[{'id':'t1','quote':q,'domain':'service_fee','operation':'detail','facet':'amount','target':'PC','constraints':[{'slot':'duration','quote':'30 นาที','source_record_id':'','scope':'local'}],'ambiguous':False}],'shared_bindings':[]}
checks['valid_exact_source_plan_accepted']=parse(json.dumps(valid,ensure_ascii=False),q).accepted
def rejected(name,value):
 try:
  result=parse(value if isinstance(value,str) else json.dumps(value,ensure_ascii=False),q);checks[name]=not result.accepted;details[name]={'reason':result.reason,'accepted':result.accepted}
 except Exception as e:checks[name]=False;details[name]={'raised':type(e).__name__}
for label,path,value in [('domain_object',('tasks',0,'domain'),{}),('domain_list',('tasks',0,'domain'),['service_fee']),('unbound_target',('tasks',0,'target'),'invented resource'),('business_value',('tasks',0,'price'),0),('unsupported_operation',('tasks',0,'operation'),'execute_sql'),('wrong_schema_version',('version',),'invented-plan-v9'),('unbound_slot',('tasks',0,'constraints',0,'quote'),'999 invented minutes'),('invented_source_id',('tasks',0,'constraints',0,'source_record_id'),'not_in_snapshot')]:
 bad=copy.deepcopy(valid);parent=bad
 for key in path[:-1]:parent=parent[key]
 parent[path[-1]]=value;rejected(label+'_rejected_without_exception',bad)
bad=copy.deepcopy(valid);bad['tasks'].append(copy.deepcopy(bad['tasks'][0]));rejected('duplicate_task_id_rejected',bad)
rejected('duplicate_root_key_rejected',json.dumps(valid,ensure_ascii=False)[:-1]+',"focus":"price"}')
rejected('deep_json_rejected_without_recursion_error','['*1500+'0'+']'*1500)
rejected('oversized_payload_rejected_before_parse',json.dumps(valid,ensure_ascii=False)+' '*140000)
bad=copy.deepcopy(valid);bad['tasks'][0]['quote']='ราคา PC';bad['tasks'][0]['constraints']=[];rejected('dropped_numeric_condition_rejected',bad)
bad=copy.deepcopy(valid);bad['confidence']=1;rejected('self_reported_confidence_not_a_root_authority',bad)
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from unittest.mock import patch
# Use a normal source engine; the registered unsupported combination must be
# rejected before any reader or selector can approximate it with a detail call.
from verification_support import snapshot
engine=Engine.from_snapshot(snapshot());proposal=Understanding([MeaningTask(q,'service_fee','C06','list','amount','PC')],True,'controlled_unsupported_combination',{'model_called':False})
with patch.object(engine,'plan',side_effect=AssertionError('unsupported operation reached a reader')):
 result=engine.answer(q,'th',at='2026-10-26T12:00:00+07:00',allow_llm=False,understanding=proposal)
checks['registered_but_unsupported_pair_does_not_fall_back_to_detail']=not result['claims'] and any(n['reason']=='unsupported_operation' for n in result['needs'])
report={'all_passed':all(checks.values()),'checks':checks,'details':details,'actual_model_inferences':0,'user_data_modified':False,'semantic_correctness_not_inferred_from_valid_json':True};(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
