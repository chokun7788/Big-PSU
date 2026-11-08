import sys,json,unittest
from test_r66_reader import a,B
from harness import configure
from datetime import datetime
from app.knowledge.common.registry import value
enabled=len(sys.argv)>1 and sys.argv[1]=='1';configure('common',enabled)
from app.knowledge.common.planner import plan_fields
def read(q,lang='th'):return a.answer(q,locale=lang,at=datetime.fromisoformat('2026-10-14T12:00:00+07:00'),planner=plan_fields if enabled else None)
class ValidationRegressions(unittest.TestCase):
 def test_match_policy_resolves_competition_before_game_policy(self):
  for q in ['I am preparing for a Valo match. What is the policy for pre-match and on-site requirements?','Could you please help me with this: I am preparing for a Counter Strike 2 match. What is the policy for eligibility, roster, and registration']:
   r=read(q,'en');self.assertTrue(r.validation.ok,r.validation.errors);self.assertEqual(r.decision_artifact['query_plan']['operation'],'rules');self.assertIn('Competition rules',r.answer);self.assertTrue(any(o['field']=='text' and o['status']=='known' for o in r.decision_artifact['obligations']))
 def test_protest_policy_does_not_request_game_details(self):
  r=read('Could you please help me with this: I am preparing for a Counter Strike 2 match. What is the policy for protests and disputes','en');self.assertTrue(r.validation.ok,r.validation.errors);self.assertIn('15 minutes',r.answer);self.assertIn('coach',r.answer.lower())
 def test_cancel_question_returns_cancel_source_not_booking_steps(self):
  for q in ['ยกเลิกการจองยังไง','ยกเลิกการจองยังงัย','How do I cancel a booking?']:
   r=read(q,'en' if q.startswith('How') else 'th');self.assertTrue(r.validation.ok,r.validation.errors);self.assertIn('อีเมล' if not q.startswith('How') else 'email',r.answer);self.assertIn('1',r.answer);self.assertNotIn('ขั้นตอนจองคือ',r.answer)
 def test_phone_polite_repetition_keeps_known_answer_valid(self):
  r=read('เบอร์ติดต่อคืออะไรอ่าา');self.assertTrue(r.validation.ok,r.validation.errors);self.assertIn('7627',r.answer);self.assertNotIn('ยังตีความคำถามบางส่วน',r.answer)
 def test_lost_item_question_tail_is_not_a_new_field(self):
  r=read('ของหายทำยังไง');self.assertTrue(r.validation.ok,r.validation.errors);self.assertIn('สูญหาย',r.answer);self.assertNotIn('ยังตีความคำถามบางส่วน',r.answer)
 def test_address_is_typed_before_model_selection(self):
  for q,lang in [('ศูนย์อยู่ตรงไหน','th'),('Where is the studio? Could you check this for me?','en')]:
   r=read(q,lang);self.assertTrue(r.validation.ok,r.validation.errors);self.assertIn('83120',r.answer);self.assertIn('อาคาร 5' if lang=='th' else 'Building 5',r.answer)
 def test_extra_unrelated_faq_clause_is_not_marked_as_complete(self):
  r=read('เบอร์ติดต่อและขออนุญาตยืมเครื่องกลับบ้าน')
  if r:self.assertNotEqual(r.decision_artifact.get('query_plan',{}).get('method'),'common_named_faq_content')
 def test_reviewed_question_translations_preserve_domain(self):
  rs=a.store.snapshot()['release']['records'];self.assertNotIn('zero',value(rs['migrated_owner_claim_contact'],'question')['en']);self.assertNotIn('flight',value(rs['migrated_owner_claim_change_machine'],'question')['en'])
if __name__=='__main__':
 r=unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(ValidationRegressions));p=B/('VALIDATION_REGRESSIONS_'+str(len(list(B.glob('VALIDATION_REGRESSIONS_*.json')))+1)+'.json');p.write_text(json.dumps({'tests_run':r.testsRun,'llm_enabled':enabled,'failures':[{'test':str(t),'stack':s} for t,s in r.failures],'errors':[{'test':str(t),'stack':s} for t,s in r.errors]},ensure_ascii=False,indent=2),encoding='utf-8');raise SystemExit(0 if r.wasSuccessful() else 1)
