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
    from .named_spans import outside,quantity_in_name
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
        out=outside(index,out,lambda text:pattern.sub(lambda m:f"{numbers[m[1].casefold()]:g} {m[2]}",text),meaning.target or None)
    for c in meaning.constraints:
        quote=c['quote']
        if c['slot'] in {'duration','sessions','persons'}:
            if quantity_in_name(index,question,quote,meaning.target or None):continue
            converted=pattern.sub(lambda m:f"{numbers[m[1].casefold()]:g} {m[2]}",quote)
            out=outside(index,out,lambda text:text.replace(quote,converted),meaning.target or None)
        rid=c.get('source_record_id');record=index.records.get(rid,{})
        if c['slot'] not in {'audience','negation'} or record.get('kind')!='audience':continue
        label=title(record)['en'] or title(record)['th']
        if not label:continue
        start=question.find(quote);before=question[max(0,start-28):start] if start>=0 else ''
        negative=c['slot']=='negation' or bool(re.search(r'ไม่ใช่|ไม่ได้เป็น|\bnot\b|\bwithout\b',quote,re.I) or re.search(r'(?:ไม่ใช่|ไม่ได้เป็น|not(?: an?| a)?)\s*$',before,re.I))
        if not contains(out,label):out+=(' not ' if negative else ' ') + label
    return out

def apply(index,question,meaning,original,at):
    if meaning is None:return original
    cat=meaning.category;facet=meaning.facet
    if cat=='C14':facet={'description':'body','date':'event_start','registration':'registration_url'}.get(facet,facet)
    if meaning.ambiguous:
        result=blocked(cat or '', 'meaning_requires_clarification','missing_input')
        if cat=='C12':
            prompt={'th':'ต้องการเช็กเครื่องหรือบริการใด และวันที่เท่าไรครับ? ตารางเวลาประจำยังยืนยันเครื่องว่างจริงไม่ได้','en':'Which machine or service and which date should I check? A regular timetable does not establish live availability.'}
        elif cat=='C05':
            prompt={'th':'ต้องการปุ่มของเกมอะไรครับ? กรุณาระบุชื่อเกมและแพลตฟอร์มที่เล่น','en':'Which game do you want controls for? Please give the game and platform.'}
        elif len({c['quote'] for c in meaning.constraints if c['slot']=='duration'})>1:
            prompt={'th':'ระยะเวลาที่ระบุแต่ละช่วงหมายถึงอะไรครับ ต้องการเล่นนานเท่าไร และช่วงใดเป็นเวลาต่อรอบ?','en':'What does each stated duration mean? Please distinguish total play time from any session length.'}
        else:
            prompt={'th':'หมายถึงเกม เครื่อง หรือบริการใดครับ? ยังไม่มีชื่อที่อ้างอิงได้ชัดเจน','en':'Which game, machine or service do you mean? I cannot identify the referent from this request.'}
        result.metadata['context_clarification']=prompt
        result.locked=True
        return result
    if cat=='C11':
        from .calendar_sets import weekly_requested,weekly_plan
        if meaning.operation=='list' and facet in {'open_periods','bookable_periods','maintenance_periods'} and weekly_requested(question):
            if facet=='open_periods' and re.search(r'เปิด|ปิด|opening|\bopen\b|\bclosed\b',question,re.I) and not re.search(r'อาคาร|พื้นที่.*เปิด|physical|building',question,re.I):return original
            return weekly_plan(index,facet,question,at,'recorded_weekly_calendar_field')
    if original.locked:return original
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
        from .control_scope import candidates
        pool=candidates(index,question,pool)
        if meaning.operation=='list' and facet=='input_bindings' and pool:
            scopes={f['record_id'] for f in pool}
            if len(scopes)>1:
                result=blocked(cat,'control_layout_scope_required','missing_input')
                result.metadata['context_clarification']={'th':'กรุณาระบุแพลตฟอร์ม พรีเซ็ต หรือเวอร์ชันที่ต้องการ เพราะมีชุดควบคุมที่บันทึกไว้มากกว่าหนึ่งชุดครับ','en':'Please specify the platform, preset or game version; more than one recorded control layout matches.'}
                return result
            result=confirmed(cat,pool,'complete_source_binding_set',complete_set=True,member_count=len(pool),operator='list')
            if any(f.get('control_source_coverage') in {'partial_official','official_needs_layout_verify','mapping_unavailable_needs_staff_capture'} for f in pool):
                result.status='partial';result.reason='source_control_layout_is_partial'
                result.metadata['complete_set']=False;result.metadata['control_layout_partial']=True
            return result
        # Single-action lookup still requires source action semantics; do not
        # turn a list of all bindings into a guessed answer to one action.
        return original
    if cat=='C04' and facet=='zone':
        if meaning.operation in {'group_list','group_count'}:
            candidates=[f for f in (pool or index.bycat[cat]) if f['facet']=='zone']
            if re.search(r'หลายโซน|มากกว่าหนึ่งโซน|multiple zones|more than one zone',question,re.I):candidates=[f for f in candidates if len(f.get('zone_ids',[]))>1]
            groups={}
            for f in candidates:
                for zid in f.get('zone_ids',[]):groups.setdefault(zid,set()).add(f['record_id'])
            if not groups:return blocked(cat,'game_zone_relations_not_recorded')
            result=confirmed(cat,candidates,'source_game_zone_groups',operator=meaning.operation,grouping_kind='zone',group_member_ids={k:sorted(v) for k,v in groups.items()},complete_set=False,relation_completeness='Counts and lists describe only confirmed game-to-zone relations.')
            result.status='partial';return result
        if meaning.operation in {'list','group_list','group_count'} and re.search(r'หลายโซน|มากกว่าหนึ่งโซน|multiple zones|more than one zone',question,re.I):
            # Only an explicit "multiple zones" qualifier supports this filter.
            if not re.search(r'หลายโซน|มากกว่าหนึ่งโซน|multiple zones|more than one zone',question,re.I):return original
            matches=[f for f in index.bycat[cat] if f['facet']=='zone' and len(f.get('zone_ids',[]))>1]
            if matches:
                result=confirmed(cat,matches,'confirmed_multi_zone_subset',operator=meaning.operation,complete_set=False,
                                 relation_completeness='Only confirmed game/service/resource/zone edges are included.')
                result.status='partial';return result
            return blocked(cat,'multi_zone_relations_not_confirmed')
        chosen=[f for f in ((pool or index.bycat[cat]) if meaning.operation=='list' else pool) if f['facet']=='zone']
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
            groups={}
            for f in chosen:
                key=str(value(index.records.get(f['record_id'],{}),'platform') or f['subject']['en'])
                groups.setdefault(key,set()).update(f.get('member_ids',[]))
            result=confirmed(cat,chosen,'recorded_catalog_operator',operator=meaning.operation,
                             catalog_member_ids=sorted({rid for f in chosen for rid in f.get('member_ids',[])}),
                             catalog_group_counts={key:len(members) for key,members in groups.items()},catalog_group_members={key:sorted(members) for key,members in groups.items()},
                             count_scope='recorded_offered_relations',complete_set=False)
            return result
    if cat=='C06' and meaning.operation=='compare' and facet=='duration_minutes':
        from .financial import rate_pool
        from .scope import requested_minutes
        durations=[c['quote'] for c in meaning.constraints if c['slot']=='duration']
        options={requested_minutes(execution_query(index,s,meaning)):s for s in durations}
        options.pop(None,None)
        if len(options)>=2 and not re.search(r'\d+\s*(?:คน|people|persons?|players?|sessions?|รอบ)',question,re.I):
            scope=question
            for text in durations:scope=scope.replace(text,' ').replace(execution_query(index,text,meaning),' ')
            fs=[f for f in rate_pool(index,scope) if value(index.records.get(f['record_id'],{}),'duration_minutes') in options and f['facet'] in {'duration_minutes','amount'}]
            if fs:
                result=confirmed(cat,fs,'source_rate_duration_comparison',operator='compare',
                    comparison_options={f['id']:execution_query(index,options[value(index.records[f['record_id']],'duration_minutes')],meaning) for f in fs},
                    comparison_scope='recorded_duration_and_rate_only')
                missing=set(options)-{value(index.records[f['record_id']],'duration_minutes') for f in fs}
                if missing:result.status='partial';result.metadata['unanswered_comparison_minutes']=sorted(missing)
                result.locked=True;return result
    # Keep financial calculations, policies, live providers and rule dependency
    # readers in control of their own conditions, even with a valid meaning plan.
    if cat in {'C06','C07','C08','C09','C10','C12','C13'}:return original
    if cat=='C02':
        # Inverse lookup owns its role filter. A scalar field on one exact
        # person still passes finish_plan's shared public/date-scope guard.
        if not original.ids and meaning.operation=='detail' and len({f['record_id'] for f in pool if index.records.get(f['record_id'],{}).get('kind')=='person'})==1:
            chosen=[f for f in pool if f['facet']==facet and index.records.get(f['record_id'],{}).get('kind')=='person']
            if chosen:return confirmed(cat,chosen,'meaning_bound_person_field',operator='detail')
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
    if cat=='C03' and re.search(r'คืออะไร|\bwhat is\b',question,re.I):
        models={f['record_id'] for f in pool if index.records.get(f['record_id'],{}).get('kind')=='equipment_model'}
        fields={'usage','device_type','quantity','location'}
        selected=[f for rid in models for f in index.byrecord[rid] if f['facet'] in fields]
        if selected:return confirmed(cat,selected,'equipment_definition_card',operator='detail')
    if cat in {'C01','C03','C04','C14'} and pool:
        if meaning.operation in {'group_count','compare','recommendation'} or meaning.operation=='count' and facet not in {'quantity','capacity_persons','service_capacity','controllers','room_seats','players_max'}:
            # Do not quietly emit a detail record for an unimplemented operator.
            return blocked(cat,'requested_operator_not_supported_by_reader')
        chosen=[f for f in pool if f['facet']==facet or f['id'] in original.ids and f['facet'] in original.facets]
        if chosen:return confirmed(cat,chosen,'meaning_bound_requested_field',operator=meaning.operation,
                                   explicit_reader_facets_preserved=original.facets)
    return original
