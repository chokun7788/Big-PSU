"""Bounded qualification of declared topic scope. No policy facts or IDs here.

Only subject/ownership/context language is interpreted. Uncovered text blocks
projection; financial/age unknowns keep their existing unconfirmed handling.
"""
import re
from .query_contract import normalize
from .registry import value
from .question_profiles import tasks,KINDS

HEADER=re.compile(r'^\s*(?:yes(?:\s+please)?|yep|yeah|ใช่(?:ครับ|ค่ะ|เลย)?|ถูกต้อง(?:ครับ|ค่ะ)?)\s*[,;:!—–\-]?\s*(?P<link>but\b|however\b|except\b|only\s+if\b|แต่|ถ้า)\s*[,;:—–\-]?\s*',re.I)
OWNERS={
 'studio':r'ของ(?:ศูนย์|ร้าน|สตูดิโอ)|\b(?:studio|cent(?:er|re)|venue)[’\x27]s\b|\b(?:studio|cent(?:er|re)|venue)[ -]owned\b|\bbelongs? to (?:the )?(?:studio|cent(?:er|re)|venue)\b',
 'personal':r'ของ(?:ผม|ฉัน|เรา|ตัวเอง)|ส่วนตัว|\b(?:mine|my own|personal)\b|\bbelongs? to me\b',
}
CONTEXTS={'competition':r'การแข่งขัน|ตอนแข่ง|แข่ง|กติกา|\b(?:competition|tournament|rulebook)\b',
 'studio':r'ใช้บริการทั่วไป|เล่นทั่วไป|ไม่ได้แข่งเล่นทั่วไป|\b(?:normal use|regular use|casual play|general studio use)\b'}
NEGATION=re.compile(r'(?:\b(?:not(?:\s+(?:a|an|the|for|in|at)){0,3}|isn[’\x27]t|aren[’\x27]t)\s*|ไม่ใช่(?:ของ)?|ไม่(?:ได้)?(?:ใช้ใน|ใช้|เอาไป|สำหรับ|ตอน)?|ไม่ได้)\s*$')

def qualification(question):
    if not isinstance(question,str):return None
    m=HEADER.match(question)
    if not m:return None
    return {'qualifier':question[m.end():].strip(),'connector':m['link'],'raw_prefix':question[:m.end()]}

def labels(subject):return {normalize(s) for s in subject.values() if isinstance(s,str) and s}
def expression(term):
    return (r'(?<![a-z0-9])'+re.escape(term)+r's?(?![a-z0-9])') if re.search('[a-z0-9]',term) else re.escape(term)

def scope_plan(tail,source,records):
    p=value(source,'query_profile');q=normalize(tail);spans=[]
    positives={'ownership':set(),'context':set()};negatives={'ownership':set(),'context':set()}
    def slot(group,name,start,end):
        prefix=q[:start];neg=NEGATION.search(prefix)
        negatives[group].add(name) if neg else positives[group].add(name)
        spans.append((neg.start() if neg else start,end))
    for group,patterns in [('ownership',OWNERS),('context',CONTEXTS)]:
        for name,pattern in patterns.items():
            for m in re.finditer(pattern,q):slot(group,name,*m.span())
    declared=[]
    for r in records.values():
        v=value(r,'query_profile')
        if r['kind'] in KINDS and isinstance(v,dict) and v.get('task')==p['task']:
            for s in v['subjects']:
                if s not in declared:declared.append(s)
    matched=[]
    for s in declared:
        for term in labels(s):
            for m in re.finditer(expression(term),q):
                matched.append(s);spans.append(m.span())
                if re.search(r'\bmy\s+(?:own\s+|personal\s+)*$',q[:m.start()]):
                    my=re.search(r'\bmy\s+(?:own\s+|personal\s+)*$',q[:m.start()])
                    slot('ownership','personal',my.start(),m.end())
    mask=list(q)
    for start,end in spans:mask[start:end]=' '*(end-start)
    remainder=''.join(mask)
    # Grammar only. Unattached negation, numbers and modifiers stay unresolved.
    remainder=re.sub(r"\b(?:it[’']s|it's|it|its|is|are|this|that|the|a|an|one|ones|i|am|can|could|may|use|using|bring|bringing|for|at|in|from|to|belongs|belong|owned|by|with|if|then|please|actually|rather|instead|and|but|however)\b",' ',remainder)
    remainder=re.sub(r'เป็น|ใช้|เอา|นำ|มา|ไป|เล่น|อันนี้|อันนั้น|ของ|ครับ|ค่ะ|คะ|นะ|ล่ะ|ถ้า|ผม|ฉัน|แต่|และ|กับ',' ',remainder)
    remainder=re.sub(r'[\s,.!?;:—–\-]+',' ',remainder).strip()
    audit={'positive_slots':{k:sorted(v) for k,v in positives.items()},'negative_slots':{k:sorted(v) for k,v in negatives.items()},
        'uncovered_text':remainder,'source_task':p['task'],'meaning_verified_by_model':False}
    if any(len(v)>1 or v&negatives[k] for k,v in positives.items()):return None,{**audit,'reason':'conflicting_slots'}
    if remainder or not tail.strip():return None,{**audit,'reason':'uncovered_qualification'}
    owner=next(iter(positives['ownership']),p['ownership']);context=next(iter(positives['context']),p['context'])
    if owner in negatives['ownership'] or context in negatives['context']:return None,{**audit,'reason':'negated_scope_without_replacement'}
    subjects=list({tuple(sorted(s.items())):s for s in matched}.values()) or p['subjects']
    ids=[]
    for rid,r in records.items():
        v=value(r,'query_profile')
        if r['kind'] not in KINDS or not isinstance(v,dict) or v['task']!=p['task'] or v['context']!=context:continue
        if v['ownership']!='any' and v['ownership']!=owner:continue
        if all(any(labels(s)&labels(t) for t in v['subjects']) for s in subjects):ids.append(rid)
    return ids,{**audit,'reason':'declared_scope_match' if ids else 'no_profile_for_qualified_scope',
        'qualified_scope':{'ownership':owner,'context':context,'subjects':subjects},'candidate_ids':ids}

def resolve_qualification(question,pending,records):
    parsed=qualification(question)
    if parsed is None:return None
    opts=pending['options'];visible=opts[pending['page']*6:(pending['page']+1)*6]
    base={'qualification':parsed,'blocked_unqualified_ids':[o['record_id'] for o in visible]}
    if len(opts)!=1:return {**base,'action':'qualification_unconfirmed','audit':{'reason':'topic_not_uniquely_selected'}}
    o=opts[0];rid=o['record_id']
    from .profile_confirmation import fingerprint
    if rid not in records or fingerprint(records[rid])!=o['routing_sha256']:return {'action':'expired'}
    tail=parsed['qualifier'];p=value(records[rid],'query_profile')
    from .unconfirmed_request import topic
    unknown=topic(tail)
    if unknown:return {**base,'action':'qualification_unconfirmed','audit':{'reason':'specific_unconfirmed_need','unconfirmed_topic':unknown}}
    from .request_roles import analyze
    anaphora=bool(re.search(r'\b(?:it|this|that|these|those|them)\b|อันนี้|อันนั้น|เครื่องนี้|แบบนี้|มัน',normalize(tail)))
    starts_question=bool(re.match(r'^(?:how|what|when|where|which|can|could|may|do|does|is|are)\b',tail,re.I))
    fragment=bool(re.match(r'^(?:what\s+(?:if|about)|if)\b|^ถ้า|^กรณี',tail,re.I))
    if analyze(tail) or (starts_question and not anaphora and not fragment and p['task'] not in tasks(tail)):
        return {**base,'action':'qualified_request','replacement':tail,'declined_profile_ids':base['blocked_unqualified_ids']}
    ids,audit=scope_plan(tail,records[rid],records)
    if ids and len(ids)==1:
        target=ids[0]
        return {**base,'action':'qualified_selected','record_id':target,'routing_sha256':fingerprint(records[target]),'audit':audit,
            'basis':'explicit_qualified_reply_and_declared_scope'}
    if ids and len(ids)>1:audit['reason']='ambiguous_qualified_profiles'
    return {**base,'action':'qualification_unconfirmed','audit':audit}
