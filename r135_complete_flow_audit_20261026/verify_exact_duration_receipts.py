"""Adversarial replay of actual exact-duration verifier input without model calls."""
import copy,json,time
from verification_support import R,index
from app.knowledge.common.domain_flow.request_verifier import verify
p=R/'exact_rate_duration_controls_1793135127312579700/DETAILS.json';sample=json.loads(p.read_text('utf8'))[0];q=sample['question'].replace('one hour','1 hour');base=sample['artifact']['execution_contract'];idx=index();checks={}
def proven(c):
 result=verify(idx,q,c);return 'exact_single_source_rate_duration_and_scoped_receipt_recomputed' in json.dumps(result)
checks['actual_scoped_receipt_replayed']=proven(base)
x=copy.deepcopy(base);x['tasks'][0]['receipts'][0]['record_revision']+=1;checks['wrong_revision_rejected']=not proven(x)
x=copy.deepcopy(base);x['tasks'][0]['receipts'][0]['requested_scope']['verified']=False;checks['unscoped_receipt_rejected']=not proven(x)
x=copy.deepcopy(base);x['tasks'][0]['receipts'][0]['value_validation']='unverified';checks['unverified_numeric_rejected']=not proven(x)
x=copy.deepcopy(base);x['tasks'][0]['receipts'][0]['evidence_refs']=[e for e in x['tasks'][0]['receipts'][0]['evidence_refs'] if not e['locator'].endswith('/duration_minutes')];checks['missing_duration_evidence_rejected']=not proven(x)
x=copy.deepcopy(base);x['executor_results'][0]['claims'][0]['numeric']+=1;checks['altered_amount_rejected']=not proven(x)
out=R/('exact_duration_receipt_controls_'+str(time.time_ns()));out.mkdir();(out/'RESULT.json').write_text(json.dumps({'checks':checks,'all_passed':all(checks.values()),'actual_model_calls':0,'complete_semantics_proven':False},indent=2)+'\n','utf8');print(json.dumps({'path':str(out),'checks':checks}));assert all(checks.values())
