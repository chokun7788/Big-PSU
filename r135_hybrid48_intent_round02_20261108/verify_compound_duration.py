"""Replay source-backed compound receipt and direct mutations, no inference."""
import copy,json,time
from verification_support import R
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.request_verifier import verify
sample=json.loads((R/'natural_delivery_1794131016058503200/DETAILS.json').read_text('utf8'))[0]
question=sample['question'];base=sample['artifact']['execution_contract']
idx=Engine.from_snapshot(DraftSnapshotView(CommonStore(R/'natural_delivery_1794131016058503200/copy.sqlite')).snapshot()).index
def proven(contract):
    result=verify(idx,question,contract)
    return result['constraint_coverage']['constraints'][0]['status']=='structurally_supported'
checks={'actual_two_hour_price_and_booking_duration_proven':proven(base)}
for name,mutate in [
    ('forged_total_rejected',lambda c:c['executor_results'][0]['calculation_receipts'][0].__setitem__('total_thb',9999)),
    ('forged_claim_amount_rejected',lambda c:c['executor_results'][0]['claims'][0].__setitem__('numeric',9999)),
    ('forged_duration_rejected',lambda c:c['executor_results'][0]['calculation_receipts'][0]['unit_calculation'].__setitem__('requested_minutes',999)),
    ('wrong_source_revision_rejected',lambda c:c['tasks'][0]['receipts'][0].__setitem__('record_revision',9999)),
    ('unscoped_receipt_rejected',lambda c:c['tasks'][0]['receipts'][0]['requested_scope'].__setitem__('verified',False)),
    ('missing_duration_source_rejected',lambda c:c['tasks'][0]['receipts'][0].__setitem__('evidence_refs',[r for r in c['tasks'][0]['receipts'][0]['evidence_refs'] if not r.get('locator','').endswith('/duration_minutes')])),
    ('wrong_task_category_rejected',lambda c:c['request_plan']['tasks'][0].__setitem__('category','C08')),
    ('rejected_executor_not_duration_proof',lambda c:c['executor_results'][0].__setitem__('status','rejected')),
    ('stale_snapshot_rejected',lambda c:c['request_plan']['snapshot'].__setitem__('epoch',-1)),
    ('missing_calculation_rule_evidence_rejected',lambda c:c['tasks'][0]['receipts'][0].__setitem__('evidence_refs',[r for r in c['tasks'][0]['receipts'][0]['evidence_refs'] if not r.get('locator','').endswith('/calculation_rule')])),
]:
    changed=copy.deepcopy(base);mutate(changed);checks[name]=not proven(changed)
out=R/('compound_duration_'+str(time.time_ns()));out.mkdir()
report={'checks':checks,'all_passed':all(checks.values()),'model_calls':0,'scope':'source-only duration receipt replay, not authority or whole-question semantic acceptance'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');print(json.dumps({'output':str(out),**report}),flush=True)
assert report['all_passed']
