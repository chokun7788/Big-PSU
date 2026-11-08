"""New scoped data, natural topic queries; synthetic sources only."""
import sys,json,unittest,copy,os
from test_r66_reader import B
from tests.test_common_content_r58 import CommonTests,record
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.scoped_topics import lookup,scoped
from app.knowledge.common.query_scope import derived_names
from app.knowledge.common.registry import value
from datetime import datetime
enabled=len(sys.argv)>1 and sys.argv[1]=='1'
os.environ['PSU_LOCAL_LLM_ASSIST_ENABLED']='1' if enabled else '0'
from app.knowledge.common.planner import plan_fields
class ScopedTopics(unittest.TestCase):
 def setUp(self):
  self.t=CommonTests();self.t.setUp();self.t.fixture()
  for rid,name in [('fixture_service','Neon Rig'),('other_service','Coral Rig')]:
   r=record('service',rid);r['fields']['name']['value']={'th':name,'en':name}
   self.t.approve(self.t.save(r,1 if rid=='fixture_service' else 0))
  for rid,sid,answer in [('new_install','fixture_service','Ask staff before installing; sample A.'),('other_install','other_service','Never install; sample B.')]:
   r=record('faq',rid)
   for key,v in {'question':{'th':'ติดตั้งเกมเพิ่มได้ไหม','en':'May I install additional games?'},'answer':{'th':'ถามเจ้าหน้าที่ก่อนติดตั้ง ตัวอย่าง A' if rid=='new_install' else 'ห้ามติดตั้ง ตัวอย่าง B','en':answer},'related_ids':[sid]}.items():r['fields'][key].update(status='known',value=v,evidence_refs=[],note=None)
   self.t.approve(self.t.save(r))
  self.t.publish();self.reader=CommonAnswerer(self.t.store)
 def tearDown(self):self.t.tearDown()
 def read(self,q,lang='en'):return self.reader.answer(q,locale=lang,at=datetime.fromisoformat('2026-10-14T12:00:00+07:00'),planner=plan_fields if enabled else None)
 def test_new_scoped_faq_is_read_in_both_languages(self):
  for q,lang in [('May I install additional games on Neon Rig?','en'),('Neon Rig ติดตั้งเกมเพิ่มได้ไหม','th')]:
   r=self.read(q,lang);self.assertIsNotNone(r);self.assertIn('sample A' if lang=='en' else 'ตัวอย่าง A',r.answer);self.assertNotIn('sample B',r.answer);self.assertEqual(r.decision_artifact['query_plan']['method'],'declared_scoped_topic');self.assertTrue(r.validation.ok)
 def test_other_scope_does_not_leak(self):
  r=self.read('May I install additional games on Coral Rig?');self.assertIn('sample B',r.answer);self.assertNotIn('sample A',r.answer)
 def test_new_policy_reads_declared_conditions_and_details(self):
  r=record('policy','new_photography');r['fields']['subject']['value']={'th':'ถ่ายรูปได้ไหม','en':'May I take photographs?'};r['fields']['topic']['value']='photographs';r['fields']['conditions_all']['value']=[{'field':'service_id','operator':'eq','value':'fixture_service'}];r['fields']['details']['value']={'th':'ตัวอย่าง ต้องไม่ติดหน้าผู้อื่น','en':'Sample: exclude other visitors from photographs.'};self.t.approve(self.t.save(r));self.t.publish(['new_photography'])
  a=self.read('May I take photographs on Neon Rig?');self.assertIn('exclude other visitors',a.answer);self.assertIn('conditions_all',a.decision_artifact['query_plan']['requested_fields']);self.assertTrue(a.validation.ok)
 def test_new_procedure_reads_steps(self):
  r=record('procedure','new_account_recovery');r['fields']['topic']['value']='account recovery';r['fields']['steps']['value']=[{'order':1,'instruction':{'th':'ตัวอย่าง แจ้งเจ้าหน้าที่เพื่อกู้บัญชี','en':'Sample: contact staff for account recovery.'},'contact_id':None}];self.t.approve(self.t.save(r));self.t.publish(['new_account_recovery'])
  a=self.read('Neon Rig account recovery please');self.assertIn('contact staff for account recovery',a.answer);self.assertEqual(a.decision_artifact['query_plan']['method'],'declared_scoped_topic');self.assertTrue(a.validation.ok)
 def test_procedure_preconditions_do_not_cross_service(self):
  for rid,sid,instruction in [('neon_recovery','fixture_service','Neon staff recovery only'),('coral_recovery','other_service','Coral self-service recovery only')]:
   r=record('procedure',rid);r['fields']['topic']['value']='account recovery';r['fields']['preconditions']['value']=[{'field':'service_id','operator':'eq','value':sid}];r['fields']['steps']['value']=[{'order':1,'instruction':{'th':instruction,'en':instruction},'contact_id':None}];self.t.approve(self.t.save(r))
  self.t.publish(['neon_recovery','coral_recovery'])
  for device,want,forbid in [('Neon Rig','Neon staff recovery','Coral self-service'),('Coral Rig','Coral self-service','Neon staff recovery')]:
   a=self.read(device+' account recovery please');self.assertIn(want,a.answer);self.assertNotIn(forbid,a.answer);self.assertTrue(a.validation.ok)
 def test_unknown_owned_attribute_does_not_borrow_faq(self):
  r=self.read('Neon Rig maximum duration minutes');self.assertNotIn('sample A',r.answer);self.assertNotEqual(r.decision_artifact['query_plan']['method'],'declared_scoped_topic')
 def test_live_does_not_borrow_static_faq(self):
  self.assertIsNone(self.read('Is Neon Rig available now?'))
 def test_name_alone_is_not_topic(self):
  r=self.read('Can Neon Rig explain quantum gravity?')
  if r:self.assertNotIn('sample A',r.answer);self.assertNotIn('sample B',r.answer)
 def test_declared_policy_conditions_and_unknown_procedure_are_filtered(self):
  r=record('policy');r['fields']['conditions_all']['value']=[{'field':'service_id','operator':'eq','value':'other_service'}]
  self.assertFalse(scoped(r,{'fixture_service'}));self.assertTrue(scoped(r,{'other_service'}))
  r=record('procedure');r['fields']['preconditions'].update(status='unknown',value=None)
  self.assertFalse(scoped(r,{'fixture_service'}))
  r['fields']['preconditions'].update(status='known',value=[{'field':'resource_id','operator':'eq','value':'other_resource'}]);self.assertFalse(scoped(r,{'fixture_resource'}));self.assertTrue(scoped(r,{'other_resource'}))
 def test_unresolved_number_cannot_select_known_resource(self):
  records=self.t.store.snapshot()['release']['records'];names=derived_names({},records)
  ids,audit=lookup('Neon Rig PC #99 install games',records,names,['fixture_service'],allow_llm=enabled)
  self.assertIsNone(ids);self.assertEqual(audit['reason'],'numbered_target_unresolved')
 def test_root_validity_is_not_bypassed(self):
  r=self.t.store.get('fixture_service')['record'];r['validity']['effective_until']='2026-10-01T00:00:00+07:00';self.t.approve(self.t.save(r,2));self.t.publish(['fixture_service'])
  r=self.read('May I install additional games on Neon Rig?');self.assertNotIn('sample A',r.answer);self.assertNotEqual(r.decision_artifact['query_plan']['method'],'declared_scoped_topic')
if __name__=='__main__':
 r=unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(ScopedTopics));p=B/('SCOPED_TOPICS_'+str(len(list(B.glob('SCOPED_TOPICS_*.json')))+1)+'.json');p.write_text(json.dumps({'tests_run':r.testsRun,'llm_enabled':enabled,'synthetic_fixture_only':True,'failures':[{'test':str(t),'stack':s} for t,s in r.failures],'errors':[{'test':str(t),'stack':s} for t,s in r.errors]},ensure_ascii=False,indent=2),encoding='utf-8');raise SystemExit(0 if r.wasSuccessful() else 1)
