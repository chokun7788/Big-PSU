"""Execute supported interpretation operators against the current fact index.

The interpreter cannot override a locked source/safety guard or create facts.
Unsupported operators are explicit scope gaps, never approximated by top-K.
"""
import re
from .readers import confirmed,blocked
from .scope import contains,norm
from .projection import value

def execution_query(index,question,meaning):
    """Normalize quoted language units, not business rules or source values."""
    from .projection import title
    out=question
    numbers={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
             'a':1,'an':1,'half an':0.5,'half a':0.5,'one and a half':1.5,
             'หนึ่ง':1,'สอง':2,'สาม':3,'สี่':4,'ห้า':5}
    words='|'.join(re.escape(k) for k in sorted(numbers,key=len,reverse=True))
    pattern=re.compile(r'(?<![a-z])('+words+r')\s*(hours?|hrs?|minutes?|sessions?|people|persons?|players?|ชั่วโมง|นาที|รอบ|คน)\b',re.I)
    # Explicit units are also available in the original text when the model
    # omitted a slot. Do not rely on a complete model slot array for arithmetic.
    # Comparative bounds are not an exact duration; leave them for clarification.
    if meaning.category in {'C06','C07'} and not re.search(r'อย่างน้อย|ไม่เกิน|น้อยกว่า|มากกว่า|\b(?:at least|less than|more than|up to|under|over)\b',out,re.I):
        out=pattern.sub(lambda m:f"{numbers[m[1].casefold()]:g} {m[2]}",out)
    for c in meaning.constraints:
        quote=c['quote']
        if c['slot'] in {'duration','sessions','persons'}:
            converted=pattern.sub(lambda m:f"{numbers[m[1].casefold()]:g} {m[2]}",quote)
            out=out.replace(quote,converted)
        rid=c.get('source_record_id');record=index.records.get(rid,{})
        if c['slot'] not in {'audience','negation'} or record.get('kind')!='audience':continue
        label=title(record)['en'] or title(record)['th']
        if not label:continue
        start=question.find(quote);before=question[max(0,start-28):start] if start>=0 else ''
        negative=c['slot']=='negation' or bool(re.search(r'ไม่ใช่|ไม่ได้เป็น|\bnot\b|\bwithout\b',quote,re.I) or re.search(r'(?:ไม่ใช่|ไม่ได้เป็น|not(?: an?| a)?)\s*$',before,re.I))
        if not contains(out,label):out+=(' not ' if negative else ' ') + label
    return out

def apply(index,question,meaning,original,at):
    if meaning is None or original.locked:return original
    cat=meaning.category;facet=meaning.facet
    if meaning.ambiguous:return blocked(cat or '', 'meaning_requires_clarification','missing_input')
    if not cat or not facet:return original
    # Use only targets actually named by the user; an interpretation is not a
    # licence to search a different record or broaden a selected game/platform.
    pool=index.bind(cat,meaning.target or question)
    if not pool:pool=index.bind(cat,question)
    coordinated=[]
    if cat=='C04':
        from .precision import coordinated_games
        coordinated=coordinated_games(index,question)
        if coordinated:pool=[f for rid in coordinated for f in index.byrecord[rid] if f['category']=='C04']
    if cat=='C05':
        for pattern,platform in [(r'\bps5\b|playstation','playstation'),(r'\bpc\b|keyboard','pc'),(r'nintendo|switch','switch')]:
            if re.search(pattern,question,re.I):
                pool=[f for f in pool if platform in norm(' '.join(f['subject'].values()))];break
        if meaning.operation=='list' and facet=='input_bindings' and pool:
            scopes={tuple(sorted(f['subject'].items())) for f in pool}
            if len(scopes)>1:return blocked(cat,'control_platform_required','missing_input')
            result=confirmed(cat,pool,'complete_source_binding_set',complete_set=True,member_count=len(pool),operator='list')
            requested=re.search(r'\b(?:the|all)\s+(\d+)\s+buttons?\b|(?:จำนวน|ทั้งหมด|ขอ)\s*(\d+)\s*ปุ่ม',question,re.I)
            if requested:
                count=int(next(s for s in requested.groups() if s is not None))
                if count!=len(pool):
                    result.status='partial';result.reason='requested_control_subset_not_identified'
                    result.metadata['requested_binding_count']=count;result.metadata['recorded_binding_entries']=len(pool)
                    result.metadata['complete_set']=False
            return result
        # Single-action lookup still requires source action semantics; do not
        # turn a list of all bindings into a guessed answer to one action.
        return original
    if cat=='C04' and facet=='zone':
        if meaning.operation in {'list','group_list','group_count'} and re.search(r'หลายโซน|มากกว่าหนึ่งโซน|multiple zones|more than one zone',question,re.I):
            # Only an explicit "multiple zones" qualifier supports this filter.
            if not re.search(r'หลายโซน|มากกว่าหนึ่งโซน|multiple zones|more than one zone',question,re.I):return original
            matches=[f for f in index.bycat[cat] if f['facet']=='zone' and len(f.get('zone_ids',[]))>1]
            if matches:
                result=confirmed(cat,matches,'confirmed_multi_zone_subset',operator=meaning.operation,complete_set=False,
                                 relation_completeness='Only confirmed game/service/resource/zone edges are included.')
                result.status='partial';return result
            return blocked(cat,'multi_zone_relations_not_confirmed')
        chosen=[f for f in pool if f['facet']=='zone']
        if chosen:
            result=confirmed(cat,chosen,'typed_game_zone_projection',operator=meaning.operation)
            missing=set(coordinated)-{f['record_id'] for f in chosen}
            if missing:
                from .projection import title
                result.status='partial';result.reason='some_game_zone_relations_unconfirmed'
                result.metadata['unanswered_targets']=[title(index.records[rid]) for rid in sorted(missing)]
            return result
        known_services=[f for f in pool if f['facet']=='studio_services']
        if known_services:
            result=confirmed(cat,known_services,'known_services_zone_relation_unconfirmed',zone_projection_missing=True)
            result.status='partial';return result
        return blocked(cat,'game_zone_relation_not_confirmed')
    if cat=='C04' and facet=='game_catalog' and meaning.operation in {'list','count','group_count','group_list'}:
        chosen=[f for f in pool if f['facet']=='game_catalog']
        if not chosen and not meaning.target:chosen=[f for f in index.bycat[cat] if f['facet']=='game_catalog']
        if chosen:
            result=confirmed(cat,chosen,'recorded_catalog_operator',operator=meaning.operation,
                             catalog_member_ids=sorted({rid for f in chosen for rid in f.get('member_ids',[])}),
                             catalog_group_counts={f['record_id']:len(f.get('member_ids',[])) for f in chosen},
                             count_scope='recorded_offered_relations',complete_set=False)
            return result
    # Keep financial calculations, policies, live providers and rule dependency
    # readers in control of their own conditions, even with a valid meaning plan.
    if cat in {'C06','C07','C08','C09','C10','C12','C13'}:return original
    if cat=='C02':
        # Inverse roles must pass the shared personnel/public-scope contract.
        # Never bypass it with a generic name projection.
        return original
    if cat=='C11':
        if re.search(r'วันนี้|พรุ่งนี้|ตอนนี้|\btoday\b|\btomorrow\b|right now|20\d\d[-/]',question,re.I):return original
        if not pool:
            # An explicit weekday may be in a quoted slot separate from target.
            pool=index.bind(cat,question)
        if not pool and facet=='maintenance_periods' and not re.search(r'จันทร์|อังคาร|พุธ|พฤหัส|ศุกร์|เสาร์|อาทิตย์|monday|tuesday|wednesday|thursday|friday|saturday|sunday',question,re.I):
            pool=index.bycat[cat]
        chosen=[f for f in pool if f['facet']==facet]
        if chosen:
            result=confirmed(cat,chosen,'interpreted_recorded_calendar_facet',operator=meaning.operation)
            result.metadata['calendar_source_limits']=['recorded_periods_only','opening_hours_and_applicability_not_inferred']
            if facet in {'open_periods','closing_time'} and any(index.records.get(f['record_id'],{}).get('fields',{}).get('open_periods',{}).get('status')=='conflicted' for f in chosen):return original
            return result
        return original
    if cat in {'C01','C03','C04','C14'} and pool:
        if meaning.operation in {'group_count','compare','recommendation'} or meaning.operation=='count' and facet not in {'quantity','capacity_persons','controllers','room_seats','players_max'}:
            # Do not quietly emit a detail record for an unimplemented operator.
            return blocked(cat,'requested_operator_not_supported_by_reader')
        chosen=[f for f in pool if f['facet']==facet or f['id'] in original.ids and f['facet'] in original.facets]
        if chosen:return confirmed(cat,chosen,'meaning_bound_requested_field',operator=meaning.operation,
                                   explicit_reader_facets_preserved=original.facets)
    return original
