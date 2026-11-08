import json,hashlib
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r30_report_path.txt').read_text().strip());assert (r/'final_G5_all_summary.json').exists()
for rel in ['app/pipeline/competition_detail.py','tests/test_r30_remaining_source_contracts.py']:
    dest=r/'before_G6'/rel;dest.parent.mkdir(parents=True,exist_ok=True)
    with dest.open('xb') as out:out.write((p/rel).read_bytes())
f=p/'app/pipeline/competition_detail.py';s=f.read_text(encoding='utf-8');old="    DetailConcept('language',";assert s.count(old)==1
new="    DetailConcept('event_duration_venue', ('cs2',), r'แข่ง(?:ขัน)?\\s*(?:ทั้งหมด|นาน)?\\s*กี่วัน|(?:แข่ง(?:ขัน)?|จัดแข่ง(?:ขัน)?)(?:\\s*(?:CS2|Counter-Strike 2))?\\s*ที่ไหน|(?:รายการ|การแข่งขัน)(?:\\s*(?:CS2|นี้))?\\s*(?:จัด(?:ขึ้น)?ที่ไหน|สถานที่)|number of days.{0,35}(?:tournament|competition)|(?:tournament|competition)\\s+(?:last|runs?)(?=\\s*(?:[?.,;]|and\\b|or\\b|for\\b|$))|(?:tournament|competition)\\s+held\\b|(?:tournament|competition).{0,25}\\b(?:venue|take place)\\b', r'การแข่งขันจะแข่งขันทั้งหมด 1 วัน|(?:competition|tournament).{0,55}(?:1 day|one day)'),\n"+old
f.write_text(s.replace(old,new),encoding='utf-8',newline='\n')
f=p/'app/pipeline/competition_detail.py';s=f.read_text(encoding='utf-8');old="    answer = render_rule_reply(first, selected[1:], used[0], locale)";assert s.count(old)==1
new="    if any(c.name == 'event_duration_venue' for c in concepts) and target.reason != 'unique_registered_rulebook_edition':\n        label = target.targets[0].label\n        first = (f'According to the recorded {label} rulebook: ' if locale == 'en' else f'ตามเอกสารกติกา {label} ที่มี: ') + first\n"+old
f.write_text(s.replace(old,new),encoding='utf-8',newline='\n')
f=p/'tests/test_r30_remaining_source_contracts.py';s=f.read_text(encoding='utf-8');s+='''
    def test_event_duration_and_venue_preserve_one_literal_source_clause(self):
        for q,l,terms in [('CS2 แข่งกี่วันและแข่งที่ไหน','th',['1 วัน','PSU Esports Studio']),('How many days does the CS2 tournament last and where is it held?','en',['one day','PSU Esports Studio'])]:
            with self.subTest(q=q):
                a=lookup_competition_reply(q,l)
                for term in terms:self.assertIn(term,a.answer)
                self.assertIn('event_duration_venue',a.concepts)
                self.assertTrue(any(row['id'].endswith('s08_c01') for row in a.rows))
        from app.pipeline.competition_detail import CONCEPTS
        import re
        concept=next(x for x in CONCEPTS if x.name=='event_duration_venue')
        for q in ['Under CS2 tournament rules, may players leave in the last round?','CS2 แข่งแล้วตั้งค่าปุ่มยิงอยู่ที่ไหน','How many days can a CS2 player pause a tournament?']:
            with self.subTest(q=q):self.assertIsNone(re.search(concept.question,q,re.I))
''';f.write_text(s,encoding='utf-8',newline='\n')
cases=json.loads((r/'focused_fixture_G5_source.json').read_text(encoding='utf-8'))['cases']
for q,l,yes in [('CS2 แข่งกี่วันและแข่งที่ไหน','th',['1 วัน','PSU Esports Studio']),('CS2 แข่งกี่วันแล้วจัดที่ไหน แบบสรุป','th',['1 วัน','PSU Esports Studio']),('CS2 ต้องแข่งทั้งหมดกี่วันและสนามอยู่ที่ไหน','th',['1 วัน','PSU Esports Studio']),('How many days does the CS2 tournament last and where is it held?','en',['one day','PSU Esports Studio']),('Where is the CS2 tournament held and how many days does it last?','en',['one day','PSU Esports Studio']),('How long does the CS2 tournament last?','en',['one day','PSU Esports Studio'])]:
    cases.append(dict(id='G6-'+str(len(cases)+1),locale=l,question=q,must_contain=yes,must_not_contain=[],required_source='competition_rules_cs2',group='source_G6',outcome=None,mode_prefix='pipeline:competition_rule_detail_source'))
with (r/'focused_fixture_G6_source.json').open('x',encoding='utf-8') as out:json.dump({'cases':cases,'scope':'source-derived contracts plus recorded event clause; no current event date inferred'},out,ensure_ascii=False,indent=2)
with (r/'app_freeze_G6.json').open('x',encoding='utf-8') as out:json.dump({str(f.relative_to(p)).replace('\\','/'):hashlib.sha256(f.read_bytes()).hexdigest() for f in (p/'app').rglob('*.py')},out,indent=2)
for old,new in [('r30_extra_G5.py','r30_extra_G6.py'),('r30_extra_analyze_G5.py','r30_extra_analyze_G6.py'),('r30_build_G5_analysis.py','r30_build_G6_analysis.py'),('r30_http_G5.py','r30_http_G6.py'),('r30_source_G5_tests.py','r30_source_G6_tests.py'),('r30_preflight_G5.py','r30_preflight_G6.py')]:
    s=Path(old).read_text(encoding='utf-8').replace('G5','G6')
    if new=='r30_http_G6.py':s=s.replace('competition_G63','competition_G43')
    if new=='r30_build_G6_analysis.py':
        s=s.replace('final_G6_runtime_guard500','final_G5_runtime_guard500')
        s=s.replace('scope\':\'LLM/semantic disabled',"scope':'Combined G5 complete sweep with G6 affected-competition replay; timestamps/latencies span both runs. LLM/semantic disabled")
    if new=='r30_preflight_G6.py':s=s.replace('app_freeze_G6b.json','app_freeze_G6.json').replace('final_G6b_source_G6_summary.json','final_G6_source_G6_summary.json').replace("units['tests']==424","units['tests']==425").replace("source['passed']==39","source['passed']==45")
    with Path(new).open('x',encoding='utf-8') as out:out.write(s)
print(json.dumps({'new_source_fixture_cases':len(cases),'production_change':'one CS2-only source concept; no change outside competition_detail.py from G5b'}))
