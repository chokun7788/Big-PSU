import sys,json,unittest
from datetime import datetime
from test_r66_reader import a,B
from tests.test_common_content_r58 import CommonTests,record
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.dialogue import state_from_answer
from harness import configure
enabled=len(sys.argv)>1 and sys.argv[1]=='1';configure('common',enabled)
from app.knowledge.common.planner import plan_fields
AT=datetime.fromisoformat('2026-10-14T12:00:00+07:00')
def read(reader,q,history=None,lang='en'):return reader.answer(q,locale=lang,history=history,at=AT,planner=plan_fields if enabled else None)
def turn(q,r):return [{'role':'user','content':q},{'role':'assistant','content':r.answer,'common_read_state':state_from_answer(r)}]
class Comparison(unittest.TestCase):
 def setUp(self):
  self.t=CommonTests();self.t.setUp();self.t.fixture()
  r=record('audience');r['fields']['name']['value']={'th':'PSU Student and Staff','en':'PSU Student and Staff'};self.t.approve(self.t.save(r,1))
  r=record('audience','new_general');r['fields']['name']['value']={'th':'General Adult','en':'General Adult'};self.t.approve(self.t.save(r))
  for rid,aid,amount,version in [('fixture_rate','fixture_audience',0,1),('new_rate','new_general',3500,0)]:
   r=record('rate',rid)
   for k,v in {'audience_id':aid,'amount_minor':amount,'currency':'THB','unit':'per_session','duration_minutes':60,'persons_min':1,'persons_max':1,'calculation_rule':'session_ceil'}.items():r['fields'][k].update(status='known',value=v,evidence_refs=[],note=None)
   self.t.approve(self.t.save(r,version))
  self.t.publish();self.reader=CommonAnswerer(self.t.store)
 def tearDown(self):self.t.tearDown()
 def compare(self):return read(self.reader,'Fixture service General Adult and PSU staff same price?')
 def change(self,rid,fn):
  row=self.t.store.get(rid);r=row['record'];fn(r);self.t.approve(self.t.save(r,row['version']));self.t.publish([rid])
 def test_current_different_rates_have_same_billing_basis(self):
  r=self.compare();self.assertTrue(r.validation.ok,r.validation.errors);self.assertEqual(r.decision_artifact['query_plan']['price_comparison']['results'][0]['status'],'different');self.assertIn('current base rates are different',r.answer)
 def test_equal_rates_are_calculated_from_source(self):
  self.change('new_rate',lambda r:r['fields']['amount_minor'].update(value=0));r=self.compare();self.assertTrue(r.validation.ok);self.assertEqual(r.decision_artifact['query_plan']['price_comparison']['results'][0]['status'],'equal')
 def test_expired_operand_does_not_produce_current_equality(self):
  self.change('new_rate',lambda r:r['validity'].update(effective_until='2026-10-01T00:00:00+07:00'));r=self.compare();self.assertTrue(r.validation.ok);self.assertEqual(r.decision_artifact['query_plan']['price_comparison']['results'][0]['status'],'not_confirmed');self.assertNotIn('current base rates are equal',r.answer)
 def test_different_units_cannot_be_compared_as_equal(self):
  self.change('new_rate',lambda r:r['fields']['duration_minutes'].update(value=30));r=self.compare();self.assertTrue(r.validation.ok);self.assertEqual(r.decision_artifact['query_plan']['price_comparison']['results'][0]['reason'],'different_billing_basis')
 def test_missing_service_is_requested_without_all_rate_table(self):
  r=read(self.reader,'General Adult and PSU staff same rate?');self.assertEqual(r.decision_artifact['response_type'],'clarification');self.assertEqual(r.decision_artifact['query_plan']['price_comparison']['missing'],['service']);self.assertNotIn('35.00 THB',r.answer)
 def test_unknown_guest_group_is_not_assumed_as_general_adult(self):
  r=read(a,'Do guests pay the same rate as PSU students?');self.assertTrue(r.validation.ok);self.assertEqual(r.decision_artifact['response_type'],'clarification');self.assertFalse(r.decision_artifact['query_plan']['price_comparison']['guest_group_assumed']);self.assertNotIn('0.00 THB',r.answer)
 def test_missing_service_and_group_are_filled_in_three_turns(self):
  q='Do guests pay the same rate as PSU students?';first=read(a,q);h=turn(q,first);second=read(a,'PC',h);self.assertEqual(second.decision_artifact['query_plan']['price_comparison']['missing'],['at_least_two_explicit_audiences']);h+=turn('PC',second);third=read(a,'General Adult',h);self.assertTrue(third.validation.ok,third.validation.errors);plan=third.decision_artifact['query_plan'];self.assertEqual(len(plan['price_comparison']['audience_ids']),2);self.assertTrue(all(x['status']=='not_confirmed' for x in plan['price_comparison']['results']));self.assertEqual(third.decision_artifact['response_type'],'partial_answer')
 def test_services_comparison_uses_one_explicit_audience(self):
  r=record('service','second_service');r['fields']['name']['value']={'th':'Second Rig','en':'Second Rig'};self.t.approve(self.t.save(r))
  rate=record('rate','second_rate');rate['fields'].update(self.t.store.get('new_rate')['record']['fields']);rate['fields']['service_id'].update(value='second_service',evidence_refs=[]);self.t.approve(self.t.save(rate));self.t.publish(['second_service','second_rate'])
  r=read(self.reader,'Fixture service vs Second Rig, General Adult same price?');self.assertTrue(r.validation.ok,r.validation.errors);plan=r.decision_artifact['query_plan']['price_comparison'];self.assertEqual(plan['axis'],'service',str(plan));self.assertEqual(plan['results'][0]['status'],'equal')
 def test_thai_comparison_asks_only_missing_operands(self):
  r=read(a,'คนนอกกับนักศึกษา ม.อ. จ่ายราคาเท่ากันไหม',lang='th');self.assertEqual(r.decision_artifact['response_type'],'clarification');self.assertNotIn('ราคา: 0.00',r.answer);self.assertTrue(r.validation.ok)
 def test_unobserved_shared_alias_cannot_remove_a_second_named_target(self):
  from app.knowledge.common.answer import named
  self.assertEqual(named('Neon Rig versus Coral Rig',{'a':['Neon Rig','PC'],'b':['Coral Rig','PC']},allow_fuzzy=False),(['a','b'],'exact'))
  self.assertEqual(named('Gaming PC usage',{'a':['PC'],'b':['Gaming PC']},allow_fuzzy=False),(['b'],'exact'))
if __name__=='__main__':
 r=unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(Comparison));p=B/('PRICE_COMPARISON_'+str(len(list(B.glob('PRICE_COMPARISON_*.json')))+1)+'.json');p.write_text(json.dumps({'tests_run':r.testsRun,'llm_enabled':enabled,'synthetic_rates_not_production':True,'failures':[{'test':str(t),'stack':s} for t,s in r.failures],'errors':[{'test':str(t),'stack':s} for t,s in r.errors]},ensure_ascii=False,indent=2),encoding='utf-8');raise SystemExit(0 if r.wasSuccessful() else 1)
