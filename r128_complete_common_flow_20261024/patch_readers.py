from pathlib import Path
R=Path(__file__).resolve().parent;D=R/'system/app/knowledge/common/domain_flow'
def edit(path,old,new):
 s=path.read_text('utf8');assert old in s,(path,old[:90]);path.write_text(s.replace(old,new,1),'utf8')
edit(D/'integration.py',"'explicit_offered_game_catalog_request'}:","'explicit_offered_game_catalog_request','canonical_source_operation'}:")
edit(D/'engine.py',"return [f for _,f in self.index.rank(category,question,pool=pool,limit=8)]", "return [f for _,f in self.index.rank(category,question,pool=pool,limit=24)]")
edit(D/'model.py',"candidates=t['facts'][:8]", "candidates=t['facts'][:24]")
edit(D/'model.py',"'format':output_schema(len(tasks),8)", "'format':output_schema(len(tasks),24)")
web=R/'system/app/web_api/server.py'
edit(web,"            if metadata.get('common_approved') is not True:\n                continue", "            if metadata.get('common_approved') is not True and metadata.get('content_view') not in {'evaluation_draft','synthetic_demo'}:\n                continue")
edit(web,"source_id = str(metadata.get('title') or 'Approved center information')", "source_id = str(metadata.get('title') or ('Draft center information' if metadata.get('content_view')=='evaluation_draft' else 'Approved center information'))")
# Cross-record audience overlap: resolve maximal spans once across all groups.
p=D/'financial.py';s=p.read_text('utf8');a=s.index('    for rid,r in index.records.items():',s.index('def audience_mentions'));b=s.index('    return positive-negative,negative',a)
s=s[:a]+'''    observed=[]
    for rid,r in index.records.items():
        if r['kind']!='audience':continue
        for label in set(norm(s) for s in _labels(r)):
            if label and contains(q,label):
                observed.extend((m.start(),m.end(),rid) for m in re.finditer(re.escape(label),q))
    observed=[(a,b,rid) for a,b,rid in observed if not any(c<=a and b<=d and d-c>b-a for c,d,_ in observed)]
    for start,end,rid in observed:
        before=q[max(0,start-28):start]
        if re.search(r'(?:ไม่ใช่|ไม่ได้เป็น|not(?: an?| a)?)\\s*$',before):negative.add(rid)
        else:positive.add(rid)
'''+s[b:];p.write_text(s,'utf8')
edit(p,"        if len(selected)!=1:missing.append(title(r));continue", """        if len(selected)>1:
            def rate_signature(f):
                rate=records[f['record_id']];service=records.get(value(rate,'service_id'),{})
                return (value(service,'platform'),f.get('numeric'),value(rate,'duration_minutes'),f.get('billing_unit'),f.get('calculation_rule'),str(rate.get('validity')),f.get('confirmation_as_of'))
            if len({rate_signature(f) for f in selected})==1:selected=[sorted(selected,key=lambda f:f['id'])[0]]
        if len(selected)!=1:missing.append(title(r));continue""")
# Recognized booking semantics survive wording changes at the actual reader boundary.
edit(D/'vocabulary.py',"r'จอง.*(?:ทำยังไง|อย่างไร|ยังไง)|วิธีจอง|ขั้นตอน.*จอง|how (?:can|do|should) (?:i|we) (?:book|reserve)'", "r'จอง.*(?:ทำยังไง|อย่างไร|ยังไง)|วิธีจอง|ขั้นตอน.*จอง|เข้าไปเล่น.*เริ่ม|how.*(?:start|begin).*(?:play|visit)|how (?:to|(?:can|do|should) (?:i|we)) (?:book|reserve)'")
# Canonical source procedures require equivalent ordered actions and no distinct condition.
edit(D/'readers.py',"        result=confirmed(cat,list(variants.values()),'recorded_booking_procedure_variants'", """        from .source_operations import equivalent_procedure
        canonical=equivalent_procedure(list(variants.values()))
        if canonical:
            result=confirmed(cat,[canonical],'canonical_equivalent_procedure',policy_intents=['booking_steps'],corroborating_fact_ids=[f['id'] for f in candidates],procedure_steps=True)
            result.locked=True;return result
        result=confirmed(cat,list(variants.values()),'recorded_booking_procedure_variants'""")
edit(D/'precision.py',"    if not wanted:return None", """    if not wanted:
        from .source_operations import control_action
        return control_action(index,q,pool)""")
edit(D/'distilled_policy.py'," if re.search(r'ถ้า|กรณี|\\bif\\b|\\bwhen\\b|โกง|cheat|pause|บั๊ก|\\bbug\\b',question,re.I):return None", " if re.search(r'โกง|cheat|pause|บั๊ก|\\bbug\\b|disconnect|หลุด|มาสาย',question,re.I):return None")
# Never emit source-backed claims for the wrong requested field after a failed obligation.
edit(D/'task_execution.py',"        elif ledger['terminal_state']=='partial' and result['status']=='answer':", """        elif result['claims'] and 'requested_field_not_delivered' in ledger['reason_codes']:
            p=blocked(cat,'requested_operation_not_satisfied');result=engine._render_one(cat,q,locale,p,at)
        elif ledger['terminal_state']=='partial' and result['status']=='answer':""")
print('Reader patches complete')
