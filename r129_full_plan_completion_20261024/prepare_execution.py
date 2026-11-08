"""Prepare isolated API and the retained full-workload harness (no run)."""
import ast,json
from pathlib import Path
R=Path(__file__).resolve().parent;OLD=R.parent/'r128_complete_common_flow_20261024';F=R.parent/'r106_complete_flow_20261020'
api=(OLD/'serve_api.py').read_text('utf8').replace('R128','R129').replace('12421','12921')
(R/'serve_api.py').write_text(api,'utf8')
start=(OLD/'start_candidate.py').read_text('utf8')
start=start.replace("os.environ.get('R128_PORT','12822')","os.environ.get('R129_PORT','12922')")
# Use the reviewed local instrumentation file; never regenerate it at launch.
begin=start.index('source=(R.parent/');end=start.index("OUT=R/('api_'",begin);start=start[:begin]+start[end:]
start=start.replace('psu-r121-trained:latest','psu-r129:latest').replace('12421','12921').replace('r128-complete-common-flow','r129-full-plan-flow').replace("PSU_RUNTIME_VERSION='R128'","PSU_RUNTIME_VERSION='R129'")
start=start.replace("env.update(OLLAMA_URL=","env.update(PSU_PLANNER_PROFILE=os.environ.get('PSU_PLANNER_PROFILE','retained'),OLLAMA_URL=")
(R/'start_candidate.py').write_text(start,'utf8')
for name in ['run_acceptance.py','run_context_acceptance.py']:(R/name).write_text((OLD/name).read_text('utf8'),'utf8')
(R/'reference_grader.py').write_bytes((F/'reference_grader.py').read_bytes())
full=(F/'run_common.py').read_text('utf8')
full=full.replace("PSU_ESPORTS_NOW='2026-10-16T12:00:00+07:00'","PSU_ESPORTS_NOW='2026-10-16T12:00:00+07:00',OLLAMA_URL='http://127.0.0.1:12921',PSU_CHATBOT_OLLAMA_MODEL='psu-r129:latest',PSU_KNOWLEDGE_LLM_MODEL='psu-r129:latest',PSU_QUERY_PLANNER_MODEL='psu-r129:latest',PSU_TOOL_ROUTER_MODEL='psu-r129:latest',PSU_INTENT_LLM_MODEL='psu-r129:latest'")
full=full.replace("PSU_PIPELINE_GLOBAL_TIMEOUT_SEC='18'","PSU_PIPELINE_GLOBAL_TIMEOUT_SEC='180'").replace("PSU_PRODUCT_BACKEND_TIMEOUT_SEC='20'","PSU_PRODUCT_BACKEND_TIMEOUT_SEC='190'")
full=full.replace("global_timeout_sec=18","global_timeout_sec=180").replace("conn.poll(28)","conn.poll(200)").replace('request watchdog 28 seconds','request watchdog 200 seconds').replace("conn.poll(90)","conn.poll(120)")
full=full.replace("(':11434/' in url)","(':12921/' in url)")
full=full.replace('R95 controlled unavailable; no actual booking oracle','R129 controlled unavailable; no actual booking oracle')
full=full.replace("R/'SELECTED_JOBS.jsonl'","R.parent/'r95_merged_flow_implementation_20261018/FULL_JOBS.jsonl'")
(R/'run_common.py').write_text(full,'utf8')
for name in ['serve_api.py','start_candidate.py','run_acceptance.py','run_context_acceptance.py','reference_grader.py','run_common.py']:ast.parse((R/name).read_text('utf8'))
(R/'EXECUTION_CONFIGURATION.json').write_text(json.dumps({'full_workload_source':'saved R95 FULL_JOBS.jsonl','full_request_deadline_sec':180,'worker_watchdog_sec':200,'retained_reference_contract_latency_ceiling_unchanged':True,'deadline_changed_from_R106_and_must_be_reported':True,'llm_allowed_not_forced':True,'full_live_provider':'controlled_unavailable','real_provider_separate_readiness':True,'full_reference_clock':'2026-10-16 plus each retained explicit reference_date','three_arm_reference_clock':'2026-10-24T12:00:00+07:00','full_test_started':False},indent=2),'utf8')
print('Prepared API and common-only LLM-ON harness; no full questions executed.')
