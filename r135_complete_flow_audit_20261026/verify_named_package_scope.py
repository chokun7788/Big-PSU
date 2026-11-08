"""Actual named-package predicates and independent source counterfactuals."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.package_intent import request,price_scenario
from app.knowledge.common.domain_flow.request_verifier import observe,verify
from app.knowledge.common.domain_flow.projection import value,title
O=R/('named_package_scope_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite')
a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);b.close();a.close()
store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);snapshot=view.snapshot();e=Engine.from_snapshot(snapshot);checks={};details=[]
W=R/'training_review_workbench_1793037663397671000';examples=[json.loads(x) for x in (W/'review_round_012/EXAMPLES.jsonl').read_text('utf8').splitlines()];lookup={x['annotation_provenance']['historical_review_ref']['line']-1:x for x in examples}
cases={208:('package_8','room_seats'),209:('package_5','duration_minutes'),210:('package_9','amount_thb'),211:('package_11','room_seats'),212:('package_0','equipment_included'),213:('package_15','equipment_included'),214:('package_3','duration_minutes'),215:('package_2','room_seats'),216:('package_22','equipment_included'),217:('package_3','equipment_included'),218:('package_17','equipment_included'),219:('package_12','equipment_included')}
def run(q,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP/model forbidden')):r=CommonAnswerer(source or view).answer(q,locale='auto',at='2026-10-27T10:00:00+07:00',planner=None)
 c=r.decision_artifact['execution_contract'];tasks=c['request_plan']['tasks'];claims=[claim for x in c['executor_results'] for claim in x.get('claims',[])];details.append({'q':q,'answer':r.answer,'artifact':r.decision_artifact});return r,tasks,claims
for row,(rid,facet) in cases.items():
 q=lookup[row]['raw_question'];r,tasks,claims=run(q);key='row'+str(row)
 checks[key+'_one_local_package_field']=len(tasks)==1 and tasks[0]['category']=='C07' and tasks[0]['facet']==facet and tasks[0]['operation']!='bounded_compatibility'
 checks[key+'_only_exact_source_package_claim']=bool(claims) and all(c['record_id']==rid and c['facet']==facet for c in claims)
 seen=observe(e.index,q);checks[key+'_independent_observer_no_inventory_or_session_rate']=len(seen['needs'])==1 and seen['needs'][0]['category']=='C07' and seen['needs'][0]['facet']==facet
 checks[key+'_name_component_not_independent_platform_or_service']=not any(s['slot'] in {'platform','service'} for t in tasks for s in t.get('slots',[]))
q=lookup[210]['raw_question'];r,tasks,claims=run(q);contract=r.decision_artifact['execution_contract'];rows=contract['verifier_result']['constraint_coverage']['constraints'];checks['sole_hypothetical_package_price_scenario_recomputed']=len(rows)==1 and rows[0]['status']=='structurally_supported' and any(p['basis']=='sole_hypothetical_named_package_unit_price_source_recomputed' and not p['permission_or_booking_confirmed'] for p in rows[0]['proof'])
children=[{'claims':copy.deepcopy(ex['claims']),'execution_contract':copy.deepcopy(next(t for t in contract['tasks'] if t['task_id']==ex['task_id']))} for ex in contract['executor_results']]
for key,change in [('amount',lambda c:c[0]['claims'][0].update(numeric=98765)),('record',lambda c:c[0]['claims'][0].update(fact_id='C07:package_8:amount_thb',record_id='package_8')),('revision',lambda c:c[0]['execution_contract']['receipts'][0].update(record_revision=98765)),('clock',lambda c:c[0]['execution_contract']['receipts'][0]['snapshot'].update(reference_time='2035-01-01T00:00:00+07:00')),('no_receipt',lambda c:c[0]['execution_contract'].update(receipts=[]))]:
 bad=copy.deepcopy(children);change(bad);checked=verify(e.index,q,contract,r.answer,bad);checks['scenario_forged_'+key+'_not_verified']=all(x['status']=='review_required' for x in checked['constraint_coverage']['constraints'])
name9=title(snapshot['release']['records']['package_9'])['th']
for n,question in enumerate(['หากได้รับอนุญาตให้เช่า '+name9+' ต้องจ่ายกี่บาท','ผมไม่ใช่หน่วยงานภายนอก ถ้าเช่า '+name9+' ต้องจ่ายกี่บาท','ถ้าเช่า '+name9+' 2 แพ็กเกจ ต้องจ่ายกี่บาท','ถ้าเช่า '+name9+' แล้วคืนเงินได้ไหม']):checks['additional_condition_or_quantity_'+str(n)+'_not_sole_unit_scenario']=price_scenario(e.index,question) is None
record=snapshot['release']['records']['package_8'];name=title(record)['en'];r,tasks,claims=run('How many seats are in '+name+'?');checks['english_full_source_name_retains_package_seats']=len(tasks)==1 and any(c['record_id']=='package_8' and c['facet']=='room_seats' and c['numeric']==value(record,'room_seats') for c in claims)
th=title(snapshot['release']['records']['package_15'])['th'];r,tasks,claims=run('แพ็กเกจ '+th+' มีอุปกรณ์อะไรให้; What is Nintendo Switch OLED used for?');checks['real_package_and_equipment_siblings_both_preserved']={t['category'] for t in tasks}=={'C07','C03'} and 'Nintendo Switch 1' in r.answer and 'ครอบครัว' in r.answer
r,tasks,claims=run('VR เล่น 30 นาที ราคาเท่าไหร่');checks['ordinary_play_fee_stays_C06']=any(t['category']=='C06' for t in tasks) and not any(t['category']=='C07' for t in tasks)
r,tasks,claims=run('ใน Nintendo Switch Zone มีอุปกรณ์อะไรบ้าง');checks['real_zone_inventory_stays_C03']=any(t['category']=='C03' for t in tasks) and 'TV 86' in r.answer
for q in ['Can I plug my laptop into a power outlet?','What is Nintendo Switch OLED used for?','What games are in VR Zone?']:
 checks['unrelated_predicate_not_package_'+str(len(checks))]=request(e.index,q) is None
edited=copy.deepcopy(snapshot['release']['records']['package_15']);edited['fields']['equipment_included']['value']={'th':'รายการจากแหล่งแพ็กเกจที่แก้แล้ว','en':'Edited package inclusion'};save_owner_record(store,edited,edited['revision'],'isolated-source-control')
r,tasks,claims=run(lookup[213]['raw_question']);checks['actual_owner_package_field_edit_changes_answer']='รายการจากแหล่งแพ็กเกจที่แก้แล้ว' in r.answer and 'Nintendo Switch 1' not in r.answer and all(c['record_id']=='package_15' for c in claims)
unknown=copy.deepcopy(snapshot['release']['records']['package_8']);unknown['fields']['room_seats'].update(status='unknown',value=None,evidence_refs=[]);save_owner_record(store,unknown,unknown['revision'],'isolated-source-control')
r,tasks,claims=run(lookup[208]['raw_question']);checks['unknown_package_seats_not_replaced_with_zone_or_device_capacity']=len(tasks)==1 and tasks[0]['category']=='C07' and r.decision_artifact['response_type']!='retry' and not any(c.get('facet')=='room_seats' for c in claims) and '34' not in r.answer
renamed=copy.deepcopy(view.snapshot()['release']['records']['package_8']);renamed['fields']['room_seats']=copy.deepcopy(record['fields']['room_seats']);renamed['fields']['name']['value']={'th':'แพ็กเกจสำหรับงานทดลององค์กร','en':'Experimental organization package'};save_owner_record(store,renamed,renamed['revision'],'isolated-source-control')
r,tasks,claims=run('แพ็กเกจสำหรับงานทดลององค์กร มีที่นั่งกี่ที่');checks['new_owner_package_name_needs_no_training']=len(tasks)==1 and tasks[0]['category']=='C07' and any(c['record_id']=='package_8' and c['numeric']==34 for c in claims)
report={'all_passed':all(checks.values()),'checks':checks,'actual_HTTP_or_model_inferences':0,'actual_owner_or_frozen_source_modified':False,'whole_rental_semantics_accepted':False,'remaining':'Arbitrary conditions/quantities, missing targets, runtime-model/paired/final category and source-validity acceptance remain separate.'}
(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(O),'all_passed':report['all_passed'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v]}));assert report['all_passed']
