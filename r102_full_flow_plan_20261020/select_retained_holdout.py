"""Select saved domain questions without examining answers or running a model."""
import random,json,re,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent;source=R.parent/'r95_merged_flow_implementation_20261018/FULL_JOBS.jsonl'
seen={json.loads(x)['key'] for x in (R.parent/'r98_flow_v2_implementation_20261019/FOCUSED_JOBS.jsonl').read_text('utf8').splitlines()}
groups={k:[] for k in ['th','en','auto']};eligible=0
for line in source.open(encoding='utf8'):
 x=json.loads(line);q=x['question']
 if x['key'] in seen or len(q)>350 or re.search(r'500\s*(?:words|คำ)|essay|บทความ',q,re.I):continue
 if not re.search(r'ศูนย์|เกม|จอง|ราคา|ค่าบริการ|อุปกรณ์|แข่ง|เปิด|ปิด|บัญชี|\b(?:PSU|studio|games?|PC|VR|PS5|Switch|ROV|VALORANT|CS2|book\w*|rent\w*|fees?|prices?|hours?|equipment)\b',q,re.I):continue
 if x['locale'] in groups:groups[x['locale']].append(x);eligible+=1
rng=random.Random(10220261020);selected=[]
for locale,rows in groups.items():selected.extend(rng.sample(rows,min(64,len(rows))))
rng.shuffle(selected);target=R/'RETAINED_HOLDOUT_JOBS.jsonl'
if target.exists():raise SystemExit('Refusing to overwrite selected cohort')
target.write_text('\n'.join(json.dumps(x,ensure_ascii=False) for x in selected)+'\n','utf8')
report={'count':len(selected),'per_locale':{k:sum(x['locale']==k for x in selected) for k in groups},'overlap_with_91':len({x['key'] for x in selected}&seen),
 'eligible_population':eligible,'seed':10220261020,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'scope':'Retained prior-version questions; selected without manually inspecting individual answers during R102. Not independent unseen project data.',
 'model_calls':0,'chatbot_requests':0}
(R/'HOLDOUT_SELECTION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8');print(json.dumps(report,ensure_ascii=False))
