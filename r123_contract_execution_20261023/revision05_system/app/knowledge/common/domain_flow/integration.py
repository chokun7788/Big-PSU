"""Adapt domain claims to the existing chat/owner API contracts."""
import os,time
from dataclasses import asdict,replace
from .engine import Engine,language as effective_language
from .routing import route,split_needs
from .contracts import RequestBudget
from .scope import norm,canonical_resource,requested_resources,contains

TASKS={'C01':'record_detail','C02':'personnel','C03':'equipment','C04':'game_detail','C05':'game_controls','C06':'price','C07':'rental',
 'C08':'procedure','C09':'payment_policy','C10':'policy','C11':'schedule','C12':'live_status','C13':'competition_rules','C14':'news'}
PUBLIC={'answer':'answer','partial':'partial_answer','missing_source':'unconfirmed','missing_input':'clarification','not_current':'not_current','unavailable':'unavailable'}
NEED_STATES={'answer':'supported','partial':'partial_supported','missing_source':'missing_source','missing_input':'needs_user_slot','not_current':'not_current','unavailable':'temporary_failure'}

def answer(reader,question,**kwargs):
    from ..flow_context import request_context
    with request_context() as ctx:
        if not ctx.input:ctx.input={'raw_question':question,'locale':kwargs.get('locale','th')}
        result=_answer(reader,question,**kwargs)
        if result is None:return None
        from .request_provenance import capture,attach_compiled
        from .native_contract import invalidate
        art=dict(result.decision_artifact or {})
        c=art.get('execution_contract') or {'version':'r123','path':'native_unaccepted_wire_compatibility','whole_question_semantics_verified':False}
        if 'request_context' not in c:attach_compiled(c,capture((c.get('request_plan') or {}).get('question',question),kwargs.get('history')))
        if art.get('response_type')=='retry':
            c=invalidate(c);art['obligations']=[]
            art['need_results']=[{**row,'status':'temporary_failure','receipts':[],'claim_packets':[],
                'coverage':{**row.get('coverage',{}),'receipts':[]},
                'execution_contract':invalidate({'tasks':[row['execution_contract']]})['tasks'][0] if row.get('execution_contract') else {}}
                for row in art.get('need_results',[])]
        art['execution_contract']=c
        return replace(result,decision_artifact=art)


def _answer(reader,question,*,locale='th',history=None,at=None,planner=None,_composing=False,_snapshot=None,_budget=None,_understanding=None):
    if os.getenv('PSU_DOMAIN_FLOW_ENABLED','1')!='1':return None
    from app.calendar.service_calendar import now_bangkok
    from ..request_plan import VERSION,Need,RequestPlan
    from ..registry import value
    from .projection import title
    started=time.perf_counter();snap=_snapshot if _snapshot is not None else reader.store.snapshot()
    if not snap.get('release'):return None
    at=at or now_bangkok();engine=Engine.from_snapshot(snap,cache_key=reader.store.path.resolve())
    from .financial import resume_financial
    resumed=resume_financial(question,history,engine.index.records) if history else None
    if resumed:
        from .request_provenance import derived_input
        from ..followup_scope import delivered_state
        pending=(delivered_state(history) or {}).get('r114_pending',{})
        origin=pending.get('query','')
        derived_input(resumed,'delivered_financial_resume',[
            {'origin':'delivered_pending_query','start':0,'end':len(origin),'text':origin},
            {'origin':'current_user_reply','start':len(origin)+1,'end':len(origin)+1+len(question),'text':question},
            *([{'origin':'native_billing_period_rule','text':'per session'}] if resumed!=origin+' '+question else [])],
            source_state_slot=pending.get('slot'),facts_inherited=False)
        question=resumed
    # Existing explicit topic-rejection and confirmation dialogue owns these
    # replies; do not reinterpret a short "no" as a factual new question.
    if history and len(norm(question))<12:return None
    from .understanding import interpret
    budget=_budget or RequestBudget()
    interpretation_question=question
    if not _composing and not resumed:
        # explicit_request_focus may strip an introduction containing the game,
        # event or audience. Retain that current-turn context for interpretation.
        from ..flow_context import CURRENT
        context=CURRENT.get();original=(context.input if context is not None else {}).get('normalized_question')
        if isinstance(original,str) and original and len(original)<=4000:interpretation_question=original
    understanding=_understanding if _understanding is not None else interpret(interpretation_question,budget,allow_llm=planner is not None,index=engine.index)
    if not hasattr(reader,'understanding_audits'):reader.understanding_audits=[]
    reader.understanding_audits.append(understanding.as_dict())
    compiled=None
    if understanding.accepted:
        question=interpretation_question
        from .native_contract import prepare
        try:understanding,compiled=prepare(question,understanding,engine,at)
        except ValueError:
            # The engine owns the bounded invalid-plan response. Never send a
            # malformed accepted plan to an unguarded provider adapter.
            return package(reader,snap,started,question,engine.answer(question,locale,at=at,allow_llm=False,budget=budget,understanding=understanding))
    parts=[t.quote for t in understanding.tasks] if understanding.accepted else split_needs(question,engine.index)
    categories=[t.category for t in understanding.tasks] if understanding.accepted else [route(engine.index,p) for p in parts]
    cat=next((c for c in categories if c is not None),None)
    if cat is None:return None
    records=engine.index.records;language=effective_language(question,locale)
    # Calendar and live observations must keep their typed adapters even when
    # combined with another domain. All children share the pinned snapshot,
    # request-local provider cache and one selector budget.
    if not _composing and len(parts)>1 and any(c in {'C11','C12'} for c in categories):
        from ..request_plan import aggregate
        needs=[];outputs=[]
        for i,part in enumerate(parts,1):
            child_q=part;child_understanding=understanding.child(i-1) if understanding.accepted else understanding
            if compiled is not None:
                from .native_contract import scoped_question
                from .request_provenance import derived_input
                from .understanding import Understanding
                task=compiled.tasks[i-1]
                if task.errors or task.ambiguities or task.capability['status']=='unsupported_operation':
                    # Native special paths must not bypass the compiler's
                    # missing-input/capability gate.
                    from .readers import blocked
                    reason='unsupported_operation' if task.capability['status']=='unsupported_operation' else 'invalid_compiled_scope'
                    p=blocked(task.category or '',reason,'missing_source' if reason=='unsupported_operation' else 'missing_input')
                    n=engine._render_one(task.category or '',part,locale,p,at);n.update(question=part,execution_query=part)
                    from .obligation_verifier import assess
                    ledger=assess(engine.index,task,n,compiled.snapshot,part);n['execution_contract']=ledger
                    child=package(reader,snap,started,part,{'answer':n['answer'],'status':n['status'],'claims':[],
                        'needs':[n],'model_events':budget.events,'understanding':understanding.as_dict(),'fixture':False,
                        'english_translation_missing':False,'execution_contract':{'version':'r123','path':'native_preflight_blocked',
                        'tasks':[ledger],'whole_question_semantics_verified':False}})
                else:
                    child_q=scoped_question(understanding.tasks[i-1]).strip()
                    child_understanding=Understanding([replace(understanding.tasks[i-1],quote=child_q)],True,'compiled_parent_scope',
                        {**understanding.event,'derived_from_parent_task':task.id})
                    derived_input(child_q,'compiled_parent_task',[
                        {'origin':'current_question_task','source_span':asdict(task.source_span)},
                        *[{'origin':'explicit_shared_binding','binding':asdict(b)} for b in task.bindings]],parent_question=question)
                    child=answer(reader,child_q,locale=locale,history=None,at=at,planner=planner,_composing=True,_snapshot=snap,_budget=budget,_understanding=child_understanding)
            else:
                child=answer(reader,child_q,locale=locale,history=history,at=at,planner=planner,_composing=True,_snapshot=snap,_budget=budget,_understanding=child_understanding)
            task=TASKS.get(categories[i-1],'unresolved');ids=[]
            if child is not None:
                old=(child.decision_artifact.get('request_plan') or {}).get('needs',[])
                if len(old)==1:task=old[0]['task'];ids=old[0]['record_ids']
            needs.append(Need('r114_part'+str(i),task,part,part,ids,[],predicate=task));outputs.append(child)
        composed=aggregate(reader,snap,started,RequestPlan(VERSION,question,needs,{'router':'r114','pinned_snapshot':True}),outputs,language)
        art={**composed.decision_artifact,'domain_flow':{'version':'r114','path':'shared_native_multi_need',
            'categories':categories,'model_events':budget.events,'single_snapshot':True,'single_request_budget':True},'understanding':understanding.as_dict()}
        if compiled is not None:
            from .native_contract import aggregate_contract
            art['execution_contract']=aggregate_contract(compiled,outputs)
            art['need_results']=[{**row,'execution_contract':ledger} for row,ledger in zip(art.get('need_results',[]),art['execution_contract']['tasks'])]
        if art.get('response_type')=='retry':
            art['query_plan']={'method':'r114_snapshot_changed','record_ids':[],'requested_fields':[]}
            art['need_results']=[{**r,'receipts':[],'claim_packets':[],'coverage':{},'status':'temporary_failure'} for r in art.get('need_results',[])]
            art['obligations']=[]
        return replace(composed,decision_artifact=art)
    if compiled is not None and len(parts)==1:
        task=compiled.tasks[0]
        if task.errors or task.ambiguities or task.capability['status']=='unsupported_operation':
            return package(reader,snap,started,question,engine.answer(question,locale,at=at,allow_llm=False,budget=budget,understanding=understanding))
    special=None
    if len(parts)==1 and cat=='C11':
        # A recorded weekday period must not be replaced by a broad old FAQ
        # when the typed schedule's zone/effective scope is unknown.
        recorded=engine.plan('C11',question,at,meaning=understanding.tasks[0] if understanding.accepted else None)
        if recorded.ids and (recorded.reason=='recorded_play_service_calendar' or all(engine.index.byid[f]['facet'] in {'bookable_periods','maintenance_periods'} for f in recorded.ids)):
            result=engine.answer(question,locale,at=at,allow_llm=False,budget=budget,understanding=understanding)
            return package(reader,snap,started,question,result)
        from ..open_day import status_question,answer as open_day
        from ..query_scope import calendar_ids
        if status_question(question):
            ids,day=calendar_ids(question,records,at)
            if day is not None:special=open_day(reader,snap,started,question,language,at,records)
        if special is None:
            from ..calendar_queries import answer as calendar_query
            special=calendar_query(reader,question,snap,records,language,at)
    if len(parts)==1 and cat=='C12':
        guard_plan=engine.plan('C12',question,at)
        if guard_plan.locked and guard_plan.reason=='booking_reference_unconfirmed':
            return package(reader,snap,started,question,engine.answer(question,locale,at=at,allow_llm=False,budget=budget,understanding=understanding))
        # Bind identifiers against current resources before any live reader.
        asked=requested_resources(question);resource_ids=[]
        for rid,r in records.items():
            if r['kind']!='resource':continue
            labels=list(title(r).values())+sum(r.get('aliases',{}).values(),[])
            if any(canonical_resource(x)==canonical_resource(s) for x in asked for s in labels):resource_ids.append(rid)
        if asked and not resource_ids:
            result=engine.answer(question,locale,at=at,allow_llm=False,budget=budget,understanding=understanding)
            result['status']='missing_source';result['needs'][0]['status']='missing_source';result['needs'][0]['reason']='unknown_exact_resource'
            from .native_contract import guard_contract
            guard_contract(result,compiled,'missing_source','unknown_exact_resource')
            return package(reader,snap,started,question,result)
        from ..live_reader import answer as live_read
        roots=list(resource_ids)
        if not asked:
            for rid,r in records.items():
                if r['kind'] not in {'service','zone','game','resource'}:continue
                labels=list(title(r).values())+sum(r.get('aliases',{}).values(),[])
                if r['kind']=='service' and value(r,'platform'):labels.append(value(r,'platform'))
                if any(contains(question,s) for s in labels):roots.append(rid)
        need=Need('r114_live','live_status',question,question,list(dict.fromkeys(roots)),[],predicate='live_availability')
        special=live_read(reader,need,snap,at,language)
        if special is None:
            result=engine.answer(question,locale,at=at,allow_llm=False,budget=budget,understanding=understanding)
            result['status']='unavailable';result['needs'][0]['status']='unavailable';result['needs'][0]['reason']='live_binding_or_provider_not_confirmed'
            from .native_contract import guard_contract
            guard_contract(result,compiled,'missing_source','live_binding_not_confirmed_no_provider_read')
            result['answer']='ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ' if language=='th' else 'No confirmed live binding is available, so occupancy cannot be checked.'
            return package(reader,snap,started,question,result)
    if special is not None:
        from ..request_plan import attach
        if cat=='C11':
            ids=(special.decision_artifact.get('query_plan') or {}).get('record_ids',[])
            need=Need('r114_calendar','schedule',question,question,ids,[],predicate='schedule')
        special=attach(special,RequestPlan(VERSION,question,[need],{'source':'current_pinned_snapshot','router':'r114'}),snap)
        live=special.decision_artifact.get('live_booking',{});observations=live.get('observations',[])
        if cat=='C12' and special.validation.ok and observations and all(o.get('status')=='supported' and o.get('freshness_checked') for o in observations):
            special=replace(special,decision_artifact={**special.decision_artifact,'need_results':[
                {**r,'status':'supported','reason_codes':['native_binding_date_window_mapping_and_freshness_checked'],
                 'live_observations':observations,'semantic_correctness_verified':False} for r in special.decision_artifact.get('need_results',[])]})
        art={**(special.decision_artifact or {}),'domain_flow':{'version':'r114','category':cat,'path':'shared_calendar_or_live_contract'},
          'flow_contract':{'version':'r114','semantic_correctness_verified':False,'shared_typed_adapter':True},'understanding':understanding.as_dict()}
        special=replace(special,decision_artifact=art)
        if compiled is not None:
            from .native_contract import attach_native
            special=attach_native(reader,special,snap,compiled,at,language)
        return special
    # Mature common readers retain tasks not projected into the replacement
    # yet (e.g. an existing FAQ with no declared category/profile). Explicit
    # scope guards remain terminal and cannot fall through to another record.
    result=engine.answer(question,locale,at=at,allow_llm=planner is not None,history=history,budget=budget,understanding=understanding)
    if cat=='C14' and not result['claims']:
        # All current news records are projected. An unbound event must not
        # fall through to general contact info or another tournament's rules.
        return package(reader,snap,started,question,result)
    if not result['claims'] and not understanding.accepted and all(n['reason'] in {'requested_facet_not_bound','entity_not_bound','domain_not_bound'} or n['plan']['metadata'].get('compatibility_allowed') for n in result['needs']):return None
    return package(reader,snap,started,question,result)

def package(reader,snap,started,question,result):
    from ..request_plan import VERSION,Need,RequestPlan
    needs=[];rows=[];hits=[];obs=[]
    allclaims=result['claims'];label_by_id={(c['fact_id'],c.get('numeric'),c['value']):'S'+str(i+1) for i,c in enumerate(allclaims)}
    records=snap['release']['records'];sources=snap['release']['sources']
    for i,n in enumerate(result['needs'],1):
        ridlist=list(dict.fromkeys(c['record_id'] for c in n['claims']));task=TASKS.get(n['category'],'unresolved')
        needs.append(Need('r114_n'+str(i),task,n.get('question',question),n.get('question',question),ridlist,[],predicate=task))
        receipts=[]
        for c in n['claims']:
            r=records.get(c['record_id'],{});field='answer' if r.get('kind')=='faq' else 'amount_minor' if c['facet'] in {'amount','amount_thb'} else c['facet']
            receipts.append({'record_id':c['record_id'],'field':field,'status':'known','evidence_refs':c['evidence_refs']})
        rows.append({'need_id':'r114_n'+str(i),'task':task,'category':n['category'],'source_span':n.get('question',question),'execution_query':n.get('execution_query'),'status':NEED_STATES[n['status']],
          'reason_codes':[n['reason']],'receipts':receipts,'claim_packets':n['claims'],'execution_contract':n.get('execution_contract',{}),'semantic_correctness_verified':False})
        obs+=receipts
    for c in allclaims:
        for ref in c['evidence_refs']:
            source=sources.get(ref['source_id'])
            if source is None:raise ValueError('Domain claim source is outside pinned snapshot')
            hits.append({'id':c['fact_id']+':'+str(len(hits)),'record_id':c['record_id'],'field':c['facet'],'title':c['record_id'],
              'text':c['value'],'source_id':ref['source_id'],'snapshot_sha256':source['sha256'],'locator':ref['locator'],
              'citation_label':label_by_id[(c['fact_id'],c.get('numeric'),c['value'])],'source_url':source.get('public_url') or ''})
    plan={'record_ids':list(dict.fromkeys(c['record_id'] for c in allclaims)),'requested_fields':list(dict.fromkeys(o['field'] for o in obs)),
      'method':'r114_domain_readers','operation':'compound' if len(needs)>1 else 'domain','source_answer_confirmed':result['status']=='answer'}
    if len(result['needs'])==1 and result['status']=='missing_input' and result['needs'][0]['category'] in {'C06','C07'}:
        from .projection import title,value
        roots=[rid for rid,r in records.items() if r['kind'] in {'service','zone'} and any(contains(question,s) for s in [*title(r).values(),*sum(r.get('aliases',{}).values(),[]),*([value(r,'platform')] if r['kind']=='service' and value(r,'platform') else [])])]
        missing=result['needs'][0]['plan']['metadata'].get('missing_slots',[])
        plan['r114_pending']={'version':1,'category':result['needs'][0]['category'],'query':question,'root_ids':roots,'slot':missing[0] if missing else None,'facts_in_state':False}
    out=reader.finish(snap,started,result['answer'],hits,plan,obs,response=PUBLIC[result['status']])
    if out.decision_artifact.get('response_type')=='retry':
        allclaims=[]
        for row in rows:row.update(status='temporary_failure',receipts=[],claim_packets=[],reason_codes=['snapshot_changed_before_delivery'])
    art={**out.decision_artifact,'request_plan':asdict(RequestPlan(VERSION,question,needs,{'source':'current_pinned_snapshot','router':'r114'})),
      'need_results':rows,'understanding':result.get('understanding',{}),'execution_contract':result.get('execution_contract',{}),'domain_flow':{'version':'r114','categories':[n['category'] for n in result['needs']],'path':'domain_readers',
      'status':result['status'],'model_events':result['model_events'],'typed_claims':allclaims,'fixture':result['fixture'],
      'english_translation_missing':result['english_translation_missing']},'flow_contract':{'version':'r114','source_contract':'domain_scoped_facts','semantic_correctness_verified':False}}
    return replace(out,decision_artifact=art)
