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
    observed=[]
    for rid,r in index.records.items():
        if r['kind']!='audience':continue
        for label in set(norm(s) for s in _labels(r)):
            if label and contains(q,label):
                observed.extend((m.start(),m.end(),rid) for m in re.finditer(re.escape(label),q))
    observed=[(a,b,rid) for a,b,rid in observed if not any(c<=a and b<=d and d-c>b-a for c,d,_ in observed)]
    for start,end,rid in observed:
        label=q[start:end]
        if len(label)<=3 and re.fullmatch(r'[ก-๙]+',label) and (start and re.match(r'[ก-๙]',q[start-1]) or end<len(q) and re.match(r'[ก-๙]',q[end])):continue
        if label=='คนนอก':continue  # External affiliation does not uniquely establish age/student status.
        before=q[max(0,start-28):start]
        if re.search(r'(?:ไม่ใช่|ไม่ได้เป็น|not(?: an?| a)?)\s*$',before):negative.add(rid)
        else:positive.add(rid)
    return positive-negative,negative

def quantity_text(index,q,facts):
    q=norm(q);labels={norm(s) for f in facts for s in f['subject'].values()}
    for f in facts:
        record=index.records.get(f['record_id'],{});service=index.records.get(value(record,'service_id')) if record else None
        if service:labels.update(norm(s) for s in title(service).values())
    from .named_spans import spans,masked
    for s in sorted(labels,key=len,reverse=True):
        # Repeated text can name the service first and the requested duration
        # later. Mask source-bound entity positions, not every matching string.
        q=masked(index,q,s) if spans(index,q,s) else q.replace(s,' ')
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

def service_scope(index,q):
    """Bind source service identities independently from price availability."""
    from .dialogue_task import strip_negated_platforms
    q=strip_negated_platforms(q)[0]
    records=index.records
    explicit={rid for rid in index.record_mentions(q) if records.get(rid,{}).get('kind')=='rate'}
    if explicit:return {value(records[rid],'service_id') for rid in explicit if records.get(value(records[rid],'service_id'),{}).get('kind')=='service'}
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
    return {rid for rid in service_ids if records.get(rid,{}).get('kind')=='service'}


def rate_pool(index,q):
    from .dialogue_task import strip_negated_platforms
    q=strip_negated_platforms(q)[0];records=index.records
    explicit={rid for rid in index.record_mentions(q) if records.get(rid,{}).get('kind')=='rate'}
    if explicit:return [f for f in index.bycat['C06'] if f['record_id'] in explicit]
    service_ids=service_scope(index,q)
    if not service_ids:return []
    groups,denied=audience_mentions(index,q)
    if not groups and re.search(r'คนนอก|บุคคลภายนอก|external (?:visitor|user)|outsider',q,re.I):
        groups={rid for rid,r in records.items() if r['kind']=='audience' and re.search(r'general|ต่างสถาบัน|บุคคลทั่วไป', ' '.join(_labels(r)),re.I) and not re.search(r'organization|หน่วยงาน',' '.join(_labels(r)),re.I)}
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

def rental_audiences(index,q):
    positive,negative=audience_mentions(index,q)
    organizations={rid:r for rid,r in index.records.items() if r['kind']=='audience' and re.search(r'หน่วยงาน|organization|internal unit',' '.join(_labels(r)),re.I)}
    positive&=organizations.keys();negative&=organizations.keys()
    organization_context=bool(re.search(r'หน่วยงาน|\b(?:organizations?|agencies|agency|units?)\b',q,re.I))
    for pattern in [r'ภายใน|\binternal\b',r'ภายนอก|\bexternal\b']:
        groups={rid for rid,r in organizations.items() if re.search(pattern,' '.join(_labels(r)),re.I)}
        for match in re.finditer(pattern,q,re.I):
            before=q[max(0,match.start()-35):match.start()]
            negated=bool(re.search(r'(?:ไม่ใช่(?:หน่วยงาน)?|ไม่ได้เป็น(?:หน่วยงาน)?|not(?: an?| the)?)\s*$',before,re.I))
            if not negated and not organization_context:continue
            (negative if negated else positive).update(groups)
    return positive-negative,negative


def rental_units(q):
    return [{'quantity':float(m[1]),'unit':m[2],'quote':m[0],'start':m.start(),'end':m.end()} for m in re.finditer(r'(?<![\d.-])(-?\d+(?:\.\d+)?)\s*(วัน|แพ็กเกจ|days?\b|packages?\b)',q,re.I)]


def rental_pool(index,q):
    from .package_intent import mentions
    named={h['record_id'] for h in mentions(index,q)}
    if named:
        return [f for f in index.bycat['C07'] if f['record_id'] in named]
    records=index.records;zones={};groups,negative_groups=rental_audiences(index,q);periods=set()
    for rid,r in records.items():
        if r['kind']=='zone' and any(contains(q,s) for s in _labels(r)):zones[rid]=r
        if r['kind']=='service' and value(r,'platform') and contains(q,value(r,'platform')):
            for resource in value(r,'resource_ids') or []:
                if resource in records and value(records[resource],'zone_id') in records:
                    zid=value(records[resource],'zone_id');zones[zid]=records[zid]
    if re.search(r'ครึ่งวัน|half.day',q,re.I):periods.add('half_day')
    if re.search(r'เต็มวัน|full.day',q,re.I):periods.add('full_day')
    if negative_groups and not groups:return []
    if not zones and not groups and not periods:return []
    out=[]
    for f in index.bycat['C07']:
        r=records.get(f['record_id'],{})
        if r.get('kind')!='rental_package':continue
        if zones and not set(zones).intersection(value(r,'zone_ids') or []):continue
        if groups and value(r,'audience_id') not in groups:continue
        if value(r,'audience_id') in negative_groups:continue
        if periods and value(r,'period_label') not in periods:continue
        out.append(f)
    return out

def person_counts(index,q,groups):
    """Explicit per-audience counts, shared by billing and delivered slot state."""
    counts={};q=norm(q);spans=[]
    for gid in groups:
        r=index.records.get(gid,{})
        if r.get('kind')!='audience':continue
        for label in _labels(r):
            if not contains(q,label):continue
            spans.extend((m.start(),m.end(),gid) for m in re.finditer(re.escape(norm(label)),q))
    spans=[(a,b,gid) for a,b,gid in spans if not any(c<=a and b<=d and d-c>b-a for c,d,_ in spans)]
    found={}
    for a,b,gid in spans:
        suffix=re.match(r'\s*(\d+)\s*(?:คน|people|persons?|players?)',q[b:])
        prefix=re.search(r'(\d+)\s*(?:คน|people|persons?|players?)\s*$',q[:a])
        if suffix or prefix:found.setdefault(gid,set()).add(int((suffix or prefix)[1]))
    for gid,ns in found.items():
        if len(ns)==1:counts[gid]=next(iter(ns))
    return counts

def billing(index,q,facts):
    """Return independent source-backed audience lines only with known counts."""
    records=index.records;rates=[f for f in facts if f['facet']=='amount'];groups={value(records[f['record_id']],'audience_id') for f in rates if f['record_id'] in records}
    if not groups or len(groups)<2 or not re.search(r'\d+\s*(?:คน|people|persons?|players?)',q):return None
    positives,_=audience_mentions(index,q);matched={gid:r for gid,r in records.items() if gid in groups and gid in positives}
    if len(matched)<2:return None
    lines=[];missing=[];counts=person_counts(index,q,matched)
    for gid,r in matched.items():
        if gid not in counts:missing.append(title(r));continue
        selected=[f for f in rates if value(records[f['record_id']],'audience_id')==gid]
        if len(selected)>1:
            def rate_signature(f):
                rate=records[f['record_id']];service=records.get(value(rate,'service_id'),{})
                calc=unit_calculation(index,f,q)
                if calc.get('error'):return ('unresolved',f['id'])
                return (value(service,'platform'),calc['amount_thb'],f.get('billing_unit'),value(rate,'persons_min'),value(rate,'persons_max'),str(rate.get('validity')),f.get('confirmation_as_of'))
            if len({rate_signature(f) for f in selected})==1:selected=[sorted(selected,key=lambda f:f['id'])[0]]
        if len(selected)!=1:missing.append(title(r));continue
        lines.append({'fact_id':selected[0]['id'],'persons':counts[gid]})
    if missing:return Plan(category='C06',status='missing_input',reason='per_audience_counts_or_service_required',locked=True,metadata={'missing_slots':['persons_per_audience'],'choices':missing})
    return lines

def unit_calculation(index,fact,question):
    """Apply only declared period arithmetic and reject undeclared rounding."""
    q=quantity_text(index,question,[fact]);record=index.records.get(fact['record_id'],{})
    session_mentions=list(re.finditer(r'(\d+)\s*รอบ|\b(\d+)\s+sessions?\b',q))
    if len(session_mentions)>1:return {'error':'multiple_session_quantities_require_roles','status':'missing_input'}
    sessions=session_mentions[0] if session_mentions else None
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


def resource_quantities(index,question,target=None):
    """Resource counts are not sessions or people; billing applicability is separate."""
    from .named_spans import masked
    text=masked(index,question,target)
    return [{'quantity':float(m[1]),'start':m.start(),'end':m.end(),'quote':question[m.start():m.end()]} for m in re.finditer(r'(?<![\w.])(-?\d+(?:\.\d+)?)\s*(?:เครื่อง|ชุด|machines?\b|devices?\b|consoles?\b|computers?\b|PCs\b)',text,re.I)]
