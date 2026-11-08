"""Create immutable proposed review round incorporating the individual row 266 amendment."""
import copy,json,time
from pathlib import Path
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import Artifacts,admit,digest,example_sha,file_sha
W=R/'training_review_workbench_1793037663397671000'; S=W/'review_round_013'; A=W/'amendment_266_adjudication_1793132277637482000'
read=lambda p:json.loads(p.read_text(encoding='utf8'))
rows=lambda p:[json.loads(s) for s in p.read_text(encoding='utf8').splitlines() if s.strip()]
inputs=[S/'EXAMPLES.jsonl',S/'REVIEWS.jsonl',A/'EXAMPLE_266.json',A/'REVIEW_266.json',A/'RESULT.json',A/'RUNTIME_CONTRACT.json',W/'SOURCE_REF.json']
pins={str(p):file_sha(p) for p in inputs}
assert read(A/'RESULT.json')['all_passed']
examples=rows(inputs[0]); reviews=rows(inputs[1]); amended=read(inputs[2]); review=read(inputs[3]); key=amended['question_key']
assert len(examples)==289 and len(reviews)==289
indices=[i for i,x in enumerate(examples) if x['question_key']==key]; ri=[i for i,x in enumerate(reviews) if x['question_key']==key]
assert len(indices)==len(ri)==1 and examples[indices[0]]['annotation_provenance']['historical_review_ref']['line']-1==266
old=examples[indices[0]]; assert old['raw_question']==amended['raw_question'] and old['family']==amended['family'] and old['original_families']==amended['original_families'] and old['exposure']==amended['exposure'] and old['annotation_provenance']['origin_ref']==amended['annotation_provenance']['origin_ref']
art=Artifacts(R.parent); decision=admit(amended,review,art,read(W/'SOURCE_REF.json'),read(A/'RUNTIME_CONTRACT.json'));assert decision['eligible'],decision
assert not admit(amended,reviews[ri[0]],art,read(W/'SOURCE_REF.json'),read(A/'RUNTIME_CONTRACT.json'))['eligible']
examples[indices[0]]=amended; reviews[ri[0]]=review
O=W/('review_round_014_candidate_'+str(time.time_ns()));O.mkdir()
for name,content in [('EXAMPLES.jsonl',examples),('REVIEWS.jsonl',reviews)]:
 (O/name).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in content),encoding='utf8')
assert all(file_sha(Path(p))==h for p,h in pins.items())
manifest={'prior_round':str(S),'amendment':str(A),'input_sha256':pins,'changed_original_rows':[266],'prior_example_sha256':example_sha(old),'amended_example_sha256':example_sha(amended),'unique_questions':len(examples),'unique_new_reviews':0,'admission_decision':decision,'full_family_review_complete':False,'optimizer_authorized':False,'historical_inputs_unchanged':True}
(O/'STAGING_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'round':O.name,'path':str(O),'amendment_accepted':decision['eligible'],'unique_new_reviews':0,'optimizer_authorized':False},ensure_ascii=False))
