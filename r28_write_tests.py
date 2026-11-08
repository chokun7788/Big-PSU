from pathlib import Path
PROJECT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
code=r'''import unittest
from unittest.mock import patch
from app.pipeline.engine import answer_question_pipeline_debug
from app.pipeline.competition_source_gaps import lookup_competition_reply
from app.core.intent_cue_recovery import recover_intent_cues

def answer(q,locale='th'):
    return answer_question_pipeline_debug(q,locale=locale,experimental_allow_llm=False,experimental_rag_fallback=True)

class CompositionR28Tests(unittest.TestCase):
    def test_two_equipment_prohibitions_are_both_answered(self):
        result=answer('Under CS2 tournament rules, are macros allowed and may I install software?','en')
        self.assertIn('No scripts or macros',result.answer)
        self.assertIn('install',result.answer);self.assertIn('prohibited',result.answer)
        self.assertTrue(result.validation.ok)

    def test_regular_money_and_overtime_are_not_mutually_excluded(self):
        result=answer('กติกา CS2 เงินเริ่มต้นและเวลาระเบิดรอบปกติเท่าไร แล้วต่อเวลามีกี่รอบและเงินเริ่มต้นเท่าไร')
        for word in ('$800','$10,000','40 วินาที','6'):self.assertIn(word,result.answer)

    def test_only_overtime_cannot_borrow_regulation_money(self):
        result=answer('What is CS2 tournament overtime starting money?','en')
        self.assertIn('$10,000',result.answer);self.assertNotIn('$800',result.answer)

    def test_protest_language_and_procedure_preserve_both(self):
        result=answer('Under CS2 tournament rules, which language must protests use, who may file a protest and within how many minutes?','en')
        for term in ('Thai','15 minutes','captain','coach'):self.assertIn(term,result.answer)

    def test_fee_is_not_late_registration(self):
        for locale,q in [('th','กติกา CS2 ค่าสมัครกี่บาท'),('en','What is the CS2 tournament registration fee?')]:
            result=answer(q,locale)
            self.assertIn('no_answer',result.mode)
            self.assertNotIn('after the registration period',result.answer)
            self.assertFalse(result.hits)

    def test_supported_clause_is_kept_with_unknown_fee(self):
        result=answer('Under CS2 tournament rules, are scripts allowed and what is the registration fee?','en')
        self.assertIn('No scripts or macros',result.answer)
        self.assertIn('could not find a registration fee',result.answer)
        self.assertIn('partial',result.mode)
        self.assertLess(result.answer.index('could not find'),result.answer.index('Source:'))

    def test_truncated_numbered_clause_does_not_borrow_other_penalties(self):
        for locale,q in [('th','กติกา RoV ข้อ 6.1.5.1 บทลงโทษเต็มว่าอะไร'),('en','What is the complete RoV tournament penalty clause 6.1.5.1?')]:
            result=answer(q,locale)
            self.assertIn('no_answer',result.mode);self.assertFalse(result.hits)
            self.assertIn('6.1.5.1',result.answer)
            self.assertNotIn('6.2.4.1',result.answer);self.assertNotIn('6.1.2.1',result.answer)

    def test_numbered_reference_must_be_exact(self):
        reply=lookup_competition_reply('กติกา RoV ข้อ 6.1.5.10 ว่าอะไร','th')
        self.assertEqual(reply.outcome,'no_answer')
        self.assertIn('explicit_clause_not_covered',reply.reasons)

    def test_complete_numbered_clause_keeps_resume_condition(self):
        reply=lookup_competition_reply('กติกา RoV ข้อ 4.3.1 ว่าอะไร','th')
        self.assertEqual(reply.outcome,'answer')
        for word in ('5 ครั้ง','1 นาที','Resume'):self.assertIn(word,reply.answer)

    def test_pause_conflict_is_visible_before_permission(self):
        for locale,q in [('th','กติกา Tekken 8 หยุดเกมได้ไหม'),('en','May I pause under Tekken 8 tournament rules?')]:
            result=answer(q,locale)
            self.assertIn('conflict',result.mode)
            self.assertIn('ขัดกัน' if locale=='th' else 'conflict',result.answer.splitlines()[0])
            self.assertGreaterEqual(len(result.hits),2)

    def test_future_explicit_age_source_is_not_treated_as_missing(self):
        row={'id':'competition_rules_cs2_psu_phuket_2026_s99_c01','text':'ผู้เข้าแข่งขันต้องมีอายุขั้นต่ำ 20 ปี','game':'Counter-Strike 2','tournament':'PSU Phuket CS2 2026 Tournament','source_url':'local://fixture'}
        with patch('app.pipeline.competition_source_gaps._rows',return_value=[row]):
            reply=lookup_competition_reply('กติกา CS2 อายุขั้นต่ำกี่ปี','th')
        self.assertEqual(reply.outcome,'answer');self.assertIn('20 ปี',reply.answer)

    def test_future_explicit_fee_source_is_read_without_guessing(self):
        row={'id':'competition_rules_cs2_psu_phuket_2026_s99_c01','text':'ค่าสมัครการแข่งขัน 250 บาทต่อทีม','game':'Counter-Strike 2','tournament':'PSU Phuket CS2 2026 Tournament','source_url':'local://fixture'}
        with patch('app.pipeline.competition_source_gaps._rows',return_value=[row]):
            reply=lookup_competition_reply('กติกา CS2 ค่าสมัครกี่บาท','th')
        self.assertEqual(reply.outcome,'answer');self.assertIn('250 บาทต่อทีม',reply.answer)

    def test_recovery_preserves_meaning_and_protected_values(self):
        q='Under CS2 tournament rules, no macros, 1:55 round time and $800 in regulation?'
        self.assertEqual(recover_intent_cues(q),q)
'''
with (PROJECT/'tests/test_competition_composition_r28_20261001.py').open('x',encoding='utf-8') as f:f.write(code)
base=Path(__file__).parent
s=(base/'r27_unit_check.py').read_text(encoding='utf-8').replace('r27_report_path.txt','r28_report_path.txt').replace("names=[","names=['tests.test_competition_composition_r28_20261001',",1)
with (base/'r28_unit_check.py').open('x',encoding='utf-8') as f:f.write(s)
