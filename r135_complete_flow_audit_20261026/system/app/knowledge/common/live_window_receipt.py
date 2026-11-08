"""Aggregate provider window receipts; gaps never become an occupied result."""
import hashlib,json,re
VERSION='wordpress-window-receipt-v1'
SLOT_TERMINALS={'no_show':'occupied','past':'unavailable'}
def digest(value):return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def minutes(text,end=False):
 if end and text=='24:00':return 1440
 if not isinstance(text,str) or not re.fullmatch(r'(?:[01]\d|2[0-3]):[0-5]\d',text):raise ValueError('invalid_provider_time')
 a,b=text.split(':');return int(a)*60+int(b)

def payload(snapshot,resource):
 return {'date':snapshot.date,'now':snapshot.now,'generated_at':snapshot.generated_at,'source':snapshot.source,'transport':snapshot.transport,
         'center_open':snapshot.center_open,'open_periods':[list(x) for x in snapshot.open_periods],'resource':resource.as_dict()}

def build(snapshot,resource,window,raw_window,day_wide,mapping,historical=False):
 result={'version':VERSION,'target_date':snapshot.date,'payload':payload(snapshot,resource),'payload_sha256':digest(payload(snapshot,resource)),
    'scope_kind':'day_slots' if day_wide else 'historical_range' if historical else 'range' if window and window.end else 'point',
    'requested_window':{'start':raw_window.start,'end':raw_window.end,'explicit':raw_window.explicit} if raw_window else None,
    'effective_window':{'start':window.start,'end':window.end,'explicit':window.explicit} if window else None,
    'window_transformation':'native_provider_slot_and_existing_occupancy_contract','status_mapping':mapping,'slot_terminal_protocol':SLOT_TERMINALS}
 result['decision']=verify(result,mapping)
 return result

def verify(receipt,mapping):
 """Recompute from aggregate slot values and requested scope, never prose."""
 def unknown(reason):return {'verified':False,'normalized_status':'unknown','decision_kind':'unconfirmed','reason':reason,'available_count':None}
 if receipt.get('version')!=VERSION or receipt.get('status_mapping')!=mapping or receipt.get('slot_terminal_protocol')!=SLOT_TERMINALS:return unknown('window_receipt_protocol_mismatch')
 p=receipt.get('payload',{})
 if digest(p)!=receipt.get('payload_sha256') or p.get('date')!=receipt.get('target_date'):return unknown('window_payload_identity_mismatch')
 resource=p.get('resource',{});capacity=resource.get('capacity');slots=resource.get('slots',[])
 if type(capacity) is not int or capacity<1:return unknown('invalid_provider_capacity')
 if mapping.get(resource.get('status'),'unknown')=='unknown':return unknown('unmapped_provider_status')
 try:
  window=receipt.get('effective_window')
  scope=receipt.get('scope_kind')
  start=minutes(window['start']) if window and scope!='day_slots' else None
  end=minutes(window['end'],True) if window and window.get('end') and scope!='day_slots' else None
  all_slots=[]
  for slot in slots:
   a,b=minutes(slot['start']),minutes(slot['end'],True)
   if a>=b:raise ValueError('inverted_slot')
   if start is not None and not (a<=start<b if end is None else a<end and b>start):continue
   if any(type(slot.get(k)) is not int or slot[k]<0 for k in ['booked_count','no_show_count','available_count']) or slot['available_count']>capacity:raise ValueError('invalid_provider_count')
   state=mapping.get(slot.get('status'),SLOT_TERMINALS.get(slot.get('status'),'unknown'))
   if state=='unknown':return unknown('unmapped_provider_slot_status')
   if (state=='free')!=(slot['available_count']>0):return unknown('inconsistent_provider_slot_availability')
   all_slots.append((a,b,slot,state))
  all_slots.sort(key=lambda x:(x[0],x[1]))
  if any(a[1]>b[0] for a,b in zip(all_slots,all_slots[1:])):return unknown('overlapping_provider_slots')
  if receipt['scope_kind']=='day_slots':
   if not all_slots and p.get('center_open'):return unknown('slot_coverage_incomplete')
   return {'verified':True,'normalized_status':'unknown','decision_kind':'recorded_day_slots','reason':None,'available_count':None,'slot_count':len(all_slots),'daywide_free_or_busy_claimed':False}
  if not window:return unknown('requested_time_window_unresolved')
  start=minutes(window['start']);end=minutes(window['end'],True) if window.get('end') else None
  if end is not None and end<=start:return unknown('invalid_requested_window')
  periods=[(minutes(a),minutes(b,True)) for a,b in p.get('open_periods',[])]
  from .calendar_slots import covers
  if not p.get('center_open') or not covers(periods,start,end):
   return {'verified':True,'normalized_status':'unavailable','decision_kind':'closed_by_provider_calendar','reason':None,'available_count':0}
  matched=[row for row in all_slots if row[0]<=start<row[1]] if end is None else [row for row in all_slots if row[0]<end and row[1]>start]
  if not matched:return unknown('slot_coverage_incomplete')
  if end is not None:
   cursor=start
   for a,b,slot,state in matched:
    if a>cursor:return unknown('slot_coverage_incomplete')
    cursor=max(cursor,b)
   if cursor<end:return unknown('slot_coverage_incomplete')
  if receipt['scope_kind']=='historical_range':
   history='closed' if any(state=='unavailable' for _,_,_,state in matched) else 'booked' if any(slot['booked_count']>0 or slot['no_show_count']>0 for _,_,slot,_ in matched) else 'not_booked'
   return {'verified':True,'normalized_status':'occupied' if history=='booked' else 'unavailable' if history=='closed' else 'unknown','decision_kind':'historical_'+history,'reason':None,'available_count':None,'bookable_now_claimed':False}
  unavailable=any(state=='unavailable' for _,_,_,state in matched)
  free=not unavailable and all(state=='free' and slot['available_count']>0 for _,_,slot,state in matched)
  return {'verified':True,'normalized_status':'free' if free else 'unavailable' if unavailable else 'occupied','decision_kind':'requested_window_availability','reason':None,'available_count':min(slot['available_count'] for _,_,slot,_ in matched) if free else 0,'slot_count':len(matched)}
 except (KeyError,TypeError,ValueError):return unknown('malformed_provider_window_payload')
