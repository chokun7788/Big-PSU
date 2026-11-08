"""Data growth/revision contracts in an isolated copy; no model accuracy claim."""
import copy,hashlib,json,os,sqlite3,sys
from pathlib import Path
from unittest.mock import patch
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system';T=B/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False)
original=S/'data/knowledge/common.sqlite';before=hashlib.sha256(original.read_bytes()).hexdigest();db=T/'system/data/knowledge/common.sqlite';db.parent.mkdir(parents=True)
a=sqlite3.connect(original.resolve().as_uri()+'?mode=ro',uri=True);z=sqlite3.connect(db);a.backup(z);a.close();z.close()
os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(db),PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_LLM_PREFLIGHT='0',PSU_PIPELINE_WARMUP='0',PSU_CHAT_LOG_DIR=str(T/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(T/'logs/transcripts.sqlite'),PSU_CONVERSATION_STATE_PATH=str(T/'state.sqlite'),PSU_BILINGUAL_EN_ENABLED='1')
sys.path.insert(0,str(S));import app.knowledge.common as pkg;pkg.__path__.insert(0,str(B/'candidate/app/knowledge/common'))
if True:
 import app.pipeline as pipeline_pkg;pipeline_pkg.__path__.insert(0,str(B/'candidate/app/pipeline'))
from app.knowledge.common import migrated_view
migrated_view.SYSTEM_ROOT=db.parents[2]
from app.knowledge.common.registry import template,now
from app.knowledge.common.store import CommonStore
from app.knowledge.common.dialogue import state_from_answer
from app.pipeline.migrated_chat import answer
from app.core.locale import LocaleDecision
from app.pipeline import zone_rental
from app.rules.matcher import RuleMatcher
store=CommonStore(db);checks=[]
def check(name,ok,detail=None):
 row={'case':name,'passed':bool(ok),'detail':detail};checks.append(row)
 with (T/'CHECKS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
 print(json.dumps({'case':name,'passed':bool(ok)}),flush=True)
def ask(q,h=None,lang='en'):
 r=answer(q,locale=LocaleDecision(lang,lang,lang,1,'explicit_fixture_locale'),history=h or [],allow_llm=True)
 return r
def hist(q,r):return [{'role':'user','text':q},{'role':'assistant','text':r.answer,'common_read_state':state_from_answer(r) or {},'delivery_status':'server_written'}]
def save(r,values):
 try:rev=store.get(r['record_id'])['record']['revision']
 except (KeyError,ValueError):rev=0
 raw=json.dumps(values,ensure_ascii=False,sort_keys=True);sha=hashlib.sha256(raw.encode()).hexdigest();sid='fixture_r87_'+sha[:24]
 store.add_source({'source_id':sid,'kind':'derived_curated','path':'isolated-fixture://'+sid,'sha256':sha,'authority_for':[r['kind']],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None},raw,actor='isolated_fixture')
 for key,v in values.items():r['fields'][key]={'status':'known','value':v,'evidence_refs':[{'source_id':sid,'locator':'/'+key}],'note':'ISOLATED FIXTURE; not production data'}
 store.save(r,actor='isolated_fixture',expected_version=rev,change_note='R87 isolated example');return store.get(r['record_id'])['record']
from app.pipeline import retrieval
with patch.object(retrieval,'load_curated_rows',side_effect=AssertionError('Do not read legacy competition facts')),patch('urllib.request.urlopen',side_effect=OSError('CONTROLLED unavailable transport; fixture test only')):
 snap=migrated_view.MigratedView(db).snapshot();rs=snap['release']['records']
 from app.knowledge.common.registry import value
 section=next(r for r in rs.values() if r['kind']=='competition_rule' and 'cs2' in value(r,'competition_id') and 'Objections must be submitted' in str(value(r,'text')))
 source=value(section,'text');save(section,{'text':{lang:body.replace('15','23') for lang,body in source.items()}})
 for lang,q in [('th','กติกา CS2 เรื่องการประท้วงและข้อพิพาท ว่าอย่างไร'),('en','CS2 competition rules: who can submit a protest and when?')]:
  r=ask(q,lang=lang)
  check('Current source edited deadline in '+lang,r.validation.ok and '23' in r.answer and '15' not in r.answer and r.decision_artifact['query_plan'].get('method')=='common_legacy_proposition_detail',{'answer':r.answer,'artifact':r.decision_artifact})
 # A new source row must participate without adding its ID or fact to code.
 r=copy.deepcopy(section);r['record_id']='fixture_new_rov_clause';save(r,{'competition_id':'competition_competition_rules_rov_blueket_2025_men','source_order':1,'heading':{'th':'ข้อทดลองอุปกรณ์','en':'Fixture equipment clause'},'text':{'th':'ผู้เล่นต้องใช้อุปกรณ์ FIXTURE_PAD_901 สำหรับการแข่งขันทดลองเท่านั้น','en':'Players must use FIXTURE_PAD_901 equipment for this fixture competition only.'},'facets':['equipment']})
 for lang,q in [('th','ROV สรุปกติกาสั้นๆ'),('en','Give me a brief overview of RoV competition rules')]:
  a=ask(q,lang=lang)
  check('New source clause read in summary '+lang,a.validation.ok and 'FIXTURE_PAD_901' in a.answer and a.decision_artifact['query_plan'].get('summary_is_complete') is False,{'answer':a.answer,'plan':a.decision_artifact['query_plan']})
 store.withdraw(r['record_id'],actor='isolated_fixture');a=ask('Give me a brief overview of RoV competition rules')
 check('Withdrawn summary clause disappears','FIXTURE_PAD_901' not in a.answer,a.answer)
 store.withdraw(section['record_id'],actor='isolated_fixture');a=ask('CS2 competition rules: who can submit a protest and when?')
 check('Withdrawn detail cannot return old or fixture deadline','23' not in a.answer and '15 minutes' not in a.answer and section['record_id'] not in str(a.hits),a.answer)
check('Real knowledge database unchanged',before==hashlib.sha256(original.read_bytes()).hexdigest())
result={'count':len(checks),'passed':sum(x['passed'] for x in checks),'checks':checks,'isolated_fixture':True,'llm_on':True,'controlled_transport':True,'real_model_inference_verified':False,'full_test_executed':False}
with (T/'SUMMARY.json').open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in result.items() if k!='checks'}));raise SystemExit(any(not x['passed'] for x in checks))
