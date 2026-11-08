"""Future v3 language proposal to actual source execution, with v2 frozen."""
import copy,json,time
from verification_support import R,snapshot
from app.knowledge.common.domain_flow import graph_protocol as v2,graph_protocol_v3 as v3
from app.knowledge.common.domain_flow.understanding import parse as retained_parse,schema as retained_schema
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.training_contract import runtime_contract
O=R/('period_wire_v3_'+str(time.time_ns()));O.mkdir();checks={};details=[]
before={'messages':v2.messages('retained question'),'schema':retained_schema()}
q='Please tell me: What time is the afternoon session'
label={'version':v3.VERSION,'focus':'service_periods','context_quotes':[],'tasks':[{'id':'t1','quote':q,'domain':'schedule','operation':'list','facet':'service_periods','target':'','constraints':[{'slot':'time','quote':'afternoon','source_record_id':'','scope':'local'}],'ambiguous':False}],'shared_bindings':[]}
encoded=json.dumps(label);u=v3.parse(encoded,q);checks['explicit_v3_field_and_focus_accepted']=u.accepted and u.tasks[0].facet=='service_periods' and u.event['wire_version']==v3.VERSION
checks['no_semantic_facet_disguised_as_bookable']=u.accepted and not u.event['semantic_facet_rewritten'] and u.tasks[0].facet!='bookable_periods'
e=Engine.from_snapshot(snapshot());r=e.answer(q,'en',at='2026-10-27T10:00:00+07:00',allow_llm=False,understanding=u);details.append({'case':'actual_row191_v3_source_execution','proposal':label,'understanding':u.as_dict(),'result':r})
checks['v3_proposal_dispatches_same_actual_service_source']=len(r['claims'])==7 and all(c['facet']=='service_periods' for c in r['claims']) and 'Friday — afternoon: 13:00–16:00 (maintenance)' in r['answer']
checks['no_FAQ_or_booking_window_substitution']=all(e.index.records[c['record_id']]['kind']=='schedule' for c in r['claims']) and '09:00' not in r['answer']
checks['retained_v2_parser_does_not_silently_accept_v3']=not retained_parse(encoded,q).accepted
old=copy.deepcopy(label);old['version']=v2.VERSION;checks['v3_does_not_silently_accept_old_version']=not v3.parse(json.dumps(old),q).accepted
for name,change in [
 ('business_field',lambda p:p.update(answer='13:00')),
 ('business_task',lambda p:p['tasks'][0].update(answer='open')),
 ('foreign_id',lambda p:p['tasks'][0]['constraints'][0].update(source_record_id='migrated_schedule_4')),
 ('invented_target',lambda p:p['tasks'][0].update(target='Friday')),
 ('invented_quote',lambda p:p['tasks'][0]['constraints'][0].update(quote='morning')),
 ('wrong_domain',lambda p:p['tasks'][0].update(domain='payment')),
 ('unsupported_operation',lambda p:p['tasks'][0].update(operation='execute_sql')),
 ('wrong_task_id',lambda p:p['tasks'][0].update(id='t3')),
 ('self_edge',lambda p:p['shared_bindings'].append({'source_task_id':'t1','target_task_id':'t1','slot':'time','quote':'afternoon','basis':'shared_prefix'})),
 ('truncated_single_task',lambda p:p['tasks'][0].update(quote='What time is the afternoon session'))]:
 p=copy.deepcopy(label);change(p);checks[name+'_rejected']=not v3.parse(json.dumps(p),q).accepted
checks['duplicate_wire_keys_rejected']=not v3.parse(encoded[:-1]+',"focus":"bookable_periods"}',q).accepted
checks['oversized_wire_rejected']=not v3.parse(' '*131073,q).accepted
checks['native_schema_extension_not_global_v2_mutation']=before=={'messages':v2.messages('retained question'),'schema':retained_schema()} and 'service_periods' not in v2.DOMAIN_FACETS['schedule'].split()
checks['new_protocol_prompt_and_schema_are_distinct']=v3.messages(q)!=v2.messages(q) and v3.schema()!=retained_schema()
W=R/'training_review_workbench_1793037663397671000';A=sorted(W.glob('current_admission_*'))[-1];ad=json.loads((W/'review_round_010/ADJUDICATION_191.json').read_text('utf8'))
checks['old_row191_quarantine_not_readmitted_by_codec']=ad['adjudication_status']=='quarantined' and json.loads((A/'SUMMARY.json').read_text('utf8'))['quarantined']==1
checks['retained_training_consumer_wire_not_silently_switched']=json.loads((A/'RUNTIME_CONTRACT.json').read_text('utf8'))['wire_version']==v2.VERSION
report={'all_passed':all(checks.values()),'checks':checks,'new_protocol':v3.VERSION,'production_wire_changed':False,'actual_model_generation_or_training':0,'training_dataset_readmitted':False,'remaining':'Explicit v3 training admission/migration records, actual generated model provenance, same-protocol three-arm freeze/evaluation and dated exception mapping remain pending. Native/source execution is not proof a model learned v3.'}
(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(O),'all_passed':report['all_passed'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v]}));assert report['all_passed']
