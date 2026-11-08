"""Adapt domain claims to the existing chat/owner API contracts."""
import os,time
from dataclasses import asdict,replace
from .engine import Engine
from .routing import route,split_needs
from .contracts import RequestBudget
from .scope import norm,canonical_resource,requested_resources

TASKS={'C01':'record_detail','C02':'personnel','C03':'equipment','C04':'game_detail','C05':'game_controls','C06':'price','C07':'rental',
 'C08':'procedure','C09':'payment_policy','C10':'policy','C11':'schedule','C12':'live_status','C13':'competition_rules','C14':'news'}
PUBLIC={'answer':'answer','partial':'partial_answer','missing_source':'unconfirmed','missing_input':'clarification','not_current':'not_current','unavailable':'unavailable'}
NEED_STATES={'answer':'supported','partial':'partial_supported','missing_source':'missing_source','missing_input':'needs_user_slot','not_current':'not_current','unavailable':'temporary_failure'}

def answer(reader,question,*,locale='th',history=None,at=None,planner=None,_composing=False,_snapshot=None):
    if os.getenv('PSU_DOMAIN_FLOW_ENABLED','1')!='1':return None
    from app.calendar.service_calendar import now_bangkok
    from ..request_plan import VERSION,Need,RequestPlan
    from ..registry import value
    from .projection import title
    started=time.perf_counter();snap=_snapshot if _snapshot is not None else reader.store.snapshot()
    if not snap.get('release'):return None
    at=at or now_bangkok();engine=Engine.from_snapshot(snap,cache_key=reader.store.path.resolve());cat=route(engine.index,question)
    if cat is None:return None
    # Existing explicit topic-rejection and confirmation dialogue owns these
    # replies; do not reinterpret a short "no" as a factual new question.
    if history and len(norm(question))<12:return None
    records=engine.index.records;language='en' if locale=='en' else 'th'
    special=None
    if len(split_needs(question))==1 and cat=='C11':
        from ..open_day import status_question,answer as open_day
        from ..query_scope import calendar_ids
        if status_question(question):
            ids,day=calendar_ids(question,records,at)
            if day is not None:special=open_day(reader,snap,started,question,language,at,records)
        if special is None:
            from ..calendar_queries import answer as calendar_query
            special=calendar_query(reader,question,snap,records,language,at)
    if len(split_needs(question))==1 and cat=='C12':
        # Bind identifiers against current resources before any live reader.
        asked=requested_resources(question);resource_ids=[]
        for rid,r in records.items():
            if r['kind']!='resource':continue
            labels=list(title(r).values())+sum(r.get('aliases',{}).values(),[])
            if any(canonical_resource(x)==canonical_resource(s) for x in asked for s in labels):resource_ids.append(rid)
        if asked and not resource_ids:
            result=engine.answer(question,locale,category='C12',at=at,allow_llm=False)
            result['status']='missing_source';result['needs'][0]['status']='missing_source';result['needs'][0]['reason']='unknown_exact_resource'
            return package(reader,snap,started,question,result)
        from ..live_reader import answer as live_read
        need=Need('r114_live','live_status',question,question,resource_ids,[],predicate='live_availability')
        special=live_read(reader,need,snap,at,language)
        if special is None:
            result=engine.answer(question,locale,category='C12',at=at,allow_llm=False)
            result['status']='unavailable';result['needs'][0]['status']='unavailable';result['needs'][0]['reason']='live_binding_or_provider_not_confirmed'
            result['answer']='ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ' if language=='th' else 'No confirmed live binding is available, so occupancy cannot be checked.'
            return package(reader,snap,started,question,result)
    if special is not None:
        art={**(special.decision_artifact or {}),'domain_flow':{'version':'r114','category':cat,'path':'shared_calendar_or_live_contract'},
          'flow_contract':{'version':'r114','semantic_correctness_verified':False,'shared_typed_adapter':True}}
        return replace(special,decision_artifact=art)
    # Mature common readers retain tasks not projected into the replacement
    # yet (e.g. an existing FAQ with no declared category/profile). Explicit
    # scope guards remain terminal and cannot fall through to another record.
    result=engine.answer(question,locale,at=at,allow_llm=planner is not None,history=history)
    if not result['claims'] and all(n['reason'] in {'requested_facet_not_bound','entity_not_bound','domain_not_bound'} or n['plan']['metadata'].get('compatibility_allowed') for n in result['needs']):return None
    return package(reader,snap,started,question,result)

def package(reader,snap,started,question,result):
    from ..request_plan import VERSION,Need,RequestPlan
    needs=[];rows=[];hits=[];obs=[]
    allclaims=result['claims'];label_by_id={c['fact_id']:'S'+str(i+1) for i,c in enumerate(allclaims)}
    records=snap['release']['records'];sources=snap['release']['sources']
    for i,n in enumerate(result['needs'],1):
        ridlist=list(dict.fromkeys(c['record_id'] for c in n['claims']));task=TASKS.get(n['category'],'unresolved')
        needs.append(Need('r114_n'+str(i),task,n.get('question',question),n.get('question',question),ridlist,[],predicate=task))
        receipts=[]
        for c in n['claims']:
            r=records.get(c['record_id'],{});field='answer' if r.get('kind')=='faq' else 'amount_minor' if c['facet'] in {'amount','amount_thb'} else c['facet']
            receipts.append({'record_id':c['record_id'],'field':field,'status':'known','evidence_refs':c['evidence_refs']})
        rows.append({'need_id':'r114_n'+str(i),'task':task,'category':n['category'],'source_span':n.get('question',question),'status':NEED_STATES[n['status']],
          'reason_codes':[n['reason']],'receipts':receipts,'claim_packets':n['claims'],'semantic_correctness_verified':False})
        obs+=receipts
    for c in allclaims:
        for ref in c['evidence_refs']:
            source=sources.get(ref['source_id'])
            if source is None:raise ValueError('Domain claim source is outside pinned snapshot')
            hits.append({'id':c['fact_id']+':'+str(len(hits)),'record_id':c['record_id'],'field':c['facet'],'title':c['record_id'],
              'text':c['value'],'source_id':ref['source_id'],'snapshot_sha256':source['sha256'],'locator':ref['locator'],
              'citation_label':label_by_id[c['fact_id']],'source_url':source.get('public_url') or ''})
    plan={'record_ids':list(dict.fromkeys(c['record_id'] for c in allclaims)),'requested_fields':list(dict.fromkeys(o['field'] for o in obs)),
      'method':'r114_domain_readers','operation':'compound' if len(needs)>1 else 'domain','source_answer_confirmed':result['status']=='answer'}
    out=reader.finish(snap,started,result['answer'],hits,plan,obs,response=PUBLIC[result['status']])
    if out.decision_artifact.get('response_type')=='retry':
        allclaims=[]
        for row in rows:row.update(status='temporary_failure',receipts=[],claim_packets=[],reason_codes=['snapshot_changed_before_delivery'])
    art={**out.decision_artifact,'request_plan':asdict(RequestPlan(VERSION,question,needs,{'source':'current_pinned_snapshot','router':'r114'})),
      'need_results':rows,'domain_flow':{'version':'r114','categories':[n['category'] for n in result['needs']],'path':'domain_readers',
      'status':result['status'],'model_events':result['model_events'],'typed_claims':allclaims,'fixture':result['fixture'],
      'english_translation_missing':result['english_translation_missing']},'flow_contract':{'version':'r114','source_contract':'domain_scoped_facts','semantic_correctness_verified':False}}
    return replace(out,decision_artifact=art)
