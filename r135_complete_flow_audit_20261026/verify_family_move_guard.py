"""Artifact-bound split planning controls; never writes an admitted cohort."""
import copy,json,time
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import Artifacts,file_sha
from app.knowledge.common.domain_flow.semantic_family_plan import apply_reviewed_family_moves
w=R/'training_review_workbench_1793037663397671000';source=w/'protocol_v3_admission_1793109982985437000/EXAMPLES.jsonl';xs=[json.loads(t) for t in source.read_text('utf8').splitlines()];d=w/'semantic_amendments_round014';paths=[d/'FAMILY_PSU_PRICE_BOOKING_104_133_134_135.json',d/'FAMILY_EN_PRICE_BOOKING_141_282.json'];groups=[json.loads(p.read_text('utf8')) for p in paths];out=R/('family_move_guard_controls_'+str(time.time_ns()));out.mkdir();checks={}
def ref(p):return {'path':str(p.resolve()),'sha256':file_sha(p)}
refs=list(map(ref,paths));old=file_sha(source)
def run(data=xs,rs=refs):return apply_reviewed_family_moves(data,rs,Artifacts(R.parent))
changed,moves=run(); checks['four_train_to_dev_only']=len(moves)==4 and all(m['from']=='train' and m['to']=='development' and m['saved_split']=='train' for m in moves);checks['input_and_source_unchanged']=file_sha(source)==old and all(a['split']==b['split'] or (a['split']=='train' and b['split']=='development') for a,b in zip(xs,changed))
def reject(name,data,rs):
 try:run(data,rs);checks[name]=False
 except (ValueError,KeyError,TypeError):checks[name]=True
def changedref(name,value):
 p=out/(name+'.json');p.write_text(json.dumps(value,ensure_ascii=False),'utf8');return ref(p)
a=copy.deepcopy(groups[0]);a['members'][0]['proposed_split']='train';reject('proposed_train_rejected',xs,[changedref('train',a)])
a=copy.deepcopy(groups[0]);a['members'][0]['original_family']='forged';reject('identity_forgery_rejected',xs,[changedref('family',a)])
a=copy.deepcopy(groups[0]);a['members'][0]['review_ref']['sha256']='0'*64;reject('changed_review_rejected',xs,[changedref('review',a)])
a=copy.deepcopy(groups[0]);a['members'].append(copy.deepcopy(a['members'][0]));reject('duplicate_member_rejected',xs,[changedref('duplicate',a)])
a=copy.deepcopy(xs);key=groups[0]['members'][0]['question_key'];next(x for x in a if x['question_key']==key)['raw_question']+=' altered';reject('changed_question_rejected',a,refs)
a=copy.deepcopy(xs);next(x for x in a if x['question_key']==key)['split']='development';reject('changed_input_split_rejected',a,refs)
a=copy.deepcopy(groups[0]);a['members'][0]['example_ref']['sha256']='0'*64;reject('changed_source_rejected',xs,[changedref('source',a)])
a=copy.deepcopy(groups[0]);a['semantic_rationale']='';reject('missing_rationale_rejected',xs,[changedref('rationale',a)])
a=copy.deepcopy(xs); target=next(x for x in a if x['question_key']==key); target['annotation_provenance']['origin_ref']=copy.deepcopy(next(x for x in xs if __import__('pathlib').Path(x['annotation_provenance']['origin_ref']['path']).stem=='test')['annotation_provenance']['origin_ref']);reject('changed_saved_split_origin_rejected',a,refs)
a=copy.deepcopy(xs);next(x for x in a if x['question_key']==key)['exposure']='unseen';reject('changed_exposure_rejected',a,refs)
r={'checks':checks,'all_passed':all(checks.values()),'input_sha256':old,'moves':moves,'cohort_written':False,'semantic_review_complete':False,'optimizer_started':False};(out/'RESULT.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'path':str(out),'passed':r['all_passed'],'checks':checks}));assert r['all_passed']
