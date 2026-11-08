import sys,json,copy,unittest
from datetime import datetime
from unittest.mock import patch
from test_r66_reader import a,B
from harness import configure
from app.knowledge.common.query_scope import derived_names
from app.knowledge.common.registry import template
enabled=len(sys.argv)>1 and sys.argv[1]=='1';configure('common',enabled)
from app.knowledge.common.planner import plan_fields
def read(q,lang='en'):return a.answer(q,locale=lang,at=datetime.fromisoformat('2026-10-14T12:00:00+07:00'),planner=plan_fields if enabled else None)
class ImportedFaq(unittest.TestCase):
 def test_return_policy_does_not_need_network_selection(self):
  with patch('urllib.request.urlopen',side_effect=AssertionError('Exact source topic should not need a model')):
   r=read('What is the studio policy for return equipment games?');self.assertIsNotNone(r);self.assertTrue(r.validation.ok,r.validation.errors);self.assertIn('return',r.answer.lower());self.assertTrue(r.hits);self.assertNotIn('could not select',r.answer)
 def test_source_question_is_not_mutated(self):
  r=template('faq');r['record_id']='faq_a';r['fields']['question'].update(status='known',value={'th':'return_equipment_games','en':'return_equipment_games'});before=copy.deepcopy(r);names={'faq_a':['return_equipment_games']};out=derived_names(names,{'faq_a':r});self.assertIn('return equipment games',out['faq_a']);self.assertEqual(r,before);self.assertEqual(names,{'faq_a':['return_equipment_games']})
 def test_other_kind_ids_are_not_reinterpreted_as_titles(self):
  r=template('game');r['record_id']='some_record_id';self.assertEqual(derived_names({'some_record_id':['Known game']},{'some_record_id':r}),{'some_record_id':['Known game']})
 def test_absent_withdrawn_target_is_not_reintroduced(self):
  r=template('faq');r['record_id']='gone';r['fields']['question'].update(status='known',value={'th':'return_equipment_games','en':'return_equipment_games'});self.assertEqual(derived_names({}, {'gone':r}),{})
 def test_source_digits_are_preserved(self):
  r=template('faq');r['record_id']='faq_b';r['fields']['question'].update(status='known',value={'th':'device_99_rule','en':'device_99_rule'});out=derived_names({'faq_b':[]},{'faq_b':r});self.assertIn('device 99 rule',out['faq_b']);self.assertNotIn('device 9 rule',out['faq_b'])
 def test_normal_owner_question_still_uses_normal_question(self):
  r=template('faq');r['record_id']='f';r['fields']['question'].update(status='known',value={'th':'คืนจอยไว้ตรงไหน','en':'Where should I return a controller?'});out=derived_names({'f':[]},{'f':r});self.assertIn('Where should I return a controller?',out['f'])
if __name__=='__main__':
 r=unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(ImportedFaq));p=B/('IMPORTED_FAQ_TITLES_'+str(len(list(B.glob('IMPORTED_FAQ_TITLES_*.json')))+1)+'.json');p.write_text(json.dumps({'tests_run':r.testsRun,'llm_enabled':enabled,'failures':[{'test':str(t),'stack':s} for t,s in r.failures],'errors':[{'test':str(t),'stack':s} for t,s in r.errors]},ensure_ascii=False,indent=2),encoding='utf-8');raise SystemExit(0 if r.wasSuccessful() else 1)
