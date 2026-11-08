import sys,json,unittest,copy
from datetime import datetime
from test_r66_reader import a,B
from harness import configure
from app.knowledge.common.registry import value
from app.knowledge.common.query_scope import complete_control_notes,control_projection
from app.knowledge.common.answer import title
enabled=len(sys.argv)>1 and sys.argv[1]=='1';configure('common',enabled)
from app.knowledge.common.planner import plan_fields
def read(q,lang='en'):return a.answer(q,locale=lang,at=datetime.fromisoformat('2026-10-14T12:00:00+07:00'),planner=plan_fields if enabled else None)
class Completeness(unittest.TestCase):
 def test_damage_ranges_and_actual_cost_condition_are_not_omitted(self):
  r=read('What happens if I damage equipment?');self.assertIn('100-500 THB',r.answer);self.assertIn('actual cost or 500-2,000 THB',r.answer);self.assertIn('full compensation',r.answer);self.assertTrue(r.validation.ok)
 def test_original_thai_fines_unchanged(self):
  r=read('ทำอุปกรณ์เสียหายต้องรับผิดชอบยังไง','th');self.assertIn('100–500',r.answer);self.assertIn('500–2,000',r.answer)
 def test_every_detected_control_omission_is_retained_with_pending_label(self):
  rows=json.loads((B/'CONTROL_NOTE_OMISSIONS.json').read_text(encoding='utf-8'))
  restored=0
  for x in rows:
   v={'th':'\n'.join(m['th'] for m in x['missing']),'en':'\n'.join(m['en'] for m in x['missing'])};before=copy.deepcopy(v);out,n=complete_control_notes(v,'en');self.assertEqual(v,before);self.assertEqual(n,len(x['missing']),x['id']);restored+=n
   for m in x['missing']:self.assertIn(m['th'].split('|')[2].strip(),out['en'])
  self.assertEqual(restored,390);self.assertEqual(len(rows),36)
 def test_unaligned_buttons_are_not_paired_by_position(self):
  v={'th':'A | กระโดด | หมายเหตุเดิม |','en':'B | Jump | |'};out,n=complete_control_notes(v,'en');self.assertEqual(out,v);self.assertEqual(n,0)
 def test_projection_keeps_only_the_requested_button_note(self):
  v={'th':'A | กระโดด | กระโดดข้ามสิ่งกีดขวาง |\nB | หยิบ | หยิบสิ่งของ |','en':'A | Jump | |\nB | Pick up | |'};display,n=complete_control_notes(v,'en');out=control_projection(display,'What does A do?','en');self.assertIn('กระโดดข้าม',out);self.assertNotIn('หยิบสิ่งของ',out);self.assertEqual(n,2)
 def test_response_discloses_partial_translation(self):
  from app.knowledge.common.answer import CommonAnswerer
  from app.knowledge.common.store import CommonStore
  configure('common',enabled,db=B/'common_before_control_notes.sqlite')
  try:
   reader=CommonAnswerer(CommonStore(B/'common_before_control_notes.sqlite'))
   r=reader.answer('What does A do in Moving Out 2 on Nintendo Switch?',locale='en',at=datetime.fromisoformat('2026-10-14T12:00:00+07:00'),planner=plan_fields if enabled else None);self.assertIn('Translation pending',r.answer);self.assertIn('กระโดดข้ามสิ่งกีดขวาง',r.answer);self.assertEqual(r.decision_artifact['response_type'],'partial_answer');self.assertTrue(r.decision_artifact['query_plan']['localization_gaps']);self.assertTrue(r.validation.ok)
  finally:configure('common',enabled)
 def test_translated_notes_restore_existing_english_columns(self):
  import re
  from app.knowledge.common.translation import validate_translation
  repair=json.loads((B/'CONTROL_NOTE_TRANSLATION_REPAIRS.json').read_text(encoding='utf-8'));self.assertEqual(repair['records'],36);self.assertEqual(repair['notes'],390)
  for item in repair['changes']:
   p=B/'CONTROL_NOTE_REVIEWED'/(item['record_id']+'.json');d=json.loads(p.read_text(encoding='utf-8'))
   for n in d['notes']:validate_translation(n['th'],n['en']);self.assertFalse(re.search('[\u0e00-\u0e7f]',n['en']))
  r=read('What does A do in Moving Out 2 on Nintendo Switch?');self.assertNotIn('Translation pending',r.answer);self.assertNotIn('กระโดด',r.answer);self.assertIn('obstacle',r.answer.lower());self.assertTrue(r.validation.ok);self.assertFalse(r.decision_artifact['query_plan'].get('localization_gaps'))
  for q,required,forbidden in [('What does X do in PUBG on PC?','Holster','Drop the weapon'),('What does R1 do in Monster Hunter Rise on PS5?','sheathed','weapon is equipped'),('What does R3 do in The Last of Us Part I on PS5?','Click to toggle','Press and hold')]:
   r=read(q);self.assertTrue(r.validation.ok,r.validation.errors);self.assertIn(required,r.answer);self.assertNotIn(forbidden,r.answer)
 def test_faq_caption_does_not_display_legacy_regex(self):
  r=read('What happens if I damage equipment?');self.assertNotIn('.*',r.answer)
  fake={'kind':'faq','fields':{'question':{'status':'known','value':{'th':'เสียหาย.*รับผิดชอบ','en':'damage.*responsibility'}}}};self.assertEqual(title(fake,'en'),'damage — responsibility')
 def test_general_game_title_and_thai_source_are_not_rewritten(self):
  v={'th':'A | กระโดด | คำอธิบาย |','en':'A | Jump | Complete note |'};self.assertEqual(complete_control_notes(v,'th'),(v,0));self.assertEqual(complete_control_notes(v,'en')[1],0)
  game={'kind':'game','fields':{'title':{'status':'known','value':{'th':'C++.*','en':'C++.*'}}}};self.assertEqual(title(game,'en'),'C++.*')
if __name__=='__main__':
 r=unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(Completeness));p=B/('TRANSLATION_COMPLETENESS_'+str(len(list(B.glob('TRANSLATION_COMPLETENESS_*.json')))+1)+'.json');p.write_text(json.dumps({'tests_run':r.testsRun,'llm_enabled':enabled,'failures':[{'test':str(t),'stack':s} for t,s in r.failures],'errors':[{'test':str(t),'stack':s} for t,s in r.errors]},ensure_ascii=False,indent=2),encoding='utf-8');raise SystemExit(0 if r.wasSuccessful() else 1)
