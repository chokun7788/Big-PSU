"""Prepare all289 historical proposals for current individual review.

Historical artifacts remain immutable. No review is invented by this importer.
"""
import json,time,subprocess,sys,hashlib
from pathlib import Path
from verification_support import R,snapshot
from app.knowledge.common.domain_flow.training_contract import source_identity,digest,file_sha,runtime_contract
out=R/('training_review_workbench_'+str(time.time_ns()));out.mkdir();old=R.parent/'r129_full_plan_completion_20261024/training_v2'
def read(p):return json.loads(p.read_text('utf8'))
def rows(p):return [json.loads(line) for line in p.read_text('utf8').splitlines() if line.strip()]
def write(name,v):
 p=out/name;p.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in v) if name.endswith('.jsonl') else json.dumps(v,ensure_ascii=False,indent=2)+'\n','utf8');return p
def ref(p,**kw):return {'path':str(p.resolve()),'sha256':file_sha(p),**kw}
reviews=rows(old/'ANNOTATION_REVIEW.jsonl');original_path=old.parent/'LABELS_REVIEW_INPUT.json';originals=read(original_path);saved={}
for split in ['train','validation','test']:
 p=old/(split+'.jsonl')
 for line,row in enumerate(rows(p),1):saved[row['key']]=(row,ref(p,line=line),split)
source_path=write('SOURCE_SNAPSHOT.json',snapshot());source_ref=ref(source_path);write('SOURCE_REF.json',source_ref);write('SOURCE_IDENTITY.json',source_identity(read(source_path)))
tokenizer=Path('D:/CodexTraining/psu-r121-20261022/model/tokenizer_config.json');profile={'base_repository':'typhoon-ai/typhoon2.5-qwen3-4b','base_revision':'ce0a7416fe82d4404b2b4a253ce3ac095ab1252c','precision':'HF_NF4_doublequant_BF16','selector_profile':'base','generic_profile':'base'};write('DECLARED_MODEL_PROFILE.json',profile)
runtime=runtime_contract(read(tokenizer),chat_template=tokenizer.with_name('chat_template.jinja').read_text('utf8'),model_profile=profile);write('RUNTIME_CONTRACT.json',runtime)
examples=[]
for review in reviews:
 i=review['row'];original=originals[i];prior,origin,final_split=saved.get(review['key'],(original,ref(original_path,pointer='/'+str(i)),None));families=list(dict.fromkeys(str(prior[k]) for k in ['family','review_family'] if prior.get(k)))
 examples.append({'question_key':review['key'],'family':prior.get('review_family') or original['family'],'original_families':families,'split':'train' if final_split=='train' else 'development','raw_question':original['question'],'allowed_context':[],'contract_version':review['reviewed_label']['version'],'plan_label':review['reviewed_label'],'annotation_provenance':{'method':'legacy_unverified_proposal','origin_ref':origin,'historical_review_ref':ref(old/'ANNOTATION_REVIEW.jsonl',line=i+1),'final_saved_split_file':final_split,'runtime_contract_sha256':digest(runtime),'allowed_context_basis':'saved training messages contain current question only; individual review must adjudicate missing context, not invent history'},'messages':prior.get('messages',[]),'exposure':'development'})
assert len(examples)==len({e['question_key'] for e in examples})==289
write('EXAMPLES.jsonl',examples);write('REVIEWS.jsonl',[]);write('INVENTORY.json',{'question_keys':[e['question_key'] for e in examples],'known_exposed_question_keys':[e['question_key'] for e in examples],'fresh_holdout':False,'historical_test_rows_moved_to_development':True,'all_historical_labels_individually_adjudicated':False})
write('IMPORT_RECEIPT.json',{'rows':289,'invented_current_reviews':0,'historical_source_files':{str(p.resolve()):file_sha(p) for p in [original_path,old/'ANNOTATION_REVIEW.jsonl',old/'DATASET_FREEZE.json',*[old/(s+'.jsonl') for s in ['train','validation','test']]]},'source_identity_sha256':digest(source_identity(read(source_path))),'runtime_contract_sha256':digest(runtime),'context_note':'No actual previous dialogue is present in saved training messages; fragments needing history remain unresolved until individual review. This importer does not approve context flattening.','teacher_trace_refs_invented':False,'historical_files_modified':False,'optimizer_started':False})
command=[sys.executable,str(R/'system/tools/prepare_reviewed_planner_dataset.py'),'--examples',str(out/'EXAMPLES.jsonl'),'--reviews',str(out/'REVIEWS.jsonl'),'--inventory',str(out/'INVENTORY.json'),'--source-ref',str(out/'SOURCE_REF.json'),'--tokenizer-config',str(tokenizer),'--model-profile',str(out/'DECLARED_MODEL_PROFILE.json'),'--artifact-root',str(R.parent),'--output',str(out/'initial_blocked_bundle')]
r=subprocess.run(command,capture_output=True,text=True,encoding='utf8');write('INITIAL_ADMISSION_PROCESS.json',{'command':command,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr});assert r.returncode==2,r.stderr
admission=read(out/'initial_blocked_bundle/ADMISSION.json');assert not admission['ready_for_optimization'] and all(not x['eligible'] for x in admission['rows']) and len(admission['rows'])==289
print(json.dumps({'output':str(out),'rows':289,'eligible':0,'unreviewed':289,'training_ready':False,'historical_files_modified':False}))
