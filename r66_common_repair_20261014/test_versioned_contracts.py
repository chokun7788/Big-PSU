import json,unittest,os
from pathlib import Path
from unittest.mock import patch
from test_r66_reader import a
from app.knowledge.common import planner
B=Path(__file__).resolve().parent
class UpdatedContracts(unittest.TestCase):
 def test_invalid_platform_and_boolean_string_are_still_rejected(self):
  with a.store.connect() as c:rs=a.store.heads(c)
  for proposal in [{'requested_fields':['bindings'],'all_fields':False,'platform':'PS4'},{'requested_fields':['bindings'],'all_fields':'true','platform':None}]:self.assertIsNone(planner.checked_plan(proposal,['game_detail_cs2'],rs))
 def test_game_price_schema_requires_a_declared_rate_relation(self):
  with a.store.connect() as c:rs=a.store.heads(c)
  ids=['game_detail_cs2'];proposal={'requested_fields':['amount_minor'],'all_fields':False,'platform':None}
  clean=planner.checked_plan(proposal,ids,rs);self.assertIsNotNone(clean)
  denied,audit=planner.semantic_guard('What genre is this game?',clean,ids,rs);self.assertIsNone(denied)
  allowed,audit=planner.semantic_guard('What is the price?',clean,ids,rs);self.assertIsNotNone(allowed);self.assertEqual(allowed['requested_fields'],['amount_minor'])
 def test_two_batches_are_kept_for_known_how_to_play_clauses(self):
  q=' and '.join(['how to play']*7);p=planner.FieldPlan({'requested_fields':['how_to_play'],'all_fields':False,'platform':None},{'unclear_clauses':[]})
  with patch.dict(os.environ,{'PSU_COMMON_PLAN_MAX_BATCHES':'2'}),patch.object(planner,'_plan_fields_batch',return_value=p) as fetch:
   result=planner.plan_fields(q,{'a':{'kind':'game','fields':{}}},['a']);self.assertIsNotNone(result);self.assertEqual(fetch.call_count,2);self.assertEqual(fetch.call_args.kwargs['whole_question'],q)
 def test_unknown_seven_clauses_are_not_proven_by_a_schema_valid_mock(self):
  q=' and '.join(['unfamiliar feature '+str(n) for n in range(7)]);p=planner.FieldPlan({'requested_fields':['how_to_play'],'all_fields':False,'platform':None},{'unclear_clauses':[]})
  with patch.dict(os.environ,{'PSU_COMMON_PLAN_MAX_BATCHES':'2'}),patch.object(planner,'_plan_fields_batch',return_value=p) as fetch:self.assertIsNone(planner.plan_fields(q,{'a':{'kind':'game','fields':{}}},['a']));self.assertEqual(fetch.call_count,2)
if __name__=='__main__':
 r=unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(UpdatedContracts));p=B/('VERSIONED_CONTRACTS_'+str(len(list(B.glob('VERSIONED_CONTRACTS_*.json')))+1)+'.json');p.write_text(json.dumps({'tests_run':r.testsRun,'failures':[{'test':str(t),'stack':s} for t,s in r.failures],'errors':[{'test':str(t),'stack':s} for t,s in r.errors],'original_tests_modified':False},ensure_ascii=False,indent=2),encoding='utf-8');raise SystemExit(0 if r.wasSuccessful() else 1)
