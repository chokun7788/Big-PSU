"""Audit native calendar/live adapters without claiming text entailment.

Native providers still own date/window/freshness behavior. A source-pointer
receipt is not proof of business truth or whole-question interpretation.
"""
import copy,json,time
from dataclasses import asdict,replace
from ..registry import aware,value
from .plan_contract import compile_request
from .context_guard import apply as guard
from .scope import reference_time

def prepare(question,proposal,engine,at):
    working=guard(question,engine.index,copy.deepcopy(proposal))
    snapshot={'release_id':engine.data.get('release_id'),'epoch':engine.data.get('epoch'),'reference_time':reference_time(at).isoformat()}
    return working,compile_request(question,working,engine.index,snapshot)

def scoped_question(meaning):
    material=[meaning.target,*[c['quote'] for c in meaning.constraints]]
    return meaning.quote+' '+' '.join(s for s in dict.fromkeys(material) if s and s not in meaning.quote)

def frozen_ref(ref):return json.dumps(ref,sort_keys=True,ensure_ascii=False)

def receipt_checks(result,snap,at):
    art=result.decision_artifact or {};records=snap['release']['records'];sources=snap['release']['sources']
    checks=[];errors=[]
    for row in art.get('obligations',[]):
        if row.get('status')!='known':continue
        rid=row.get('record_id');key=row.get('field');record=records.get(rid,{})
        field=record.get('fields',{}).get(key,{})
        refs=row.get('evidence_refs') or []
        allowed={frozen_ref(x) for x in field.get('evidence_refs',[])}
        ok=bool(refs) and rid not in snap.get('withdrawn',[]) and field.get('status')=='known' and all(frozen_ref(x) in allowed and x.get('source_id') in sources for x in refs)
        checks.append({'record_id':rid,'field':key,'record_revision':record.get('revision'),'release_id':snap['active'],
            'epoch':snap['epoch'],'evidence_refs':refs if ok else [],'pointer_verified':ok,'value_entailment_verified':False})
        if not ok:errors.append('native_source_receipt_mismatch')
    # Recheck the delivered timestamp against the request clock and source TTL.
    # Provider slot semantics still belong to the native, bounded adapter.
    live_checks=[]
    for o in (art.get('live_booking') or {}).get('observations',[]):
        binding=records.get(o.get('binding_id'),{})
        if o.get('status')!='supported':
            live_checks.append({'binding_id':o.get('binding_id'),'terminal_state':'missing_input' if o.get('reason')=='time_required' else 'provider_unavailable','reason':o.get('reason')});continue
        ttl=value(binding,'freshness_max_age_seconds') if binding else None
        try:
            from datetime import timedelta
            elapsed=o.get('request_clock_elapsed_seconds',0)
            if not isinstance(elapsed,(int,float)) or not 0<=elapsed<=600:raise ValueError('invalid_request_clock_elapsed')
            if o.get('freshness_clock_basis')=='provider_wall_clock':
                from ..legacy_live_on_demand import freshness_now
                check_clock=freshness_now()
            else:check_clock=reference_time(at)+timedelta(seconds=elapsed)
            if o.get('observed_at_timezone'):
                from ..legacy_live_on_demand import observed_time
                if o['observed_at_timezone']!=value(binding,'timezone'):raise ValueError('timezone_binding_mismatch')
                stamp=observed_time(o.get('observed_at'),o['observed_at_timezone'])
            else:stamp=aware(o.get('observed_at'))
            age=(check_clock-stamp).total_seconds()
        except (TypeError,ValueError):age=None
        mapping={x['raw']:x['normalized'] for x in (value(binding,'status_mapping') or [])} if binding else {}
        slots=o.get('slot_coverage',[])
        expected=mapping.get(o.get('provider_status'),'unknown')
        if slots:
            states=[mapping.get(s.get('raw_status'),'unknown') for s in slots]
            expected='free' if all(s=='free' for s in states) else 'unavailable' if 'unavailable' in states else 'occupied' if 'occupied' in states else 'unknown'
        ok=(binding.get('kind')=='live_binding' and binding.get('record_id') not in snap.get('withdrawn',[])
            and type(ttl) is int and ttl>0 and age is not None and 0<=age<=ttl
            and o.get('max_age_seconds')==ttl and o.get('resource_key')==value(binding,'external_resource_key')
            and o.get('physical_pool_key')==value(binding,'physical_pool_key') and o.get('provider')==value(binding,'provider')
            and o.get('normalized_status')==expected and expected!='unknown' and o.get('freshness_checked') is True)
        live_checks.append({'binding_id':o.get('binding_id'),'terminal_state':'supported' if ok else 'invalid_plan',
            'binding_mapping_and_clock_checked':ok,'age_seconds_recomputed':age,'provider_fact_independently_verified':False,
            'window_coverage_basis':'native_live_adapter'})
        if not ok:errors.append('native_live_mapping_or_freshness_mismatch')
    return checks,live_checks,list(dict.fromkeys(errors))

def terminal(art):
    response=art.get('response_type')
    if response=='retry':return 'not_current'
    if (art.get('query_plan') or {}).get('time_required'):return 'missing_input'
    return {'answer':'supported','list':'supported','partial_answer':'partial','unconfirmed':'missing_source',
        'clarification':'missing_input','not_current':'not_current','live_unavailable':'provider_unavailable',
        'unavailable':'provider_unavailable'}.get(response,'missing_source')

def attach_native(reader,result,snap,compiled,at,lang):
    receipts,live,errors=receipt_checks(result,snap,at)
    art=result.decision_artifact or {};state=terminal(art)
    if not result.validation.ok:errors.append('native_validation_rejected')
    if errors:
        rejected={'response_type':art.get('response_type'),'errors':errors}
        body='หลักฐานของส่วนนี้ยังตรวจยืนยันไม่ได้ครับ' if lang=='th' else 'The evidence for this part could not be verified.'
        safe=reader.finish(snap,time.perf_counter(),body,[],{'record_ids':[],'requested_fields':[],'method':'r123_native_receipt_rejected'},[],response='unconfirmed')
        result=replace(safe,decision_artifact={**safe.decision_artifact,'native_rejection':rejected,'understanding':art.get('understanding',{})})
        art=result.decision_artifact;receipts=[];state='invalid_plan'
    task=compiled.tasks[0]
    delivered={r['field'] for r in receipts if r.get('pointer_verified')}
    field_aliases={'open_periods':{'open_periods','service_periods'},'bookable_periods':{'bookable_periods','service_periods'},'maintenance_periods':{'maintenance_periods'},'closing_time':{'open_periods','service_periods','closing_time'},'local_date':{'service_periods'}}
    obligations=[]
    for o in task.obligations:
        proved=bool(state=='supported' and not errors and ((o.kind=='task_completion' and delivered & field_aliases.get(o.expected,{o.expected})) or (o.expected=='live_status' and live and all(r['terminal_state']=='supported' for r in live))))
        obligations.append({'id':o.id,'kind':o.kind,'expected':o.expected,'verification':'typed_source_field_and_native_provider_contract','fulfilled':proved if proved or state!='supported' else None,'semantic_review_required':not proved,'source_receipt_fields':sorted(delivered)})
    ledger={'task_id':task.id,'terminal_state':state,'receipts':receipts,'live_observations':live,'fatal':errors,
        'obligations':obligations,
        'source_pointer_verification_only':True,'whole_question_semantics_verified':False}
    contract={'version':'r123','path':'native_calendar_live_bridge','request_plan':compiled.as_dict(),'tasks':[ledger],
        'schedule':[{'phase':'native_typed_adapter','task_id':task.id}],'typed_reads_before_fallback':True,
        'compatibility_readers_explicit':True,'whole_question_semantics_verified':False}
    rows=[{**row,'execution_contract':ledger} for row in art.get('need_results',[])]
    from .result_contract import package
    typed={'claims':art.get('domain_flow',{}).get('typed_claims',[]),'plan':{'metadata':{}},'reason':(art.get('query_plan') or {}).get('method'),'computations':[]}
    contract['executor_results']=[package(task,ledger,typed,compiled.snapshot)]
    return replace(result,decision_artifact={**art,'execution_contract':contract,'need_results':rows})

def aggregate_contract(compiled,outputs,typed_first=False,schedule_events=None):
    ledgers=[];schedule=[]
    for task,child in zip(compiled.tasks,outputs):
        art=(child.decision_artifact or {}) if child is not None else {}
        c=art.get('execution_contract') or {};rows=c.get('tasks') or []
        # Keep the original child contract for audit; parent IDs refer to the
        # whole question, never to the synthetic child execution text.
        ledger=copy.deepcopy(rows[0]) if len(rows)==1 else {'terminal_state':'missing_source','receipts':[],'obligations':[]}
        ledger.update(task_id=task.id,child_contract_path=c.get('path','unverified_native_compatibility'),child_contract=c)
        ledgers.append(ledger);schedule.append({'phase':'native_child_delivered','task_id':task.id})
    return {'version':'r123','path':'native_compound_bridge','request_plan':compiled.as_dict(),'tasks':ledgers,'schedule':(schedule_events or [])+schedule,
        'typed_reads_before_fallback':typed_first,'scheduling_scope':'all_native_typed_children_then_deferred_evidence_selection' if typed_first else 'native_compatibility_sequential',
        'compatibility_readers_explicit':True,'whole_question_semantics_verified':False}

def guard_contract(result,compiled,state,reason):
    """A missing binding is a source gap, not a failed provider/model call."""
    if compiled is None:return
    ledgers=[]
    for task,need in zip(compiled.tasks,result['needs']):
        need['claims']=[]
        ledger={'task_id':task.id,'terminal_state':state,'reason':reason,'receipts':[],
            'obligations':[{'id':o.id,'kind':o.kind,'expected':o.expected,'fulfilled':False} for o in task.obligations],
            'provider_read_attempted':False,'model_transport_failure':False,'whole_question_semantics_verified':False}
        need['execution_contract']=ledger;ledgers.append(ledger)
    result['claims']=[]
    result['execution_contract']={'version':'r123','path':'native_guard_bridge','request_plan':compiled.as_dict(),'tasks':ledgers,
        'typed_reads_before_fallback':True,'whole_question_semantics_verified':False,'compatibility_readers_explicit':True}

def invalidate(contract):
    """A snapshot retry invalidates delivery, including nested child receipts."""
    c=copy.deepcopy(contract);c['delivery_invalidated']=True;c['delivery_reason']='snapshot_changed_before_delivery'
    for task in c.get('tasks',[]):
        task.update(terminal_state='not_current',receipts=[],live_observations=[])
        for obligation in task.get('obligations',[]):obligation.update(fulfilled=False,verification='delivery_invalidated')
        if task.get('child_contract'):task['child_contract']=invalidate(task['child_contract'])
    return c
