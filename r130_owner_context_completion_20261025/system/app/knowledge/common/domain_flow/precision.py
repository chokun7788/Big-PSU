"""Exact identities and inverse operators over current source facts.

No answer strings, benchmark keys or source record IDs live here. Model
selection cannot substitute a nearby button, actor or title for an exact one.
"""
import re
from .scope import norm,contains
from .readers import confirmed,blocked,pending

def button_text(f):
    return norm(f.get('button_label',{}).get('en') or f['value']['en'].split(' — ')[0])

def button_codes(text):
    return set(re.findall(r'(?<![a-z0-9])(?:[lr][123]|zl|zr)(?![a-z0-9])',norm(text)))

def controls(index,q):
    pool=index.bind('C05',q)
    if not pool:return None
    for pattern,platform in [(r'\bps5\b|playstation','playstation'),(r'\bpc\b|keyboard','pc'),(r'nintendo|switch','switch')]:
        if re.search(pattern,q,re.I):
            pool=[f for f in pool if platform in norm(f.get('platform',''))];break
    codes=button_codes(q)
    # Named key expressions are read only from their binding column, never
    # from explanatory notes (R2 notes can themselves mention L1).
    labels={button_text(f) for f in pool}
    labels={s for s in labels if len(s)>1 and contains(q,s)}
    if labels:
        longest={s for s in labels if not any(s!=t and contains(t,s) for t in labels)}
    else:longest=set()
    single=re.findall(r'(?:\bbutton\s+|ปุ่ม\s*)([a-z0-9])(?=\s|[?.,]|$)',norm(q))
    single+=re.findall(r'(?<![a-z0-9])([a-z0-9])\s+button\b',norm(q))
    wanted=bool(codes or longest or single)
    if not wanted:
        from .source_operations import control_action
        return control_action(index,q,pool)
    if not pool:return blocked('C05','control_platform_not_recorded')
    if len({f['record_id'] for f in pool})>1:return blocked('C05','control_platform_required','missing_input')
    # Prefer an entire recorded chord over its component keys. A chord not in
    # the source is never answered using the closest component.
    chord=re.search(r'(?<![a-z0-9])(?:[lr][123]|zl|zr)\s*\+\s*(?:[lr][123]|zl|zr)(?![a-z0-9])',norm(q))
    if chord:
        expr=re.sub(r'\s+','',chord[0])
        chosen=[f for f in pool if re.sub(r'\s+','',button_text(f)).split('(')[0]==expr]
    elif longest and any('+' in s or '/' in s for s in longest):
        # A complete literal compound binding outranks the last single letter
        # immediately before "button" (Shift + Q / W / E / R button).
        chosen=[f for f in pool if button_text(f) in longest]
    elif codes:
        chosen=[f for f in pool if button_codes(button_text(f)) and button_codes(button_text(f))<=codes]
    elif single:
        chosen=[f for f in pool if button_text(f) in single]
    else:
        chosen=[f for f in pool if button_text(f) in longest]
    if not chosen:return blocked('C05','exact_button_not_recorded')
    result=confirmed('C05',chosen,'exact_button_reverse_lookup',operator='button_to_action',requested_button_codes=sorted(codes))
    found=set().union(*(button_codes(button_text(f)) for f in chosen))
    if codes-found:
        result.status='partial';result.metadata['unanswered_buttons']=sorted(codes-found)
    result.locked=True
    return result

def inverse_people(index,q):
    if not re.search(r'ใคร|รายชื่อ|\b(?:who|names?|list)\b',q,re.I):return None
    from .projection import value
    def role_labels(f):
        source=[*f['value'].values(),*(value(index.records[f['record_id']],'role_aliases') or [])]
        # A role may follow a source description such as 'student: Developer'.
        # Use exact source substrings, never names or inferred qualifications.
        headings={'role','position','student','intern','internship','ตำแหน่ง','หน้าที่'}
        parts=[s.strip() for label in source for s in re.split(r'[;:]',label) if len(s.strip())>=4 and norm(s) not in headings]
        return list(dict.fromkeys(source+parts))
    roles=[f for f in index.bycat['C02'] if f['facet']=='role' and any(contains(q,s) for s in role_labels(f))]
    if not roles:return None
    mentioned={norm(s) for f in roles for s in role_labels(f) if contains(q,s)}
    longest={s for s in mentioned if not any(s!=t and contains(t,s) for t in mentioned)}
    roles=[f for f in roles if any(norm(s) in longest for s in role_labels(f))]
    team_labels={norm(s) for f in index.bycat['C02'] if f['facet']=='team' for s in f['value'].values() if contains(q,s)}
    if team_labels:
        allowed={f['record_id'] for f in index.bycat['C02'] if f['facet']=='team' and any(norm(s) in team_labels for s in f['value'].values())}
        roles=[f for f in roles if f['record_id'] in allowed]
    if not roles:return blocked('C02','role_and_team_intersection_empty')
    result=confirmed('C02',roles,'inverse_role_to_people',operator='role_to_people',matched_people=len({f['record_id'] for f in roles}))
    result.locked=True
    return result

def equipment(index,q):
    keys=[k for k,pattern in [('GPU',r'\bgpu\b|การ์ดจอ'),('CPU',r'\bcpu\b|หน่วยประมวลผล'),('RAM',r'\bram\b|แรม')] if re.search(pattern,q,re.I)]
    if not keys:return None
    from .projection import value
    pool=index.bind('C03',q)
    if not pool:
        binding_q=re.sub(r'\bpcs\b','pc',norm(q))
        ids={rid for rid,r in index.records.items() if r.get('kind')=='equipment_model' and value(r,'device_type') and contains(binding_q,str(value(r,'device_type')))}
        pool=[f for rid in ids for f in index.byrecord[rid] if f['category']=='C03']
    if not pool:return None
    chosen=[f for f in pool if f['facet']=='specifications' and any(isinstance(x,dict) and str(x.get('key','')).upper() in keys for x in value(index.records[f['record_id']],'specifications') or [])]
    if not chosen:return blocked('C03','requested_hardware_component_not_recorded')
    result=confirmed('C03',chosen,'typed_hardware_component',specification_keys=keys,operator='component_lookup')
    result.locked=True;return result

def coordinated_games(index,q):
    # Resolve literal shared-prefix edition lists only, then require each
    # expanded title to match exactly one current game. Never fuzzy-match I/II.
    m=re.search(r'([^:?!]+?\b(part|chapter|episode))\s+(IV|I{1,3}|V|\d+)\s*/\s*(?:\2\s+)?(IV|I{1,3}|V|\d+)(?!\w)',q,re.I)
    if not m:return []
    from .projection import title
    found=[]
    for part in [m[3],m[4]]:
        matches=[]
        for rid,r in index.records.items():
            if r.get('kind')!='game':continue
            for s in [*title(r).values(),*sum(r.get('aliases',{}).values(),[])]:
                plain=norm(s)
                if re.search(r'\b(?:part|chapter|episode)\s+'+re.escape(norm(part))+r'$',plain) and contains(m[1]+' '+part,plain):
                    matches.append(rid);break
        if len(set(matches))!=1:return []
        found.extend(matches)
    return list(dict.fromkeys(found))

def lookup(index,cat,q):
    if cat=='C01':return center_location(index,q)
    if cat=='C04':return game_presence(index,q)
    if cat=='C05':return controls(index,q)
    if cat=='C02':return inverse_people(index,q)
    if cat=='C03':return equipment(index,q)
    return None

def ambiguous_game_variants(index,q):
    """An alias shared by different recorded editions requires a choice."""
    from .projection import title
    if coordinated_games(index,q) or re.search(r'อะไรบ้าง|ทั้งหมด|รายชื่อ|\b(?:list|all games|catalog)\b',q,re.I):return None
    hits=[]
    for rid,r in index.records.items():
        if r.get('kind')!='game':continue
        labels=[*title(r).values(),*sum(r.get('aliases',{}).values(),[])]
        labels=[re.sub(r'[!™®]','',s) for s in labels]
        lengths=[len(norm(s)) for s in labels if len(norm(s))>3 and contains(re.sub(r'[!™®]','',q),s)]
        if lengths:hits.append((max(lengths),rid))
    if not hits:return None
    longest=max(n for n,_ in hits)
    choices={rid:title(index.records[rid]) for n,rid in hits if n==longest}
    # Cosmetic punctuation alone is not an edition distinction.
    names={re.sub(r'[!™®\W_]+','',norm(t['en'] or t['th'])) for t in choices.values()}
    editions={tuple(re.findall(r'\d+|\b(?:remastered|remake|deluxe|ultimate|part\s+[ivx]+)\b',norm(t['en'] or t['th']))) for t in choices.values()}
    if len(names)<2 or len(editions)<2:return None
    result=blocked('C04','game_alias_matches_multiple_editions','missing_input');result.locked=True
    shown=' / '.join(t['en'] or t['th'] for t in choices.values())
    result.metadata.update(source_choices=choices,context_clarification={'th':'หมายถึงเกมรุ่นใดครับ: '+shown+'?','en':'Which recorded edition do you mean: '+shown+'?'})
    return result

def center_location(index,q):
    from .vocabulary import FACETS,matches
    from .projection import title
    if not (matches(FACETS['address'],q) or re.search(r'อยู่ที่หน(?:ใด|อ|$)',q)):return None
    if not re.search(r'ศูนย์|สตูดิโอ|\b(?:studio|cent(?:er|re))\b',q,re.I):
        rest=re.sub(r'ขอข้อมูลเรื่อง|ขอสอบถามหน่อยครับ|ขอข้อมูล|ครับ|ค่ะ|อยู่ที่ไหน|อยู่ที่หน|ที่อยู่|\b(?:where|is|it|located|address|please)\b|[\s?!.,:]','',q,flags=re.I)
        if rest:return None
    # A facility/device/person location is a different requested subject.
    for r in index.records.values():
        if r.get('kind') not in {'facility','equipment_model','resource','person','game'}:continue
        if any(contains(q,s) for s in [*title(r).values(),*sum(r.get('aliases',{}).values(),[])]):return None
    sources=[f for f in index.bycat['C01'] if f['facet']=='address' and index.records[f['record_id']]['kind']=='center']
    if len(sources)!=1:return None
    result=confirmed('C01',sources,'native_center_address_before_generic_location_faq')
    result.locked=True;return result

def game_presence(index,q):
    """Legacy presence intent; current game -> offered service/zone edges."""
    from app.runtime.fast_answer import _looks_like_game_availability
    from .projection import title,value
    if re.search(r'ว่าง|ตอนนี้|ปุ่ม|ควบคุม|กติกา|ราคา|\b(?:free|now|today|tomorrow|buttons?|controls?|controller|tournament|rules?|price|cost)\b',q,re.I):return None
    if not (_looks_like_game_availability(q) or re.search(r'\b(?:can|may)\s+(?:i|we)\s+play\b|\bdo you have\b|\bwhich (?:device|machine|console).{0,65}\bplay(?:ed)?\b',q,re.I)):return None
    hits=[]
    for rid,r in index.records.items():
        if r.get('kind')!='game':continue
        sizes=[len(norm(s)) for s in [*title(r).values(),*sum(r.get('aliases',{}).values(),[])] if len(norm(s))>2 and contains(q,s)]
        if sizes:hits.append((max(sizes),rid))
    if not hits:return None
    longest=max(n for n,_ in hits);games={rid for n,rid in hits if n==longest}
    if len(games)!=1:return None
    game_id=next(iter(games))
    # Cosmetic accents/punctuation in migrated duplicate titles do not make a
    # different edition. Join only exact folded full-title identities, never fuzzy titles.
    import unicodedata
    def identity(s):return re.sub(r'[^a-z0-9ก-๙]','',''.join(ch for ch in unicodedata.normalize('NFKD',norm(s)) if not unicodedata.combining(ch)))
    keys={identity(s) for s in title(index.records[game_id]).values() if s}
    equivalent={rid for rid,r in index.records.items() if r.get('kind')=='game' and keys&{identity(s) for s in title(r).values() if s}}
    fs=[f for rid in sorted(equivalent) for f in index.byrecord[rid]]
    zones={rid for rid,r in index.records.items() if r.get('kind')=='zone' and any(contains(q,s) for s in [*title(r).values(),*sum(r.get('aliases',{}).values(),[])])}
    zone_request=bool(re.search(r'โซนไหน|ที่โซนใด|which (?:studio )?zone|what zone',q,re.I))
    if zones or zone_request:
        source=[f for f in fs if f['category']=='C04' and f['facet']=='zone']
        if not source or zones and not zones<=set(source[0].get('zone_ids',[])):return blocked('C04','requested_zone_offering_not_recorded')
        result=confirmed('C04',source,'native_game_offered_in_requested_zone',operator='relation_lookup',requested_zone_ids=sorted(zones))
    else:
        source=[f for f in fs if f['category']=='C04' and f['facet']=='studio_services']
        if not source:return blocked('C04','game_offering_not_recorded')
        result=confirmed('C04',source,'native_game_offered_services',operator='relation_lookup')
    result.locked=True;return result

def validate(index,cat,q,plan):
    """Last identity check after model selection; do not certify semantics."""
    if cat=='C05' and plan.ids:
        expected=controls(index,q)
        if expected is not None and not set(plan.ids)<=set(expected.ids):return blocked(cat,'final_button_identity_mismatch')
    if any(not index.byid[k].get('evidence_refs') for k in plan.ids if k in index.byid):return blocked(cat,'final_source_reference_missing')
    plan.metadata['evidence_identity_checked']=True
    return plan
