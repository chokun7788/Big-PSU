"""Same dispatcher, explicit preview/published isolation and source refresh."""
import copy,dataclasses,json,os,sys
from pathlib import Path
from unittest.mock import patch
R=Path(__file__).resolve().parent;S=R/'system';T=R/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False)
sys.path.insert(0,str(S));os.environ.update(PSU_COMMON_CHAT_PROFILE='common-r101-published',PSU_ESPORTS_NOW='2026-10-19T12:00:00+07:00',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0')
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record,preview_answer
from app.knowledge.common.dialogue import state_from_answer
from app.pipeline.migrated_chat import answer
from app.core.locale import LocaleDecision
from app.knowledge.common.migrated_view import enabled
store=CommonStore(T/'ISOLATED_PUBLISHED.sqlite');store.initialize();checks=[]
def check(name,ok,detail=None):
 row={'case':name,'passed':bool(ok),'detail':detail};checks.append(row)
 with (T/'CHECKS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
 print(name,bool(ok),flush=True)
def ask(q,h=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('No model in publication contract')):
  return answer(q,locale=LocaleDecision('en','en','en',1,'test'),store=store,allow_llm=False,allow_live=False,history=h or [])
def publish(rid,key):
 r=store.get(rid);store.approve(rid,r['record']['revision'],r['hash'],actor='isolated-test')
 store.publish([rid],actor='isolated-test',expected_active=store.snapshot()['active'],request_key=key)
check('new profile enters exclusive common dispatcher',enabled())
r=ask('What is Nova Published Fixture?')
check('empty published store is a source gap, not unavailable database',r.decision_artifact.get('publication_empty') and r.decision_artifact['need_results'][0]['status']=='missing_source',dataclasses.asdict(r))
g=template('game');g['record_id']='fixture_nova_published';g['localization']['en_status']='agent_translated'
for k,v in {'title':{'th':'โนวาทดสอบ','en':'Nova Published Fixture'},'summary':{'th':'รายละเอียด V1','en':'Published test details V1'}}.items():g['fields'][k].update(status='known',value=v,evidence_refs=[])
g=save_owner_record(store,g,0,'isolated-test')['record']
check('draft insert cannot leak through published reader','details V1' not in ask('What is Nova Published Fixture?').answer)
check('explicit owner preview sees draft','details V1' in preview_answer(store,'What is Nova Published Fixture?',locale='en',draft=True).answer)
publish(g['record_id'],'nova-v1');r=ask('What is Nova Published Fixture?')
check('approved release answers from same flow','details V1' in r.answer and r.decision_artifact['flow_contract']['version']=='r101',dataclasses.asdict(r))
check('published metadata never labels release draft',r.decision_artifact['migration']['production_publication_verified'] and not r.decision_artifact['migration']['draft_preview_only'])
history=[{'role':'user','text':'What is Nova Published Fixture?'},{'role':'assistant','text':r.answer,'common_read_state':state_from_answer(r),'delivery_status':'server_written'}]
g=copy.deepcopy(store.get(g['record_id'])['record']);g['fields']['summary']['value']={'th':'รายละเอียด V2','en':'Published test details V2'}
g=save_owner_record(store,g,g['revision'],'isolated-test')['record']
check('draft edit retains published V1','details V1' in ask('What is Nova Published Fixture?').answer)
publish(g['record_id'],'nova-v2');r=ask('summary',history)
check('follow-up re-reads published revision after edit','details V2' in r.answer and 'details V1' not in r.answer)
store.withdraw(g['record_id'],actor='isolated-test');r=ask('summary',history)
check('withdraw cannot resurrect old answer through delivered state','details V1' not in r.answer and 'details V2' not in r.answer)
summary={'count':len(checks),'passed':sum(c['passed'] for c in checks),'failed':[c['case'] for c in checks if not c['passed']],'real_approvals_created':False,'source':'isolated synthetic publication fixture'}
(T/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(summary);sys.exit(bool(summary['failed']))
