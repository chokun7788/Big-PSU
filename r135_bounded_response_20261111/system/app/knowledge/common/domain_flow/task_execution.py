"""Compile scoped task graphs, finish typed reads, then spend shared fallback.

Wire compatibility and whole-question semantic accuracy remain distinct from
the implemented compiler. Weight provenance is recorded by ModelGateway.
"""
import copy,re,time
from .contracts import RequestBudget
from .readers import blocked
from .scope import reference_time
from .plan_contract import compile_request,prepared_meaning
from .obligation_verifier import assess,withhold_delivery
from .policy_scope import contradicts_customer_actor

def compatibility_contract(engine,question,result,path,at,reason=None,locale='auto'):
    """Audit bounded fallback without inventing a validated requested operator."""
    from .plan_contract import CompiledTask,Span,Obligation,CompiledRequest,span
    from .result_contract import package
    from .terminal_states import aggregate
    snapshot={'release_id':engine.data.get('release_id'),'epoch':engine.data.get('epoch'),'reference_time':at.isoformat()}
    tasks=[];ledgers=[];executors=[]
    for i,child in enumerate(result.get('needs',[]),1):
        quoted=child.get('question') or question;source=span(question,quoted) or Span(0,len(question),question)
        task=CompiledTask('t'+str(i),source,child.get('category'),'bounded_compatibility','',{'operation':'bounded_compatibility','semantic_operation':'bounded_compatibility','status':'compatibility_limited','requested_operation_verified':False})
        task.obligations=[Obligation(task.id+':scope','compatibility_operation_scope',task.id,'requires_independent_operation_review')]
        ledger=assess(engine.index,task,child,snapshot,child.get('execution_query') or quoted)
        ledger['compatibility_limits_explicit']=True
        if ledger['fatal']:
            child=engine._render_one(child.get('category') or '',quoted,locale,blocked(child.get('category') or '','source_receipt_verification_failed'),at)
            ledger=withhold_delivery(ledger,'source_receipt_verification_failed','invalid_plan')
        child['execution_contract']=ledger;child['executor_result']=package(task,ledger,child,snapshot)
        result['needs'][i-1]=child;tasks.append(task);ledgers.append(ledger);executors.append(child['executor_result'])
    plan=CompiledRequest(question,snapshot,tasks,wire_adapter='bounded_compatibility_no_validated_operation')
    result['execution_contract']={'version':'r135','path':path,'reason':reason,'request_plan':plan.as_dict(),'tasks':ledgers,'executor_results':executors,'compatibility_limits_explicit':True,'whole_question_semantics_verified':False}
    def key(c):return c['fact_id'],c.get('numeric'),c['value']
    result['claims']=list({key(c):c for child in result.get('needs',[]) for c in child.get('claims',[])}.values())
    labels={key(c):i+1 for i,c in enumerate(result['claims'])};blocks=[]
    for child in result.get('needs',[]):
        local={i+1:labels[key(c)] for i,c in enumerate(child.get('claims',[]))}
        blocks.append(re.sub(r'\[S(\d+)\]',lambda m:'[S'+str(local[int(m[1])])+']',child['answer']))
    result['answer']='\n\n'.join(blocks)
    result['terminal_state']=aggregate((l['terminal_state'] for l in ledgers),bool(result['claims']))
    result['status']={'supported':'answer','partial':'partial','conflict':'partial','budget_exhausted':'partial','missing_input':'missing_input','not_current':'not_current','model_unavailable':'unavailable','provider_unavailable':'unavailable'}.get(result['terminal_state'],'missing_source')
    return result

def execute(engine,question,locale='auto',category=None,at=None,allow_llm=True,history=None,budget=None,understanding=None):
    from ..flow_context import request_context
    from .engine import language
    with request_context() as ctx:
        if not ctx.input:ctx.input={'raw_question':question,'requested_locale':locale,'effective_locale':language(question,locale)}
        at=ctx.pin_reference_time(at)
        if not ctx.snapshot or any(ctx.snapshot.get(k)!=engine.data.get(k) for k in ['release_id','epoch']):ctx.bind_snapshot(engine.data)
        from .input_derivation import check
        proof=check(question)
        if not proof['verified']:return input_rejection(engine,question,locale,at,proof)
        return _execute_with_context(engine,question,locale,category,at,allow_llm,history,budget,understanding)

def input_rejection(engine,question,locale,at,proof):
    from .engine import language
    from .routing import route
    cat=route(engine.index,question) or 'C01'
    need=engine._render_one(cat,question,locale,blocked(cat,'invalid_compiled_input_derivation'),at)
    need['answer']='ยังยืนยันการตีความคำถามนี้ไม่ได้ กรุณาระบุคำถามอีกครั้งครับ' if language(question,locale)=='th' else 'The request interpretation could not be verified. Please restate the question.'
    need.update(question=question,execution_query=question)
    result={'answer':need['answer'],'status':'missing_source','claims':[],'needs':[need],'model_events':[],'understanding':{},'fixture':False,'english_translation_missing':False,'release_id':engine.data.get('release_id'),'epoch':engine.data.get('epoch'),'effective_locale':language(question,locale),'selection_basis':'input_derivation_guard'}
    result=compatibility_contract(engine,question,result,'input_derivation_guard',at,'invalid_compiled_input_derivation',locale)
    from .request_provenance import capture,attach_compiled
    result['execution_contract']['input_derivation_validation']=proof;attach_compiled(result['execution_contract'],capture(question))
    return result

def _cancel_procedure_receipt_matches(record,receipt,claims):
    """Require receipt references to the actual typed fields and delivered fact."""
    fields=record.get('fields',{});rid=record.get('id') or receipt.get('record_id')
    refs=receipt.get('evidence_refs',[])
    def bound(field):
        expected=fields.get(field,{}).get('evidence_refs',[])
        return bool(expected and any(ref in refs for ref in expected))
    scope=receipt.get('requested_scope',{})
    action=scope.get('policy_action',{})
    return (receipt.get('record_id')==rid and receipt.get('record_revision')==record.get('revision')
            and receipt.get('value_validation')=='exact_source_value' and bound('steps') and bound('topic')
            and scope.get('verified') is True and action.get('verified') is True
            and 'customer_cancel' in action.get('requested_actions',[]) and 'customer_cancel' in action.get('source_actions',[])
            and any(c.get('record_id')==rid and c.get('fact_id')==receipt.get('fact_id') for c in claims))

def _execute_with_context(engine,question,locale='auto',category=None,at=None,allow_llm=True,history=None,budget=None,understanding=None):
    from .request_provenance import capture,attach_compiled
    result=_execute(engine,question,locale,category,at,allow_llm,history,budget,understanding)
    attach_compiled(result['execution_contract'],capture(question,history))
    # A cancellation deadline does not establish the requested procedure.
    # Only a delivered, source-verified typed procedure with an explicit general
    # cancellation topic and no unresolved conditions can satisfy this guard.
    how_cancel = re.search(r'(?:วิธี|ขั้นตอน|อย่างไร|ยังไง).{0,40}ยกเลิก.{0,30}จอง|ยกเลิก.{0,30}จอง.{0,30}(?:อย่างไร|ยังไง|วิธี)|\bhow\s+(?:do|can|to).{0,35}cancel.{0,25}(?:booking|reservation)',question,re.I)
    if how_cancel and not re.search(r'เปลี่ยน|แก้ไข|ผิดเครื่อง|change|edit|wrong',question,re.I):
        contract=result['execution_contract']; valid=[]
        for task in contract.get('tasks',[]):
            if task.get('fatal'):continue
            for receipt in task.get('receipts',[]):
                rid=receipt.get('record_id');record=engine.index.records.get(rid,{})
                fields=record.get('fields',{});topic=fields.get('topic',{});pre=fields.get('preconditions',{});steps=fields.get('steps',{})
                refs=receipt.get('evidence_refs',[])
                if (record.get('kind')=='procedure' and topic.get('status')=='known' and topic.get('value') in {'cancel_booking','cancel_reservation','booking_cancellation'} and pre.get('status') in {'known','not_applicable'} and not pre.get('value') and steps.get('status')=='known' and steps.get('value') and not contradicts_customer_actor(steps.get('value')) and _cancel_procedure_receipt_matches(record,receipt,result.get('claims',[]))):valid.append(rid)
        contract.setdefault('additional_obligations',[]).append({'kind':'cancellation_procedure','fulfilled':bool(valid),'claim_record_ids':valid,'reason':None if valid else 'action_specific_procedure_not_independently_verified'})
        if not valid:
            if result.get('terminal_state') in {'supported','partial'}:result['terminal_state']='partial';result['status']='partial';contract['terminal_state']='partial'
            from .engine import language
            notice=('ขั้นตอนการยกเลิกการจองยังไม่ยืนยันจากข้อมูลที่ตรวจสอบครับ' if language(question,locale)=='th' else 'The cancellation procedure is not confirmed from the checked information.')
            result['answer']=notice+'\n\n'+result['answer']
    from .request_verifier import verify
    verified=verify(engine.index,question,result['execution_contract'],result.get('answer',''),result.get('needs',[]))
    result['execution_contract']['verifier_result']=verified
    from .request_verifier import attach_constraint_obligations
    attach_constraint_obligations(result['execution_contract'],verified)
    if verified['requires_partial_delivery'] and result.get('terminal_state') in {'supported','partial'}:
        result['terminal_state']='partial' if result.get('claims') else 'missing_source'
        result['status']='partial' if result.get('claims') else 'missing_source'
        result['execution_contract']['terminal_state']=result['terminal_state']
        from .request_verifier import delivery_notice
        from .engine import language
        result['answer']+='\n\n'+delivery_notice(verified,language(question,locale))
    return result

def _execute(engine,question,locale='auto',category=None,at=None,allow_llm=True,history=None,budget=None,understanding=None):
    from .understanding import interpret
    from .context_guard import apply as guard_context
    from .meaning_reader import execution_query
    from .engine import language
    started=time.monotonic();at=reference_time(at);budget=budget or RequestBudget()
    if category is not None:
        result=engine._legacy_answer(question,locale,category,at,allow_llm,history,budget,understanding)
        return compatibility_contract(engine,question,result,'explicit_category_compatibility',at,locale=locale)
    proposal=understanding if understanding is not None else interpret(question,budget,allow_llm,index=engine.index)
    if not proposal.accepted:
        result=engine._legacy_answer(question,locale,category,at,allow_llm,history,budget,proposal)
        return compatibility_contract(engine,question,result,'unaccepted_wire_compatibility',at,proposal.reason,locale)
    # The original proposal remains observable. Deterministic enrichments are
    # compiled after the existing review and are not attributed to the adapter.
    from .request_verifier import supplement
    working=guard_context(question,engine.index,supplement(engine.index,question,proposal))
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
    def read_plan(task,checked,scoped):
        if any(b.validation_outcome=='source_relation_missing' for b in task.bindings):return blocked(task.category or '', 'shared_service_game_offering_not_confirmed')
        if task.errors:return blocked(task.category or '', 'invalid_compiled_scope','missing_input')
        if task.capability['status']=='unsupported_operation' and not task.ambiguities:return blocked(task.category or '', 'unsupported_operation')
        if task.category is None:return blocked('','domain_not_bound')
        from .capabilities import dispatch
        return dispatch(engine,task,checked,scoped,at)
    for task,meaning in zip(compiled.tasks,working.tasks):
        checked=prepared_meaning(meaning,task);part=meaning.quote
        material=[checked.target,*[c['quote'] for c in checked.constraints]]
        scoped=part+' '+' '.join(s for s in material if s and s not in part)
        scoped=execution_query(engine.index,scoped,checked)
        plan=blocked(task.category or '', 'awaiting_execution_prerequisite','missing_input') if task.execution_dependencies else read_plan(task,checked,scoped)
        prepared.append({'task':task,'meaning':checked,'question':scoped,'plan':plan})
        schedule.append({'phase':'execution_dependency_deferred' if task.execution_dependencies else 'typed_read_complete','task_id':task.id,'reason':plan.reason,'model_calls_used':budget.model_calls})
    # Every ready independent deterministic read has finished. Dependent reads
    # remain deferred until a source-verified prerequisite outcome is known.
    pending=[]
    for item in prepared:
        p=item['plan'];task=item['task']
        if p.ambiguous and allow_llm and not p.locked:
            candidates=engine.scoped_candidates(task.category,item['question'],p,at)
            if candidates:pending.append((item,candidates))
    pending.sort(key=lambda x:(-len(x[0]['task'].obligations),x[0]['task'].id))
    for item,candidates in pending:
        from ..bounded_time import exhausted
        if exhausted():
            item['plan']=blocked(item['task'].category or '', 'analysis_time_budget_exhausted','unavailable')
            item['plan'].metadata['context_clarification']={'th':'ส่วนนี้วิเคราะห์ไม่ทันเวลาที่กำหนด กรุณาระบุรายละเอียดเพิ่มเติมหรือลองใหม่','en':'This part exceeded the analysis time budget; please clarify or retry.'}
            schedule.append({'phase':'analysis_budget_exhausted','task_id':item['task'].id,'verified_siblings_retained':True})
            continue
        plans,event=engine.selector.select([{'question':item['question'],'language':language(item['question'],locale),'facts':candidates}],budget)
        item['plan']=plans[0];item['plan'].category=item['task'].category
        schedule.append({'phase':'bounded_fallback','task_id':item['task'].id,'reason':item['plan'].reason,'model_calls_used':budget.model_calls})
    children=[];ledgers=[]
    for item in prepared:
        task=item['task'];p=item['plan'];q=item['question'];cat=task.category or ''
        dependency=None
        if task.execution_dependencies:
            from .execution_dependencies import evaluate,notice,blocked_reason
            dependency=evaluate(engine.index,question,compiled.tasks,task.id,[c['executor_result'] for c in children],snapshot)
            schedule.append({'phase':'execution_dependency_evaluated','task_id':task.id,'outcome':dependency['outcome'],'reason':dependency['reason'],'source_task_id':dependency.get('edge',{}).get('source_task_id'),'model_calls_used':budget.model_calls})
            if dependency['outcome']=='true':
                p=read_plan(task,item['meaning'],q)
                schedule.append({'phase':'dependent_typed_read_complete','task_id':task.id,'reason':p.reason,'model_calls_used':budget.model_calls})
                if p.ambiguous and allow_llm and not p.locked:
                    candidates=engine.scoped_candidates(cat,q,p,at)
                    if candidates:
                        plans,event=engine.selector.select([{'question':q,'language':language(q,locale),'facts':candidates}],budget);p=plans[0];p.category=task.category
                        schedule.append({'phase':'dependent_bounded_fallback','task_id':task.id,'reason':p.reason,'model_calls_used':budget.model_calls})
            else:
                reason=blocked_reason(dependency);p=blocked(cat,reason,'missing_source' if reason=='unsupported_operation' else 'missing_input')
                p.metadata['execution_notice']={l:notice(dependency,l) for l in ['th','en']}
        if p.reason=='request_model_budget_exhausted':
            p.status='missing_source';p.metadata['execution_notice']={'th':'ยังตรวจส่วนนี้ไม่ครบภายในงบของคำขอนี้ ส่วนที่มีหลักฐานแล้วแสดงไว้แยกกัน','en':'This part could not be completed within the request budget. Supported parts are retained separately.'}
        elif p.reason=='unsupported_operation':
            p.metadata.setdefault('execution_notice',{'th':'ตัวอ่านข้อมูลยังไม่รองรับวิธีประมวลผลที่คำถามนี้ต้องการ จึงยังยืนยันคำตอบส่วนนี้ไม่ได้','en':'The reader does not support the requested operation, so this part cannot be confirmed.'})
        if p.ambiguous and not allow_llm:
            p.status='missing_source';p.reason='typed_interpretation_unresolved';p.ambiguous=False
        p=engine.finish_plan(cat,q,p,at)
        result=engine._render_one(cat,q,locale,p,at)
        ledger=assess(engine.index,task,result,snapshot,q)
        if ledger['fatal']:
            p=blocked(cat,'source_receipt_verification_failed');result=engine._render_one(cat,q,locale,p,at)
            ledger=withhold_delivery(ledger,'source_receipt_verification_failed','invalid_plan')
        elif result['claims'] and any(reason in ledger['reason_codes'] for reason in ['requested_field_not_delivered','substantive_clause_not_delivered']):
            if p.reason=='source_declared_scoped_decision' and p.metadata.get('source_decision'):
                # Explicitly limited adjacent facts remain useful, while the
                # original requested obligation stays unfulfilled in the ledger.
                # A wrong planner field must not erase a verified answer to a
                # source-scoped question, or be silently marked fulfilled.
                result['status']='partial'
                ledger['terminal_state']='partial'
                ledger['adjacent_source_subset_retained']=True
            else:
                p=blocked(cat,'requested_operation_not_satisfied');result=engine._render_one(cat,q,locale,p,at)
                ledger=withhold_delivery(ledger,'requested_operation_not_satisfied','missing_source')
        elif ledger['terminal_state']=='partial' and result['status']=='answer':
            result['status']='partial'
            notice='ตอบได้เฉพาะส่วนที่มีหลักฐาน ความครบตามรูปแบบที่ขอยังยืนยันไม่ได้' if language(q,locale)=='th' else 'The source-backed subset is shown; completeness for the requested operation is not established.'
            result['answer']=notice+'\n'+result['answer']
        if dependency is not None:
            from .execution_dependencies import attach_ledger
            attach_ledger(ledger,task,dependency,result)
        result.update(question=item['meaning'].quote,execution_query=q,execution_contract=ledger)
        from .result_contract import package
        result['executor_result']=package(task,ledger,result,snapshot,{'request_model_calls':budget.model_calls})
        children.append(result);ledgers.append(ledger)
    def key(c):return c['fact_id'],c.get('numeric'),c['value']
    claims=list({key(c):c for child in children for c in child['claims']}.values())
    labels={key(c):i+1 for i,c in enumerate(claims)};blocks=[];rendered_by_question={}
    for child in children:
        local={i+1:labels[key(c)] for i,c in enumerate(child['claims'])}
        shown=re.sub(r'\[S(\d+)\]',lambda m:'[S'+str(local[int(m[1])])+']',child['answer'])
        # A corrective task can be fully answered by an earlier task for the
        # same request. Suppress only an exact, already rendered subset; keep
        # the task and receipts, and retain any new caveat or different text.
        question_key=child['question'].strip()
        lines={line.strip() for line in shown.splitlines() if line.strip()}
        prior=rendered_by_question.setdefault((question_key,child['status']),{'lines':set(),'claims':set()})
        child_claims={key(c) for c in child['claims']}
        if child_claims and child_claims <= prior['claims'] and lines and lines <= prior['lines']:
            continue
        prior['lines'].update(lines);prior['claims'].update(child_claims)
        if len(children)>1:shown='**'+child['question'].strip()+'**\n\n'+shown
        blocks.append(shown)
    states=[c['status'] for c in children]
    state=states[0] if len(set(states))==1 else 'partial' if claims else 'unavailable' if 'unavailable' in states else 'missing_source'
    from .terminal_states import aggregate,VERSION as status_version
    terminal_state=aggregate((l['terminal_state'] for l in ledgers),bool(claims))
    return {'answer':'\n\n'.join(blocks),'status':state,'terminal_state':terminal_state,'status_mapping_version':status_version,'claims':claims,'needs':children,'model_events':budget.events,
        'understanding':working.as_dict(),'elapsed_sec':time.monotonic()-started,'fixture':any(c['fixture'] for c in children),
        'english_translation_missing':any(c['english_translation_missing'] for c in children),'selection_basis':'r123_typed_first_adapters',
        'effective_locale':language(question,locale),'release_id':engine.data.get('release_id'),'epoch':engine.data.get('epoch'),
        'execution_contract':{'version':'r129','path':'compiled_task_graph','request_plan':compiled.as_dict(),'tasks':ledgers,'executor_results':[child['executor_result'] for child in children],'schedule':schedule,
            'typed_reads_before_fallback':True,'scheduling_scope':'ready_independent_typed_tasks_then_fallback_then_verified_dependents','execution_dependencies_checked':True,'whole_question_semantics_verified':False,'compatibility_readers_explicit':True}}
