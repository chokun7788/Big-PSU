"""Serial real local-model probes; no retry and no simulated model success."""
import json,os,sys,time
from verification_support import R
os.environ.update({'PSU_MODEL_FIRST_TRIAL':'1','OLLAMA_URL':'http://127.0.0.1:12921','PSU_CHATBOT_OLLAMA_MODEL':'psu-r129:latest','PSU_ANALYSIS_BUDGET_SEC':'60','PSU_ANALYSIS_CALL_SEC':'35','PSU_PLANNER_PROFILE':'retained','PSU_LLM_PREFLIGHT':'0','PSU_CONVERSATION_STATE_PATH':str(R/'probe_runtime/conversations.sqlite')})
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.migrated_view import MigratedView
reader=CommonAnswerer(MigratedView(R/'system/data/knowledge/verified_sources.sqlite'))
q=sys.argv[1] if len(sys.argv)>1 else 'Tekken 8 อยู่โซนไหน แล้วเครื่องไหนพร้อมให้เล่น Tekken 8 บ้าง'
out=R/('actual_model_probe_'+str(time.time_ns()));out.mkdir();started=time.perf_counter()
result=reader.answer(q,locale='th',planner=None);audit=(result.decision_artifact or {}).get('model_first',{})
summary={'question':q,'seconds':time.perf_counter()-started,'answer':result.answer,'mode':result.mode,'actual_model_plan':audit,'request_plan':(result.decision_artifact or {}).get('request_plan'),'limits':'one actual model request; not a semantic accuracy score; source renderer not free-form model prose'}
(out/'RESULT.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf8');(out/'ARTIFACT.json').write_text(json.dumps(result.decision_artifact,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'output':str(out),**summary},ensure_ascii=False))
