"""Bind local text to each need; retain provenance without adding answer facts.

This conservative repair supplements the trained planner. It is not a claim
that the model learned these rules, nor a general semantic parser.
"""
import re
from .scope import contains,requested_resources

ANAPHOR=r'\b(?:it|its|that|those|same)\b|เครื่องนั้น|เกมนั้น|โซนนั้น|เดียวกัน|แล้วมัน|มันมี|มันเล่น|อันเดิม|อันนั้น'
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
    from .style_scope import masked
    text=masked(text,index);found=[]
    from .controller_catalog import platform_question
    text=platform_question(index,text)
    for cat in ('C03','C04','C06','C07'):
        for labels in (index.subject_labels[cat],index.entity_labels[cat]):
            for label in labels:
                if len(label)<2 or not contains(text,label) or re.fullmatch(ANAPHOR,label,re.I):continue
                for m in re.finditer(re.escape(label),text,re.I):
                    # A short Thai noun inside a longer word is not a named
                    # referent: e.g. a screen alias embedded in booking.
                    # Reference inheritance is conservative; longer aliases
                    # or an explicit isolated mention can still bind.
                    if len(label)<=2 and re.search(r'[\u0e00-\u0e7f]',label) and (m.start()>0 and re.match(r'[\u0e00-\u0e7f]',text[m.start()-1]) or m.end()<len(text) and re.match(r'[\u0e00-\u0e7f]',text[m.end()])):continue
                    found.append(m[0])
    return list(dict.fromkeys(s for s in found if not any(s.casefold()!=t.casefold() and s.casefold() in t.casefold() for t in found)))

def apply(question,index,result):
    if not result.accepted or index is None:return result
    from .context_bindings import service_game_relation
    from .named_spans import quantity_in_name,range_in_name
    audits=[];previous=None
    from .understanding import style_only_quote
    if len(result.tasks)>1:
        keep=[]
        for task in result.tasks:
            if style_only_quote(task.quote) and not named_targets(index,task.quote):
                audits.append({'action':'presentation_modifier_not_factual_task','task_quote':task.quote,'proposed_category':task.category})
            else:keep.append(task)
        if keep:result.tasks=keep
    for task in result.tasks:
        from .style_scope import masked
        from .execution_dependencies import referent_text
        local=task.quote;anaphor=bool(re.search(ANAPHOR,referent_text(masked(local,index)),re.I));shared=''
        from .controller_catalog import request as controller_request
        device=controller_request(index,local) if task.category=='C04' else None
        from .package_intent import mentions as package_mentions
        packages=package_mentions(index,local) if task.category=='C07' else []
        def package_only(quote):
            hits=list(re.finditer(re.escape(quote),local,re.I)) if quote else []
            return bool(hits and all(any(p['start']<=m.start() and m.end()<=p['end'] for p in packages) for m in hits))
        def device_only(quote):
            hits=list(re.finditer(re.escape(quote),local)) if quote else []
            return bool(device and hits and all(device['source_span']['start']<=m.start() and m.end()<=device['source_span']['end'] for m in hits))
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
                  and (index.bind('C04',names[0]) or service_game_relation(index,names[0])['entity_refs'])):
                shared=names[0];shared_basis='source_related_service_game_ellipsis'
            elif (not anaphor and len(names)==1 and task.category=='C08' and previous.category in {'C03','C04','C06','C07'}
                  and not named_targets(index,local) and re.search(r'จอง(?:ยังไง|อย่างไร)|how (?:do I|to) book',local,re.I)
                  ):
                shared=names[0];shared_basis='source_related_booking_ellipsis'

        allowed=[]
        for c in task.constraints:
            if c['slot'] in {'service','platform'} and package_only(c['quote']):
                audits.append({'action':'package_name_component_is_not_separate_service_or_platform','task_quote':local,'constraint':c});continue
            if c['slot'] in {'service','platform'} and device_only(c['quote']):
                audits.append({'action':'input_device_is_not_console_or_service_slot','task_quote':local,'constraint':c});continue
            if c['slot'] in {'duration','persons','sessions'} and quantity_in_name(index,local,c['quote'],task.target or None):
                audits.append({'action':'removed_quantity_inside_source_entity_name','task_quote':local,'constraint':c});continue
            # A shared referent is not permission to inherit another need's
            # price, audience, duration or negation. Preserve only the name.
            if c['quote'] in local or (shared and c['slot'] in {'service','platform'} and contains(shared,c['quote'])):allowed.append(c)
            else:audits.append({'action':'removed_cross_need_constraint','task_quote':local,'constraint':c})
        if task.target and task.target not in local and not (shared and contains(shared,task.target)):
            audits.append({'action':'removed_unrelated_target','task_quote':local,'target':task.target});task.target=''
        if device and device_only(task.target):
            audits.append({'action':'input_device_model_is_not_game_target','task_quote':local,'target':task.target});task.target=''
        if device and not any(c['slot']=='requested_scope' and c['quote']==device['source_span']['text'] for c in allowed):allowed.append({'slot':'requested_scope','quote':device['source_span']['text'],'source_record_id':''})
        if shared and not task.target:
            task.target=shared;audits.append({'action':shared_basis,'task_quote':local,'source_quote':shared})
            if task.category=='C05' and index.bind('C05',shared):
                # The earlier generic "which game?" ambiguity is resolved.
                # Platform/layout ambiguity is still checked by the control reader.
                task.ambiguous=False;audits.append({'action':'control_referent_resolved','task_quote':local,'source_quote':shared})
        for slot,pattern in PATTERNS:
            for match in re.finditer(pattern,local,re.I):
                if slot=='platform' and any(p['start']<=match.start() and match.end()<=p['end'] for p in packages):continue
                if slot=='platform' and device and device['source_span']['start']<=match.start() and match.end()<=device['source_span']['end']:continue
                if slot in {'duration','persons','sessions'} and range_in_name(index,local,match.start(),match.end(),task.target or None):continue
                c={'slot':slot,'quote':match[0],'source_record_id':''}
                if not any(x['slot']==slot and x['quote']==match[0] for x in allowed):allowed.append(c)
        task.constraints=allowed
        from .policy_scope import local_booking_reference
        booking_reference=task.category=='C08' and local_booking_reference(local)
        if anaphor and not booking_reference and task.category in {'C03','C04','C05','C06','C07','C08','C12'} and not task.target and not named_targets(index,local):
            task.ambiguous=True;audits.append({'action':'unresolved_referent','task_quote':local})
        # No conversion of an ordinary opening question into occupancy.
        vacant=bool(re.search(r'ว่าง|available|\bfree\b|ถูกจอง',local,re.I))
        now=bool(re.search(r'ตอนนี้|right now|\btoday\b|\btomorrow\b|วันนี้|พรุ่งนี้|\d{1,2}:\d\d|20\d\d[-/]',local,re.I))
        if vacant and now and task.category in {'C11','C12'}:
            task.domain='live';task.category='C12';task.operation='availability';task.facet='live_status'
            if not requested_resources(local+' '+task.target):
                from app.booking.live_status import _resource_scopes,_asks_resource_list
                if not _resource_scopes(local+' '+task.target) and not _asks_resource_list(local):task.ambiguous=True
            audits.append({'action':'occupancy_distinct_from_regular_timetable','task_quote':local})
        durations=[c['quote'] for c in allowed if c['slot']=='duration']
        additive=bool(re.search(r'\d+\s*(?:ชั่วโมง|hours?|hrs?)\s*(?:and\s*)?\d+\s*(?:นาที|minutes?)',local,re.I))
        if task.category in {'C06','C07'} and len(set(durations))>1 and not additive and task.operation!='compare' and not re.search(r'ต่อ|/|per\b|each\b|session|รอบ|เปรียบเทียบ|compare|different|ต่างจาก|ต่างกัน|หรือ|\bor\b',local,re.I):
            task.ambiguous=True;audits.append({'action':'duration_roles_not_distinguished','source_quotes':durations})
        previous=task
    if audits:result.event['context_scope_review']=audits
    result.event['context_scope_version']='r129'
    from .context_bindings import compile_shared
    return compile_shared(question,index,result)
