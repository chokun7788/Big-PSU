"""Source/field/day/locale/forgery controls for the native period boundary."""
import copy,json,os,time
from unittest.mock import patch
from verification_support import R,snapshot
from app.knowledge.common.registry import template
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.native_intents import propose
from app.knowledge.common.domain_flow.understanding import WIRE_FACETS,FACETS,parse
from app.knowledge.common.domain_flow.period_scope import request,plan
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
from app.knowledge.common.answer import CommonAnswerer
O=R/('named_periods_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite')
store=CommonStore(O/'controlled.sqlite');store.initialize(allow_demo=False);view=DraftSnapshotView(store)
clock='2026-10-26T10:00:00+07:00';checks={};details=[];records={}
validity={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':'2028-01-01T00:00:00+07:00'}
def known(v):return {'status':'known','value':v,'evidence_refs':[],'note':''}
def save(r,revision):
 s=save_owner_record(store,copy.deepcopy(r),revision,'controlled-native-period')['record'];records[s['record_id']]=s;return s
for day in range(7):
 r=template('schedule');r['record_id']='period_day_'+str(day);r['validity']=copy.deepcopy(validity);r['localization']['en_status']='agent_translated'
 fields={'weekday':day,'timezone':'Asia/Bangkok','zone_ids':[],'open_periods':[{'start':'08:00','end':'18:00'}],
 'bookable_periods':[{'start':'09:00','end':'12:00'}],'maintenance_periods':[],'service_closed':day>4,
 'service_slots':[] if day>4 else [{'code':'morning','start':'09:00','end':'12:00','state':'open'},{'code':'afternoon','start':'13:00','end':'16:00','state':'maintenance' if day==4 else 'open'}]}
 for k,v in fields.items():r['fields'][k]=known(v)
 save(r,0)
def engine():return Engine.from_snapshot(view.snapshot(),cache_key=view.path)
def run(q,locale='auto'):
 e=engine();u=propose(e.index,q)
 with patch('urllib.request.urlopen',side_effect=AssertionError('actual HTTP forbidden')):
  r=e.answer(q,locale,at=clock,allow_llm=False,understanding=u)
 details.append({'question':q,'locale':locale,'result':r});return e,u,r
q='Please tell me: What time is the afternoon session';e,u,r=run(q)
checks['native_task_uses_service_not_bookable']=u.tasks[0].facet=='service_periods' and u.event['wire_boundary']=='native_only_not_r129_plan_v2'
checks['full_recorded_weekday_set']=len(r['claims'])==7 and all(c['facet']=='service_periods' for c in r['claims'])
checks['friday_maintenance_and_weekend_closed_distinct']='Friday — afternoon: 13:00–16:00 (maintenance)' in r['answer'] and 'Saturday — afternoon: recorded closed day' in r['answer']
checks['only_requested_period_rendered']='09:00' not in r['answer'] and '08:00' not in r['answer'] and 'booking windows' in r['answer']
child=r['needs'][0];context=r['execution_contract']['request_plan']['snapshot'];task=compile_request(q,u,e.index,context).tasks[0]
checks['typed_source_receipts_and_complete_recorded_set']=not child['execution_contract']['fatal'] and child['execution_contract']['collection_proof']['verified']
for name,change in [
 ('time',lambda m:m['named_period_receipt']['rows'][0]['slots'][0].update(start='14:30')),
 ('state',lambda m:m['named_period_receipt']['rows'][4]['slots'][0].update(state='open')),
 ('day',lambda m:m['named_period_receipt']['rows'][0].update(weekday=6)),
 ('revision',lambda m:m['named_period_receipt']['rows'][0].update(record_revision=999)),
 ('render',lambda m:m['named_period_answer'].update(en='The afternoon is bookable at 14:30')),
 ('missing',lambda m:m.pop('named_period_receipt'))]:
 bad=copy.deepcopy(child);change(bad['plan']['metadata']);checks['forged_'+name+'_rejected']='source_receipt_named_period_projection_mismatch' in assess(e.index,task,bad,context,q)['fatal']
_,_,friday=run('What time is the afternoon session on Friday?');checks['friday_scope_exact']=len(friday['claims'])==1 and friday['claims'][0]['record_id']=='period_day_4' and 'maintenance' in friday['answer'] and 'Monday' not in friday['answer']
play_q='Please answer from verified studio information: Please tell me: When can I play on Monday afternoon'
_,play_u,play_r=run(play_q);checks['explicit_play_time_without_session_noun']=play_u.tasks[0].facet=='service_periods' and len(play_r['claims'])==1 and play_r['claims'][0]['record_id']=='period_day_0' and 'Monday — afternoon: 13:00–16:00' in play_r['answer'] and 'Friday' not in play_r['answer']
with patch('urllib.request.urlopen',side_effect=AssertionError('actual HTTP forbidden')):play_public=CommonAnswerer(view).answer(play_q,locale='auto',at=clock,planner=None)
checks['public_explicit_play_uses_typed_monday_not_broad_faq']=play_public is not None and 'Monday — afternoon: 13:00–16:00' in play_public.answer and 'Friday' not in play_public.answer
_,_,play_th=run('เล่นเวลาไหนช่วงบ่ายวันจันทร์');checks['thai_explicit_play_keeps_day_period']='จันทร์' in play_th['answer'] and '13:00–16:00' in play_th['answer'] and 'Friday' not in play_th['answer']
_,_,play_closed=run('When can I play on Sunday afternoon?');checks['explicit_play_closed_day_not_invented_hours']=len(play_closed['claims'])==1 and play_closed['claims'][0]['record_id']=='period_day_6' and 'recorded closed day' in play_closed['answer'] and '13:00' not in play_closed['answer']
for extra in ['Is Monday afternoon open?','What time does the building open on Monday afternoon?','When can I book Monday afternoon?','When can I play for the afternoon price?']:
 checks['explicit_play_predicate_boundary_'+str(len(checks))]=request(e.index,extra) is None
original_monday=copy.deepcopy(records['period_day_0']);changed=copy.deepcopy(original_monday);changed['fields']['service_slots']['value'][1]['start']='14:15';save(changed,changed['revision'])
_,_,play_changed=run(play_q);checks['explicit_play_follows_changed_owner_slot']='14:15–16:00' in play_changed['answer'] and '13:00–16:00' not in play_changed['answer']
save(original_monday,records['period_day_0']['revision'])
_,_,both=run('What time are the morning and afternoon sessions on Friday?');checks['both_requested_periods_retained']='09:00–12:00' in both['answer'] and '13:00–16:00' in both['answer']
_,_,thai=run('รอบบ่ายเวลาไหนวันศุกร์');checks['thai_auto_locale']='บำรุงรักษา' in thai['answer'] and 'Friday' not in thai['answer']
_,_,override=run(q,'th');checks['explicit_language_override']='รอบบ่าย' in override['answer']
_,_,dated=run('What time is the afternoon session on 2026-10-30?');checks['dated_scope_exact']=dated['status']=='answer' and len(dated['claims'])==1 and dated['claims'][0]['record_id']=='period_day_4' and '2026-10-30' in dated['answer']
_,_,relative=run('What time is the afternoon session tomorrow?');checks['relative_uses_reference_clock']=len(relative['claims'])==1 and relative['claims'][0]['record_id']=='period_day_1' and '2026-10-27' in relative['answer']
for name,text in [('weekday_conflict','What time is the afternoon session Monday 2026-10-30?'),('many_dates','What time is the afternoon session on 2026-10-30 and 2026-10-31?'),('clock','What time is the afternoon session after 14:00?')]:
 p=plan(e.index,text,clock);checks[name+'_not_silently_dropped']=p is not None and not p.ids and p.status=='missing_input'
for text in ['What time can I book the afternoon session?','Is the afternoon session available today?','What time does the building open in the afternoon?','How much does the afternoon session cost?','What time is the registration deadline for the afternoon session?','What time can I contact the office about the afternoon session?','I sometimes play afternoon games','What time is the longer morning session versus the afternoon session?']:
 checks['different_predicate_not_period_'+str(len(checks))]=request(e.index,text) is None
checks['wire_v2_unchanged_native_field_not_model_vocabulary']='service_periods' not in WIRE_FACETS['C11'] and 'service_periods' in FACETS['C11']
wire={'tasks':[{'quote':q,'domain':'schedule','operation':'list','facet':'service_periods','target':'','ambiguous':False,'constraints':[]}]}
checks['model_cannot_claim_native_only_facet']=not parse(json.dumps(wire),q).accepted
for extra in ['What time is the afternoon session in 2029?','What time is the afternoon session ปี 2569?']:
 p=plan(e.index,extra,clock);checks['unprojected_year_scope_'+str(len(checks))]=not p.ids and p.status=='missing_input'
p=plan(e.index,'What time is the afternoon session Monday to Friday on 2026-10-30?',clock);checks['date_plus_extra_weekdays_not_dropped']=not p.ids and p.status=='missing_input'
missing_snap=copy.deepcopy(view.snapshot());missing_snap['release']['records'].pop('period_day_4');missing_engine=Engine.from_snapshot(missing_snap)
missing=missing_engine.answer(q,'en',at=clock,allow_llm=False,understanding=propose(missing_engine.index,q));details.append({'case':'missing_weekday','result':missing})
checks['missing_weekday_not_closed_or_complete']=missing['status']=='partial' and len(missing['claims'])==6 and 'Missing weekday source: Friday' in missing['answer'] and not missing['needs'][0]['execution_contract']['collection_proof']['verified']
original_friday=copy.deepcopy(records['period_day_4'])
changed=copy.deepcopy(original_friday);changed['validity']['effective_until']='2026-01-02T00:00:00+07:00';save(changed,changed['revision'])
_,_,expired=run('What time is the afternoon session on Friday?');checks['expired_source_not_delivered']=not expired['claims'] and expired['status']=='not_current'
changed=copy.deepcopy(original_friday);save(changed,records['period_day_4']['revision'])
duplicate=copy.deepcopy(records['period_day_4']);duplicate['record_id']='period_friday_second_scope';duplicate['revision']=0;save(duplicate,0)
_,_,conflicted=run(q);checks['multiple_weekday_versions_disclosed']=conflicted['status']=='partial' and len(conflicted['claims'])==6 and 'Multiple unresolved weekday sources: Friday' in conflicted['answer']
_,_,conflicted_day=run('What time is the afternoon session on Friday?');checks['no_arbitrary_weekday_version_selected']=not conflicted_day['claims']
# Withdraw only from this isolated view; leave both actual owner evidence
# revisions intact. This models an explicit publication scope boundary.
base_view=view
class WithoutDuplicate:
 path=base_view.path
 def snapshot(self):
  s=copy.deepcopy(base_view.snapshot());s['release']['records'].pop('period_friday_second_scope');s['epoch']+=100;return s
 def still_current(self,s):return s==self.snapshot()
view=WithoutDuplicate()
changed=copy.deepcopy(records['period_day_4']);changed['fields']['service_slots']['value']=changed['fields']['service_slots']['value'][:1];save(changed,changed['revision'])
_,_,unrecorded=run('What time is the afternoon session on Friday?');checks['absent_period_is_not_live_unavailability']='afternoon: period not recorded' in unrecorded['answer'] and '13:00' not in unrecorded['answer']
changed=copy.deepcopy(original_friday);save(changed,records['period_day_4']['revision'])
c=template('closure');c['record_id']='period_dated_exception';c['validity']=copy.deepcopy(validity);c['localization']['en_status']='agent_translated'
for k,v in {'local_date':'2026-10-30','zone_ids':[],'state':'closed','reason':{'th':'ทดสอบประกาศ','en':'Controlled announcement'}}.items():c['fields'][k]=known(v)
save(c,0)
_,_,exception=run('What time is the afternoon session on 2026-10-30?');checks['dated_exception_never_silently_overridden_by_weekly_source']=not exception['claims'] and exception['needs'][0]['reason']=='named_period_dated_exception_requires_service_scope_review'
changed=copy.deepcopy(records['period_day_4']);changed['fields']['service_slots']['value'][1]['start']='13:30';save(changed,changed['revision'])
_,_,edited=run('What time is the afternoon session on Friday?');checks['actual_source_edit_changes_next_answer']='13:30–16:00' in edited['answer'] and '13:00–16:00' not in edited['answer']
changed=copy.deepcopy(records['period_day_4']);changed['validity']={'state':'unknown','effective_from':None,'effective_until':None};save(changed,changed['revision'])
_,_,unknown=run('What time is the afternoon session on Friday?');checks['unknown_effective_interval_disclosed']=unknown['status']=='partial' and 'not fully confirmed' in unknown['answer']
actual=Engine.from_snapshot(snapshot());actual_u=propose(actual.index,q)
with patch('urllib.request.urlopen',side_effect=AssertionError('actual HTTP forbidden')):actual_r=actual.answer(q,'auto',at=clock,allow_llm=False,understanding=actual_u)
details.append({'case':'actual_retained_row191','result':actual_r});checks['actual_row191_typed_source_not_faq']=actual_u.tasks[0].facet=='service_periods' and len(actual_r['claims'])==7 and all(c['facet']=='service_periods' for c in actual_r['claims']) and 'maintenance' in actual_r['answer']
with patch('urllib.request.urlopen',side_effect=AssertionError('actual HTTP forbidden')):public=CommonAnswerer(view).answer(q,locale='auto',at=clock,planner=None)
details.append({'case':'public_common','answer':public.answer if public else None,'artifact':public.decision_artifact if public else None});checks['public_common_skips_wrong_faq_facet']=public is not None and 'Recorded play-service periods' in public.answer and '13:30' in public.answer
changed=copy.deepcopy(records['period_day_0']);changed['fields']['service_slots']['value'].append({'code':'twilight','label':'รอบค่ำ','start':'17:00','end':'19:00','state':'open'});save(changed,changed['revision'])
_,_,dynamic=run('What time is the twilight session on Monday?');checks['new_owner_named_period_without_retraining']='twilight: 17:00–19:00' in dynamic['answer'] and '13:00' not in dynamic['answer']
_,_,dynamic_th=run('รอบค่ำเวลาไหนวันจันทร์');checks['new_owner_thai_label_bound_exactly']='รอบค่ำ: 17:00–19:00' in dynamic_th['answer']
changed=copy.deepcopy(records['period_day_0']);slot=changed['fields']['service_slots']['value'][1];slot.pop('code');slot['label']='afternoon';save(changed,changed['revision'])
_,_,label_only=run('What time is the afternoon session on Monday?');checks['valid_optional_code_label_is_source_bound']='afternoon: 13:00–16:00' in label_only['answer'] and label_only['status']=='answer'
changed=copy.deepcopy(records['period_day_0']);changed['fields']['service_slots']['value'][1].pop('label');save(changed,changed['revision'])
_,_,unlabelled=run('What time is the afternoon session on Monday?');checks['valid_unnamed_slot_not_inferred_from_clock']=unlabelled['status']=='partial' and 'unconfirmed period identities' in unlabelled['answer'] and '13:00' not in unlabelled['answer']
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_provider_HTTP':0,'actual_owner_modified':False,'wire_boundary':'native-only; row191 retained wire target remains quarantined','remaining':'Dated exception mapping, general language grammar, full category/API/final acceptance pending.'}
(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8')
print(json.dumps({'output':str(O),'all_passed':report['all_passed'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v]}));assert report['all_passed']
