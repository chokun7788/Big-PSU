from pathlib import Path
R=Path(__file__).resolve().parent;D=R/'system/app/knowledge/common/domain_flow'
def edit(name,old,new):
 p=D/name;s=p.read_text('utf8');assert old in s,(name,old[:80]);p.write_text(s.replace(old,new,1),'utf8')
edit('native_intents.py',r'\s+and\s+(?=(?:what|how|which|can|is|when)\b)',r'\s+(?:and|ans|adn)\s+(?=(?:what|how|which|can|is|when)\b)')
edit('native_intents.py',"    if re.search(r'และ.*(?:ราคา|เปิด)|", "    if re.search(r'ปุ่ม|buttons?|controls?',q,re.I) and re.search(r'ราคา|price|cost',q,re.I):return None\n    if re.search(r'และ.*(?:ราคา|เปิด)|")
edit('native_intents.py',r'มีของอะไร.*(?:เตรียม|ให้ใช้)|what equipment',r'มีของอะไร.*(?:เตรียม|ให้ใช้)|มีอะไรให้ใช้|what equipment')
edit('native_intents.py',"MeaningTask(question,'reservation','C08','detail','owner_policy')],True,'canonical_checkin_documents'", "MeaningTask(question,'reservation','C08','detail','owner_policy',canonical_operation='policy.checkin_documents')],True,'canonical_checkin_documents'")
edit('vocabulary.py',r'(?:can|may|must).{0,20}(?:eat|drink)',r'\b(?:can|may|must)\b.{0,20}\b(?:eat|drink)\b')
edit('vocabulary.py',r'(?:eat|eating).{0,25}(?:area|desk|designated)',r'\b(?:eat|eating)\b.{0,25}\b(?:area|desk|designated)\b')
# A specific source-clause match precedes top-k selection, retaining dependency checks.
edit('readers.py',"    if labels:\n        top=max(n for n,_ in labels)", """    if not labels:
        from .source_operations import source_clause_terms
        direct=source_clause_terms(index,fieldq,pool)
        if direct:labels=[(1,f) for f in direct]
    if labels:
        top=max(n for n,_ in labels)""")
# Substantive questions cannot be answered with a section caption alone.
edit('obligation_verifier.py',"    if task.capability['operation']=='compare_durations' and claims:", """    if task.category=='C13' and claims and re.search(r'can|may|where|allowed|permitted|ได้ไหม|อนุญาต|ที่ไหน',question,re.I):
        substantive=any(re.sub(r'^\\d+[.)]\\s*','',c['value'].strip()).casefold()!=re.sub(r'^\\d+[.)]\\s*','',index.byid[c['fact_id']]['label'].get('en' if re.search('[a-z]',question,re.I) else 'th','').strip()).casefold() for c in claims)
        obligations.append({'id':task.id+':substantive','kind':'substantive_clause','fulfilled':substantive,'reason':None if substantive else 'substantive_clause_not_delivered','claim_refs':[c['fact_id'] for c in claims] if substantive else []})
    if task.capability['operation']=='compare_durations' and claims:""")
edit('task_execution.py',"'requested_field_not_delivered' in ledger['reason_codes']", "any(reason in ledger['reason_codes'] for reason in ['requested_field_not_delivered','substantive_clause_not_delivered'])")
# Clarify varying policy texts rather than allowing the model to choose source authority.
edit('readers.py',"    if len(candidates)==1:return confirmed(cat,candidates,'action_condition_policy',policy_intents=list(names))", """    if len(candidates)==1:return confirmed(cat,candidates,'action_condition_policy',policy_intents=list(names))
    if len(intents)==1 and candidates:
        result=confirmed(cat,candidates,'policy_source_scope_or_revision_conflict',policy_intents=[intents[0][0]],authority_conflict=True)
        result.status='partial';result.locked=True;return result""")
edit('engine.py',"        if category=='C02' and selected:", """        if plan.metadata.get('authority_conflict'):
            blocks.insert(0,'มีข้อความนโยบายหลายฉบับที่ยังไม่ยืนยันขอบเขตหรือฉบับที่ใช้แทนกัน กรุณาตรวจสอบกับศูนย์ก่อนใช้เงื่อนไขที่ต่างกัน' if lang=='th' else 'Policy sources have differing wording or scope without a confirmed superseding version. Please confirm the differing conditions with the studio.')
        if category=='C02' and selected:""")
# Backend output remains escaped text in table cells; do not inject HTML line breaks.
edit('customer_render.py',".replace('\\n','<br>')", ".replace('\\n','; ')")
print('Broader regression findings patched')
