from .selection_surface import canonical as selection_surface
"""Data-derived game ambiguity and delivered target selection, not new facts."""
import re,time
from .query_contract import normalize,matches
from .registry import value
from .followup_scope import delivered_state

def _operation(question):
    q=normalize(question)
    if re.search(r'เล่นได้ที่ไหน|อยู่โซนไหน|มีให้เล่นที่ไหน|\b(?:where (?:can|do)|which (?:studio )?zone|available at|do you have)\b',q):return 'game_at_studio'
    if re.search(r'คือเกมอะไร|เป็นเกมอะไร|\b(?:what is|what kind of game|overview|tell me about)\b',q):return 'game_overview'
    if re.search(r'กี่คน|\bhow many players\b',q):return 'game_players'
    return None

def answer(reader,question,snap,records,names,lang,history,at,planner):
    from .answer import title
    q=selection_surface(question);state=delivered_state(history) or {};pending=state.get('pending_target') or {}
    games={k:r for k,r in records.items() if r['kind']=='game'}
    if pending.get('version')==1 and pending.get('task') in {'game_at_studio','game_overview','game_players'}:
        candidates=pending.get('candidate_ids',[])
        if isinstance(candidates,list) and len(candidates)<=50:
            selected=[k for k in candidates if k in games and any(normalize(a)==q for a in names.get(k,[]))]
            number=re.fullmatch(r'(?:อันที่|รายการที่|option|number|#)\s*(\d+)',q)
            if number and 1<=int(number[1])<=len(candidates):
                target=candidates[int(number[1])-1];selected=[target] if target in games else []
            if len(selected)==1:
                rid=selected[0];task=pending['task']
                # Replace only the ambiguous mention. Keep all original
                # conditions; a selected edition cannot erase a year/exception.
                original=pending.get('original_query');mention=pending.get('source_mention')
                if not isinstance(original,str) or not isinstance(mention,str) or not mention or len(original)>4000:return None
                active=re.sub(re.escape(mention),lambda m:title(games[rid],'en'),original,count=1,flags=re.I)
                if active==original:return None
                result=reader.answer(active,locale=lang,history=[],at=at,planner=planner,_composing=True,_snapshot=snap)
                if result is not None:
                    art=result.decision_artifact
                    binding={'task':task,'record_id':rid,'origin':'current_user','task_origin':'delivered_state','source_span':question,'previous_answer_facts_used':False}
                    art['target_binding']=binding
                    rp=art.get('request_plan',{});rp['question']=question
                    for need in rp.get('needs',[]):
                        need.update(source_span=question,slot_origin='delivered_state_selection',slots={'subject':{'record_ids':[rid],'origin':'current_user','source_span':question},'task':{'value':task,'origin':'delivered_state'},'qualified_query':{'quote':original,'origin':'delivered_state','binding_reason':'preserve_original_constraints'}})
                    for row in art.get('need_results',[]):row.update(source_span=question,slots=rp.get('needs',[{}])[0].get('slots',{}))
                return result
    task=_operation(question)
    if not task:return None
    # Explicitly naming two complete titles is a multi-subject request, not
    # an edition ambiguity. The shared composer retains that case.
    exact=[k for k,r in games.items() if any(isinstance(t,str) and matches(q,t) for t in (value(r,'title') or {}).values())]
    if len(exact)==1:return None
    if len(exact)>1:return None
    aliases={}
    for rid in games:
        for alias in names.get(rid,[]):
            a=normalize(alias)
            if len(a)>=3 and matches(q,a):aliases.setdefault(a,set()).add(rid)
    groups=[(len(a),a,ids) for a,ids in aliases.items() if len(ids)>1]
    # Match title prefixes even when a shorter shared alias already matched.
    # Punctuation (e.g. a colon before an edition) is a title boundary too.
    for chunk in re.findall(r'[a-z0-9]+(?:[ :\-]+[a-z0-9]+){1,8}',q):
        words=chunk.split()
        for start in range(len(words)-1):
            for length in range(2,len(words)-start+1):
                a=' '.join(words[start:start+length]);ids={k for k,r in games.items() if any(isinstance(t,str) and normalize(t).startswith(a) and len(normalize(t))>len(a) and normalize(t)[len(a)] in ' :-—' for t in (value(r,'title') or {}).values())}
                if len(ids)>1:groups.append((len(a),a,ids))
    if not groups:return None
    _,mention,ids=max(groups,key=lambda r:r[0]);ids=sorted(ids)
    body=('หมายถึงเกมฉบับใดครับ: ' if lang=='th' else 'Which game edition do you mean: ')+ ' / '.join(title(games[k],lang) for k in ids)
    plan={'record_ids':[],'requested_fields':[],'operation':'context','method':'catalog_target_ambiguity','pending_target':{'version':1,'task':task,'candidate_ids':ids,'source_mention':mention,'original_query':question},'source_answer_confirmed':False}
    return reader.finish(snap,time.perf_counter(),body,[],plan,[],response='clarification')

def unmatched_mention(question,records,names):
    match=re.search(r'\bgame\s+(?:called|named)\s+[\"\x27]?([^?!.\n\"\x27]{2,100})|เกมชื่อ\s*[\"\x27]?([^?!.\n\"\x27]{2,100})',question,re.I)
    if not match:return None
    name=(match[1] or match[2]).strip()
    if any(normalize(name)==normalize(alias) for k,r in records.items() if r['kind']=='game' for alias in names.get(k,[])):return None
    return name
