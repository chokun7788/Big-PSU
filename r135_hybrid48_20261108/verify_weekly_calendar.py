"""Known/unknown weekday sets are distinct from date/zone applicability."""
import copy,json,time
from verification_support import R
from app.knowledge.common.registry import template
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.scope import reference_time
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
from app.knowledge.common.domain_flow.collection_contract import verify
from app.knowledge.common.domain_flow.native_contract import attach_native
from dataclasses import dataclass
from types import SimpleNamespace
@dataclass
class NativeOutput:
 answer:str
 validation:object
 decision_artifact:dict
out=R/('weekly_calendar_'+str(time.time_ns()));out.mkdir();store=CommonStore(out/'controlled_weekly.sqlite');store.initialize(allow_demo=False);view=DraftSnapshotView(store);clock=reference_time('2026-10-26T12:00:00+07:00');checks={};rows=[];records={}
validity={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':'2028-01-01T00:00:00+07:00'}
def known(v):return {'status':'known','value':v,'evidence_refs':[],'note':''}
def save(r,version=None):
 saved=save_owner_record(store,copy.deepcopy(r),r['revision'] if version is None else version,'controlled-test')['record'];records[saved['record_id']]=saved;return saved
for day in range(7):
 r=template('schedule');r['record_id']='controlled_weekday_'+str(day);r['localization']['en_status']='agent_translated';r['validity']=copy.deepcopy(validity)
 fields={'weekday':day,'timezone':'Asia/Bangkok','zone_ids':[],'open_periods':[{'start':'08:00','end':'18:00'}],'bookable_periods':[{'start':'10:00','end':'11:00'}],'maintenance_periods':[{'start':'13:00','end':'16:00'}] if day<6 else [],'service_slots':[{'code':'morning','start':'09:00','end':'12:00','state':'open'},{'code':'afternoon','start':'13:00','end':'16:00','state':'maintenance'}],'service_closed':False}
 for key,v in fields.items():r['fields'][key]=known(v)
 save(r,0)
def run(q,facet='maintenance_periods',op='list'):
 e=Engine.from_snapshot(view.snapshot(),cache_key=view.path);u=Understanding([MeaningTask(q,'schedule','C11',op,facet)],True,'controlled_weekly_calendar',{'model_called':False});r=e.answer(q,'en',at=clock,allow_llm=False,understanding=u);rows.append({'q':q,'result':r});return e,r,u
def native_receipts(q,ids):
 snap=view.snapshot();index=Engine.from_snapshot(snap,cache_key=view.path).index;refs=[{'status':'known','record_id':rid,'field':'maintenance_periods','evidence_refs':snap['release']['records'][rid]['fields']['maintenance_periods']['evidence_refs']} for rid in ids]
 u=Understanding([MeaningTask(q,'schedule','C11','list','maintenance_periods')],True,'controlled_native_source_set',{'model_called':False});compiled=compile_request(q,u,index,{'release_id':snap['active'],'epoch':snap['epoch'],'reference_time':clock.isoformat()})
 output=NativeOutput('Controlled native source fields',SimpleNamespace(ok=True),{'response_type':'answer','obligations':refs,'query_plan':{'method':'controlled_native_fields'},'need_results':[{}]})
 return attach_native(CommonAnswerer(view),output,snap,compiled,clock,'en').decision_artifact['execution_contract']
q='List weekly maintenance periods';e,r,u=run(q);child=r['needs'][0];proof=child['execution_contract']['collection_proof']
checks['all_seven_recorded_maintenance_weekdays_proven']=r['status']=='answer' and len(r['claims'])==7 and proof['verified'] and proof['scope_verified'] and not proof['physical_world_completeness_claimed']
checks['known_empty_day_not_missing_source']=any(c['record_id']=='controlled_weekday_6' for c in r['claims']) and child['plan']['metadata']['weekly_missing_weekdays']==[]
checks['known_source_does_not_claim_unknown_validity_or_scope']=child['plan']['metadata']['calendar_source_limits']==[] and 'Unconfirmed:' not in r['answer'] and 'Recorded effective intervals:' in r['answer']
original=copy.deepcopy(child);context=r['execution_contract']['request_plan']['snapshot'];task=compile_request(q,u,e.index,context).tasks[0]
forged=copy.deepcopy(child);forged['plan']['metadata']['calendar_source_periods'][0]['validity']['effective_until']='2030-01-01T00:00:00+07:00';checks['forged_effective_display_rejected']='source_receipt_calendar_set_projection_mismatch' in assess(e.index,task,forged,context,q)['fatal']
_,play,_=run('What days is play service open weekly?','open_periods');checks['known_weekly_play_source_not_forced_partial']=play['status']=='answer' and len(play['claims'])==7 and all(c['facet']=='service_periods' for c in play['claims']) and 'not live machine availability or building access hours' in play['answer']
_,book,_=run('List weekly bookable periods when open','bookable_periods');book_task=book['needs'][0];checks['bookable_not_replaced_by_play_service_slots']=len(book_task['claims'])==7 and all(c['facet']=='bookable_periods' and '10:00' in c['value'] and '09:00' not in c['value'] for c in book_task['claims'])
_,physical,_=run('List weekly building opening hours','open_periods');checks['physical_hours_distinct_from_play_and_bookable']=len(physical['claims'])==7 and all(c['facet']=='open_periods' and '08:00' in c['value'] for c in physical['claims'])
_,future,_=run('List weekly maintenance periods in 2027');checks['future_known_interval_used_at_requested_year']=len(future['claims'])==7 and future['status']=='answer'
_,monday,_=run('List weekly maintenance periods on Monday');checks['explicit_weekday_not_expanded_to_all_seven']=len(monday['claims'])==1 and monday['claims'][0]['record_id']=='controlled_weekday_0' and monday['needs'][0]['execution_contract']['collection_proof']['verified']
_,range_days,_=run('List weekly maintenance periods Monday to Friday');checks['weekday_range_covers_intermediate_days_exactly']=len(range_days['claims'])==5 and {c['record_id'] for c in range_days['claims']}=={'controlled_weekday_'+str(d) for d in range(5)} and range_days['needs'][0]['execution_contract']['collection_proof']['verified']
for label,question,days in [('same_day_range','List weekly maintenance periods Monday to Monday',{0}),('wrapped_range','List weekly maintenance periods Friday to Monday',{4,5,6,0}),('thai_full_weekday_range','ตารางบำรุงรักษารายสัปดาห์วันพฤหัสบดีถึงวันเสาร์',{3,4,5})]:
 _,subset,_=run(question);checks[label+'_exact_requested_set']={c['record_id'] for c in subset['claims']}=={'controlled_weekday_'+str(d) for d in days} and subset['needs'][0]['execution_contract']['collection_proof']['verified']
_,detail,_=run('Show weekly maintenance periods',op='detail');checks['weekly_detail_proposal_gets_explicit_set_obligation']=detail['execution_contract']['request_plan']['tasks'][0]['operation']=='list' and detail['needs'][0]['execution_contract']['collection_proof']['verified'] and detail['understanding']['tasks'][0]['operation']=='detail'
from app.knowledge.common.answer import CommonAnswerer
native=native_receipts(q,[c['record_id'] for c in r['claims']]);checks['native_collection_also_reconciles_full_source_set']=native['tasks'][0]['collection_proof']['verified'] and native['terminal_state']=='supported'
public=CommonAnswerer(view).answer('List weekly maintenance periods',locale='en',at=clock,planner=None);contract=public.decision_artifact['execution_contract'];checks['real_common_chat_uses_same_weekly_set_contract']=contract['tasks'][0]['collection_proof']['verified'] and contract['terminal_state']=='supported' and '13:00' in public.answer
public_play=CommonAnswerer(view).answer('What days is play service open weekly?',locale='en',at=clock,planner=None);cp=public_play.decision_artifact['execution_contract'];checks['real_weekly_play_chat_preserves_typed_scope_and_proof']=cp['tasks'][0]['collection_proof']['verified'] and cp['terminal_state']=='supported' and 'not live machine availability or building access hours' in public_play.answer
reservation_question='What are the studio service days and hours for reservations?'
public_reservation=CommonAnswerer(view).answer(reservation_question,locale='en',at=clock,planner=None);rc=public_reservation.decision_artifact['execution_contract'];task=rc['request_plan']['tasks'][0];claims=[c for child in rc['executor_results'] for c in child['claims']]
checks['reservation_days_query_reads_bookable_weekly_source']=task['category']=='C11' and task['facet']=='bookable_periods' and {c['record_id'] for c in claims}==set(records) and '10:00–11:00' in public_reservation.answer
checks['reservation_days_not_physical_or_live']=all(c['facet']=='bookable_periods' for c in claims) and '08:00–18:00' not in public_reservation.answer and 'not live' in public_reservation.answer
checks['reservation_days_collection_has_source_proof']=rc['tasks'][0]['collection_proof']['verified'] and rc['terminal_state']=='supported'
from app.knowledge.common.domain_flow.native_intents import propose
for i,question in enumerate(['What are the studio service days and hours for tournament registrations?','What are the studio service days and hours for reservations and how much does it cost?','Are reservations available right now on Monday?']):
 candidate=propose(Engine.from_snapshot(view.snapshot()).index,question)
 if i==1:checks['compound_reservation_calendar_and_price_remain_separate']=bool(candidate and any(t.canonical_operation=='calendar.weekly_bookable_periods' for t in candidate.tasks) and any(t.category=='C06' for t in candidate.tasks))
 else:checks['reservation_calendar_does_not_absorb_other_predicate_'+str(i)]=not candidate or all(t.canonical_operation!='calendar.weekly_bookable_periods' for t in candidate.tasks)
monday=copy.deepcopy(records['controlled_weekday_0']);changed_monday=copy.deepcopy(monday);changed_monday['fields']['bookable_periods']=known([{'start':'10:30','end':'11:00'}]);save(changed_monday)
public_changed=CommonAnswerer(view).answer(reservation_question,locale='en',at=clock,planner=None);checks['reservation_days_uses_actual_new_source']='10:30–11:00' in public_changed.answer
save(monday,records['controlled_weekday_0']['revision'])
_,invalid,_=run('List weekly maintenance periods on 2026-02-31');checks['invalid_date_is_targeted_input_failure_not_exception']=not invalid['claims'] and invalid['status']=='missing_input'
r0=copy.deepcopy(records['controlled_weekday_0']);r0['validity']={'state':'unknown','effective_from':None,'effective_until':None};save(r0)
_,unknown,_=run(q);checks['unknown_interval_keeps_recorded_set_proof_but_partial_applicability']=unknown['status']=='partial' and unknown['needs'][0]['execution_contract']['collection_proof']['verified'] and 'effective date interval' in unknown['answer']
r0=copy.deepcopy(records['controlled_weekday_0']);r0['validity']=copy.deepcopy(validity);r0['fields']['zone_ids']={'status':'unknown','value':None,'evidence_refs':[],'note':'Controlled unresolved scope'};save(r0)
_,zone,_=run(q);checks['unknown_zone_not_silently_global']=zone['status']=='partial' and 'applicable resource or zone' in zone['answer']
r0=copy.deepcopy(records['controlled_weekday_0']);r0['fields']['zone_ids']=known([]);save(r0)
edit=copy.deepcopy(records['controlled_weekday_1']);edit['fields']['maintenance_periods']=known([{'start':'15:00','end':'16:00'}]);save(edit)
_,changed,_=run(q);checks['owner_edit_updates_exact_weekday_field']=any(c['record_id']=='controlled_weekday_1' and c['value']=='15:00–16:00' for c in changed['claims'])
store.withdraw('controlled_weekday_2',actor='controlled-test');_,missing,_=run(q);checks['withdrawn_weekday_keeps_other_six_and_names_missing_day']=len(missing['claims'])==6 and missing['status']=='partial' and 'No applicable record for: Wednesday' in missing['answer'] and not missing['needs'][0]['execution_contract']['collection_proof']['verified']
# Restore as a new source identity, not by resurrecting a withdrawn record.
replacement=copy.deepcopy(records['controlled_weekday_2']);replacement['record_id']='controlled_weekday_2_replacement';save(replacement,0)
expired=copy.deepcopy(records['controlled_weekday_3']);expired['validity']['effective_until']='2026-10-25T00:00:00+07:00';save(expired)
_,old,_=run(q);checks['expired_weekday_not_delivered_as_current']=len(old['claims'])==6 and all(c['record_id']!='controlled_weekday_3' for c in old['claims']) and old['status']=='partial'
fresh=copy.deepcopy(records['controlled_weekday_3']);fresh['validity']=copy.deepcopy(validity);save(fresh)
# A second same-scope source for one day is not silently chosen or certified.
duplicate=copy.deepcopy(records['controlled_weekday_4']);duplicate['record_id']='controlled_weekday_4_variant';duplicate['fields']['maintenance_periods']=known([{'start':'14:00','end':'16:00'}]);save(duplicate,0)
current,ambiguous,_=run(q);checks['weekday_variants_not_arbitrarily_selected']=len(ambiguous['claims'])==6 and ambiguous['status']=='partial' and 'Unresolved source versions or scope for: Friday' in ambiguous['answer']
checks['seven_rows_cannot_hide_extra_source_version']=not verify(current.index,task,original,question=q,at=clock)['verified']
store=CommonStore(out/'controlled_zones.sqlite');store.initialize(allow_demo=False);view=DraftSnapshotView(store);records={}
for group,start in [('blue','13:00'),('red','14:00')]:
 zone=template('zone');zone['record_id']='controlled_'+group+'_zone';zone['localization']['en_status']='agent_translated';zone['fields']['name']=known({'th':group+' test zone','en':group.title()+' test zone'});save(zone,0)
 for day in range(7):
  r=template('schedule');r['record_id']='controlled_'+group+'_'+str(day);r['localization']['en_status']='agent_translated';r['validity']=copy.deepcopy(validity)
  for key,v in {'weekday':day,'timezone':'Asia/Bangkok','zone_ids':[zone['record_id']],'maintenance_periods':[{'start':start,'end':'16:00'}]}.items():r['fields'][key]=known(v)
  save(r,0)
current,blue,_=run('List weekly maintenance periods for Blue test zone');checks['known_zone_scopes_select_only_matching_seven_records']=blue['status']=='answer' and len(blue['claims'])==7 and all(c['record_id'].startswith('controlled_blue_') and '13:00' in c['value'] for c in blue['claims']) and blue['needs'][0]['execution_contract']['collection_proof']['verified']
unqualified=SimpleNamespace(category='C11',facet='maintenance_periods',source_span=SimpleNamespace(text=q))
checks['seven_valid_other_scope_rows_do_not_prove_unqualified_set']=not verify(current.index,unqualified,blue['needs'][0],question=q,at=clock)['verified']
native=native_receipts(q,[c['record_id'] for c in blue['claims']]);checks['native_seven_rows_cannot_hide_other_scope_sources']=not native['tasks'][0]['collection_proof']['verified'] and native['terminal_state']=='partial'
_,unspecified,_=run(q);checks['unqualified_multiple_zone_calendars_not_guessed']=not unspecified['claims'] and unspecified['status']=='missing_source'
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_provider_calls':0,'user_data_modified':False,'controlled_source_not_real_business_data':True};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
