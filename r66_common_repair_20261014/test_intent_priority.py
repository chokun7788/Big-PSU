import sys,json,unittest
from datetime import datetime
from test_r66_reader import a,B
from harness import configure
enabled=len(sys.argv)>1 and sys.argv[1]=='1';configure('common',enabled)
from app.knowledge.common.planner import plan_fields
from app.knowledge.common.query_contract import live_request
def read(q,lang='en'):return a.answer(q,locale=lang,at=datetime.fromisoformat('2026-10-14T12:00:00+07:00'),planner=plan_fields if enabled else None)
class IntentPriority(unittest.TestCase):
 def test_damage_money_is_not_the_service_fee(self):
  for q,lang in [('ถ้าทำ PS5 เสียหาย ต้องเสียค่าปรับกี่บาท','th'),('If I damage a PS5, how much is the fine?','en'),('How much do I pay if I damage PS5?','en')]:
   r=read(q,lang);self.assertTrue(r.validation.ok,r.validation.errors);self.assertEqual(r.decision_artifact['query_plan']['operation'],'policy');self.assertNotIn('Service rate',r.answer);self.assertIn('ค่าปรับ' if lang=='th' else 'damage',r.answer.lower())
 def test_normal_hourly_price_keeps_the_price_operation(self):
  r=read('General Adult PC for 2 hours price?');self.assertIn('140.00 THB',r.answer);self.assertEqual(r.decision_artifact['query_plan']['operation'],'price')
 def test_competition_damage_does_not_become_a_studio_fine(self):
  r=read('Under VALORANT tournament rules, explain when officials may roll back before and after damage.');self.assertEqual(r.decision_artifact['query_plan']['operation'],'rules');self.assertTrue(r.validation.ok,r.validation.errors);self.assertIn('Challenge',r.answer)
 def test_paid_cancel_action_is_not_the_payment_deadline(self):
  for q,lang in [('How do I cancel a paid booking?','en'),('จ่ายแล้วจะยกเลิกการจองยังไง','th')]:
   r=read(q,lang);self.assertTrue(r.validation.ok,r.validation.errors);self.assertIn('email' if lang=='en' else 'อีเมล',r.answer);self.assertNotIn('10 minutes' if lang=='en' else '10 นาที',r.answer)
 def test_unpaid_automatic_cancel_still_uses_payment_source(self):
  for q,lang in [("What happens if I don't pay within 10 minutes after booking?",'en'),('หลังจองไม่จ่ายใน 10 นาทีจะถูกยกเลิกไหม','th')]:
   r=read(q,lang);self.assertTrue(r.validation.ok,r.validation.errors);self.assertIn('10',r.answer);self.assertIn('cancel' if lang=='en' else 'ยกเลิก',r.answer.lower())
 def test_time_and_availability_win_over_static_installation(self):
  for q,lang in [('Is PC #03 available for Warzone today at 15:00?','en'),('ตอน 15:00 PC #03 ว่างเล่น Warzone ไหม','th')]:
   self.assertTrue(live_request(q));self.assertIsNone(read(q,lang))
 def test_static_installed_game_still_reads_declared_source(self):
  r=read('Does PC #03 have Call of Duty: Warzone installed?');self.assertEqual(r.decision_artifact['query_plan']['method'],'declared_game_installation_scope');self.assertIn('PC #03',r.answer)
 def test_current_game_catalog_is_static_and_keeps_new_common_data(self):
  from tests.test_common_content_r58 import CommonTests
  from app.knowledge.common.answer import CommonAnswerer
  t=CommonTests();t.setUp()
  try:
   t.fixture();q='What games are currently available?';self.assertFalse(live_request(q));r=CommonAnswerer(t.store).answer(q,locale='en',at=datetime.fromisoformat('2026-10-14T12:00:00+07:00'));self.assertIn('Starfish Quest',r.answer);self.assertEqual(r.decision_artifact['query_plan']['method'],'offered_game_service_catalog')
  finally:t.tearDown()
 def test_live_pipeline_uses_the_unavailable_fixture_not_an_installed_game_answer(self):
  from harness import init,execute
  init('common',enabled)
  q='Is PC #03 available for Warzone today at 15:00?';result=execute({'key':'r66_priority_live','question':q,'locale':'en','reference_date':'','entries':[]})
  self.assertFalse(result.get('exception'),result.get('exception'));r=result['result'];self.assertIn('live_booking_status_unavailable',r['mode']);self.assertNotIn('Confirmed game records',r['answer'])
 def test_draft_route_reason_does_not_claim_approval(self):
  r=read('PC price?');self.assertFalse(r.decision_artifact['production_publication_verified']);self.assertNotIn('approved',r.route.reason);self.assertIn('draft',r.route.reason)
if __name__=='__main__':
 r=unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(IntentPriority));p=B/('INTENT_PRIORITY_'+str(len(list(B.glob('INTENT_PRIORITY_*.json')))+1)+'.json');p.write_text(json.dumps({'tests_run':r.testsRun,'llm_enabled':enabled,'actual_new_wordpress_oracle':False,'failures':[{'test':str(t),'stack':s} for t,s in r.failures],'errors':[{'test':str(t),'stack':s} for t,s in r.errors]},ensure_ascii=False,indent=2),encoding='utf-8');raise SystemExit(0 if r.wasSuccessful() else 1)
