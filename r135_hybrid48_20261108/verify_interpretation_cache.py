import copy,json,os,time
from unittest.mock import patch
from verification_support import R,index
from app.knowledge.common.domain_flow import understanding as u
from app.knowledge.common.domain_flow.context_guard import apply
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.contracts import RequestBudget
idx=index();q='ราคา VR 30 นาที เทียบ 1 ชั่วโมง แล้วจองยังไง'
original=u.Understanding([u.MeaningTask('ราคา VR 30 นาที เทียบ 1 ชั่วโมง','service_fee','C06','compare','duration_minutes',target='VR'),u.MeaningTask('แล้วจองยังไง','reservation','C08','detail','owner_policy')],True,'controlled_cache_source',{'wire_version':'r129-plan-v2','proposed_shared_bindings':[{'source_task_id':'t1','target_task_id':'t2','slot':'target','quote':'VR','basis':'source_related_ellipsis'}],'model_provenance':{'effective_profile':'retained','profile_digest':'fixture-only'},'transport_ok':True,'schema_ok':True})
original=apply(q,idx,original);snap={'release_id':'fixture','epoch':1,'reference_time':'2026-10-26T12:00:00+07:00'}
checks={};calls=[]
def inferred(*args,**kwargs):calls.append(os.getenv('PSU_PLANNER_PROFILE'));return copy.deepcopy(original)
with patch.dict(os.environ,{'PSU_PLANNER_PROFILE':'retained','OLLAMA_URL':'http://127.0.0.1:12921'}),patch.object(u,'_interpret_uncached',inferred):
 a=u.interpret(q,RequestBudget(),index=idx);budget=RequestBudget();b=u.interpret(q,budget,index=idx)
 checks['same_profile_reuses_without_new_inference']=len(calls)==1 and b.event['cache_hit'] and budget.model_calls==0
 checks['cache_preserves_graph_bindings_and_wire']=b.event['proposed_shared_bindings']==a.event['proposed_shared_bindings'] and b.event['wire_version']==a.event['wire_version']
 ca=compile_request(q,apply(q,idx,a),idx,snap);cb=compile_request(q,apply(q,idx,b),idx,snap)
 checks['cached_plan_keeps_booking_service_binding']=[t.bindings for t in ca.tasks]==[t.bindings for t in cb.tasks] and cb.tasks[1].target_span.text=='VR'
 checks['origin_receipt_not_claimed_fresh_transport']=b.event['cached_origin_receipt']['model_provenance']==a.event['model_provenance'] and not b.event['transport_ok'] and not b.event['fresh_model_inference_claimed']
 checks['cache_hit_recorded_in_request_audit']=len(budget.events)==1 and budget.events[0]['cache_hit']
 os.environ['PSU_PLANNER_PROFILE']='new';u.interpret(q,RequestBudget(),index=idx);checks['profile_change_invalidates_cache']=len(calls)==2
 os.environ['OLLAMA_URL']='http://127.0.0.1:13521';u.interpret(q,RequestBudget(),index=idx);checks['backend_change_invalidates_cache']=len(calls)==3
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'real_source_changes':0};out=R/('interpretation_cache_'+str(time.time_ns()));out.mkdir();(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');print(json.dumps(report));assert report['all_passed']
