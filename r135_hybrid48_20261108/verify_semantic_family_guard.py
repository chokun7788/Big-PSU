"""Recheck staged actual family identities without altering admitted datasets."""
import copy,json,time
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import digest,file_sha
from app.knowledge.common.domain_flow.training_optimizer import verify_semantic_families
w=R/'training_review_workbench_1793037663397671000'; source=w/'protocol_v3_admission_1793109982985437000/EXAMPLES.jsonl'
by={x['question_key']:x for x in map(json.loads,source.read_text('utf8').splitlines())}; groups=[]; examples=[]
for name in ['FAMILY_PSU_PRICE_BOOKING_104_133_134_135.json','FAMILY_EN_PRICE_BOOKING_141_282.json']:
 d=json.loads((w/'semantic_amendments_round014'/name).read_text('utf8'));members=d['members'];keys=[m['question_key'] for m in members]
 for m in members:
  e=copy.deepcopy(by[m['question_key']]);assert e['family']==m['original_family'];e['split']='development';examples.append(e)
 groups.append({'semantic_family':d['family_id'],'question_keys':keys,'original_family_by_key':{m['question_key']:m['original_family'] for m in members},'reason':d['semantic_rationale']})
keys=[e['question_key'] for e in examples]; review={'version':'r135-semantic-family-review-v2','inventory_sha256':digest(sorted(keys)),'groups':groups};checks={}
def check(name,rev,ex,expected):
 try:verify_semantic_families(rev,ex,keys);ok=True
 except (ValueError,KeyError,TypeError):ok=False
 checks[name]=ok==expected
check('actual_groups_preserve_original_identities',review,examples,True)
x=copy.deepcopy(examples);x[0]['split']='train';check('cross_split',review,x,False)
x=copy.deepcopy(review);x['groups'][0]['original_family_by_key'][keys[0]]='forged';check('forged_family',x,examples,False)
x=copy.deepcopy(review);x['groups'][0]['question_keys'].pop();check('missing_member',x,examples,False)
x=copy.deepcopy(review);x['groups'][0]['question_keys'].append(keys[0]);check('duplicate_member',x,examples,False)
x=copy.deepcopy(review);x['groups'][0]['semantic_family']='';check('unnamed_group',x,examples,False)
x=copy.deepcopy(review);x['groups'][0]['reason']='';check('missing_reason',x,examples,False)
x=copy.deepcopy(review);x['inventory_sha256']='0'*64;check('wrong_inventory',x,examples,False)
x=copy.deepcopy(examples);x[0]['family']='changed';check('changed_identity',review,x,False)
x=copy.deepcopy(review);x['groups'][0]['original_family_by_key']['unknown']='x';check('extra_mapping',x,examples,False)
out=R/('semantic_family_guard_controls_'+str(time.time_ns()));out.mkdir();result={'checks':checks,'all_passed':all(checks.values()),'source_sha256':file_sha(source),'scope':'six actual staged members with simulated development splits only','cohort_changed':False,'optimizer_started':False,'full_review':False};(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n','utf8');print(json.dumps({'path':str(out),'passed':result['all_passed'],'count':len(checks)}));assert result['all_passed']
