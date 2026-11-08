"""Reuse trusted legacy routing patterns, never legacy answer payloads.

Rules supply only interpretation/priority/category. Current common intent_key
and source-backed answer fields determine whether any fact can be read.
"""
from functools import lru_cache
import re
from .registry import value
from .query_contract import normalize

@lru_cache(maxsize=1)
def routing_patterns():
    from app.rules.loader import load_rule_files
    from app.rules.matcher import RuleMatcher
    rows=[]
    for rule in load_rule_files():
        if not rule.get('intent'):continue
        for pattern in rule.get('patterns',[]):
            try:compiled=RuleMatcher._compile_pattern(pattern)
            except re.error:continue
            rows.append((int(rule.get('priority',0)),rule.get('category'),rule['intent'],pattern,compiled))
    return tuple(rows)

def select(question,records):
    from .question_profiles import tasks
    from .unconfirmed_request import topic
    from .query_scope import operation
    q=normalize(question);op=operation(q)
    if len(q)>1200 or tasks(q) or topic(q) or op in {'rules','rental','price','games','controls','equipment','people'}:return None
    category={'booking':'reservation','calendar':'schedule','policy':'rules'}.get(op)
    matches=[]
    for priority,cat,intent,pattern,compiled in routing_patterns():
        if category and cat!=category:continue
        match=compiled.search(q)
        if not match:continue
        remainder=q[:match.start()]+' '+q[match.end():]
        remainder=re.sub(r'\b(?:please|i|we|you|could|can|would|like|to|know|tell|me|us|do|does|must|should|the|a|an)\b|ขอสอบถาม|สอบถาม|อยากทราบ|ขอทราบ|ช่วยบอก|กรุณา|ต้อง|หน่อย|ครับ|ค่ะ|คะ|ผม|ฉัน',' ',remainder)
        if remainder.strip(' \t\n?!.,:'):continue
        ids=[rid for rid,r in records.items() if r['kind']=='faq' and value(r,'intent_key')==intent and value(r,'answer')]
        if ids:matches.append((priority,intent,pattern,ids))
    if not matches:return None
    highest=max(x[0] for x in matches);top=[x for x in matches if x[0]==highest]
    ids=list(dict.fromkeys(rid for _,_,_,group in top for rid in group))
    if len(ids)!=1:return None
    return {'record_id':ids[0],'matched_patterns':[p for _,_,p,_ in top], 'intent_keys':sorted({i for _,i,_,_ in top}),
            'priority':highest,'source':'trusted_legacy_routing_configuration','whole_query_pattern_coverage':True,'legacy_answer_read':False,'facts_provider':'current_common_snapshot'}

def source_for_need(question,need,records):
    """A previous unknown does not veto new source-backed owner content."""
    from .correction_scope import subject_types
    from .profile_confirmation import eligible
    wanted=subject_types(question)
    for rid,r in records.items():
        if r['kind'] not in {'faq','policy','procedure'}:continue
        if not any(value(r,k) for k in ('answer','steps','decision')):continue
        if value(r,'intent_key')==need:return rid
        p=value(r,'query_profile')
        if need in {'wrong_amount','identity_correction'} and isinstance(p,dict) and p.get('task')=='correction' and wanted:
            have=set().union(*(subject_types(' '.join(v for v in sub.values() if isinstance(v,str))) for sub in p.get('subjects',[])))
            if wanted<=have and rid in eligible(question,{rid:r}):return rid
    return None
