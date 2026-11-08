"""Bind local text to each need; retain provenance without adding answer facts.

This conservative repair supplements the trained planner. It is not a claim
that the model learned these rules, nor a general semantic parser.
"""
import re
from .scope import contains,requested_resources

ANAPHOR=r'\b(?:it|its|that|those|same)\b|เครื่องนั้น|เกมนั้น|โซนนั้น|เดียวกัน'
PATTERNS=(
 ('duration',r'(?<![\w.])(?:one and a half|half an?|one|two|three|four|five|six|a|an|\d+(?:\.\d+)?)\s*(?:hours?|hrs?|minutes?)\b|(?:\d+(?:\.\d+)?|หนึ่ง|สอง|สาม|ครึ่ง)\s*(?:ชั่วโมง|นาที)'),
 ('persons',r'\b\d+\s*(?:people|persons?|players?)\b|\d+\s*คน'),
 ('sessions',r'\b\d+\s*sessions?\b|\d+\s*รอบ'),
 ('date',r'(?<!\d)20\d\d[-/]\d\d[-/]\d\d(?!\d)|\b(?:today|tomorrow|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b|วันนี้|พรุ่งนี้|(?:วัน)?(?:จันทร์|อังคาร|พุธ|พฤหัสบดี|ศุกร์|เสาร์|อาทิตย์)'),
 ('time',r'(?<!\d)\d{1,2}:\d{2}(?!\d)|\b\d{1,2}\s*(?:am|pm)\b|ตอนนี้|right now|ช่วงบ่าย|ตอนบ่าย|ช่วงเช้า|ตอนเช้า'),
 ('platform',r'PlayStation(?:\s*/\s*PS5|\s*5)?|\bPS5\b|\bPC\b|Nintendo Switch'),
 ('negation',r'ไม่ได้ถามเรื่อง(?:กิน|ดื่ม)|ไม่ใช่(?:นักศึกษา)?\s*PSU|\bnot asking(?: about)? (?:eating|drinking)\b|\bwithout\s+booking\b|\bnot(?: an?| a)?\s+PSU(?:\s+(?:student|staff))?\b'),
)

def named_targets(index,text):
    """Exact source entity labels only, returning the user's original spelling."""
    found=[]
    for cat in ('C03','C04','C06','C07'):
        for labels in (index.subject_labels[cat],index.entity_labels[cat]):
            for label in labels:
                if len(label)<2 or not contains(text,label) or re.fullmatch(ANAPHOR,label,re.I):continue
                for m in re.finditer(re.escape(label),text,re.I):found.append(m[0])
    return list(dict.fromkeys(s for s in found if not any(s.casefold()!=t.casefold() and s.casefold() in t.casefold() for t in found)))

def apply(question,index,result):
    if not result.accepted or index is None:return result
    audits=[];previous=None
    for task in result.tasks:
        local=task.quote;anaphor=bool(re.search(ANAPHOR,local,re.I));shared=''
        if task.target and re.fullmatch(ANAPHOR,task.target,re.I):
            audits.append({'action':'pronoun_is_not_an_entity_target','source_quote':task.target});task.target=''
        shared_basis='unique_previous_source_named_referent'
        if previous is not None:
            names=named_targets(index,previous.quote)
            if anaphor and len(names)==1:shared=names[0]
            elif (not anaphor and len(names)==1 and task.category=='C04'
                  and previous.category in {'C03','C06','C07','C08'}
                  and not named_targets(index,local)
                  and task.facet in {'game_catalog','studio_services'}
                  and index.bind('C04',names[0])):
                shared=names[0];shared_basis='source_related_service_game_ellipsis'

        allowed=[]
        for c in task.constraints:
            # A shared referent is not permission to inherit another need's
            # price, audience, duration or negation. Preserve only the name.
            if c['quote'] in local or (shared and c['slot'] in {'service','platform'} and contains(shared,c['quote'])):allowed.append(c)
            else:audits.append({'action':'removed_cross_need_constraint','task_quote':local,'constraint':c})
        if task.target and task.target not in local and not (shared and contains(shared,task.target)):
            audits.append({'action':'removed_unrelated_target','task_quote':local,'target':task.target});task.target=''
        if shared and not task.target:
            task.target=shared;audits.append({'action':shared_basis,'task_quote':local,'source_quote':shared})
        for slot,pattern in PATTERNS:
            for match in re.finditer(pattern,local,re.I):
                c={'slot':slot,'quote':match[0],'source_record_id':''}
                if not any(x['slot']==slot and x['quote']==match[0] for x in allowed):allowed.append(c)
        task.constraints=allowed
        if anaphor and task.category in {'C03','C04','C05','C06','C07','C08','C12'} and not task.target and not named_targets(index,local):
            task.ambiguous=True;audits.append({'action':'unresolved_referent','task_quote':local})
        # No conversion of an ordinary opening question into occupancy.
        vacant=bool(re.search(r'ว่าง|available|\bfree\b|ถูกจอง',local,re.I))
        now=bool(re.search(r'ตอนนี้|right now|\btoday\b|\btomorrow\b|วันนี้|พรุ่งนี้|\d{1,2}:\d\d|20\d\d[-/]',local,re.I))
        if vacant and now and task.category in {'C11','C12'}:
            task.domain='live';task.category='C12';task.operation='availability';task.facet='live_status'
            if not requested_resources(local+' '+task.target):task.ambiguous=True
            audits.append({'action':'occupancy_distinct_from_regular_timetable','task_quote':local})
        durations=[c['quote'] for c in allowed if c['slot']=='duration']
        if task.category in {'C06','C07'} and len(set(durations))>1 and task.operation!='compare' and not re.search(r'ต่อ|/|per\b|each\b|session|รอบ|เปรียบเทียบ|compare|different|ต่างจาก|ต่างกัน|หรือ|\bor\b',local,re.I):
            task.ambiguous=True;audits.append({'action':'duration_roles_not_distinguished','source_quotes':durations})
        previous=task
    if audits:result.event['context_scope_review']=audits
    result.event['context_scope_version']='r122';return result
