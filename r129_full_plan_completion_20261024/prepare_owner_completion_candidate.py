"""Create the next isolated candidate; never alter the running experiment."""
import hashlib,json,shutil,time
from pathlib import Path
P=Path(__file__).resolve().parent;R=P.parent/'r130_owner_context_completion_20261025';R.mkdir(exist_ok=True)
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
frozen=json.loads((P/'EXECUTION_FREEZE_V2.json').read_text('utf8'));assert all(sha(p)==h for p,h in frozen.items()),'R129 changed before candidate copy'
assert not (R/'system').exists(),'Do not overwrite a candidate'
shutil.copytree(P/'system',R/'system',ignore=shutil.ignore_patterns('__pycache__','*.pyc','*-wal','*-shm'))
shutil.copytree(P/'spec',R/'spec')
files={str(p.resolve()):sha(p) for p in (P/'system').rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc'}
(R/'PARENT_FREEZE.json').write_text(json.dumps(files,indent=2),'utf8');(R/'REQUIREMENTS.json').write_bytes((P/'REQUIREMENTS.json').read_bytes())
source=P.parent/'r107_owner_questions_20261020/owner_update_50'
inputs=[source/'SOURCE_OWNER_50.json',source/'PREFILL_PAYLOAD.json',P.parent/'r109_owner_answers_20261020/SOURCE_STATE.json',P.parent/'r109_owner_answers_20261020/REMAINING_LIMITS.json']
(R/'OWNER_INPUT_FREEZE.json').write_text(json.dumps({str(p.resolve()):sha(p) for p in inputs},indent=2),'utf8')
(R/'LINEAGE.json').write_text(json.dumps({'parent_candidate':str(P),'created_at':time.time(),'purpose':'Complete original R123 P3 owner-source mappings and authority on every answer path','parent_system_unchanged':True,'real_data_changed':False,'production_approvals_changed':False,'production_installed':False,'planner_weights':str(P/'training_v2/train01/adapter'),'new_training_needed_for_business_data_changes':False,'paired_context_outputs':'Reuse saved R129 three_arm02 only with exact messages/schema/profile/precision/decoding receipts; replay same new engine/data for all arms','full_test_target':'latest completed candidate only, common LLM ON 20554 keys / 55811 grades'},ensure_ascii=False,indent=2),'utf8')
(R/'STATUS.json').write_text(json.dumps({'phase':'owner_source_scope_audit','complete':False,'source_migration_complete':False,'paired_replay_complete':False,'full_test_complete':False},indent=2),'utf8')
print(json.dumps({'candidate':str(R),'parent_unchanged':True,'frozen_owner_inputs':len(inputs)}))
