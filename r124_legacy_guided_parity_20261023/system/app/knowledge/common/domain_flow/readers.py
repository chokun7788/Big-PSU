"""Domain readers: scope first, then typed fields, relations or decisions."""
import re
from datetime import timedelta
from .contracts import Plan
from .scope import norm,contains,years,requested_years,matching_subjects,resource_scope,reference_time,validity_allows,in_year,event_years
from .vocabulary import FACETS,POLICY_INTENTS,UNRECORDED_FIELDS,matches
from .projection import value,title

ALLOWED={
 'C01':{'operator','description','address','building','floor','map_url','value','office_hours','location','usage_conditions'},
 'C02':{'display_name','role','team','affiliation','period'},
 'C03':{'name','device_type','specifications','usage','location','quantity','capacity_persons','service_capacity','controllers','room_seats'},
 'C04':{'summary','official_description','genre','how_to_play','supported_platforms','studio_services','game_catalog','players_max'},
 'C05':set(),'C06':{'amount','duration_minutes'},'C07':{'amount_thb','duration_minutes','equipment_included','room_seats','terms'},
 'C08':{'owner_policy'},'C09':{'owner_policy','payer'},'C10':{'owner_policy'},
 'C11':{'open_periods','bookable_periods','maintenance_periods','local_date','reason','weekday_closing'},
 'C12':{'live_status'},'C13':{'rule_clause'},'C14':{'description','body','date','event_start','registration','registration_url','status'},
}

def pending(cat,pool,reason='semantic_interpretation_needed',facets=()):
    return Plan(category=cat,reason=reason,status='missing_source',ambiguous=bool(pool),candidates=[f['id'] for f in pool],facets=list(facets))

def confirmed(cat,fs,reason,**metadata):
    return Plan(ids=[f['id'] for f in fs],category=cat,status='answer',reason=reason,facets=list(dict.fromkeys(f['facet'] for f in fs)),metadata=metadata)

def blocked(cat,reason,status='missing_source'):
    return Plan(category=cat,status=status,reason=reason,locked=True)

def guard(index,cat,q,at):
    fs=index.bycat[cat];asked=requested_years(q)
    if cat=='C06':
        from .financial import quantity_text
        quantities=quantity_text(index,q,fs)
        if matches(r'(?<!\d)(?:-\d+|0|\d+\.\d+)\s*(?:คน|รอบ|sessions?|people|persons?|players?)',quantities):
            return Plan(category=cat,status='missing_input',reason='non_positive_quantity',locked=True,metadata={'missing_slots':['positive_quantity']})
    from .vocabulary import PREDICATE_GAPS
    predicate_gaps=PREDICATE_GAPS
    for asked_pattern,source_pattern in predicate_gaps.get(cat,[]):
        if matches(asked_pattern,q):
            supported=[f for f in fs if matches(source_pattern,' '.join([*f['subject'].values(),*f['label'].values(),*list((f.get('faq_question') or {}).values()),*f.get('declared_predicates',[]),*(f['value'].values() if cat=='C07' and f['facet']=='terms' else [])]))]
            if not supported:return blocked(cat,'requested_predicate_not_declared_by_source')
    if cat=='C11' and asked and asked!={at.year}:
        available_years=set().union(*(years(' '.join(f['value'].values())) for f in fs if f['facet']=='local_date')) if fs else set()
        if not asked<=available_years:return blocked(cat,'calendar_year_not_confirmed')
    if cat=='C14':
        real=[f for f in fs if not f.get('fixture')]
        named_fixture=[f for f in fs if f.get('fixture') and any(contains(q,s) for s in f['subject'].values())]
        if not real and not named_fixture:return blocked(cat,'no_real_news_source_for_requested_scope')
        if asked:
            pool=real+named_fixture;available_years=set().union(*(years(' '.join([*f['subject'].values(),*f['value'].values()])) for f in pool)) if pool else set()
            if not asked<=available_years:return blocked(cat,'news_year_not_confirmed')
    quoted=re.findall(r'(?:ราคา|เกม|เครื่อง|บริการ|package|game|service)\s*[“"「]([^”"」]+)[”"」]',q,re.I)
    for mention in quoted:
        if not any(contains(s,mention) for f in index.facts for s in [*f['subject'].values(),*f.get('entity_aliases',[]),*f['label'].values()]):
            return blocked(cat,'explicit_named_target_not_in_source')
    if cat in {'C06','C07'} and asked:
        # Explicit owner re-confirmation applies to the observed current year;
        # it never licenses projecting rates into unconfirmed future years.
        if asked!={at.year}:
            compatible=[f for f in fs if any(validity_allows(f,in_year(at,y)) is True for y in asked)]
            if not compatible:return blocked(cat,'no_confirmed_rate_for_requested_year','not_current')
    if cat=='C13':asked=event_years(index,q)
    if cat=='C13' and asked:
        source_years=set().union(*(event_years(index,' '.join(f['subject'].values())) for f in fs)) if fs else set()
        if not asked<=source_years:return blocked(cat,'event_year_not_in_source')
    if cat=='C12':
        scoped=resource_scope(fs,q)
        if scoped==[]:return blocked(cat,'unknown_exact_resource')
        # Unknown opaque booking references must not select a nearby machine.
        if re.search(r'(?:รายการจอง|booking|reservation).{0,30}(?:เลข|หมายเลข|number|id|#)|secret[-_]?\d+',q,re.I):
            if not any(contains(q,s) for f in fs for s in f['subject'].values()):return blocked(cat,'booking_reference_unconfirmed')
    if matches(UNRECORDED_FIELDS,q):
        # A newly supplied exact FAQ is allowed to answer the field. Otherwise
        # related records do not establish salary/serial/private credentials.
        explicit=[f for f in fs if f.get('faq_question') and any(norm(q)==norm(s) for s in f['faq_question'].values())]
        if not explicit:return blocked(cat,'requested_field_has_no_confirmed_source')
    return None

def policy(index,cat,q):
    fs=index.bycat[cat];intents=[]
    if cat=='C10':
        from app.pipeline.protected_intents import _food_facet,_asks_personal_power
        claim='food_bring' if _food_facet(q)=='food_bring_permission' else 'personal_power' if _asks_personal_power(q) else None
        selected=[f for f in fs if claim and f.get('service_policy_claim')==claim and f.get('service_policy_variant')=='general']
        if len(selected)==1:
            result=confirmed(cat,selected,'legacy_intent_current_native_policy',policy_intents=[claim],legacy_intent_only=True)
            result.locked=True;return result
    for intent,domain,source_pattern,question_pattern in POLICY_INTENTS:
        if intent=='food_consumption' and matches(r'นำ.*เข้า|ถือ.*เข้า|เอา.*เข้า|\bbring\b|ไม่ได้ถาม|ไม่ใช่ถาม|not.{0,15}ask',q):continue
        if domain==cat and matches(question_pattern,q):
            candidates=[f for f in fs if any(matches(source_pattern,s) for s in [*f['subject'].values(),' '.join(f['subject'].values())]) or f.get('policy_intent')==intent or f.get('policy_intent','').endswith('.'+intent)]
            if candidates:intents.append((intent,candidates))
    if not intents:return None
    names={x[0] for x in intents}
    if len(names)>1 and 'booking_steps' in names:intents=[x for x in intents if x[0]!='booking_steps']
    if 'studio_cancel' in names:intents=[x for x in intents if x[0]!='customer_cancel']
    # Specific scenarios dominate general actions without discarding unrelated
    # requested needs, which the outer splitter processes independently.
    if 'rain_reschedule' in names:intents=[x for x in intents if x[0] not in {'late_notice','change_paid_booking'}]
    if 'correct_booking_name' in names:intents=[x for x in intents if x[0]!='change_paid_booking']
    if 'game_failure_switch' in names:intents=[x for x in intents if x[0]!='change_service']
    if 'rental_terms' in names:intents=[x for x in intents if x[0]!='rental_contact']
    candidates=list({f['id']:f for _,group in intents for f in group}.values())
    preferred=[f for f in candidates if f.get('owner_confirmed')]
    if preferred and len(intents)==1:candidates=preferred
    # Same-language literal duplicates are one decision with several sources.
    # Keep the individual fact identity; never merge merely similar decisions.
    if candidates and len(intents)==1:
        signatures={norm(f['value'].get('th') or f['value'].get('en')) for f in candidates}
        if len(signatures)==1:
            chosen=sorted(candidates,key=lambda f:(not bool(f.get('procedure_complete')),f['id']))[0]
            return confirmed(cat,[chosen],'equivalent_literal_policy_sources',policy_intents=[x[0] for x in intents],
                             corroborating_fact_ids=sorted(f['id'] for f in candidates))
    if cat=='C08' and len(intents)==1 and names=={'booking_steps'} and candidates:
        # Present source variants explicitly. Do not ask the selector to choose
        # an authority among same-action procedure versions or silently merge.
        variants={}
        for f in candidates:variants.setdefault(norm(f['value'].get('th') or f['value'].get('en')),f)
        result=confirmed(cat,list(variants.values()),'recorded_booking_procedure_variants',policy_intents=['booking_steps'],policy_source_variants=True)
        result.status='partial';result.locked=True;return result
    # Quantified/extra predicates must have evidence of their own. A broad
    # overpayment rule does not establish a credit expiry/refund deadline.
    unsupported=r'หมดอายุ.*กี่(?:วัน|เดือน|ปี)|คืนเงิน.*ภายใน.*กี่(?:วัน|ชั่วโมง)|มัดจำ.*(?:กี่(?:บาท|เปอร์เซ็นต์)|เปอร์เซ็นต์)|(?:ค่าปรับ|โอที|ขั้นต่ำ|สูงสุด).*(?:กี่(?:บาท|ขวบ|ปี|คน)|ตายตัว)|ขั้นต่ำ.*อายุ|อายุขั้นต่ำ|guarantee|guaranteed|expires?.*days|refund.*within.*days|minimum age|fixed.*penalt'
    if matches(unsupported,q):return blocked(cat,'requested_extra_condition_unconfirmed')
    if len(candidates)==1:return confirmed(cat,candidates,'action_condition_policy',policy_intents=list(names))
    # Do not merge distinct policies merely because both contain "payment".
    return pending(cat,candidates,'multiple_policy_actions_need_disambiguation')

def tuple_pool(index,cat,q):
    direct=index.bind(cat,q)
    if direct:return direct
    scored=[]
    for f in index.bycat[cat]:
        dimensions=[x.strip() for x in f['subject'].get('th','').split(' / ')]
        dimensions+= [x.strip() for x in f['subject'].get('en','').split(' / ')]
        hits=[s for s in dimensions if contains(q,s)]
        if hits:scored.append((len(hits),sum(map(len,hits)),f))
    if not scored:return []
    top=max(n for n,_,_ in scored)
    return [f for n,length,f in scored if n==top]

def field_reader(index,cat,q,at=None):
    allfs=index.bycat[cat];pool=tuple_pool(index,cat,q) if cat in {'C06','C07'} else index.bind(cat,q)
    if cat in {'C06','C07'}:
        from .financial import rate_pool,rental_pool
        native=(rate_pool if cat=='C06' else rental_pool)(index,q)
        if native:
            explicit=matching_subjects(allfs,q)
            pool=[f for f in native if f['id'] in {x['id'] for x in explicit}] if explicit else native
    if cat=='C06':
        from .financial import audience_mentions
        positive,negative=audience_mentions(index,q)
        if negative and not positive:return Plan(category=cat,status='missing_input',reason='audience_negated_no_positive_group',locked=True,metadata={'missing_slots':['audience']})
        if negative:pool=[f for f in pool if value(index.records.get(f['record_id'],{}),'audience_id') not in negative]
        if not index.bind(cat,q):
            from .financial import rate_pool
            pool=rate_pool(index,q)
    if cat in {'C06','C07'} and not pool:
        from .financial import rate_pool,rental_pool
        pool=rate_pool(index,q) if cat=='C06' else rental_pool(index,q)
        if not pool:return Plan(category=cat,status='missing_input',reason='financial_subject_not_bound',locked=True,metadata={'missing_slots':['service' if cat=='C06' else 'rental_package']})
    if cat in {'C06','C07'} and at is not None and pool:
        asked=requested_years(q);target=in_year(at,next(iter(asked))) if len(asked)==1 else at
        current=[f for f in pool if validity_allows(f,target) is not False or f.get('confirmation_ref') and (not asked or asked=={at.year})]
        if not current:return blocked(cat,'no_effective_rate_in_bound_scope','not_current')
        pool=current
    native_policies=[f for f in pool if 'policy_complete' in f]
    if cat=='C10' and native_policies:
        if any(not f['policy_complete'] for f in native_policies):return blocked(cat,'policy_conditions_or_exceptions_not_confirmed')
        return confirmed(cat,native_policies,'typed_policy_with_all_conditions',conditions_not_assumed_met=True)
    procedures=[f for f in pool if f.get('procedure_complete')]
    if cat=='C08' and procedures:return confirmed(cat,procedures,'typed_ordered_procedure')
    if cat=='C03' and matches(r'มีอุปกรณ์อะไร|อุปกรณ์.*(?:ทั้งหมด|บ้าง)|equipment list|list.*equipment|what equipment|which devices',q):
        zones={rid:r for rid,r in index.records.items() if r['kind']=='zone' and any(contains(q,s) for s in [*title(r).values(),*sum(r.get('aliases',{}).values(),[])])}
        names=[f for f in allfs if f['facet']=='name']
        if zones:
            labels={norm(s) for r in zones.values() for s in title(r).values()}
            def in_zone(f):
                r=index.records[f['record_id']]
                return any(isinstance(s,dict) and s.get('key')=='zone' and norm(s.get('value','')) in labels for s in value(r,'specifications') or [])
            names=[f for f in names if in_zone(f)]
        if names:return confirmed(cat,names,'complete_equipment_set',zone_ids=list(zones),member_ids=[f['record_id'] for f in names],complete_set=True)
        return blocked(cat,'equipment_set_has_no_confirmed_members')
    fieldq=q
    for rid in index.record_mentions(q):fieldq=fieldq.replace(norm(rid),' ')
    if pool:
        for s in sorted({v for f in pool for v in f['subject'].values()},key=len,reverse=True):
            if contains(fieldq,s):fieldq=fieldq.replace(norm(s),' ')
    facets=set()
    for facet in ALLOWED[cat]:
        aliases=[f['label'][l] for f in pool for l in ['th','en'] if f['facet']==facet]
        if any(contains(fieldq,s) for s in aliases if len(norm(s))>=2) or (facet in FACETS and matches(FACETS[facet],fieldq)):facets.add(facet)
    if cat=='C01':
        if 'floor' in facets and matches(r'ชั้นใดของอาคาร|which floor.*building',q) and not matches(r'อาคารไหน|ตึกไหน|which building',q):facets.discard('building')
        if 'description' in facets and not any(f['facet']=='description' for f in allfs) and matches(r'ศูนย์|studio|university',q):facets.add('operator')
        # "where is the studio" is address, not every facility location.
        if 'address' in facets:
            if any(f['facet']=='address' for f in pool):facets.discard('location')
            elif any(f['facet']=='location' for f in pool):facets.discard('address');facets.add('location')
    if cat=='C03':
        if 'room_seats' in facets:facets.discard('capacity_persons')
        if 'specifications' in facets:facets.discard('device_type')
    if cat=='C04':
        if 'official_description' in facets:facets.discard('summary')
        if 'how_to_play' in facets:facets.discard('summary')
        if 'genre' in facets:facets.discard('summary')
        if 'game_catalog' in facets:facets.discard('summary');facets.discard('studio_services')
    if cat=='C06' and 'duration_minutes' in facets and not matches(r'กี่บาท|ราคา|ค่าบริการ|ค่าเล่น|\bprice\b|\bcost\b|how much|\bfee\b',fieldq):
        # "How long / เท่าไหร่ ... เป็นนาที" requests duration, not an
        # additional money amount. Explicit requests for both retain both.
        facets.discard('amount')
    if cat=='C14':
        if 'registration' in facets:facets.add('registration_url')
        if 'description' in facets:facets.add('body')
        if 'date' in facets:facets.add('event_start')
    if not pool:
        if cat=='C01' and facets:pool=allfs
        elif cat=='C04' and 'game_catalog' in facets:pool=[f for f in allfs if f['facet']=='game_catalog']
        elif cat=='C02' and matches(r'บุคลากร|รายชื่อ|staff|personnel|directory',q):pool=allfs;facets=facets or {'display_name'}
        else:return pending(cat,allfs,'entity_not_bound',facets)
    if cat=='C07' and matches(r'มัดจำ|เกินเวลา|ค่าปรับ|โอที|deposit|overtime|penalt',q):
        terms=[f for f in pool if f['facet']=='terms']
        return pending(cat,terms,'requested_rental_term_not_recorded') if terms else blocked(cat,'requested_rental_term_not_recorded')
    if cat=='C04' and matches(r'DLC|แพตช์ที่ติดตั้ง|บัญชีเกม.*ซื้อ|installed patch|purchased.*account',q):return blocked(cat,'installed_version_or_entitlement_not_recorded')
    if cat=='C05':
        # Binding labels are action semantics. Only select the longest actual
        # action mention inside the bound game/platform, never an entire map.
        hits=[]
        for f in pool:
            lengths=[len(norm(s)) for s in f['label'].values() if contains(fieldq,s)]
            if lengths:hits.append((max(lengths),f))
        if hits:
            top=max(n for n,_ in hits);return confirmed(cat,[f for n,f in hits if n==top],'exact_action_binding')
        if matches(r'auto.?win|เทเลพอร์ตอัตโนมัติ|สร้างด่านใหม่อัตโนมัติ',q):return blocked(cat,'binding_not_recorded')
        return pending(cat,pool,'action_not_bound')
    chosen=[f for f in pool if f['facet'] in facets]
    if chosen:
        if cat=='C06':
            from .financial import billing,quantity_text
            lines=billing(index,q,chosen)
            if isinstance(lines,Plan):return lines
            if lines:
                ids={x['fact_id'] for x in lines};chosen=[f for f in chosen if f['id'] in ids]
                return confirmed(cat,chosen,'typed_audience_billing',billing_lines=lines)
            quant=quantity_text(index,q,chosen)
            if len([f for f in chosen if f['facet']=='amount'])>1 and matches(r'\d+\s*(?:คน|people|persons?|players?)',quant) and matches(r'รวม|ทั้งหมด|total|ต้องจ่าย',q):
                from .financial import audience_mentions
                positives,_=audience_mentions(index,q)
                if len(positives)==1:return Plan(category=cat,status='missing_input',reason='billing_period_or_service_required',locked=True,metadata={'missing_slots':['billing_period']})
                groups={value(index.records.get(f['record_id'],{}),'audience_id') for f in chosen}
                choices=[title(index.records[k]) for k in sorted(k for k in groups if k in index.records)]
                return Plan(category=cat,status='missing_input',reason='audience_required_for_total',locked=True,metadata={'missing_slots':['audience'],'choices':choices})
        return confirmed(cat,chosen,'typed_requested_fields')
    # A newly added FAQ can be selected from its original question metadata.
    exact=[f for f in pool if f.get('faq_question') and any(norm(q)==norm(s) for s in f['faq_question'].values())]
    if exact:return confirmed(cat,exact,'exact_new_owner_question')
    return pending(cat,pool,'requested_facet_not_bound',facets)

def live_reader(index,q,at):
    fs=index.bycat['C12'];scoped=resource_scope(fs,q)
    pool=scoped if scoped is not None else index.bind('C12',q)
    if not pool:return blocked('C12','live_resource_or_time_missing','missing_input')
    # Static benchmark snapshots require the exact resource AND slot, not the
    # best nearby text. Live production reads are delegated with these slots.
    direct=matching_subjects(pool,q)
    if direct:return confirmed('C12',direct,'exact_live_snapshot')
    date=re.search(r'20\d{2}-\d{2}-\d{2}',q);clock=re.search(r'(?<!\d)([01]?\d|2[0-3]):([0-5]\d)(?!\d)',q)
    if not date or not clock:return blocked('C12','live_resource_or_time_missing','missing_input')
    slot=date[0]+' '+f'{int(clock[1]):02}:{clock[2]}'
    matched=[f for f in pool if any(slot in s for s in f['subject'].values())]
    return confirmed('C12',matched,'exact_live_resource_time') if matched else blocked('C12','no_provider_snapshot_for_requested_slot')

def rules_reader(index,q,at):
    fs=index.bycat['C13'];pool=index.bind('C13',q);asked=event_years(index,q)
    game_ids={rid for rid,r in index.records.items() if r['kind']=='game' and any(contains(q,s) for s in [*title(r).values(),*sum(r.get('aliases',{}).values(),[])])}
    if game_ids:
        scoped=[f for f in pool or fs if f.get('game_id') in game_ids]
        if not scoped:return blocked('C13','no_rules_for_requested_game')
        pool=scoped
    if asked:pool=[f for f in pool or fs if asked<=event_years(index,' '.join(f['subject'].values()))]
    if not pool:return blocked('C13','event_or_rule_not_bound','missing_input')
    events={f.get('event_id') for f in pool if f.get('event_id')}
    if len(events)>1 and not asked:return Plan(category='C13',status='missing_input',reason='event_edition_required',locked=True,metadata={'missing_slots':['event']})
    from .distilled_policy import broad_rule_family
    family=broad_rule_family(index,q,pool)
    if family is not None:return family
    fieldq=q
    for s in sorted({s for f in pool for s in f['subject'].values()},key=len,reverse=True):fieldq=fieldq.replace(norm(s),' ')
    labels=[]
    for f in pool:
        hits=[len(norm(s)) for s in f['label'].values() if len(norm(s))>2 and contains(fieldq,s)]
        if hits:labels.append((max(hits),f))
    if not labels and matches(r'\bmap\s*pool\b|แผนที่ในการแข่งขัน',fieldq):
        # A bilingual topic bridge, not map names or event-specific answers.
        labels=[(1,f) for f in pool if any(matches(r'\bmap\s*pool\b|แผนที่ในการแข่งขัน',s) for s in f['label'].values())]
    if not labels and matches(r'อุปกรณ์(?:การแข่งขัน|แข่งขัน)|competition equipment|equipment and devices',fieldq):
        # The event and game were bound above. Bridge a topic synonym to an
        # existing heading; the clause and all permissions still come from it.
        topic=[f for f in pool if any(matches(r'อุปกรณ์|\bequipment\b|\bdevices\b',s) for s in f['label'].values())]
        primary=[f for f in topic if index.records.get(f['record_id'],{}).get('kind')=='competition_rule']
        if len(primary)==1:labels=[(1,primary[0])]
    if labels:
        top=max(n for n,_ in labels);chosen=[f for n,f in labels if n==top]
        # Declared dependencies remain in the same event; an absent dependency
        # prevents pretending the selected clause is complete.
        deps=[];queue=list(chosen);visited=set()
        while queue:
            f=queue.pop(0)
            if f['id'] in visited:continue
            visited.add(f['id'])
            for rid in f.get('depends_on_ids',[]):
                linked=[d for d in fs if d['record_id']==rid and d.get('event_id')==f.get('event_id')]
                if not linked:return blocked('C13','rule_dependency_missing')
                deps+=linked;queue+=linked
        return confirmed('C13',list({f['id']:f for f in chosen+deps}.values()),'event_clause_dependency_read',dependency_scope='all_declared_dependencies')
    return pending('C13',pool,'clause_semantics_needed')

def calendar_reader(index,q,at):
    p=policy(index,'C11',q)
    if p:return p
    # Specific weekday after closing: this source is distinct from bookable
    # periods. Never infer opening merely because the booking list is empty.
    if matches(FACETS['weekday_closing'],q):
        fs=[f for f in index.bycat['C11'] if f['facet']=='weekday_closing']
        if fs:return confirmed('C11',fs,'confirmed_weekday_closing')
    if matches(r'ปี\s*(?:202[7-9]|203\d)|\b(?:202[7-9]|203\d)\b',q):return blocked('C11','future_calendar_not_confirmed')
    from .service_calendar import plan as play_service
    service=play_service(index,q,at)
    if service is not None:return service
    # Day/time resolution is backed by the shared calendar adapter in the
    # integrated app. Static fact evaluation deliberately does not invent an
    # open_periods field absent from its frozen projection.
    if matches(r'วันนี้|พรุ่งนี้|ตอนนี้|\btoday\b|\btomorrow\b|right now',q):
        return blocked('C11','calendar_interval_adapter_required')
    result=field_reader(index,'C11',q)
    limits=[]
    for fid in result.ids:
        f=index.byid[fid];record=index.records.get(f['record_id'],{})
        if record.get('kind')!='schedule':continue
        if record.get('fields',{}).get('zone_ids',{}).get('status')!='known':limits.append('zone_scope_unknown')
        if record.get('validity',{}).get('state','unknown')=='unknown':limits.append('effective_period_unknown')
        if f['facet']=='open_periods' and record.get('fields',{}).get('open_periods',{}).get('status')=='conflicted':limits.append('opening_hours_conflicted')
    if limits:
        result.metadata['calendar_source_limits']=sorted(set(limits))
        if any(index.byid[f]['facet']=='bookable_periods' for f in result.ids):
            result.status='partial';result.reason='recorded_periods_applicability_unconfirmed'
    return result

def read(index,cat,q,at):
    at=reference_time(at);q=norm(q)
    safety=guard(index,cat,q,at)
    if safety:return safety
    from .precision import lookup
    exact=lookup(index,cat,q)
    if exact is not None:return exact
    if cat in {'C06','C07','C08','C09','C10','C11'}:
        selected=policy(index,cat,q)
        if selected and not (cat=='C06' and 'mixed_audience' in selected.metadata.get('policy_intents',[]) and matches(FACETS['amount'],q) and matches(r'\d+\s*(?:คน|people|persons?|players?)',q)):return selected
    if cat=='C12':return live_reader(index,q,at)
    if cat=='C13':return rules_reader(index,q,at)
    if cat=='C11':return calendar_reader(index,q,at)
    result=field_reader(index,cat,q,at)
    # Exact typed fields/relations and locked guards take precedence over an
    # older broad query profile. Profiles recover unresolved wording only.
    if result.ids or result.locked:return result
    if cat not in {'C06','C07','C11','C12','C13'}:
        from .legacy_profile import plan as source_profile
        profiled=source_profile(index,cat,q)
        if profiled is not None:return profiled
    return result
