"""Data growth/revision contracts in an isolated copy; no model accuracy claim."""
import copy,hashlib,json,os,sqlite3,sys
from pathlib import Path
from unittest.mock import patch
B=Path(__file__).resolve().parent;S=B/'system';T=B/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False)
original=S/'data/knowledge/common.sqlite';before=hashlib.sha256(original.read_bytes()).hexdigest();db=T/'system/data/knowledge/common.sqlite';db.parent.mkdir(parents=True)
a=sqlite3.connect(original.resolve().as_uri()+'?mode=ro',uri=True);z=sqlite3.connect(db);a.backup(z);a.close();z.close()
os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(db),PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_LLM_PREFLIGHT='0',PSU_PIPELINE_WARMUP='0',PSU_CHAT_LOG_DIR=str(T/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(T/'logs/transcripts.sqlite'),PSU_CONVERSATION_STATE_PATH=str(T/'state.sqlite'),PSU_BILINGUAL_EN_ENABLED='1')
sys.path.insert(0,str(S));import app.knowledge.common as pkg;pkg.__path__.insert(0,str(B/'system/app/knowledge/common'))
if True:
 import app.pipeline as pipeline_pkg;pipeline_pkg.__path__.insert(0,str(B/'system/app/pipeline'))
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
with patch.object(zone_rental,'load_zone_rental_data',side_effect=AssertionError('Legacy price facts must not be read')),patch.object(zone_rental,'build_zone_rental_answer',side_effect=AssertionError('Legacy factual renderer must not be used')),patch.object(RuleMatcher,'match',side_effect=AssertionError('Legacy rule answers must not be used')),patch('urllib.request.urlopen',side_effect=OSError('CONTROLLED unavailable transport; fixture test only')):
 q='PC full-day rental for external organizations price';r=ask(q);h=hist(q,r)
 check('Legacy fact loaders blocked; current common package answered',r.validation.ok and '4,000' in r.answer,{'answer':r.answer,'artifact':r.decision_artifact})
 compound='PC full-day rental for external organizations and VR half-day rental for internal units price';cr=ask(compound)
 selected=ask('VR',hist(compound,cr))
 check('Compound follow-up preserves the selected tuple only',selected.decision_artifact['query_plan']['record_ids']==['rental_vr_internal_half_day'] and '1,500' in selected.answer,selected.answer)
 unknown=ask('PS6',h)
 check('Unknown short device cannot inherit old price',unknown.decision_artifact['query_plan'].get('bridge_status')=='unknown_target' and '4,000' not in unknown.answer,unknown.answer)
 custom=ask('เหมา PC 5 ชั่วโมงเท่าไหร่',lang='th')
 check('Custom duration cannot be priced from half/full-day packages',custom.decision_artifact['query_plan'].get('bridge_status')=='custom_package',custom.answer)
 canceled=ask('No more prices',h)
 check('Cancel closes rental context',not (state_from_answer(canceled) or {}).get('request_contract'),canceled.answer)
 excluded=ask('ราคาเหมาทุกแพ็กเกจยกเว้น VR',lang='th')
 check('Catalog exclusions preserve other packages without VR zone prices',bool(excluded.decision_artifact['query_plan'].get('record_ids')) and not any(rid.startswith('rental_vr_') for rid in excluded.decision_artifact['query_plan']['record_ids']),excluded.answer)
 check('Unknown validity is explicit, never a fully confirmed current price',not r.decision_artifact['query_plan']['source_answer_confirmed'] and any(o.get('field')=='validity' and o.get('status')=='unknown' for o in r.decision_artifact['obligations']),r.decision_artifact['query_plan'])
 package=store.get('rental_pc_external_full_day')['record'];save(package,{'amount_minor':450000})
 r2=ask('price again',h)
 check('Edited price read on follow-up; history facts not reused','4,500' in r2.answer and '4,000' not in r2.answer,r2.answer)
 package=store.get('rental_pc_external_half_day')['record'];save(package,{'amount_minor':225000})
 r3=ask('What about half-day?',h)
 check('Period replacement preserves PC/external with latest revision','2,250' in r3.answer and set(r3.decision_artifact['query_plan']['record_ids'])=={'rental_pc_external_half_day'},r3.answer)
 package=store.get('rental_pc_external_full_day')['record'];package['validity']={'state':'known','effective_from':'2020-01-01T00:00:00+07:00','effective_until':'2021-01-01T00:00:00+07:00'};save(package,{})
 r4=ask('price again',h)
 check('Expired package never asserted as current price','4,500' not in r4.answer and 'rental_pc_external_full_day' in r4.decision_artifact['query_plan']['not_current_ids'],r4.answer)
 z=template('zone');z['record_id']='fixture_aurora_zone';z['aliases']={'th':['ออโรร่า'],'en':['Aurora']};z=save(z,{'name':{'th':'โซนออโรร่า ข้อมูลทดลอง','en':'Aurora Zone'}})
 p=copy.deepcopy(store.get('rental_vr_internal_half_day')['record']);p['record_id']='fixture_aurora_package';p['aliases']={'th':[],'en':[]}
 p=save(p,{'name':{'th':'เหมาออโรร่าครึ่งวันหน่วยงานภายใน ข้อมูลทดลอง','en':'Aurora half-day internal organization fixture'},'zone_ids':[z['record_id']],'amount_minor':98700,'equipment_included':{'th':'AURORA_PAD ข้อมูลทดลอง','en':'AURORA_PAD fixture equipment'}})
 qn='Aurora half-day rental for internal units price';rn=ask(qn)
 check('New common zone works without editing code catalogs','987.00' in rn.answer and rn.decision_artifact['query_plan']['record_ids']==[p['record_id']],rn.answer)
 eq=ask('What equipment is included?',hist(qn,rn))
 check('New zone equipment follow-up reads new common fields','AURORA_PAD' in eq.answer,eq.answer)
 save(store.get(p['record_id'])['record'],{'amount_minor':123400})
 pn=ask('price again',hist(qn,rn))
 check('New zone revised price follows current revision','1,234' in pn.answer and '987.00' not in pn.answer,pn.answer)
 store.withdraw(p['record_id'],actor='isolated_fixture');withdrawn=ask('price again',hist(qn,rn))
 check('Withdrawn package does not fall back to legacy or stale state','987.00' not in withdrawn.answer and '1,234' not in withdrawn.answer and p['record_id'] not in str(withdrawn.hits),withdrawn.answer)
 # Add a new correction fact for a previously unknown need, in fixture only.
 f=template('faq');f['record_id']='fixture_amount_correction';f=save(f,{'question':{'th':'วิธีแก้ยอดเงินผิด ข้อมูลทดลอง','en':'Payment amount correction fixture'},'answer':{'th':'ข้อมูลทดลอง AMOUNT_REVIEW_V1','en':'ISOLATED AMOUNT_REVIEW_V1'},'topic':'isolated_fixture','query_profile':{'task':'correction','ownership':'any','context':'studio','subjects':[{'th':'ยอดเงิน','en':'payment amount'}]}})
 qa='The amount I paid was wrong. How can I correct it?';ra=ask(qa)
 state=state_from_answer(ra) or {};check('New source is not blocked by old unknown-topic guard',bool(state.get('profile_confirmation')) or 'AMOUNT_REVIEW_V1' in ra.answer,ra.answer)
 if state.get('profile_confirmation'):
  rr=ask('yes',hist(qa,ra));check('Confirmation reads newly added source answer','AMOUNT_REVIEW_V1' in rr.answer,rr.answer)
 save(store.get(f['record_id'])['record'],{'answer':{'th':'ข้อมูลทดลอง AMOUNT_REVIEW_V2','en':'ISOLATED AMOUNT_REVIEW_V2'}})
 rr=ask('The payment amount was incorrect. How do I fix it?')
 check('New correction source update is effective without router edit','AMOUNT_REVIEW_V2' in rr.answer and 'AMOUNT_REVIEW_V1' not in rr.answer,rr.answer)
 store.withdraw(f['record_id'],actor='isolated_fixture');rr=ask('The payment amount was incorrect. How do I fix it?')
 check('Withdrawn new correction restores precise unconfirmed state',rr.decision_artifact['query_plan'].get('unconfirmed_topic')=='wrong_amount' and 'AMOUNT_REVIEW' not in rr.answer,rr.answer)
check('Real knowledge database unchanged',before==hashlib.sha256(original.read_bytes()).hexdigest())
result={'count':len(checks),'passed':sum(x['passed'] for x in checks),'checks':checks,'isolated_fixture':True,'llm_on':True,'controlled_transport':True,'real_model_inference_verified':False,'full_test_executed':False}
with (T/'SUMMARY.json').open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in result.items() if k!='checks'}));raise SystemExit(any(not x['passed'] for x in checks))
