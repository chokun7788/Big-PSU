from pathlib import Path
import json
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r30_report_path.txt').read_text().strip())
src=r'''import unittest
from app.core.duration_alternatives import parse_duration_alternatives
from app.pipeline.closed_query_improvements import answer_closed_query_improvement
from app.pipeline.control_button_target import explicit_button_selection
class R30FinalTests(unittest.TestCase):
    def test_three_choices_and_shared_units(self):
        for q,v in [('PC 1 or 2 or 3 hours cost?',(60,120,180)),('PC 1 ชั่วโมงหรือ 2 หรือ 3 ชั่วโมงกี่บาท',(60,120,180)),('VR 30 minutes or 1 or 2 hours cost?',(30,60,120))]:
            with self.subTest(q=q):self.assertEqual(parse_duration_alternatives(q).minutes,v)
    def test_denied_affiliation_is_not_a_free_price(self):
        for q,l in [('ผมไม่ใช่นักศึกษา มอ PC 1 หรือ 2 ชั่วโมงกี่บาท','th'),('I am not a PSU student, PC for 1 or 2 hours cost?','en')]:
            with self.subTest(q=q):
                category,r=answer_closed_query_improvement(q,l)
                self.assertEqual(category,'clarification');self.assertNotIn('0 THB',r.answer);self.assertNotIn('0 บาท',r.answer)
    def test_broad_fee_table_uses_all_stored_packages(self):
        for q,l in [('ค่าเล่นแต่ละเครื่องมีอะไรบ้าง','th'),('อุปกรณ์แต่ละโซนราคาเท่าไหร่','th'),('How much does each service cost?','en')]:
            with self.subTest(q=q):
                category,r=answer_closed_query_improvement(q,l)
                self.assertEqual(category,'service_fee')
                for v in ['PC','PlayStation 5','Nintendo Switch','Cockpit','VR','2026-07-27']:self.assertIn(v,r.answer)
                self.assertNotIn('ยังไม่พบราคา',r.answer)
    def test_unknown_identifier_all_letter_prefixes(self):
        self.assertEqual(explicit_button_selection('What does the Z9 button do?',[]).rows,())
    def test_unknown_game_does_not_silently_drop_booking_target(self):
        category,r=answer_closed_query_improvement('What do I need to book to play Roblox?','en')
        self.assertEqual(category,'clarification');self.assertTrue(r.evidence['no_inferred_booking_service']);self.assertNotIn('Booking steps:',r.answer)
'''
f=p/'tests/test_r30_final_improvements.py';assert not f.exists();f.write_text(src,encoding='utf-8')
base=json.loads((r/'focused_fixture_v1.json').read_text(encoding='utf-8'))
new=[
('three-en','PC 1 or 2 or 3 hours cost?','en','answer',['60 minutes','120 minutes','180 minutes'],[]),
('three-th','PC 1 หรือ 2 หรือ 3 ชั่วโมงกี่บาท','th','answer',['60 นาที','120 นาที','180 นาที'],[]),
('neg-group-th','ผมไม่ใช่นักศึกษา มอ PC 1 หรือ 2 ชั่วโมงกี่บาท','th','clarification',['กลุ่ม'],['0 บาท']),
('neg-group-en','I am not a PSU student, PC for 1 or 2 hours cost?','en','clarification',['user group'],['0 THB']),
('broad-th','ค่าเล่นแต่ละเครื่องมีอะไรบ้าง','th','answer',['PC','PlayStation 5','Nintendo Switch','Cockpit','VR','25 บาท'],['ยังไม่พบราคา']),
('broad-en','How much does each service cost?','en','answer',['PC','PlayStation 5','Nintendo Switch','Cockpit','VR','25 THB'],[]),
('unknown-th','ปุ่ม Q9 ใน Gran Turismo 7 ใช้ทำอะไร','th','no_answer',['Q9','ยังไม่พบ'],['•    R2:']),
('unknown-en','What does the Z9 button do in Gran Turismo 7?','en','no_answer',['Z9','could not find'],['R2: Accelerate']),
('unknown-book-en','What do I need to book to play Roblox?','en','clarification',['full game title'],['Booking steps:']),
('unknown-book-th','ต้องจองอะไรถ้าจะเล่น Roblox','th','clarification',['ชื่อเกม'],['ขั้นตอนจอง:'])]
for id,q,l,o,m,n in new:base['cases'].append({'id':'R30-'+id,'question':q,'locale':l,'outcome':o,'must_contain':m,'must_not_contain':n,'group':'additional_boundaries'})
with (r/'focused_fixture_v2.json').open('x',encoding='utf-8') as f:json.dump(base,f,ensure_ascii=False,indent=2)
print('Added five test methods and ten pipeline cases.')
