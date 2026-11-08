import sys,os,unittest,json
from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
sys.path.insert(0,str(P));os.environ['PYTHONDONTWRITEBYTECODE']='1'
from app.session.context_resolver import resolve_question_with_context
from app.pipeline.competition_conversation_signals import is_broad_rule_request,is_rulebook_catalog_request

def history(q='ขอกฎแข่ง VALORANT',domain='competition_rules'):
    return [{'role':'user','text':q},{'role':'assistant','text':'กติกา','route_category':domain,'resolved_text':q}]

class Boundaries(unittest.TestCase):
 def test_more_uses_active_rulebook(self):
  for q in ('มีกฏอื่นไหม','มีข้ออื่นอีกป่าว','แล้วข้ออื่นล่ะ','ต่ออีกหน่อย','anything else','more please','continue'):
   with self.subTest(q=q):
    r=resolve_question_with_context(q,history())
    self.assertTrue(r.used_context);self.assertEqual(r.context_game,'VALORANT');self.assertEqual(r.context_operation,'rule_more')
 def test_more_without_competition_context_does_not_select_rulebook(self):
  for q in ('ต่ออีกหน่อย','มีข้ออื่นอีกป่าว','anything else'):
   for h in ([],history('เปิดกี่โมง','schedule'),history('กฎศูนย์มีอะไรบ้าง','rules')):
    with self.subTest(q=q,h=h):self.assertNotEqual(resolve_question_with_context(q,h).context_domain,'competition_rules')
 def test_explicit_new_topic_does_not_inherit_rules(self):
  for q in ('เปิดกี่โมง','กฎศูนย์มีอะไรบ้าง','VALORANT คืออะไร','ราคา PC เท่าไหร่','VALORANT เล่นยังไง'):
   with self.subTest(q=q):self.assertNotEqual(resolve_question_with_context(q,history()).context_domain,'competition_rules')
 def test_names_recover_only_with_prior_competition_task(self):
  for q in ('valroant','valorantt','valorat'):
   with self.subTest(q=q):
    r=resolve_question_with_context(q,history());self.assertTrue(r.used_context);self.assertEqual(r.context_game,'VALORANT')
    self.assertFalse(resolve_question_with_context(q,[]).used_context)
 def test_years_unknown_games_and_specific_topics_are_preserved(self):
  for q in ('กฎแข่ง VALORANT ปี 2024','กฎแข่ง Tekken 7','กฎแข่ง Minecraft','ขอกฎ VALORANT เรื่องขายไอเท็ม','ไม่เอากฎ VALORANT'):
   with self.subTest(q=q):self.assertEqual(resolve_question_with_context(q,history()).resolved_question,q)
 def test_damaged_courtesy_keeps_task(self):
  for q in ('ขอกฏหนาอย','ขอกฎหน่อยยย','ขอกฎเกมนี้หน่อยย','กติกาเกมนี้มีไรมั่ง','can i see the rulez for this game pls'):
   with self.subTest(q=q):
    r=resolve_question_with_context(q,history());self.assertTrue(r.used_context);self.assertEqual(r.context_game,'VALORANT')
 def test_real_words_are_not_corrected_to_rules(self):
  for q in ('can i see the runes','show me the ruse','can i see the roles'):
   with self.subTest(q=q):self.assertFalse(is_broad_rule_request(q));self.assertFalse(resolve_question_with_context(q,history()).used_context)
 def test_catalogue_and_future_event_are_distinct(self):
  for q in ('มีเกมไรให้แข่งมั่ง','แข่งเกมไหนได้บ้าง','Which games can we compete in?'):
   with self.subTest(q=q):self.assertTrue(is_rulebook_catalog_request(q))
  for q in ('มีเกมอะไรบ้าง','แข่งเกมไหนเดือนหน้า','Which games are open for registration?','เกมแข่งแนวไหน','ไม่อยากแข่งเกมไหนได้บ้าง'):
   with self.subTest(q=q):self.assertFalse(is_rulebook_catalog_request(q))
 def test_declined_rule_task_keeps_original_for_audit(self):
  q='ไม่เอากฎแล้ว VALORANT คืออะไร';r=resolve_question_with_context(q,history())
  self.assertEqual(r.original_question,q);self.assertEqual(r.resolved_question,'VALORANT คืออะไร');self.assertFalse(r.used_context);self.assertEqual(r.context_domain,'games')
 def test_history_is_not_mutated(self):
  h=history();old=json.dumps(h);resolve_question_with_context('ต่ออีกหน่อย',h);self.assertEqual(json.dumps(h),old)
 def test_failed_generic_rule_reply_does_not_erase_target(self):
  h=history()+history('ขอกฏของเกมหน่อย','knowledge')
  self.assertEqual(resolve_question_with_context('มีกฎอื่นไหม',h).context_game,'VALORANT')
 def test_topic_change_blocks_search_back(self):
  h=history()+history('เปิดกี่โมง','schedule')
  self.assertNotEqual(resolve_question_with_context('มีกฎอื่นไหม',h).context_domain,'competition_rules')

R=Path((Path(__file__).parent/'r37_report_path.txt').read_text(encoding='utf-8').strip())
run=sys.argv[1]
with (R/(run+'_regression.log')).open('x',encoding='utf-8') as out:result=unittest.TextTestRunner(stream=out,verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Boundaries))
summary={'tests':result.testsRun,'passed':result.wasSuccessful(),'failures':[(str(t),m) for t,m in result.failures],'errors':[(str(t),m) for t,m in result.errors]}
(R/(run+'_regression.json')).write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False));sys.exit(not result.wasSuccessful())
