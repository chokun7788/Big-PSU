"""Resolve financial slots from source relations, never from a nearest price."""
import re
from decimal import Decimal
from math import ceil
from .contracts import Plan
from .scope import norm,contains,requested_minutes,validity_allows
from .projection import value,title

def _labels(record):return [*title(record).values(),*sum(record.get('aliases',{}).values(),[])]

def audience_mentions(index,q):
    q=norm(q);positive=set();negative=set()
    for rid,r in index.records.items():
        if r['kind']!='audience':continue
        observed=[]
        for label in set(norm(s) for s in _labels(r)):
            if not contains(q,label):continue
            for hit in re.finditer(re.escape(label),q):
                observed.append(hit.span())
        observed=[(a,b) for a,b in observed if not any(c<=a and b<=d and d-c>b-a for c,d in observed)]
        for start,end in observed:
            before=q[max(0,start-28):start]
            if re.search(r'(?:ไม่ใช่|ไม่ได้เป็น|not(?: an?| a)?)\s*$',before):negative.add(rid)
            else:positive.add(rid)
    return positive-negative,negative

def quantity_text(index,q,facts):
    q=norm(q);labels={norm(s) for f in facts for s in f['subject'].values()}
    for f in facts:
        record=index.records.get(f['record_id'],{});service=index.records.get(value(record,'service_id')) if record else None
        if service:labels.update(norm(s) for s in title(service).values())
    for s in sorted(labels,key=len,reverse=True):q=q.replace(s,' ')
    return q

def time_constraints(q):
    """Separate an explicit billing period from requested total play time."""
    q=norm(q);number=r'\d+(?:\.\d+)?\s*(?:นาที|ชั่วโมง|minutes?|hours?|hrs?)'
    pattern=r'(?:รอบละ|ต่อรอบ)\s*'+number+'|'+number+r'\s*(?:ต่อรอบ|per session|each session|each\b)'
    hits=list(re.finditer(pattern,q,re.I));periods={requested_minutes(h[0]) for h in hits}
    remaining=q
    for h in reversed(hits):remaining=remaining[:h.start()]+' '+remaining[h.end():]
    return {'total_minutes':requested_minutes(remaining),'period_minutes':next(iter(periods)) if len(periods)==1 else None,
            'error':'conflicting_billing_periods' if len(periods)>1 else None}

def resume_financial(question,history,records):
    """Resume a displayed missing slot from trusted intent state, never facts."""
    from ..followup_scope import delivered_state
    state=delivered_state(history) or {};pending=state.get('r114_pending')
    if not isinstance(pending,dict) or pending.get('version')!=1 or pending.get('category') not in {'C06','C07'}:return None
    original=pending.get('query');roots=pending.get('root_ids',[])
    if not isinstance(original,str) or len(original)>2000 or not isinstance(roots,list) or any(rid not in records for rid in roots):return None
    q=norm(question)
    if len(q)>200:return None
    residual=q;recognized=False
    labels={norm(s) for r in records.values() if r['kind'] in {'audience','service','zone'} for s in _labels(r)}
    for s in sorted(labels,key=len,reverse=True):
        if contains(residual,s):residual=residual.replace(s,' ');recognized=True
    durations=re.compile(r'(?:รอบละ|ต่อรอบ)?\s*\d+(?:\.\d+)?\s*(?:นาที|ชั่วโมง|minutes?|hours?|hrs?)(?:\s*(?:ต่อรอบ|per session|each))?',re.I)
    if durations.search(residual):recognized=True;residual=durations.sub(' ',residual)
    if pending['category']=='C07' and re.search(r'ครึ่งวัน|เต็มวัน|half.day|full.day',residual):recognized=True;residual=re.sub(r'ครึ่งวัน|เต็มวัน|half.day|full.day',' ',residual)
    if not recognized or not re.fullmatch(r'(?:\s|[?!.,]|ครับ|ค่ะ|คะ|เป็น|สำหรับ|for|please|per session|each)*',residual):return None
    suffix=question
    constraints=time_constraints(question)
    if pending.get('slot')=='billing_period' and constraints['period_minutes'] is None and constraints['total_minutes'] is not None:suffix+=' per session'
    return original+' '+suffix

def rate_pool(index,q):
    records=index.records
    explicit={rid for rid in index.record_mentions(q) if records.get(rid,{}).get('kind')=='rate'}
    if explicit:return [f for f in index.bycat['C06'] if f['record_id'] in explicit]
    services={k:r for k,r in records.items() if r['kind']=='service'}
    games={k:r for k,r in records.items() if r['kind']=='game'}
    game_labels={norm(s) for r in games.values() for s in _labels(r)}
    service_ids=set()
    for rid,r in services.items():
        labels=[s for s in _labels(r) if norm(s) not in game_labels]
        if value(r,'platform'):labels.append(value(r,'platform'))
        if any(contains(q,s) for s in labels):service_ids.add(rid)
    game_ids={rid for rid,r in games.items() if any(contains(q,s) for s in _labels(r))}
    if not service_ids and game_ids:
        service_ids={value(r,'service_id') for r in records.values() if r['kind']=='game_service' and value(r,'game_id') in game_ids and value(r,'offered') is True}
    if not service_ids:return []
    groups,denied=audience_mentions(index,q)
    out=[]
    for f in index.bycat['C06']:
        r=records.get(f['record_id'],{})
        if r.get('kind')!='rate' or value(r,'service_id') not in service_ids:continue
        if groups and value(r,'audience_id') not in groups:continue
        if value(r,'audience_id') in denied:continue
        out.append(f)
    time=time_constraints(q);minutes=time['period_minutes'] if time['period_minutes'] is not None else time['total_minutes']
    if minutes is not None:
        exact=[f for f in out if value(records[f['record_id']],'duration_minutes')==minutes]
        if exact:out=exact
    return out

def rental_pool(index,q):
    records=index.records;zones={};groups=set();periods=set()
    for rid,r in records.items():
        if r['kind']=='zone' and any(contains(q,s) for s in _labels(r)):zones[rid]=r
        if r['kind']=='audience' and any(contains(q,s) for s in _labels(r)):groups.add(rid)
        if r['kind']=='service' and value(r,'platform') and contains(q,value(r,'platform')):
            for resource in value(r,'resource_ids') or []:
                if resource in records and value(records[resource],'zone_id') in records:
                    zid=value(records[resource],'zone_id');zones[zid]=records[zid]
    if re.search(r'ครึ่งวัน|half.day',q,re.I):periods.add('half_day')
    if re.search(r'เต็มวัน|full.day',q,re.I):periods.add('full_day')
    # Internal/external here describes organization rental groups, not a
    # student's personal hourly rate. Match only declared organization names.
    for rid,r in records.items():
        if r['kind']!='audience':continue
        shown=' '.join(_labels(r))
        if re.search(r'หน่วยงาน|organization|internal unit',shown,re.I):
            if re.search(r'ภายใน|internal',q,re.I) and re.search(r'ภายใน|internal',shown,re.I):groups.add(rid)
            if re.search(r'ภายนอก|external',q,re.I) and re.search(r'ภายนอก|external',shown,re.I):groups.add(rid)
    if not zones and not groups and not periods:return []
    out=[]
    for f in index.bycat['C07']:
        r=records.get(f['record_id'],{})
        if r.get('kind')!='rental_package':continue
        if zones and not set(zones).intersection(value(r,'zone_ids') or []):continue
        if groups and value(r,'audience_id') not in groups:continue
        if periods and value(r,'period_label') not in periods:continue
        out.append(f)
    return out

def billing(index,q,facts):
    """Return independent source-backed audience lines only with known counts."""
    records=index.records;rates=[f for f in facts if f['facet']=='amount'];groups={value(records[f['record_id']],'audience_id') for f in rates if f['record_id'] in records}
    if not groups or len(groups)<2:return None
    positives,_=audience_mentions(index,q);matched={gid:r for gid,r in records.items() if gid in groups and gid in positives}
    if len(matched)<2:return None
    lines=[];missing=[]
    for gid,r in matched.items():
        hits=[]
        for label in _labels(r):
            if not contains(q,label):continue
            pattern=re.escape(norm(label))
            suffix=re.search(pattern+r'\s*(\d+)\s*(?:คน|people|persons?|players?)',norm(q))
            prefix=re.search(r'(\d+)\s*(?:คน|people|persons?|players?)\s*'+pattern,norm(q))
            if suffix:hits.append(int(suffix[1]))
            elif prefix:hits.append(int(prefix[1]))
        if not hits or len(set(hits))!=1:missing.append(title(r));continue
        selected=[f for f in rates if value(records[f['record_id']],'audience_id')==gid]
        if len(selected)!=1:missing.append(title(r));continue
        lines.append({'fact_id':selected[0]['id'],'persons':hits[0]})
    if missing:return Plan(category='C06',status='missing_input',reason='per_audience_counts_or_service_required',locked=True,metadata={'missing_slots':['persons_per_audience'],'choices':missing})
    return lines

def unit_calculation(index,fact,question):
    """Apply only declared period arithmetic and reject undeclared rounding."""
    q=quantity_text(index,question,[fact]);record=index.records.get(fact['record_id'],{})
    sessions=re.search(r'(\d+)\s*รอบ|\b(\d+)\s+sessions?\b',q)
    factor=Decimal(next(x for x in sessions.groups() if x)) if sessions else Decimal(1)
    time=time_constraints(q)
    if time['error']:return {'error':time['error'],'status':'missing_input'}
    minutes=time['total_minutes'];duration=value(record,'duration_minutes') if record else None
    if time['period_minutes'] is not None and time['period_minutes']!=duration:return {'error':'requested_billing_period_not_bound','status':'missing_input'}
    rule=fact.get('calculation_rule') or (value(record,'calculation_rule') if record else None)
    if minutes is not None:
        if not duration:return {'error':'rate_duration_not_confirmed','status':'missing_source'}
        if sessions and Decimal(str(minutes))!=Decimal(duration)*factor:return {'error':'duration_and_sessions_conflict','status':'missing_input'}
        if not sessions:
            ratio=Decimal(str(minutes))/Decimal(duration)
            if ratio==1:factor=ratio
            elif rule=='linear':factor=ratio
            elif rule=='session_ceil':factor=Decimal(ceil(ratio))
            else:return {'error':'duration_arithmetic_not_declared','status':'missing_input'}
    if factor<=0:return {'error':'non_positive_quantity','status':'missing_input'}
    if rule=='no_extrapolation' and factor!=1:return {'error':'rate_disallows_extrapolation','status':'missing_source'}
    amount=Decimal(str(fact['numeric']))*factor
    if amount*100!=(amount*100).to_integral_value():return {'error':'currency_rounding_not_declared','status':'missing_source'}
    return {'amount_thb':float(amount),'billed_units':float(factor),'requested_minutes':minutes,'period_minutes':duration,'rule':rule or 'explicit_whole_sessions'}
