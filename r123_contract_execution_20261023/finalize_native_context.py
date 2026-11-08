"""Freeze/report native bridge evidence without inventing accuracy scores."""
import hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;ROOT=R.parent;S=R/'revision05_system'
def read(p):return json.loads(p.read_text('utf8'))
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def find_run(pattern):
 paths=[p for p in sorted(R.glob(pattern)) if read(p).get('all_passed') and any('revision05_system' in k for k in read(p.parent/'RUN_FREEZE.json'))]
 assert paths;return paths[-1]
vp=find_run('verification_*/VERIFICATION.json');np=find_run('native_verification_*/VERIFICATION.json')
V=vp.parent;N=np.parent;v=read(vp);n=read(np)
pp=sorted(R.glob('PACKAGE_VERIFICATION_*.json'))[-1];pack=read(pp);assert pack['all_passed']
assert pack['artifact']['execution_contract']['request_context']['version']=='r123-request-provenance-v1'
# Confirm non-vacuous fixture coverage from saved outputs, not just all(...).
native_rows=read(N/'OUTPUTS.json')
fixture_supported=[x for x in native_rows if x['artifact']['execution_contract'].get('path')=='native_calendar_live_bridge' and x['artifact'].get('response_type')=='answer']
assert fixture_supported and all(any(o.get('binding_mapping_and_clock_checked') for t in x['artifact']['execution_contract']['tasks'] for o in t.get('live_observations',[])) for x in fixture_supported)
assert n['provider_calls'] and set(n['provider_calls'])=={'2026-10-21'}
compound=next(x for x in native_rows if x['artifact']['execution_contract'].get('path')=='native_compound_bridge')
assert [r['execution_contract']['task_id'] for r in compound['artifact']['need_results']]==['t1','t2']
old=read(R/'verification_1792693569208529000/SAVED_PLANNER_REPLAY.json')+read(R/'verification_1792693569208529000/RETAINED_API_PROPOSAL_REPLAY.json')
new=read(V/'SAVED_PLANNER_REPLAY.json')+read(V/'RETAINED_API_PROPOSAL_REPLAY.json')
changes=[]
for a,b in zip(old,new):
 assert (a['key'],a['question'])==(b['key'],b['question'])
 def projected(x):return {k:x['result'][k] for k in ('answer','status','claims')}
 if projected(a)!=projected(b):changes.append({'key':b['key'],'question':b['question'],'before':projected(a),'after':projected(b)})
regression={'parent':'R123 revision03','candidate':'R123 revision05','saved_proposals':len(new),'unique_question_keys':len({x['key'] for x in new}),
 'changed_answer_status_or_claim_rows':len(changes),'changes':changes,'new_model_calls':0,'semantic_accuracy':None}
(R/'NATIVE_CONTEXT_REGRESSION.json').write_text(json.dumps(regression,ensure_ascii=False,indent=2),'utf8')
protected={}
paths=[R/'PARENT_FREEZE.json',R/'REVISION04_PARENT_FREEZE.json',R/'REVISION05_PARENT_FREEZE.json',
 ROOT/'r121_context_planner_training_20261022/PROTECTED_INPUTS.json',ROOT/'r121_context_planner_training_20261022/train02/RUN_FREEZE.json',
 *R.glob('verification_*/RUN_FREEZE.json'),*R.glob('native_verification_*/RUN_FREEZE.json')]
for path in paths:
 for name,h in read(path).items():
  assert name not in protected or protected[name]==h,('contradictory_freeze',name)
  protected[name]=h
design=ROOT/'r123_plan_distillation_architecture_20261023'
for name,h in read(design/'PLAN_STATUS.json')['document_sha256'].items():protected[str((design/name).resolve())]=h
changed=[name for name,h in protected.items() if not Path(name).is_file() or sha(Path(name))!=h]
assert not changed,changed
adapter=ROOT/'r121_context_planner_training_20261022/train02/adapter/adapter_model.safetensors'
assert sha(S/'data/knowledge/common.sqlite')==read(R/'LINEAGE.json')['database_sha256']
assert sha(adapter)==read(ROOT/'r122_context_scope_calendar_20261022/LINEAGE.json')['same_adapter_sha256']
preservation={'files_checked':len(protected),'changed':changed,'database_sha256':sha(S/'data/knowledge/common.sqlite'),
 'same_r121_adapter_sha256':sha(adapter),'new_model_calls':0,'new_training':False,'production_installed':False,
 'foundation_verification':str(vp),'native_verification':str(np),'packaging_verification':str(pp),
 'non_vacuous_native_fixture_success_confirmed':True,'all_provider_fixture_calls_used_pinned_date':True,'compound_need_ids_match_parent_task_ids':True}
(R/'NATIVE_CONTEXT_FINAL_VERIFICATION.json').write_text(json.dumps(preservation,ensure_ascii=False,indent=2),'utf8')
prior=R/'IMPLEMENTATION_STATUS_foundation_r03.json'
if not prior.exists():shutil.copyfile(R/'IMPLEMENTATION_STATUS.json',prior)
status={'status':'native_context_bridge_implemented_and_verified','candidate':str(S),'design_version':'R123','implementation_revision':'native-context-r05',
 'full_r123_architecture_implemented':False,'candidate_ready_for_production':False,'candidate_ready_for_new_distillation':False,
 'phase_scope':{'P0':'legacy planner wire retained; input raw/normalization/derived provenance receipts added',
 'P1':'compiled tasks and ordinary-history path connected; shared-prefix semantics and general history binding still incomplete',
 'P2':'calendar/live and missing-binding guards audited; native compounds sequential, not globally typed-first',
 'P3_P8':'authority/compiler completion, semantic annotation review, new training and heldout comparison pending'},
 'verification':{'foundation_checks':len(v['checks']),'native_context_checks':len(n['checks']),'packaging_checks':len(pack['checks']),
 'all_passed':True,'annotation_rows_compiled':289,'saved_proposals_replayed':40,'unique_question_keys':32,
 'native_adapter_response_observations':len(native_rows),'native_question_keys':len({x['key'] for x in native_rows}),
 'new_model_calls':0,'actual_http_benchmark':False,'full_test':False,'fresh_semantic_accuracy':None},
 'data_limitations':{'live_binding_count_in_current_database':0,'provider_binding_test':'in-memory fixtures only; not published or saved to DB'},
 'artifacts':{'report':str(R/'NATIVE_CONTEXT_REPORT_TH.md'),'flow':str(R/'FLOW_NATIVE_CONTEXT_TH.md'),'preservation':str(R/'NATIVE_CONTEXT_FINAL_VERIFICATION.json'),
 'regression':str(R/'NATIVE_CONTEXT_REGRESSION.json'),'manual_launcher':str(R/'launch_revision05.py')},
 'next_work':['complete shared-prefix and typed history bindings with explicit source scope','finish authority/collection/operator diagnostics',
 'semantic-review the complete label set before new distillation','freeze unexposed question families and evaluate base/current/new planner with identical executors/data']}
(R/'IMPLEMENTATION_STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2),'utf8')
(R/'NATIVE_CONTEXT_STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'status':status['status'],'checks':status['verification'],'preservation_files':len(protected),'changed':changed,'regression_rows_changed':len(changes)},ensure_ascii=False,indent=2))
