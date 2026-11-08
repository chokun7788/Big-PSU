"""Domain readers: scope first, then typed fields, relations or decisions."""
import re
from datetime import timedelta
from .contracts import Plan
from .scope import norm,contains,years,requested_years,matching_subjects,resource_scope,reference_time,validity_allows
from .vocabulary import FACETS,POLICY_INTENTS,UNRECORDED_FIELDS,matches
from .projection import value,title

ALLOWED={
 'C01':{'operator','description','address','building','floor','map_url','value','office_hours','location','usage_conditions'},
 'C02':{'display_name','role','team'},
 'C03':{'name','device_type','specifications','usage','location','quantity','capacity_persons','controllers','room_seats'},
 'C04':{'summary','genre','how_to_play','supported_platforms','studio_services','game_catalog','players_max'},
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
    quoted=re.findall(r'(?:ราคา|เกม|เครื่อง|บริการ|package|game|service)\s*[“"「]([^”"」]+)[”"」]',q,re.I)
    for mention in quoted:
        if not any(contains(s,mention) for f in index.facts for s in [*f['subject'].values(),*f.get('entity_aliases',[]),*f['label'].values()]):
            return blocked(cat,'explicit_named_target_not_in_source')
    if cat in {'C06','C07'} and asked:
        # Explicit owner re-confirmation applies to the observed current year;
        # it never licenses projecting rates into unconfirmed future years.
        if asked!={at.year}:
            compatible=[f for f in fs if any(validity_allows(f,at.replace(year=y)) is True for y in asked)]
            if not compatible:return blocked(cat,'no_confirmed_rate_for_requested_year','not_current')
    if cat=='C13':asked=years(q)
    if cat=='C13' and asked:
        source_years=set().union(*(years(' '.join(f['subject'].values())) for f in fs)) if fs else set()
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
    for intent,domain,source_pattern,question_pattern in POLICY_INTENTS:
        if domain==cat and matches(question_pattern,q):
            candidates=[f for f in fs if matches(source_pattern,' '.join(f['subject'].values())) or f.get('policy_intent')==intent or f.get('policy_intent','').endswith('.'+intent)]
            if candidates:intents.append((intent,candidates))
    if not intents:return None
    names={x[0] for x in intents}
    # Specific scenarios dominate general actions without discarding unrelated
    # requested needs, which the outer splitter processes independently.
    if 'rain_reschedule' in names:intents=[x for x in intents if x[0] not in {'late_notice','change_paid_booking'}]
    if 'correct_booking_name' in names:intents=[x for x in intents if x[0]!='change_paid_booking']
    if 'game_failure_switch' in names:intents=[x for x in intents if x[0]!='change_service']
    candidates=list({f['id']:f for _,group in intents for f in group}.values())
    preferred=[f for f in candidates if f.get('owner_confirmed')]
    if preferred and len(intents)==1:candidates=preferred
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
    top=max((n,length) for n,length,_ in scored)
    return [f for n,length,f in scored if (n,length)==top]

def field_reader(index,cat,q):
    allfs=index.bycat[cat];pool=tuple_pool(index,cat,q) if cat in {'C06','C07'} else index.bind(cat,q)
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
    if pool:
        for s in sorted({v for f in pool for v in f['subject'].values()},key=len,reverse=True):
            if contains(fieldq,s):fieldq=fieldq.replace(norm(s),' ')
    facets=set()
    for facet in ALLOWED[cat]:
        aliases=[f['label'][l] for f in pool for l in ['th','en'] if f['facet']==facet]
        if any(contains(fieldq,s) for s in aliases if len(norm(s))>=2) or (facet in FACETS and matches(FACETS[facet],fieldq)):facets.add(facet)
    if cat=='C01':
        if 'description' in facets and not any(f['facet']=='description' for f in allfs) and matches(r'ศูนย์|studio|university',q):facets.add('operator')
        # "where is the studio" is address, not every facility location.
        if 'address' in facets:facets.discard('location')
    if cat=='C03':
        if 'room_seats' in facets:facets.discard('capacity_persons')
        if 'specifications' in facets:facets.discard('device_type')
    if cat=='C04':
        if 'how_to_play' in facets:facets.discard('summary')
        if 'genre' in facets:facets.discard('summary')
        if 'game_catalog' in facets:facets.discard('summary');facets.discard('studio_services')
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
    if chosen:return confirmed(cat,chosen,'typed_requested_fields')
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
    fs=index.bycat['C13'];pool=index.bind('C13',q);asked=years(q)
    if asked:pool=[f for f in pool or fs if asked<=years(' '.join(f['subject'].values()))]
    if not pool:return pending('C13',fs,'event_or_rule_not_bound')
    fieldq=q
    for s in sorted({s for f in pool for s in f['subject'].values()},key=len,reverse=True):fieldq=fieldq.replace(norm(s),' ')
    labels=[]
    for f in pool:
        hits=[len(norm(s)) for s in f['label'].values() if len(norm(s))>2 and contains(fieldq,s)]
        if hits:labels.append((max(hits),f))
    if labels:
        top=max(n for n,_ in labels);chosen=[f for n,f in labels if n==top]
        # Declared dependencies remain in the same event; an absent dependency
        # prevents pretending the selected clause is complete.
        deps=[]
        for f in chosen:
            for rid in f.get('depends_on_ids',[]):
                linked=[d for d in fs if d['record_id']==rid and d.get('event_id')==f.get('event_id')]
                if not linked:return blocked('C13','rule_dependency_missing')
                deps+=linked
        return confirmed('C13',list({f['id']:f for f in chosen+deps}.values()),'event_clause_dependency_read')
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
    # Day/time resolution is backed by the shared calendar adapter in the
    # integrated app. Static fact evaluation deliberately does not invent an
    # open_periods field absent from its frozen projection.
    if matches(r'วันนี้|พรุ่งนี้|ตอนนี้|\btoday\b|\btomorrow\b|right now',q):
        return blocked('C11','calendar_interval_adapter_required')
    return field_reader(index,'C11',q)

def read(index,cat,q,at):
    at=reference_time(at);q=norm(q)
    safety=guard(index,cat,q,at)
    if safety:return safety
    if cat in {'C06','C07','C08','C09','C10','C11'}:
        selected=policy(index,cat,q)
        if selected:return selected
    if cat=='C12':return live_reader(index,q,at)
    if cat=='C13':return rules_reader(index,q,at)
    if cat=='C11':return calendar_reader(index,q,at)
    return field_reader(index,cat,q)
