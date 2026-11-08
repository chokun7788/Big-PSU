"""R97 orchestration shared by every common task and owner preview.

Domain adapters retain proven calculators/rule readers; none gets a separate
model budget or a separate snapshot. A semantic plan enters execute_task
directly, without being vetoed by the old sentence grammar a second time.
"""
from dataclasses import asdict,replace
import re,time
from .registry import value
from .flow_context import request_context,CURRENT
from .task_contracts import TASKS
from .request_plan import make_plan,attach,aggregate
from .read_graph import compile,evaluate,REQUIRED,linked

def execute(reader,need,snap,at,lang):
    records={k:r for k,r in snap['release']['records'].items() if k not in snap.get('withdrawn',[])}
    task=need.task;ids=[k for k in need.record_ids if k in records]
    temporal=None
    if task not in {'live_status','schedule'}:
        from .temporal_query import scope as query_time
        temporal=query_time(need.query,at,records,snap['release']['names'])
        if temporal and temporal.get('invalid'):
            return reader.finish(snap,time.perf_counter(),'วันที่ระบุไม่ถูกต้อง กรุณาระบุวันที่ใหม่ / The requested date is invalid. Please specify it again.',[],{'record_ids':ids,'requested_fields':[],'date_required':True,'method':'r102_invalid_date'},[],response='clarification')
        if temporal:at=temporal['target']
    from .flow_audit import event
    event('S07_compile',need_id=need.id,task=task,record_ids=ids)
    if task not in TASKS:return None
    if not ids and task not in {'live_status','competition_rules','schedule','equipment_list'}:return None
    from .query_contract import strip_names
    from .query_scope import same_platform
    games=[k for k in ids if records[k]['kind']=='game']
    residual=strip_names(need.query,games,snap['release']['names'])
    platforms={value(r,'platform') for r in records.values() if isinstance(value(r,'platform'),str)}
    platform_matches={p for p in platforms if re.search(r'(?<![a-z0-9])'+re.escape(p)+r'(?![a-z0-9])',residual,re.I)}
    # Platform shorthand is derived from declared service names/aliases.
    from .answer import named
    service_ids,_=named(residual,{k:snap['release']['names'].get(k,[]) for k,r in records.items() if r['kind']=='service'},allow_fuzzy=False)
    platform_matches.update(value(records[k],'platform') for k in service_ids if value(records[k],'platform'))
    anchor=next(iter(platform_matches)) if platform_matches else None
    selected_platform=anchor if anchor and all(same_platform(p,anchor) for p in platform_matches) else None
    if task not in {'price','rental','live_status','equipment_specs','game_players','game_controls','game_at_studio','game_account','game_version','competition_rules'}:
        ids=[k for k in ids if records[k]['kind'] in TASKS[task].kinds]
    # Financial, calendar, rule and live calculations use the existing typed
    # adapters. A model cannot invent a formula, choose an audience or convert
    # a prose policy into an unconditional yes/no.
    if task=='live_status':
        from .live_reader import answer as read_live
        bound=read_live(reader,need,snap,at,lang)
        if bound is not None:return bound
        if reader.external_executor is None:return None
        ctx=CURRENT.get();key=('live',need.query)
        if ctx and key in ctx.live:return ctx.live[key]
        result=reader.external_executor(need.query)
        if ctx:ctx.live[key]=result
        return result
    if task=='rental':
        from .rental_bridge import answer as rental
        result=rental(reader,snap,time.perf_counter(),need.query,lang,records,[],at)
        if result is not None:return result
    if task=='schedule':
        from .open_day import answer as opening
        result=opening(reader,snap,time.perf_counter(),need.query,lang,at,records)
        if result is not None:return result
        from .query_scope import calendar_ids
        selected,day=calendar_ids(need.query,records,at)
        if not day:return None
        ids=selected
        if not ids:return None
    if task=='competition_rules':
        from .rules_reader import answer as rules_read
        result=rules_read(reader,need,snap,at,lang)
        if result is not None:return result
        from .competition_bridge import answer as competition
        result=competition(reader,snap,time.perf_counter(),need.query,lang,records,ids,at,{'record_ids':ids})
        if result is not None:return result
    fields=list(TASKS[task].fields)
    graph,targets,edges=compile(task,ids,records,fields=fields,predicate=need.predicate)
    if selected_platform and task in {'game_controls','game_players','game_version'}:
        targets=[k for k in targets if same_platform(value(records[k],'platform'),selected_platform)]
        if targets:graph,_,_=compile(task,targets,records,fields=fields,predicate=need.predicate)
    if not targets:
        if ids and task in {'game_at_studio','game_controls','game_players','game_account','game_version'}:
            body='ยังไม่มีข้อมูลที่เชื่อมกับรายการนี้สำหรับส่วนที่ถามครับ' if lang=='th' else 'No linked source is recorded for the requested detail of this item.'
            return reader.finish(snap,time.perf_counter(),body,[],{'record_ids':ids,'requested_fields':[],'method':'r104_required_relation_missing'},[],response='unconfirmed')
        return None
    if task=='rental' and len(targets)>1 and not re.search(r'ทั้งหมด|ทุกแพ็กเกจ|\b(?:all|every)\b',need.query,re.I):
        from .answer import title
        body=('ต้องการแพ็กเกจใดครับ: ' if lang=='th' else 'Which rental package do you mean: ')+', '.join(title(records[k],lang) for k in targets)
        return reader.finish(snap,time.perf_counter(),body,[],{'record_ids':[],'requested_fields':[],'method':'r101_rental_package_slot','pending_selection':{'candidate_ids':targets,'subject_kind':None,'allow_all':True}},[],response='clarification')
    groups=None
    if task=='price':
        from .claim_bindings import current_claims
        overrides=[c for c in current_claims(snap,at) if c['predicate']=='current_rate' and c['authority_refs'] and any(k+'#amount_minor' in c['supersedes_refs'] for k in targets)]
        if overrides:
            body='แหล่งข้อมูลใหม่ใช้แทนอัตราเดิมแล้ว แต่ยังไม่มีอัตราตัวเลขฉบับใหม่สำหรับคำนวณ กรุณาให้ผู้ดูแลแก้ตารางราคาครับ' if lang=='th' else 'A new source supersedes the old rate, but the replacement numeric rate has not been entered for calculation. Please ask the owner to update the rate table.'
            return reader.finish(snap,time.perf_counter(),body,[],{'record_ids':[],'requested_fields':[],'method':'r103_superseded_numeric_rate','superseding_claim_ids':[c['claim_id'] for c in overrides]},[],response='unconfirmed')
        from .financial_scope import resolve as financial_scope
        targets,groups,scoped_result=financial_scope(reader,need,snap,records,ids,targets,lang)
        if scoped_result is not None:return scoped_result
        if not targets:return None
        graph,_,_=compile(task,targets,records,fields=fields,predicate=need.predicate)
        if temporal and not temporal['explicit_time']:
            from .registry import aware
            intersects=lambda r:not (r['validity'].get('effective_from') and aware(r['validity']['effective_from'])>=temporal['day_end'] or r['validity'].get('effective_until') and aware(r['validity']['effective_until'])<=temporal['day_start'])
            targets=[k for k in targets if records[k]['validity']['state']!='known' or intersects(records[k])]
            if not targets:
                body='ยังไม่มีอัตราราคาที่มีผลสำหรับวันที่ถามครับ' if lang=='th' else 'No rate is confirmed as applicable to the requested date.'
                return reader.finish(snap,time.perf_counter(),body,[],{'record_ids':ids,'requested_fields':[],'method':'r102_price_outside_target_date'},[],response='not_current')
            graph,_,_=compile(task,targets,records,fields=fields,predicate=need.predicate)
            partial=[k for k in targets if records[k]['validity']['state']=='known' and ((records[k]['validity']['effective_from'] and aware(records[k]['validity']['effective_from'])>temporal['day_start']) or (records[k]['validity']['effective_until'] and aware(records[k]['validity']['effective_until'])<temporal['day_end']))]
            if partial:
                body='อัตราราคาใช้ไม่ครอบคลุมทุกช่วงเวลาของวันที่ถาม ต้องการใช้เวลากี่โมงครับ?' if lang=='th' else 'The rates do not apply throughout the requested date. What time do you want to use the service?'
                return reader.finish(snap,time.perf_counter(),body,[],{'record_ids':[],'requested_fields':[],'method':'r102_price_time_applicability_slot','pending_selection':{'candidate_ids':ids,'slot':'time'}},[],response='clarification')
    evaluated=evaluate(graph,snap,at,need.id,need.predicate)
    if evaluated['status'] in {'broken_relation','unsupported','conflict'}:
        body='ข้อมูลที่เชื่อมกับรายการนี้ไม่ถูกต้องหรือไม่อยู่ในขอบเขตที่อนุญาต จึงยังยืนยันคำตอบไม่ได้ครับ' if lang=='th' else 'The linked data is invalid or outside its allowed scope, so this detail cannot be confirmed.'
        result=reader.finish(snap,time.perf_counter(),body,[],{'record_ids':ids,'requested_fields':[],'method':'r102_invalid_graph_dependency','graph_result':evaluated},[],response='unconfirmed')
        return replace(result,decision_artifact={**result.decision_artifact,'need_results':[{'need_id':need.id,'task':task,'status':evaluated['status'],'reason_codes':[evaluated.get('reason','invalid_dependency')],'receipts':[]}]})
    from .qualifier_contract import requirements
    qualifiers=requirements(need,records,targets,point_date=bool(temporal))
    if not qualifiers['satisfied']:
        body=('ข้อมูลยังไม่ยืนยันเงื่อนไขที่ถาม: ' if lang=='th' else 'The source does not confirm the requested conditions: ')+', '.join(qualifiers['missing'])
        return reader.finish(snap,time.perf_counter(),body,[],{'record_ids':ids,'requested_fields':[],'method':'r101_qualifier_source_gap','qualifier_review':qualifiers},[],response='unconfirmed')
    if task=='price':
        # Rates stay named by audience/unit; no implicit audience default.
        fields=list(dict.fromkeys(fields+['service_id','audience_id','currency','unit','duration_minutes','calculation_rule']))
    if task in {'policy','procedure','faq_content','game_account'}:
        # Select one declared policy scope. Conditions remain complete source
        # text; permission is never inferred from a matching keyword.
        for rid in targets:
            r=records[rid]
            profile=value(r,'query_profile')
            if profile:
                from .qualified_reply import scope_plan
                _,audit=scope_plan(need.query,r,records)
                if audit.get('reason') in {'conflicting_slots','unsupported_qualifier','ambiguous_qualified_profiles'}:return None
        if task in {'policy','game_account'}:
            fields=list(dict.fromkeys(fields+['topic','subject','decision','conditions_all','exceptions','details','consequence']))
    if task=='people':fields=list(dict.fromkeys(fields+['public_scope']))
    if task=='competition_rules':fields=['heading','text','completeness']
    required_keys={key for branch in REQUIRED[task] for key in branch}
    requested=[f for f in fields if any(f in records[k]['fields'] and (f in required_keys or value(records[k],f) is not None) for k in targets)]
    if not requested:return None
    plan={'record_ids':targets,'scope_ids':ids,'requested_fields':requested,'operation':TASKS[task].operation,
      'all_fields':False,'platform':selected_platform,'unresolved_clauses':[],'method':'r101_accepted_need_executor',
      'task_plan':{'task':task,'predicate':need.predicate,'qualifiers':need.qualifiers,'slots':need.slots},
      'read_graph':asdict(graph),'relation_paths':edges,'required_claims':need.required_claims,
      'semantic_plan_accepted':True}
    plan['qualifier_review']=qualifiers
    if temporal:plan.update(temporal_applicability_checked=True,temporal_target=at.isoformat(),requested_date_span=temporal['source_span'])
    if task=='price':
        from .budget import budget_request
        from .answer import effective
        current={k:r for k,r in records.items() if effective(r,at,records)}
        budget=budget_request(need.query,current,[k for k in [*ids,*(groups or [])] if k in current])
        if budget is not None:plan['budget']=budget
    if any(c['requirement']=='requested_year_applicability' and c['satisfied'] for c in qualifiers['checks']):
        from datetime import datetime
        year=re.search(r'(?:\b(?:in|for|during)\b|ในปี|ปี)\s*(20\d{2}|25\d{2})(?!\d)',need.query,re.I)
        y=int(year[1]);y=y-543 if y>=2500 else y
        at=datetime.fromisoformat(f'{y}-01-01T00:00:00+07:00')
        plan.update(temporal_applicability_checked=True,temporal_target=at.isoformat())
    from .authority import classify,field_ownership
    plan['authority']=classify(need.query,snap,ids)
    if plan['authority']['decision']!='common':return None
    plan['field_authority']=field_ownership(snap,targets,requested)
    event('S08_read',need_id=need.id,task=task,record_ids=targets,fields=requested,relation_paths=edges)
    return reader.execute_task(need.query,snap=snap,at=at,lang=lang,plan=plan)

def _task_for_result(need,art,records):
    plan=art.get('query_plan') or {}
    executed=(plan.get('task_plan') or {}).get('task') or art.get('task_flow',{}).get('task')
    if need.task=='unresolved' and executed in TASKS:return executed
    if need.task=='unresolved':
        ids=plan.get('record_ids',[]);kinds={records[k]['kind'] for k in ids if k in records}
        mapping={'faq':'faq_content','policy':'policy','procedure':'procedure','news':'news','contact':'contact','facility':'facility','person':'people','audience':'audience','game':'game_overview','competition_rule':'competition_rules'}
        if len(kinds)==1:return mapping.get(next(iter(kinds)),'unresolved')
    return need.task

def certify(result,plan,snap,at):
    """Graph and claim packets bind actual values to the executed need."""
    if result is None:return None
    art=dict(result.decision_artifact or {});records=snap['release']['records']
    if art.get('flow_contract',{}).get('version')=='r101':return result
    qp=art.get('query_plan') or {};rows=art.get('need_results',[])
    if len(plan.needs)>1 and len(rows)==len(plan.needs):
        art['flow_contract']={'version':'r101','revision':'r103','all_needs_executed':True,'child_count':len(rows)}
        art['claim_packets']=[p for row in rows for p in row.get('claim_packets',[])]
        return replace(result,decision_artifact=art)
    from .claim_conflicts import detect
    read_ids=list(dict.fromkeys(qp.get('record_ids',[])+[o['record_id'] for o in art.get('obligations',[]) if o.get('record_id')]))
    unsafe_people=[k for k in read_ids if k in records and records[k]['kind']=='person' and (records[k]['fields'].get('public_scope',{}).get('status')!='known' or re.search(r'private|internal|not public|ภายใน|ห้ามเผยแพร่',str(value(records[k],'public_scope') or ''),re.I))]
    if unsafe_people and art.get('response_type') in {'answer','list','partial_answer'}:
        body='ยังยืนยันขอบเขตข้อมูลบุคลากรที่เปิดเผยได้ไม่ครบ จึงยังแสดงรายละเอียดส่วนนี้ไม่ได้ครับ' if re.search('[\u0e00-\u0e7f]',plan.question) else 'The public scope of the staff information is not fully confirmed, so these details cannot be shown.'
        art.update(response_type='unconfirmed',claim_packets=[],obligations=[],request_plan=asdict(plan),
          need_results=[{'need_id':n.id,'task':n.task,'status':'unsupported','reason_codes':['person_public_scope_not_confirmed'],'receipts':[]} for n in plan.needs],
          flow_contract={'version':'r101','revision':'r102','all_needs_executed':True})
        return replace(result,answer=body,hits=[],mode='pipeline:common_unconfirmed',decision_artifact=art)
    conflicts=detect(read_ids,snap,at)
    from .flow_audit import event
    event('S10_evidence',record_ids=read_ids,conflict_count=len(conflicts))
    if conflicts and art.get('response_type') in {'answer','list','partial_answer'}:
        body='ข้อมูลที่มีผลในขอบเขตเดียวกันขัดกัน จึงยังยืนยันค่าที่ถูกต้องไม่ได้ครับ กรุณาให้ผู้ดูแลตรวจข้อขัดแย้งนี้ก่อน' if re.search('[\u0e00-\u0e7f]',plan.question) else 'Current sources disagree within the same scope. The value cannot be confirmed until the administrator resolves this conflict.'
        art.update(response_type='unconfirmed',claim_conflicts=conflicts,claim_packets=[],obligations=[],
          request_plan=asdict(plan),need_results=[{'need_id':n.id,'task':n.task,'predicate':n.predicate,'status':'conflict','reason_codes':['contradictory_current_typed_claims'],'receipts':[]} for n in plan.needs],
          flow_contract={'version':'r101','all_needs_executed':True})
        return replace(result,answer=body,hits=[],mode='pipeline:common_unconfirmed',decision_artifact=art)
    if any(n.task=='price' for n in plan.needs):
        from .claim_bindings import current_claims
        stale=[c for c in current_claims(snap,at) if c['predicate']=='current_rate' and c['authority_refs'] and any(k+'#amount_minor' in c['supersedes_refs'] for k in read_ids)]
        if stale:
            body='ตารางราคาเดิมถูกแทนที่แล้ว ต้องปรับตัวเลขอัตราฉบับใหม่ก่อนคำนวณครับ' if re.search('[\u0e00-\u0e7f]',plan.question) else 'The old rate has been superseded. The replacement numeric rate is required before calculation.'
            art.update(response_type='unconfirmed',claim_packets=[],obligations=[],request_plan=asdict(plan),need_results=[{'need_id':n.id,'task':n.task,'status':'missing_source','reason_codes':['superseded_rate_requires_typed_replacement'],'receipts':[]} for n in plan.needs],flow_contract={'version':'r101','revision':'r103','all_needs_executed':True})
            return replace(result,answer=body,hits=[],mode='pipeline:common_unconfirmed',decision_artifact=art)
    if any(n.task=='live_status' for n in plan.needs) and not art.get('live_booking') and art.get('response_type') in {'answer','list','partial_answer'}:
        body='ยังยืนยันสถานะว่างปัจจุบันไม่ได้ครับ' if re.search('[\u0e00-\u0e7f]',plan.question) else 'Current availability is not confirmed.'
        art.update(response_type='live_unavailable',claim_packets=[],obligations=[],request_plan=asdict(plan),need_results=[{'need_id':n.id,'task':n.task,'status':'live_unavailable','reason_codes':['live_observation_required'],'receipts':[]} for n in plan.needs],flow_contract={'version':'r101','revision':'r103','all_needs_executed':True})
        return replace(result,answer=body,hits=[],mode='pipeline:common_live_unavailable',decision_artifact=art)
    if art.get('mapped_claim_packets'):
        art.update(request_plan=asdict(plan),claim_packets=art['mapped_claim_packets'],flow_contract={'version':'r101','revision':'r102','all_needs_executed':True,'mapping_receipts_verified':True})
        return replace(result,decision_artifact=art)
    # Compound children have already been certified before aggregation.
    if len(plan.needs)>1 and len(rows)==len(plan.needs):
        art['flow_contract']={'version':'r101','all_needs_executed':True,'child_count':len(rows)}
        return replace(result,decision_artifact=art)
    packets=[];newrows=[]
    for i,need in enumerate(plan.needs):
        task=_task_for_result(need,art,records)
        if task in TASKS:need.task=task
        existing=rows[i] if i<len(rows) else {'need_id':need.id,'task':task,'status':'missing_source','receipts':[]}
        ids=[k for k in qp.get('record_ids',[]) if k in records]
        fields=qp.get('requested_fields',[])
        if task in TASKS:
            graph,targets,edges=compile(task,ids,records,fields=fields,predicate=need.predicate)
            from .registry import aware
            read_at=aware(qp['temporal_target']) if qp.get('temporal_applicability_checked') and qp.get('temporal_target') else at
            evaluated=evaluate(graph,snap,read_at,need.id,need.predicate)
            # Selected fields are the delivered claims. Full graph readiness
            # must not certify a claim the response never actually rendered.
            known={(o.get('record_id'),o.get('field')) for o in art.get('obligations',[]) if o.get('status')=='known' and o.get('evidence_refs')}
            claims=[p for p in evaluated.get('receipts',[]) if result.validation.ok and (p['record_id'],p['field']) in known]
            required={ (p['record_id'],p['field']) for p in evaluated.get('receipts',[]) }
            delivered=bool(claims) and required<=known
            check={'graph':asdict(graph),'targets':targets,'relation_paths':edges,'evaluation':evaluated,'required_claims_delivered':delivered}
            # Preserve domain distinctions and do not replace an explicit
            # partial/ambiguous/error state with mere field completeness.
            if existing['status']=='scope_unverified':
                if evaluated['status']=='supported' and delivered:existing={**existing,'status':'supported','reason_codes':['typed_graph_and_delivered_claims']}
                elif known:existing={**existing,'status':'partial_supported','reason_codes':['source_excerpt_without_complete_required_claims']}
                else:existing={**existing,'status':evaluated['status'],'reason_codes':[evaluated.get('reason','required_claims_not_delivered')]}
            existing={**existing,'task':task,'read_graph':check,'claim_packets':claims}
            if existing['status']=='supported' and evaluated['status']!='supported' and task not in {'schedule','equipment_list','schema_attributes'}:
                # Typed coverage from an old adapter cannot bypass a missing
                # dependency in the shared graph. Existing schedule prose and
                # inventory-set adapters have separate predicate/set receipts.
                existing={**existing,'status':'partial_supported' if known else evaluated['status'],
                  'reason_codes':['required_graph_dependency_not_supported']}
            packets.extend(claims)
        newrows.append(existing)
    art.update(request_plan=asdict(plan),need_results=newrows,claim_packets=packets,
      flow_contract={'version':'r101','all_needs_executed':True,'semantic_entailment_claimed':False},
      request_context=CURRENT.get().public() if CURRENT.get() else {})
    # Include explicit source-set proof only when the adapter enumerated the
    # whole scope, not by counting top-K search candidates.
    if art.get('response_type')=='list' and qp.get('list_scope'):
        art['scope_receipt']={'release_id':snap['active'],'epoch':snap['epoch'],'filter':{'task':plan.needs[0].task},
          'member_ids':qp.get('record_ids',[]),'total_members':len(qp.get('record_ids',[])),
          'returned_members':len(qp.get('record_ids',[])),'scope':'adapter_enumerated_common_set'}
    # A bare decision with unknown conditions is not a confirmed permission.
    # Do not leave an unconditional assertion above a disclaimer.
    policies=[records[k] for k in qp.get('record_ids',[]) if k in records and records[k]['kind']=='policy']
    if art.get('response_type') in {'answer','partial_answer'} and any(value(r,'decision') is not None and r['fields'].get('conditions_all',{}).get('status')!='known' for r in policies):
        language='en' if not re.search('[\u0e00-\u0e7f]',plan.question) else 'th'
        body='เงื่อนไขของข้อกำหนดนี้ยังไม่ครบ จึงยังยืนยันการอนุญาตหรือการห้ามในกรณีที่ถามไม่ได้ครับ' if language=='th' else 'The conditions of this policy are incomplete, so permission or prohibition for the requested situation is not confirmed.'
        art['response_type']='unconfirmed';art['claim_packets']=[];art['obligations']=[]
        art['need_results']=[{**r,'status':'missing_source','claim_packets':[],'receipts':[],'reason_codes':['policy_conditions_unknown']} for r in newrows]
        result=replace(result,answer=body,hits=[],mode='pipeline:common_unconfirmed')
    return replace(result,decision_artifact=art)

def _answer(reader,question,*,locale='th',history=None,at=None,planner=None,_composing=False,_snapshot=None):
    from .snapshot_provider import PinnedSnapshotView
    from .authority import scoped_names
    from .query_scope import derived_names
    from app.calendar.service_calendar import now_bangkok
    with request_context() as ctx:
        # Pin even direct/owner calls, which do not enter migrated dispatcher.
        snap=_snapshot if _snapshot is not None else reader.store.snapshot()
        if not snap.get('release'):return None
        ctx.snapshot={'release_id':snap['active'],'epoch':snap['epoch'],'reference_time':(at or now_bangkok()).isoformat(),'locale':locale}
        at=at or now_bangkok();lang='en' if locale=='en' else 'th'
        ctx.event('S01_pin_context',snapshot=ctx.snapshot)
        records={k:r for k,r in snap['release']['records'].items() if k not in snap.get('withdrawn',[])}
        names=derived_names(scoped_names(snap),records)
        from .interpret_surface import canonical as interpret
        interpreted=interpret(question,records,names)
        if interpreted!=question:ctx.event('S02_normalize',raw_question=question,interpreted_question=interpreted,owner_names_protected=True)
        question=interpreted
        plan=make_plan(question,records,names,history,split=not _composing)
        ctx.event('S03_state_binding',trusted_state=plan.scope.get('history_has_trusted_state',False),slot_origins=[n.slot_origin for n in plan.needs])
        ctx.event('S04_discovery',records_in_snapshot=len(records),explicit_root_ids=list(dict.fromkeys(k for n in plan.needs for k in n.record_ids)))
        ctx.event('S05_plan',needs=[{'id':n.id,'task':n.task,'subjects':n.record_ids,'qualifiers':n.qualifiers,'slots':n.slots} for n in plan.needs])
        if len(plan.needs)>1:
            if planner is not None and any(n.task=='unresolved' for n in plan.needs):
                from .grounded_plan import propose
                semantic=propose(question,records,names,list(dict.fromkeys(k for n in plan.needs for k in n.record_ids)))
                if semantic:plan=semantic
            results=[]
            for n in plan.needs:
                r=execute(reader,n,snap,at,lang) if n.task in TASKS else None
                if r is None and n.task!='unresolved':r=answer(reader,n.query,locale=locale,history=history,at=at,planner=None,_composing=True,_snapshot=snap)
                if r is not None:
                    from .request_plan import RequestPlan
                    child_plan=RequestPlan(plan.version,n.query,[n],plan.scope)
                    r=certify(attach(r,child_plan,snap),child_plan,snap,at)
                results.append(r)
            result=aggregate(reader,snap,time.perf_counter(),plan,results,lang)
            return certify(result,plan,snap,at)
        # Keep mature typed calculations and existing targeted pending flows;
        # remove their independent field-level LLM entry points.
        need=plan.needs[0]
        # A named catalog miss is already a resolved subject constraint. It
        # cannot become an unrelated FAQ merely because retrieval finds one.
        from .target_selection import unmatched_mention
        missing_target=unmatched_mention(question,records,names)
        if missing_target:
            body=('ยังไม่พบรายการเกมที่ตรงกับ “'+missing_target+'” ในข้อมูลชุดนี้ครับ จึงยังยืนยันบริการสำหรับเกมนี้ไม่ได้' if lang=='th' else 'No game record matching “'+missing_target+'” was found in this data set, so its studio offering is not confirmed.')
            result=reader.finish(snap,time.perf_counter(),body,[],{'record_ids':[],'requested_fields':[],
              'method':'r101_catalog_subject_gap','bridge_status':'unknown_target'},[],response='unconfirmed')
            result=replace(result,decision_artifact={**result.decision_artifact,'public_response_kind':'no_answer',
              'unmatched_target':{'mention':missing_target,'reason':'no_catalog_match','scope':'current_common_release'}})
            return certify(attach(result,plan,snap),plan,snap,at)
        from .target_selection import answer as target_answer
        result=target_answer(reader,question,snap,records,names,lang,history,at,planner)
        if result is None:
            from .qualified_tasks import answer as qualified_context
            result=qualified_context(reader,question,snap,records,names,lang,history,at)
        from .catalog_reader import answer as catalog
        if result is None:result=catalog(reader,need,snap,at,lang)
        if result is None and not history and need.task=='competition_rules':result=execute(reader,need,snap,at,lang)
        from .gap_explanations import direct
        if result is None:result=direct(reader,need,snap,at,lang)
        if result is None:
            from .set_reader import answer as declared_set
            result=declared_set(reader,need,snap,at,lang)
        if result is None:
            from .policy_coverage import answer as cover_policy
            result=cover_policy(reader,need,snap,at,lang)
        if result is None and need.task=='schedule':result=execute(reader,need,snap,at,lang)
        if result is None and need.task=='live_status':
            result=execute(reader,need,snap,at,lang)
        from .unified_pending import resolve as resolve_pending
        binding=resolve_pending(question,history,records,names)
        if binding and not binding['invalid']:
            need.task=binding['task'];need.predicate=binding['predicate'];need.record_ids=binding['record_ids']
            need.query=binding['query'];need.slots=binding['slots'];need.slot_origin='delivered_state_selection'
            result=execute(reader,need,snap,at,lang)
            if result is None:
                body='ยังไม่มีข้อมูลยืนยันสำหรับหัวข้อที่เลือกของรายการนี้ครับ' if lang=='th' else 'No confirmed source for the selected task is available for this item.'
                result=reader.finish(snap,time.perf_counter(),body,[],{'record_ids':need.record_ids,'requested_fields':[],'method':'r101_selected_task_source_gap'},[],response='unconfirmed')
        elif binding and binding['invalid']:
            body='กรุณาระบุชื่อรายการที่ต้องการให้ชัดอีกครั้งครับ' if lang=='th' else 'Please specify the item you want again.'
            result=reader.finish(snap,time.perf_counter(),body,[],{'record_ids':[],'requested_fields':[],'method':binding['reason']},[],response='clarification')
        if result is None and need.record_ids and re.search(r'ทั้งหมดทุกส่วน|ครบทุกส่วน|\b(?:all details|all fields|every detail)\b',question,re.I):
            need.task='schema_attributes';need.predicate='explicit_record_attributes'
            read={'record_ids':need.record_ids,'scope_ids':need.record_ids,'requested_fields':[],
              'all_fields':True,'operation':'read','method':'r101_explicit_full_record',
              'unresolved_clauses':[],'task_plan':{'task':'schema_attributes'}}
            result=reader.execute_task(question,snap=snap,at=at,lang=lang,plan=read)
        # Ordinary typed tasks use the graph executor FIRST. Financial/rule/
        # calendar/live adapters remain specialized executors under this plan.
        # Pending selectors must resolve their original qualified request first.
        if result is None and not history and need.record_ids and need.task=='price' and re.search(r'ไม่|\b(?:not|without|budget|afford)\b',question,re.I):
            result=execute(reader,need,snap,at,lang)
        if result is None and not history and need.record_ids and (need.task in {'game_version','game_account'} or need.task=='procedure' and any(records[k]['kind']=='procedure' for k in need.record_ids)):
            result=execute(reader,need,snap,at,lang)
        if result is None and not history and need.record_ids:
            from .task_flow import typed_task,_compatible_remainder
            task,basis=typed_task(question,need.record_ids,records,names)
            if task and need.task in {'unresolved',task} and TASKS[task].operation not in {'price','calendar','rules','live','policy','booking'} and _compatible_remainder(question,need.record_ids,records,names,task,basis):
                need.task=task
                from .intent_contracts import PREDICATES
                need.predicate=PREDICATES.get(task,task)
                result=execute(reader,need,snap,at,lang)
        if result is None and not history and need.record_ids and need.task in TASKS and TASKS[need.task].operation not in {'price','calendar','rules','live','policy','booking'}:
            result=execute(reader,need,snap,at,lang)
        if result is None:
            from .selection_surface import canonical as selection_surface
            from .followup_scope import delivered_state
            current_state=delivered_state(history) or {}
            selected_query=selection_surface(question) if any(current_state.get(k) for k in ('price_scope_request','pending_target','pending_competition_scope','r98_pending_context')) else question
            result=reader._compat_answer(selected_query,locale=locale,history=history,at=at,planner=None,_composing=_composing,_snapshot=snap)
        if result is not None and 'temporal_applicability_unconfirmed' in ((result.decision_artifact or {}).get('predicate_rejection') or {}).get('reason_codes',[]) and ctx.reserve_corrective():
            ctx.event('S09_corrective_read',reason='temporal_applicability',remaining_quota=0)
            temporal=execute(reader,need,snap,at,lang)
            if temporal is not None:result=temporal
        if result is None:
            from .unified_pending import resolve
            selection=resolve(question,history,records,names)
            if selection and not selection['invalid']:
                need.task=selection['task'];need.predicate=selection['predicate'];need.record_ids=selection['record_ids']
                need.query=selection['query'];need.slots=selection['slots'];need.slot_origin='delivered_state_selection'
                result=execute(reader,need,snap,at,lang)
        if result is None:
            # Existing reusable grammars propose the same Need contract. New
            # names are read from the current snapshot, never embedded in code.
            from .task_flow import typed_task,_compatible_remainder
            task,basis=typed_task(question,need.record_ids,records,names) if need.record_ids else (None,None)
            if task and need.task in {'unresolved',task} and _compatible_remainder(question,need.record_ids,records,names,task,basis):
                need.task=task
                result=execute(reader,need,snap,at,lang)
        response=(result.decision_artifact or {}).get('response_type') if result else None
        if need.task=='game_controls' and not any(records[k]['kind']=='game' or records[k]['kind']=='control_set' and value(records[k],'game_id') in records for k in need.record_ids if k in records):
            query=(result.decision_artifact or {}).get('query_plan',{}) if result else {}
            if not any(query.get(k) for k in ('pending_target','profile_confirmation')):
                from .answer import title
                games=sorted(k for k,r in records.items() if r['kind']=='game')[:6]
                if games:
                    body=('ต้องการทราบปุ่มของเกมไหนครับ? ระบุชื่อเกม เช่น ' if lang=='th' else 'Which game do you want the controls for? Name a game, for example: ')+', '.join(title(records[k],lang) for k in games)
                    result=reader.finish(snap,time.perf_counter(),body,[],{'record_ids':[],'requested_fields':[],'method':'r101_required_game_slot','pending_selection':{'candidate_ids':games,'subject_kind':'game','allow_all':False}},[],response='clarification')
                    response='clarification'
        # A source gap/expiry is not an interpretation failure. Semantic work
        # is reserved for absent or unresolved interpretations only.
        if result is None:
            from app.booking.live_status import is_live_booking_question
            if is_live_booking_question(question):
                # The dispatcher owns the existing read-only live fallback
                # when no common binding resolved. Static FAQ retrieval must
                # never steal a recognized live predicate.
                ctx.audits.append({'stage':'whole_request_plan','attempted':False,'reason':'recognized_live_predicate_reserved_for_provider'})
                return None
        retry_semantic=result is None or (response=='clarification' and not any((result.decision_artifact.get('query_plan') or {}).get(k) for k in ('profile_confirmation','pending_target','pending_selection','price_scope_request','r98_pending_context')))
        if result is not None and 'unresolved_query_clause' in result.validation.errors:
            # A sourced excerpt does not mean every input clause was understood.
            # Spend the shared whole-request model quota to repair interpretation.
            retry_semantic=True
        if result is not None and any(o.get('status')=='unsupported_scope' for o in (result.decision_artifact or {}).get('obligations',[])):
            retry_semantic=True
        if result is not None:
            qp=(result.decision_artifact or {}).get('query_plan') or {}
            if qp.get('bridge_status') or qp.get('date_required') or any(r.get('status')=='needs_user_slot' for r in (result.decision_artifact or {}).get('need_results',[])):
                # An accepted typed request with a missing slot, catalog item
                # or package is not an NLU failure to retry with a model.
                retry_semantic=False
        if planner is not None and retry_semantic:
            from .grounded_plan import propose
            roots=list(need.record_ids)
            if not roots and re.search(r'เกมนี้|อันนี้|\b(?:it|that|this game)\b',question,re.I):
                from .followup_scope import delivered_state
                state=delivered_state(history) or {}
                roots=[k for k in state.get('record_ids',[]) if k in records and records[k]['kind'] in {'game','service','resource','equipment_model','competition'}]
            semantic=propose(question,records,names,roots)
            if semantic:
                outputs=[execute(reader,n,snap,at,lang) for n in semantic.needs]
                if any(outputs):
                    plan=semantic
                    from .request_plan import RequestPlan
                    certified=[certify(attach(r,RequestPlan(plan.version,n.query,[n],plan.scope),snap),RequestPlan(plan.version,n.query,[n],plan.scope),snap,at) if r else None for n,r in zip(plan.needs,outputs)]
                    result=certified[0] if len(certified)==1 else aggregate(reader,snap,time.perf_counter(),plan,certified,lang)
            if ctx.audits and ctx.audits[-1].get('reason') in {'model_transport_failure','model_schema_failure','model_busy','model_admission','deadline'} and (result is None or not any(o.get('status')=='known' for o in (result.decision_artifact or {}).get('obligations',[]))):
                body='ระบบตีความคำถามไม่พร้อมชั่วคราว กรุณาลองอีกครั้งครับ' if lang=='th' else 'Question interpretation is temporarily unavailable. Please retry.'
                result=reader.finish(snap,time.perf_counter(),body,[],{'record_ids':[],'requested_fields':[],'method':'r101_model_unavailable'},[],response='unavailable')
        if result is not None:
            # Rebind to the accepted plan instead of reconstructing needs from
            # response fields. Preserve explicit target/follow-up repair plans.
            art=result.decision_artifact or {}
            old=art.get('request_plan',{})
            if old.get('needs') and not plan.scope.get('semantic'):
                from .request_plan import RequestPlan,Need
                try:plan=RequestPlan(old['version'],old['question'],[Need(**n) for n in old['needs']],old['scope'])
                except (KeyError,TypeError):pass
            elif plan.scope.get('semantic'):
                art={k:v for k,v in art.items() if k not in {'request_plan','need_results'}};result=replace(result,decision_artifact=art)
            from .zone_projection import apply as project_zones
            if len(plan.needs)==1:result=project_zones(result,plan.needs[0],snap,at,lang,reader.store)
            from .gap_explanations import refine
            result=refine(result,plan,snap,lang)
            result=attach(result,plan,snap)
            return certify(result,plan,snap,at)
        if need.task=='equipment_list':
            body='ยังไม่มีรายการอุปกรณ์ที่ยืนยันครบสำหรับขอบเขตที่ถามครับ' if lang=='th' else 'A complete equipment inventory is not confirmed for the requested scope.'
            return certify(attach(reader.finish(snap,time.perf_counter(),body,[],{'record_ids':[],'requested_fields':[],'method':'r103_inventory_scope_unknown'},[],response='unconfirmed'),plan,snap),plan,snap,at)
        return None


def answer(reader,question,**kwargs):
    from .flow_audit import finish
    from .response_locale import requested_output
    target_locale=requested_output(question)
    if target_locale:kwargs['locale']=target_locale
    with request_context() as ctx:
        if not ctx.input:ctx.input={'raw_question':question,'locale':kwargs.get('locale','th')}
        ctx.event('S00_receive',question=question,profile=type(reader.store).__name__)
        result=_answer(reader,question,**kwargs)
        ctx.event('S14_verify',result_present=result is not None)
        return finish(result)
