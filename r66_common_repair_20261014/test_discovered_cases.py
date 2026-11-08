"""Regression cases discovered after the broad sweep, not old score rewrites."""
import sys,json,unittest,os
from pathlib import Path
B=Path(__file__).resolve().parent
from test_r66_reader import answer,a
llm_enabled=len(sys.argv)>1 and sys.argv[1]=='1'
if llm_enabled:
 from harness import configure
 from app.knowledge.common.planner import plan_fields
 from datetime import datetime
 configure('common',True)
 def answer(q,lang='th',history=None):return a.answer(q,locale=lang,history=history,at=datetime.fromisoformat('2026-10-14T12:00:00+07:00'),planner=plan_fields)
class Discovered(unittest.TestCase):
 def test_daily_question_does_not_turn_per_booking_limit_into_daily_policy(self):
  r=answer('PS5 เล่นได้กี่ชั่วโมงต่อวัน');self.assertIn('3 Sessions',r.answer);self.assertIn('ต่อการจอง',r.answer);self.assertIn('ยังไม่มีข้อมูลยืนยันเพดานต่อวัน',r.answer);self.assertEqual(r.decision_artifact['response_type'],'partial_answer')
 def test_unrelated_model_selection_has_no_topic_alignment(self):
  from app.knowledge.common.entity_search import topic_alignment
  def faq(title):return {'kind':'faq','fields':{'question':{'status':'known','value':{'th':title,'en':title}}}}
  self.assertFalse(topic_alignment('How much is it?',faq('damage_penalty_summary'))[0])
  self.assertFalse(topic_alignment('May a parent use Nintendo equipment?',faq('Service Fee 2026'))[0])
  self.assertTrue(topic_alignment('What penalties apply to damage?',faq('damage penalty summary'))[0])
 def test_valid_words_do_not_fuzzily_select_game_names(self):
  from app.knowledge.common.answer import named
  self.assertEqual(named('cooperative education',{'test':['Overcooked']}),([], 'none'))
 def test_game_alias_on_control_set_still_resolves_game_details(self):
  for q,lang in [('Call of Duty: Warzone เป็นเกมแนวไหน','th'),('What kind of game is Animal Crossing: New Horizons','en')]:
   r=answer(q,lang);self.assertIsNotNone(r);self.assertIn('game' if lang=='en' else 'แนว',r.answer.lower());self.assertNotIn('Which part',r.answer);self.assertNotIn('ยังตีความ',r.answer)
 def test_button_identifier_survives_a_typo_in_button_word(self):
  r=answer('Wat does the R3 vutton do in Gran Turismo 7 on PlayStation / PS5','en');self.assertIn('R3',r.answer);self.assertIn('Nitro',r.answer)
 def test_compound_games_and_prices(self):
  r=answer('PS5 มีเกมอะไรกับราคาเท่าไหร่');self.assertIn('TEKKEN 8',r.answer);self.assertIn('ค่าบริการ',r.answer);self.assertEqual(r.decision_artifact['query_plan']['method'],'common_compound_operations')
 def test_model_translation_envelope_is_rejected(self):
  from app.knowledge.common.translation import validate_translation
  for target in ['{"kind":"game","field":"summary","text":"A game"}','["A game"]']:
   with self.assertRaises(ValueError):validate_translation('เกม',target)
  self.assertEqual(validate_translation('เล่น 2 คน','For 2 players'),'For 2 players')
  with self.assertRaises(ValueError):validate_translation('ห้ามเล่น','Play freely')
 def test_game_format_numeric_tie(self):
  for q,lang in [('What happens at a 1-1 tie in the Tekken 8 tournament?','en'),('แข่ง Tekken 8 เสมอ 1-1 ทำยังไง','th')]:
   r=answer(q,lang);self.assertIn('1-1',r.answer);self.assertIn('deciding' if lang=='en' else 'ตัดสิน',r.answer)
 def test_food_and_roster_are_both_returned(self):
  r=answer('กติกา CS2 ช่วงเตรียมตัวมีผู้เล่นได้กี่คนและในพื้นที่แข่งกินดื่มอะไรได้บ้าง');self.assertIn('6 คน',r.answer);self.assertIn('หมากฝรั่ง',r.answer)
 def test_english_multiple_topics(self):
  r=answer('Under VALORANT tournament rules, are macros permitted and what food or beverages are allowed?','en');self.assertIn('macro',r.answer.lower());self.assertIn('chewing gum',r.answer.lower())
 def test_early_arrival(self):
  r=answer('How early must VALORANT tournament teams arrive at the venue?','en');self.assertIn('30 minutes',r.answer);self.assertIn('before',r.answer)
 def test_prices_not_replaced_with_resource_inventory(self):
  r=answer('ค่าเล่นแต่ละเครื่องมีอะไรบ้าง');self.assertIn('ค่าบริการ',r.answer);self.assertNotIn('รายการที่เผยแพร่ในฐานข้อมูลกลาง: 14',r.answer)
 def test_no_structured_object_inside_translated_prose(self):
  for q in ['Tell me about Animal Crossing: New Horizons','What are the Tekken 8 competition rules?']:
   r=answer(q,'en');self.assertNotIn('"kind":',r.answer);self.assertNotIn('"field":',r.answer)
 def test_translation_food_has_no_invented_board_game(self):
  r=answer('กติกา CS2 กินดื่มอะไรได้บ้าง','en');self.assertIn('chewing gum',r.answer.lower());self.assertNotIn('checkers',r.answer.lower());self.assertNotIn('single-serving',r.answer.lower())
if __name__=='__main__':
 result=unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(Discovered))
 p=B/('DISCOVERED_'+str(len(list(B.glob('DISCOVERED_*.json')))+1)+'.json');p.write_text(json.dumps({'tests_run':result.testsRun,'llm_enabled':llm_enabled,'failures':[{'test':str(t),'stack':s} for t,s in result.failures],'errors':[{'test':str(t),'stack':s} for t,s in result.errors]},ensure_ascii=False,indent=2),encoding='utf-8');sys.exit(0 if result.wasSuccessful() else 1)
