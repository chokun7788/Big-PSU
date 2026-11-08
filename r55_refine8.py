from pathlib import Path
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def edit(name,old,new):
    p=ROOT/name;s=p.read_text(encoding='utf-8');assert old in s,(name,old[:100]);p.write_text(s.replace(old,new,1),encoding='utf-8')
edit('app/session/conversation_plan.py',"explicit and (usage or service_mentions", "explicit and (usage or customer_filter(q)[0] or service_mentions")
edit('app/pipeline/service_query_completion.py',"r'เท่าไหร่|เท่าไร|\\b(?:cost|how much)","r'กี่บาท|เท่าไหร่|เท่าไร|\\b(?:cost|how much)")
edit('app/pipeline/user_service_facts.py',"        if _has(q,subject) and _has(q,condition):", """        subject_present=_has(q,subject)
        if field=='game_installation_permission' and _has(q,r'\\b(?:install|add)\\b'):
            from app.runtime.fast_answer import is_known_unsupported_game_query
            from app.session.context_resolver import detect_game
            subject_present=subject_present or bool(detect_game(q) or is_known_unsupported_game_query(q))
        if subject_present and _has(q,condition):""")
edit('app/calculator/service_fee.py',"    match = re.search(r\"(\\d+)\\s*(?:คน|persons?|people)\", q)\n    return int(match.group(1)) if match else None", """    match = re.search(r'(\\d+)\\s*(?:คน|persons?|people|ppl)',q)
    if match:return int(match.group(1))
    words={'หนึ่ง':1,'สอง':2,'สาม':3,'สี่':4,'ห้า':5,'หก':6,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6}
    match=re.search(r'(?<![a-z])('+'|'.join(words)+r')\\s*(?:คน|persons?|people|ppl|of us)',q)
    if match:return words[match.group(1)]
    match=re.search(r'\\bgroup of (one|two|three|four|five|six)\\b',q)
    return words[match.group(1)] if match else None""")
edit('app/pipeline/service_query_completion.py',"from app.calculator.service_fee import SERVICE_FEES\n", "from app.calculator.service_fee import SERVICE_FEES,_detect_people\n")
edit('app/pipeline/service_query_completion.py',"filters={},per_target_filters={}","filters={'people_count':_detect_people(q)},per_target_filters={}")
edit('app/pipeline/service_query_completion.py',"    if en and re.search(r'\\b(?:shoot|reload)\\b',q):", """    if not en and re.search(r'ปุ่ม|ควบคุม',q) and not re.search(r'กฎ|กฏ|กติกา|แข่ง|ราคา|จอง|เสีย|พัง',q):
        from app.session.context_resolver import detect_games
        named=detect_games(q)
        if len(named)==1:
            from app.pipeline.structured_tools import _control_answer
            from app.pipeline.schemas import UniversalIntent
            value=_control_answer(q,UniversalIntent('game_controls','control_lookup',target=named[0]))
            if value:return _result(value.answer,value.hits,'game_controls','control_lookup',{'basis':'existing_structured_control_handler',**value.evidence})
    if en and re.search(r'\\b(?:shoot|reload)\\b',q):""")
edit('tests/test_service_repairs_r55.py',"    def test_game_scope_task_memory(self):", """    def test_new_phrasings_and_capacity(self):
        p=resolve_request_plan('ขอราคาบุคคลทั่วไป',[])
        self.assertIn('service',p['tasks'][0]['pending_slots'])
        self.assertIsNone(resolve_request_plan('คอมมีเกมไรบ้าง แล้วบุคคลทั่วไปเล่นสามชั่วโมงกี่บาท',[]))
        self.assertIn('game_installation_permission',answer_user_service_facts('Can I install Minecraft myself?','en')['validation'].warnings)
        result=answer_budget('General adult budget 200 THB Nintendo Switch four people','en')
        rows=result['trace'][0].metadata['packages']
        self.assertEqual([(r['package'],r['sessions']) for r in rows],[('nintendo_switch_3_4',0)])
    def test_game_scope_task_memory(self):""")
print('new paraphrases, budget capacity and deterministic controls repaired')
