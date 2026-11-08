"""Require real local generation and a source-validated selector before bulk."""
import hashlib,json,os,sys,time,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent;S=R/'system';T=R/'preflight';T.mkdir(exist_ok=False)
sys.path.insert(0,str(B/'r82_automatic_llm_check_20261017'))
from auto_test import Runner
runner=Runner(T);tags=runner.get('model_list','http://127.0.0.1:11434/api/tags');warm=runner.ensure_model(tags,'scb10x/typhoon2.5-qwen3-4b')
assert warm.get('http_ok') and (warm.get('body') or {}).get('done'),'Real model generation not verified'
os.environ['PSU_R88_RUN_TAG']='preflight'
sys.path.insert(0,str(R));from run_common import configure
configure('canary')
from app.pipeline.engine import answer_question_pipeline_debug
from app.core.locale import LocaleDecision
from app.knowledge.common.dialogue import state_from_answer
native=urllib.request.urlopen;calls=[]
def observe(req,*args,**kw):
 url=getattr(req,'full_url',str(req));d={'url':url,'transport_ok':False}
 if ':11434/' in url:calls.append(d)
 try:response=native(req,*args,**kw);d['transport_ok']=True;return response
 except Exception as e:d.update(error_type=type(e).__name__,error=str(e));raise
urllib.request.urlopen=observe
cases=[('th','เหมา PC เต็มวันหน่วยงานภายนอกราคาเท่าไหร่','common_legacy_rental_bridge'),('th','ROV สรุปกติกาสั้นๆ','common_legacy_clause_overview'),('th','แนบหลักฐานชำระเงินผิด ต้องแก้ยังไง','selector')]
rows=[]
for lang,q,expected in cases:
 r=answer_question_pipeline_debug(q,locale=lang,locale_decision=LocaleDecision(lang,lang,lang,1,'r88_canary'),experimental_rag_fallback=False,experimental_allow_llm=True,global_timeout_sec=18,recent_history=[])
 art=r.decision_artifact or {};plan=art.get('query_plan') or {};state=state_from_answer(r) or {}
 if expected=='selector':
  audit=plan.get('entity_selection') or {};ok=bool(state.get('profile_confirmation')) and audit.get('attempted') is True and audit.get('transport_ok') is True and audit.get('schema_accepted') is True
 elif 'rental' in expected:ok=plan.get('legacy_fact_fallback_used') is False and '4,000' in r.answer and bool(plan.get('request_contract'))
 else:ok=plan.get('method')==expected
 rows.append({'question':q,'expected':expected,'passed':bool(ok and r.validation.ok),'answer':r.answer,'artifact':art,'hits':r.hits})
 print(json.dumps({'question':q,'passed':rows[-1]['passed'],'method':plan.get('method')},ensure_ascii=False),flush=True)
config=json.loads((R/'CONFIG.json').read_text('utf8'));digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':all(x['passed'] for x in rows),'real_generation_verified':True,'observed_model_calls':calls,'cases':rows,'source_frozen_hashes_verified':all(digest(S/e['path'])==e['sha256'] for e in config['source_manifest']),'database_matches_source':digest(S/'data/knowledge/common.sqlite')==config['test_database_sha256'],'llm_enabled':True,'format':'common'}
with (R/'PREFLIGHT_RESULT.json').open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2,default=str)
assert result['passed'] and result['source_frozen_hashes_verified'] and result['database_matches_source'],'Preflight failed; bulk not launched'
print('R88 PREFLIGHT PASSED',flush=True)
