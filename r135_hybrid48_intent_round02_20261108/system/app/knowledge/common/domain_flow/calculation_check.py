"""Independent, bounded source arithmetic and explicit quantity verification.

Does not call the selector's financial.billing/unit_calculation helpers.
Unsupported quantity language cannot establish a calculated total.
"""
import re
from decimal import Decimal, InvalidOperation, ROUND_CEILING
from .projection import value, title

def errors(index, question, result):
    computations=result.get('computations',[])
    if not computations:return []
    problems=[];seen=set();expected_sum=Decimal(0)
    facts=[index.byid.get(c.get('fact_id')) for c in computations]
    audience_ids={value(index.records[f['record_id']],'audience_id') for f in facts if f}
    for item,fact in zip(computations,facts):
        try:
            if not fact or item['fact_id'] in seen:raise ValueError('fact identity')
            seen.add(item['fact_id']);record=index.records[fact['record_id']]
            source_rate=Decimal(str(value(record,'amount_minor')))/100
            if value(record,'currency')!='THB':raise ValueError('currency')
            service=index.records[value(record,'service_id')];audience=index.records[value(record,'audience_id')]
            text=question.casefold()
            # Names may themselves contain numbers/durations; source names are
            # entity labels, not requested play time or requested headcounts.
            for label in sorted([*title(service).values(),*sum(service.get('aliases',{}).values(),[])],key=len,reverse=True):
                if label:text=re.sub(re.escape(label.casefold()),' ',text)
            counts=list(re.finditer(r'(?<![\d.])(\d+)\s*(?:คน|people\b|persons?\b|players?\b)',text))
            if len(audience_ids)>1:
                labels=[*title(audience).values(),*sum(audience.get('aliases',{}).values(),[])]
                bound=[]
                all_labels=[]
                for aid in audience_ids:
                    a=index.records.get(aid,{})
                    for label in [*title(a).values(),*sum(a.get('aliases',{}).values(),[])]:
                        if label:all_labels.extend((m.start(),m.end(),aid) for m in re.finditer(re.escape(label.casefold()),text))
                for count in counts:
                    before=[x for x in all_labels if x[1]<=count.start() and count.start()-x[1]<=30]
                    if before and max(before,key=lambda x:x[1])[2]==value(record,'audience_id'):bound.append(count)
                if len(bound)!=1:raise ValueError('audience quantity not independently bound')
                persons=Decimal(bound[0][1])
            else:
                if len(counts)==0 and not re.search(r'(?:total|รวม).{0,35}(?:price|cost|fee|บาท|เงิน)|(?:price|cost|fee|ราคา|บาท).{0,35}(?:total|รวม)',question,re.I):
                    persons=Decimal(1)  # ordinary unit-rate presentation, not a requested party total
                elif len(counts)==1:persons=Decimal(counts[0][1])
                else:raise ValueError('explicit unique count required')
            quantity=Decimal(1) if value(record,'unit')=='per_group' else persons
            if persons<=0 or Decimal(str(item['billing_quantity']))!=quantity:raise ValueError('quantity')
            sessions=re.findall(r'(?<![\d.])(\d+)\s*(?:รอบ|sessions?\b)',text)
            times=re.findall(r'(?<![\d.])(\d+(?:\.\d+)?)\s*(นาที|ชั่วโมง|minutes?\b|hours?\b|hrs?\b)',text)
            if len(times)>1 or len(sessions)>1:raise ValueError('multiple duration roles require separate proof')
            factor=Decimal(sessions[0]) if sessions else Decimal(1)
            duration=value(record,'duration_minutes');rule=value(record,'calculation_rule')
            if times:
                minutes=Decimal(times[0][0])*(60 if times[0][1] in {'ชั่วโมง','hour','hours','hr','hrs'} else 1)
                if not duration:raise ValueError('duration')
                ratio=minutes/Decimal(str(duration))
                if sessions and ratio!=factor:raise ValueError('session/time mismatch')
                if not sessions:
                    if ratio==1 or rule=='linear':factor=ratio
                    elif rule=='session_ceil':factor=ratio.to_integral_value(rounding=ROUND_CEILING)
                    else:raise ValueError('undeclared extrapolation')
            if factor<=0 or rule=='no_extrapolation' and factor!=1:raise ValueError('billing factor')
            total=source_rate*factor*quantity
            if Decimal(str(item['unit_rate_thb']))!=source_rate or Decimal(str(item['total_thb']))!=total:raise ValueError('source arithmetic')
            expected_sum+=total
        except (KeyError,TypeError,ValueError,InvalidOperation,ZeroDivisionError):
            problems.append('hybrid_independent_calculation_unproven')
    # An output-only mutation must not survive a perfectly valid receipt.
    totals=re.findall(r'(?:^|\n)(?:Total:\s*|รวม\s*)([\d,]+(?:\.\d+)?)\s*(?:THB|บาท)',result.get('answer',''),re.I)
    if any(Decimal(t.replace(',',''))!=expected_sum for t in totals):problems.append('hybrid_rendered_total_mismatch')
    return sorted(set(problems))


def duration_proofs(index, task, executor, ledger, snapshot, expected):
    """One explicit period, one source rate; authority may remain unconfirmed.

    A partial public status must not erase arithmetic that is independently
    source-checked. This establishes duration application only, not a complete
    purchase, current publication, or another task's requested time.
    """
    if task.get('category')!='C06' or executor.get('task_id')!=task.get('id') or executor.get('status') not in {'supported','partial'} or ledger.get('fatal'):return []
    if index.snapshot_identity!={k:snapshot.get(k) for k in ['release_id','epoch']}:return []
    question=task['source_span']['text']
    times=re.findall(r'(?<![\d.])(\d+(?:\.\d+)?)\s*(นาที|ชั่วโมง|minutes?\b|hours?\b|hrs?\b)',question,re.I)
    if len(times)!=1 or re.search(r'\d+\s*(?:รอบ|sessions?\b)',question,re.I):return []
    minutes=Decimal(times[0][0])*(60 if times[0][1].casefold() in {'ชั่วโมง','hour','hours','hr','hrs'} else 1)
    if minutes!=Decimal(str(expected)):return []
    claims=[c for c in executor.get('claims',[]) if c.get('facet')=='amount']
    calculations=executor.get('calculation_receipts',[])
    if len(claims)!=1 or len(calculations)!=1:return []
    claim=claims[0];calc=calculations[0];fact=index.byid.get(claim.get('fact_id'),{})
    record=index.records.get(claim.get('record_id'),{})
    try:
        if record.get('kind')!='rate' or fact.get('record_id')!=record['record_id'] or calc['fact_id']!=claim['fact_id']:return []
        if errors(index,question,{'computations':[calc]}):return []
        period=Decimal(str(value(record,'duration_minutes')));ratio=minutes/period
        rule=value(record,'calculation_rule')
        if ratio==1 or rule=='linear':units=ratio
        elif rule=='session_ceil':units=ratio.to_integral_value(rounding=ROUND_CEILING)
        else:return []
        amount=Decimal(str(value(record,'amount_minor')))/100*units
        unit=calc['unit_calculation']
        if any(Decimal(str(unit[k]))!=v for k,v in [('requested_minutes',minutes),('period_minutes',period),('billed_units',units),('amount_thb',amount)]):return []
        if unit.get('rule')!=(rule or 'explicit_whole_sessions') or Decimal(str(claim['numeric']))!=amount:return []
        if calc.get('transformation')!='decimal_source_declared_billing_v2' or calc.get('snapshot')!=snapshot or calc.get('evidence_refs')!=fact.get('evidence_refs') or calc.get('input_claim_refs')!=[fact['id']]:return []
        for receipt in ledger.get('receipts',[]):
            if receipt.get('fact_id')!=fact['id'] or receipt.get('record_revision')!=record['revision'] or receipt.get('snapshot')!=snapshot:continue
            scope=receipt.get('requested_scope',{})
            if not scope.get('verified') or record['record_id'] not in scope.get('allowed_record_ids',[]) or receipt.get('value_validation')!='numeric_recomputed':continue
            refs=receipt.get('evidence_refs',[])
            if not all(ref in refs for ref in fact.get('evidence_refs',[])):continue
            required=['/duration_minutes']+(['/calculation_rule'] if ratio!=1 else [])
            if not all(any(ref.get('locator','').endswith(key) for ref in refs) for key in required):continue
            return [{'fact_id':fact['id'],'basis':'single_rate_duration_independently_recomputed_from_source_and_receipt','value':expected,'record_revision':record['revision'],'authority_verified':False}]
    except (KeyError,TypeError,ValueError,InvalidOperation,ZeroDivisionError):pass
    return []
