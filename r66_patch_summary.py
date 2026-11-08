from pathlib import Path
S=Path(__file__).resolve().parent/'r66_common_repair_20261014/system'
def patch(path,old,new):
 p=S/path;t=p.read_text(encoding='utf-8');assert t.count(old)==1,(path,t.count(old),old[:60]);p.write_text(t.replace(old,new),encoding='utf-8')
patch('app/knowledge/common/query_scope.py',"    if re.search(r'จอง|\\b(?:book|booking|reserve|reservation)\\b',q):return 'booking'", "    if re.search(r'จอง|จะเล่นต้องทำ(?:ไง|ยังไง|อย่างไร)|เข้า(?:ใช้บริการ|เล่น).*ต้องทำ|\\b(?:book|booking|reserve|reservation|start using the studio)\\b',q):return 'booking'")
patch('app/knowledge/common/query_scope.py',"    if not re.search(r'จอง|\\b(?:book|booking|reserve|reservation)\\b',q):return []", "    if not re.search(r'จอง|จะเล่นต้องทำ(?:ไง|ยังไง|อย่างไร)|เข้า(?:ใช้บริการ|เล่น).*ต้องทำ|\\b(?:book|booking|reserve|reservation)\\b',q):return []")
patch('app/knowledge/common/query_scope.py',"        if r['kind']=='service':\n            p=value(r,'platform')", "        for key in ('title','name','event_name','display_name','question'):\n            v=value(r,key)\n            if isinstance(v,dict):out[rid].extend(s for s in v.values() if isinstance(s,str) and s)\n        if r['kind']=='service':\n            p=value(r,'platform')")
patch('app/knowledge/common/dialogue.py',"    if len(q)>400:return None", "    if len(q)>400:return None\n    if s.get('operation')=='booking' and re.search(r'สรุป|ทำ(?:ไง|ยังไง|อย่างไร)|\\b(?:summary|summarize|so how|then how|steps)\\b',q):\n        return {'record_ids':prior,'method':'typed_common_state','previous_fields':s['requested_fields']}")
patch('app/knowledge/common/answer.py',"        procedure_ids=operation_faqs(question,records,query_operation)","""        from .dialogue import previous_state
        prior_context=previous_state(history,records)
        procedure_query=question
        if query_operation is None and prior_context and prior_context.get('operation')=='booking' and re.search(r'สรุป|ทำ(?:ไง|ยังไง|อย่างไร)|\\b(?:summary|summarize|so how|then how|steps)\\b',normal(question)):
            query_operation='booking';procedure_query='booking steps'
            scope_ids=list(prior_context.get('scope_ids') or ids)
        procedure_ids=operation_faqs(procedure_query,records,query_operation)""")
print('typed booking summary inheritance and raw localized identities')
