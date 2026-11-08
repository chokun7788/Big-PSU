import json,os,sys
from pathlib import Path
from types import SimpleNamespace
B=Path(__file__).resolve().parent;T=B/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False)
os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(B/'system/data/knowledge/common.sqlite'),PSU_PIPELINE_WARMUP='0',PSU_PIPELINE_WORKER_SUPERVISOR='0',PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_LLM_PREFLIGHT='0',PSU_CHAT_LOG_DIR=str(T/'logs'),PSU_CONVERSATION_STATE_PATH=str(T/'state.sqlite'))
sys.path.insert(0,str(B/'system'))
from app.web_api.server import _trace_query_debug
results=json.loads((B/'verification/rephrase02/RESULTS.json').read_text(encoding='utf8'))
case=next(r for r in results['checks'] if r['case']=='No, I mean how do I pay?')
artifact=case['detail']['artifact'];repair=artifact['dialogue_repair'];q=repair['original_input']
debug=_trace_query_debug(SimpleNamespace(trace=[],decision_artifact=artifact),q,q)
plain=_trace_query_debug(SimpleNamespace(trace=[],decision_artifact={}),q,q)
rows=[{'case':'Stored repaired answer exposes actual active query','passed':debug['active_query']=='how do I pay?' and debug['active_query_changed'],'detail':debug},
 {'case':'Original raw question remains available for analysis','passed':debug['original_question']==q and debug['resolved_question']==q},
 {'case':'Normal debug path keeps original behavior','passed':plain['active_query']==q and not plain['active_query_changed']}]
result={'count':len(rows),'passed':sum(r['passed'] for r in rows),'scope':'debug extraction using stored dispatcher output, no new model/HTTP request','checks':rows}
(T/'RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({k:v for k,v in result.items() if k!='checks'}));raise SystemExit(any(not r['passed'] for r in rows))
