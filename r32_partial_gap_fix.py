from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');R=Path(Path(__file__).with_name('r32_report_path.txt').read_text().strip());path=P/'app/pipeline/competition_source_gaps.py'
with (R/'final11_source_gaps_before_partial_age.py').open('xb') as f:f.write(path.read_bytes())
s=path.read_text(encoding='utf-8');anchor="    detail=lookup_competition_detail(supported_query,locale)\n";assert s.count(anchor)==1
s=s.replace(anchor,"    if re.search(r'\\band\\b|และ|กับ|[,;]',query,re.I):\n        supported_query=re.sub(r'minimum age|age requirement|อายุขั้นต่ำ|อายุอย่างน้อย','',supported_query,flags=re.I)\n"+anchor);path.write_text(s,encoding='utf-8')
test='''import unittest
from app.pipeline.competition_source_gaps import lookup_competition_reply
from app.pipeline.competition_request_contract import validate_requested_clauses

class PartialSourceAgeTests(unittest.TestCase):
    def test_supported_eligibility_kept_when_age_is_missing(self):
        for q,l,known,note in [('กติกา CS2 คุณสมบัติและอายุขั้นต่ำคืออะไร','th','เปิดรับเฉพาะ','อายุขั้นต่ำ'),('What are CS2 tournament eligibility and minimum age requirements?','en','General eligibility','minimum-age')]:
            with self.subTest(q=q):
                x=lookup_competition_reply(q,l);self.assertEqual(x.outcome,'partial');self.assertIn(known,x.answer);self.assertIn(note,x.answer)
                self.assertTrue(any(r['id'].endswith('s17_c01') for r in x.rows))
                errors=validate_requested_clauses(q,'Missing age only',[{'id':r['id']} for r in x.rows],l,'pipeline:competition_rule_detail_partial_source')
                self.assertTrue(errors,'Must reject an age-gap-only response even with the correct eligibility source')
    def test_age_only_does_not_imply_general_eligibility(self):
        for q,l in [('กติกา CS2 อายุขั้นต่ำเท่าไร','th'),('What is the CS2 tournament minimum age?','en')]:
            x=lookup_competition_reply(q,l);self.assertEqual(x.outcome,'no_answer');self.assertFalse(x.rows)
'''
with (P/'tests/test_partial_source_age_r32.py').open('x',encoding='utf-8') as f:f.write(test)
