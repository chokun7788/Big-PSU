import json,copy
from pathlib import Path
from r56_contracts import evaluate
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r56_current_path.txt').read_text());prior=Path((BASE/'r55_current_path.txt').read_text())
rows={r['case']['id']:r['job']['result'] for r in json.loads((prior/'web_final6.json').read_text(encoding='utf-8'))};contracts={c['id']:c for c in json.loads((OUT/'answer_contracts_v2.json').read_text(encoding='utf-8'))};checks=[]
def check(label,cid,mutate):
 r=copy.deepcopy(rows[cid]);mutate(r);a=evaluate(r,contracts[cid]);checks.append(dict(label=label,id=cid,mutation_rejected=bool(a['errors']),errors=a['errors']))
check('omit mandatory owner condition','c020',lambda r:r.update(answer=r['answer'].replace('named in','somewhere else')))
check('omit a game from requested complete catalog','c075',lambda r:r.update(answer=r['answer'].replace('Mario Kart 8 Deluxe','')))
check('replace correct target game in overview metadata','c081',lambda r:[t['metadata'].update(game_ids=['valorant']) for t in r['trace'] if t['stage']=='competition_overview'])
check('retain keywords but wrong price','c061',lambda r:r.update(answer=r['answer'].replace('140','999')))
check('retain answer amount but wrong eligibility binding','c061',lambda r:[row.update(group_id='general_student') for t in r['trace'] for row in t['metadata'].get('rows',[])])
check('retain answer amount but wrong price multiplication','c061',lambda r:[row.update(total=999) for t in r['trace'] for row in t['metadata'].get('rows',[])])
check('omit validity warning','c064',lambda r:r.update(answer=r['answer'].replace('2026-03-31','')))
check('assert unknown install permission','c096',lambda r:r.update(answer='สามารถติดตั้งเกมเองได้ครับ'))
check('omit second compound answer','c145',lambda r:r.update(answer=r['answer'].split('\n\n')[0]))
check('fake full-rule coverage','c086',lambda r:r['rule_coverage'].update(returned_ids=['not_in_source']))
check('Arabic contamination in controls','c141',lambda r:r.update(answer=r['answer']+' بشكل'))
with (OUT/'validator_mutations.json').open('x',encoding='utf-8') as f:json.dump(checks,f,ensure_ascii=False,indent=2)
print('mutations',len(checks),'rejected',sum(c['mutation_rejected'] for c in checks));assert all(c['mutation_rejected'] for c in checks)
