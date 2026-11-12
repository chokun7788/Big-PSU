"""Frozen development/fresh probes; serial, one bounded review, no retries."""
import hashlib,json,os,re,time
from verification_support import R
selected=os.getenv('TEST_PLANNER','retained')
os.environ.update(PSU_MODEL_FIRST_TRIAL='1',PSU_MODEL_FIRST_PLANNER=selected,PSU_MODEL_FIRST_REVIEW='1' if selected=='compact' else '0',PSU_PLANNER_PROFILE='retained',OLLAMA_URL='http://127.0.0.1:12921',PSU_CHATBOT_OLLAMA_MODEL='psu-r129:latest',PSU_ANALYSIS_BUDGET_SEC='60',PSU_ANALYSIS_CALL_SEC='35',PSU_LLM_PREFLIGHT='0')
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.migrated_view import MigratedView
cases=[
 ('dev_static','development','Tekken 8 อยู่โซนไหน แล้ว Tekken 8 มีให้เล่นบนเครื่องอะไรบ้าง',[['C04','zone'],['C04','studio_services']]),
 ('dev_typo','development','มีเกสอะไรบ้าง แล้วจองยังงไ',[['C04','game_catalog'],['C08','owner_policy']]),
 ('fresh_english','fresh_exact_question','Where is Tekken 8 located, and which studio services offer Tekken 8?',[['C04','zone'],['C04','studio_services']]),
 ('fresh_price','fresh_exact_question','บุคคลทั่วไปเล่น Nintendo Switch 30 นาทีราคาเท่าไหร่ แล้วต้องจองอย่างไร',[['C06','amount'],['C08','owner_policy']]),
 ('fresh_two_services','fresh_exact_question','นักศึกษา PSU เล่น PC 30 นาทีราคาเท่าไหร่ และบุคคลทั่วไปเล่น PS5 30 นาทีราคาเท่าไหร่',[['C06','amount'],['C06','amount']]),
 ('fresh_three','fresh_exact_question','Tekken 8 อยู่โซนไหน Tekken 8 ใช้ปุ่มอะไรโจมตี และจองยังไง',[['C04','zone'],['C05','input_bindings'],['C08','owner_policy']])]
def normal(s):return re.sub(r'\W','',s.casefold())
known=set()
for p in [R.parent/'r121_context_planner_training_20261022/train.jsonl',R.parent/'r129_full_plan_completion_20261024/training_v2/train.jsonl',R.parent/'r135_hybrid_eval10_20261110/evaluation/RESULTS.jsonl']:
 for line in p.open(encoding='utf8'):
  row=json.loads(line);q=row.get('question') or row.get('query') or ''
  if q:known.add(normal(q))
assert all(normal(q) not in known for _,kind,q,_ in cases if kind=='fresh_exact_question'),'Fresh probe overlaps saved training/eval exactly'
out=R/(selected+'_real_batch_'+str(time.time_ns()));out.mkdir()
manifest={'cases':cases,'planner':selected,'app_sha256':{str(p.relative_to(R/'system')):hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'system/app').rglob('*.py')},'workers':1,'request_retries':0,'max_model_calls_per_request':2,'freshness':'normalised exact text checked against two training files and saved eval10 rows; not a semantic-family holdout','prompt_examples_added':False}
(out/'MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
reader=CommonAnswerer(MigratedView(R/'system/data/knowledge/verified_sources.sqlite'));rows=[]
for name,kind,q,expected in cases:
 started=time.perf_counter();result=reader.answer(q,locale='en' if kind=='fresh_exact_question' and name=='fresh_english' else 'th',planner=None);audit=result.decision_artifact.get('model_first',{});needs=audit.get('validated_needs',[]);attempts=audit.get('attempts',[])
 if selected=='compact':attempts=[{'transport_completed':audit.get('transport_completed'),'provenance':audit.get('returned_provenance',{})}]+([audit['plan_review']] if audit.get('plan_review',{}).get('attempted') else [])
 expected_profile='retained' if selected=='retained' else 'base'
 checks={'needs_match_declared_intents':sorted([[n['category'],n['facet']] for n in needs])==sorted(expected),'all_raw_spans_exact':all(q[n['source_span']['start']:n['source_span']['end']]==n['quote'] for n in needs),'actual_profile_provenance':bool(attempts) and all(a.get('provenance',{}).get('effective_profile')==expected_profile for a in attempts if a.get('transport_completed')) and any(a.get('transport_completed') for a in attempts),'at_most_one_review':len(attempts)<=2}
 rows.append({'id':name,'kind':kind,'question':q,'seconds':time.perf_counter()-started,'checks':checks,'answer':result.answer,'mode':result.mode,'artifact':result.decision_artifact})
 (out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'id':name,'seconds':rows[-1]['seconds'],'checks':checks,'answer':result.answer},ensure_ascii=False),flush=True)
report={'requests':len(rows),'declared_intent_cases_passed':sum(r['checks']['needs_match_declared_intents'] for r in rows),'cases':[{k:r[k] for k in ['id','kind','seconds','checks']} for r in rows],'scope':'development and fresh exact questions; task checks are not final-answer/source semantic accuracy; failures retained'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report}))
