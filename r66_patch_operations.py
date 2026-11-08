from pathlib import Path
B=Path(__file__).resolve().parent/'r66_common_repair_20261014';S=B/'system'
def patch(path,old,new):
 p=S/path;t=p.read_text(encoding='utf-8');assert t.count(old)==1,(path,t.count(old));p.write_text(t.replace(old,new),encoding='utf-8')
patch('app/knowledge/common/answer.py','rule_selection,derived_names','rule_selection,derived_names,operation_faqs,control_projection')
patch('app/knowledge/common/answer.py',"        scope_ids=list(ids)\n        if query_operation", "        scope_ids=list(ids)\n        procedure_ids=operation_faqs(question,records,query_operation)\n        if procedure_ids:\n            # Prefer the requested language when duplicate migrated textual rows exist.\n            localized=[rid for rid in procedure_ids if (value(records[rid],'answer') or {}).get(lang)]\n            ids=(localized or procedure_ids)[:1];method='common_procedure_topic';query_operation='booking'\n        if query_operation")
patch('app/knowledge/common/answer.py',"        if method=='published_semantic_candidates' and all(records[rid]['kind']=='faq' for rid in ids):requested=['answer','scope_note']", "        if method=='common_procedure_topic':requested=['answer'];broad=False\n        if method=='published_semantic_candidates' and all(records[rid]['kind']=='faq' for rid in ids):requested=['answer','scope_note']")
patch('app/knowledge/common/answer.py',"        if method=='published_semantic_candidates' and all(records[rid]['kind']=='faq' for rid in ids):plan['unresolved_clauses']=[]", "        if method in {'common_procedure_topic','published_semantic_candidates'} and all(records[rid]['kind']=='faq' for rid in ids):plan['unresolved_clauses']=[];review=False")
patch('app/knowledge/common/answer.py',"                    elif key=='bindings' and partial is not None:out=text(v,lang)", "                    elif key=='bindings' and partial is not None:\n                        out=control_projection(v,raw_query,lang) or text(v,lang)")
patch('app/knowledge/common/answer.py',"                platforms=", "                platforms=") if False else None
print('procedure and control action projection')
