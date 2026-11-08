from pathlib import Path
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
p=ROOT/'app/pipeline/competition_conversation_signals.py'
s=p.read_text(encoding='utf-8');old='|ครบ|ไหม|มั้ย|หน่อย|ครับ|';assert old in s
p.write_text(s.replace(old,'|ครบ|ไหม|มั้ย|ล่ะ|หน่อย|ครับ|',1),encoding='utf-8')
p=ROOT/'tests/test_service_repairs_r55.py';s=p.read_text(encoding='utf-8')
anchor='    def test_timeout_partial_progress_is_scoped_and_not_a_claimed_cause(self):'
assert anchor in s
s=s.replace(anchor,"""    def test_explicit_rule_overview_with_discourse_particle(self):
        from app.pipeline.competition_conversation_signals import is_broad_rule_request
        for q in ('กฎแข่ง ROV ล่ะ','กฎแข่ง CS2 ล่ะ','What about the rules for RoV?'):
            with self.subTest(q=q):
                self.assertTrue(is_broad_rule_request(q))
                r=resolve_question_with_context(q,[])
                self.assertEqual(r.reason,'canonicalized_explicit_generic_competition_rules')
                self.assertFalse(r.used_context)
        self.assertFalse(is_broad_rule_request('กฎแข่ง ROV ปี 2030 ล่ะ'))
        self.assertFalse(is_broad_rule_request('กฎแข่ง ROV เรื่องการพักเกมล่ะ'))
"""+anchor,1)
p.write_text(s,encoding='utf-8')
print('bounded discourse particle keeps explicit rule overview; edition/facet preserved')
