"""Retain original graders/questions; configure the actual available model server."""
import json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent/'r130_owner_context_completion_20261025'
p=R/'start_candidate.py';text=p.read_text('utf8')
text=text.replace("OLLAMA_URL='http://127.0.0.1:13221'", "OLLAMA_URL=os.environ.get('R132_MODEL_URL','http://127.0.0.1:12921')")
p.write_text(text,'utf8')
for name in ['reference_grader.py','verify_extended.py','verify_graph_runtime.py','verify_owner_scopes.py','verify_comparisons.py','verify_live.py','verify_source_guards.py','verify_source_match_metadata.py','run_acceptance.py','run_context_acceptance.py','run_owner_api_acceptance.py']:
 target=R/name
 if not target.exists():shutil.copy2(P/name,target)
(R/'MODEL_ACTIVATION_STATUS.json').write_text(json.dumps({'actual_url':'http://127.0.0.1:12921','actual_model_alias':'psu-r129:latest','actual_base':'typhoon-ai/typhoon2.5-qwen3-4b','context_profile':'retained','weights_changed':False,'explicit_prompt_protocol_fix_active_in_candidate':True,'staged_schema_decoder':'lm-format-enforcer0.11.3','staged_decoder_activated':False,'staged_decoder_handoff_auto_review':'blocked by policy','existing_server_stopped':False},indent=2),'utf8')
print('Original graders and acceptance inputs retained; runtime uses the existing model server.')
