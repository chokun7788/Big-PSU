import json,re,hashlib
from pathlib import Path
r=Path(Path('r31_report_path.txt').read_text().strip());p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
# Preserve the exact predecessor of the one-line scoring correction.
grader=(p/'tools/eval_contract_v2.py').read_text(encoding='utf-8')
previous=grader.replace('        "pipeline:competition_rule_detail_source",\n','',1)
assert previous!=grader
with (r/'grader_v2_before_r31_reconstructed_from_exact_patch.py').open('x',encoding='utf-8') as out:out.write(previous)
details=json.loads((r/'R31_V2_NEW_FAILURE_DETAILS.json').read_text(encoding='utf-8'));cases=[]
for key,d in details.items():
    q=d['r31']['q'];loc='th' if re.search('[\u0e00-\u0e7f]',q) else 'en'
    cases.append(dict(id=key,question=q,locale=loc,must_contain=['2 ครั้ง','10 นาที','กรรมการ','4 ครั้ง','30 วินาที','Freeze time'] if loc=='th' else ['two times','10 minutes','referees','4','30 seconds','Freeze time'],must_not_contain=[],required_source='competition_rules_cs2',outcome=None,group='r31_source'))
for q,l,parts,forbidden in [
    ('CS2 timeout และ pause ได้กี่ครั้ง ใช้กี่นาที','th',['2 ครั้ง','10 นาที','4 ครั้ง','30 วินาที'],[]),
    ('What are CS2 timeout and pause rules?','en',['two times','10 minutes','4','30 seconds'],[]),
    ('CS2 technical timeout rules?','en',['two times','10 minutes','referees'],['4 per team','30 seconds']),
    ('CS2 เวลานอกทางเทคนิคขอได้กี่ครั้ง','th',['2 ครั้ง','10 นาที'],['4 ครั้ง','30 วินาที']),
    ('How long is a CS2 timeout during freeze time?','en',['4','30 seconds','Freeze time'],['10 minutes']),
    ('CS2 timeout ตอน freeze time กี่วินาที','th',['4 ครั้ง','30 วินาที','Freeze time'],['10 นาที'])]:
    cases.append(dict(id='B-control-'+str(len(cases)),question=q,locale=l,must_contain=parts,must_not_contain=forbidden,required_source='competition_rules_cs2',outcome=None,group='r31_source'))
with (r/'compound_pause_fixture_B.json').open('x',encoding='utf-8') as out:json.dump(dict(cases=cases,scope='Source-backed complete technical+tactical clauses and separate-clause negative controls; not owner policy approval'),out,ensure_ascii=False,indent=2)
http=Path('r31_http.py').read_text(encoding='utf-8').replace("tasks=[('r31_source',","tasks=[('compound18',json.loads((r/'compound_pause_fixture_B.json').read_text(encoding='utf-8'))['cases']),('r31_source',",1).replace("'r31_source'):","'r31_source','compound18'):")
with Path('r31_http_B.py').open('x',encoding='utf-8') as out:out.write(http)
