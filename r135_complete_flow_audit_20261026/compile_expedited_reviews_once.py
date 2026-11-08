"""One final corpus compilation after all64 actual staged reviews exist."""
import copy,json
from pathlib import Path
from manual_review_support import record_round,W
from app.knowledge.common.domain_flow.training_contract import file_sha,digest,source_identity

def read(p):return json.loads(p.read_text('utf8'))
O=W/'expedited_staged_reviews_20261027';paths=sorted(O.glob('STAGED_*.json'));records=[read(p) for p in paths];missing=sorted(set(range(225,289))-{r['original_row'] for r in records})
if missing:
 print(json.dumps({'compiled':False,'phase':'individual_review_incomplete','missing_original_rows':missing,'current_cohorts_unchanged':True}));raise SystemExit(2)
assert len(records)==64 and len({r['question_key'] for r in records})==64
base=W/'review_round_012';examples=[json.loads(x) for x in (base/'EXAMPLES.jsonl').read_text('utf8').splitlines()];lookup={x['annotation_provenance']['historical_review_ref']['line']-1:x for x in examples};source=read(W/'SOURCE_SNAPSHOT.json');base_sha=file_sha(base/'EXAMPLES.jsonl');source_sha=file_sha(W/'SOURCE_SNAPSHOT.json');identity=digest(source_identity(source))
for r in records:
 x=lookup[r['original_row']];assert r['raw_question']==x['raw_question'] and r['question_key']==x['question_key'] and r['prior_label']==x['plan_label'] and r['base_example_ref']['sha256']==base_sha and r['source_snapshot_ref']['sha256']==source_sha and r['source_identity_sha256']==identity
 for rid,e in r['source_field_evidence'].items():assert e=={'revision':source['release']['records'][rid]['revision'],'record_sha256':digest(source['release']['records'][rid])}
if (O/'COMPILATION_RECEIPT.json').exists():
 old=read(O/'COMPILATION_RECEIPT.json');assert old['staged_files']=={str(p.name):file_sha(p) for p in paths};print(json.dumps({'compiled':True,'already_compiled':True,**old}));raise SystemExit(0)
from app.knowledge.common.domain_flow.training_contract import CRITERIA
notes={r['original_row']:tuple(r['notes'][k] for k in CRITERIA) for r in records};ids={r['original_row']:r['source_record_ids'] for r in records};issues={r['original_row']:r['source_answer_issues'] for r in records};quarantines={r['original_row']:r['quarantine_reason'] for r in records if r['quarantine_reason']}
def replace(value):
 def apply(p):p.clear();p.update(copy.deepcopy(value))
 return apply
edits={r['original_row']:replace(r['reviewed_label']) for r in records if r['reviewed_label']!=r['prior_label']}
record_round('review_round_013','review_round_012',notes,ids,edits,issues,quarantines=quarantines)
summary=read(W/'review_round_013/SUMMARY.json');assert summary['individually_adjudicated']==289 and summary['unreviewed']==0
receipt={'compiled_round':'review_round_013','staged_files':{p.name:file_sha(p) for p in paths},'summary_sha256':file_sha(W/'review_round_013/SUMMARY.json'),'repeated_semantic_reviews_claimed':False,'current_v2_v3_packers_or_optimizers_switched':False,'actual_model_inferences_or_training':0}
(O/'COMPILATION_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'compiled':True,**receipt}))
