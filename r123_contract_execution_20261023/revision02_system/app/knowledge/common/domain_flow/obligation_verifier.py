"""Source/operation receipts, not an assertion of whole-question semantics."""
import json,re
from dataclasses import asdict
from .projection import value

VERSION='r123-obligation-verifier-v1'

def numeric_text_supported(fact,claim,calc):
    text=claim['value'];amount=claim['numeric']
    if text in fact['value'].values() and abs(float(amount)-float(fact['numeric']))<0.000001:return True
    if fact['category']!='C06' or fact['facet']!='amount':return False
    pattern=r'(?P<amount>\d+(?:\.\d+)?)\s+(?:THB(?:\s+(?:per person|per group|for the stated billing unit))?\s+for\s+(?P<count>\d+(?:\.\d+)?)\s+(?P<unit>minutes|sessions))'
    match=re.fullmatch(pattern,text,re.I)
    if match is None:
        pattern=r'(?P<amount>\d+(?:\.\d+)?)\s+บาท(?:ต่อคน|ต่อกลุ่ม|ตามหน่วยที่ระบุ)?\s+สำหรับ\s+(?P<count>\d+(?:\.\d+)?)\s+(?P<unit>นาที|รอบ)'
        match=re.fullmatch(pattern,text)
    if match is None or abs(float(match['amount'])-float(amount))>0.000001 or calc is None:return False
    if re.search(r'per person|ต่อคน',text,re.I) and not (fact.get('confirmed_per_person') or fact.get('billing_unit')=='per_person' or fact.get('calculation')=='integer_sessions_per_person'):return False
    if re.search(r'per group|ต่อกลุ่ม',text,re.I) and fact.get('billing_unit')!='per_group':return False
    expected=calc['requested_minutes'] if match['unit'] in {'minutes','นาที'} else calc['billed_units']
    return expected is not None and abs(float(match['count'])-float(expected))<0.000001

def terminal(result):
    reason=result['reason'];status=result['status']
    if reason=='request_model_budget_exhausted':return 'budget_exhausted'
    if reason=='unsupported_operation':return reason
    if reason.startswith(('invalid_compiled','source_receipt_')):return 'invalid_plan'
    return {'answer':'supported','partial':'partial','missing_input':'missing_input','missing_source':'missing_source','not_current':'not_current','unavailable':'provider_unavailable'}[status]

def assess(index,task,result,snapshot,question=''):
    claims=result['claims'];issues=[];receipts=[];fatal=[]
    for c in claims:
        f=index.byid.get(c.get('fact_id'))
        if not f or f['category']!=task.category or f['record_id']!=c.get('record_id'):
            fatal.append('source_receipt_identity_mismatch');continue
        allowed={json.dumps(r,sort_keys=True,ensure_ascii=False) for r in f.get('evidence_refs',[])+f.get('confirmation_evidence_refs',[])}
        refs=c.get('evidence_refs',[])
        if not refs or any(json.dumps(r,sort_keys=True,ensure_ascii=False) not in allowed for r in refs):
            fatal.append('source_receipt_reference_mismatch');continue
        mode='exact_source_value'
        metadata=result['plan']['metadata']
        if f.get('numeric') is None and c.get('numeric') is not None:
            fatal.append('source_receipt_numeric_mismatch');continue
        if f.get('numeric') is not None and c.get('numeric') is None:
            fatal.append('source_receipt_numeric_missing');continue
        if f.get('numeric') is not None and c.get('numeric') is not None:
            expected=f['numeric']
            calc=None
            if f['category']=='C06' and f['facet']=='amount':
                from .financial import unit_calculation
                query=metadata.get('comparison_options',{}).get(f['id'],question)
                calc=unit_calculation(index,f,query)
                if not calc.get('error'):expected=calc['amount_thb']
                elif f['id'] not in metadata.get('arithmetic_unconfirmed',[]):
                    fatal.append('source_receipt_arithmetic_unproven');continue
            if abs(float(c['numeric'])-float(expected))>0.000001:
                fatal.append('source_receipt_numeric_mismatch');continue
            if not numeric_text_supported(f,c,calc):
                fatal.append('source_receipt_value_mismatch');continue
            mode='numeric_recomputed'
        elif c.get('value') not in f['value'].values():
            if f['facet']=='specifications' and metadata.get('specification_keys'):mode='registered_specification_projection'
            elif f['id']==metadata.get('calendar_service_fact_id'):mode='registered_calendar_projection'
            else:fatal.append('source_receipt_value_mismatch');continue
        record=index.records.get(f['record_id'],{})
        receipts.append({'fact_id':f['id'],'record_id':f['record_id'],'facet':f['facet'],'record_revision':record.get('revision'),
            'snapshot':snapshot,'evidence_refs':refs,'support_level':'projected_source_refs_checked','value_validation':mode,'semantic_entailment_verified':False})
    facets={c['facet'] for c in claims};metadata=result['plan']['metadata'];obligations=[]
    for obligation in task.obligations:
        fulfilled=False;reason=None;proof=[]
        if obligation.kind=='task_completion':
            acceptable={obligation.expected}
            if task.category=='C11' and obligation.expected in {'open_periods','bookable_periods','maintenance_periods'}:acceptable.add('service_periods')
            fulfilled=bool(claims and (not obligation.expected or facets&acceptable))
            proof=[c['fact_id'] for c in claims if not obligation.expected or c['facet'] in acceptable]
            if not fulfilled:reason='requested_field_not_delivered' if claims else result['reason']
        elif obligation.kind=='duration_option':
            option=obligation.expected
            # The source period itself must exist; a 30-minute rate scaled to
            # 60 minutes cannot impersonate a separate 60-minute source option.
            relevant=[c for c in claims if c['facet'] in {'amount','duration_minutes'} and value(index.records.get(c['record_id'],{}),'duration_minutes')==option]
            fulfilled=bool(relevant and any(c['facet']=='duration_minutes' for c in relevant))
            proof=[c['fact_id'] for c in relevant]
            if not fulfilled:reason='comparison_option_not_delivered'
        elif obligation.kind=='collection_scope':
            fulfilled=bool(metadata.get('complete_set') or 'catalog_member_ids' in metadata or metadata.get('weekday_count')==7)
            if fulfilled:proof=[c['fact_id'] for c in claims]
            else:reason='collection_completeness_not_proven'
        obligations.append({**asdict(obligation),'fulfilled':fulfilled,'reason':reason,'claim_refs':proof})
    if task.capability['operation']=='compare_durations' and claims:
        options={o.expected for o in task.obligations if o.kind=='duration_option'}
        groups={}
        for c in claims:
            if c['facet']!='amount':continue
            r=index.records.get(c['record_id'],{});audience=value(r,'audience_id')
            groups.setdefault(audience,set()).add(value(r,'duration_minutes'))
            calc=metadata.get('unit_calculations',{}).get(c['fact_id'])
            if calc and calc.get('requested_minutes')!=value(r,'duration_minutes'):issues.append('comparison_option_arithmetic_scope_mismatch')
        if any(values!=options for values in groups.values()):issues.append('comparison_audience_options_incomplete')
        if not metadata.get('comparison_options'):issues.append('comparison_executor_proof_missing')
    if fatal:issues+=fatal
    if claims:
        issues+=sorted({o['reason'] for o in obligations if not o['fulfilled'] and o['reason']})
    state=terminal(result)
    if fatal:state='invalid_plan'
    elif issues and state=='supported':state='partial'
    return {'version':VERSION,'task_id':task.id,'terminal_state':state,'reason_codes':sorted(set([result['reason'],*issues])),
        'obligations':obligations,'receipts':receipts,'fatal':sorted(set(fatal)),
        'source_refs_checked':not fatal,'all_obligations_fulfilled':all(o['fulfilled'] for o in obligations),
        'whole_question_semantics_verified':False,'planned_task_coverage_only':True}
