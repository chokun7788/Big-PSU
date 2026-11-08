import copy,json,time
from verification_support import R,snapshot
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.request_verifier import observe,verify,supplement
from app.knowledge.common.domain_flow.scope import reference_time
e=Engine.from_snapshot(snapshot());idx=e.index;checks={};rows=[]
q='How much does PC cost and how do I book?'
broken=Understanding([MeaningTask(q,'service_fee','C06','price_calculate','amount')],True,'fixture_dropped_booking',{'model_called':False})
o=observe(idx,q);checks['detector_sees_need_absent_from_planner']={'C06','C08'}<={n['category'] for n in o['needs']}
fixed=supplement(idx,q,broken);checks['bounded_typed_correction_without_model']=len(fixed.tasks)>len(broken.tasks) and any(t.category=='C08' for t in fixed.tasks) and not any(x['model_called'] for x in fixed.event['typed_corrective_tasks'])
r=e.answer(q,'en',at=reference_time('2026-10-25T12:00:00+07:00'),allow_llm=False,understanding=broken);rows.append({'question':q,'result':r})
v=r['execution_contract']['verifier_result'];checks['omitted_booking_executed']=any(n['category']=='C08' and n['claims'] for n in r['needs'])
checks['five_distinct_verification_sections']=all(k in v for k in ['plan_coverage','constraint_coverage','execution_coverage','evidence_support','answer_coverage'])
checks['no_false_semantic_certificate']=v['whole_question_semantics_verified'] is False and v['observations']['detector_completeness_claimed'] is False
raw_contract=copy.deepcopy(r['execution_contract']);raw_contract['request_plan']['tasks']=[t for t in raw_contract['request_plan']['tasks'] if t['category']=='C06']
omitted=verify(idx,q,raw_contract,r['answer'],r['needs']);checks['wide_quote_does_not_hide_wrong_category_omission']=bool(omitted['plan_coverage']['uncovered_need_ids']) and omitted['requires_partial_delivery']
q2='What building and floor is the studio in, and what is its address and contact?'
seed=Understanding([MeaningTask(q2,'contact','C01','detail','building')],True,'fixture_single_field',{'model_called':False})
after=supplement(idx,q2,seed);checks['same_category_multiple_fields_not_collapsed']={'building','floor','address','value'}<={t.facet for t in after.tasks}
checks['original_proposal_not_mutated']=len(seed.tasks)==1 and len(broken.tasks)==1
q3='How much does PC cost for 3 people for 120 minutes if I am not a PSU student?'
obs=observe(idx,q3);checks['quantity_and_condition_observed_independently']={'persons','duration','condition'}<={c['kind'] for c in obs['constraints']}
bad=verify(idx,q3,{'tasks':[],'executor_results':[],'request_plan':{'tasks':[]}},'A fluent answer')
checks['fluent_answer_no_proof_remains_uncovered']=bad['answer_coverage']['status']=='incomplete' and bad['constraint_coverage']['status']=='review_required'
q4='What is the unrecognised quantum coffee treaty?';unrecognised=observe(idx,q4);checks['unknown_predicate_not_falsely_covered']=bool(unrecognised['uncertain'])
conditional=copy.deepcopy(r['execution_contract']);condition_q=q+' if I am not a PSU student?'
condition_verifier=verify(idx,condition_q,conditional,r['answer'],r['needs'])
checks['unverified_influential_condition_requires_partial_delivery']=condition_verifier['requires_partial_delivery'] and any(c['kind']=='condition' and c['status']=='review_required' for c in condition_verifier['constraint_coverage']['constraints'])
out=R/('request_coverage_verification_'+str(time.time_ns()));out.mkdir();report={'checks':checks,'all_passed':all(checks.values()),'details':rows,'actual_model_inferences':0,'real_source_changes':0};(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'checks':checks,'output':str(out)},ensure_ascii=False));assert report['all_passed']
