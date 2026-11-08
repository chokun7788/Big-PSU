"""Wire the complete R102 contracts before any behavioral test is started."""
from pathlib import Path
R=Path(__file__).resolve().parent/'system/app/knowledge/common'
def edit(name,old,new):
 p=R/name;t=p.read_text('utf8')
 if t.count(old)!=1:raise ValueError((name,old[:80],t.count(old)))
 p.write_text(t.replace(old,new),'utf8')
edit('flow_context.py',"    snapshot:dict=field(default_factory=dict)","    snapshot:dict=field(default_factory=dict)\n    events:list=field(default_factory=list)\n    input:dict=field(default_factory=dict)\n    def event(self,stage,**detail):\n        if len(self.events)<400:self.events.append({'stage':stage,'elapsed_ms':round((time.perf_counter()-self.started)*1000,3),**detail})")
edit('flow_context.py',"'budget':b.metadata() if b else {'global_timeout_enabled':False},'audits':self.audits}","'budget':b.metadata() if b else {'global_timeout_enabled':False},'audits':self.audits,'events':self.events,'input':self.input}")
edit('request_plan.py',"if any(task=='unresolved' or not re.search(request_cues,part,re.I) for task,part in zip(tasks,parts)):return []", "if any(not re.search(request_cues,part,re.I) for task,part in zip(tasks,parts)):return []")
edit('request_plan.py',"text='ยังไม่มีข้อมูลยืนยันสำหรับส่วนนี้' if lang=='th' else 'No confirmed source is available for this part.'\n            status='missing_source';rows=[];art={}","text=('ยังตีความส่วนนี้ไม่ชัด กรุณาระบุหัวข้อหรือรายการของส่วนนี้เพิ่มครับ' if lang=='th' else 'This part is not clear yet. Please specify its topic or item.') if need.task=='unresolved' else ('ยังไม่มีข้อมูลยืนยันสำหรับส่วนนี้' if lang=='th' else 'No confirmed source is available for this part.')\n            status='ambiguous_interpretation' if need.task=='unresolved' else 'missing_source';rows=[];art={}")
edit('grounded_plan.py',"if proposal['unresolved'] or not isinstance(proposal['unresolved'],list):return None,'unresolved'", "if not isinstance(proposal['unresolved'],list):return None,'invalid_unresolved'")
edit('grounded_plan.py',"    # Do not discard unknown clauses. All non-conjunction words must belong", "    for quote in proposal['unresolved']:\n        span=bind(question,quote)\n        if not span or any(span['start']<b and a<span['end'] for a,b in spans):return None,'invalid_unresolved_span'\n        result.append(Need('n'+str(len(result)+1),'unresolved',span['quote'],span['quote'],[],[],predicate='unresolved'))\n        spans.append((span['start'],span['end']))\n    if len(result)>8:return None,'invalid_need_count'\n    # Do not discard unknown clauses. All non-conjunction words must belong")
edit('grounded_plan.py',"        # An explicit game/device cannot be silently replaced by retrieval.","        # Confident domain constraints cannot become an unrelated FAQ.\n        from .intent_contracts import infer\n        from app.booking.live_status import is_live_booking_question\n        declared=infer(span['quote'])\n        if is_live_booking_question(span['quote']) and task!='live_status':return None,'live_predicate_mismatch'\n        if declared['task'] in {'price','rental','schedule','competition_rules'} and task!=declared['task']:return None,'explicit_task_mismatch'\n        # An explicit game/device cannot be silently replaced by retrieval.")
edit('complete_flow.py',"    if task not in TASKS or (not ids and task!='live_status'):return None", "    from .flow_audit import event\n    event('S07_compile',need_id=need.id,task=task,record_ids=ids)\n    if task not in TASKS or (not ids and task!='live_status'):return None")
edit('complete_flow.py',"    return reader.execute_task(need.query,snap=snap,at=at,lang=lang,plan=plan)", "    event('S08_read',need_id=need.id,task=task,record_ids=targets,fields=requested,relation_paths=edges)\n    return reader.execute_task(need.query,snap=snap,at=at,lang=lang,plan=plan)")
edit('claim_conflicts.py',"    return [{'predicate_key':key", "    typed=[{'predicate_key':key")
with (R/'claim_conflicts.py').open('a',encoding='utf8') as f:f.write("\n    from .claim_bindings import conflicts\n    return typed+conflicts(record_ids,snapshot,at)\n")
edit('complete_flow.py',"    conflicts=detect(read_ids,snap,at) if any(n.task in {'price','schedule'} for n in plan.needs) else []", "    conflicts=detect(read_ids,snap,at)\n    from .flow_audit import event\n    event('S10_evidence',record_ids=read_ids,conflict_count=len(conflicts))")
edit('complete_flow.py',"    # Compound children have already been certified before aggregation.", "    if art.get('mapped_claim_packets'):\n        art.update(request_plan=asdict(plan),claim_packets=art['mapped_claim_packets'],flow_contract={'version':'r101','revision':'r102','all_needs_executed':True,'mapping_receipts_verified':True})\n        return replace(result,decision_artifact=art)\n    # Compound children have already been certified before aggregation.")
edit('complete_flow.py',"def answer(reader,question,*,locale='th'", "def _answer(reader,question,*,locale='th'")
edit('complete_flow.py',"        if len(plan.needs)>1:\n            results=[answer(reader,n.query,locale=locale,history=history,at=at,planner=None,_composing=True,_snapshot=snap) for n in plan.needs]", """        ctx.event('S05_plan',needs=[{'id':n.id,'task':n.task,'subjects':n.record_ids,'qualifiers':n.qualifiers,'slots':n.slots} for n in plan.needs])
        if len(plan.needs)>1:
            if planner is not None and any(n.task=='unresolved' for n in plan.needs):
                from .grounded_plan import propose
                semantic=propose(question,records,names,list(dict.fromkeys(k for n in plan.needs for k in n.record_ids)))
                if semantic:plan=semantic
            results=[]
            for n in plan.needs:
                r=execute(reader,n,snap,at,lang) if plan.scope.get('semantic') and n.task in TASKS else None
                if r is None and n.task!='unresolved':r=answer(reader,n.query,locale=locale,history=history,at=at,planner=None,_composing=True,_snapshot=snap)
                if r is not None:
                    from .request_plan import RequestPlan
                    child_plan=RequestPlan(plan.version,n.query,[n],plan.scope)
                    r=certify(attach(r,child_plan,snap),child_plan,snap,at)
                results.append(r)""")
edit('complete_flow.py',"        result=None\n        if need.task=='live_status':", "        from .gap_explanations import direct\n        result=direct(reader,need,snap,at,lang)\n        if result is None:\n            from .policy_coverage import answer as cover_policy\n            result=cover_policy(reader,need,snap,at,lang)\n        if result is None and need.task=='live_status':")
edit('complete_flow.py',"            result=attach(result,plan,snap)\n            return certify(result,plan,snap,at)", "            from .gap_explanations import refine\n            result=refine(result,plan,snap,lang)\n            result=attach(result,plan,snap)\n            return certify(result,plan,snap,at)")
with (R/'complete_flow.py').open('a',encoding='utf8') as f:f.write('''

def answer(reader,question,**kwargs):
    from .flow_audit import finish
    with request_context() as ctx:
        if not ctx.input:ctx.input={'raw_question':question,'locale':kwargs.get('locale','th')}
        ctx.event('S00_receive',question=question,profile=type(reader.store).__name__)
        result=_answer(reader,question,**kwargs)
        ctx.event('S14_verify',result_present=result is not None)
        return finish(result)
''')
p=R.parents[1]/'pipeline/migrated_chat.py';t=p.read_text('utf8')
old="  return replace(result,hits=hits,language=locale,elapsed=time.perf_counter()-started,decision_artifact="
assert t.count(old)==1;t=t.replace(old,"  from app.knowledge.common.flow_audit import finish as finish_audit\n  result=replace(result,hits=hits,language=locale,elapsed=time.perf_counter()-started,decision_artifact=")
needle="  def message(" # actual nested function is one-space, use next def anchor
anchor=" def message(text,kind='clarification'):";assert t.count(anchor)==1
t=t.replace(anchor,"  return finish_audit(result)\n"+anchor);p.write_text(t,'utf8')
print('Shared planning, scoped coverage/gaps, mapped conflicts, per-need audit wired; behavioral tests not run')
