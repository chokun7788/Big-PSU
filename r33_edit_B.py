from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
f=P/'app/core/task_frame_recovery.py';s=f.read_text(encoding='utf-8')
s=s.replace("if re.search(r'\\b(?:reservation|booking|book|cancel)\\b',low):targets.extend", "if re.search(r'\\b(?:reservation|booking|book|cancel|policy)\\b',low):targets.extend")
s=s.replace("if re.search(r'\\b(?:open|hours?|operating|schedule|days?|morning|sundays?)\\b',low):", "if re.search(r'\\b(?:open|hours?|operating|schedule|days?|morning|sundays?|now|play)\\b',low):")
s=s.replace("if re.search(r'\\b(?:play|listed|have|available)\\b',low):targets.append('game')", "if re.search(r'\\b(?:play|listed|have|available|called|unknown)\\b',low):targets.append('game')\n        if re.search(r'\\b(?:who|categories|divided)\\b',low):targets.append('members')\n        if re.search(r'\\bpenalties\\b',low):targets.append('damage')\n        if re.search(r'\\bacross\\b.*\\bzones\\b',low):targets.append('multiple')\n        if re.search(r'\\bdevice\\s+is\\s+$',before):targets.append('best')\n        if re.search(r'\\bcan\\s+i\\s+$',before) and re.match(r'\\s+(?:this|his)\\b',after):targets.append('book')")
s=s.replace("winners={t for t in targets if len(word)>=3 and abs(len(t)-len(word))<=1 and osa_distance(word,t)==1}", "winners={t for t in targets if len(word)>=3 and abs(len(t)-len(word))<=1 and osa_distance(word,t)==1}\n        # Two errors in a long modifier need an intact hardware noun.\n        if not winners and re.match(r'\\s+(?:monitors?|keyboard|mouse|chair)\\b',after) and len(word)>=5 and osa_distance(word,'gaming')==2:\n            return m.start(),m.group(),'gaming',2,'two-edit modifier before exact hardware noun'")
s=s.replace("    # Thai has no word boundaries.", "    # Keep Thai competition propositions on the separate source-bound path.\n    from app.pipeline.competition_targets import looks_like_competition_rule_query\n    if looks_like_competition_rule_query(text):return None\n    # Thai has no word boundaries.")
s=s.replace("frames += [('ราคาเท่าไหร่',2),('เสียกี่บาท',2),('กี่บาท',1),('ต้องเสียเงินไหม',1),('แพงกว่า',1)]", "frames += [('เสียกี่บาท',2),('ต้องเสียเงินไหม',1),('อันไหนแพงกว่า',2)]\n        if not re.search(r'ราคาเท่า(?:ไหร่|ไร)|ราคากี่บาท',text):frames += [('ราคาเท่าไหร่',2)]\n        if re.search(r'บาท|ราคา|เสีย|ครึ่งชั่วโมง',text) or re.search(r'กี่[^\\s]{1,4}\\s*$',text):frames += [('กี่บาท',1)]")
s=s.replace("frames += [('ว่างไหม',1),('ว่างมั้ย',2)]", "frames += [('ว่างไหม',1),('ว่างมั้ย',2)]")
s=s.replace("if 'ตอน' in text or 'โมง' in text or 'บ่าย' in text:","if 'ตอน' in text or 'โมง' in text or 'บ่าย' in text:")
s=s.replace("if has_game:\n        frames +=", "if has_game:\n        frames += [('มีปุ่มอะไรบ้าง',1)]\n        frames +=")
s=s.replace("if re.search(r'ถึง|ต้อง|ลืม|จอง|แนบ',text):frames += [('เช็กอิน',1),('สลิป',1)]", "if re.search(r'ถึง|ต้อง|ลืม|จอง|แนบ',text):frames += [('เช็กอิน',1),('สลิปไหม',2)]\n    if re.search(r'ข้อมูลเรื่อง|ข้อมูลเรื|สูบ|กฎ',text):frames += [('สูบบุหรี่',1)]\n    if re.search(r'หาย|เปียก|เปียด',text):frames += [('ของหาย',1),('อุปกรณ์เปียก',1)]\n    if 'ปานกลาง' in text:frames += [('เสียหายปานกลาง',2)]\n    if 'คือใคร' in text:frames += [('ตำแหน่ง',1),('เลขานุการ',1)]\n    if re.search(r'เล่นได้[^\\s]{1,3}\\s*(?:[?]|$)',text):frames += [('เล่นได้ไหม',1)]\n    if has_resource and re.search(r'ต้องทำ(?:ยังไง|บังไง|อย่างไร)',text):frames += [('จอง',1)]\n    if re.search(r'ดำเนนการ|ดำเนินการ',text):frames += [('หน่วยงาน',1),('ดำเนินการ',1)]")
s=s.replace("    candidates=[]\n    for target,budget in frames:", "    protected=[(m.start(),m.end()) for m in re.finditer(r'ไม่|ห้าม|อย่า|เกิน|กี่นาที|ราคาเท่าไร|ราคาเท่าไหร่|สูบบุหรี่|อุปกรณ์|เช็กอิน|เช็คอิน|สลิปไหม|ตำแหน่งอะไร',text)]\n    candidates=[]\n    for target,budget in frames:")
s=s.replace("                if len(observed)!=length or not re.fullmatch", "                if any(start < end and start+length > begin for begin,end in protected):continue\n                if len(observed)!=length or not re.fullmatch")
s=s.replace("                distance=osa_distance(observed,target)", "                # Keep trailing question particles outside a noun.\n                suffix=text[start+length:]\n                if target in {'เช็กอิน','อาหาร','คีย์บอร์ด','เสียหาย','ของหาย','เปียก','สูบบุหรี่','เลขานุการ','ตำแหน่ง','จอง','หน่วยงาน','ดำเนินการ'}:\n                    if suffix and re.match(r'[\\u0e00-\\u0e7f]',suffix) and not re.match(r'(?:ไหม|มั้ย|อะไร|ยังไง|อย่างไร|ตัวเอง|ดัวเอง|มา|รับผิด|เล็กน้อย|ปานกลาง|คือใคร|อะไร|มี|ใคร|ต้อง)',suffix):continue\n                distance=osa_distance(observed,target)")
f.write_text(s,encoding='utf-8')
f=P/'app/pipeline/bilingual_english.py';s=f.read_text(encoding='utf-8')
needle='    member_rows = _member_rows_for_requested_role(query)'
assert s.count(needle)==1
s=s.replace(needle,'''    # An explicit person is not a request for the complete member directory.
    # Only source names or approved name localizations can bind an identity.
    person_request = re.search(r"\\b(?:position|role)\\s+(?:does|do|is)\\s+(.+?)(?:\\s+(?:hold|holds|old)\\b|[?.]|$)", query, re.I)
    if person_request:
        named = person_request.group(1).strip()
        def name_key(value):
            return re.sub(r"\\b(?:mr|mrs|ms|dr|prof)\\.?|[^\\w\\u0e00-\\u0e7f]+", "", value.casefold())
        matches = tuple(row for row in _member_rows() if any(
            name_key(value) and name_key(value) == name_key(named)
            for value in (str(row.get('name') or ''), approved_localization(row, 'name') or '')
        ))
        if not matches:
            return _result(
                "I could not verify a member record for " + named + ". Please provide the exact name from the official member directory; I cannot infer an official identity from an unverified English spelling.",
                category="overview", intent="members_lookup", mode="pipeline:member_person_not_found_en",
                confidence=0.98, hits=[_hit("Members", "members", MEMBERS_URL, "Members")],
                reason="explicit person has no exact source or approved localized name match", answer_type="no_answer",
            )
        member_rows = matches
    else:
        member_rows = _member_rows_for_requested_role(query)''')
needle='    scope_guidance = _answer_english_scope_guidance(query)'
assert s.count(needle)==1
s=s.replace(needle,'''    if re.search(r"\\b(?:studio|usage|house)\\s+rule\\b", query, re.I) and not _competition_target(query):
        general_rules = _rule_answer("What are the studio rules", matcher)
        if general_rules is not None:
            return general_rules
'''+needle)
f.write_text(s,encoding='utf-8')
print('B: Thai span boundaries, negation protection, source-bound person lookup, singular rule')
