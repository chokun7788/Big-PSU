"""Behavior of the new whole-request path, including rejection and budgets."""
import dataclasses,json,os,sys,copy
from pathlib import Path
from unittest.mock import patch
R=Path(__file__).resolve().parent;S=R/'system';T=R/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False)
sys.path.insert(0,str(S));os.environ.update(PSU_COMMON_ALLOW_DEMO='1',PSU_ESPORTS_NOW='2026-10-19T12:00:00+07:00',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0')
from app.knowledge.common.registry import template,value
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.request_plan import RequestPlan,Need,VERSION,aggregate,make_plan
from app.knowledge.common.task_contracts import TASKS
from app.knowledge.common.read_graph import REQUIRED,evaluate,compile,fact
from app.knowledge.common.flow_context import request_context
from app.knowledge.common.translation import validate_translation
from app.knowledge.common.dialogue import state_from_answer
from app.knowledge.common.qualifier_contract import requirements
from app.knowledge.common.open_day import classify
from app.calendar.service_calendar import now_bangkok
import app.knowledge.local_models as local_models
class SimulatedModelLease:
 def acquire(self,timeout=None):return True
 def release(self):pass
# This suite verifies request protocol; physical admission/latency is tested
# separately with real Ollama. Do not race its inter-process hardware lease.
local_models.MODEL_WORK=SimulatedModelLease()
store=CommonStore(T/'SYNTHETIC_ONLY.sqlite');store.initialize(allow_demo=True);checks=[]
def check(name,ok,detail=None):
 row={'case':name,'passed':bool(ok),'detail':detail};checks.append(row)
 with (T/'CHECKS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
 print(name,bool(ok),flush=True)
g=template('game');g['record_id']='fixture_r101_comet';g['aliases']={'th':['ดาวหางทดสอบ'],'en':['Comet Shop Fixture']}
for k,v in {'title':{'th':'ดาวหางทดสอบ','en':'Comet Shop Fixture'},'summary':{'th':'สำรวจแผนที่ COMET_FACT','en':'Explore a map COMET_FACT'},'how_to_play':{'th':'เดินและกระโดด COMET_PLAY','en':'Move and jump COMET_PLAY'}}.items():g['fields'][k].update(status='known',value=v,evidence_refs=[])
g=save_owner_record(store,g,0,'isolated-r101-semantic')['record'];view=DraftSnapshotView(store);rs=view.snapshot()['release']['records'];reader=CommonAnswerer(view)
check('all task contracts have executable graph definitions',set(REQUIRED)==set(TASKS))
for question in ['is the studio open right now ?', 'Is the studio open now?']:
 with patch('urllib.request.urlopen',side_effect=AssertionError('Live fallback must not invoke semantic FAQ retrieval')):
  live=reader.answer(question,locale='en',planner=lambda *a:None)
 check('recognized live opening cannot become static FAQ '+question,live is None or not live.hits,dataclasses.asdict(live) if live else None)
for language,question,mention in [('en','Can I use an unkown game called Example Quest? Please amswer briefly','Example Quest'),('en','Tell me about a game named Unlisted Comet?','Unlisted Comet'),('th','มีเกมชื่อ ดาวไม่อยู่ในฐาน ไหม?','ดาวไม่อยู่ในฐาน')]:
 with patch('urllib.request.urlopen',side_effect=AssertionError('Catalog miss must not invoke semantic retrieval')):
  missing=reader.answer(question,locale=language,planner=lambda *a:None)
 check('named catalog miss cannot become unrelated policy '+language+' '+mention,missing is not None and mention in missing.answer and not missing.hits and missing.decision_artifact.get('unmatched_target',{}).get('reason')=='no_catalog_match',dataclasses.asdict(missing) if missing else None)
with patch('urllib.request.urlopen',side_effect=AssertionError('No model required for missing game slot')):
 first=reader.answer('What is the shoot button?',locale='en',planner=lambda *a:None)
 state=state_from_answer(first)
 history=[{'role':'user','text':'What is the shoot button?'},{'role':'assistant','text':first.answer,'common_read_state':state,'delivery_status':'server_written'}]
 selected=reader.answer('Comet Shop Fixture',locale='en',history=history,planner=lambda *a:None)
check('missing game asks targeted slot before model',first.decision_artifact['need_results'][0]['status']=='needs_user_slot')
check('bare game retains controls task, does not answer its overview',selected.decision_artifact['request_plan']['needs'][0]['task']=='game_controls' and 'COMET_FACT' not in selected.answer,dataclasses.asdict(selected))
from app.knowledge.common.grounded_plan import validate
row={'record_id':g['record_id'],'kind':'game','name':'Comet Shop Fixture'}
unrelated='server versus client'
p={'needs':[{'task':'game_overview','record_ids':[g['record_id']],'quote':unrelated}],'unresolved':[]}
check('semantic model cannot choose unmentioned game from retrieval',validate(p,unrelated,[row],rs)[0] is None)
p['needs']*=2
check('same quote cannot manufacture multiple user needs',validate(p,unrelated,[row],rs)[0] is None)
calls=[]
class FakeResponse:
 def __init__(self,p):self.p=p
 def __enter__(self):return self
 def __exit__(self,*a):pass
 def read(self,n):return json.dumps({'response':json.dumps(self.p)}).encode()
def model(req,*a,**kw):
 data=json.loads(req.data);calls.append(data);question=json.loads(data['prompt'])['question']
 return FakeResponse({'needs':[{'task':'game_overview','record_ids':[g['record_id']],'quote':question}],'unresolved':[]})
q='Could you walk me through the basic idea behind Comet Shop Fixture?'
with patch('urllib.request.urlopen',side_effect=model):r=reader.answer(q,locale='en',planner=lambda *a:None)
check('new semantic plan reaches graph executor without old fullmatch veto','COMET_FACT' in r.answer and r.decision_artifact['query_plan']['method']=='r101_accepted_need_executor',dataclasses.asdict(r))
check('one model call for whole request',len(calls)==1 and r.decision_artifact['request_context']['semantic_attempts']==1)
check('model generates no business facts','COMET_FACT' not in json.dumps(calls[0]) and r.decision_artifact['request_plan']['scope']['model_generated_business_facts'] is False)
check('supported claims carry actual source value and revision',any(p['value']==value(g,'summary') and p['revision']==g['revision'] for p in r.decision_artifact.get('claim_packets',[])))
with patch('urllib.request.urlopen',side_effect=model):child=reader.answer(q+' for children',locale='en',planner=lambda *a:None)
check('semantic selection cannot certify missing age eligibility','COMET_FACT' not in child.answer and child.decision_artifact['response_type']=='unconfirmed',dataclasses.asdict(child))
with patch('urllib.request.urlopen',side_effect=OSError('controlled transport failure')):failed=reader.answer(q,locale='en',planner=lambda *a:None)
check('model transport failure is observable separately',failed is None or not failed.hits)
snap=view.snapshot();fake=reader.finish(snap,0,'DERIVED_VALUE_MUST_NOT_LEAK',[],{'record_ids':[],'requested_fields':[]},[],response='answer')
source=reader.finish(snap,0,'Unconfirmed source',[],{'record_ids':[],'requested_fields':[]},[],response='unconfirmed')
n1=Need('n1','price','price','price',[],[]);n2=Need('n2','price','budget','budget',[],[],hard_dependencies=['n1'])
out=aggregate(reader,snap,0,RequestPlan(VERSION,'price and budget',[n1,n2],{}),[source,fake],'en')
check('unsupported required need prevents derived conclusion','DERIVED_VALUE_MUST_NOT_LEAK' not in out.answer and out.decision_artifact['need_results'][1]['unmet_dependencies']==['n1'])
def record(kind,fields):
 r=template(kind)
 for k,v in fields.items():r['fields'][k].update(status='known',value=v,evidence_refs=[])
 return r
check('bookable period alone cannot prove physical opening',classify(record('schedule',{'bookable_periods':[{'start':'09:00','end':'12:00'}]}))[0] is None)
check('explicit known empty open periods proves closed',classify(record('schedule',{'open_periods':[]}))[0]=='closed')
for source,target in [('ห้ามใช้ 2 ชั่วโมง ยกเว้นวันหยุด','Use for 2 hours.'),('ราคา 300 บาท','Price 30 baht.')]:
 try:validate_translation(source,target);ok=False
 except ValueError:ok=True
 check('translation rejects lost negation/exception/numeric value '+source,ok)
scopeq='Where is the studio?'
from app.pipeline.engine import answer_question_pipeline_debug
os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(S/'data/knowledge/common.sqlite'))
with patch('urllib.request.urlopen',side_effect=AssertionError('No network for outside scope')):
 out=answer_question_pipeline_debug('What should I eat for dinner?',experimental_allow_llm=False,locale='en')
check('outer scope guard has explicit unsupported NeedResult',out.decision_artifact.get('need_results',[{}])[0].get('status')=='unsupported',dataclasses.asdict(out))
summary={'count':len(checks),'passed':sum(c['passed'] for c in checks),'failed':[c['case'] for c in checks if not c['passed']],
 'network':'model protocol simulated; controlled transport failure','real_model_accuracy_claimed':False}
(T/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(summary);sys.exit(bool(summary['failed']))
