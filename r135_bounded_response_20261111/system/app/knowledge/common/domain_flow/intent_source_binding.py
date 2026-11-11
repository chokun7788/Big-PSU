"""Bounded price-task source chain, separate from arithmetic and authority."""
from .projection import value

def price_chain(index,category,question,claims):
    if category!='C06':return {'applicable':False,'errors':[],'chains':[]}
    from .dialogue_task import platforms
    requested=set(platforms(index,question));errors=[];chains=[]
    for claim in claims:
        if claim.get('facet')!='amount':continue
        record=index.records.get(claim.get('record_id'),{})
        fact=index.byid.get(claim.get('fact_id'),{})
        service_id=value(record,'service_id') if record else None
        audience_id=value(record,'audience_id') if record else None
        service=index.records.get(service_id,{})
        audience=index.records.get(audience_id,{})
        if record.get('kind')!='rate' or fact.get('category')!='C06' or fact.get('record_id')!=claim.get('record_id') or service.get('kind')!='service' or audience.get('kind')!='audience':
            errors.append('intent_price_source_chain_invalid');continue
        source_platform=set(platforms(index,str(value(service,'platform') or '')))
        if requested and not requested.intersection(source_platform):
            errors.append('intent_price_requested_platform_mismatch');continue
        refs=claim.get('evidence_refs',[])
        for key in ['service_id','audience_id']:
            expected=record.get('fields',{}).get(key,{}).get('evidence_refs',[])
            if not expected or not all(ref in refs for ref in expected):errors.append('intent_price_relation_evidence_missing')
        chains.append({'category':'C06','facet':'amount','rate_id':record['record_id'],'service_id':service_id,'audience_id':audience_id,'requested_platforms':sorted(requested),'source_platforms':sorted(source_platform),'record_revision':record['revision'],'source_refs':refs})
    return {'applicable':True,'errors':sorted(set(errors)),'chains':chains,'authority_verified':False,'complete_intent_semantics_verified':False}
