import sys,json,unittest
from datetime import datetime
from unittest.mock import patch
from test_r66_reader import a,B
from harness import configure
from app.knowledge.common import entity_search
from app.knowledge.common.query_scope import operation
enabled=len(sys.argv)>1 and sys.argv[1]=='1';configure('common',enabled)
from app.knowledge.common.planner import plan_fields
def read(q,lang='en'):return a.answer(q,locale=lang,at=datetime.fromisoformat('2026-10-14T12:00:00+07:00'),planner=plan_fields if enabled else None)
class SelectorLatency(unittest.TestCase):
 def test_personal_laptop_permission_from_existing_source(self):
  for q,lang in [('Can a visitor plug in their own laptop?','en'),('May I plug in my personal laptop?','en'),('เอาโน้ตบุ๊กส่วนตัวมาเสียบปลั๊กไฟได้ไหม','th')]:
   r=read(q,lang);self.assertTrue(r.validation.ok,r.validation.errors);self.assertRegex(r.answer,r'permission|authorization' if lang=='en' else 'อนุญาต');self.assertEqual(r.decision_artifact['query_plan']['operation'],'policy')
 def test_missing_power_source_does_not_create_a_policy(self):
  from app.knowledge.common.faq_topics import select
  self.assertEqual(select('Can I plug in my laptop?',{},'policy'),[])
 def test_competition_is_not_studio_power_permission(self):
  self.assertEqual(operation('Under VALORANT tournament rules, may I plug in personal equipment?'),'rules')
 def test_normal_price_and_peripherals_do_not_use_power_policy(self):
  from app.knowledge.common.faq_topics import select
  with a.store.connect() as c:records=a.store.heads(c)
  self.assertEqual(operation('How much does charging a laptop cost?'),'price');self.assertEqual(select('May I bring my own keyboard?',records,'policy'),[])
 def test_unanchored_noise_does_not_call_the_model(self):
  with a.store.connect() as c:records=a.store.heads(c)
  with patch.object(entity_search,'candidates',return_value=[{'record_id':'migrated_faq_curated_rule_power_outlet','score':.9,'kind':'faq','text':'power outlet permission'}]),patch.object(entity_search.urllib.request,'urlopen',side_effect=AssertionError('No model call for an unanchored candidate')) as call:
   result,audit=entity_search.select('asdfghjkl',records,{})
   self.assertIsNone(result);self.assertFalse(audit['attempted']);self.assertEqual(audit['reason'],'no_independent_topic_anchor');call.assert_not_called()
 def test_alignment_still_rejects_other_selected_candidates(self):
  with a.store.connect() as c:records=a.store.heads(c)
  self.assertFalse(entity_search.topic_alignment('asdfghjkl',records['migrated_faq_curated_rule_power_outlet'])[0])
 def test_existing_source_question_remains_supported(self):
  r=read('What happens if I damage equipment?');self.assertIn('100-500 THB',r.answer);self.assertNotIn('4.8',r.answer)
if __name__=='__main__':
 r=unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(SelectorLatency));p=B/('SELECTOR_LATENCY_'+str(len(list(B.glob('SELECTOR_LATENCY_*.json')))+1)+'.json');p.write_text(json.dumps({'tests_run':r.testsRun,'llm_enabled':enabled,'failures':[{'test':str(t),'stack':s} for t,s in r.failures],'errors':[{'test':str(t),'stack':s} for t,s in r.errors]},ensure_ascii=False,indent=2),encoding='utf-8');raise SystemExit(0 if r.wasSuccessful() else 1)
