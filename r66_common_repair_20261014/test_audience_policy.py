"""Source labels constrain audience meaning; unknown policy must answer the gap."""
import sys,json,copy,unittest
from test_r66_reader import a,B
from app.knowledge.common.audience_scope import resolve
from app.knowledge.common.registry import value
from tests.test_common_content_r58 import record
from app.knowledge.common.budget import budget_request
from harness import configure
from datetime import datetime
enabled=len(sys.argv)>1 and sys.argv[1]=='1';configure('common',enabled)
from app.knowledge.common.planner import plan_fields
def read(q,lang='th'):return a.answer(q,locale=lang,at=datetime.fromisoformat('2026-10-14T12:00:00+07:00'),planner=plan_fields if enabled else None)
class AudiencePolicy(unittest.TestCase):
 def setUp(self):self.records=a.store.snapshot()['release']['records']
 def selected_rates(self,result):
  plan=result.decision_artifact['query_plan'];return [r for rid,r in self.records.items() if r['kind']=='rate' and rid in {o['record_id'] for o in result.decision_artifact['obligations']}]
 def test_thai_adult_price_does_not_include_student_or_staff(self):
  r=read('เล่น PC 2 ชั่วโมง บุคคลทั่วไปกี่บาท');self.assertIn('140.00 THB',r.answer);self.assertNotIn('50.00 THB',r.answer);self.assertNotIn('ราคา: 0.00 THB',r.answer);self.assertTrue(r.validation.ok)
  groups={value(self.records[value(rate,'audience_id')],'name')['en'] for rate in self.selected_rates(r)};self.assertEqual(groups,{'General Adult'})
 def test_english_adult_price_matches_thai_scope(self):
  r=read('PC for 2 hours, general adult price?','en');self.assertIn('140.00 THB',r.answer);self.assertNotIn('50.00 THB',r.answer);self.assertTrue(r.validation.ok)
 def test_alumni_price_uses_existing_combined_group(self):
  r=read('ศิษย์เก่า เล่น PC 2 ชั่วโมงกี่บาท');self.assertIn('50.00 THB',r.answer);self.assertNotIn('140.00 THB',r.answer)
 def test_not_affiliated_is_not_a_positive_audience(self):
  for q in ['ไม่ใช่นักศึกษา','not PSU staff','ไม่ได้เป็นบุคคลทั่วไป','not a general adult']:
   ids,audit=resolve(q,self.records);self.assertEqual(ids,[]);self.assertTrue(audit['negated_group_removed'])
 def test_unknown_outsider_is_not_assumed_adult(self):
  for q in ['คนนอก','บุคคลภายนอก','outside visitor']:
   ids,audit=resolve(q,self.records);self.assertIsNone(ids)
 def test_psu_alumni_label_does_not_select_psu_staff_too(self):
  ids,_=resolve('PSU Alumni and General Student',self.records);self.assertEqual(len(ids),1);self.assertIn('Alumni',value(self.records[ids[0]],'name')['en'])
 def test_psu_staff_is_resolved_from_label(self):
  for q in ['PSU staff','บุคลากรมอ','บุคลากร ม.อ.']:
   ids,_=resolve(q,self.records);self.assertEqual(len(ids),1);self.assertIn('Staff',value(self.records[ids[0]],'name')['en'])
 def test_id_is_not_used_as_a_taxonomy_label(self):
  r=record('audience','unrelated_uuid');r['fields']['name']['value']={'th':'General Adult','en':'General Adult'}
  ids,_=resolve('บุคคลทั่วไป',{'unrelated_uuid':r});self.assertEqual(ids,['unrelated_uuid'])
 def test_missing_source_group_is_not_invented(self):
  r=record('audience','audience_general_adult');r['fields']['name']['value']={'th':'VIP tournament guest','en':'VIP tournament guest'}
  ids,_=resolve('บุคคลทั่วไป',{'audience_general_adult':r});self.assertEqual(ids,[])
 def test_negative_then_explicit_other_group(self):
  ids,_=resolve('not PSU staff; general adult',self.records);self.assertEqual(len(ids),1);self.assertEqual(value(self.records[ids[0]],'name')['en'],'General Adult')
 def test_budget_filters_to_resolved_group(self):
  ids,_=resolve('บุคคลทั่วไป',self.records);result=budget_request('บุคคลทั่วไป มีเงิน 200 บาท เล่น PC ได้นานไหม',self.records,ids)
  self.assertTrue(result['rows']);self.assertTrue(all(row['audience_id'] in ids for row in result['rows']))
 def test_budget_question_uses_audience_in_the_real_reader(self):
  r=read('บุคคลทั่วไปมีเงิน 200 บาท เล่น PC ได้นานไหม');rows=r.decision_artifact['query_plan']['budget']['rows'];self.assertTrue(rows);self.assertTrue(all(value(self.records[row['audience_id']],'name')['en']=='General Adult' for row in rows))
 def test_unknown_age_policy_names_the_missing_topic(self):
  for q,lang in [('เด็กอายุ 12 ใช้ VR ได้ไหม','th'),('Can a 12 years old visitor use VR?','en')]:
   r=read(q,lang);self.assertEqual(r.decision_artifact['response_type'],'partial_answer');self.assertIn('อายุขั้นต่ำ' if lang=='th' else 'minimum age',r.answer);self.assertNotIn('Which part',r.answer);self.assertTrue(r.validation.ok)
 def test_unknown_take_home_does_not_invent_permission(self):
  for q,lang in [('ไม่ใช่นักศึกษา แต่อยากยืม PS5 กลับบ้านได้ไหม','th'),('Can I borrow PS5 to take home?','en')]:
   r=read(q,lang);self.assertEqual(r.decision_artifact['query_plan']['method'],'common_policy_unconfirmed');self.assertIn('ยังไม่มีข้อมูลยืนยัน' if lang=='th' else 'not confirmed',r.answer);self.assertTrue(r.validation.ok)
 def test_known_damage_policy_is_not_replaced_by_unknown(self):
  r=read('ถ้าทำ PS5 ของศูนย์เสียหายต้องเสียค่าปรับไหม');self.assertIn('ค่าปรับ',r.answer);self.assertNotEqual(r.decision_artifact['query_plan']['method'],'common_policy_unconfirmed')
 def state_history(self,q,r):
  from app.knowledge.common.dialogue import state_from_answer
  return [{'role':'user','content':q},{'role':'assistant','content':r.answer,'common_read_state':state_from_answer(r)}]
 def follow(self,q,history,lang='th'):return a.answer(q,locale=lang,history=history,at=datetime.fromisoformat('2026-10-14T12:00:00+07:00'),planner=plan_fields if enabled else None)
 def test_thai_followup_changes_audience_or_duration_without_old_price(self):
  q='บุคคลทั่วไปเล่น PC 2 ชั่วโมงกี่บาท';first=read(q);h=self.state_history(q,first)
  r=self.follow('ถ้าเป็นศิษย์เก่าล่ะ',h);self.assertTrue(r.validation.ok,r.validation.errors);self.assertIn('รวม 50.00 THB',r.answer);self.assertNotIn('รวม 140.00 THB',r.answer);self.assertEqual(r.decision_artifact['query_plan']['inherited_constraints'],{'duration_minutes':120})
  r=self.follow('แล้ว 1 ชั่วโมงล่ะ',h);self.assertTrue(r.validation.ok,r.validation.errors);self.assertIn('รวม 70.00 THB',r.answer);self.assertNotIn('รวม 140.00 THB',r.answer)
 def test_english_three_turns_keep_only_requested_constraints(self):
  q='PC for 2 hours, general adult price?';first=read(q,'en');h=self.state_history(q,first)
  second=self.follow('What about alumni?',h,'en');self.assertTrue(second.validation.ok,second.validation.errors);self.assertIn('total 50.00 THB',second.answer)
  h+=self.state_history('What about alumni?',second);third=self.follow('And for 1 hour?',h,'en');self.assertTrue(third.validation.ok,third.validation.errors);self.assertIn('total 25.00 THB',third.answer);self.assertNotIn('total 50.00 THB',third.answer)
 def test_price_constraints_do_not_leak_into_new_topic(self):
  q='บุคคลทั่วไปเล่น PC 2 ชั่วโมงกี่บาท';first=read(q);h=self.state_history(q,first)
  r=self.follow('PS5 มีเกมอะไรบ้าง',h);self.assertIn('TEKKEN 8',r.answer);self.assertNotIn('inherited_constraints',r.decision_artifact['query_plan'])
  r=self.follow('ถ้าเป็นศิษย์เก่าแล้วขอยืมเครื่องกลับบ้านด้วย',h)
  if r:self.assertNotEqual(r.decision_artifact.get('query_plan',{}).get('method'),'state_audience_selection')
if __name__=='__main__':
 r=unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(AudiencePolicy));p=B/('AUDIENCE_POLICY_'+str(len(list(B.glob('AUDIENCE_POLICY_*.json')))+1)+'.json');p.write_text(json.dumps({'tests_run':r.testsRun,'llm_enabled':enabled,'failures':[{'test':str(t),'stack':s} for t,s in r.failures],'errors':[{'test':str(t),'stack':s} for t,s in r.errors]},ensure_ascii=False,indent=2),encoding='utf-8');raise SystemExit(0 if r.wasSuccessful() else 1)
