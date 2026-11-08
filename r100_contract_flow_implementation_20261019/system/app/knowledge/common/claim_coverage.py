"""Check typed predicate coverage separately from source-pointer validity.

Only declared contracts can be verified here. Unmigrated text readers remain
explicitly scope-unverified; this is not a universal natural-language verifier.
"""
import re
from .registry import value

def evaluate(need,result,snapshot):
    art=result.decision_artifact or {};plan=art.get('query_plan') or {}
    records=((snapshot or {}).get('release') or {}).get('records',{})
    known=[o for o in art.get('obligations',[]) if o.get('status')=='known' and o.get('evidence_refs')]
    receipts=[]
    for o in known:
        rid=o.get('record_id');record=records.get(rid,{})
        receipts.append({'need_id':need.id,'record_id':rid,'field':o.get('field'),'predicate':need.predicate,'evidence_refs':o['evidence_refs'],'release_id':art.get('release_id'),'revision':record.get('revision'),'validity':record.get('validity'),'claim_entailment_verified':False})
    fields={o['field'] for o in known};predicate=need.predicate
    finding={'version':1,'predicate':predicate,'task':need.task,'decision':'scope_unverified','reason_codes':['compatibility_scope_not_migrated'],'receipts':receipts,'semantic_correctness_verified':False}
    if not result.validation.ok:
        finding.update(decision='rejected',reason_codes=list(result.validation.errors));finding['receipts']=[];return finding
    if art.get('response_type') not in {'answer','list','partial_answer'}:return finding
    selected=[records[k] for k in plan.get('record_ids',[]) if k in records]
    def field_rows(kind,keys):
        return [o for o in known if records.get(o.get('record_id'),{}).get('kind')==kind and o.get('field') in keys]
    accepted=None;reason=None
    if predicate=='game_summary':
        rows=field_rows('game',{'summary'});accepted=bool(rows);reason='game_summary_required'
        if need.record_ids and rows:accepted=all(any(o['record_id']==rid for o in rows) for rid in need.record_ids if records.get(rid,{}).get('kind')=='game')
    elif predicate=='center_location':accepted=bool(field_rows('center',{'address','building','floor','map_url'}));reason='center_location_field_required'
    elif predicate=='game_player_count':
        rows=field_rows('game_mode',{'players_min','players_max'})
        games=[k for k in need.record_ids if records.get(k,{}).get('kind')=='game']
        accepted=bool(rows) and (not games or all(any(value(records[o['record_id']],'game_id')==gid for o in rows) for gid in games));reason='linked_game_mode_count_required'
    elif predicate=='current_rate':
        rows=field_rows('rate',{'amount_minor'})
        accepted=bool(rows) and all(records[o['record_id']]['validity']['state']=='known' for o in rows);reason='current_rate_effective_period_required'
        # An exhaustive catalog with explicit missing rows is a legitimate
        # partial result. Never certify every member from one known amount.
        receipt=plan.get('set_receipt')
        if receipt:
            finding['set_coverage']={'total_members':receipt.get('total_members'),'returned_members_count':receipt.get('returned_members_count'),'unconfirmed_members':receipt.get('members_with_unconfirmed_prices',[])}
            if receipt.get('total_members')!=receipt.get('returned_members_count'):accepted=False;reason='incomplete_set_enumeration'
    elif predicate in {'bookable_period','closing_time','service_schedule'}:
        typed=bool(field_rows('schedule',{'bookable_periods'} if predicate=='bookable_period' else {'open_periods','bookable_periods'}))
        faq=[r for r in selected if r['kind']=='faq']
        declared=any(value(r,'intent_key')=='service_schedule' or re.search(r'timetable|service schedule|ตารางเวลาให้บริการ',str(value(r,'question') or {}),re.I) for r in faq)
        accepted=typed or (declared and bool(fields&{'answer'}));reason='schedule_predicate_requires_schedule_source'
        if predicate=='closing_time' and typed and not fields&{'open_periods'}:
            finding['physical_closing_confirmed']=False
    elif predicate=='booking_steps':
        if field_rows('procedure',{'steps'}):accepted=True
        else:
            faq=[r for r in selected if r['kind']=='faq']
            accepted=bool(fields&{'answer'}) and any(re.search(r'ขั้นตอน.{0,15}จอง|วิธีจอง|book(?:ing)?.{0,12}(?:steps|procedure)|how.{0,20}book',str(value(r,'question') or {})+' '+str(value(r,'intent_key') or ''),re.I) for r in faq)
        reason='booking_steps_require_procedure_source'
        # Booking eligibility/payment/cancellation are distinct tasks. Leave
        # those adapters unverified rather than rejecting a valid policy.
        if plan.get('operation')!='booking' or plan.get('role_selection') or plan.get('question_profile'):accepted=None
    elif predicate=='booking_required':
        faq=[r for r in selected if r['kind']=='faq']
        accepted=bool(fields&{'answer'}) and any(re.search(r'เดินเข้า|ต้องจอง|walk.in|booking.required|must.book',str(value(r,'question') or {})+' '+str(value(r,'intent_key') or ''),re.I) for r in faq)
        reason='booking_requirement_requires_eligibility_source'
    elif predicate=='offered_game_location':
        rows=field_rows('game_service',{'offered','service_id','installed_resource_ids'})
        games=[k for k in need.record_ids if records.get(k,{}).get('kind')=='game']
        accepted=bool(rows) and (not games or all(any(value(records[o['record_id']],'game_id')==gid for o in rows) for gid in games));reason='offering_requires_matching_game_service'
    if predicate in {'offered_game_location','current_rate','rental_package'}:
        year=re.search(r'(?:\b(?:in|for|during)\b|ในปี|ปี)\s*(20\d{2}|25\d{2})(?!\d)',need.query,re.I)
        if year:
            from app.calendar.service_calendar import now_bangkok
            requested=int(year[1]);requested=requested-543 if requested>=2500 else requested
            if requested!=now_bangkok().year and not plan.get('temporal_applicability_checked'):
                accepted=False;reason='temporal_applicability_unconfirmed'
    if art.get('source_scope_review') or plan.get('scope_limits'):
        finding['scope_limits']=plan.get('scope_limits',[])
    if accepted is True:
        finding.update(decision='contract_supported',reason_codes=[],semantic_correctness_verified=False)
        for receipt in receipts:receipt['predicate_contract_checked']=True
    elif accepted is False:
        # Missing current price is source unavailability, never a fabricated
        # number. A mismatch is blocking only when a purported answer exists.
        finding.update(decision='predicate_mismatch',reason_codes=[reason]);finding['receipts']=[]
    return finding
