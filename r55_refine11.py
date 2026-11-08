from pathlib import Path
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
p=ROOT/'app/pipeline/service_query_completion.py';s=p.read_text(encoding='utf-8')
a="""        from app.session.context_resolver import detect_games
        named=detect_games(q)
        if len(named)==1:
            from app.pipeline.structured_tools import _control_answer
            from app.pipeline.schemas import UniversalIntent
            value=_control_answer(q,UniversalIntent('game_controls','control_lookup',target=named[0]))"""
b="""        from app.pipeline.structured_tools import _control_answer,_detect_game
        from app.pipeline.competition_targets import resolve_competition_targets
        # The control handler's catalog already recognizes CS2 and merges
        # the Tekken title variants. Reuse it rather than a session alias list.
        named=_detect_game(q,allow_fuzzy=False)
        multiple=resolve_competition_targets(q).status=='multiple'
        if named and not multiple and not re.search(r'และ|หรือ|เทียบ|\\b(?:and|or|versus|compare)\\b',q):
            from app.pipeline.schemas import UniversalIntent
            value=_control_answer(q,UniversalIntent('game_controls','control_lookup',target=named['game']))"""
assert a in s;p.write_text(s.replace(a,b,1),encoding='utf-8')
p=ROOT/'tests/test_service_repairs_r55.py';s=p.read_text(encoding='utf-8')
a='    def test_explicit_booking_scope(self):'
b="""    def test_control_preflight_reuses_existing_catalog_aliases(self):
        for q,game in [('ปุ่มยิงกับรีโหลดใน CS2 คืออะไร','Counter-Strike 2'),('ขอปุ่ม Tekken 8 ทั้งหมด','TEKKEN 8')]:
            with self.subTest(q=q):
                result=answer_explicit_source_operation(q,'th',RuleMatcher.default())
                self.assertEqual(result['mode'],'pipeline:source_operation_control_lookup')
                self.assertIn(game,result['answer'])
                self.assertIn('ยังไม่ได้ตรวจยืนยัน',result['answer'])
        self.assertIsNone(answer_explicit_source_operation('ขอปุ่ม CS2 กับ Tekken 8','th',RuleMatcher.default()))
"""+a
assert a in s;p.write_text(s.replace(a,b,1),encoding='utf-8')
print('Use the existing control catalog resolver for explicit single-game controls.')
