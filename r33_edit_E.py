from pathlib import Path
import sys
P=Path(sys.argv[1]) if len(sys.argv)>1 else Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
f=P/'app/core/task_frame_recovery.py';s=f.read_text(encoding='utf-8')
s=s.replace('embers ember rice','house home good shark smote contact contacts opens opening closing roles holds categories groups embers ember rice')
needle='    tokens=list(_LATIN.finditer(text))';assert s.count(needle)==1
s=s.replace(needle,needle+'''
    protected_names=[(m.start(1),m.end(1)) for m in re.finditer(r"\\b(?:called|named)\\s+([^?!.]+)|\\b(?:Mr|Ms|Mrs|Dr)\\.?\\s+(.+?)(?=\\s+(?:hold|holds|old)\\b|[?]|$)",text,re.I) if m.group(1)]
    for m in re.finditer(r"\\b(?:Mr|Ms|Mrs|Dr)\\.?\\s+(.+?)(?=\\s+(?:hold|holds|old)\\b|[?]|$)",text,re.I):
        protected_names.append((m.start(1),m.end(1)))
''')
s=s.replace('        if word in _WORDS:continue','        if word in _WORDS or any(m.start()<end and m.end()>start for start,end in protected_names):continue')
needle="        if near('studio') and re.search(r'\\b(?:what|rules?|policy|inside|can|penalties|food|noise)\\b',low):\n            targets.extend(('studio','rules','policy','damage','smoke','food','sharp','object'))"
assert s.count(needle)==1
s=s.replace(needle,'''        if near('studio'):
            if re.search(r'\\b(?:the|studio|stduio|studoi)\\s+$',before):targets.extend(('rules','policy'))
            if re.search(r'\\b(?:penalties|responsibility|noise)\\b',low):targets.append('damage')
            if re.search(r'\\b(?:inside|smoking)\\b',low) and re.search(r'\\b(?:can|i|policy)\\b',low):targets.append('smoke')
            if re.search(r'\\b(?:drinks|noise)\\b',low) and re.search(r'\\b(?:for|about|bring)\\s+$',before):targets.append('food')
            if re.match(r'\\s+objects?\\b',after):targets.append('sharp')
            if re.search(r'\\bsharp\\s+$',before):targets.append('object')''')
needle="        if near('gaming') and re.search(r'\\b(?:used|what|where|equipment|studio)\\b',low):targets.extend(('mouse','chair','keyboard','monitor'))";assert s.count(needle)==1
s=s.replace(needle,'''        previous=tokens[tokens.index(m)-1].group().casefold() if tokens.index(m)>0 else ''
        if previous and osa_distance(previous,'gaming')<=1 and re.search(r'\\b(?:used|what|where|equipment|studio)\\b',low):targets.extend(('mouse','chair','keyboard','monitor'))
        if re.search(r'\\b(?:make|create)\\s+(?:a|my|the)\\s+$',before):targets.append('reservation')''')
s=s.replace('ก่อน|ภายใน|','ก่อน|ภายใน|')
s=s.replace('ยังไง|อย่างไร|เข้า|ตัวเอง','ยังไง|อย่างไร|เข้า|ก่อน|ภายใน|ตัวเอง')
f.write_text(s,encoding='utf-8')
f=P/'app/pipeline/engine.py';s=f.read_text(encoding='utf-8');s=s.replace('(?:open|opening|hours|schedule|close|closing)', '(?:opens?|opening|hours|schedule|closes?|closing)',1);f.write_text(s,encoding='utf-8')
f=P/'app/pipeline/bilingual_english.py';s=f.read_text(encoding='utf-8');s=s.replace('{"open", "opening", "close", "closing", "hours", "schedule", "time",', '{"open", "opens", "opening", "close", "closes", "closing", "hours", "schedule", "time",',1);f.write_text(s,encoding='utf-8')
f=P/'app/pipeline/closed_query_improvements.py';s=f.read_text(encoding='utf-8')
s=s.replace("capacity=fee['capacity'].replace('คน','people') if en else fee['capacity']", "capacity=('1 person' if fee['capacity']=='1 คน' else fee['capacity'].replace('คน','people')) if en else fee['capacity']")
needle='def answer_closed_query_improvement(query,locale):';assert s.count(needle)==1
extra='''def _contact_fields(query,locale):
    if not (re.search(r'อีเมล|\\be-?mail\\b',query,re.I) and re.search(r'เบอร์|โทร|\\b(?:phone|telephone|tel)\\b',query,re.I)):return None
    if re.search(r'ส่วนตัว|\\b(?:personal|private)\\b',query,re.I):return None
    if not re.search(r'ศูนย์|สตูดิโอ|ติดต่อ|\\b(?:studio|contact)\\b',query,re.I):return None
    from app.rules.matcher import RuleMatcher
    from app.pipeline.bilingual_english import _rule_answer
    from app.core.source_registry import make_source_hits
    matcher=RuleMatcher.default()
    if locale=='en':
        result=_rule_answer('How can I contact the studio',matcher)
        if result is None:return None
        return StructuredToolResult(result.answer,result.hits,'structured_contact_fields',.98,{'required_fields':['email','phone'],'approved_contact_rule':True})
    results=[matcher.match(q,category='contact',locale='th') for q in ('อีเมล','เบอร์โทร')]
    if not all(results):return None
    source_ids=list(dict.fromkeys(source for result in results for source in result.get('source_ids',[])))
    hits=make_source_hits(source_ids)
    answer='\\n'.join(result['answer'] for result in results)
    for url in dict.fromkeys(result.get('source_url','') for result in results):
        if url:answer+='\\nแหล่งข้อมูล: '+url
    return StructuredToolResult(answer,hits,'structured_contact_fields',.98,{'required_fields':['email','phone']})

'''
s=s.replace(needle,extra+needle).replace("[('no_answer',_non_catalog_request)","[('contact',_contact_fields),('no_answer',_non_catalog_request)")
f.write_text(s,encoding='utf-8')
print('E applied to '+str(P)+': local noun frames, protected names, Thai following boundaries, English inflections, complete contact fields')
