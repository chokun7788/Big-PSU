"""Focused source-backed regression contracts, separate from old protocol gold."""
import os,sys,json,time,unittest
from pathlib import Path
from datetime import datetime
from unittest.mock import patch
B=Path(__file__).resolve().parent;sys.path[:0]=[str(B/'system'),str(B)]
from harness import configure,test_temp,offline_booking
test_temp('r66_focused');configure('common',False);offline_booking()
from app.knowledge.common.store import CommonStore
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.dialogue import state_from_answer
from app.knowledge.common.registry import value
from app.knowledge.common.planner import semantic_guard,checked_plan
a=CommonAnswerer(CommonStore(B/'common.sqlite'))
def answer(q,lang='th',history=None):return a.answer(q,locale=lang,history=history,at=datetime.fromisoformat('2026-10-14T12:00:00+07:00'))
class Regressions(unittest.TestCase):
 def test_minimal_reference_title_is_supported(self):
  from app.knowledge.common.answer import title
  self.assertEqual(title({'record_id':'reference','fields':{'value':{'status':'known','value':'https://example.invalid/help'}}},'en'),'https://example.invalid/help')
 def test_optional_expired_context_does_not_expire_independent_facts(self):
  from app.knowledge.common.answer import effective
  from app.knowledge.common.registry import template
  def rec(kind,rid,**fields):
   r=template(kind);r['record_id']=rid
   for k,v in fields.items():r['fields'][k].update(status='known',value=v)
   return r
  game=rec('game','g');service=rec('service','s');policy=rec('policy','p');policy['validity'].update(state='known',effective_until='2026-10-01T00:00:00+07:00')
  link=rec('game_service','link',game_id='g',service_id='s',account_policy_id='p',offered=True)
  old=rec('competition','old',game_id='g');old['validity'].update(state='known',effective_until='2026-10-01T00:00:00+07:00')
  current=rec('competition','new',game_id='g',supersedes_id='old');rows={r['record_id']:r for r in (game,service,policy,link,old,current)};at=datetime.fromisoformat('2026-10-14T12:00:00+07:00')
  self.assertTrue(effective(link,at,rows));self.assertTrue(effective(current,at,rows));self.assertFalse(effective(policy,at,rows))
  game['validity'].update(state='known',effective_until='2026-10-01T00:00:00+07:00');self.assertFalse(effective(link,at,rows));self.assertFalse(effective(current,at,rows))
 def test_named_game_identity_is_not_a_zone_game_list(self):
  r=answer('Tekken 8 คือเกมอะไร');self.assertIn('TEKKEN 8',r.answer);self.assertNotIn('เกมที่มีให้เล่น',r.answer);self.assertNotIn('Delta Force',r.answer)
  self.assertEqual(r.decision_artifact['query_plan']['record_ids'],['game_detail_tekken_8'])
 def test_compound_price_booking_and_arrival_proof_keeps_each_clause(self):
  r=answer('PC ราคาเท่าไหร่ แล้วจองยังไง และตอนมาถึงต้องแสดงหลักฐานอะไร')
  self.assertIn('เลือกบริการ',r.answer);self.assertIn('บัตรประชาชน',r.answer);self.assertIn('70.00',r.answer);self.assertNotIn('150.00',r.answer)
  self.assertEqual(r.decision_artifact['query_plan']['method'],'common_compound_operations');self.assertEqual(len(r.decision_artifact['query_plan']['clauses']),3)
 def test_short_available_device_delegates_but_game_offering_does_not(self):
  self.assertIsNone(answer('Is PC available?','en'));self.assertIsNone(answer('Is Cockpit free?','en'))
  self.assertIsNotNone(answer('Is PC free of charge?','en'))
 def test_booking_summary_reuses_typed_task(self):
  first=answer('แล้วจองไง');history=[{'role':'user','content':'แล้วจองไง'},{'role':'assistant','content':first.answer,'common_read_state':state_from_answer(first)}]
  r=answer('สรุปคือทำยังไง',history=history);self.assertIn('ขั้นตอนจอง',r.answer);self.assertIn('เลือกบริการ',r.answer)
 def test_multiple_rule_facets_keep_protest_timing_and_language(self):
  r=answer('Under CS2 tournament rules, which language must protests use and who may file a protest within how many minutes?','en')
  self.assertIn('15',r.answer);self.assertIn('Thai',r.answer);self.assertIn('captain',r.answer.lower());self.assertNotIn('starting money',r.answer.lower())
 def test_specific_rules_do_not_dump_all_sections(self):
  r=answer('Under VALORANT tournament rules, may abilities be used outside map boundaries for information?','en')
  self.assertIn('KAY/O',r.answer);self.assertNotIn('smartwatch',r.answer.lower());self.assertLess(len(r.answer),12000)
 def test_person_directory_followup_keeps_names(self):
  first=answer('ทีมงานมีใครบ้าง');history=[{'role':'user','content':'ทีมงานมีใครบ้าง'},{'role':'assistant','content':first.answer,'common_read_state':state_from_answer(first)}]
  r=answer('แล้วแต่ละหมวดมีใครบ้าง',history=history);self.assertEqual(r.decision_artifact['query_plan']['method'],'common_people_directory');self.assertIn('ชื่อ',r.answer)
 def test_rental_period_not_hourly_rate(self):
  r=answer('ราคาเหมา PC ครึ่งวันและเต็มวัน')
  self.assertIsNotNone(r);self.assertEqual(r.decision_artifact['query_plan']['method'],'common_rental_scope');self.assertNotIn('หมดอายุ',r.answer)
 def test_expired_price_scope_is_not_called_unsupported(self):
  r=answer('TEKKEN 8 ราคาเท่าไหร่');self.assertIn('ราคาปัจจุบัน',r.answer);self.assertNotIn('outside the selected',r.answer);self.assertNotIn('amount minor',r.answer)
 def test_maps_have_pool_and_veto_without_studio_map(self):
  r=answer('Counter-Strike 2 แข่งจริง กฎเกี่ยวกับแผนที่และการเลือกแผนที่ เป็นแบบไหน')
  self.assertIn('ANCIENT',r.answer);self.assertIn('MAPBAN.GG',r.answer);self.assertNotIn('maps.app.goo',r.answer);self.assertNotIn('เงินเริ่มต้น',r.answer);self.assertTrue(r.validation.ok)
 def test_dispute_not_document_metadata(self):
  for q in ['TEKKEN 8 การแก้ข้อพิพาททำยังไง','TEKKEN 8 ถ้าประท้วงผลต้องทำยังไง']:
   r=answer(q);self.assertIn('กรรมการ',r.answer);self.assertIn('สิ้นสุด',r.answer);self.assertNotIn('competition_dates',r.answer);self.assertLess(len(r.answer),3000)
 def test_known_controls_from_partial_rows_without_invented_gesture(self):
  r=answer('Mario Kart 8 Deluxe ปุ่มเร่งเครื่องกดอะไร');self.assertIn('A | เร่งเครื่อง',r.answer);self.assertIn('กดค้าง',r.answer);self.assertNotIn('B | เบรก',r.answer)
  adapters=r.decision_artifact['query_plan']['representation_adapters'];self.assertEqual(adapters[0]['gesture'],'unknown')
 def test_new_rulebook_short_name_does_not_select_every_event(self):
  r=answer('กฎตอนแข่ง rov มีอะไรบ้าง');self.assertIn('Blueket',r.answer);self.assertNotIn('Counter-Strike',r.answer);self.assertNotIn('TEKKEN',r.answer)
 def test_offered_catalog_scope_and_counts(self):
  r=answer('PC มีเกมอะไรบ้าง');self.assertIn(': 6',r.answer);self.assertIn('Counter-Strike',r.answer);self.assertNotIn('Mario Kart',r.answer)
  r=answer('PS5 มีเกมอะไรบ้าง');self.assertIn(': 17',r.answer);self.assertNotIn('Animal Crossing',r.answer)
 def test_no_pc_price_inference_from_other_services(self):
  for q in ['General Adult เล่น PC 30 นาที เสียกี่บาท','PC ราคาเท่าไหร่','What is the price of Counter-Strike 2?']:
   r=answer(q,'en' if q.startswith('What') else 'th');self.assertIsNotNone(r);self.assertTrue(r.validation.ok);self.assertIn('70.00',r.answer);self.assertNotIn('150.00',r.answer);self.assertNotIn('140.00',r.answer);self.assertNotEqual(r.decision_artifact['response_type'],'answer')
 def test_equipment_source_zone_and_hardware_note(self):
  r=answer('PC สเปกอะไร');self.assertIn('i5-14400',r.answer);self.assertIn('32GB',r.answer);self.assertNotIn('Driving Force Shifter',r.answer);self.assertTrue(r.validation.ok)
 def test_booking_process_from_common_faq(self):
  r=answer('How do I book a PC?','en');self.assertIsNotNone(r);self.assertIn('book',r.answer.lower());self.assertNotIn('Which part',r.answer);self.assertEqual(r.decision_artifact['query_plan']['method'],'common_procedure_topic')
 def test_short_game_followup_keeps_service_scope(self):
  first=answer('PS5 มีเกมอะไรบ้าง');history=[{'role':'user','content':'PS5 มีเกมอะไรบ้าง'},{'role':'assistant','content':first.answer,'common_read_state':state_from_answer(first)}]
  r=answer('แล้วมีเกมอะไรบ้าง',history=history);self.assertIn(': 17',r.answer);self.assertNotIn('Animal Crossing',r.answer)
 def test_short_controls_followup_keeps_game(self):
  first=answer('Mario Kart 8 Deluxe เล่นยังไง');history=[{'role':'user','content':'Mario Kart 8 Deluxe เล่นยังไง'},{'role':'assistant','content':first.answer,'common_read_state':state_from_answer(first)}]
  r=answer('ปุ่ม',history=history);self.assertIn('A | เร่งเครื่อง',r.answer)
 def test_calendar_maintenance_and_lunch_bookable(self):
  r=answer('วันจันทร์ช่วงจองและ Maintenance เป็นยังไง');self.assertIn('13:00',r.answer);self.assertIn('09:00',r.answer);self.assertIn('12:00',r.answer);self.assertTrue(r.validation.ok)
  for wd in range(7):
   with a.store.connect() as c:rows=a.store.heads(c)
   r=next(r for r in rows.values() if r['kind']=='schedule' and value(r,'weekday')==wd)
   for p in value(r,'bookable_periods') or []:self.assertFalse(p['start']<'13:00' and p['end']>'12:00')
 def test_wrong_model_fields_not_accepted_as_correct(self):
  with a.store.connect() as c:records=a.store.heads(c)
  rid=next(k for k,r in records.items() if r['kind']=='competition' and 'tekken' in k)
  p={'requested_fields':['competition_dates','coverage','supersedes_id'],'all_fields':False,'platform':None}
  clean,audit=semantic_guard('What are the dispute rules?',checked_plan(p,[rid],records),[rid],records)
  self.assertIsNone(clean);self.assertIn('rejected',audit['semantic_status'])
 def test_layout_and_numbered_edition_safety(self):
  from app.knowledge.common.name_candidates import recover
  self.assertIsNone(recover('PC 2 controls',{'fixture':['PC 1']}))
  self.assertIsNotNone(recover('cockpik controls',{'fixture':['Cockpit']}))
 def test_latin_title_not_marked_as_thai_prose(self):
  from app.knowledge.common.answer import text
  self.assertEqual(text({'th':'Counter-Strike 2','en':None},'en'),'Counter-Strike 2')
 def test_invalid_schema_only_proposal_cannot_prove_semantics(self):
  p={'requested_fields':['competition_dates'],'all_fields':False,'platform':None};records={'fixture':{'kind':'competition','fields':{}}}
  clean,audit=semantic_guard('unfamiliar feature',p,['fixture'],records);self.assertIsNone(clean)
if __name__=='__main__':
 suite=unittest.TestLoader().loadTestsFromTestCase(Regressions);r=unittest.TextTestRunner(verbosity=2).run(suite)
 result={'tests_run':r.testsRun,'failures':[{'test':str(t),'stack':s} for t,s in r.failures],'errors':[{'test':str(t),'stack':s} for t,s in r.errors]}
 filename=B/('FOCUSED_READER_'+str(len(list(B.glob('FOCUSED_READER*.json')))+1)+'.json');filename.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
 sys.exit(0 if r.wasSuccessful() else 1)
