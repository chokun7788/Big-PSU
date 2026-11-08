"""Compile all tasks, execute all local readers, then spend bounded fallback.

The old meaning wire and readers remain explicit adapters. New training and
the full R123 history/authority/compiler architecture are not implied here.
"""
import copy,re,time
from .contracts import RequestBudget
from .readers import blocked
from .scope import reference_time
from .plan_contract import compile_request,prepared_meaning
from .obligation_verifier import assess

def execute(engine,question,locale='auto',category=None,at=None,allow_llm=True,history=None,budget=None,understanding=None):
    from .request_provenance import capture,attach_compiled
    result=_execute(engine,question,locale,category,at,allow_llm,history,budget,understanding)
    attach_compiled(result['execution_contract'],capture(question,history))
    return result

def _execute(engine,question,locale='auto',category=None,at=None,allow_llm=True,history=None,budget=None,understanding=None):
    from .understanding import interpret
    from .context_guard import apply as guard_context
    from .meaning_reader import execution_query
    from .engine import language
    started=time.monotonic();at=reference_time(at);budget=budget or RequestBudget()
    if category is not None:
        result=engine._legacy_answer(question,locale,category,at,allow_llm,history,budget,understanding)
        result['execution_contract']={'version':'r123','path':'explicit_category_compatibility','whole_question_semantics_verified':False}
        return result
    proposal=understanding if understanding is not None else interpret(question,budget,allow_llm,index=engine.index)
    if not proposal.accepted:
        result=engine._legacy_answer(question,locale,category,at,allow_llm,history,budget,proposal)
        result['execution_contract']={'version':'r123','path':'unaccepted_wire_compatibility','reason':proposal.reason,'whole_question_semantics_verified':False}
        return result
    # The original proposal remains observable. Deterministic enrichments are
    # compiled after the existing review and are not attributed to the adapter.
    working=guard_context(question,engine.index,copy.deepcopy(proposal))
    snapshot={'release_id':engine.data.get('release_id'),'epoch':engine.data.get('epoch'),'reference_time':at.isoformat()}
    try:compiled=compile_request(question,working,engine.index,snapshot)
    except ValueError as exc:
        cat=next((t.category for t in working.tasks if t.category),'')
        p=blocked(cat,'invalid_compiled_plan','missing_input')
        result=engine._render_one(cat,question,locale,p,at);result.update(question=question,execution_query=question)
        return {'answer':result['answer'],'status':'missing_input','claims':[],'needs':[result],'model_events':budget.events,
            'understanding':working.as_dict(),'elapsed_sec':time.monotonic()-started,'fixture':False,'english_translation_missing':False,
            'selection_basis':'r123_invalid_plan','effective_locale':language(question,locale),'release_id':snapshot['release_id'],'epoch':snapshot['epoch'],
            'execution_contract':{'version':'r123','path':'invalid_compiled_plan','reason':str(exc),'whole_question_semantics_verified':False}}
    prepared=[];schedule=[]
    for task,meaning in zip(compiled.tasks,working.tasks):
        checked=prepared_meaning(meaning,task);part=meaning.quote
        material=[checked.target,*[c['quote'] for c in checked.constraints]]
        scoped=part+' '+' '.join(s for s in material if s and s not in part)
        scoped=execution_query(engine.index,scoped,checked)
        if task.errors:plan=blocked(task.category or '', 'invalid_compiled_scope','missing_input')
        elif task.capability['status']=='unsupported_operation' and not task.ambiguities:
            plan=blocked(task.category or '', 'unsupported_operation')
        elif task.category is None:plan=blocked('','domain_not_bound')
        else:plan=engine.plan(task.category,scoped,at,meaning=checked)
        prepared.append({'task':task,'meaning':checked,'question':scoped,'plan':plan})
        schedule.append({'phase':'typed_read_complete','task_id':task.id,'reason':plan.reason,'model_calls_used':budget.model_calls})
    # Every deterministic read has now finished, including later independent
    # tasks. Only scoped unresolved items may request evidence selection.
    pending=[]
    for item in prepared:
        p=item['plan'];task=item['task']
        if p.ambiguous and allow_llm and not p.locked:
            candidates=engine.scoped_candidates(task.category,item['question'],p,at)
            if candidates:pending.append((item,candidates))
    pending.sort(key=lambda x:(-len(x[0]['task'].obligations),x[0]['task'].id))
    for item,candidates in pending:
        plans,event=engine.selector.select([{'question':item['question'],'language':language(item['question'],locale),'facts':candidates}],budget)
        item['plan']=plans[0];item['plan'].category=item['task'].category
        schedule.append({'phase':'bounded_fallback','task_id':item['task'].id,'reason':item['plan'].reason,'model_calls_used':budget.model_calls})
    children=[];ledgers=[]
    for item in prepared:
        task=item['task'];p=item['plan'];q=item['question'];cat=task.category or ''
        if p.reason=='request_model_budget_exhausted':
            p.status='missing_source';p.metadata['execution_notice']={'th':'ยังตรวจส่วนนี้ไม่ครบภายในงบของคำขอนี้ ส่วนที่มีหลักฐานแล้วแสดงไว้แยกกัน','en':'This part could not be completed within the request budget. Supported parts are retained separately.'}
        elif p.reason=='unsupported_operation':
            p.metadata['execution_notice']={'th':'ตัวอ่านข้อมูลยังไม่รองรับวิธีประมวลผลที่คำถามนี้ต้องการ จึงยังยืนยันคำตอบส่วนนี้ไม่ได้','en':'The reader does not support the requested operation, so this part cannot be confirmed.'}
        if p.ambiguous and not allow_llm:
            p.status='missing_source';p.reason='typed_interpretation_unresolved';p.ambiguous=False
        p=engine.finish_plan(cat,q,p,at)
        result=engine._render_one(cat,q,locale,p,at)
        ledger=assess(engine.index,task,result,snapshot,q)
        if ledger['fatal']:
            p=blocked(cat,'source_receipt_verification_failed');result=engine._render_one(cat,q,locale,p,at)
        elif ledger['terminal_state']=='partial' and result['status']=='answer':
            result['status']='partial'
            notice='ตอบได้เฉพาะส่วนที่มีหลักฐาน ความครบตามรูปแบบที่ขอยังยืนยันไม่ได้' if language(q,locale)=='th' else 'The source-backed subset is shown; completeness for the requested operation is not established.'
            result['answer']=notice+'\n'+result['answer']
        result.update(question=item['meaning'].quote,execution_query=q,execution_contract=ledger)
        children.append(result);ledgers.append(ledger)
    def key(c):return c['fact_id'],c.get('numeric'),c['value']
    claims=list({key(c):c for child in children for c in child['claims']}.values())
    labels={key(c):i+1 for i,c in enumerate(claims)};blocks=[]
    for child in children:
        local={i+1:labels[key(c)] for i,c in enumerate(child['claims'])}
        blocks.append(re.sub(r'\[S(\d+)\]',lambda m:'[S'+str(local[int(m[1])])+']',child['answer']))
    states=[c['status'] for c in children]
    state=states[0] if len(set(states))==1 else 'partial' if claims else 'unavailable' if 'unavailable' in states else 'missing_source'
    return {'answer':'\n\n'.join(blocks),'status':state,'claims':claims,'needs':children,'model_events':budget.events,
        'understanding':working.as_dict(),'elapsed_sec':time.monotonic()-started,'fixture':any(c['fixture'] for c in children),
        'english_translation_missing':any(c['english_translation_missing'] for c in children),'selection_basis':'r123_typed_first_adapters',
        'effective_locale':language(question,locale),'release_id':engine.data.get('release_id'),'epoch':engine.data.get('epoch'),
        'execution_contract':{'version':'r123','path':'compiled_legacy_wire','request_plan':compiled.as_dict(),'tasks':ledgers,'schedule':schedule,
            'typed_reads_before_fallback':True,'whole_question_semantics_verified':False,'full_r123_architecture_implemented':False}}
