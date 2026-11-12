"""Four declared serial actual-model cases, retain failures; never retry a case."""
import json,os,time
from verification_support import R
os.environ.update({'PSU_MODEL_FIRST_TRIAL':'1','OLLAMA_URL':'http://127.0.0.1:12921','PSU_CHATBOT_OLLAMA_MODEL':'psu-r129:latest','PSU_ANALYSIS_BUDGET_SEC':'60','PSU_ANALYSIS_CALL_SEC':'35','PSU_LLM_PREFLIGHT':'0','PSU_CONVERSATION_STATE_PATH':str(R/'probe_runtime/conversations.sqlite')})
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.migrated_view import MigratedView
cases=[('clear_static','Tekken 8 อยู่โซนไหน แล้ว Tekken 8 มีให้เล่นบนเครื่องอะไรบ้าง'),('explicit_live','Tekken 8 อยู่โซนไหน แล้วเครื่องไหนว่างให้เล่น Tekken 8 ตอนนี้บ้าง'),('typo_two','มีเกสอะไรบ้าง แล้วจองยังงไ'),('price_booking','นักศึกษา PSU เล่น PC 30 นาที เสียกี่บาท แล้วจองยังไง')]
out=R/('real_model_batch_'+str(time.time_ns()));out.mkdir();reader=CommonAnswerer(MigratedView(R/'system/data/knowledge/verified_sources.sqlite'));rows=[]
(out/'MANIFEST.json').write_text(json.dumps({'cases':cases,'worker_count':1,'retry_count':0,'scope':'focused development cases, not unseen semantic accuracy'},ensure_ascii=False,indent=2),encoding='utf8')
for name,q in cases:
 started=time.perf_counter();result=reader.answer(q,locale='th',planner=None);a=(result.decision_artifact or {}).get('model_first',{});needs=a.get('validated_needs',[])
 checks={'actual_model_transport':a.get('transport_completed') is True,'two_model_needs':len(needs)==2}
 if name=='clear_static':checks['two_required_meanings']={n['facet'] for n in needs}=={'zone','studio_services'};checks['machine_scope_notice']='ไม่ใช่สถานะว่าเครื่องว่าง' in result.answer
 if name=='explicit_live':checks['live_not_substituted_with_static']=any(n['category']=='C12' or n['ambiguity']!='none' for n in needs)
 if name=='typo_two':checks['catalog_and_booking']={n['facet'] for n in needs}=={'game_catalog','owner_policy'};checks['booking_delivered']='สลิป' in result.answer
 if name=='price_booking':checks['price_and_booking']={n['facet'] for n in needs}=={'amount','owner_policy'};checks['price_delivered']='0 บาท' in result.answer;checks['booking_delivered']='สลิป' in result.answer
 rows.append({'id':name,'question':q,'seconds':time.perf_counter()-started,'checks':checks,'passed':all(checks.values()),'answer':result.answer,'mode':result.mode,'audit':a,'artifact':result.decision_artifact})
 (out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
 print(json.dumps({'id':name,'seconds':rows[-1]['seconds'],'checks':checks,'answer':result.answer},ensure_ascii=False),flush=True)
report={'requests':len(rows),'checks_passed_cases':sum(x['passed'] for x in rows),'all_declared_cases_passed':all(x['passed'] for x in rows),'cases':[{k:x[k] for k in ['id','seconds','checks','passed']} for x in rows],'scope':'actual model outputs with purpose-built checks; semantic adequacy/source validity must be reviewed separately; no benchmark score'}
(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report},ensure_ascii=False))
