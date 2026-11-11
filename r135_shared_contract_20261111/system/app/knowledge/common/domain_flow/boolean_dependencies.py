"""Recompute finite calendar/live predicates from current source and request data.

No rendered yes/no, stored outcome flag or HTTP success is predicate authority.
"""
import copy,json,re
from .projection import value
from .scope import reference_time

def source_fields(index,record,keys):
 from ..registry import source_errors,pointer
 refs=[]
 for key in keys:
  field=record.get('fields',{}).get(key,{})
  if field.get('status')!='known' or not field.get('evidence_refs'):raise ValueError('source_field_unconfirmed')
  for ref in field['evidence_refs']:
   metadata,body=index.source_pairs[ref['source_id']]
   if metadata!=index.sources.get(ref['source_id']) or source_errors(metadata,body,demo=False) or pointer(json.loads(body),ref['locator'])!=field['value']:raise ValueError('source_pointer_changed')
  refs+=field['evidence_refs']
 return refs

def calendar_projection(index,source,executor,snapshot):
 """Rebuild a delivered calendar projection without depending on child metadata."""
 from .service_calendar import plan
 text=source['source_span']['text'];material=[(source.get('target_span') or {}).get('text',''),*[s['source_span']['text'] for s in source.get('slots',[])]]
 q=text+' '+' '.join(s for s in material if s and s not in text)
 if executor.get('status')!='supported' or executor.get('unresolved_obligations') or executor.get('result_scope',{}).get('snapshot')!=snapshot:raise ValueError('calendar_executor_not_complete')
 p=plan(index,q,reference_time(snapshot['reference_time']))
 if not p or p.status!='answer':raise ValueError('calendar_source_not_complete')
 refs=[]
 for fid in p.ids:
  fact=index.byid[fid];record=index.records[fact['record_id']]
  keys=['weekday','service_closed','service_slots','zone_ids'] if record['kind']=='schedule' else ['local_date','state','zone_ids']
  refs+=source_fields(index,record,keys)
  if record.get('validity',{}).get('state')!='known':raise ValueError('calendar_validity_unknown')
  claims=[c for c in executor.get('claims',[]) if c.get('fact_id')==fid]
  if len(claims)!=1:raise ValueError('calendar_claim_missing')
  if fid==p.metadata.get('calendar_service_fact_id') and claims[0].get('value') not in p.metadata['calendar_service_answer'].values():raise ValueError('calendar_projected_claim_changed')
  if not any(r.get('fact_id')==fid and r.get('record_revision')==record['revision'] and r.get('snapshot')==snapshot for r in executor.get('receipts',[])):raise ValueError('calendar_receipt_missing')
 return p,refs

def evaluate(index,source,executor,edge,snapshot,base):
 text=source['source_span']['text'];material=[(source.get('target_span') or {}).get('text',''),*[s['source_span']['text'] for s in source.get('slots',[])]]
 q=text+' '+' '.join(s for s in material if s and s not in text)
 fail=lambda reason:{**base,'reason':reason}
 try:
  at=reference_time(snapshot['reference_time'])
  if executor.get('result_scope',{}).get('snapshot')!=snapshot:return fail('prerequisite_snapshot_receipt_missing')
  from .request_verifier import observe
  if any(c['kind'] not in {'date','time','duration','weekday'} for c in observe(index,q)['constraints']):return fail('prerequisite_quantity_or_condition_scope_unverified')
  if edge['predicate']=='recorded_service_window_boolean':
   # A timetable listing has no single affirmative truth value. Neither does
   # a physical-building question or a negative/alternative question.
   if not edge.get('state_predicate_explicit') and not (re.search(r'^\s*(?:is|will)\b.+\bopen\b',text,re.I) or re.search(r'เปิด.*(?:ไหม|หรือไม่)',text)) or re.search(r'\b(?:closed|not|or)\b|ไม่เปิด|หรือปิด',text,re.I):return fail('unsupported_dependency_predicate')
   p,refs=calendar_projection(index,source,executor,snapshot);window=p.metadata.get('calendar_window_evaluation')
   if not p or p.status!='answer' or not window or type(window.get('open_entire_window')) is not bool:return fail('calendar_boolean_window_not_source_complete')
   ids=window['source_fact_ids']
   observed=window['open_entire_window'];details={'calendar_window_evaluation':window,'source_evidence_refs':refs};claim_refs=ids
  else:
   if not edge.get('state_predicate_explicit') and not (re.search(r'^\s*(?:is|will)\b.+\b(?:available|free)\b',text,re.I) or re.search(r'ว่าง.*(?:ไหม|หรือไม่)',text)) or re.search(r'\b(?:not|occupied|busy|or)\b|ไม่ว่าง',text,re.I):return fail('unsupported_dependency_predicate')
   from ..flow_context import CURRENT
   from .. import legacy_live_on_demand as bridge
   from app.booking import live_status as live
   from ..live_window_receipt import build
   from ..pinned_live_calendar import conflict
   from ..answer import effective
   ctx=CURRENT.get();day=live.resolve_live_target_date(q,reference_date=at.date());cached=ctx.live.get(('wordpress_booking',day)) if ctx else None
   if not cached or not cached.ok or cached.date!=day:return fail('live_current_request_observation_missing')
   groups=live._resource_groups_for_query(cached,q);members=[r for _,group in groups for r in group]
   if len(members)!=1:return fail('live_scalar_resource_not_unique')
   resource=members[0];bindings=[b for b in index.records.values() if b['kind']=='live_binding' and value(b,'provider')=='wordpress_booking' and value(b,'external_resource_key')==resource.resource_id]
   from .scope import requested_resources,canonical_resource
   if len({canonical_resource(r) for r in requested_resources(q)})>1:return fail('live_scalar_resource_not_unique')
   if len(bindings)!=1:return fail('live_binding_not_unique')
   binding=bindings[0];refs=source_fields(index,binding,['provider','external_resource_key','physical_pool_key','timezone','status_mapping','freshness_max_age_seconds'])
   raw=live.requested_time_window(q,cached)
   daywide=day!=at.date().isoformat() and not (raw and raw.explicit) and not re.search(r'ตอนนี้|ขณะนี้|เวลานี้|\b(?:now|currently)\b',q,re.I)
   window=live._slot_window_for_resources(groups[0][1],raw)
   if daywide or not window or live._historical_window(cached,window):return fail('live_daywide_or_historical_not_boolean_availability')
   checked=bridge.freshness_now();age=(checked-bridge.observed_time(cached.generated_at,value(binding,'timezone'))).total_seconds();ttl=value(binding,'freshness_max_age_seconds')
   if type(ttl) is not int or not 0<=age<=ttl or not effective(binding,checked,index.records):return fail('live_binding_or_observation_not_current')
   mapping={x['raw']:x['normalized'] for x in value(binding,'status_mapping')};receipt=build(cached,resource,window,raw,False,mapping,False);decision=receipt['decision']
   snap={'active':snapshot['release_id'],'epoch':snapshot['epoch'],'release':{'records':index.records,'sources':index.sources},'withdrawn':[]}
   if conflict(snap,binding,receipt):return fail('live_recorded_calendar_conflict')
   observations=executor.get('observation_receipts',[])
   if len(observations)!=1:return fail('live_scalar_receipt_not_unique')
   o=observations[0]
   if o.get('binding_id')!=binding['record_id'] or o.get('binding_revision')!=binding['revision'] or o.get('source_snapshot')!=index.snapshot_identity or o.get('target_date')!=day or o.get('requested_window')!=receipt['requested_window'] or o.get('effective_window')!=receipt['effective_window'] or o.get('payload_sha256')!=receipt['payload_sha256'] or o.get('scope_kind')!=receipt['scope_kind'] or o.get('decision')!=decision:return fail('live_receipt_differs_from_actual_request_recomputation')
   if not decision.get('verified') or decision.get('decision_kind') not in {'requested_window_availability','closed_by_provider_calendar'} or decision.get('normalized_status') not in {'free','occupied','unavailable'}:return fail('live_requested_window_not_source_complete')
   observed=decision['normalized_status']=='free';details={'window_decision':decision,'payload_sha256':receipt['payload_sha256'],'requested_window':receipt['requested_window'],'effective_window':receipt['effective_window'],'age_seconds_recomputed':age,'source_evidence_refs':refs};claim_refs=[binding['record_id']]
  outcome=observed==edge['expected_boolean']
  return {**base,'verified':True,'outcome':'true' if outcome else 'false','reason':'source_boolean_window_recomputed','observed_boolean':observed,'expected_boolean':edge['expected_boolean'],'source_claim_refs':claim_refs,**copy.deepcopy(details)}
 except (KeyError,ValueError,TypeError,AttributeError,ArithmeticError):return fail('prerequisite_boolean_source_revalidation_failed')
