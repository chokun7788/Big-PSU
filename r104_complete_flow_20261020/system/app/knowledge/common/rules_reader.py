"""Named rulebook and clause reads with same-event dependency closure."""
import re,time
from .registry import value
from .query_contract import strip_names,normalize

def answer(reader,need,snap,at,lang):
    if need.task!='competition_rules':return None
    from .answer import effective,title,text,named
    records=snap['release']['records'];names=snap['release']['names'];q=need.query
    ids=[k for k in need.record_ids if k in records]
    games=[k for k in ids if records[k]['kind']=='game']
    explicit_rules=[k for k in ids if records[k]['kind']=='competition_rule']
    events=[k for k in ids if records[k]['kind']=='competition']
    events=list(dict.fromkeys(events+[value(records[k],'competition_id') for k in explicit_rules]))
    if not events and games:events=[k for k,r in records.items() if r['kind']=='competition' and value(r,'game_id') in games]
    if not games and not events:
        choices=[k for k,r in records.items() if r['kind']=='game' and any(e['kind']=='competition' and value(e,'game_id')==k for e in records.values())]
        if not choices:return None
        body=('ต้องการกติกาของเกมไหนครับ: ' if lang=='th' else 'Which game rules do you mean: ')+', '.join(title(records[k],lang) for k in choices)
        return reader.finish(snap,time.perf_counter(),body,[],{'record_ids':[],'requested_fields':[],'method':'r103_rule_game_slot','pending_selection':{'candidate_ids':choices,'subject_kind':'game','allow_all':False}},[],response='clarification')
    if len(events)!=1:
        body=('ยังไม่มีเอกสารกติกาที่ตรงกับเกมนี้ครับ' if lang=='th' else 'No rulebook matching this game is recorded.') if not events else (('ต้องการกติกาของรายการไหนครับ: ' if lang=='th' else 'Which event rulebook do you mean: ')+', '.join(title(records[k],lang) for k in events))
        return reader.finish(snap,time.perf_counter(),body,[],{'record_ids':[],'requested_fields':[],'method':'r103_rulebook_scope','bridge_status':'missing_rulebook' if not events else 'event_selection','pending_selection':{'candidate_ids':events,'subject_kind':'competition','allow_all':False} if events else None},[],response='clarification' if events else 'unconfirmed')
    event=events[0]
    if not effective(records[event],at,records):return None
    children=[k for k,r in records.items() if r['kind']=='competition_rule' and value(r,'competition_id')==event and effective(r,at,records)]
    semantic_clause_selection=bool(explicit_rules and all(records[k]['kind']=='competition_rule' for k in ids))
    if not semantic_clause_selection:
        from .competition_bridge import answer as mature_clause
        prior=mature_clause(reader,snap,time.perf_counter(),q,lang,records,[event],at,{'record_ids':[event]})
        if prior is not None:return prior
    residual=strip_names(q,ids+[event,value(records[event],'game_id')],names)
    # Owner-authored headings are the primary dynamic topic vocabulary.
    def topic(t):
        t=normalize(t);t=re.sub(r'\bdisconnect(?:ed|ion)?\b','disconnect',t)
        return re.sub(r'ก่อน|หลัง|\b(?:before|after|the)\b|[\s?!.,]','',t)
    chosen=[k for k in children if any(topic(h) and topic(h) in topic(residual) for h in (value(records[k],'heading') or {}).values() if isinstance(h,str) and len(h)>2)]
    if semantic_clause_selection:chosen=list(explicit_rules)
    # Coordinated before/after clauses share a topic, not one selected phase.
    if re.search(r'ก่อน.*หลัง|\bbefore\b.*\bafter\b',q,re.I):
        generic={'before','after','first','the','and','rules','competition','tournament','for','what','how','does','differ'}
        tokens={w for w in re.findall(r'[a-z]{4,}',residual.casefold()) if w not in generic}
        for k in children:
            body=str(value(records[k],'text') or '').casefold()
            if tokens and any(re.search(r'\b'+re.escape(w)+r'\b',body) for w in tokens) and k not in chosen:chosen.append(k)
    if not chosen:
        # Reuse the old proposition interpreter for detailed domain questions.
        from .competition_bridge import answer as legacy_clause
        bridge=legacy_clause(reader,snap,time.perf_counter(),q,lang,records,[event],at,{'record_ids':[event]})
        if bridge is not None:return bridge
        # Selection helper is optional across retained adapters; generic overview
        # is accepted only when the residual contains no extra proposition.
        residue=re.sub(r'กฎ|กติกา|การแข่งขัน|แข่งขัน|แข่ง|ขอ|มีอะไรบ้าง|มีอะไรมั่ง|เรื่อง|ก่อน|หลัง|และ|\b(?:what|are|the|competition|tournament|rules?|rulebook|for|of|in|all|entire|complete|every|please|explain|before|after|and)\b|[\s?!.,:ๆ]','',residual,flags=re.I)
        if not residue:chosen=children
        else:return None
    chosen=list(dict.fromkeys(chosen));queue=list(chosen)
    for k in queue:
        r=records.get(k)
        if not r or value(r,'competition_id')!=event:return _gap(reader,snap,lang,'broken_relation')
        if value(r,'completeness')!='complete':return _gap(reader,snap,lang,'missing_source')
        for dep in value(r,'depends_on_ids') or []:
            if dep not in records or value(records[dep],'competition_id')!=event:return _gap(reader,snap,lang,'broken_relation')
            if dep not in chosen:chosen.append(dep);queue.append(dep)
    if not chosen:return _gap(reader,snap,lang,'missing_source')
    from .source_rows import render
    return render(reader,snap,[(k,['competition_id','heading','text','completeness','depends_on_ids']) for k in chosen],lang,
      {'method':'r103_source_rule_closure','operation':'rules','task_plan':{'task':'competition_rules'},'event_id':event,'dependency_closure':chosen,'scope_ids':[event]},caption=('กติกาตามเอกสาร — ' if lang=='th' else 'Rulebook — ')+title(records[event],lang))

def _gap(reader,snap,lang,status):
    from dataclasses import replace
    result=reader.finish(snap,time.perf_counter(),'ข้อกติกาหรือข้อที่อ้างถึงยังไม่ครบ จึงยังยืนยันไม่ได้ครับ' if lang=='th' else 'The clause or its required references are incomplete; this rule cannot be confirmed.',[],{'record_ids':[],'requested_fields':[],'method':'r103_rule_dependency_gap'},[],response='unconfirmed')
    return replace(result,decision_artifact={**result.decision_artifact,'need_results':[{'need_id':'n1','task':'competition_rules','status':status,'reason_codes':['rule_dependency_incomplete'],'receipts':[]}]})
