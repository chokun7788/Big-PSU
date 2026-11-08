"""Pin two source-specific English questions sharing a price/booking frame."""
import json
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import file_sha
W=R/'training_review_workbench_1793037663397671000';A=W/'protocol_v3_admission_1793109982985437000';O=W/'semantic_amendments_round014';O.mkdir(exist_ok=True)
xs=[json.loads(t) for t in (A/'EXAMPLES.jsonl').read_text('utf8').splitlines()];reviews={r['question_key']:r for r in map(json.loads,(A/'REVIEWS.jsonl').read_text('utf8').splitlines())};members=[]
for line,x in enumerate(xs,1):
 row=x['annotation_provenance']['historical_review_ref']['line']-1
 if row not in {141,282}:continue
 q=x['raw_question'];tasks=x['plan_label']['tasks'];r=reviews[x['question_key']]
 assert q.startswith('How much does it cost for ') and ' to play ' in q and 'how do I book' in q
 assert {(t['domain'],t['operation']) for t in tasks}=={('service_fee','price_calculate'),('reservation','detail')} and x['plan_label']['shared_bindings']
 assert r['adjudication_status'] in {'accepted','corrected'} and file_sha(r['adjudication_ref']['path'])==r['adjudication_ref']['sha256']
 members.append({'original_row':row,'question_key':x['question_key'],'question':q,'current_split':x['split'],'proposed_split':'development','original_family':x['family'],'original_families':x['original_families'],'service_target':tasks[0]['target'],'price_audience_quotes':[c['quote'] for c in tasks[0]['constraints'] if c['slot']=='audience'],'price_duration_quotes':[c['quote'] for c in tasks[0]['constraints'] if c['slot']=='duration'],'binding_basis':x['plan_label']['shared_bindings'][0]['basis'],'review_ref':r['adjudication_ref'],'example_ref':{'path':str((A/'EXAMPLES.jsonl').resolve()),'line':line,'sha256':file_sha(A/'EXAMPLES.jsonl')}})
assert {m['original_row'] for m in members}=={141,282} and {m['current_split'] for m in members}=={'train','development'}
assert len({m['service_target'] for m in members})==2 and len({str(m['price_audience_quotes']) for m in members})==2
record={'version':'r135-family-review-v1','state':'manually_identified_conservative_group_staged_not_compiled','family_id':'english_audience_price_and_booking_template_v1','semantic_rationale':'Both questions use the same English price-for-audience/duration/service followed by booking frame, one with an explicit it and one with an ellipsis. Audience, service, duration and source prices differ; they are not identical factual questions. This cross-split frame may inflate generalization to unseen phrasing.','members':members,'split_policy':'Place the current training member in development for the next candidate cohort. Preserve original split files, family labels, exposure and source/review hashes. Never move historical validation or test into training.','new_unique_question_reviews':0,'semantic_labels_changed':False,'current_cohorts_modified':False,'fresh_holdout_claimed':False,'optimizer_authorized':False,'completeness_claim':'This manually inspected pair does not establish complete semantic or cross-language family coverage.'}
p=O/'FAMILY_EN_PRICE_BOOKING_141_282.json'
if p.exists():assert json.loads(p.read_text('utf8'))==record
else:p.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n','utf8')
print(json.dumps({'path':str(p.relative_to(R)),'sha256':file_sha(p),'members':2,'train_to_development_proposed':1,'cohort_changed':False,'complete_family_audit':False}))
