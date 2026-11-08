import sys,json,unittest
from datetime import datetime
from unittest.mock import patch
from test_r66_reader import a,B
from harness import configure
from app.knowledge.common.faq_topics import select
enabled=len(sys.argv)>1 and sys.argv[1]=='1';configure('common',enabled)
from app.knowledge.common.planner import plan_fields
def read(q,lang='en'):return a.answer(q,locale=lang,at=datetime.fromisoformat('2026-10-14T12:00:00+07:00'),planner=plan_fields if enabled else None)
class ReturnPolicy(unittest.TestCase):
 def test_policy_uses_existing_content_without_a_model(self):
  with patch('urllib.request.urlopen',side_effect=AssertionError('Known policy should not need a model')):
   for q,lang in [('What is the studio policy for return equipment games?','en'),('What is the policy on returning equipment and game discs?','en'),('นโยบายการคืนอุปกรณ์และแผ่นเกมเป็นยังไง','th')]:
    r=read(q,lang);self.assertIsNotNone(r);self.assertTrue(r.validation.ok,r.validation.errors);self.assertIn('after use' if lang=='en' else 'ใช้งานเสร็จ',r.answer);self.assertTrue(r.hits)
 def test_refunds_are_not_equipment_returns(self):
  with a.store.connect() as c:records=a.store.heads(c)
  self.assertEqual(select('What is the refund policy for game equipment?',records,'policy'),[])
 def test_competition_returns_are_not_studio_policy(self):
  with a.store.connect() as c:records=a.store.heads(c)
  self.assertEqual(select('Under tournament rules, return equipment games?',records,'rules'),[])
 def test_no_source_does_not_invent_return_rules(self):
  self.assertEqual(select('What is the policy for return equipment games?',{},'policy'),[])
 def test_record_id_is_not_used_as_a_question(self):
  from app.knowledge.common.registry import template
  r=template('faq');r['record_id']='return_equipment_games';r['fields']['question'].update(status='known',value={'th':'ติดต่อ','en':'Contact'});self.assertEqual(select('What is the policy for return equipment games?',{'return_equipment_games':r},'policy'),[])
 def test_other_policy_is_not_replaced_by_return_topic(self):
  with a.store.connect() as c:records=a.store.heads(c)
  ids=select('Can I plug in my laptop?',records,'policy');self.assertTrue(ids);self.assertNotIn('migrated_faq_curated_rule_return_equipment',ids)
if __name__=='__main__':
 r=unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(ReturnPolicy));p=B/('RETURN_POLICY_'+str(len(list(B.glob('RETURN_POLICY_*.json')))+1)+'.json');p.write_text(json.dumps({'tests_run':r.testsRun,'llm_enabled':enabled,'failures':[{'test':str(t),'stack':s} for t,s in r.failures],'errors':[{'test':str(t),'stack':s} for t,s in r.errors]},ensure_ascii=False,indent=2),encoding='utf-8');raise SystemExit(0 if r.wasSuccessful() else 1)
