"""Topic clarification for unverified semantic proposals, never policy approval.

State stores source IDs and routing fingerprints, never answer text. Every
compatible profile remains reachable by pagination, independently of top-k.
"""
import hashlib,json,re
from .query_contract import normalize
from .question_profiles import tasks,KINDS,phrase_match
from .registry import value
PAGE_SIZE=6

def fingerprint(record):
    raw={'kind':record['kind'],'profile':value(record,'query_profile')}
    return hashlib.sha256(json.dumps(raw,sort_keys=True,ensure_ascii=False).encode()).hexdigest()

def eligible(question,records):
    q=normalize(question);wanted=tasks(question)
    if len(wanted)!=1:return []
    competition=bool(re.search(r'แข่ง|กติกา|\b(?:competition|tournament|rulebook)\b',q))
    found=[]
    for rid,r in records.items():
        p=value(r,'query_profile')
        if r['kind'] not in KINDS or not isinstance(p,dict) or p.get('task') not in wanted:continue
        if (p.get('context')=='competition')!=competition:continue
        from .correction_scope import compatible
        if not compatible(question,p):continue
        if p.get('ownership')=='personal' and (not re.search(r'ส่วนตัว|ตัวเอง|ของผม|ของฉัน|\b(?:own|personal|my|mine)\b',q) or re.search(r'ของศูนย์|\b(?:studio|center|venue)[’\x27]?s\b',q)):continue
        found.append(rid)
    # Stable independent of SQLite insertion order. This is a topic menu,
    # not a ranking or assertion that each option answers the request.
    return sorted(found)

def build(question,records,preferred=None):
    ids=eligible(question,records)
    if not ids:return None
    preferred=[rid for rid in (preferred or []) if rid in ids]
    ids=list(dict.fromkeys(preferred+ids))
    return {'version':1,'options':[{'record_id':rid,'routing_sha256':fingerprint(records[rid])} for rid in ids],
        'page':0,'page_size':PAGE_SIZE,'reason':'unverified_meaning_requires_topic_selection'}

def prompt(pending,records,lang):
    from .answer import title
    opts=pending['options'];start=pending['page']*PAGE_SIZE;page=opts[start:start+PAGE_SIZE]
    if len(opts)==1:
        label=title(records[opts[0]['record_id']],lang)
        return ('คุณหมายถึงหัวข้อนี้ใช่ไหมครับ: '+label+'?\nตอบ “ใช่” หรือ “ไม่ใช่” ได้ครับ' if lang=='th' else 'Do you mean this topic: '+label+'?\nReply “yes” or “no”.')
    lines=[str(i+1)+'. '+title(records[o['record_id']],lang) for i,o in enumerate(opts) if start<=i<start+PAGE_SIZE]
    body=('ต้องการถามหัวข้อไหนครับ? กรุณาตอบเลขข้อหรือชื่อหัวข้อ\n' if lang=='th' else 'Which topic do you mean? Reply with its number or title.\n')+'\n'.join(lines)
    body+=('\nพิมพ์ “ถัดไป” เพื่อดูหัวข้ออื่น หรือ “ไม่ใช่” เพื่อระบุเรื่องใหม่' if lang=='th' else '\nType “next” for more topics, or “no” to specify a different topic.') if len(opts)>PAGE_SIZE else ('\nถ้าไม่มีหัวข้อที่ต้องการ พิมพ์ “ไม่ใช่” ได้ครับ' if lang=='th' else '\nReply “no” if none of these topics match.')
    return body

def latest(history):
    for turn in reversed((history or [])[-8:]):
        if not isinstance(turn,dict) or turn.get('role')!='assistant':continue
        if turn.get('delivery_status') not in {'server_written','client_acknowledged'}:return None
        s=turn.get('common_read_state')
        p=s.get('profile_confirmation') if isinstance(s,dict) and s.get('schema_version')==1 else None
        if not isinstance(p,dict) or p.get('version')!=1:return None
        opts=p.get('options');page=p.get('page')
        if not isinstance(opts,list) or not opts or len(opts)>2000 or type(page) is not int or not 0<=page<(len(opts)+PAGE_SIZE-1)//PAGE_SIZE:return None
        if any(not isinstance(o,dict) or set(o)!={'record_id','routing_sha256'} or not isinstance(o['record_id'],str) or not isinstance(o['routing_sha256'],str) for o in opts):return None
        if len({o['record_id'] for o in opts})!=len(opts):return None
        return p
    return None

def resolve(question,history,records):
    p=latest(history)
    if not p:return None
    q=normalize(question).strip(' ?!.,');opts=p['options']
    from .reply_repair import rejection
    rejected=rejection(question)
    if rejected:
        visible=opts[p['page']*PAGE_SIZE:(p['page']+1)*PAGE_SIZE]
        return {'action':'rephrase' if rejected['replacement'] else 'cancel','replacement':rejected['replacement'],
            'declined_profile_ids':[o['record_id'] for o in visible],'basis':rejected['reason']}
    from .qualified_reply import resolve_qualification
    qualified=resolve_qualification(question,p,records)
    if qualified:return qualified
    yes=bool(re.fullmatch(r'yes|yes please|yep|ใช่|ใช่ครับ|ใช่ค่ะ|ใช่เลย|ถูกต้อง',q))
    next_page=q in {'next','more','ถัดไป','หน้าถัดไป','ดูเพิ่ม'}
    index=int(q)-1 if re.fullmatch(r'[0-9]{1,4}',q) else None
    chosen=opts[0] if yes and len(opts)==1 else None
    if next_page:
        # Deleted/changed routing entries must not become selectable via a
        # stale menu. Caller asks a fresh question rather than silently remaps.
        if any(o['record_id'] not in records or fingerprint(records[o['record_id']])!=o['routing_sha256'] for o in opts):return {'action':'expired'}
        return {'action':'prompt','pending':{**p,'page':(p['page']+1)%((len(opts)+PAGE_SIZE-1)//PAGE_SIZE)}}
    if index is not None:
        if not p['page']*PAGE_SIZE<=index<min(len(opts),(p['page']+1)*PAGE_SIZE):return {'action':'prompt','pending':p}
        chosen=opts[index]
    if not chosen and not yes:
        from .answer import title
        visible=opts[p['page']*PAGE_SIZE:(p['page']+1)*PAGE_SIZE]
        exact=[o for o in visible if o['record_id'] in records and any(normalize(title(records[o['record_id']],lang)).strip(' ?!.,')==q for lang in ('th','en'))]
        # Bare source-declared subject names are allowed; complete new
        # questions do not inherit the old task just because they contain it.
        subjects=[o for o in visible if o['record_id'] in records and any(normalize(t)==q for s in (value(records[o['record_id']],'query_profile') or {}).get('subjects',[]) for t in s.values() if isinstance(t,str) and t)]
        matches={o['record_id']:o for o in exact+subjects}
        if len(matches)==1:chosen=next(iter(matches.values()))
    if yes and len(opts)>1:return {'action':'prompt','pending':p}
    if not chosen:return None
    rid=chosen['record_id']
    if rid not in records or fingerprint(records[rid])!=chosen['routing_sha256']:return {'action':'expired'}
    return {'action':'selected','record_id':rid,'routing_sha256':chosen['routing_sha256'],'basis':'explicit_user_topic_selection'}
