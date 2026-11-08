"""Boundary and applicability controls for owner and provider interval unions."""
import copy,dataclasses,json,time
from verification_support import R
from app.booking.live_status import LiveBookingSnapshot,LiveResource,LiveSlot,TimeWindow,is_open_for_window,_historical_window
from app.knowledge.common.live_window_receipt import build
from app.knowledge.common.pinned_live_calendar import conflict
from app.knowledge.common.registry import template
clock='2026-10-28T10:00:00+07:00';window=TimeWindow('10:00','11:30',True)
resource=LiveResource('15','PC2',1,'available',1,(LiveSlot('09:00','12:00','available',0,0,1),))
snapshot=LiveBookingSnapshot(ok=True,date='2026-10-28',now=clock,generated_at=clock,source='controlled_interval_fixture',center_open=True,center_reason='controlled',open_periods=(('09:00','11:00'),('11:00','12:00')),resources=(resource,))
mapping={'available':'free','busy':'occupied','closed':'unavailable'};checks={}
receipt=build(snapshot,resource,window,window,False,mapping)
checks['adjacent_provider_periods_do_not_create_false_closure']=is_open_for_window(snapshot,window) and receipt['decision']['normalized_status']=='free'
gap=dataclasses.replace(snapshot,open_periods=(('09:00','10:30'),('11:00','12:00')))
checks['real_provider_gap_not_whole_window_free']=not is_open_for_window(gap,window) and build(gap,resource,window,window,False,mapping)['decision']['normalized_status']=='unavailable'
past=dataclasses.replace(snapshot,date='2026-10-27');checks['midnight_24_end_is_historical_next_day_boundary']=_historical_window(past,TimeWindow('23:00','24:00',True))
def known(v):return {'status':'known','value':v,'evidence_refs':[{'source_id':'controlled_source','locator':'/controlled'}],'note':''}
record=template('schedule');record['record_id']='controlled_schedule';record['validity']={'state':'known','effective_from':'2026-10-28T09:00:00+07:00','effective_until':'2026-10-28T12:00:00+07:00'}
for key,value in {'weekday':2,'zone_ids':[],'bookable_periods':[{'start':'09:00','end':'11:00'},{'start':'11:00','end':'12:00'}]}.items():record['fields'][key]=known(value)
owner={'active':'controlled_interval_source','epoch':1,'withdrawn':[],'release':{'records':{'controlled_schedule':record}}};binding={'fields':{'physical_pool_key':known(None)}}
checks['adjacent_owner_bookable_periods_no_false_conflict']=conflict(owner,binding,receipt) is None
record['fields']['bookable_periods']=known([{'start':'09:00','end':'10:30'},{'start':'11:00','end':'12:00'}]);proof=conflict(owner,binding,receipt)
checks['known_current_booking_gap_has_source_bound_conflict']=proof is not None and proof['record_ids']==['controlled_schedule'] and not proof['authority_winner_selected']
record['validity']['effective_until']='2026-10-28T11:00:00+07:00';record['fields']['bookable_periods']=known([{'start':'09:00','end':'11:00'}])
checks['expired_tail_not_used_to_prove_contradiction']=conflict(owner,binding,receipt) is None
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_provider_calls':0,'controlled_scope_kernel_only':True,'user_data_changes':0};out=R/('interval_boundaries_'+str(time.time_ns()));out.mkdir();(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
