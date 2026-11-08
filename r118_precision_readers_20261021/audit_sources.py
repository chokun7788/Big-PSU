import json,sys,collections
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.projection import compile_snapshot,value,title
from app.knowledge.common.domain_flow.engine import Engine
d=compile_snapshot(MigratedView(R/'system/data/knowledge/common.sqlite').snapshot());e=Engine(d)
(R/'SOURCE_REFERENCE.json').write_text(json.dumps(d,ensure_ascii=False,indent=2),'utf8')
print('COUNTS',len(d['records']),len(d['facts']),collections.Counter(r['kind'] for r in d['records'].values()))
for cat in ['C02','C05','C08']:
 fs=d['facts'];fs=[f for f in fs if f['category']==cat and (cat=='C02' or cat=='C08' and ('cancel' in str(f).lower() or f.get('procedure_complete')) or cat=='C05' and 'god_of_war_ragnar' in f['record_id'])]
 print('CATEGORY',cat)
 for f in fs:print(json.dumps(f,ensure_ascii=False))
print('RELATIONS')
for rid,r in d['records'].items():
 if r['kind'] in {'game_service','resource','zone'} or any(s in str(title(r)) for s in ['Mario','Last of Us','Nightmares']):print(rid,json.dumps(r,ensure_ascii=False))
print('OLD_FAILURE_QUESTIONS')
rows=[json.loads(s) for s in (R.parent/'r116_retained_full_ten_percent_20261021/full01/RESULTS.jsonl').open(encoding='utf8')]
for r in rows:
 gs=[g for g in r['grades'] if g['positive_literal']]
 if gs and not all(g['literal_passed'] for g in gs):print(json.dumps({'key':r['key'],'q':r['question'],'domain':r['domain']},ensure_ascii=False))
