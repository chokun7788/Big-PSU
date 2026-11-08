import sys,json,unittest
from pathlib import Path
from unittest.mock import patch
from test_r66_reader import B
from tests.test_common_content_r58 import CommonTests
from app.knowledge.common.answer import CommonAnswerer
class Projection(unittest.TestCase):
 def setUp(self):self.t=CommonTests();self.t.setUp();self.t.fixture()
 def tearDown(self):self.t.tearDown()
 def read(self,q):
  with patch('app.knowledge.common.entity_search.select',return_value=(['fixture_faq'],{'attempted':False,'reason':'mocked_selector_for_projection_only'})):
   return CommonAnswerer(self.t.store).answer(q,locale='en',planner=lambda *args:None)
 def test_unknown_unrequested_scope_does_not_degrade_a_known_faq_answer(self):
  r=self.read('Please explain the example');self.assertEqual(r.decision_artifact['response_type'],'answer');self.assertEqual(r.decision_artifact['query_plan']['requested_fields'],['answer']);self.assertNotIn('Not yet confirmed',r.answer);self.assertTrue(r.validation.ok)
 def test_explicit_scope_request_still_reports_the_unknown(self):
  r=self.read('Please explain the example and its scope');self.assertIn('scope_note',r.decision_artifact['query_plan']['requested_fields']);self.assertEqual(r.decision_artifact['response_type'],'partial_answer');self.assertIn('Not yet confirmed',r.answer);self.assertTrue(r.validation.ok)
if __name__=='__main__':
 r=unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(Projection));p=B/('FAQ_PROJECTION_'+str(len(list(B.glob('FAQ_PROJECTION_*.json')))+1)+'.json');p.write_text(json.dumps({'tests_run':r.testsRun,'failures':[{'test':str(t),'stack':s} for t,s in r.failures],'errors':[{'test':str(t),'stack':s} for t,s in r.errors],'model_selector_mocked':True,'synthetic_fixture_only':True},ensure_ascii=False,indent=2),encoding='utf-8');raise SystemExit(0 if r.wasSuccessful() else 1)
