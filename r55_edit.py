from pathlib import Path
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def edit(name,old,new):
    p=ROOT/name;s=p.read_text(encoding='utf-8');assert old in s,(name,old[:90]);p.write_text(s.replace(old,new,1),encoding='utf-8')
# Guard clock, duration, currency and people suffixes before interpreting IDs.
p=ROOT/'app/booking/live_status.py';s=p.read_text(encoding='utf-8');start=s.index('    family_patterns = {',s.index('def _requested_resource_number'));end=s.index('    pattern =',start)
s=s[:start]+s[start:end].replace(r'(\d{1,2})\b',r'(\d{1,2})(?!\d|\s*(?::|โมง|นาที|ชั่วโมง|คน|บาท|am\b|pm\b|minutes?\b|hours?\b|people\b|persons?\b|thb\b))')+s[end:]
s=s.replace(r'(\d{1,2})(?!\d|:|โมง)',r'(\d{1,2})(?!\d|\s*(?::|โมง|นาที|ชั่วโมง|คน|บาท|am\b|pm\b|minutes?\b|hours?\b|people\b|persons?\b|thb\b))');p.write_text(s,encoding='utf-8')
edit('app/calculator/service_fee.py','    q = normalize_text(query)\n    if contains_alias(q, TIME_WORD_ALIASES["half_hour"], fuzzy=False)[0]:','''    q = normalize_text(query)
    # Word numbers are quantity slots only next to a duration unit. Preserve
    # identifiers and time of day; never rewrite the user's raw query.
    words = {'หนึ่ง':1,'สอง':2,'สาม':3,'สี่':4,'ห้า':5,'หก':6,
             'one':1,'two':2,'three':3,'four':4,'five':5,'six':6}
    word_match = re.search(r'(?<![a-z])('+'|'.join(words)+r')\\s*(ชั่วโมง|ชม\\.?|hours?|hrs?|นาที|minutes?|mins?)',q)
    if word_match:
        return words[word_match.group(1)] * (60 if re.match(r'ชั่วโมง|ชม|hour|hr',word_match.group(2)) else 1)
    if contains_alias(q, TIME_WORD_ALIASES["half_hour"], fuzzy=False)[0]:''')
edit('app/session/conversation_plan.py',"    # Negation must win before the legacy group's positive substring aliases.","""    if re.search(r'\\b(?:general\\s+adults?|adults?(?:\\s+from\\s+the\\s+public)?|non[- ]student)\\b|บุคคลทั่วไป|คนทั่วไป|ผู้ใหญ่',q) and not re.search(r'ไม่(?:ใช่|เป็น).{0,6}(?:บุคคลทั่วไป|คนทั่วไป)|\\bnot\\s+(?:a\\s+)?(?:general\\s+)?adult\\b',q):
        return 'general_adult', ['general_adult']
    # Negation must win before the legacy group's positive substring aliases.""")
edit('app/session/conversation_plan.py',"    elif all_selected:\n        if isinstance(history,list)","    elif all_selected and BOOKING.search(q):\n        return None  # All steps belongs to this explicit booking operation.\n    elif all_selected:\n        if isinstance(history,list)")
edit('app/pipeline/service_fact_query.py'," ('slip',r'", " ('documents',r'\\b(?:bring|check.?in|arriv\\w*)\\b'),\n ('slip',r'")
edit('app/pipeline/service_fact_query.py',"('สลิป',r'แนบ|รูป|ผิด|โอน')","('สลิป',r'แนบ|รูป|ผิด|โอน|อัพ|ส่ง')")
edit('app/pipeline/user_service_facts.py',"(?:four|4) (?:of us|people|friends)","(?:four|4) (?:of us|people|friends|ppl)|\\bgroup of (?:four|4)")
edit('app/pipeline/user_service_facts.py',"เลือก|เล่นอะไร|แนะนำ|\\b(?:choose|recommend|which service)","เลือก|เล่น(?:อะไร|อันไหน)|แนะนำ|\\b(?:choose|recommend|which service|what.*play)")
edit('app/pipeline/user_service_facts.py',"คนจอง.*คนเล่น|คนเล่น.*คนจอง|จองแทน|ใช้แทน|รายชื่อ.*จอง|", "คนจอง.*คนเล่น|คนเล่น.*คนจอง|จองแทน|ใช้แทน|รายชื่อ.*จอง|ไม่มีชื่อ.*(?:จอง|เล่น)|จองชื่อ.*(?:เพื่อน|เล่นแทน)|")
edit('app/pipeline/user_service_facts.py',"หลักฐาน|แสดง.*บัตร|บัตร.*แสดง|", "หลักฐาน|แสดง.*บัตร|บัตร.*แสดง|(?:เอา|นำ|พก).*บัตร|บัตรอะไร.*(?:ไป|เช็คอิน|เช็กอิน)|")
edit('app/pipeline/user_service_facts.py',"ทั้งกลุ่ม|แทน|รายคน|", "ทั้ง(?:กลุ่ม|แก๊ง|ทีม)|แทน|รายคน|")
edit('app/pipeline/user_service_facts.py',"ที่นั่งพัก|นั่งพัก|นั่งรอพัก|โซนกลาง|", "ที่นั่งพัก|นั่งพัก|นั่งรอพัก|(?:ที่|ตรง).{0,6}นั่งรอ|โซนกลาง|")
edit('app/pipeline/user_service_facts.py',"sit and rest|rest seating|rest area|", "sit and rest|seating.*rest|rest seating|rest area|")
edit('app/pipeline/user_service_facts.py',"if 'spectators' in keys and _has(q,r'ฟรี|ราคา|ค่าเข้า|", "if 'spectators' in keys and _has(q,r'ฟรี|ราคา|ค่าเข้า|เสียเงิน|จ่ายเงิน|")
edit('app/pipeline/competition_conversation_signals.py',"เพิ่มเติม|เพิ่ม|อีก|ทั้งหมด", "เพิ่มเติม|เพิ่ม|อีก|ต่อ|เหลือ|ที่เหลือ|ทั้งหมด")
edit('app/pipeline/competition_conversation_signals.py',"other|more|additional|all|full", "other|more|additional|continue|remaining|rest|next|all|full")
edit('app/pipeline/competition_conversation_signals.py',"อื่น|เพิ่มเติม|เพิ่ม|อีก|\\b(?:more|other|additional)\\b", "อื่น|เพิ่มเติม|เพิ่ม|อีก|ต่อ|เหลือ|\\b(?:more|other|additional|continue|remaining|next)\\b")
edit('app/session/task_memory.py',"                return _resolved(question,question,task,'all_catalog_axis_ambiguous',error='scope')", """                if task.get('targets'):
                    queries=[f'What games are on {t}?' if locale=='en' else f'{t} มีเกมอะไรบ้าง' for t in task['targets']]
                    return _resolved(question,'; '.join(queries),task,'all_games_preserves_selected_zone')
                return _resolved(question,question,task,'all_catalog_axis_ambiguous',error='scope')""")
edit('app/pipeline/bilingual_english.py','    if route.intent == "chatbot_identity":','    if route.intent == "chatbot_identity" and re.search(r"\\b(?:who\\s+are\\s+you|what\\s+(?:are|can)\\s+you|your\\s+name)\\b", query, re.I):')
edit('app/pipeline/bilingual_english.py','"key", "keys", "press"})','"key", "keys", "press", "shoot", "reload"})')
edit('app/pipeline/bilingual_english.py','else ()\n    if action_terms and rows:', '''else tuple(action for action in ('shoot','reload') if re.search(r'\\b'+action+r'\\b',query,re.I))
    if action_terms and rows:''')
print('r55 foundational edits applied')
