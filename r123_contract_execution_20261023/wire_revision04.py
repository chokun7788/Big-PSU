"""Wire revision04 only, with exact assertions against the frozen parent code."""
import ast
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'revision04_system';C=S/'app/knowledge/common';D=C/'domain_flow'
def change(p,old,new):
 x=p.read_text('utf8');assert old in x,(p,old[:100]);x=x.replace(old,new);ast.parse(x);p.write_text(x,'utf8')
change(D/'task_execution.py',"def execute(engine,question,locale='auto',category=None,at=None,allow_llm=True,history=None,budget=None,understanding=None):",'''def execute(engine,question,locale='auto',category=None,at=None,allow_llm=True,history=None,budget=None,understanding=None):
    from .request_provenance import capture,attach_compiled
    result=_execute(engine,question,locale,category,at,allow_llm,history,budget,understanding)
    attach_compiled(result['execution_contract'],capture(question,history))
    return result

def _execute(engine,question,locale='auto',category=None,at=None,allow_llm=True,history=None,budget=None,understanding=None):''')
change(D/'task_execution.py',"if category is not None or history:","if category is not None:")
change(D/'task_execution.py',"'path':'trusted_history_compatibility' if history else 'explicit_category_compatibility'","'path':'explicit_category_compatibility'")
change(D/'integration.py',"    with request_context():return _answer(reader,question,**kwargs)",'''    with request_context():
        result=_answer(reader,question,**kwargs)
        if result is None:return None
        from .request_provenance import capture,attach_compiled
        from .native_contract import invalidate
        art=dict(result.decision_artifact or {})
        c=art.get('execution_contract') or {'version':'r123','path':'native_unaccepted_wire_compatibility','whole_question_semantics_verified':False}
        if 'request_context' not in c:attach_compiled(c,capture(question,kwargs.get('history')))
        if art.get('response_type')=='retry':c=invalidate(c)
        art['execution_contract']=c
        return replace(result,decision_artifact=art)''')
change(D/'integration.py',"    if resumed:question=resumed",'''    if resumed:
        from .request_provenance import derived_input
        from ..followup_scope import delivered_state
        pending=(delivered_state(history) or {}).get('r114_pending',{})
        origin=pending.get('query','')
        derived_input(resumed,'delivered_financial_resume',[
            {'origin':'delivered_pending_query','start':0,'end':len(origin),'text':origin},
            {'origin':'current_user_reply','start':len(origin)+1,'end':len(origin)+1+len(question),'text':question},
            *([{'origin':'native_billing_period_rule','text':'per session'}] if resumed!=origin+' '+question else [])],
            source_state_slot=pending.get('slot'),facts_inherited=False)
        question=resumed''')
change(D/'integration.py',"    if understanding.accepted:question=interpretation_question\n    parts=",'''    compiled=None
    if understanding.accepted:
        question=interpretation_question
        from .native_contract import prepare
        try:understanding,compiled=prepare(question,understanding,engine,at)
        except ValueError:
            # The engine owns the bounded invalid-plan response. Never send a
            # malformed accepted plan to an unguarded provider adapter.
            return package(reader,snap,started,question,engine.answer(question,locale,at=at,allow_llm=False,budget=budget,understanding=understanding))
    parts=''')
change(D/'integration.py',"            child=answer(reader,part,locale=locale,history=history,at=at,planner=planner,_composing=True,_snapshot=snap,_budget=budget,\n                         _understanding=understanding.child(i-1) if understanding.accepted else understanding)",'''            child_q=part;child_understanding=understanding.child(i-1) if understanding.accepted else understanding
            if compiled is not None:
                from .native_contract import scoped_question
                from .request_provenance import derived_input
                from .understanding import Understanding
                task=compiled.tasks[i-1]
                if task.errors or task.ambiguities or task.capability['status']=='unsupported_operation':
                    # Native special paths must not bypass the compiler's
                    # missing-input/capability gate.
                    from .contracts import Plan
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
                child=answer(reader,child_q,locale=locale,history=history,at=at,planner=planner,_composing=True,_snapshot=snap,_budget=budget,_understanding=child_understanding)''')
change(D/'integration.py',"        if art.get('response_type')=='retry':",'''        if compiled is not None:
            from .native_contract import aggregate_contract
            art['execution_contract']=aggregate_contract(compiled,outputs)
        if art.get('response_type')=='retry':''')
# Above exact text occurs in both wrapper and compound? Wrapper uses a one-line
# condition, so only the compound branch is replaced.
change(D/'integration.py',"    special=None",'''    if compiled is not None and len(parts)==1:
        task=compiled.tasks[0]
        if task.errors or task.ambiguities or task.capability['status']=='unsupported_operation':
            return package(reader,snap,started,question,engine.answer(question,locale,at=at,allow_llm=False,budget=budget,understanding=understanding))
    special=None''')
change(D/'integration.py',"        return replace(special,decision_artifact=art)",'''        special=replace(special,decision_artifact=art)
        if compiled is not None:
            from .native_contract import attach_native
            special=attach_native(reader,special,snap,compiled,at,language)
        return special''')
# Keep request-clock injection backwards compatible with all legacy callers.
change(S/'app/booking/live_status.py',"def resolve_live_target_date(query: str) -> str:","def resolve_live_target_date(query: str, *, reference_date: date | None = None) -> str:")
change(S/'app/booking/live_status.py',"    today = today_bangkok()\n    if \"yesterday\"", "    today = reference_date if reference_date is not None else today_bangkok()\n    if \"yesterday\"")
change(C/'live_reader.py',"    day=resolve_live_target_date(need.query);ctx=CURRENT.get();cache_key=('wordpress_booking',str(day))",'''    from zoneinfo import ZoneInfo
    day=resolve_live_target_date(need.query,reference_date=at.astimezone(ZoneInfo('Asia/Bangkok')).date());ctx=CURRENT.get();cache_key=('wordpress_booking',str(day))''')
# The dispatcher can discover a newer snapshot after any domain adapter has
# returned. Invalidate the nested R123 delivery receipts at that boundary too.
change(S/'app/pipeline/migrated_chat.py',"    art['need_results']=[{**r,'status':'temporary_failure','reason_codes':['snapshot_changed_before_delivery'],'receipts':[]} for r in art.get('need_results',[])]",'''    art['need_results']=[{**r,'status':'temporary_failure','reason_codes':['snapshot_changed_before_delivery'],'receipts':[],'claim_packets':[],
     'coverage':{**r.get('coverage',{}),'receipts':[]},'execution_contract':{}} for r in art.get('need_results',[])]
    if art.get('execution_contract'):
     from app.knowledge.common.domain_flow.native_contract import invalidate
     art['execution_contract']=invalidate(art['execution_contract'])''')
for old,new in [('verify_foundation03.py','verify_foundation04.py'),('verify_packaging03.py','verify_packaging04.py')]:
 x=(R/old).read_text('utf8').replace('revision03_system','revision04_system');ast.parse(x);(R/new).write_text(x,'utf8')
print('Revision04 wiring complete')
