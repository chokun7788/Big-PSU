"""Read training wire structure and serving identity; never train/relabel."""
import hashlib,json,sys,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent;root=R.parent;sys.path.insert(0,str(R/'system'))
from app.knowledge.common.domain_flow.context_contract import SYSTEM
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows=[]
for name,folder in [('retained','r121_context_planner_training_20261022'),('new','r129_full_plan_completion_20261024/training_v2')]:
 p=root/folder/'train.jsonl';systems=set();keys=set();count=0
 for line in p.open(encoding='utf8'):
  item=json.loads(line);messages=item['messages'];systems.add(hashlib.sha256(messages[0]['content'].encode()).hexdigest());answer=json.loads(messages[-1]['content']);keys.add(tuple(sorted(answer)));count+=1
 rows.append({'profile':name,'training_file_sha256':sha(p),'training_rows':count,'system_message_sha256':sorted(systems),'answer_root_keys':[list(k) for k in keys]})
health=json.load(urllib.request.urlopen('http://127.0.0.1:12921/health',timeout=5))
report={'profiles':rows,'candidate_retained_system_sha256':hashlib.sha256(SYSTEM.encode()).hexdigest(),'candidate_system_matches_retained_training':hashlib.sha256(SYSTEM.encode()).hexdigest() in rows[0]['system_message_sha256'],'serving':health,'finding':'Compact stage uses base; retained training uses focus/context_quotes/tasks. New adapter training uses versioned graph. Do not mix wire and adapter or claim base inference is retained.'}
(R/'TRAINED_PLANNER_AUDIT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(report,ensure_ascii=False))
