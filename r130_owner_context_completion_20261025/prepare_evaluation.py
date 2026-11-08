"""Prepare the latest candidate harness; never launch a second raw comparison."""
import hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent/'r129_full_plan_completion_20261024'
def put(name,text):
 target=R/name
 if name=='EVALUATION_PREPARATION.json' and not (R/'EXECUTION_FREEZE_R130.json').exists():target.write_text(text,'utf8');return
 if target.exists():assert target.read_text('utf8')==text,('Do not overwrite prepared artifact',name)
 else:target.write_text(text,'utf8')
text=(P/'compare_planners_v2.py').read_text('utf8')
text=text.replace("D=R/'training_v2'","P=R.parent/'r129_full_plan_completion_20261024';D=P/'training_v2'")
text=text.replace("OUT=R/'three_arm02'","OUT=R/'paired_replay03'")
text=text.replace("R/'compare_planners_v2.py'","R/'replay_planners.py'").replace("R/'serve_model.py'","P/'serve_model.py'")
text=text.replace("prior=R/'three_arm01/RESULTS.jsonl'","prior=P/'three_arm02/RESULTS.jsonl'\nassert json.loads((prior.parent/'SUMMARY.json').read_text('utf8'))['complete']\nassert sum(1 for _ in prior.open(encoding='utf8'))==330")
text=text.replace("row['raw_transport_reused_from']='three_arm01/RESULTS.jsonl';row['planner_elapsed_sec']=previous['elapsed_sec']","row['raw_transport_reused_from']=str(prior);row['new_context_inference']=False;row['planner_elapsed_sec']=previous.get('planner_elapsed_sec',previous['elapsed_sec'])")
old="""    else:
     req=urllib.request.Request('http://127.0.0.1:12921/api/chat',data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
     with urllib.request.urlopen(req,timeout=100) as response:raw=json.load(response)
     row['planner_elapsed_sec']=time.monotonic()-before"""
assert old in text
text=text.replace(old,"""    else:
     row['new_context_inference']=False
     raise ValueError('Saved raw transport or identity unavailable; do not regenerate planner output')""")
text=text.replace("'phase':'paired_inference'","'phase':'paired_source_execution_replay'")
text=text.replace("'PLANNER_ADJUDICATION.json'","'PLANNER_ADJUDICATION_R130.json'")
text=text.replace("'harness_version':'r129-paired-v2-invalid-wire-fallback-and-shared-budget'","'harness_version':'r130-frozen-raw-planner-replay-same-engine-and-source-all-three-arms'")
text=text.replace("'historically_exposed_questions':True","'new_context_model_inferences':0,'raw_model_output_source':str(prior),'historically_exposed_questions':True")
anchor="    prov=raw['provenance'];assert raw['model']==payload['model'] and prov['effective_profile']==arm and prov['effective_messages_sha256']==digest(wire) and prov['effective_schema_sha256']==digest(sch)"
text=text.replace(anchor,anchor+"\n    identity=json.loads((P/'MODEL_IDENTITY_BEFORE.json').read_text('utf8'))\n    assert prov['profile_digest']==identity['profile_digests'][arm] and prov['adapter_sha256']==identity['profiles'][arm] and prov['base_revision']==identity['base_revision'] and prov['quantization']==identity['quantization'] and prov['stage']=='context_understanding' and prov['effective_max_new_tokens']==900")
text=text.replace("all_rows=[];start=time.time()","freeze[str(prior.resolve())]=sha(prior);write('RUN_FREEZE.json',freeze)\nassert len(cached_transport)<=330\nall_rows=[];start=time.time()")
put('replay_planners.py',text)
for name in ['EVALUATION_PROTOCOL.json','EVALUATION_GATE_ADDENDUM.json','reference_grader.py','run_common.py','serve_api.py','run_acceptance.py','run_context_acceptance.py','SAVED_LEGACY_REFERENCE.json']:
 text=(P/name).read_text('utf8')
 if name in {'serve_api.py','run_common.py'}:text=text.replace('R129 controlled unavailable','R130 controlled unavailable')
 put(name,text)
text=(P/'start_candidate.py').read_text('utf8').replace("'R129_PORT','12922'","'R130_PORT','13024'").replace("PSU_RUNTIME_PROFILE='r129-full-plan-flow',PSU_RUNTIME_VERSION='R129'","PSU_RUNTIME_PROFILE='r130-owner-context-complete-flow',PSU_RUNTIME_VERSION='R130'")
put('start_candidate.py',text)
text=(P/'analyze_full_v2.py').read_text('utf8').replace('EXECUTION_FREEZE_V2.json','EXECUTION_FREEZE_R130.json').replace('R129','R130')
anchor="identity=load(R/'MODEL_IDENTITY_BEFORE.json')['profile_digests']==load(R/'MODEL_IDENTITY_AFTER.json')['profile_digests']"
text=text.replace(anchor,anchor+"\nlogical_source_unchanged=load(R/'SOURCE_SNAPSHOT_BEFORE.json')==load(R/'SOURCE_SNAPSHOT_AFTER.json')\nassert logical_source_unchanged,'Logical source changed, including potential WAL changes'")
put('analyze_full.py',text)
text=(P/'reconcile_saved_scores.py').read_text('utf8').replace('R129','R130')
text=text.replace("[R/'SAVED_LEGACY_ROWS.jsonl.gz']","[R.parent/'r129_full_plan_completion_20261024/SAVED_LEGACY_ROWS.jsonl.gz']")
put('reconcile_saved_scores.py',text)
hashes={name:hashlib.sha256((R/name).read_bytes()).hexdigest() for name in ['replay_planners.py','run_common.py','reference_grader.py','start_candidate.py','analyze_full.py','reconcile_saved_scores.py']}
put('EVALUATION_PREPARATION.json',json.dumps({'prepared':True,'new_raw_planner_inferences_authorized_by_this_script':0,'paired_replay_requires_all_330_saved_outputs':True,'raw_context_wire_unchanged':all((R/'system/app/knowledge/common/domain_flow'/name).read_bytes()==(P/'system/app/knowledge/common/domain_flow'/name).read_bytes() for name in ['graph_protocol.py','understanding.py']),'full_test_not_started':True,'harness_sha256':hashes},indent=2))
print('Prepared R130 replay and latest-candidate-only full harness. No inference started.')
