"""Verify preserved parent and actual HTTP trace; no inference or source edits."""
import hashlib,json,sqlite3
from pathlib import Path
R=Path(__file__).resolve().parent
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
base=json.loads((R/'BASELINE_MANIFEST.json').read_text());parent=Path(base['parent'])
unchanged=all(digest(parent/'system'/p)==h for p,h in base['app_sha256'].items())
assert unchanged,'Parent changed'
delta=[p for p,h in base['app_sha256'].items() if digest(R/'system'/p)!=h]
http=R/'http_model_first_1794469634351112700'
response=json.loads((http/'RESPONSE.json').read_text(encoding='utf8'))
conn=sqlite3.connect((R/'preview/runtime/logs/transcripts.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
row=conn.execute("select metadata_json from chat_messages where session_id=? and role='assistant' order by id desc limit 1",(response['session_id'],)).fetchone();conn.close()
artifact=json.loads(row[0])['decision_artifact'];audit=artifact['model_first']
assert audit['transport_completed'] and len(audit['validated_needs'])==2
(http/'ARTIFACT.json').write_text(json.dumps(artifact,ensure_ascii=False,indent=2),encoding='utf8')
manifest={'parent_preserved':unchanged,'parent_app_files_checked':len(base['app_sha256']),'changed_inherited_app_files':delta,'new_app_files':['app/knowledge/common/model_first.py'],'app_sha256':{str(p.relative_to(R/'system')):digest(p) for p in (R/'system/app').rglob('*.py')},'actual_http':{'result':'http_model_first_1794469634351112700/RESULT.json','seconds':json.loads((http/'RESULT.json').read_text())['seconds'],'trace_model_transport_completed':True,'trace_model_need_count':2,'profile':audit['returned_provenance']['effective_profile'],'raw_plan_sha256':hashlib.sha256(audit['raw_model_content'].encode()).hexdigest()},'final_source_replay':'saved_plan_replay_1794469494989192800/RESULT.json','final_mocked_protocol':'protocol_controls_1794469538506149800/RESULT.json','actual_final_probe':'actual_model_probe_1794469548606677900/RESULT.json','raw_logs_private':True,'deployed':False,'full_eval_started':False,'semantic_accuracy_claimed':False}
(R/'IMPLEMENTATION_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
(R/'STATUS.json').write_text(json.dumps({'phase':'model_first_trial_evidence_saved_known_semantic_gaps','parent':'r135_recovery_loop_20261112','deployed':False,'full_eval_running':False,'preview_port':8145,'report':'MODEL_FIRST_REPORT_TH.md','next_group':'bind task context spans then reconcile request coverage; preserve failed model intents'},ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'parent_preserved':unchanged,'parent_files':len(base['app_sha256']),'changed_files':delta,'http_trace_verified':True}))
