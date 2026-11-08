"""Resolve delivered intent slots before every reader; never inherit answer facts."""
import copy,re
from .scope import norm,contains,requested_minutes
from .projection import title,value

VERSION=1
NUMBERS={'หนึ่ง':1,'สอง':2,'สาม':3,'สี่':4,'ห้า':5,'หก':6,'เจ็ด':7,'แปด':8,'เก้า':9,'สิบ':10,'สิบห้า':15,'ยี่สิบ':20,'สามสิบ':30,'ครึ่ง':.5,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'half':.5}
def normalize_numbers(q):
    pattern=r'(?<![a-z])('+ '|'.join(re.escape(s) for s in sorted(NUMBERS,key=len,reverse=True))+r')\s*(?=ชั่วโมง|นาที|คน|วัน|hours?\b|minutes?\b|people\b|persons?\b|days?\b)'
    def number(m):
        if m[1].lower() in {'ครึ่ง','half'} and re.match(r'วัน|days?\b',q[m.end():],re.I):return m[0]
        return str(NUMBERS[m[1].lower()])+' '
    return re.sub(pattern,number,q,flags=re.I)

def labels(r):return [s for s in [*title(r).values(),*sum(r.get('aliases',{}).values(),[])] if isinstance(s,str) and s]

def mentions(index,q,kinds):
    hits=[]
    for rid,r in index.records.items():
        if r.get('kind') not in kinds:continue
        for s in labels(r):
            if not contains(q,s):continue
            for m in re.finditer(re.escape(norm(s)),norm(q)):hits.append((m.start(),m.end(),rid))
    # Longest only for overlapping spans; coordinated independent entities survive.
    return list(dict.fromkeys(rid for a,b,rid in sorted(hits) if not any(c<=a and b<=d and d-c>b-a for c,d,_ in hits)))

def platforms(index,q):
    q=norm(strip_negated_platforms(q)[0]);out=[]
    aliases=[(r'\bpc\b|คอม(?:พิวเตอร์)?','PC'),(r'\bps5\b|เพลย์(?:สเตชัน|ห้า)|playstation','PS5'),(r'nintendo|switch|นินเทนโด','Nintendo Switch'),(r'\bvr\b|วีอาร์','VR'),(r'cockpit|ค็อกพิท|คอกพิท','Cockpit')]
    for pat,label in aliases:
        if re.search(pat,q,re.I):out.append(label)
    def position(label):
        pattern=next(pat for pat,text in aliases if text==label)
        return re.search(pattern,q,re.I).start()
    return sorted(out,key=position)

def strip_negated_platforms(q):
    denied=[]
    pattern=r'(?:ไม่ใช่|ไม่เอา|ไม่เล่น|\bnot)\s*(PC\b|PS5\b|PlayStation\s*5\b|Nintendo\s*Switch\b|Switch\b|VR\b|Cockpit\b)'
    def remove(m):denied.append(m[1]);return ' '
    return re.sub(pattern,remove,q,flags=re.I),denied

def focus(q):
    rules=[('competition_rules',r'แข่ง|กติกา|tournament|rulebook'),('rental',r'เหมา|rental|half.day|full.day'),('price',r'ราคา|กี่บาท|เงินเท่า|เตรียมเงิน|price|cost|how much'),('live',r'ว่าง|available|occupied'),('schedule',r'ศูนย์.*(?:เปิด|ปิด)|เปิดไหม|ปิดไหม|\bopen\b|\bclosed\b'),('controls',r'ปุ่ม|กดตรงไหน|ตีแรง|โจมตีหนัก|buttons?|controls?|heavy attack'),('booking',r'จอง|เข้าไปเล่น.*เริ่ม|book|reserv'),('policy',r'ยกเลิก|cancel|นำ.*มา|นั่งดู|bring|spectator'),('catalog',r'เกม.*(?:อะไรบ้าง|อะไรมั่ง)|(?:what|which|list|all) games'),('game_zone',r'โซนไหน|which.*zone'),('definition',r'คือ(?:เกม)?อะไร|what is|what kind of game')]
    return next((name for name,pattern in rules if re.search(pattern,q,re.I)),None)

def resolve(index,question,history,release_id,at=None):
    from ..followup_scope import delivered_state
    q=normalize_numbers(question);q,denied_platforms=strip_negated_platforms(q);prior=delivered_state(history) or {};old=prior.get('dialogue_task')
    old=copy.deepcopy(old) if isinstance(old,dict) and old.get('version')==VERSION and old.get('release_id')==release_id else {}
    # Only source IDs that still exist may be resumed. All business facts are re-read.
    for key in ('game_ids','entity_ids','audience_ids'):
        if any(rid not in index.records for rid in old.get(key,[])):old={};break
    games=mentions(index,q,{'game'});entities=mentions(index,q,{'equipment_model','person','competition','center','contact','zone','resource'})
    ps=platforms(index,q);f=focus(q)
    from .financial import audience_mentions,person_counts
    audiences,denied=audience_mentions(index,q)
    duration=requested_minutes(q);state={'version':VERSION,'release_id':release_id,'game_ids':games,'entity_ids':entities,'platforms':ps,'audience_ids':sorted(audiences),'duration_minutes':duration,'focus':f,'facts_in_state':False}
    state['person_counts']=person_counts(index,q,audiences);state['excluded_audience_ids']=sorted(denied);state['excluded_platforms']=denied_platforms
    current_person_counts=copy.deepcopy(state['person_counts'])
    from app.booking.live_status import requested_time_window
    from types import SimpleNamespace
    window=requested_time_window(q,SimpleNamespace(now=''))
    if window and window.explicit:state['time_window']={'start':window.start,'end':window.end}
    from .scope import requested_resources
    state['resource_queries']=sorted(requested_resources(q))
    from .date_context import resolve as resolve_date
    from app.calendar.service_calendar import now_bangkok
    date_scope=resolve_date(q,at or now_bangkok(),history)
    if date_scope and date_scope.get('status')=='resolved':state['date']=date_scope['target_date']
    if not audiences and re.search(r'คนนอก|บุคคลภายนอก|outsider|external visitor',q,re.I):state['audience_scope']='external_unspecified'
    used=[];execution=q
    if re.search(r'มีอะไร.*(?:เลือกเล่น|ให้เล่น)|เกม.*(?:อะไร|บ้าง)',q,re.I) and ps:
        execution=q+' '+' '.join(ps)
    follow=bool(re.search(r'^แล้ว|^เปลี่ยนเป็น|^ส่วน|ล่ะ|เกมนี้|อันนี้|อันที่|เครื่องนี้|\b(?:and|what about|how about|this game|it|instead|first|second|third)\b',q,re.I)) or bool(old and not games and re.search(r'โซนไหน|ปุ่ม|กี่คน|which zone|buttons?|how many players',q,re.I))
    if old and len(q)<120 and (ps or audiences or denied or duration is not None or re.search(r'^เปลี่ยน|ครึ่งวัน|เต็มวัน|half.day|full.day',q,re.I)):follow=True
    shift=bool(re.search(r'เปลี่ยนเรื่อง|อีกเรื่อง|new topic|different topic',q,re.I)) or f in {'schedule','live','catalog','rental','competition_rules'} and f!=old.get('focus')
    if old.get('context_entity_ids') and not games and not entities and not ps and len(q)<120:
        from ..query_contract import resolve_fields
        fields=resolve_fields(q)[0]
        if fields and f not in {'schedule','live','catalog','price','rental','competition_rules'}:follow=True
    if old and follow and not shift:
        ordinal=re.search(r'อันที่\s*(หนึ่ง|สอง|สาม|1|2|3)|\b(first|second|third)\b',q,re.I)
        if ordinal:
            token=next(s for s in ordinal.groups() if s);number={'หนึ่ง':1,'สอง':2,'สาม':3,'first':1,'second':2,'third':3}.get(token,int(token) if token.isdigit() else 0)
            options=old.get('ordered_options',[])
            if 0<number<=len(options) and options[number-1].get('record_id') in index.records:
                chosen=options[number-1];execution=(chosen.get('platform') or title(index.records[chosen['record_id']])['en'])+' '+q
                state['platforms']=platforms(index,execution);used.append('delivered_ordered_option')
            else:state['ordinal_unresolved']=True
        if not games and old.get('game_ids') and f not in {'schedule','live','rental'} and (not entities and not ps or re.search(r'เกมนี้|this game',q,re.I)):
            state['game_ids']=old['game_ids'];used.append('game_ids')
            execution=' '.join(title(index.records[rid])['en'] or title(index.records[rid])['th'] for rid in state['game_ids'])+' '+execution
        if old.get('focus')=='live' and f in {None,'live'}:
            state['focus']='live'
            if not state.get('date') and old.get('date'):state['date']=old['date'];used.append('date')
            execution=q+' ว่างไหม'+(' '+state['date'] if state.get('date') else '')
            if not ps and not state['resource_queries']:
                state['resource_queries']=old.get('resource_queries',[]);execution+=' '+' '.join(state['resource_queries'] or old.get('platforms',[]));used.append('resource_queries')
            if not state.get('time_window') and old.get('time_window') and not re.search(r'ตอนนี้|\bnow\b',q,re.I):
                state['time_window']=old['time_window'];used.append('time_window')
                execution+=' '+state['time_window']['start']+('-'+state['time_window']['end'] if state['time_window'].get('end') else '')
        active=old.get('context_entity_ids',[])
        if not games and not entities and not ps and len(active)==1 and active[0] in index.records and f not in {'schedule','live','price','rental','competition_rules'}:
            execution=title(index.records[active[0]])['en']+' '+execution;state['entity_ids']=active;used.append('entity_ids')
        if old.get('focus') in {'price','rental'} and f in {None,'price','rental'} and not games and (not entities or ps):
            state['focus']=old['focus']
            for key,current in [('platforms',ps),('audience_ids',audiences),('duration_minutes',duration)]:
                if not current and old.get(key) is not None:state[key]=old[key];used.append(key)
            state['audience_ids']=[rid for rid in state['audience_ids'] if rid not in denied]
            excluded=set(platforms(index,' '.join(denied_platforms)))
            state['platforms']=[p for p in state['platforms'] if p not in excluded]
            state['person_counts']={rid:state['person_counts'].get(rid,old.get('person_counts',{}).get(rid)) for rid in state['audience_ids'] if rid in state['person_counts'] or rid in old.get('person_counts',{})}
            if state['person_counts']:used.append('person_counts')
            if not state['audience_ids'] and old.get('audience_scope'):state['audience_scope']=old['audience_scope']
            execution='ราคา '+' '.join(state['platforms'])+' '+' '.join((title(index.records[rid])['th'] or title(index.records[rid])['en'])+(' '+str(state['person_counts'][rid])+' คน' if rid in state['person_counts'] else '') for rid in state['audience_ids'])
            execution+=' '+' '.join('ไม่ใช่ '+(title(index.records[rid])['th'] or title(index.records[rid])['en']) for rid in denied)
            if state['focus']=='rental':
                period=re.search(r'ครึ่งวัน|เต็มวัน|half.day|full.day',q,re.I)
                state['rental_period']=period[0] if period else old.get('rental_period','')
                execution+=' เหมา '+state['rental_period']
            if state.get('audience_scope')=='external_unspecified':execution+=' บุคคลภายนอก'
            if state['duration_minutes'] is not None:execution+=' '+str(state['duration_minutes'])+' นาที'
        elif old.get('focus')=='booking' and f=='policy' and re.search(r'ยกเลิก|cancel',q,re.I):
            execution=q+' ยกเลิกการจอง';state['focus']='booking';used.append('booking_operation')
        elif f is None and re.search(r'อันที่\s*(?:หนึ่ง|สอง|สาม|1|2|3)|(?:first|second|third)',q,re.I):
            # Order can differ between the user's conjunction and displayed options.
            # Do not guess an ordinal unless it uniquely names a delivered option.
            state['ordinal_unresolved']=True
    if not state['focus'] and old and follow:state['focus']=old.get('focus')
    if state['focus']=='rental' and not state.get('rental_period'):
        period=re.search(r'ครึ่งวัน|เต็มวัน|half.day|full.day',q,re.I)
        if period:state['rental_period']=period[0]
    # Preserve a valid game across an intervening date question for an explicit game pronoun.
    explicit_game_source=None
    if not games and re.search(r'เกมนี้|this game',q,re.I) and not state['game_ids']:
        for turn in reversed((history or [])[-12:]):
            if turn.get('role')!='user':continue
            found=mentions(index,str(turn.get('text') or turn.get('content') or ''),{'game'})
            if len(found)==1:
                state['game_ids']=found;execution=title(index.records[found[0]])['en']+' '+execution;used.append('explicit_game_pronoun');explicit_game_source={'origin':'trusted_user_history','quote':str(turn.get('text') or turn.get('content') or ''),'source_turn_id':turn.get('request_id') or turn.get('turn_id'),'scope_only':True,'business_fact':False};break
    from ..flow_context import CURRENT
    from .request_provenance import digest
    request_ctx=CURRENT.get();turn_id=request_ctx.request_id if request_ctx else None
    provenance={};superseded=[]
    for slot in ['game_ids','entity_ids','platforms','audience_ids','person_counts','duration_minutes','date','time_window','resource_queries','rental_period']:
        current=state.get(slot)
        if current is None or current==[] or current=={}:continue
        inherited=slot in used and old.get(slot)==current
        if slot=='game_ids' and explicit_game_source:
            source=copy.deepcopy(explicit_game_source)
        elif inherited:
            source=copy.deepcopy(old.get('slot_provenance',{}).get(slot) or {'origin':'trusted_history','state_sha256':digest(prior),'source_turn_id':prior.get('request_id'),'quote':None,'scope_only':True})
            source['origin']='trusted_history'
        else:
            source={'origin':'current_user','quote':question,'source_span':{'start':0,'end':len(question),'text':question},'source_turn_id':turn_id,'transform':'deterministic_scope_or_unit_resolution','business_fact':False}
        source['normalized_slot']=current
        source['execution_text']=' '.join(str(x) for x in current) if isinstance(current,list) else str(current)
        provenance[slot]=source
        if slot=='person_counts':
            source['member_provenance']={rid:({'origin':'trusted_history','state_sha256':digest(prior),'previous_provenance':old.get('slot_provenance',{}).get('person_counts')} if rid not in current_person_counts and old.get('person_counts',{}).get(rid)==count else {'origin':'current_user','quote':question,'source_turn_id':turn_id}) for rid,count in current.items()}
        if old.get(slot) is not None and old.get(slot)!=current:superseded.append({'slot':slot,'previous_value':old.get(slot),'replacement_value':current,'replacement_source':source})
    state['slot_provenance']=provenance;state['superseded_slots']=superseded
    return {'original_question':question,'execution_question':execution,'used_context':bool(used),'inherited_slots':used,'task':state,'normalization_applied':q!=question}

def attach(result,context,records):
    from dataclasses import replace
    art=dict(result.decision_artifact or {});state=context['task']
    claims=art.get('domain_flow',{}).get('typed_claims',[])
    options={}
    for c in claims:
        if c.get('facet')!='game_catalog':continue
        rid=c['record_id'];platform=str(value(records.get(rid,{}),'platform') or title(records.get(rid,{})).get('en') or rid)
        options.setdefault(platform,{'record_id':rid,'platform':platform})
    state['ordered_options']=list(options.values())
    selected=art.get('query_plan',{}).get('record_ids',[])
    state['context_entity_ids']=[rid for rid in selected if records.get(rid,{}).get('kind') in {'person','equipment_model','resource','center','contact','rental_package','competition','news','facility','procedure'}]
    if 'C12' in art.get('domain_flow',{}).get('categories',[]):state['focus']='live'
    art['dialogue_task']=state;art['dialogue_resolution']={k:v for k,v in context.items() if k!='task'}
    return replace(result,decision_artifact=art)
