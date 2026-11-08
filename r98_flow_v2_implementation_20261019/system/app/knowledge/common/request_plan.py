"""Shared request/need boundary. Reads schema and identifiers, never legacy facts."""
from dataclasses import dataclass, asdict, replace
import re
from .query_contract import normalize, live_request, matches
from .registry import value

VERSION='common_request_plan_v2'

@dataclass
class Need:
    id: str
    task: str
    query: str
    source_span: str
    record_ids: list
    qualifiers: list
    slot_origin: str = 'current_user'

@dataclass
class RequestPlan:
    version: str
    question: str
    needs: list
    scope: dict

def task_of(question):
    from .query_scope import operation
    q=normalize(question)
    if live_request(q):return 'live_status'
    if re.search(r'ราคา|ค่าบริการ|กี่บาท|\b(?:prices?|cost|fees?|rates?|how much|budget)\b',q):return 'rental' if re.search(r'เหมา|ครึ่งวัน|เต็มวัน|\b(?:rental|half.day|full.day)\b',q) else 'price'
    if re.search(r'อยู่(?:ตรง|ที่)?ไหน|ที่อยู่|\b(?:where is|address|location)\b',q):return 'location'
    if re.search(r'กี่คน|\b(?:how many players|player count)\b',q):return 'players'
    if re.search(r'คือเกมอะไร|เป็นเกมอะไร|\b(?:what is|what kind of game|game overview)\b',q):return 'game_overview'
    if re.search(r'วิธีจอง|จอง(?:ยังไง|อย่างไร)|\b(?:how (?:do|can) i book|how to book|booking procedure)\b',q):return 'booking'
    return operation(q) or 'unresolved'

def _subjects(question,records,names):
    from .answer import named
    ids,_=named(question,{k:v for k,v in names.items() if k in records},allow_fuzzy=False)
    return [k for k in ids if records[k]['kind'] not in {'faq','policy','procedure','audience'}]

def split_needs(question,records,names):
    """Split explicit task coordination only; protect owner-entered full names."""
    q=normalize(question);spans=[]
    # Protect conjunctions in titles (e.g. a game named with 'and').
    for aliases in names.values():
        for alias in aliases:
            a=normalize(alias)
            if len(a)<4:continue
            for m in re.finditer(re.escape(a),q):spans.append(m.span())
    cuts=[m for m in re.finditer(r'\band\b|\balso\b|แล้ว(?:ก็)?|และ|[;\n]',q) if not any(a<=m.start()<b for a,b in spans)]
    if not 1<=len(cuts)<=3:return []
    parts=[];pos=0
    for cut in cuts:parts.append(q[pos:cut.start()].strip(' ?!.,'));pos=cut.end()
    parts.append(q[pos:].strip(' ?!.,'))
    if not all(parts):return []
    tasks=[task_of(part) for part in parts]
    # Do not split noun phrases or a condition joined to the same proposition.
    request_cues=r'ราคา|กี่บาท|คือเกมอะไร|เป็นเกมอะไร|ที่ไหน|อยู่ไหน|ยังไง|อย่างไร|มีอะไร|กี่คน|ว่างไหม|\b(?:what|where|how|can i|may i|is .*available|price|cost|fee|list|explain|describe|game overview)\b'
    if any(task=='unresolved' or not re.search(request_cues,part,re.I) for task,part in zip(tasks,parts)):return []
    if any(re.match(r'^(?:ถ้า|ยกเว้น|เฉพาะ|ก่อน|หลัง|if\b|unless\b|except\b|before\b|after\b)',part) for part in parts[1:]):return []
    # A single rulebook's compound clause must retain its original scope.
    if all(t=='rules' for t in tasks):return []
    first=_subjects(parts[0],records,names)
    result=[]
    for part,task in zip(parts,tasks):
        ids=_subjects(part,records,names);active=part
        if not ids and len(first)==1 and task in {'booking','price','live_status','controls','game_how_to_play'}:
            from .answer import title
            active=part+' '+title(records[first[0]],'en');ids=list(first)
        result.append({'query':active,'source_span':part,'task':task,'record_ids':ids})
    return result

def make_plan(question,records,names,history=None,*,split=True):
    clauses=split_needs(question,records,names) if split else []
    if not clauses:clauses=[{'query':question,'source_span':question,'task':task_of(question),'record_ids':_subjects(question,records,names)}]
    qualifiers=lambda q:[m.group() for m in re.finditer(r'\d+(?:[:./-]\d+)*|ไม่|ห้าม|ยกเว้น|เฉพาะ|ก่อน|หลัง|\b(?:not|no|without|except|unless|only|before|after)\b',q,re.I)]
    from .followup_scope import delivered_state
    prior=delivered_state(history)
    scope={'release_bound_at_read':True,'history_has_trusted_state':bool(prior),'candidate_source':'common_snapshot','all_requested':bool(re.search(r'ทั้งหมด|ทุกบริการ|ทุกเครื่อง|\b(?:all|every|everything)\b',normalize(question)))}
    needs=[Need('n'+str(i),r['task'],r['query'],r['source_span'],r['record_ids'],qualifiers(r['source_span']), 'delivered_state_selection' if prior and len(question.strip())<35 else 'current_user') for i,r in enumerate(clauses,1)]
    return RequestPlan(VERSION,question,needs,scope)

def attach(result,plan,snap=None):
    if result is None:return None
    art=dict(result.decision_artifact or {})
    if art.get('request_plan',{}).get('version')==VERSION:return result
    query=art.get('query_plan') or {};response=art.get('response_type','unconfirmed')
    errors=list(result.validation.errors)
    states={'answer':'supported','list':'supported','partial_answer':'partial_supported','clarification':'needs_user_slot','unconfirmed':'missing_source','not_current':'not_current','retry':'temporary_failure','withdrawn':'missing_source','live_unavailable':'live_unavailable'}
    if 'live_booking' in result.mode:
        status='live_unavailable' if 'unavailable' in result.mode else 'supported'
    else:status=states.get(response,'unsupported')
    obligations=art.get('obligations',[])
    if status=='needs_user_slot' and obligations and not any(o.get('status')=='needs_clarification' for o in obligations):
        status='conflict' if any(o.get('status')=='conflicted' for o in obligations) else 'missing_source'
    if errors:status='ambiguous_interpretation' if 'unresolved_query_clause' in errors else 'missing_source'
    if (query.get('entity_selection') or {}).get('availability_failure'):status='temporary_failure'
    rows=[]
    for need in plan.needs:
        receipts=[]
        for o in art.get('obligations',[]):
            if o.get('status')!='known' or not o.get('evidence_refs'):continue
            receipts.append({'record_id':o.get('record_id'),'field':o.get('field'),'evidence_refs':o['evidence_refs'],'release_id':art.get('release_id'),'claim_entailment_verified':False})
        rows.append({'need_id':need.id,'task':need.task,'source_span':need.source_span,'status':status,'reason_codes':errors,'record_ids':list(query.get('record_ids',[])),'receipts':receipts,'coverage_basis':'executed task and source obligations; semantic correctness not automatically verified'})
    art.update(request_plan=asdict(plan),need_results=rows)
    if snap:art['request_plan_snapshot']={'release_id':snap['active'],'epoch':snap['epoch']}
    return replace(result,decision_artifact=art)

def aggregate(reader,snap,started,plan,results,lang):
    """Each child retains its own subject, status and evidence; no fact inference."""
    blocks=[];hits=[];obs=[];needs=[];children=[]
    for need,result in zip(plan.needs,results):
        if result is None:
            text='ยังไม่มีข้อมูลยืนยันสำหรับส่วนนี้' if lang=='th' else 'No confirmed source is available for this part.'
            status='missing_source';rows=[];art={}
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
        needs.append({**row,'need_id':need.id,'task':need.task,'source_span':need.source_span})
        children.append({'need_id':need.id,'query':need.query,'clause':need.source_span,'need_status':'answered' if status=='supported' else status,'need_ledger':art.get('need_ledger'),'response_type':art.get('response_type'),'query_plan':art.get('query_plan'),'status':status,'live_booking':art.get('live_booking')})
    complete=all(r['status']=='supported' for r in needs)
    query={'record_ids':list(dict.fromkeys(rid for child in children for rid in (child.get('query_plan') or {}).get('record_ids',[]))),'requested_fields':[],'operation':'compound','method':'shared_request_plan_v2','clauses':children}
    for key in ('price_scope_request','r98_pending_context'):
        pending=[child['query_plan'][key] for child in children if isinstance(child.get('query_plan'),dict) and child['query_plan'].get(key) and child['status']=='needs_user_slot']
        if len(pending)==1:query[key]=pending[0]
    result=reader.finish(snap,started,'\n\n'.join(blocks),hits,query,obs,response='answer' if complete else 'partial_answer')
    art=dict(result.decision_artifact);art.update(request_plan=asdict(plan),need_results=needs,task_flow={'version':'r98','path':'shared_multi_need','executor':'common_domain_executors'})
    # finish may invalidate an in-flight snapshot. Never resurrect child facts.
    if art.get('response_type')=='retry':art['need_results']=[{**r,'status':'temporary_failure','receipts':[]} for r in needs]
    return replace(result,decision_artifact=art)
