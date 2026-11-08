"""C08/C09 actual owner source action/condition controls; no booking transaction."""
import copy,json,time,os,sqlite3
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.scope import reference_time
out=R/('booking_payment_matrix_'+str(time.time_ns()));out.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'dialogue.sqlite');store=CommonStore(out/'source.sqlite');store.initialize(allow_demo=False);view=DraftSnapshotView(store);checks={};details=[];bi=lambda s:{'th':s,'en':s}
cases=[
 ('C08','booking_steps','How do I book?','Choose a station, select a recorded slot, submit the form and wait for confirmation.'),
 ('C08','customer_cancel','How can I cancel my booking?','The booking customer may request cancellation at least 45 minutes before the slot; staff must confirm it.'),
 ('C08','studio_cancel','Can the studio cancel without prior notice?','The studio may cancel a booking containing invalid identification; this is a studio action, not a customer cancellation right.'),
 ('C08','booking_session_limit','How many sessions can I book?','Each booking permits at most two recorded sessions; another request requires separate confirmation.'),
 ('C08','walk_in','Can I walk in?','A walk-in may ask staff for a currently available slot; arrival does not confirm a booking.'),
 ('C08','change_time','Can I change my booking time?','Time changes require staff approval before the original slot; the booking customer must request them.'),
 ('C08','wrong_machine','I booked the wrong machine; what next?','For a wrong machine selection contact staff with the booking reference before using the machine.'),
 ('C08','checkin_documents','Which documents do I show at studio check-in?','The player must show their own identification and the booking confirmation at check-in.'),
 ('C08','checkin_advance','How early must I check in?','Check in ten minutes before the recorded start; checking in early does not authorize early play.'),
 ('C08','arrival_waiting','Where can I wait if I arrive early?','Wait in the marked lobby until staff call the slot; the play area remains reserved.'),
 ('C08','extend_session','Can I extend my session?','Request an extension before the session ends; staff approval and an available later slot are both required.'),
 ('C08','change_service','Can I switch to another service?','Changing service requires staff confirmation and a new availability check; it is not automatic.'),
 ('C08','correct_booking_name','How do I correct the name on my booking?','Only the booking customer may request a name correction with matching identification.'),
 ('C08','change_paid_booking','I paid and booked the wrong date; can I change it?','For a paid wrong-date booking contact staff; payment alone does not authorize a date change.'),
 ('C08','late_notice','I cannot arrive on time; what should I do?','Notify staff with the booking reference before the slot; a late notice does not extend play time.'),
 ('C08','rain_reschedule','Heavy rain prevents arrival; can I reschedule?','Rain rescheduling requires staff review and an available replacement slot; no automatic refund is recorded.'),
 ('C08','closure_after_booking','What if the studio closes after I book?','Staff will contact the booking customer about a closure; no replacement date is guaranteed by this clause.'),
 ('C08','spectators','Can I watch my friend without playing?','A spectator must ask staff and stay in the assigned viewing area; the player booking does not admit every guest.'),
 ('C09','wrong_slip','I attached the wrong slip; what should I do?','Send the correct slip for the same booking to staff; do not use a slip from another booking.'),
 ('C09','overpayment','I paid too much; can I get the excess back?','For an overpayment ask staff to verify the excess and return it to the original payer; it is not converted to credit.'),
 ('C09','underpayment','I underpaid; what next?','Pay the exact missing balance and submit both slips for the same booking; another payer permission is not established here.'),
 ('C09','full_payment','Can I pay a deposit instead?','Full payment is required for confirmation; a deposit does not confirm the slot.'),
 ('C09','payment_verification','The payment status has not changed; what next?','Ask staff to verify the booking reference and payment timestamp; no fixed checking deadline is promised.'),
 ('C09','documents','Can I obtain a tax invoice and receipt?','Request a receipt from staff with the payment reference; a tax invoice requires separate confirmation.'),
 ('C09','payer','Can another person be the payment sender?','Another payer may pay only with the correct booking reference; every player must still provide their own check-in identification.'),
 ('C09','payment_contact','Who can I contact about a payment problem?','Contact the payment desk through the recorded channel with the booking reference.'),
 ('C09','refund','How do I request a refund?','For a refund request submit the cancellation confirmation and original payment reference to staff; return to the original payer requires approval.'),
]
records={}
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
 for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'controlled-test')['record']
for cat,intent,q,answer in cases:
 fields={'topic':cat,'intent_key':intent,'question':bi(intent),'answer':bi(answer)}
 if intent=='payer':fields['legacy_search']={'projected_facet':'payer'}
 records[intent]=create('faq','policy_'+intent,fields)
def run(q,cat,facet='owner_policy'):
 e=Engine.from_snapshot(view.snapshot());u=Understanding([MeaningTask(q,'booking' if cat=='C08' else 'payment',cat,'detail',facet)],True,'controlled_policy_matrix',{'model_called':False})
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):r=e.answer(q,'en',at='2026-10-26T12:00:00+07:00',allow_llm=False,understanding=u)
 details.append({'question':q,'category':cat,'facet':facet,'result':r});return r,e,u
def table_rows():
 with sqlite3.connect(out/'source.sqlite') as c:return {name:c.execute('SELECT * FROM "'+name.replace('"','""')+'"').fetchall() for name, in c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")}
before=table_rows()
for cat,intent,q,answer in cases:
 r,e,u=run(q,cat,'payer' if intent=='payer' else 'owner_policy');checks['source_action_'+intent]=any(c['record_id']==records[intent]['record_id'] and c['value']==answer for c in r['claims']) and all(c['record_id']==records[intent]['record_id'] for c in r['claims'])
checks['read_only_answers_do_not_write_business_database']=before==table_rows()
r,e,u=run('I underpaid; what next?','C09');snap=r['execution_contract']['request_plan']['snapshot'];task=compile_request(details[-1]['question'],u,e.index,snap).tasks[0]
for key in ['intent_key','topic','question']:
 child=copy.deepcopy(r['needs'][0]);removed=e.index.records['policy_underpayment']['fields'][key]['evidence_refs'];child['claims'][0]['evidence_refs']=[v for v in child['claims'][0]['evidence_refs'] if v not in removed];checks['policy_scope_locator_required_'+key]=bool(assess(e.index,task,child,snap,details[-1]['question'])['fatal'])
child=copy.deepcopy(r['needs'][0]);child['plan']['metadata']['policy_intents']=['overpayment'];f=next(f for f in e.index.byrecord[records['overpayment']['record_id']] if f['category']=='C09');child['claims']=[{'fact_id':f['id'],'record_id':f['record_id'],'facet':f['facet'],'value':f['value']['en'],'numeric':None,'evidence_refs':f['evidence_refs']}];ledger=assess(e.index,task,child,snap,details[-1]['question']);checks['valid_other_payment_scenario_receipt_rejected_without_target']=bool(ledger['fatal']);details.append({'challenge':'underpayment_replaced_by_overpayment_and_forged_intent','ledger':ledger})
r,e,u=run('How can I cancel my booking?','C08');snap=r['execution_contract']['request_plan']['snapshot'];task=compile_request(details[-1]['question'],u,e.index,snap).tasks[0];child=copy.deepcopy(r['needs'][0]);f=next(f for f in e.index.byrecord[records['studio_cancel']['record_id']] if f['category']=='C08');child['claims']=[{'fact_id':f['id'],'record_id':f['record_id'],'facet':f['facet'],'value':f['value']['en'],'numeric':None,'evidence_refs':f['evidence_refs']}];ledger=assess(e.index,task,child,snap,details[-1]['question']);checks['studio_action_cannot_prove_customer_permission']=bool(ledger['fatal']);details.append({'challenge':'customer_cancel_replaced_by_studio_cancel','ledger':ledger})
for cat,intent,q,answer in cases:
 if intent not in {'customer_cancel','checkin_documents','overpayment','underpayment','payer','refund'}:continue
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):natural=CommonAnswerer(view).answer(q,locale='en',at=reference_time('2026-10-26T12:00:00+07:00'),planner=None)
 details.append({'natural_question':q,'answer':natural.answer,'artifact':natural.decision_artifact});checks['natural_Common_'+intent+'_source_action']=answer in natural.answer
for cat,intent,q in [('C08','change_time','Can I change my booking time?'),('C08','change_paid_booking','I booked the wrong date; can I change it?'),('C09','overpayment','Can I request a refund for my overpayment?')]:
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):natural=CommonAnswerer(view).answer(q,locale='en',at=reference_time('2026-10-26T12:00:00+07:00'),planner=None)
 details.append({'natural_question':q,'answer':natural.answer,'artifact':natural.decision_artifact});checks['natural_specific_'+intent]=next(answer for c,i,question,answer in cases if i==intent) in natural.answer
r,_,_=run('Can I request a refund for my overpayment?','C09');checks['overpayment_scenario_not_merged_with_general_refund']={c['record_id'] for c in r['claims']}=={'policy_overpayment'} and 'not converted to credit' in r['answer']
r,_,_=run('Must a refund arrive within how many days?','C09');checks['unrecorded_refund_deadline_not_invented']=not r['claims']
procedure=create('procedure','ordered_booking_procedure',{'topic':'booking_steps','name':bi('Controlled booking guide'),'preconditions':[{'field':'booking_reference','operator':'eq','value':'required'}],'steps':[{'order':2,'instruction':bi('Submit the slot request to staff.'),'contact_id':None},{'order':1,'instruction':bi('Prepare the booking reference.'),'contact_id':None}],'required_documents':['Own identification'],'deadline_minutes':15,'outcome':bi('A submitted request still awaits staff approval; it is not a confirmed booking.')})
r,e,u=run('How do I book?','C08');checks['procedure_and_faq_variants_not_silently_merged']={'policy_booking_steps','ordered_booking_procedure'}=={c['record_id'] for c in r['claims']} and r['status']=='partial';checks['ordered_procedure_retains_conditions_documents_deadline_outcome']=all(s in r['answer'] for s in ['1. Prepare the booking reference.','2. Submit the slot request to staff.','Own identification','15','booking_reference','still awaits staff approval']) and r['answer'].index('1. Prepare')<r['answer'].index('2. Submit')
snap=r['execution_contract']['request_plan']['snapshot'];task=compile_request(details[-1]['question'],u,e.index,snap).tasks[0];child=copy.deepcopy(r['needs'][0]);child['plan']['metadata']['policy_applicability'][child['claims'][0]['fact_id']]['record_revision']=999;checks['forged_policy_validity_revision_rejected']=bool(assess(e.index,task,child,snap,details[-1]['question'])['fatal'])
store.withdraw('policy_booking_steps',actor='controlled-test');incomplete=copy.deepcopy(procedure);incomplete['fields']['preconditions']={'status':'unknown','value':None,'evidence_refs':[],'note':'Controlled gap'};save_owner_record(store,incomplete,procedure['revision'],'controlled-test');r,e,u=run('How do I book?','C08');checks['unknown_procedure_preconditions_not_presented_as_complete']=bool(r['claims']) and r['status']=='partial' and 'unconfirmed procedure' in r['answer'].lower()
snap=r['execution_contract']['request_plan']['snapshot'];task=compile_request(details[-1]['question'],u,e.index,snap).tasks[0];child=copy.deepcopy(r['needs'][0]);child['status']='answer';child['plan']['metadata'].pop('procedure_source_limits',None);checks['forged_procedure_completeness_rejected']=bool(assess(e.index,task,child,snap,details[-1]['question'])['fatal'])
for label,q in [('future_year','Can I change my booking time in 2029?'),('two_dates','Can I change my booking time on 2026-10-27 or 2026-10-28?')]:
 r,_,_=run(q,'C08');checks[label+'_requires_specific_policy_date']=not r['claims'] and r['terminal_state']=='missing_input' and 'Which date' in r['answer']
expired=copy.deepcopy(records['refund']);expired['validity']['effective_until']='2026-02-01T00:00:00+07:00';save_owner_record(store,expired,expired['revision'],'controlled-test');r,_,_=run('How do I request a refund?','C09');checks['expired_refund_policy_not_current_permission']=not r['claims'] and r['terminal_state']=='not_current'
unknown=copy.deepcopy(records['change_time']);unknown['validity']={'state':'unknown','effective_from':None,'effective_until':None};save_owner_record(store,unknown,unknown['revision'],'controlled-test');r,_,_=run('Can I change my booking time?','C08');checks['unknown_policy_interval_keeps_recorded_clause_with_explicit_limit']=bool(r['claims']) and r['status']=='partial' and 'validity' in r['answer'].lower()
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_http_calls':0,'user_data_modified':False,'controlled_source_not_empirical_accuracy':True};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
