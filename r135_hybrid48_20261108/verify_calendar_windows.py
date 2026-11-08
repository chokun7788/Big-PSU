"""Owner-source calendar controls; no provider, model or live user data writes."""
import copy,json,time
from datetime import datetime
from verification_support import R
from app.knowledge.common.registry import template
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.obligation_verifier import assess
from app.knowledge.common.domain_flow.plan_contract import compile_request

out=R/('calendar_windows_'+str(time.time_ns()));out.mkdir()
store=CommonStore(out/'controlled_calendar.sqlite');store.initialize(allow_demo=False);view=DraftSnapshotView(store)
at=datetime.fromisoformat('2026-10-26T12:00:00+07:00');checks={};rows=[];version=0
r=template('schedule');r['record_id']='controlled_monday';r['localization']['en_status']='agent_translated'
r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':'2028-01-01T00:00:00+07:00'}
def known(v):return {'status':'known','value':v,'evidence_refs':[],'note':''}
for k,v in {'weekday':0,'timezone':'Asia/Bangkok','zone_ids':[],'service_slots':[{'code':'morning','start':'09:00','end':'12:00','state':'open'},{'code':'afternoon','start':'13:00','end':'16:00','state':'maintenance'}],'service_closed':False}.items():r['fields'][k]=known(v)
def save():
 global r,version
 saved=save_owner_record(store,copy.deepcopy(r),version,'controlled-test');version=saved['version'];r=saved['record'];return Engine.from_snapshot(view.snapshot(),cache_key=view.path)
def run(e,q):
 u=Understanding([MeaningTask(q,'calendar','C11','detail','open_periods')],True,'controlled_calendar_source',{'model_called':False})
 result=e.answer(q,'en',at=at,allow_llm=False,understanding=u);rows.append({'question':q,'result':result});return result,u
e=save()
for label,badslots in [('overlapping',[{'start':'09:00','end':'12:00','state':'open'},{'start':'11:00','end':'13:00','state':'maintenance'}]),('invalid_clock',[{'start':'29:00','end':'30:00','state':'open'}]),('unknown_state',[{'start':'09:00','end':'12:00','state':'assumed_free'}]),('inverted',[{'start':'12:00','end':'09:00','state':'open'}])]:
 bad=copy.deepcopy(r);bad['fields']['service_slots']=known(badslots)
 try:save_owner_record(store,bad,version,'controlled-negative');checks['owner_rejects_'+label+'_service_slots']=False
 except ValueError as error:checks['owner_rejects_'+label+'_service_slots']='service_slots:' in str(error)
bad=copy.deepcopy(r);bad['fields']['service_closed']=known(True)
try:save_owner_record(store,bad,version,'controlled-negative');checks['owner_rejects_closed_day_with_open_slot']=False
except ValueError as error:checks['owner_rejects_closed_day_with_open_slot']='declared closed day' in str(error)
inside,u=run(e,'Is play service open on 2026-10-26 at 10:00?')
checks['owner_source_point_inside_open']='Open for play at 10:00' in inside['answer'] and bool(inside['claims']) and not inside['needs'][0]['execution_contract']['fatal']
outside,_=run(e,'Is play service open on 2026-10-26 at 18:00?');checks['outside_hours_not_daily_open']='Closed for play at 18:00' in outside['answer']
cross,_=run(e,'Is play service open on 2026-10-26 from 11:00-14:00?');checks['range_crosses_gap_and_maintenance_not_whole_open']='Not open for play for the whole period 11:00' in cross['answer']
missing,_=run(e,'Is play service open at 10:00?');checks['time_without_day_targeted_clarification']=not missing['claims'] and missing['needs'][0]['reason']=='calendar_day_required_for_time'
invalid,_=run(e,'Is play service open on 2026-10-26 at 29:00?');checks['invalid_clock_rejected']=not invalid['claims']
reverse,_=run(e,'Is play service open on 2026-10-26 at 11:00-10:00?');checks['reverse_same_day_window_rejected']=not reverse['claims']
future,_=run(e,'Is play service open on 2027-10-25 at 10:00?');checks['future_source_year_not_hardcoded_blocked']='Open for play at 10:00' in future['answer'] and bool(future['claims'])
named,_=run(e,'Is play service open on Monday morning at 14:00?');checks['named_period_clock_conflict_clarified']=not named['claims'] and named['needs'][0]['reason']=='calendar_period_and_time_conflict'
# Reconstruct the compiled task and verify forged claim/display metadata directly.
task=compile_request(inside['question'],u,e.index,inside['execution_contract']['request_plan']['snapshot']).tasks[0] if 'question' in inside else compile_request(u.tasks[0].quote,u,e.index,inside['execution_contract']['request_plan']['snapshot']).tasks[0]
child=inside['needs'][0];snap=inside['execution_contract']['request_plan']['snapshot']
for label,mutate in [('forged_claim',lambda c:c['claims'][0].update(value='Open every hour, free of charge')),('forged_customer_display',lambda c:c['plan']['metadata']['customer_calendar_answer'].update(en='Guaranteed available all day')),('forged_time_receipt',lambda c:c['plan']['metadata']['calendar_window_evaluation'].update(open_entire_window=False)),('removed_projection_marker',lambda c:c['plan']['metadata'].pop('calendar_service_fact_id'))]:
 forged=copy.deepcopy(child);mutate(forged);ledger=assess(e.index,task,forged,snap,u.tasks[0].quote);checks[label+'_rejected']='source_receipt_projection_mismatch' in ledger['fatal']
r['validity']={'state':'unknown','effective_from':None,'effective_until':None};e=save();unknown,_=run(e,'Is play service open on Monday at 10:00?');checks['unknown_validity_only_recorded_partial']=unknown['status']=='partial' and bool(unknown['claims']) and 'unconfirmed: effective date interval' in unknown['answer']
checks['date_clock_constraints_have_actual_projection_proof']=all(c['status']=='structurally_supported' and c['proof'] for c in inside['execution_contract']['verifier_result']['constraint_coverage']['constraints'])
checks['service_slots_not_advertised_as_bookable_periods']=all(row['source_inputs']['state']=='missing_source' for cat in e.capability_catalog['categories'] if cat['category']=='C11' for row in cat['adapter_rows'] if row['field']=='bookable_periods')
unconfirmed,_=run(e,'Is play service open on 2027-10-25 at 10:00?');checks['unknown_future_year_not_guaranteed']=not unconfirmed['claims']
r['validity']={'state':'known','effective_from':'2027-10-25T09:00:00+07:00','effective_until':'2027-10-25T11:00:00+07:00'};e=save();narrow,_=run(e,'Is play service open on 2027-10-25 at 10:00?');checks['target_clock_validity_not_reference_noon']=bool(narrow['claims'])
exceeds,_=run(e,'Is play service open on 2027-10-25 at 10:00-12:00?');checks['whole_window_must_fit_validity']=not exceeds['claims']
r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':'2028-01-01T00:00:00+07:00'};r['fields']['service_slots']=known([{'code':'morning','start':'09:00','end':'12:00','state':'closed'}]);e=save();edited,_=run(e,'Is play service open on 2026-10-26 at 10:00?');checks['source_edit_changes_next_request']='Closed for play at 10:00' in edited['answer']
c=template('closure');c['record_id']='controlled_closure';c['localization']['en_status']='agent_translated';c['validity']=copy.deepcopy(r['validity'])
for k,v in {'local_date':'2026-10-26','zone_ids':[],'state':'closed','reason':{'th':'ปิดทดสอบ','en':'Controlled closure'}}.items():c['fields'][k]=known(v)
save_owner_record(store,c,0,'controlled-test');e=Engine.from_snapshot(view.snapshot(),cache_key=view.path);closed,_=run(e,'Is play service open on 2026-10-26 at 10:00?');checks['special_closure_precedes_weekly_slots']='Closed for play at 10:00' in closed['answer'] and any(x['record_id']=='controlled_closure' for x in closed['claims'])
legacy=next(f for f in e.index.bycat['C11'] if f['facet']=='service_periods');legacy['service_slots']=[{'start':'29:00','end':'30:00','state':'open'}]
bad_legacy,_=run(e,'Is play service open on 2026-10-26 at 10:00?');checks['invalid_legacy_source_withheld_without_provider_or_business_conflict_claim']=not bad_legacy['claims'] and bad_legacy['terminal_state']=='missing_source' and 'invalid or overlapping periods' in bad_legacy['answer']
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_provider_calls':0,'user_data_modified':False}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
