"""Known service periods cannot hide unknown/conflicted opening fields."""
import copy,json,os,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.service_calendar import plan
from app.knowledge.common.domain_flow.scope import reference_time
from app.knowledge.common.answer import CommonAnswerer
O=R/('calendar_opening_warning_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'isolated.sqlite');store=CommonStore(O/'source.sqlite');store.initialize(allow_demo=False);view=DraftSnapshotView(store);checks={};details=[];clock=reference_time('2026-10-27T10:00:00+07:00');r=template('schedule');r['record_id']='controlled_tuesday';r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
for k,v in {'weekday':1,'timezone':'Asia/Bangkok','zone_ids':[],'bookable_periods':[{'start':'10:00','end':'12:00'}],'maintenance_periods':[],'service_slots':[{'code':'morning','start':'10:00','end':'12:00','state':'open','label':'Controlled morning','note':'Source play service only'}]}.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
current_version=0;conflict_refs=[]
def save(status,end='17:00'):
 global r,current_version
 r['fields']['open_periods']={'status':status,'value':[{'start':'09:00','end':end}] if status=='known' else None,'evidence_refs':copy.deepcopy(conflict_refs) if status=='conflicted' else [],'note':'Controlled physical opening status'}
 r=save_owner_record(store,copy.deepcopy(r),current_version,'controlled-opening-source')['record'];current_version=r['revision']
def engine():return Engine.from_snapshot(view.snapshot())
save('known','17:00');conflict_refs+=copy.deepcopy(r['fields']['open_periods']['evidence_refs'])
save('known','16:00');conflict_refs+=copy.deepcopy(r['fields']['open_periods']['evidence_refs'])
for status in ['conflicted','unknown','known']:
 save(status);e=engine();p=plan(e.index,'Is the studio open today?',clock);w=p.metadata.get('opening_field_scope_warning');checks[status+'_warning_exact_source_status']=(w is not None)==(status!='known')
 if w:checks[status+'_warning_revision_pinned']=w['revision']==r['revision'] and w['record_id']==r['record_id'] and w['status']==status and p.status=='partial'
 checks[status+'_source_play_periods_preserved']='10:00' in p.metadata['customer_calendar_answer']['en'] and bool(p.ids)
 checks[status+'_no_live_or_building_status_proof_fabricated']=p.metadata['calendar_semantics']=='play_service_only_not_physical_building_hours_or_live_occupancy'
 play=plan(e.index,'Is play service open today?',clock);checks[status+'_explicit_play_not_mislabeled_physical_conflict']='opening_field_scope_warning' not in play.metadata
 for locale,q in [('en','Is the studio open today?'),('th','วันนี้เปิดไหม')]:
  with patch('urllib.request.urlopen',side_effect=AssertionError('actual HTTP forbidden')):a=CommonAnswerer(view).answer(q,locale=locale,at=clock,planner=None)
  details.append({'status':status,'locale':locale,'answer':a.answer,'artifact':a.decision_artifact});first=a.answer.splitlines()[0]
  checks[status+'_'+locale+'_public_source_scope_warning']=(('conflict' in first.lower() if status=='conflicted' else 'unconfirmed' in first.lower()) if locale=='en' else ('ขัดแย้ง' in first if status=='conflicted' else 'ยังไม่มีข้อมูลยืนยัน' in first)) if status!='known' else 'conflict' not in first.lower() and 'ขัดแย้ง' not in first
save('conflicted');closure=template('closure');closure['record_id']='controlled_special_closed';closure['localization']['en_status']='agent_translated';closure['validity']=copy.deepcopy(r['validity'])
for k,v in {'local_date':'2026-10-27','state':'closed','zone_ids':[],'reason':{'th':'ปิดพิเศษตามต้นทางทดสอบ','en':'Source controlled special closure'},'open_periods':[],'bookable_periods':[]}.items():closure['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
save_owner_record(store,closure,0,'controlled-special-closure');e=engine();p=plan(e.index,'Is the studio open today?',clock)
checks['known_applicable_special_closure_not_hidden_by_weekly_warning']='opening_field_scope_warning' not in p.metadata and 'Closed' in p.metadata['customer_calendar_answer']['en']
checks['known_special_closure_has_its_own_source_receipt']=any(e.index.byid[fid]['record_id']==closure['record_id'] for fid in p.ids)
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_provider_HTTP':0,'owner_data_modified':False,'source_control_scope':'isolated actual schema sources; not final calendar semantics or all-source acceptance'};(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(O),'all_passed':report['all_passed'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v]}));assert report['all_passed']
