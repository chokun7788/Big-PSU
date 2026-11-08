import sys,json,unittest,copy
from pathlib import Path
from test_r66_reader import a,answer
from app.knowledge.common.registry import value
from app.knowledge.common.billing import calculate
B=Path(__file__).resolve().parent
class BillingRecovery(unittest.TestCase):
 def setUp(self):
  with a.store.connect() as c:rs=a.store.heads(c)
  self.rate=next(r for r in rs.values() if r['record_id'].startswith('rate_recovered_pc_') and value(r,'amount_minor')==7000)
 def test_matches_existing_calculator_at_session_boundaries(self):
  from app.calculator.service_fee import _sessions_for
  for minutes in [1,30,59,60,61,90,120,121,180]:
   with self.subTest(minutes=minutes):
    r=calculate(self.rate,str(minutes)+' minutes');self.assertEqual(r['units'],_sessions_for('pc',minutes));self.assertEqual(r['amount_minor'],7000*_sessions_for('pc',minutes))
 def test_thai_english_and_word_duration(self):
  for q in ['2 ชั่วโมง','2 hours','two hours','สองชั่วโมง']:self.assertEqual(calculate(self.rate,q)['amount_minor'],14000)
 def test_unknown_rule_never_guesses_a_total(self):
  r=copy.deepcopy(self.rate);r['fields']['calculation_rule'].update(status='unknown',value=None);self.assertIsNone(calculate(r,'2 hours'))
 def test_no_proportional_discount_for_half_session(self):
  self.assertEqual(calculate(self.rate,'30 minutes')['amount_minor'],7000)
 def test_free_does_not_require_dividing_by_zero(self):
  r=copy.deepcopy(self.rate);r['fields']['amount_minor']['value']=0;self.assertEqual(calculate(r,'two hours')['amount_minor'],0)
 def test_no_total_for_unsupported_party_or_multiple_durations(self):
  self.assertIsNone(calculate(self.rate,'2 people for 2 hours'));self.assertIsNone(calculate(self.rate,'compare 30 minutes and 60 minutes'))
 def test_invalid_or_absent_duration_is_not_invented(self):
  for q in ['price please','0 minutes','100000 hours']:self.assertIsNone(calculate(self.rate,q))
 def test_current_source_date_is_not_inferred(self):
  self.assertEqual(self.rate['validity']['state'],'unknown');self.assertIsNone(self.rate['validity']['effective_from']);self.assertIsNone(self.rate['validity']['effective_until'])
 def test_answer_total_is_source_bound_and_validity_caveat_visible(self):
  for q,lang in [('General Adult PC 2 ชั่วโมง กี่บาท','th'),('What is the General Adult PC price for 2 hours?','en')]:
   r=answer(q,lang);self.assertIn('140.00',r.answer);self.assertIn('70.00',r.answer);self.assertIn('ยังไม่ระบุ' if lang=='th' else 'not specified',r.answer);self.assertTrue(r.validation.ok)
 def test_future_and_expired_fees_are_not_calculated(self):
  r=answer('General Adult Nintendo Switch 2 hours price','en');self.assertNotIn('280.00 THB',r.answer);self.assertIn('not effective',r.answer)
if __name__=='__main__':
 r=unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(BillingRecovery));p=B/('BILLING_'+str(len(list(B.glob('BILLING_*.json')))+1)+'.json');p.write_text(json.dumps({'tests_run':r.testsRun,'failures':[{'test':str(t),'stack':s} for t,s in r.failures],'errors':[{'test':str(t),'stack':s} for t,s in r.errors]},ensure_ascii=False,indent=2),encoding='utf-8');sys.exit(0 if r.wasSuccessful() else 1)
