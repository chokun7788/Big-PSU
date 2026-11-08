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
    # Experimental selection: bind the play mode and activity from source action labels.
    if re.search(r'leg[ -]strap|สายรัดขา',q,re.I) and re.search(r'soccer|ฟุตบอล',q,re.I):
        local=bool(re.search(r'local|friends|เฉพาะเครื่อง|เพื่อน',q,re.I));global_=bool(re.search(r'globally|online|ทั่วโลก',q,re.I))
        if local != global_:
            mode=r'local|friends|เฉพาะเครื่อง|เพื่อน' if local else r'globally|online|ทั่วโลก'
            fs=[f for f in pool if re.search(r'leg[ -]strap|สายรัดขา',' '.join(f['label'].values()),re.I) and re.search(r'soccer|ฟุตบอล',' '.join(f['label'].values()),re.I) and re.search(mode,' '.join(f['label'].values()),re.I)]
            if fs:
                result=confirmed('C05',fs,'experimental_source_activity_and_play_mode',operator='action_to_button');result.locked=True;return result
    aliases=[(r'ตีแรง|โจมตีหนัก|heavy attack|strong attack',r'โจมตีหนัก|โจมตีปกติหนัก|heavy attack'),(r'โจมตีเบา|light attack',r'โจมตีเบา|light attack'),(r'กระโดด|jump',r'กระโดด|\bjump\b'),(r'หลบ|dodge|evade',r'หลบ|dodge|evade')]
    for asked,source in aliases:
        if not re.search(asked,q,re.I):continue
        fs=[f for f in pool if re.search(source,' '.join(f['label'].values()),re.I)]
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
    if category=='C01' and meaning:
        from .contact_scope import plan
        scoped=plan(index,q,meaning.facet)
        if scoped is not None:return scoped
    if meaning and category=='C07' and meaning.facet in {'zone','audience'} and meaning.operation!='compare':
        from .financial import rental_pool
        pool=rental_pool(index,q) or index.bind('C07',meaning.target or q)
        selected=[f for f in pool if f['facet']==meaning.facet]
        return confirmed(category,selected,'source_package_relation',operator=meaning.operation) if selected else blocked(category,'package_relation_not_confirmed')
    if meaning and meaning.operation=='list' and category in {'C10','C13'}:
        from .collection_scopes import policies,rules
        pool=policies(index,q) if category=='C10' else rules(index,q)
        if not pool:return blocked(category,'recorded_collection_scope_not_confirmed','missing_input' if category=='C13' else 'missing_source')
        # A local list is the entire recorded source set, never a top-K search
        # result. Source applicability/condition limits remain separate.
        shown=pool
        result=confirmed(category,shown,'recorded_source_collection',operator='list',complete_set=len(shown)==len(pool),member_ids=sorted({f['record_id'] for f in shown}),recorded_source_collection=True,source_collection_size=len(pool),delivered_source_entries=len(shown),physical_world_completeness_claimed=False)
        if len(shown)<len(pool) or category=='C10' and any(f.get('policy_complete') is not True for f in shown):
            result.status='partial';result.metadata['collection_source_limits']=['recorded_sources_only','conditions_or_collection_delivery_not_complete']
        return result
    if meaning and meaning.canonical_operation.startswith('policy.') and category in {'C08','C09','C10'}:
        from .readers import policy
        result=policy(index,category,q,forced_intent=meaning.canonical_operation.split('.',1)[1])
        if result and result.ids and meaning.canonical_operation=='policy.capture' and not re.search(r'ในเกม|in.game|gameplay|screenshots?|capture',q,re.I):
            result.status='partial';result.reason='media_scope_not_established';result.locked=True
            result.metadata['media_scope_unconfirmed']=True
        return result or blocked(category,'canonical_policy_source_not_recorded')
    if category=='C03' and meaning and meaning.target and not index.bind(category,meaning.target) and re.search(r'^do you have',q,re.I):return blocked(category,'named_item_not_recorded')
    if category=='C04' and meaning and meaning.facet=='game_catalog' and len(platforms(index,q))>1:
        selected=[]
        for platform in platforms(index,q):selected.extend(f for f in index.bind('C04',platform) if f['facet']=='game_catalog')
        if selected:
            groups={}
            for f in selected:
                key=str(value(index.records.get(f['record_id'],{}),'platform') or f['subject']['en'])
                groups.setdefault(key,set()).update(f.get('member_ids',[]))
            return confirmed('C04',selected,'coordinated_source_catalogues',operator=meaning.operation,catalog_member_ids=sorted({rid for f in selected for rid in f.get('member_ids',[])}),catalog_group_counts={key:len(members) for key,members in groups.items()},catalog_group_members={key:sorted(members) for key,members in groups.items()},complete_set=False)
    if category=='C04' and meaning and meaning.facet=='players_max':
        from .player_scope import selection
        scoped=selection(index,q);count=scoped['requested_count']
        if scoped.get('error'):
            result=blocked('C04',scoped['error'],'missing_input');result.metadata['context_clarification']={'th':'ต้องการตรวจจำนวนผู้เล่นกี่คนแบบเจาะจงครับ หากมีหลายกลุ่ม กรุณาแยกจำนวนของแต่ละกลุ่ม','en':'Which exact player count should I check? Please separate counts belonging to different groups.'};return result
        if count is not None and (count<=0 or int(count)!=count):return blocked('C04','positive_integer_player_count_required','missing_input')
        if not scoped['facts']:return blocked('C04','requested_player_mode_not_recorded')
        return confirmed('C04',scoped['facts'],'source_player_mode_filter',operator='detail',complete_set=False,player_count=count,player_filter_proofs=scoped['proofs'])
    if category=='C03' and meaning and meaning.operation=='list' and meaning.facet=='name':
        from .collection_scopes import inventory
        fs=inventory(index,q)
        if fs:return confirmed('C03',fs,'source_zone_inventory',operator='list',complete_set=True,member_ids=[f['record_id'] for f in fs])
        return blocked('C03','zone_inventory_not_recorded')
    return None
