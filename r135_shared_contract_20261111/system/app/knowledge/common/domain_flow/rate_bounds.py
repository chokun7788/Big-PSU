"""Source-specific person bounds; services sharing a platform stay separate."""
from datetime import datetime
from .projection import value

def interval_overlaps(a,b):
    try:
        x=a['validity'];y=b['validity']
        if x['state']!='known' or y['state']!='known':return True
        start=lambda v:datetime.fromisoformat(v) if v else None
        xs,xe,ys,ye=map(start,[x.get('effective_from'),x.get('effective_until'),y.get('effective_from'),y.get('effective_until')])
        return not (xe and ys and xe<=ys or ye and xs and ye<=xs)
    except (KeyError,TypeError,ValueError):return True

def source_scope(index,fact):
    r=index.records.get(fact['record_id'],{});fields=r.get('fields',{})
    lo,hi=value(r,'persons_min'),value(r,'persons_max')
    known=type(lo) is int and type(hi) is int and 0<lo<=hi
    unknown=lo is None and hi is None and value(r,'unit') in {'per_person','per_session'}
    refs=[ref for k in ('persons_min','persons_max') for ref in fields.get(k,{}).get('evidence_refs',[])]
    if not known and not unknown:return {'allowed':False,'reason':'person_bounds_incomplete'}
    if known and any(not fields.get(k,{}).get('evidence_refs') for k in ('persons_min','persons_max')):return {'allowed':False,'reason':'person_bounds_receipts_missing'}
    group=tuple(value(r,k) for k in ('service_id','audience_id','duration_minutes','unit','currency'))
    if not group[0]:return {'allowed':False,'reason':'service_identity_missing'}
    for other_id,other in index.records.items():
        if other.get('kind')!='rate' or other_id==fact['record_id']:continue
        if tuple(value(other,k) for k in ('service_id','audience_id','duration_minutes','unit','currency'))!=group or not interval_overlaps(r,other):continue
        a,b=value(other,'persons_min'),value(other,'persons_max')
        valid=type(a) is int and type(b) is int and 0<a<=b
        if not valid or not known:return {'allowed':False,'reason':'competing_unknown_person_bounds'}
        if max(lo,a)<=min(hi,b) and ((lo,hi)!=(a,b) or value(r,'amount_minor')!=value(other,'amount_minor')):
            return {'allowed':False,'reason':'competing_person_bounds'}
    return {'allowed':True,'lower':lo,'upper':hi,'ranged':known and (lo,hi)!=(1,1),'refs':refs if known else []}

def claim_errors(index,claims):
    errors=[]
    for claim in claims:
        fact=index.byid.get(claim.get('fact_id'))
        if not fact or fact.get('category')!='C06' or fact.get('facet')!='amount':continue
        proof=source_scope(index,fact)
        if not proof['allowed']:errors.append('source_receipt_person_rate_scope_unproven');continue
        if any(ref not in claim.get('evidence_refs',[]) for ref in proof['refs']):errors.append('source_receipt_person_bounds_locator_missing')
        source=index.records[fact['record_id']]
        if any(fact.get(k)!=value(source,k) for k in ('persons_min','persons_max')):errors.append('source_receipt_projected_person_bounds_mismatch')
    return sorted(set(errors))
