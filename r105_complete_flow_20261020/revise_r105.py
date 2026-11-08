from pathlib import Path
R=Path(__file__).resolve().parent;C=R/'system/app/knowledge/common'
def edit(name,old,new):
 p=C/name;s=p.read_text('utf8');assert old in s,(name,old[:60]);p.write_text(s.replace(old,new),'utf8')
edit('interpret_surface.py',"|please be brief)[.!?\\s]*$','',q)","|please be brief)[.!?\\s]*$','',q,flags=re.I)")
# Reuse the mature material-context reader before domain-specific execution.
edit('complete_flow.py',"        result=target_answer(reader,question,snap,records,names,lang,history,at,planner)\n        from .catalog_reader", "        result=target_answer(reader,question,snap,records,names,lang,history,at,planner)\n        if result is None:\n            from .qualified_tasks import answer as qualified_context\n            result=qualified_context(reader,question,snap,records,names,lang,history,at)\n        from .catalog_reader")
# An accepted task is not replaced by another task derived from a title keyword.
edit('complete_flow.py',"if task and TASKS[task].operation not in", "if task and need.task in {'unresolved',task} and TASKS[task].operation not in")
edit('complete_flow.py',"if task and _compatible_remainder(question,need.record_ids,records,names,task,basis):", "if task and need.task in {'unresolved',task} and _compatible_remainder(question,need.record_ids,records,names,task,basis):")
edit('complete_flow.py',"(need.task=='game_version' or need.task=='procedure'", "(need.task in {'game_version','game_account'} or need.task=='procedure'")
# Typed source kinds bind the meaning of generic field requests.
edit('intent_contracts.py',"if kinds=={'center'} and re.search(r'เล่า|เกี่ยวกับ|", "if kinds=={'center'} and re.search(r'แนะนำ|เล่า|เกี่ยวกับ|")
edit('intent_contracts.py',"    booking_required=bool(","    if 'game' in kinds and re.search(r'บัญชี|\\baccounts?\\b',q) and not re.search(r'แข่ง|\\b(?:competition|tournament)\\b',q):task='game_account'\n    if 'facility' in kinds and re.search(r'ที่ไหน|อยู่ตรงไหน|เงื่อนไข|\\b(?:where|location|conditions)\\b',q):task='facility'\n    if 'news' in kinds and re.search(r'ประกาศ|รายละเอียด|\\b(?:announcement|news|details)\\b',q):task='news'\n    if re.search(r'ชื่อรุ่นกติกา|รุ่นกติกา|ฉบับกติกา|\\brulebook release\\b',q):task='competition_metadata'\n    booking_required=bool(")
# Recognized missing detailed rule must not fall through to every other clause.
edit('rules_reader.py',"        else:return None\n    chosen=list(dict.fromkeys(chosen))", "        else:return _gap(reader,snap,lang,'missing_source')\n    chosen=list(dict.fromkeys(chosen))")
# Restore C07's original domain-context oracle. The earlier phase interpretation
# was incorrect: the actual precondition distinguishes ordinary vs tournament play.
p=R/'acceptance_cases.py';s=p.read_text('utf8');s=s.replace("elif cid=='C07':check('complete source clause answers without invented phase slot',has(r,'RULE_EXCEPTION') and hit(r,'fx_rule'))", "elif cid=='C07':check('material context question',a.get('response_type')=='clarification' and not has(r,'RULE_EXCEPTION'))");p.write_text(s,'utf8')
# A caller that selected a competition context is already interpreted. Preserve
# that task rather than re-parsing its bare context word as an uncovered clause.
edit('qualified_tasks.py',"'game_scope':ids,'clause_selection'", "'game_scope':ids,'semantic_plan_accepted':True,'task_plan':{'task':'competition_rules','predicate':'rule_clause'},'clause_selection'")
print('R105 final grouped corrections applied; no behavioral tests run')
