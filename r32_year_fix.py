import sys,json,os
from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');R=Path(Path(__file__).with_name('r32_report_path.txt').read_text().strip())
sys.path.insert(0,str(P));os.environ['PSU_BILINGUAL_EN_ENABLED']='1'
from app.pipeline.competition_source_gaps import lookup_competition_reply
cases=[('CS2 tournament 2027 eligibility and roster','en'),('กติกา RoV ปี 2026 จำนวนผู้เล่นต่อทีม','th'),('CS2 tournament 2026 eligibility and roster','en'),('กติกา RoV ปี 2025 จำนวนผู้เล่นต่อทีม','th')]
with (R/'SOURCE_YEAR_GUARD_BEFORE.json').open('x',encoding='utf-8') as f:json.dump([dict(question=q,locale=l,outcome=x.outcome,answer=x.answer,source_ids=[r['id'] for r in x.rows]) for q,l in cases if (x:=lookup_competition_reply(q,l))],f,ensure_ascii=False,indent=2)
path=P/'app/pipeline/competition_source_gaps.py';s=path.read_text(encoding='utf-8');assert 'def _recorded_year_guard' not in s
insert='''def _recorded_year_guard(query, locale, rulebook_id):
    # Bind explicit Gregorian edition years to the registered source identity.
    # An update date, game number, or source with no edition year is not evidence.
    recorded = set(re.findall(r"(?:^|_)((?:19|20)\\d{2})(?=_|$)", rulebook_id))
    requested = set(re.findall(r"(?<![\\d.])(?:19|20)\\d{2}(?![\\d.])", query))
    if not recorded or not requested or requested <= recorded:
        return None
    have = ", ".join(sorted(recorded)); want = ", ".join(sorted(requested))
    note = (
        f"The available rulebook is recorded for {have}; it does not verify the requested {want} edition. The organizer must provide that edition before its rules can be confirmed."
        if locale == 'en' else
        f"เอกสารกติกาที่มีระบุปี {have} จึงยังยืนยันกติกาฉบับปี {want} ที่ถามไม่ได้ ต้องขอเอกสารฉบับปีนั้นจากผู้จัดก่อนครับ"
    )
    return CompetitionDetail(note, (), (), 'no_answer', ('requested_rulebook_year_not_in_source',))

'''
s=s.replace('def lookup_competition_reply(query,locale):',insert+'def lookup_competition_reply(query,locale):')
s=s.replace('    rows=_rows(target.targets[0].rulebook_id)\n','    year_guard=_recorded_year_guard(query,locale,target.targets[0].rulebook_id)\n    if year_guard is not None:return year_guard\n    rows=_rows(target.targets[0].rulebook_id)\n');path.write_text(s,encoding='utf-8')
test='''import unittest
from app.pipeline.competition_source_gaps import lookup_competition_reply, _recorded_year_guard

class RecordedEditionGuardTests(unittest.TestCase):
    def test_mismatch_both_languages(self):
        for q,l in [('CS2 tournament 2027 eligibility and roster','en'),('กติกา RoV ปี 2026 จำนวนผู้เล่นต่อทีม','th'),('VALORANT tournament 2025 rules','en'),('กติกา CS2 ปี 2025 และ 2026 คุณสมบัติ','th')]:
            with self.subTest(q=q):
                x=lookup_competition_reply(q,l)
                self.assertEqual(x.outcome,'no_answer');self.assertFalse(x.rows)
                self.assertIn('requested_rulebook_year_not_in_source',x.reasons)
    def test_matching_editions_keep_verified_clauses(self):
        for q,l in [('CS2 tournament 2026 eligibility and roster','en'),('กติกา RoV ปี 2025 จำนวนผู้เล่นต่อทีม','th')]:
            with self.subTest(q=q):
                x=lookup_competition_reply(q,l);self.assertEqual(x.outcome,'answer');self.assertTrue(x.rows)
    def test_numbers_and_undated_source_not_guessed(self):
        for q in ['CS2 rules 16000 money 1.2027', 'CS2 rule section 2027.1', 'CS2 rules for 2026']:
            self.assertIsNone(_recorded_year_guard(q,'en','competition_rules_cs2_psu_phuket_2026'))
        self.assertIsNone(_recorded_year_guard('Tekken 8 rules 2027','en','competition_rules_tekken8_psu_esports'))
'''
# Check the dataclass field name before writing tests.
test=test.replace('x.reasons','x.unresolved_reasons') if 'unresolved_reasons' in (P/'app/pipeline/competition_detail.py').read_text() else test
with (P/'tests/test_competition_recorded_year_r32.py').open('x',encoding='utf-8') as f:f.write(test)
t=json.loads((R/'REAL_BOOKING_ORACLE_PENDING_TEMPLATE.json').read_text());print(json.dumps(t,ensure_ascii=False)[:1600])
t.setdefault('oracle',{})['source_snapshot_sha256']='REPLACE_WITH_SHA256_OF_EXACT_SAVED_AGGREGATE_SNAPSHOT'
with (R/'REAL_BOOKING_ORACLE_PENDING_TEMPLATE_V2.json').open('x',encoding='utf-8') as f:json.dump(t,f,ensure_ascii=False,indent=2)
print('Saved pre-fix evidence, edition guard, tests, and versioned pending oracle template.')
