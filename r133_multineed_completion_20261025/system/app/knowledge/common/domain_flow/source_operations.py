"""Operations over source values; no venue answers, rates or record IDs."""
import re
from .scope import norm,contains

STEPS=[r'เลือกบริการ|select.*service',r'เลือกวัน|choose.*date',r'กรอก.*ข้อมูล|fill.*(?:information|details)',r'ตรวจสอบ.*ข้อมูล|review.*details',r'ชำระเงิน|pay|transfer',r'แนบ.*สลิป|upload.*slip']
def equivalent_procedure(facts):
    if not facts:return None
    signatures=[]
    for f in facts:
        q=norm(f['value'].get('th') or f['value'].get('en'))
        if re.search(r'ถ้า|ยกเว้น|เว้นแต่|เท่านั้น|ไม่|unless|except|only|\d',q):return None
        spans=[re.search(p,q,re.I) for p in STEPS]
        if not all(spans) or [m.start() for m in spans]!=sorted(m.start() for m in spans):return None
        signatures.append(tuple(range(len(STEPS))))
    return sorted(facts,key=lambda f:f['id'])[0] if len(set(signatures))==1 else None

def source_clause_terms(index,q,pool):
    """Read an entire uniquely matching source clause; never synthesize permissions."""
    primary=[f for f in pool if index.records.get(f['record_id'],{}).get('kind')=='competition_rule']
    words=set(re.findall(r'[a-z]{4,}',q.lower()))-{'what','which','where','under','rules','rulebook','change','please','verified','information','tournament','competition','allowed','permitted','studio','phuket','with','does','this','that','from','have','settings','about','could','would'}
    texts={f['id']:' '.join(f['value'].values()).lower() for f in primary}
    wanted={w for w in words if 0<sum(bool(re.search(r'\b'+re.escape(w)+r'\b',s)) for s in texts.values())<=max(3,len(primary)//4)}
    if len(wanted)<2:return []
    matches=[f for f in primary if all(re.search(r'\b'+re.escape(w)+r'\b',texts[f['id']]) for w in wanted)]
    return matches if len(matches)==1 else []

def procedure_rows(text):
    # Retain exact source substrings, splitting only at declared sequential actions.
    starts=[m.start() for m in re.finditer(r'เลือกบริการ|เลือกวัน|กรอกข้อมูล|ตรวจสอบข้อมูล|ชำระเงิน|แนบสลิป|select (?:a |the (?:desired )?)service|choose (?:the |a )?date|enter (?:customer |user )?information|fill in|verify (?:the )?details|review(?: the)? details|pay(?: by| through)?|upload(?: the)?(?: payment)? slip|attach(?: the)?(?: transfer| payment)? slip',text,re.I)]
    if len(starts)<3:return []
    return [re.sub(r'\s+(?:และ|and)$','',text[a:b].strip(' ,;，'),flags=re.I) for a,b in zip(starts,starts[1:]+[len(text)])]

def control_action(index,q,pool):
    from .readers import confirmed,blocked
    if re.search(r'ทั้งหมด|อะไรบ้าง|\ball\b|\blist\b',q,re.I):return None
    aliases=[(r'ตีแรง|โจมตีหนัก|heavy attack|strong attack',r'โจมตีหนัก|โจมตีปกติหนัก|heavy attack'),(r'โจมตีเบา|light attack',r'โจมตีเบา|light attack'),(r'กระโดด|jump',r'กระโดด|\bjump\b'),(r'หลบ|dodge|evade',r'หลบ|dodge|evade')]
    for asked,source in aliases:
        if not re.search(asked,q,re.I):continue
        fs=[f for f in pool if re.search(source,' '.join([*f['label'].values(),*f['value'].values()]),re.I)]
        if not fs:return blocked('C05','requested_action_not_recorded')
        if len({f['record_id'] for f in fs})>1:return blocked('C05','control_platform_required','missing_input')
        result=confirmed('C05',fs,'source_action_family',operator='action_to_button',action_pattern=source);result.locked=True;return result
    # Future owner action aliases are read from labels/declared aliases as data.
    fs=[f for f in pool if any(len(norm(s))>2 and contains(q,s) for s in [*f['label'].values(),*f.get('action_aliases',[])])]
    if fs:
        result=confirmed('C05',fs,'source_declared_action',operator='action_to_button');result.locked=True;return result
    return None

def native_operation(index,category,q,meaning=None):
    from .readers import confirmed,blocked
    from .projection import value,title
    from .dialogue_task import platforms
    if meaning and meaning.canonical_operation.startswith('policy.') and category in {'C08','C09','C10'}:
        from .readers import policy
        result=policy(index,category,q,forced_intent=meaning.canonical_operation.split('.',1)[1])
        if result and any(index.byid[fid].get('policy_complete') is False for fid in result.ids):return blocked(category,'policy_conditions_or_exceptions_not_confirmed')
        if result and result.ids and meaning.canonical_operation=='policy.capture' and not re.search(r'ในเกม|in.game|gameplay|screenshots?|capture',q,re.I):
            result.status='partial';result.reason='media_scope_not_established';result.locked=True
            result.metadata['media_scope_unconfirmed']=True
        return result or blocked(category,'canonical_policy_source_not_recorded')
    if category=='C03' and meaning and meaning.target and not index.bind(category,meaning.target) and re.search(r'^do you have',q,re.I):return blocked(category,'named_item_not_recorded')
    if category=='C04' and meaning and meaning.facet=='game_catalog' and len(platforms(index,q))>1:
        selected=[]
        for platform in platforms(index,q):selected.extend(f for f in index.bind('C04',platform) if f['facet']=='game_catalog')
        if selected:return confirmed('C04',selected,'coordinated_source_catalogues',operator=meaning.operation,catalog_member_ids=sorted({rid for f in selected for rid in f.get('member_ids',[])}),complete_set=False)
    if category=='C04' and meaning and meaning.facet=='players_max':
        m=re.search(r'(\d+)\s*(?:คน|people|players)',q,re.I)
        from .dialogue_task import mentions
        game_ids=set(mentions(index,q,{'game'}));ps=set(platforms(index,q))
        fs=[f for f in index.bycat['C04'] if f['facet']=='players_max' and (not game_ids or f.get('game_id') in game_ids)]
        if ps:fs=[f for f in fs if ps&set(platforms(index,str(f.get('platform',''))))]
        if not fs:return blocked('C04','player_mode_source_not_recorded')
        count=int(m[1]) if m else None
        if count is not None and count<=0:return blocked('C04','positive_player_count_required','missing_input')
        matching=[f for f in fs if value(index.records.get(f['record_id'],{}),'studio_supported') is True and (count is None or f.get('numeric') is not None and f['numeric']>=count and (value(index.records.get(f['record_id'],{}),'players_min') or 1)<=count)]
        mode=re.search(r'local|online|ออฟไลน์|ออนไลน์',q,re.I)
        if mode:matching=[f for f in matching if re.search(mode[0],str(f.get('mode_name','')),re.I)]
        if not matching:return blocked('C04','requested_player_mode_not_recorded')
        return confirmed('C04',matching,'source_player_mode_filter',operator='detail',complete_set=False,player_count=count)
    if category=='C03' and meaning and meaning.operation=='list' and meaning.facet=='name':
        fs=[f for f in index.bycat['C03'] if f['facet']=='name'];ps=platforms(index,q)
        zones={rid for rid,r in index.records.items() if r['kind']=='zone' and any(p.lower() in ' '.join(title(r).values()).lower() for p in ps)}
        if zones:
            names={' '.join(title(index.records[z]).values()).lower() for z in zones}
            def located(f):
                specs=value(index.records[f['record_id']],'specifications') or []
                location=' '.join(str(x.get('value','')) for x in specs if isinstance(x,dict) and x.get('key')=='zone').lower()
                return any(any(t.lower() in location for t in title(index.records[z]).values()) for z in zones)
            fs=[f for f in fs if located(f)]
        if fs:return confirmed('C03',fs,'source_zone_inventory',operator='list',complete_set=True,member_ids=[f['record_id'] for f in fs])
        return blocked('C03','zone_inventory_not_recorded')
    return None
