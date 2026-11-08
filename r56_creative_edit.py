from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r56_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
assert not (OUT/'EDIT6_DONE').exists()
p=ROOT/'app/pipeline/query_signals.py';t=p.read_text(encoding='utf-8');needle='def looks_like_clear_general_request(text: str) -> bool:'
addition='''def looks_like_explicit_creation_request(text: str) -> bool:
    """Named writing tasks are separate from the game's availability catalog.

    Requests for actual studio policies, live data or rates remain grounded.
    """
    q = normalize_text(text)
    named = bool(re.search(r'^(?:please\\s+)?(?:write|draft|compose)\\b.{0,100}\\b(?:invitation|scene|dialogue|post|message|caption|story)\\b|^(?:ช่วย)?(?:เขียน|ร่าง|แต่ง)(?:โพสต์|บทสนทนา|คำเชิญ|ข้อความชวน)', q, re.I))
    factual = bool(re.search(r'ราคา|ค่าบริการ|จอง|ว่าง|กฎ|กฏ|กติกา|ศูนย์|มหาวิทยาลัย|\\b(?:psu|studio|prices?|fees?|booking|reservations?|available|rules?|tournament|opening|official)\\b',q,re.I))
    return named and not factual


'''
assert needle in t;t=t.replace(needle,addition+needle,1);t=t.replace("    if has_any_signal(query, *_PSU_INVENTORY_TERMS):", "    if looks_like_explicit_creation_request(query):\n        return True\n    if has_any_signal(query, *_PSU_INVENTORY_TERMS):",1);p.write_text(t,encoding='utf-8')
p=ROOT/'app/pipeline/engine.py';t=p.read_text(encoding='utf-8');needle='            from app.pipeline.request_focus import explicit_request_focus'
addition='''            from app.pipeline.query_signals import looks_like_explicit_creation_request
            if looks_like_explicit_creation_request(question):
                from app.pipeline.experimental_fallback import _general_llm_fallback, _general_disabled_answer
                allow_llm = env_experimental_llm_default() if experimental_allow_llm is None else experimental_allow_llm
                route = PipelineRoute('general','creative_writing',1.0,'fact','low','explicit creation task; game vocabulary does not request studio inventory')
                if allow_llm:
                    result = _general_llm_fallback(question,details=('explicit_creation_task',),mode='general_llm_direct',decision='general_llm_direct')
                    return self._build_result(result.answer,result.hits,started,'pipeline:'+result.mode,result.confidence,
                        route,EntityBundle(),ValidationResult(ok=True),[*entry_timings,result.trace])
                return self._build_result(_general_disabled_answer(),[],started,'pipeline:general_llm_disabled',1.0,
                    route,EntityBundle(),ValidationResult(ok=True),entry_timings)
'''
assert needle in t;t=t.replace(needle,addition+needle,1);p.write_text(t,encoding='utf-8')
p=ROOT/'app/pipeline/experimental_fallback.py';t=p.read_text(encoding='utf-8');t=t.replace("if word_request and int(word_request.group(1)) >= 100:","if word_request and int(word_request.group(1)) >= 30:",1);t=t.replace("max(256, requested_words * 3)","max(256, requested_words * 4)",1);p.write_text(t,encoding='utf-8')
p=ROOT/'tests/test_remaining_repairs_r56.py';t=p.read_text(encoding='utf-8');needle='    def test_capacity_idempotency_and_no_ambiguous_replay(self):'
addition='''    def test_named_creative_task_not_game_catalog(self):
        from app.pipeline.query_signals import looks_like_explicit_creation_request,looks_like_clear_general_request
        for q in ('Write a short friendly invitation for friends to play video games together, about 80 words.','ช่วยเขียนโพสต์ชวนเพื่อนมาเล่นเกมด้วยกัน สั้นๆ 80 คำ'):
            self.assertTrue(looks_like_explicit_creation_request(q));self.assertTrue(looks_like_clear_general_request(q))
        for q in ('What games are on PC?','Write a message about actual PSU studio opening hours.','Write a post listing official studio prices.','Translate: Write an invitation to play games.'):
            self.assertFalse(looks_like_explicit_creation_request(q))
    def test_requested_eighty_words_not_twenty_five_word_cap(self):
        from app.pipeline.experimental_fallback import select_general_generation_profile
        for q in ('Write an invitation of about 80 words.','ช่วยเขียนโพสต์ชวนเพื่อน 80 คำ'):
            p=select_general_generation_profile(q);self.assertEqual(p.requested_words,80);self.assertEqual(p.name,'long_explanation');self.assertGreaterEqual(p.num_predict,320)
'''
assert needle in t;t=t.replace(needle,addition+needle,1);p.write_text(t,encoding='utf-8')
(OUT/'EDIT6_DONE').write_text('named creative task routed before English catalog; generation length matches 30-99 word requests',encoding='utf-8');print('creative task scope and generation budget fixed')
