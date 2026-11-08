"""Post-gate offline causal refinement; in-memory patch, never edits runtime."""
import gzip,json,sqlite3,sys,time
from dataclasses import asdict
from pathlib import Path
from unittest.mock import patch
R=Path(__file__).resolve().parent;P=R.parent/'r130_owner_context_completion_20261025';sys.path.insert(0,str(P/'system'))
from app.knowledge.common.domain_flow.projection import compile_snapshot,value
from app.knowledge.common.domain_flow.index import FactIndex
from app.knowledge.common.domain_flow.precision import equipment
c=sqlite3.connect((P/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);c.row_factory=sqlite3.Row;c.execute('BEGIN')
records={r['record_id']:json.loads(r['payload']) for r in c.execute('SELECT r.* FROM cc_revisions r JOIN cc_heads h USING(record_id) WHERE r.version=h.head AND h.withdrawn=0')}
pairs={r['source_id']:(json.loads(r['payload']),r['snapshot']) for r in c.execute('SELECT * FROM cc_sources')}
snapshot={'active':'migration-preview-r69','epoch':2497,'release':{'records':records,'sources':{k:v[0] for k,v in pairs.items()}},'source_pairs':pairs,'withdrawn':[],'allow_demo':False}
idx=FactIndex(compile_snapshot(snapshot));correct=idx.byrecord['equipment_gaming_pc'];cases=[]
for line in gzip.open(R/'CASE_DIAGNOSTICS.jsonl.gz','rt',encoding='utf8'):
 x=json.loads(line)
 if not any('requested_hardware_component_not_recorded' in str(i.get('proof')) for i in x['observed_issues']):continue
 q=x['question'];pool=idx.bind('C03',q);before=equipment(idx,q)
 with patch.object(idx,'bind',return_value=correct):after=equipment(idx,q)
 assert before.reason=='requested_hardware_component_not_recorded' and after.reason=='typed_hardware_component' and after.ids
 assert not any(f['record_id']=='equipment_gaming_pc' for f in pool)
 cases.append({'key':x['key'],'question':q,'saved_answer':x['delivered_answer'],'first_failing_stage':'entity_binding','root_cause':'Thai alias substring + longer alias suppresses correct model; nonempty wrong pool prevents device-type fallback','before_plan':asdict(before),'original_pool':[(f['record_id'],f['facet']) for f in pool],'counterfactual_plan':asdict(after),'only_changed_variable':'FactIndex.bind return pool, patched in-memory in this diagnostic process only','source_record':'equipment_gaming_pc','source_revision':records['equipment_gaming_pc']['revision'],'gpu_field':next(v for v in value(records['equipment_gaming_pc'],'specifications') if v['key']=='GPU'),'confirmed_scope':'recorded project specification exists and can be read when binding is corrected; not independent physical inventory verification'})
assert len(cases)==13
(R/'POST_GATE_GPU_CAUSAL_REFINEMENT.json').write_text(json.dumps({'created_at_unix':time.time(),'diagnosis_gate_already_completed':True,'refinement_during_sample_execution':True,'candidate_runtime_edited':False,'assistant_or_model_requests':0,'cases':cases,'unique_requests':13,'main_pretest_review_overlap':1,'additional_individually_probed_keys':12,'source_unchanged':True},ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'probed_keys':13,'only_binding_changed_in_memory':True,'all_counterfactuals_read_recorded_gpu':True,'runtime_edits':0,'model_requests':0}))
