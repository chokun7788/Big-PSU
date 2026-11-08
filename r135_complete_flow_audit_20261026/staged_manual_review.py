"""Append actual per-question reviews, defer one whole-corpus admission build.

These records bind manual reasons to the raw question, proposed label and pinned
source. They do not promote the current v2/v3 cohorts or claim model learning.
"""
import copy,json,time
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import digest,file_sha,source_identity,CRITERIA
from app.knowledge.common.domain_flow.understanding import parse
W=R/'training_review_workbench_1793037663397671000';BASE=W/'review_round_012';O=W/'expedited_staged_reviews_20261027'

def read(p):return json.loads(p.read_text('utf8'))
def stage_batch(notes,source_ids,edits,source_issues,quarantines=None):
 quarantines=quarantines or {};assert set(notes)==set(source_ids) and set(edits)<=set(notes) and set(source_issues)<=set(notes)
 source=read(W/'SOURCE_SNAPSHOT.json');identity=digest(source_identity(source));examples=[json.loads(x) for x in (BASE/'EXAMPLES.jsonl').read_text('utf8').splitlines()];lookup={x['annotation_provenance']['historical_review_ref']['line']-1:(line,x) for line,x in enumerate(examples,1)};O.mkdir(exist_ok=True);created=0
 base_sha=file_sha(BASE/'EXAMPLES.jsonl');source_sha=file_sha(W/'SOURCE_SNAPSHOT.json')
 for row,reasons in notes.items():
  assert 225<=row<=288 and len(reasons)==7 and all(isinstance(s,str) and s for s in reasons)
  line,x=lookup[row];label=copy.deepcopy(x['plan_label'])
  if row in edits:edits[row](label)
  wire=parse(json.dumps(label,ensure_ascii=False),x['raw_question']);assert wire.accepted,(row,wire.reason)
  ids=source_ids[row];assert all(rid in source['release']['records'] for rid in ids)
  record={'state':'individual_manual_review_staged_not_admitted','original_row':row,'question_key':x['question_key'],'raw_question':x['raw_question'],'prior_label':x['plan_label'],'reviewed_label':label,'notes':dict(zip(CRITERIA,reasons)),'decision':'quarantined' if row in quarantines else 'accepted' if label==x['plan_label'] else 'corrected','source_record_ids':ids,'source_answer_issues':source_issues.get(row,[]),'quarantine_reason':quarantines.get(row),'base_example_ref':{'path':str((BASE/'EXAMPLES.jsonl').resolve()),'line':line,'sha256':base_sha},'source_snapshot_ref':{'path':str((W/'SOURCE_SNAPSHOT.json').resolve()),'sha256':source_sha},'source_identity_sha256':identity,'source_field_evidence':{rid:{'revision':source['release']['records'][rid]['revision'],'record_sha256':digest(source['release']['records'][rid])} for rid in ids},'reviewer':{'id':'Codex-primary-agent-R135-source-adjudication','kind':'agent'},'wire_shape_pass_is_not_semantic_proof':True,'review_scope':'Individual language-plan/source-purpose review; admission/cohort compilation, answer/model acceptance and final requirement coverage remain pending.'}
  path=O/('STAGED_'+str(row)+'.json')
  if path.exists():assert read(path)==record,'staged_review_is_append_only'
  else:
   with path.open('x',encoding='utf8') as f:json.dump(record,f,ensure_ascii=False,indent=2);f.write('\n')
   created+=1
 records=[read(p) for p in sorted(O.glob('STAGED_*.json'))];assert len({r['original_row'] for r in records})==len(records)
 summary={'base_compiled_manual_round':BASE.name,'base_compiled_unique_reviews':225,'staged_individual_reviews':len(records),'new_staged_reviews_this_batch':created,'unique_original_questions_read_including_staged':225+len(records),'remaining_original_questions_not_individually_reviewed':64-len(records),'staged_rows':[r['original_row'] for r in records],'staged_decisions':{name:sum(r['decision']==name for r in records) for name in ['accepted','corrected','quarantined']},'current_v2_admission_unique_review_count':225,'current_v2_eligible':223,'current_v3_eligible':224,'staged_reviews_admitted_to_current_cohorts':False,'single_final_corpus_compile_pending':True,'training_ready':False,'actual_optimizer_or_model_inferences':0,'complete':False}
 (O/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(O),**summary}))
