"""Bounded missing-personal-role guard, never a guessed audience correction."""
import re
from .scope import norm,contains
from .projection import title,value

def request(index,question):
    from .financial import audience_mentions,service_scope
    q=norm(question);positive,negative=audience_mentions(index,q)
    excluded_negative_aliases=set()
    if negative:
        # A migrated alias "not a student" can overlap "not a PSU student".
        # Excluding one source group does not independently assert another.
        for rid in positive:
            record=index.records.get(rid,{})
            matched=[norm(s) for s in [*title(record).values(),*sum(record.get('aliases',{}).values(),[])] if s and contains(q,norm(s))]
            if matched and all(re.match(r'^(?:ไม่ใช่|ไม่ได้เป็น|not\b)',label,re.I) for label in matched):excluded_negative_aliases.add(rid)
        positive=positive-excluded_negative_aliases
    services=service_scope(index,q)
    masked=q
    # A source entity named "Student Lounge" does not assert the caller's role.
    labels=[]
    for record in index.records.values():
        if record.get('kind') in {'service','availability','resource','zone','game'}:
            labels.extend([*title(record).values(),*sum(record.get('aliases',{}).values(),[])])
    for label in sorted({norm(s) for s in labels if isinstance(s,str) and s},key=len,reverse=True):
        if len(label)>=3:masked=re.sub(re.escape(label),' ',masked)
    price=bool(re.search(r'ราคา|กี่บาท|เสียกี่|ค่าบริการ|ค่าเล่น|คิดเงิน|\b(?:price|cost|fees?)\b|how much',masked,re.I))
    role=bool(re.search(r'นักศึกษา|\bstudents?\b',masked,re.I))
    all_groups=bool(re.search(r'ทุกกลุ่ม|แต่ละกลุ่ม|\b(?:all|each)\s+(?:(?:user|audience|student)\s+)?groups?\b|\ball audiences\b',masked,re.I))
    if re.search(r'ไม่(?:ได้)?(?:ถาม|ต้องการ|เอา).{0,15}(?:ทุกกลุ่ม|แต่ละกลุ่ม)|\bnot\b.{0,15}\ball\b',masked,re.I):all_groups=False
    unresolved=bool(services and price and not positive and (role or negative) and not all_groups)
    ids=sorted({value(index.records[f['record_id']],'audience_id') for f in index.bycat['C06'] if index.records.get(f['record_id'],{}).get('kind')=='rate' and value(index.records[f['record_id']],'service_id') in services}-{None})
    choices=[{'record_id':rid,'label':title(index.records[rid])} for rid in ids if rid not in negative and rid in index.records]
    return {'unresolved':unresolved,'positive_audience_ids':sorted(positive),'negative_audience_ids':sorted(negative),'excluded_negative_alias_positive_ids':sorted(excluded_negative_aliases),'service_ids':sorted(services),'choices':choices,'explicit_all_groups':all_groups,'basis':'source_bound_service_with_unresolved_student_or_negated_personal_role','semantic_interpretation_verified':False}

def notice(scope,lang):
    labels=[c['label'].get(lang) or c['label'].get('en') or c['label'].get('th') for c in scope['choices']]
    prefix='กรุณายืนยันกลุ่มผู้ใช้ก่อนระบุราคาครับ' if lang=='th' else 'Please confirm your user group before a price is selected.'
    return prefix+((' กลุ่มในข้อมูล: ' if lang=='th' else ' Recorded groups: ')+', '.join(labels) if labels else '')
