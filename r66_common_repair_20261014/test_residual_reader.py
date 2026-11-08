import sys,json,unittest
from pathlib import Path
from test_r66_reader import answer,a,B
llm_enabled=len(sys.argv)>1 and sys.argv[1]=='1'
if llm_enabled:
 from harness import configure
 from app.knowledge.common.planner import plan_fields
 from datetime import datetime
 configure('common',True)
 def answer(q,lang='th',history=None):return a.answer(q,locale=lang,history=history,at=datetime.fromisoformat('2026-10-14T12:00:00+07:00'),planner=plan_fields)
class Residual(unittest.TestCase):
 def test_player_team_limit_is_not_the_rulebook_scope(self):
  r=answer('How many teams may a CS2 tournament player represent?','en');self.assertIn('one team',r.answer.lower());self.assertNotIn('Scope of Application',r.answer)
 def test_forfeit_score_keeps_the_recorded_result(self):
  r=answer('Under VALORANT tournamment rules, what score is recorded for a map forfeit?','en');self.assertIn('13-0',r.answer);self.assertNotIn('**Types of penalties in the game**',r.answer)
 def test_protest_typo_keeps_deadline_without_generic_scope(self):
  r=answer('Under CS2 tournament rules, what deadline applies when a coach submits a proest after the match?','en');self.assertIn('15 minutes',r.answer);self.assertIn('coach',r.answer.lower());self.assertNotIn('Scope of Application',r.answer)
 def test_indestructible_rule_translation_does_not_flip_polarity(self):
  r=answer('Under VALORANT tournament rules, may abilities be used outside map boundaries for information?','en');self.assertIn('indestructible',r.answer);self.assertNotIn('on destructible locations',r.answer)
 def test_translation_guard_detects_the_observed_concept_errors(self):
  from app.knowledge.common.translation import validate_translation
  for th,en in [('จุดที่ทำลายไม่ได้','destructible locations'),('เหรัญญิก','Priest'),('หมากฝรั่ง','Checkers'),('ผศ.ดร.สมชาย','Professor Somchai')]:
   with self.assertRaises(ValueError):validate_translation(th,en)
  self.assertEqual(validate_translation('จุดที่ทำลายไม่ได้','indestructible locations'),'indestructible locations')
 def test_existing_owner_address_reads_in_both_languages(self):
  for q,lang in [('ศูนย์อยู่ตรงไหน','th'),('Where is the studio? Could you check this for me?','en')]:
   r=answer(q,lang);self.assertIn('83120',r.answer);self.assertIn('อาคาร 5' if lang=='th' else 'Building 5',r.answer);self.assertIn('กะทู้' if lang=='th' else 'Kathu',r.answer);self.assertNotIn('Kata Noi',r.answer);self.assertTrue(r.validation.ok)
 def test_equipment_family_query_does_not_expand_to_whole_zone(self):
  r=answer('Please tell me: What is the Gaming PC used for? Please answer briefly.','en');self.assertIn('Gaming PC',r.answer);self.assertIn('esports',r.answer.lower());self.assertNotIn('**Gaming Chair**',r.answer);self.assertNotIn('**Gaming Headset**',r.answer)
 def test_damage_policy_keeps_service_scope_without_service_field_picker(self):
  for q,lang in [('ถ้าทำ PS5 ของศูนย์เสียหายต้องเสียค่าปรับไหม','th'),('If I damage a studio PS5, is there a penalty?','en')]:
   r=answer(q,lang);self.assertIn('ค่าปรับ' if lang=='th' else 'damage',r.answer.lower());self.assertNotIn('Which part',r.answer);self.assertNotIn('ยังตีความ',r.answer);self.assertTrue(r.validation.ok)
 def test_lost_time_compensation_is_not_equipment_damage_fine(self):
  r=answer('PC crashed and I lost 10 minutes. Is there compensation?','en')
  if r:self.assertNotIn('100-500',r.answer);self.assertNotIn('100–500',r.answer);self.assertNotIn('100 – 500',r.answer)
 def test_payment_after_booking_reads_deadline(self):
  for q,lang in [('ขอข้อมูลเรื่องชำระเงินหลัง booking ขอรายละเอียดแบบสั้น ๆ','th'),('How soon must I pay after booking?','en')]:
   r=answer(q,lang);self.assertIn('10',r.answer);self.assertIn('ยกเลิก' if lang=='th' else 'cancel',r.answer.lower());self.assertTrue(r.validation.ok)
 def test_booking_required_is_not_just_generic_steps(self):
  for q,lang in [('ไม่จองเข้าใช้ VR ได้ไหม','th'),('Can visitors use VR without booking?','en')]:
   r=answer(q,lang);self.assertIn('จอง' if lang=='th' else 'book',r.answer.lower());self.assertIn('ก่อน' if lang=='th' else 'before',r.answer.lower());self.assertNotIn('The booking steps are',r.answer);self.assertTrue(r.validation.ok)
 def test_specific_game_resource_presence_uses_installed_ids(self):
  r=answer('PC #03 มี Call of Duty: Warzone ไหม');self.assertIn('Call of Duty: Warzone',r.answer);self.assertIn('PC #03',r.answer);self.assertEqual(r.decision_artifact['query_plan']['method'],'declared_game_installation_scope');self.assertTrue(r.validation.ok)
 def test_game_not_in_target_list_is_not_invented_as_installed(self):
  r=answer('อยากรูเว่า PC #01 มี Call of Duty: Warzone ไหม');self.assertIn('PC #03-#10',r.answer);self.assertIn('ยังไม่พบ',r.answer);self.assertEqual(r.decision_artifact['response_type'],'partial_answer');self.assertFalse(r.decision_artifact['query_plan']['negative_from_absence'])
 def test_unknown_machine_number_is_preserved(self):
  r=answer('Does PC #99 have Call of Duty: Warzone?','en');self.assertIsNotNone(r);self.assertIn('PC #99',r.answer);self.assertEqual(r.decision_artifact['response_type'],'partial_answer')
 def test_ps5_platform_equivalence_does_not_hide_expired_source(self):
  r=answer('How much does PS5 cost for PSU staff? Please use verified information.','en');self.assertNotIn('No confirmed price for',r.answer);self.assertIn('not effective',r.answer);self.assertNotIn('0.00 THB',r.answer)
if __name__=='__main__':
 r=unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(Residual));p=B/('RESIDUAL_READER_'+str(len(list(B.glob('RESIDUAL_READER_*.json')))+1)+'.json');p.write_text(json.dumps({'tests_run':r.testsRun,'failures':[{'test':str(t),'stack':s} for t,s in r.failures],'errors':[{'test':str(t),'stack':s} for t,s in r.errors]},ensure_ascii=False,indent=2),encoding='utf-8');raise SystemExit(0 if r.wasSuccessful() else 1)
