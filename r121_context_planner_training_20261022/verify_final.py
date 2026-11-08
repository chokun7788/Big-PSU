import hashlib,json,sys
from pathlib import Path
R=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text('utf8'))
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
protected=read(R/'PROTECTED_INPUTS.json');assert all(Path(p).is_file() and sha(p)==h for p,h in protected.items())
runs={}
for name,expected in [('api02',16),('guard01',14),('priority01',4),('reader01',3)]:
 done=read(R/name/'TEST_COMPLETE.json');assert done['complete'] and done['total_requests']==expected
 freeze=read(R/name/'RUN_FREEZE.json');assert all(sha(p)==h for p,h in freeze.items())
 runs[name]={'complete':True,'requests':expected,'all_http_200':done['all_requests_successful'],'frozen_files_unchanged':True}
train=read(R/'train02/TRAINING_COMPLETE.json');assert train['complete'] and train['optimizer_steps']==93
freeze=read(R/'train02/RUN_FREEZE.json');assert all(sha(p)==h for p,h in freeze.items())
adapter=R/'train02/adapter/adapter_model.safetensors';adapter_sha=sha(adapter)
manifests=[read(R/name/'SERVER.json') for name in ['inference01','inference02','inference03','inference04','inference05']]
assert all(m['adapter_sha256']==adapter_sha and m['base_revision']=='ce0a7416fe82d4404b2b4a253ce3ac095ab1252c' for m in manifests)
dbhashes={name:sha(R/name/'data/knowledge/common.sqlite') for name in ['system','revision02_system','revision03_system','revision04_system']};assert len(set(dbhashes.values()))==1
proof=read(R/'train02/OPTIMIZATION_PROOF.json');assert proof['actual_weight_updates'] and proof['base_parameter_hash_unchanged'] and proof['initial_adapter']['sha256']!=proof['final_adapter']['sha256']
out={'verified':True,'original_protected_files':len(protected),'original_files_unchanged':True,'training_code_inputs_unchanged':True,'actual_optimizer_steps':93,'base_parameters_unchanged':True,'adapter_sha256':adapter_sha,'all_loaded_adapters_match':True,'native_database_sha256_by_revision':dbhashes,'native_data_and_approvals_unchanged':True,'runs':runs,'new_questions':0,'production_installed':False,'full_test_run':False,'posthoc_development_is_not_fresh_heldout':True}
(R/'FINAL_VERIFICATION.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
# Calendar source evidence helps distinguish a reader gap from missing records.
sys.path.insert(0,str(R/'revision04_system'))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.migrated_view import MigratedView
engine=Engine.from_snapshot(MigratedView(R/'revision04_system/data/knowledge/common.sqlite').snapshot())
calendar=[f for f in engine.index.bycat['C11'] if f['facet']=='service_periods']
(R/'CALENDAR_SOURCE_EVIDENCE.json').write_text(json.dumps({'recorded_service_period_facts':len(calendar),'facts':calendar,'note':'Recorded weekly service periods exist; this does not itself prove Cockpit-specific applicability or live status.'},ensure_ascii=False,indent=2),'utf8')
print(json.dumps(out,ensure_ascii=False,indent=2))
