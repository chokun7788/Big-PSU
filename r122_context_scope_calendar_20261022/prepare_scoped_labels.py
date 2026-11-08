"""Draft corrected task-local annotations, never overwrite trained labels."""
import copy,hashlib,json,os,sys
from pathlib import Path
R=Path(__file__).resolve().parent;OLD=R.parent/'r121_context_planner_training_20261022'
os.environ['PSU_COMMON_CHAT_PROFILE']='r69-migration-preview';sys.path.insert(0,str(R/'system'))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.understanding import parse
from app.knowledge.common.domain_flow.context_guard import apply
from context_contract import validate,messages
index=Engine.from_snapshot(MigratedView(R/'system/data/knowledge/common.sqlite').snapshot()).index
out=R/'annotation_draft01';out.mkdir(exist_ok=False);changes=[];counts={}
for split in ['train','validation','test']:
 rows=[]
 for line in (OLD/(split+'.jsonl')).read_text('utf8').splitlines():
  original=json.loads(line);row=copy.deepcopy(original);label=row['label']
  result=parse(json.dumps(label,ensure_ascii=False),row['question']);assert result.accepted
  result=apply(row['question'],index,result)
  label['tasks']=[{k:v for k,v in t.as_dict().items() if k!='category'} for t in result.tasks]
  label['context_quotes']=list(dict.fromkeys(c['quote'] for t in label['tasks'] for c in t['constraints']))[:12]
  ok,why=validate(label,row['question']);assert ok,(why,row['question'])
  row['messages']=messages(row['question'])+[{'role':'assistant','content':json.dumps(label,ensure_ascii=False,separators=(',',':'))}]
  row['label_source']='r122_task_local_draft_requires_semantic_review'
  if label!=original['label']:changes.append({'split':split,'key':row['key'],'question':row['question'],'before':original['label'],'after':label,'audit':result.event.get('context_scope_review',[])})
  rows.append(row)
 (out/(split+'.jsonl')).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows),'utf8');counts[split]=len(rows)
(out/'REVIEW_REQUIRED.json').write_text(json.dumps({'counts':counts,'changed_rows':len(changes),'changes':changes,'review_status':'draft, not independently adjudicated','used_for_training':False,'evaluation_reference_replaced':False,'source_business_answers_changed':False},ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'counts':counts,'changed_rows':len(changes),'training_rerun':False}))
