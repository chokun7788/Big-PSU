from pathlib import Path
import r48_probe as p
ROOT=p.p.ROOT
code='''"""Confirmed facts and boundaries of the 2026-10-08 user answers."""
import hashlib,json,unittest
from pathlib import Path
from app.pipeline.user_service_facts import answer_user_service_facts,load_facts,PATH

class UserServiceFactsTests(unittest.TestCase):
    def test_original_source_binding(self):
        raw=PATH.parents[1]/'sources/user_service_answers_20261008.json'
        facts=load_facts()
        self.assertEqual(hashlib.sha256(raw.read_bytes()).hexdigest(),facts['raw_sha256'])
        items={i['number']:i for i in json.loads(raw.read_text(encoding='utf-8'))['items']}
        self.assertEqual(50,len(items));self.assertEqual(18,len(facts['claims']))
        for claim in facts['claims'].values():
            for number in claim['source_items']:
                self.assertEqual('user_confirmed',items[number]['status'])
        self.assertEqual([45,46],facts['pending_boundary']['items'])

    def test_separate_tournament_rental_and_unknown_policies(self):
        for q in ['กฎการแข่งขัน VALORANT เอาคีย์บอร์ดตัวเองมาได้ไหม',
                  'Can I bring my own keyboard to the CS2 tournament?',
                  'Where is the RoV competition venue?',
                  'Nintendo Switch rental for four people',
                  'ขอเหมาอุปกรณ์พร้อมที่นั่งพัก',
                  'เอาจอยตัวเองมาได้ไหม','Can I bring my own controller?',
                  'โอนเกินทำยังไง','โอนขาดต้องจ่ายเพิ่มไหม',
                  'ติดตั้งเกมเองได้ไหม','มีบัญชี Steam ให้ยืมไหม',
                  'Where is the 65-inch TV located?',
                  'Where is the Xbox studio in Bangkok?']:
            with self.subTest(question=q):self.assertIsNone(answer_user_service_facts(q,'en'))

    def test_no_implication_of_refund(self):
        r=answer_user_service_facts('เปลี่ยนเวลาจองแล้วได้เงินคืนไหม')
        metadata=r['trace'][0].metadata
        self.assertIn('refund_conditions',metadata['missing_fields'])
        self.assertEqual('answered_partial',metadata['outcome'])

    def test_no_claim_of_immediate_walk_in_or_free_parking(self):
        for q,field in [('walk in เล่นได้ทันทีไหม','immediate_walk_in_slot'),
                        ('Is parking free?','parking_fee')]:
            r=answer_user_service_facts(q,'en')
            self.assertIn(field,r['trace'][0].metadata['missing_fields'])

    def test_claims_have_both_languages_and_preserved_conditions(self):
        facts=load_facts()
        for key,c in facts['claims'].items():
            with self.subTest(claim=key):
                self.assertTrue(c['answers']['th']);self.assertTrue(c['answers']['en'])
        self.assertIn('note',facts['claims']['combined_transfer']['answers']['en'])
        self.assertIn('named',facts['claims']['player_identity']['answers']['en'])
        self.assertIn('or passport',facts['claims']['checkin_documents']['answers']['en'])
        self.assertEqual('agent_translation_from_user_confirmed_thai',facts['english_status'])
'''
dest=ROOT/'tests/test_user_service_facts_r48.py'
with dest.open('x',encoding='utf-8') as f:f.write(code)
v=(p.BASE/'r47_verify_source.py').read_text().replace('r47_current_path.txt','r48_current_path.txt')
(p.BASE/'r48_verify_source.py').write_text(v,encoding='utf-8')
print(dest)
