from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
f=P/'app/core/task_frame_recovery.py';s=f.read_text(encoding='utf-8').replace('import re\n','import re\nfrom functools import lru_cache\n').replace('def recover_task_frame(text: str):','@lru_cache(maxsize=2048)\ndef recover_task_frame(text: str):')
s=s.replace('pc|ps5|vr|cockpit','pc(?:[ -]?#?\\d+)?|ps5|vr|cockpit',1)
s=s.replace('rice march pay paid','embers ember rice march pay paid')
s=s.replace("    # Keep Thai competition propositions", "    if not re.search(r'[\\u0e00-\\u0e7f]',text):return None\n    # Keep Thai competition propositions")
s=s.replace("'เล่นได้ที่เครื่องไหน',1", "'เล่นได้ที่เครื่องไหน',1")
s=s.replace("'ตัวเอง|ดัวเอง", "'ตัวเอง|ดัวเอง")
s=s.replace('ยังไง|อย่างไร|ตัวเอง', 'ยังไง|อย่างไร|เข้า|ตัวเอง')
s=s.replace("if re.search(r'หาย|เปียก|เปียด',text):frames += [('ของหาย',1),('อุปกรณ์เปียก',1)]", "if re.search(r'หาย|เปียก|เปียด',text):frames += [('ของหาย',1),('เปียก',1)]")
s=s.replace("if 'ปานกลาง' in text:", "if re.search(r'ปานกลาง|ยานกลาง',text):")
s=s.replace("range(max(3,len(target)-budget)","range(max(2,len(target)-budget)")
f.write_text(s,encoding='utf-8')
f=P/'app/pipeline/bilingual_english.py';s=f.read_text(encoding='utf-8')
s=s.replace("|[?.]|$)\", query, re.I)","|\\?|$)\", query, re.I)")
needle='    if re.search(r"\\bhow\\s+many\\s+members?\\b", query, re.I):'
assert s.count(needle)==1
s=s.replace(needle,'''    if re.search(r"\\bhow\\s+many\\s+(?:categories|groups)\\b",query,re.I) and tokens & {'member','members'}:
        rows=_member_rows()
        groups={group:sum(str(row.get('group'))==group for row in rows) for group in dict.fromkeys(str(row.get('group') or 'Unspecified group') for row in rows)}
        answer=f"The recorded member directory has {len(groups)} groups and {len(rows)} member records:\\n" + "\\n".join(f"- {group}: {count} records" for group,count in groups.items())
        return _result(answer+_source_suffix(MEMBERS_URL),category='overview',intent='members_lookup',mode='pipeline:structured_member_group_count_en',confidence=.98,hits=[_hit('Members','members',MEMBERS_URL,'Member directory')],reason='group and record counts computed directly from the source directory')
'''+needle)
s=s.replace('        if token in tokens:\n            return weekday','        if token in tokens or token + "s" in tokens:\n            return weekday')
needle='    if safe_rule is not None:\n        return safe_rule'
assert s.count(needle)==1
s=s.replace(needle,'''    if safe_rule is not None:
        if safe_rule.route.intent == 'no_answer_overnight_room':
            from dataclasses import replace
            safe_rule=replace(safe_rule,answer='I could not find verified overnight accommodation information. '+safe_rule.answer)
        return safe_rule''')
# Missing service/object questions need clarification, including a valid
# possessive left by a typo. Do not silently change his to this.
s=s.replace('elif re.search(r"\\bcan i book this\\b", q):','elif re.search(r"\\bcan i book (?:this|that|it|his|hers|theirs)\\s*[?.]*$", q):')
s=s.replace('elif re.search(r"\\bwhere can i play (?:it|this(?: game)?)\\b", q)', 'elif re.search(r"\\bwhere (?:can|an) i play (?:it|this(?: game)?)\\b", q)')
f.write_text(s,encoding='utf-8')
# Price comparison is an ordinary supported operation, not inventory lookup.
f=P/'app/core/normalization.py';s=f.read_text(encoding='utf-8');s=s.replace('return contains_alias(query, PRICE_WORD_ALIASES, fuzzy=False)[0]','return contains_alias(query, PRICE_WORD_ALIASES, fuzzy=False)[0] or any(word in normalize_text(query) for word in ("แพงกว่า", "ถูกกว่า"))');f.write_text(s,encoding='utf-8')
f=P/'app/pipeline/query_signals.py';s=f.read_text(encoding='utf-8');s=s.replace('    "คำนวณราคา",','    "คำนวณราคา",\n    "แพงกว่า",\n    "ถูกกว่า",');f.write_text(s,encoding='utf-8')
f=P/'app/pipeline/closed_query_improvements.py';s=f.read_text(encoding='utf-8');needle='def answer_closed_query_improvement(query,locale):';assert s.count(needle)==1
extra='''def _fee_comparison(query,locale):
    from app.core.normalization import SERVICE_ALIASES,contains_alias
    if not re.search(r'แพงกว่า|ถูกกว่า|\\b(?:more expensive|cheaper)\\b',query,re.I):return None
    services=[key for key,aliases in SERVICE_ALIASES.items() if contains_alias(query,aliases,fuzzy=False)[0]]
    if len(services)<2:return None
    from app.calculator.service_fee import SERVICE_FEES,GROUP_LABELS
    from app.pipeline.bilingual_english import _GROUP_LABELS_EN
    from app.core.source_registry import SERVICE_FEE_IMAGE_2026_ID,PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID,make_source_hits
    en=locale=='en';labels=_GROUP_LABELS_EN if en else GROUP_LABELS
    lines=['Recorded package prices for all requested services:' if en else 'ราคาต่อแพ็กเกจของทุกบริการที่ถาม:']
    # Do not assume an entitlement, duration or shared capacity to pick a winner.
    # Display each distinct source rate; ask what comparison the user needs.
    selected=[(key,fee) for key,fee in SERVICE_FEES.items() if any(key==service or key.startswith(service+'_') for service in services)]
    for key,fee in selected:
        capacity=fee['capacity'].replace('คน','people') if en else fee['capacity']
        lines.append(f"\\n{fee['label']} ({capacity}), {fee['minutes_per_session']} "+('minutes/session' if en else 'นาที/รอบ'))
        for group,price in fee['prices'].items():lines.append(f"- {labels[group]}: {price:,} "+('THB' if en else 'บาท'))
    lines.append('Packages have different durations/capacities. Which user group, duration and number of players should I compare?' if en else 'แพ็กเกจมีระยะเวลาและจำนวนผู้เล่นต่างกัน ต้องการเทียบสำหรับกลุ่มผู้ใช้ใด เล่นนานเท่าไร และกี่คนครับ?')
    hits=make_source_hits([SERVICE_FEE_IMAGE_2026_ID]+([PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID] if 'pc' in services else []))
    for url in dict.fromkeys(h.get('metadata',{}).get('source_url','') for h in hits):
        if url:lines.append(('Source: ' if en else 'แหล่งข้อมูล: ')+url)
    return StructuredToolResult('\\n'.join(lines),hits,'structured_service_fee_comparison',.98,{'services':services,'source_rates_only':True,'no_assumed_group_or_duration':True})

'''
s=s.replace(needle,extra+needle).replace("[('service_fee',answer_fee_alternatives)","[('service_fee',_fee_comparison),('service_fee',answer_fee_alternatives)")
f.write_text(s,encoding='utf-8')
print('C: source content, literal/negation safety, span boundaries, task recovery cache')
