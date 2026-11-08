from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
test='''import unittest
from unittest.mock import patch
from app.core.intent_cue_recovery import recover_intent_cues
from app.pipeline.engine import _split_multi_question
from app.pipeline.question_frame import _operation_from_question
from app.pipeline.schemas import PipelineRoute
from app.pipeline.protected_intents import answer_protected_intent
from app.pipeline.closed_query_improvements import _fee_comparison
from app.rules.matcher import RuleMatcher
from app.pipeline.competition_targets import resolve_competition_targets

class SourceTaskBoundariesTests(unittest.TestCase):
    def test_comparison_preface_does_not_select_equipment_contract(self):
        q='จอสอบถาม PC กับ VR อันไหนแพงกว่า'
        route=PipelineRoute('service_fee','service_fee_query',.98,'price','low','test')
        self.assertEqual(_operation_from_question(q,route,None)[:2],('price_lookup','service_fee'))
    def test_fee_source_rates_are_not_doubled_from_half_hour(self):
        result=_fee_comparison('Which is cheaper, PC or VR?','en')
        self.assertIn('375 THB',result.answer)
        self.assertNotIn('380 THB',result.answer)
    def test_comparison_conjunction_keeps_both_operands(self):
        q='ช่วยเทียบค่าบริการ PC และ VR ให้หน่อย อันไหนถูกกว่า'
        self.assertEqual(_split_multi_question(q),[q])
    def test_price_and_booking_still_have_two_operations(self):
        self.assertGreater(len(_split_multi_question('PC กับ VR อันไหนแพงกว่า แล้วจองยังไง')),1)
    def test_payment_uses_the_loaded_source_not_a_constant(self):
        row=next(r.copy() for r in RuleMatcher.default().rules if r['id']=='rule_payment_bank')
        row['answer_th']='บัญชีทดสอบจากแหล่งที่เปลี่ยนแล้ว'
        a=answer_protected_intent('จ่ายเงินยังไงตอนของ',locale='th',service=None,rules=[row])
        self.assertIn(row['answer_th'],a.answer)
        self.assertNotIn('795-',a.answer)
    def test_missing_payment_source_does_not_fabricate_bank(self):
        self.assertIsNone(answer_protected_intent('จ่ายเงินยังไง',locale='th',service=None,rules=[]))
    def test_payment_operator_does_not_correct_valid_object(self):
        q='จ่ายเงินยงไงตอนของ'
        self.assertEqual(recover_intent_cues(q),'จ่ายเงินยังไงตอนของ')
    def test_speech_fragment_is_one_transposition(self):
        self.assertEqual(recover_intent_cues('คำพูไดม่เหมาะสม'),'คำพูดไม่เหมาะสม')
    def test_affirmative_and_negative_speech_stay_literal(self):
        for q in ['คำพูดเหมาะสมในศูนย์ควรเป็นยังไง','คำพูดไม่เหมาะสม','ไม่ใช่คำพูดไม่เหมาะสม','อย่าพูดจาดูหมิ่น']:
            with self.subTest(q=q):self.assertEqual(recover_intent_cues(q),q)
    def test_negation_is_not_the_prefix_of_interrogative(self):
        self.assertEqual(recover_intent_cues('ชำระเงินอย่างไครับ'),'ชำระเงินอย่างไรครับ')
        self.assertEqual(recover_intent_cues('อย่าชำระเงินอย่างอื่น'),'อย่าชำระเงินอย่างอื่น')
    def test_reference_bootstrap_preserves_registered_game_and_year(self):
        q='ขออ้างอิงติกา อารีน่าออฟเวเลอร์ ในหัวข้อจำนวยผู้เล่นต่อทีม Blueket 2025'
        recovered=recover_intent_cues(q)
        self.assertIn('กติกา',recovered)
        self.assertEqual(resolve_competition_targets(q).targets,resolve_competition_targets(recovered).targets)
        self.assertIn('2025',recovered)
        self.assertNotIn('จำนวย',recovered)
    def test_unknown_target_does_not_bootstrap_rule_cue(self):
        q='ขออ้างอิงติกา Unknown Game'
        self.assertEqual(recover_intent_cues(q),q)
    def test_valid_words_numbers_urls_and_negation_are_not_rewritten(self):
        for q in ['rice','march','Who are the Embers','Can I pay for VALORANT','PC1 12:00-13:00 ไม่ว่างไหม','VR 30 นาทีไม่ใช่ 60 นาที ราคาเท่าไหร่','กติกา RoV 2026 ไม่ใช่ 2025','https://example.com/paymnt','นาย้ปนไค อ']:
            with self.subTest(q=q):self.assertEqual(recover_intent_cues(q),q)
    def test_rulebooks_are_not_answered_by_general_payment_bridge(self):
        self.assertIsNone(answer_protected_intent('กติกา RoV จ่ายเงินยังไง',locale='th',service=None,rules=RuleMatcher.default().rules))
'''
p=P/'tests/test_source_task_boundaries_r34_20261003.py';assert not p.exists();p.write_text(test,encoding='utf-8')
W=Path(__file__).parent
for old,new in [('r33_unit_all.py','r34_unit_all.py'),('r33_start_web.ps1','r34_start_web.ps1'),('r33_stop_owned_web.ps1','r34_stop_owned_web.ps1')]:
 p=W/new;assert not p.exists();p.write_text((W/old).read_text(encoding='utf-8').replace('r33_report_path.txt','r34_report_path.txt').replace('r33_ready_','r34_ready_'),encoding='utf-8')
print('14 regression tests added; task-owned server helpers copied with new evidence paths')
