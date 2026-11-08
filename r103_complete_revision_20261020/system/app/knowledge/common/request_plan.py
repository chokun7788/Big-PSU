"""Shared request/need boundary. Reads schema and identifiers, never legacy facts."""
from dataclasses import dataclass, asdict, replace, field
import re
from .query_contract import normalize, live_request, matches
from .registry import value

VERSION='common_request_plan_v3'

@dataclass
class Need:
    id: str
    task: str
    query: str
    source_span: str
    record_ids: list
    qualifiers: list
    slot_origin: str = 'current_user'
    predicate: str = 'unresolved'
    slots: dict = field(default_factory=dict)
    required_claims: list = field(default_factory=list)
    hard_dependencies: list = field(default_factory=list)

@dataclass
class RequestPlan:
    version: str
    question: str
    needs: list
    scope: dict

def task_of(question):
    from .intent_contracts import infer
    return infer(question)['task']

def _subjects(question,records,names):
    from .answer import named
    ids,_=named(question,{k:v for k,v in names.items() if k in records},allow_fuzzy=False)
    ids=[k for k in ids if records[k]['kind'] not in {'faq','policy','procedure','audience'}]
    games=[k for k in ids if records[k]['kind']=='game'];task=task_of(question)
    if games and task.startswith('game_'):return games
    if games and task in {'price','rental'}:
        from .query_contract import strip_names
        residual=strip_names(question,games,names)
        others,_=named(residual,{k:names.get(k,[]) for k in ids if k not in games},allow_fuzzy=False)
        return games+others
    return ids

def split_needs(question,records,names):
    """Split explicit task coordination only; protect owner-entered full names."""
    q=normalize(question);spans=[]
    # Protect conjunctions in titles (e.g. a game named with 'and').
    for aliases in names.values():
        for alias in aliases:
            a=normalize(alias)
            if len(a)<4:continue
            for m in re.finditer(re.escape(a),q):spans.append(m.span())
    cuts=[m for m in re.finditer(r'\band\b|\balso\b|แล้ว(?:ก็)?|และ|กับ|[;\n]',q) if not any(a<=m.start()<b for a,b in spans)]
    if not 1<=len(cuts)<=3:return []
    parts=[];pos=0
    for cut in cuts:parts.append(q[pos:cut.start()].strip(' ?!.,'));pos=cut.end()
    parts.append(q[pos:].strip(' ?!.,'))
    if not all(parts):return []
    tasks=[task_of(part) for part in parts]
    # Do not split noun phrases or a condition joined to the same proposition.
    request_cues=r'ราคา|กี่บาท|คือเกมอะไร|เป็นเกมอะไร|ที่ไหน|อยู่ไหน|ยังไง|อย่างไร|มีอะไร|กี่คน|ว่างไหม|\b(?:what|where|how|can i|may i|is .*available|price|cost|fee|list|explain|describe|game overview)\b'
    fee_tuples=all(re.search(r'\d+\s*(?:ชั่วโมง|นาที|hours?|minutes?)',p,re.I) and _subjects(p,records,names) for p in parts)
    if fee_tuples:parts=[p if task_of(p)=='price' else p+' price' for p in parts];tasks=['price']*len(parts)
    if any(not re.search(request_cues,part,re.I) for task,part in zip(tasks,parts)):return []
    if any(re.match(r'^(?:ถ้า|ยกเว้น|เฉพาะ|ก่อน|หลัง|if\b|unless\b|except\b|before\b|after\b)',part) for part in parts[1:]):return []
    # A single rulebook's compound clause must retain its original scope.
    if all(t=='competition_rules' for t in tasks):return []
    first=_subjects(parts[0],records,names)
    from .audience_scope import resolve as audience_scope
    shared_groups,group_audit=audience_scope(question,records)
    share_audience=bool(shared_groups and len(shared_groups)==1 and re.search(r'สำหรับ|\bfor\b',parts[-1],re.I))
    result=[]
    for part,task in zip(parts,tasks):
        ids=_subjects(part,records,names);active=part
        if not ids and len(first)==1 and task in {'procedure','price','live_status','game_controls','game_how_to_play'} and records[first[0]]['kind'] in {'game','service','resource','zone'}:
            from .answer import title
            active=part+' '+title(records[first[0]],'en');ids=list(first)
        part_groups,_=audience_scope(part,records)
        shared=None
        if share_audience and not part_groups and task in {'price','rental'}:
            from .answer import title
            active+=' for '+title(records[shared_groups[0]],'en')
            shared={'record_ids':shared_groups,'origin':'derived_with_rule','rule':'trailing_audience_applies_to_coordinated_fee_requests','source_span':question}
        result.append({'query':active,'source_span':part,'task':task,'record_ids':ids,'shared_audience':shared})
    return result

def make_plan(question,records,names,history=None,*,split=True):
    clauses=split_needs(question,records,names) if split else []
    if not clauses:clauses=[{'query':question,'source_span':question,'task':task_of(question),'record_ids':_subjects(question,records,names)}]
    qualifiers=lambda q:[m.group() for m in re.finditer(r'\d+(?:[:./-]\d+)*|ไม่|ห้าม|ยกเว้น|เฉพาะ|ก่อน|หลัง|\b(?:not|no|without|except|unless|only|before|after)\b',q,re.I)]
    from .followup_scope import delivered_state
    prior=delivered_state(history)
    from .pending_bindings import bind
    binding=bind(question,history,records,names) if not clauses or len(clauses)==1 else None
    scope={'release_bound_at_read':True,'history_has_trusted_state':bool(prior),'candidate_source':'common_snapshot','all_requested':bool(re.search(r'ทั้งหมด|ทุกบริการ|ทุกเครื่อง|\b(?:all|every|everything)\b',normalize(question)))}
    from .intent_contracts import infer
    needs=[]
    for i,r in enumerate(clauses,1):
        contract=infer(r['query'],records,r['record_ids']);slots={}
        if r.get('shared_audience'):slots['audience']=r['shared_audience']
        if binding:
            slots=binding['slots'];contract={'task':binding['task'],'predicate':binding.get('predicate','current_rate')}
            r={**r,'record_ids':binding.get('service_ids',[])}
        needs.append(Need('n'+str(i),contract['task'],r['query'],r['source_span'],r['record_ids'],qualifiers(r['source_span']), 'delivered_state_selection' if binding and binding.get('action') in {'price_selection','rental_selection'} else 'current_user',contract['predicate'],slots,[contract['predicate']] if contract['task']!='unresolved' else []))
    if binding:scope['pending_binding']=binding
    return RequestPlan(VERSION,question,needs,scope)

def attach(result,plan,snap=None):
    if result is None:return None
    art=dict(result.decision_artifact or {})
    if art.get('request_plan',{}).get('version')==VERSION:return result
    query=art.get('query_plan') or {}
    from .claim_coverage import evaluate
    from .result_contract import status as result_status
    if art.get('need_results') and (art.get('mapped_claim_packets') or query.get('graph_result') or query.get('method')=='r103_rule_dependency_gap'):
        art['request_plan']=asdict(plan)
        return replace(result,decision_artifact=art)
    rows=[]
    for need in plan.needs:
        coverage=evaluate(need,result,snap)
        status,reasons=result_status(result,coverage)
        rows.append({'need_id':need.id,'task':need.task,'predicate':need.predicate,'source_span':need.source_span,'status':status,'reason_codes':reasons,'slots':need.slots,'record_ids':list(query.get('record_ids',[])),'receipts':coverage['receipts'],'coverage':coverage,'coverage_basis':'typed predicate contract where available; unmigrated scope remains unverified'})
    if len(rows)==1 and rows[0]['coverage']['decision']=='predicate_mismatch' and art.get('response_type') in {'answer','list','partial_answer'}:
        # Correct pointers cannot justify a different requested predicate.
        lang='en' if any('a'<=c.lower()<='z' for c in plan.question) and not any('\u0e00'<=c<='\u0e7f' for c in plan.question) else 'th'
        body='ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ' if lang=='th' else 'The selected source does not directly confirm the requested detail.'
        art['response_type']='unconfirmed';art['predicate_rejection']={'reason_codes':rows[0]['reason_codes'],'original_mode':result.mode}
        art['obligations']=[]
        result=replace(result,answer=body,hits=[],mode='pipeline:common_unconfirmed',route=replace(result.route,answer_type='unconfirmed'))
    art.update(request_plan=asdict(plan),need_results=rows)
    if snap:art['request_plan_snapshot']={'release_id':snap['active'],'epoch':snap['epoch']}
    return replace(result,decision_artifact=art)

def aggregate(reader,snap,started,plan,results,lang):
    """Each child retains its own subject, status and evidence; no fact inference."""
    blocks=[];hits=[];obs=[];needs=[];children=[]
    executed_status={need.id:((r.decision_artifact or {}).get('need_results') or [{}])[0].get('status','missing_source') if r is not None else 'missing_source' for need,r in zip(plan.needs,results)}
    for need,result in zip(plan.needs,results):
        unmet=[dep for dep in need.hard_dependencies if executed_status.get(dep)!='supported']
        if unmet:
            text='ยังคำนวณส่วนนี้ไม่ได้ เพราะข้อมูลที่ต้องใช้ยังไม่ยืนยัน' if lang=='th' else 'This part cannot be derived because required inputs are not confirmed.'
            result=reader.finish(snap,started,text,[],{'record_ids':[],'requested_fields':[],'unmet_dependencies':unmet},[],response='unconfirmed')
            result=replace(result,decision_artifact={**result.decision_artifact,'need_results':[{'need_id':need.id,'status':'missing_source','unmet_dependencies':unmet,'receipts':[]}]})
        if result is None:
            text=('ยังตีความส่วนนี้ไม่ชัด กรุณาระบุหัวข้อหรือรายการของส่วนนี้เพิ่มครับ' if lang=='th' else 'This part is not clear yet. Please specify its topic or item.') if need.task=='unresolved' else ('ยังไม่มีข้อมูลยืนยันสำหรับส่วนนี้' if lang=='th' else 'No confirmed source is available for this part.')
            status='ambiguous_interpretation' if need.task=='unresolved' else 'missing_source';rows=[];art={}
        else:
            art=result.decision_artifact or {};rows=art.get('need_results',[])
            status=rows[0]['status'] if rows else 'missing_source'
            text=result.answer
            if not result.validation.ok:
                text='ยังยืนยันคำตอบภายใต้เงื่อนไขส่วนนี้ไม่ได้' if lang=='th' else 'The source does not confirm this part under the stated conditions.'
                rows=[{**r,'receipts':[]} for r in rows]
            else:
                rename={}
                for h in result.hits:
                    label='S'+str(len(hits)+1);rename[h.get('citation_label')]=label;hits.append({**h,'citation_label':label})
                text=re.sub(r'\[(S\d+)\]',lambda m:'['+rename.get(m[1],m[1])+']',text)
                obs.extend(art.get('obligations',[]))
        blocks.append(str(len(blocks)+1)+'. '+need.source_span+'\n'+text)
        row=rows[0] if rows else {'status':status,'receipts':[]}
        receipts=[{**receipt,'need_id':need.id} for receipt in row.get('receipts',[])]
        coverage={**row.get('coverage',{}),'receipts':[{**receipt,'need_id':need.id} for receipt in row.get('coverage',{}).get('receipts',[])]}
        needs.append({**row,'need_id':need.id,'task':need.task,'source_span':need.source_span,'receipts':receipts,'coverage':coverage})
        children.append({'need_id':need.id,'query':need.query,'clause':need.source_span,'need_status':'answered' if status=='supported' else status,'need_ledger':art.get('need_ledger'),'response_type':art.get('response_type'),'query_plan':art.get('query_plan'),'status':status,'live_booking':art.get('live_booking')})
    complete=all(r['status'] in {'supported','scope_unverified'} for r in needs)
    query={'record_ids':list(dict.fromkeys(rid for child in children for rid in (child.get('query_plan') or {}).get('record_ids',[]))),'requested_fields':[],'operation':'compound','method':'shared_request_plan_v2','clauses':children}
    for key in ('price_scope_request','r98_pending_context'):
        pending=[child['query_plan'][key] for child in children if isinstance(child.get('query_plan'),dict) and child['query_plan'].get(key) and child['status']=='needs_user_slot']
        if len(pending)==1:query[key]=pending[0]
    result=reader.finish(snap,started,'\n\n'.join(blocks),hits,query,obs,response='answer' if complete else 'partial_answer')
    art=dict(result.decision_artifact);art.update(request_plan=asdict(plan),need_results=needs,task_flow={'version':'r98','path':'shared_multi_need','executor':'common_domain_executors'})
    # finish may invalidate an in-flight snapshot. Never resurrect child facts.
    if art.get('response_type')=='retry':art['need_results']=[{**r,'status':'temporary_failure','receipts':[]} for r in needs]
    return replace(result,decision_artifact=art)
