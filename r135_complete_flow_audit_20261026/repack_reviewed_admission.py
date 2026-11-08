"""Repack unchanged reviewed semantics for current exact inference contracts.

No adjudication is manufactured; reviewer hashes remain bound to input/labels.
Every unreviewed proposal stays blocked and historical files stay immutable.
"""
import argparse,json,time,subprocess,sys
from pathlib import Path
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import *
W=R/'training_review_workbench_1793037663397671000'
parser=argparse.ArgumentParser();parser.add_argument('--round',default='review_round_012');args=parser.parse_args()
S=(W/args.round).resolve();assert S.parent==W.resolve() and S.name.startswith('review_round_'),'manual_round_must_be_in_workbench'
O=W/('current_admission_'+str(time.time_ns()));O.mkdir()
def read(p):return json.loads(p.read_text('utf8'))
def rows(p):return [json.loads(line) for line in p.read_text('utf8').splitlines() if line.strip()]
def write(name,value):(O/name).write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in value) if name.endswith('.jsonl') else json.dumps(value,ensure_ascii=False,indent=2)+'\n','utf8')
examples=rows(S/'EXAMPLES.jsonl');reviews=rows(S/'REVIEWS.jsonl');review_index={r['question_key']:r for r in reviews};tokenizer=Path('D:/CodexTraining/psu-r121-20261022/model/tokenizer_config.json');runtime=runtime_contract(read(tokenizer),chat_template=tokenizer.with_name('chat_template.jinja').read_text('utf8'),model_profile=read(W/'DECLARED_MODEL_PROFILE.json'));artifacts=Artifacts(R.parent);artifacts._cache={};source_ref=read(W/'SOURCE_REF.json')
for example in examples:
 origin=Path(example['annotation_provenance']['origin_ref']['path']);final_split=origin.stem if origin.stem in {'train','validation','test'} else None
 example['split']='train' if final_split=='train' else 'development';example['annotation_provenance']['final_saved_split_file']=final_split
 review=review_index.get(example['question_key'])
 if review and review['adjudication_status'] in {'accepted','corrected'}:
  effective=planner_question(example,artifacts.read(example['annotation_provenance']['origin_ref']),artifacts,source_ref)
  before=example_sha(example);example['annotation_provenance']['runtime_contract_sha256']=digest(runtime);example['messages']=messages(effective)+[{'role':'assistant','content':json.dumps(example['plan_label'],ensure_ascii=False,separators=(',',':'))}];assert example_sha(example)==before==review['example_sha256']
artifacts.verify_pinned_files()
write('EXAMPLES.jsonl',examples);write('REVIEWS.jsonl',reviews);write('RUNTIME_CONTRACT.json',runtime)
command=[sys.executable,str(R/'system/tools/prepare_reviewed_planner_dataset.py'),'--examples',str(O/'EXAMPLES.jsonl'),'--reviews',str(O/'REVIEWS.jsonl'),'--inventory',str(W/'INVENTORY.json'),'--source-ref',str(W/'SOURCE_REF.json'),'--tokenizer-config',str(tokenizer),'--model-profile',str(W/'DECLARED_MODEL_PROFILE.json'),'--artifact-root',str(R.parent),'--output',str(O/'bundle')]
r=subprocess.run(command,capture_output=True,text=True,encoding='utf8');write('PROCESS.json',{'command':command,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr});assert r.returncode in {0,2},r.stderr
report=read(O/'bundle/ADMISSION.json');eligible=[r for r in report['rows'] if r['eligible']];quarantined=sum(r['adjudication_status']=='quarantined' for r in reviews);assert len(eligible)==len(reviews)-quarantined and sum(r['inventory_adjudicated'] for r in report['rows'])==len(reviews) and report['ready_for_optimization']==(r.returncode==0)==(O/'bundle/READY_FOR_OPTIMIZATION.json').exists(),[r for r in report['rows'] if r.get('adjudication_status') and not r['inventory_adjudicated']]
summary={'manual_round':S.name,'current_runtime_contract_sha256':digest(runtime),'source_identity_sha256':report['source_identity_sha256'],'rows':len(examples),'individually_reviewed':len(reviews),'eligible_reviewed_rows':len(eligible),'quarantined':quarantined,'unreviewed':len(examples)-len(reviews),'eligible_split_counts':report['eligible_split_counts'],'training_ready':report['ready_for_optimization'],'optimizer_started':False,'semantic_adjudications_changed':0,'all_original_labels_semantically_reviewed':False,'all_original_questions_individually_reviewed':len(reviews)==len(examples),'base_protocol_and_evaluation_admission_proven':False};write('SUMMARY.json',summary);print(json.dumps({'output':str(O),**summary}))
