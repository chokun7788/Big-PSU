import json,re
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
r=Path(Path('r30_report_path.txt').read_text().strip())
for l in (p/'data/competition_rules/competition_rule_chunks.jsonl').read_text(encoding='utf-8').splitlines():
    row=json.loads(l); text=row.get('text','')
    if re.search(r'องค์ประกอบทีม|ตัวจริง|ช้าเกินกว่า|starts.*15|starting players|starters',text,re.I):
        print(json.dumps({'id':row['id'],'text':text},ensure_ascii=False))
d=json.loads((r/'HTTP_INGRESS_AUTO_SUMMARY.json').read_text(encoding='utf-8'))
print('AUTO_NEW_FAILURES',json.dumps(d['previous_pass_new_fail_grades'],ensure_ascii=False))
questions={g['question'] for g in d['previous_pass_new_fail_grades']}
for l in (r/'HTTP_INGRESS_AUTO_REPLAY.jsonl').open(encoding='utf-8'):
    row=json.loads(l)
    if row['question'] in questions: print(json.dumps({'q':row['question'],'locale':row['locale_decision'],'answer':row['result']['answer'],'mode':row['result']['mode']},ensure_ascii=False))
