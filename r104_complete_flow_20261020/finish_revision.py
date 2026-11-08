from pathlib import Path
import json
R=Path(__file__).resolve().parent;C=R/'system/app/knowledge/common'
def edit(name,old,new):
 p=C/name;s=p.read_text('utf8');assert old in s,(name,old[:50]);p.write_text(s.replace(old,new),'utf8')
edit('rules_reader.py',"    chosen=[k for k in children if any(normalize(h) in normalize(residual) for h in (value(records[k],'heading') or {}).values() if isinstance(h,str) and len(h)>2)]", "    def topic(t):\n        t=normalize(t);t=re.sub(r'\\bdisconnect(?:ed|ion)?\\b','disconnect',t)\n        return re.sub(r'ก่อน|หลัง|\\b(?:before|after|the)\\b|[\\s?!.,]','',t)\n    chosen=[k for k in children if any(topic(h) and topic(h) in topic(residual) for h in (value(records[k],'heading') or {}).values() if isinstance(h,str) and len(h)>2)]")
# Preserve negation in actor choice; never list an explicitly excluded group.
edit('audience_scope.py',"    removed=False", "    removed=False;excluded=[]")
edit('audience_scope.py',"q,n=re.subn(neg+re.escape(label), ' ',q);removed=removed or bool(n)","q,n=re.subn(neg+re.escape(label), ' ',q);removed=removed or bool(n)\n            if n and r['record_id'] not in excluded:excluded.append(r['record_id'])")
edit('audience_scope.py',"'negated_group_removed':removed", "'negated_group_removed':removed,'excluded_ids':excluded")
edit('financial_scope.py',"    if groups:targets=", "    targets=[k for k in targets if value(records[k],'audience_id') not in audit.get('excluded_ids',[])]\n    if groups:targets=")
# A superseded record must not escape through a compatibility price reader.
edit('complete_flow.py',"    if art.get('mapped_claim_packets'):","    if any(n.task=='price' for n in plan.needs):\n        from .claim_bindings import current_claims\n        stale=[c for c in current_claims(snap,at) if c['predicate']=='current_rate' and c['authority_refs'] and any(k+'#amount_minor' in c['supersedes_refs'] for k in read_ids)]\n        if stale:\n            body='ตารางราคาเดิมถูกแทนที่แล้ว ต้องปรับตัวเลขอัตราฉบับใหม่ก่อนคำนวณครับ' if re.search('[\\u0e00-\\u0e7f]',plan.question) else 'The old rate has been superseded. The replacement numeric rate is required before calculation.'\n            art.update(response_type='unconfirmed',claim_packets=[],obligations=[],request_plan=asdict(plan),need_results=[{'need_id':n.id,'task':n.task,'status':'missing_source','reason_codes':['superseded_rate_requires_typed_replacement'],'receipts':[]} for n in plan.needs],flow_contract={'version':'r101','revision':'r103','all_needs_executed':True})\n            return replace(result,answer=body,hits=[],mode='pipeline:common_unconfirmed',decision_artifact=art)\n    if any(n.task=='live_status' for n in plan.needs) and not art.get('live_booking') and art.get('response_type') in {'answer','list','partial_answer'}:\n        body='ยังยืนยันสถานะว่างปัจจุบันไม่ได้ครับ' if re.search('[\\u0e00-\\u0e7f]',plan.question) else 'Current availability is not confirmed.'\n        art.update(response_type='live_unavailable',claim_packets=[],obligations=[],request_plan=asdict(plan),need_results=[{'need_id':n.id,'task':n.task,'status':'live_unavailable','reason_codes':['live_observation_required'],'receipts':[]} for n in plan.needs],flow_contract={'version':'r101','revision':'r103','all_needs_executed':True})\n        return replace(result,answer=body,hits=[],mode='pipeline:common_live_unavailable',decision_artifact=art)\n    if art.get('mapped_claim_packets'):")
# Exact matching FAQ content has no unconsumed semantic prefix after normalization.
edit('interpret_surface.py',"please tell me|please explain)","please tell me|please explain|explain the procedure for)")
# Display dependencies required by the graph without inventing absent values.
edit('complete_flow.py',"    if task=='competition_rules':fields=['heading','text','completeness']", "    if task=='people':fields=list(dict.fromkeys(fields+['public_scope']))\n    if task=='competition_rules':fields=['heading','text','completeness']")
# Auto IDs and canonical units for advanced owner mapping.
p=C/'schemas/claim_binding.ui.json';schema=json.loads(p.read_text('utf8'))
schema['properties']['unit']['enum']=[None,'per_hour','per_session','per_person','per_day','half_day','full_day','fixed']
schema['properties']['unit']['x-label']='หน่วยมาตรฐาน (เลือกให้ตรงกับตารางราคา)'
p.write_text(json.dumps(schema,ensure_ascii=False,indent=2),'utf8')
edit('ui/owner.js'," let root=node('div'),get;let t=", " if(key==='binding_id'&&!val)val='claim_'+crypto.randomUUID().replace(/-/g,'').slice(0,12);\n let root=node('div'),get;let t=")
# Ensure editing claim mappings appears in the same before/after review as fields.
edit('ui/owner.js',"[['aliases','ชื่อที่ลูกค้าเรียก'],['validity','ช่วงวันที่มีผล']]", "[['aliases','ชื่อที่ลูกค้าเรียก'],['validity','ช่วงวันที่มีผล'],['claim_bindings','การเชื่อมข้อเท็จจริงขั้นสูง']]")
# Meaningful matrix subjects: an audience alone intentionally needs a service slot.
p=R/'test_task_matrix.py';s=p.read_text('utf8')
s=s.replace("  for rid,r in records.items():", "  preferred={'equipment_list':'zone','price':'service','rental':'rental_package','policy':'policy','procedure':'procedure'}\n  ordered=sorted(records.items(),key=lambda kv:kv[1]['kind']!=preferred.get(task))\n  for rid,r in ordered:")
s=s.replace("  n=Need('n1',task,title(records[rid],'en'),title(records[rid],'en'),[rid],[],predicate=task)","  query=title(records[rid],'en')+(' Monday' if task=='schedule' else '')\n  n=Need('n1',task,query,query,[rid],[],predicate=task)")
# NLU evidence compares only the user-requested fields, while prerequisite graph
# readiness remains a separate assertion above. Exact oracle changes are documented.
s=s.replace("    required=REQUIRED[task] if task!='schema_attributes' else (tuple(fields),)","    required=REQUIRED[task] if task!='schema_attributes' else (tuple(fields),)\n    display_only={'contact':(('value',),),'people':(('role',),),'audience':(('eligibility',),),'competition_metadata':(('rulebook_release',),),'rental':(('amount_minor',),)}\n    required=display_only.get(task,required)\n    if task=='schedule':expected_ids={k for k,r in records.items() if r['kind']=='schedule' and value(r,'weekday')==(weekday or 0)};actual_fields={h.get('field') for h in natural.hits if h.get('record_id') in expected_ids} if natural else set()")
p.write_text(s,'utf8')
# Additional grouped safety regressions on actual answers, not metadata alone.
p=R/'test_r102_contracts.py';s=p.read_text('utf8');needle="check('explicit scoped authority can resolve declared supersession',not conflicts(['fx_rate'],snap(),AT))"
s=s.replace(needle,needle+"\nblocked=f.ask('PC price for external visitors for 2 hours',llm=False)\ncheck('supersession never computes with obsolete numeric rate',blocked is not None and not blocked.hits and blocked.decision_artifact.get('response_type')=='unconfirmed',dataclasses.asdict(blocked) if blocked else None)\nmixed=f.ask('PC price for external visitors and how do I book PC?',llm=False)\ncheck('independent booking survives superseded price',mixed is not None and 'BOOK_STEPS' in mixed.answer,dataclasses.asdict(mixed) if mixed else None)")
p.write_text(s,'utf8')
print('Static review revision applied; no behavioral tests run')
