from pathlib import Path
B=Path(__file__).resolve().parent/'r66_common_repair_20261014';S=B/'system'
def patch(path,old,new):
 p=S/path;t=p.read_text(encoding='utf-8');assert t.count(old)==1,(path,t.count(old),old[:60]);p.write_text(t.replace(old,new),encoding='utf-8')
patch('app/knowledge/common/answer.py',"        names=scoped_names(snap)\n        q,ids,method=context_query", "        names=derived_names(scoped_names(snap),records)\n        q,ids,method=context_query")
# A supported rule facet is a real interpretation, not a leftover clause.
patch('app/knowledge/common/answer.py',"        plan['unresolved_clauses']=gaps if review and not broad and not overview else []", "        if query_operation=='rules' and plan.get('rule_content_all') is not None:\n            review=False;gaps=[]\n        plan['unresolved_clauses']=gaps if review and not broad and not overview else []")
patch('app/knowledge/common/answer.py',"                if not related:blocks.append('No confirmed price in this scope.' if lang=='en' else 'ยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้')", "                if not related:\n                    blocks.append(('No confirmed price for ' if lang=='en' else 'ยังไม่มีราคายืนยันสำหรับ ')+title(r,lang))\n                    obligations.append({'record_id':rid,'field':'amount_minor','status':'unknown','evidence_refs':[],'reason':'missing_declared_rate_in_scope'})")
# Expose content fields, never force unrequested unknown metadata into answers.
patch('app/knowledge/common/semantics.py',"            if key in fields and key not in keys:keys.append(key);basis[key]='necessary_context'", "            if key in fields and key not in keys and fields[key]['status'] not in {'unknown','not_applicable'}:keys.append(key);basis[key]='necessary_context'")
print('name/scope/coverage fixes')
