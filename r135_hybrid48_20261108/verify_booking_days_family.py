import copy,json,time
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import Artifacts,file_sha
from app.knowledge.common.domain_flow.semantic_family_plan import apply_reviewed_family_moves
w=R/'training_review_workbench_1793037663397671000';s=w/'family_cohort_candidate_1793167167952209900/EXAMPLES.jsonl';p=w/'semantic_amendments_round014/FAMILY_BOOKING_DAYS_137_280.json';xs=[json.loads(t) for t in s.read_text('utf8').splitlines()];g=json.loads(p.read_text('utf8'));out=R/('booking_days_family_controls_'+str(time.time_ns()));out.mkdir(); ref=lambda z:{'path':str(z.resolve()),'sha256':file_sha(z)}
def run(data,group):return apply_reviewed_family_moves(data,[ref(group)],Artifacts(R.parent))
checks={};details={}
try:
 changed,moves=run(xs,p);checks['only_137_train_to_development']=len(moves)==1 and moves[0]['question_key']==next(m['question_key'] for m in g['members'] if m['original_row']==137) and moves[0]['from']=='train' and moves[0]['to']=='development';details['moves']=moves
except Exception as e:checks['only_137_train_to_development']=False;details['positive_error']=repr(e)
for name,mutation in [('forged_review',lambda x:x['members'][0]['review_ref'].__setitem__('sha256','0'*64)),('train_destination',lambda x:x['members'][0].__setitem__('proposed_split','train')),('other_valid_review',lambda x:x['members'][0].__setitem__('review_ref',copy.deepcopy(x['members'][1]['review_ref'])))]:
 a=copy.deepcopy(g);mutation(a);f=out/(name+'.json');f.write_text(json.dumps(a,ensure_ascii=False),encoding='utf8')
 try:run(xs,f);checks[name+'_rejected']=False
 except (ValueError,KeyError,TypeError):checks[name+'_rejected']=True
report={'checks':checks,'all_passed':all(checks.values()),'details':details,'cohort_written':False,'family_audit_complete':False,'optimizer_authorized':False};(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'path':str(out),**report},ensure_ascii=False));assert report['all_passed']
