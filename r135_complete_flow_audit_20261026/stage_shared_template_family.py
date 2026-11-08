"""Stage a conservative evaluation-family correction after reading four rows.

This does not rewrite a frozen split, alter an admission cohort, or claim the
questions have identical business answers. The proposed development grouping
must be incorporated and verified before the next dataset/protocol freeze.
"""
import json,re,time
from pathlib import Path
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import file_sha,digest
W=R/'training_review_workbench_1793037663397671000';A=W/'protocol_v3_admission_1793109982985437000';O=W/'semantic_amendments_round014';O.mkdir(exist_ok=True)
def rows(p):return [json.loads(x) for x in p.read_text('utf8').splitlines() if x.strip()]
examples=rows(A/'EXAMPLES.jsonl');reviews={r['question_key']:r for r in rows(A/'REVIEWS.jsonl')};pattern=re.compile(r'นักศึกษา PSU เล่น (PC|Nintendo Switch|VR) (30 นาที|2 ชั่วโมง) เสียกี่บาท แล้วจองยังไง')
group=[]
for line,x in enumerate(examples,1):
 q=x['raw_question'];match=pattern.fullmatch(q)
 if not match:continue
 ts=x['plan_label']['tasks'];r=reviews[x['question_key']];assert {t['domain'] for t in ts}=={'service_fee','reservation'} and x['plan_label']['shared_bindings'] and r['adjudication_status'] in {'accepted','corrected'}
 group.append({'original_row':x['annotation_provenance']['historical_review_ref']['line']-1,'question_key':x['question_key'],'question':q,'source_service':match[1],'source_duration':match[2],'original_family':x['family'],'original_families':x['original_families'],'current_split':x['split'],'proposed_split':'development','review_ref':r['adjudication_ref'],'example_ref':{'path':str((A/'EXAMPLES.jsonl').resolve()),'line':line,'sha256':file_sha(A/'EXAMPLES.jsonl')}})
assert {x['original_row'] for x in group}=={104,133,134,135} and {x['current_split'] for x in group}=={'train','development'}
record={'version':'r135-family-review-v1','state':'manually_identified_conservative_group_staged_not_compiled','family_id':'thai_psu_student_price_and_booking_template_v1','semantic_rationale':'All four literal questions share the same Thai request frame, PSU-student audience, price-then-booking operations and anaphoric service continuity; only source service and duration differ. They are not identical factual questions or interchangeable price answers. Keeping the shared frame across training and development risks overstating generalization to novel phrasing.', 'members':group,'split_policy':'Conservatively move this group to development in the next candidate cohort; preserve original saved files, original family labels, historical exposures and all source/label hashes. Never move historical test/validation into training.','new_unique_question_reviews':0,'semantic_labels_changed':False,'current_cohorts_modified':False,'fresh_holdout_claimed':False,'optimizer_authorized':False,'completeness_claim':'This single reviewed family does not establish that all cross-language or semantic families have been found.'}
p=O/'FAMILY_PSU_PRICE_BOOKING_104_133_134_135.json'
if p.exists():assert json.loads(p.read_text('utf8'))==record
else:p.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n','utf8')
print(json.dumps({'path':str(p.relative_to(R)),'sha256':file_sha(p),'actual_members':len(group),'train_to_development_proposed':3,'cohort_changed':False,'whole_family_audit_complete':False}))
