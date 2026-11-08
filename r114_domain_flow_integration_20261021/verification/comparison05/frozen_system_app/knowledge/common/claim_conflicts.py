"""Detect contradictory typed current claims; never guess authority by recency."""
import json
from .registry import value

def detect(record_ids,snapshot,at):
    from .answer import effective
    records=snapshot['release']['records'];withdrawn=set(snapshot.get('withdrawn',[]));selected=set(record_ids)
    def identity(r):
        if r['kind']=='rate':
            keys=('service_id','audience_id','currency','unit','duration_minutes','persons_min','persons_max','calculation_rule')
            if any(value(r,k) is None for k in ('service_id','audience_id','currency','unit','duration_minutes','calculation_rule')):return None
            return ('rate',tuple(value(r,k) for k in keys))
        if r['kind']=='schedule' and r['fields'].get('zone_ids',{}).get('status')=='known':
            return ('schedule',value(r,'timezone'),tuple(sorted(value(r,'zone_ids') or [])),value(r,'weekday'))
        return None
    identities={identity(records[k]) for k in selected if k in records};identities.discard(None)
    buckets={}
    for rid,r in records.items():
        key=identity(r)
        if key not in identities or rid in withdrawn or not effective(r,at,records):continue
        if r['kind']=='rate' and r['validity']['state']!='known':continue
        fields=('amount_minor',) if r['kind']=='rate' else ('open_periods','bookable_periods','maintenance_periods')
        for field in fields:
            f=r['fields'].get(field,{})
            if f.get('status')!='known' or not f.get('evidence_refs'):continue
            buckets.setdefault((key,field),[]).append({'record_id':rid,'revision':r['revision'],'value':f['value'],'evidence_refs':f['evidence_refs']})
    typed=[{'predicate_key':key,'field':field,'alternatives':rows,'authority_resolution':'unresolved'} for (key,field),rows in buckets.items() if len({json.dumps(r['value'],sort_keys=True,ensure_ascii=False) for r in rows})>1]

    from .claim_bindings import conflicts
    return typed+conflicts(record_ids,snapshot,at)
