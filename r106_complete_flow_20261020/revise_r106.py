from pathlib import Path
R=Path(__file__).resolve().parent;C=R/'system/app/knowledge/common'
def edit(name,old,new):
 p=C/name;s=p.read_text('utf8');assert old in s,(name,old[:60]);p.write_text(s.replace(old,new),'utf8')
# Resolve the source actor/service intersection before checking supersession.
p=C/'complete_flow.py';s=p.read_text('utf8');start=s.index('        from .claim_bindings import current_claims\n        overrides=');end=s.index('        from .financial_scope',start);block=s[start:end];s=s[:start]+s[end:];anchor="        if not targets:return None\n        graph,_,_=compile(task,targets,records,fields=fields,predicate=need.predicate)";assert anchor in s;s=s.replace(anchor,"        if not targets:return None\n"+block+"        graph,_,_=compile(task,targets,records,fields=fields,predicate=need.predicate)");p.write_text(s,'utf8')
# Kind-aware field intent: generic equipment/count cues are not complete tasks.
edit('intent_contracts.py',"    booking_required=bool(","    if 'equipment_model' in kinds and task in {'equipment_list','unresolved','equipment_explain'}:\n        if re.search(r'สเปก|\\b(?:specs?|specifications?)\\b',q):task='equipment_specs'\n        elif re.search(r'คืออุปกรณ์อะไร|อุปกรณ์อะไร|\\b(?:what is|explain|describe)\\b',q):task='equipment_explain'\n    if task=='game_players' and kinds & {'resource','service'} and 'game' not in kinds:task='resource_capacity'\n    booking_required=bool(")
# A newly added ordinary-play FAQ must be discoverable after context selection.
edit('qualified_tasks.py',"    if phase=='general_play':\n        body=", "    if phase=='general_play':\n        from .answer import effective\n        matches=[]\n        for k,r in records.items():\n            profile=value(r,'query_profile') or {}\n            if r['kind']!='faq' or profile.get('task')!='correction' or profile.get('context')!='studio':continue\n            if not set(ids).intersection(value(r,'related_ids') or []) or not effective(r,at,records):continue\n            subjects=str(profile.get('subjects') or [])\n            if re.search(r'เกมหลุด|หลุดจากเกม|disconnect',subjects,re.I):matches.append(k)\n        if len(matches)==1:\n            return reader.execute_task(question,snap=snap,at=at,lang=lang,plan={'record_ids':matches,'scope_ids':ids,'requested_fields':['answer'],'operation':'read','method':'r106_source_normal_play_disconnection','semantic_plan_accepted':True,'unresolved_clauses':[],'task_plan':{'task':'faq_content','predicate':'normal_play_disconnection'}})\n        if len(matches)>1:\n            return reader.finish(snap,started,('มีขั้นตอนที่ตรงกันหลายรายการ กรุณาระบุรายการ: ' if lang=='th' else 'Several matching procedures are recorded. Please specify one: ')+', '.join(title(records[k],lang) for k in matches),[],{'record_ids':[],'requested_fields':[],'method':'r106_normal_play_source_selection'},[],response='clarification')\n        body=")
# Full-source references can be useful with unknown coverage metadata. They
# remain explicit excerpts; never turn a truncated decision into permission.
edit('rules_reader.py',"    chosen=[];method=None", "    chosen=[];method=None") if '    chosen=[];method=None' in (C/'rules_reader.py').read_text('utf8') else None
edit('rules_reader.py',"    if not chosen:\n        # Reuse the old proposition", "    reference_only=False\n    if not chosen:\n        # Reuse the old proposition")
edit('rules_reader.py',"        if not residue:chosen=children", "        if not residue:chosen=children;reference_only=True")
edit('rules_reader.py',"        if value(r,'completeness')!='complete':return _gap(reader,snap,lang,'missing_source')", "        if value(r,'completeness')!='complete' and not reference_only:return _gap(reader,snap,lang,'missing_source')")
edit('rules_reader.py',"    return render(reader,snap,[(k,['competition_id','heading','text','completeness','depends_on_ids']) for k in chosen],lang,", "    incomplete=[k for k in chosen if value(records[k],'completeness')!='complete']\n    caption=('กติกาตามเอกสาร — ' if lang=='th' else 'Rulebook — ')+title(records[event],lang)\n    if incomplete:caption+=('\\nแสดงข้อความข้อกติกาที่มีในชุดข้อมูล ยังไม่ยืนยันว่าเอกสารครบทุกข้อ' if lang=='th' else '\\nAvailable source clauses only; completeness of the full rulebook is not confirmed.')\n    return render(reader,snap,[(k,['competition_id','heading','text','completeness','depends_on_ids']) for k in chosen],lang,")
edit('rules_reader.py',"'dependency_closure':chosen,'scope_ids':[event]},caption=('กติกาตามเอกสาร — ' if lang=='th' else 'Rulebook — ')+title(records[event],lang))", "'dependency_closure':chosen,'scope_ids':[event],'complete_rulebook_confirmed':not incomplete,'scope_receipt':{'member_ids':chosen,'total_members':len(chosen),'returned_members':len(chosen),'complete_rulebook_confirmed':not incomplete,'enumeration':'exhaustive_selected_source_records'}},caption=caption,response='partial_answer' if incomplete else 'answer')")
# Regression tests are source-backed and run together in the final grouped gate.
p=R/'test_r102_contracts.py';s=p.read_text('utf8');anchor="check('explicit scoped authority can resolve declared supersession',not conflicts(['fx_rate'],snap(),AT))";assert anchor in s
s=s.replace(anchor,anchor+"\nstaff=f.ask('PC price for PSU staff, not External Visitors',llm=False)\ncheck('superseded external price does not block independent staff rate',staff is not None and '50.00' in staff.answer and any(h.get('record_id')=='fx_staff_rate' for h in staff.hits),dataclasses.asdict(staff) if staff else None)")
anchor="summary={'count':len(checks)";assert anchor in s
extra="""# Data growth after a material-context question: no rule may leak into normal play.
question='ROV what should I do if I disconnect?';first=f.ask(question,llm=False)
before=f.ask('general play',history=f.history(question,first),llm=False)
check('ordinary-play gap does not quote competition policy',before is not None and 'RULE_EXCEPTION' not in before.answer)
f.new('faq','fx_normal_disconnection',{'question':bi('ROV เล่นทั่วไปเกมหลุด','ROV ordinary play disconnection'),
 'answer':bi('ติดต่อผู้ดูแล NORMAL_PLAY_NEW_DATA','Contact staff NORMAL_PLAY_NEW_DATA'),'topic':'disconnection','related_ids':['fx_rov'],
 'query_profile':{'task':'correction','subjects':[bi('เกมหลุด','disconnection')],'ownership':'any','context':'studio'}})
after=f.ask('general play',history=f.history(question,first),llm=False)
check('owner-added ordinary-play FAQ is answered without code aliases',after is not None and 'NORMAL_PLAY_NEW_DATA' in after.answer and 'RULE_EXCEPTION' not in after.answer,dataclasses.asdict(after) if after else None)
rr=f.store.get('fx_rule')['record'];rr['fields']['completeness'].update(status='unknown',value=None,evidence_refs=[]);f.save(rr)
reference=f.ask('All ROV competition rules',llm=False)
check('available rule text survives unknown completeness as explicit partial reference',reference is not None and 'RULE_EXCEPTION' in reference.answer and reference.decision_artifact.get('response_type')=='partial_answer' and reference.decision_artifact.get('query_plan',{}).get('complete_rulebook_confirmed') is False,dataclasses.asdict(reference) if reference else None)
"""
s=s.replace(anchor,extra+anchor);p.write_text(s,'utf8')
print('R106 scoped update, data growth and complete-source-reference fixes applied')
