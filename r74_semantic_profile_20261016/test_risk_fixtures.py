"""Safety fixtures on copied records; never mutate installation/source DB."""
import copy,hashlib,json,os,sys,time
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
B=Path(__file__).resolve().parent;T=B/'results'/sys.argv[1];T.mkdir(parents=True,exist_ok=False)
os.environ.update(PYTHONDONTWRITEBYTECODE='1',PYTHONUTF8='1',PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(B/'system/data/knowledge/common.sqlite'),PSU_CHAT_LOG_DIR=str(T/'logs'),PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1')
sys.path.insert(0,str(B/'system'))
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.answer import CommonAnswerer,title
from app.knowledge.common.registry import value
from app.knowledge.common.planner import plan_fields
from app.knowledge.common.entity_search import candidates,topic_alignment
snapshot=MigratedView(B/'system/data/knowledge/common.sqlite').snapshot()
before=hashlib.sha256((B/'system/data/knowledge/common.sqlite').read_bytes()).hexdigest()
rows=[]
def check(name,ok,detail):
 rows.append({'case':name,'passed':bool(ok),'detail':detail})
 with (T/'CHECKS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(rows[-1],ensure_ascii=False)+'\n')
 print(json.dumps({'case':name,'passed':bool(ok)}),flush=True)
class FixtureView:
 def __init__(self,snap):self.snap=snap;self.current=True
 def snapshot(self):return copy.deepcopy(self.snap)
 def still_current(self,snap):return self.current
 def connect(self,*a,**kw):return MigratedView(B/'system/data/knowledge/common.sqlite').connect(*a,**kw)
 sources=staticmethod(MigratedView.sources)
def ask(snap,q,locale='en'):
 reader=CommonAnswerer(FixtureView(snap))
 return reader.answer(q,locale=locale,at=datetime(2026,10,16,12,tzinfo=ZoneInfo('Asia/Bangkok')),planner=plan_fields)
missing=copy.deepcopy(snapshot)
missing_ids=[rid for rid,r in missing['release']['records'].items() if r['kind']=='faq' and value(r,'intent_key')=='bank_account']
for rid in missing_ids:del missing['release']['records'][rid];missing['names'].pop(rid,None) if 'names' in missing else None
r=ask(missing,'How do I pay for my booking?')
check('Missing payment source does not answer with deadline',r is not None and '10 minutes' not in r.answer and r.decision_artifact['response_type']=='clarification',r.decision_artifact if r else None)
r=ask(missing,'How do I pay and when must I pay?')
check('Missing compound source remains explicit',r is not None and '10' in r.answer and 'no confirmed source' in r.answer and r.decision_artifact['response_type']=='partial_answer',{'answer':r.answer,'coverage':r.decision_artifact.get('task_coverage')} if r else None)
changed=copy.deepcopy(snapshot);target=changed['release']['records']['game_detail_god_of_war_ragnarok']
target['revision']+=1;target['fields']['genre']={'status':'unknown','value':None,'evidence_refs':[],'note':'Isolated fixture: owner withdrew the detail'}
r=ask(changed,'What genre is God of War Ragnarök?')
check('Changed owner revision disables identity link',r is not None and 'Action-Adventure' not in r.answer,{'answer':r.answer,'artifact':r.decision_artifact} if r else None)
withdrawn=copy.deepcopy(snapshot);withdrawn['withdrawn'].append('game_detail_god_of_war_ragnarok') if isinstance(withdrawn['withdrawn'],list) else withdrawn['withdrawn'].add('game_detail_god_of_war_ragnarok')
r=ask(withdrawn,'What genre is God of War Ragnarök?')
check('Withdrawn target cannot be revived via identity link',r is None or 'Action-Adventure' not in r.answer,{'answer':r.answer} if r else None)
rs=copy.deepcopy(snapshot['release']['records']);example=copy.deepcopy(rs['facility_parking']);example['record_id']='fixture_tail';example['fields']['name']['value']={'th':'ตัวอย่างทดสอบแยก','en':'Fixture test information'}
# A unique topic appears only after the old 1,800-character index prefix.
example['fields']['location']['value']={'th':'ข้อความทดสอบ '*350+' zebrastation luggage lockers','en':'neutral fixture filler '*350+' zebrastation luggage lockers'}
rs['fixture_tail']=example
cs=candidates('Where are zebrastation luggage lockers?',rs,{rid:[] for rid in rs})
row=next((x for x in cs if x['record_id']=='fixture_tail'),None)
check('Tail field is retrievable and reaches bounded model excerpt',row is not None and 'zebrastation' in row['text'] and len(row['text'])<=650,cs)
ok,terms=topic_alignment('What are the refund rules?',snapshot['release']['records']['facility_parking'])
check('Unrelated parking record fails independent topic guard',not ok,terms)
service=next(r for r in rs.values() if r['kind']=='service' and '30 นาที' in json.dumps(value(r,'name'),ensure_ascii=False))
check('English numeric service unit is localized without changing facts','30 minutes' in title(service,'en') and 'นาที' not in title(service,'en'),title(service,'en'))
check('Fixture run preserved actual knowledge DB',before==hashlib.sha256((B/'system/data/knowledge/common.sqlite').read_bytes()).hexdigest(),before)
(T/'RESULTS.json').write_text(json.dumps({'count':len(rows),'passed':sum(x['passed'] for x in rows),'llm_enabled':True,'scope':'copied-snapshot adversarial fixtures; no model transport success claim','details':rows},ensure_ascii=False,indent=2),encoding='utf8')
raise SystemExit(any(not r['passed'] for r in rows))
