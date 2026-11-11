"""All delivered alternative lines must pass; no model or owner mutations."""
import copy,json,time
from verification_support import R
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.calculation_check import duration_proofs
source=R/'alternative_duration_1794418323335976700/DETAILS.json'
sample=json.loads(source.read_text(encoding='utf8'))[0];base=sample['artifact']['execution_contract']
view=MigratedView(R/'system/data/knowledge/verified_sources.sqlite');index=Engine.from_snapshot(view.snapshot(),cache_key=view.path.resolve()).index
def proof(c):return duration_proofs(index,c['request_plan']['tasks'][0],c['executor_results'][0],c['tasks'][0],c['request_plan']['snapshot'],30)
normal=proof(base);checks={'all_two_alternatives_proven':len(normal)==2,'not_a_combined_total':bool(normal) and all(p['combined_purchase_proven'] is False for p in normal)}
mutations=[
 ('second_amount_forged',lambda c:c['executor_results'][0]['claims'][1].__setitem__('numeric',999)),
 ('second_total_forged',lambda c:c['executor_results'][0]['calculation_receipts'][1].__setitem__('total_thb',999)),
 ('second_duration_forged',lambda c:c['executor_results'][0]['calculation_receipts'][1]['unit_calculation'].__setitem__('requested_minutes',60)),
 ('second_quantity_forged',lambda c:c['executor_results'][0]['calculation_receipts'][1].__setitem__('billing_quantity',2)),
 ('second_revision_forged',lambda c:c['tasks'][0]['receipts'][1].__setitem__('record_revision',999)),
 ('second_scope_unverified',lambda c:c['tasks'][0]['receipts'][1]['requested_scope'].__setitem__('verified',False)),
 ('second_refs_missing',lambda c:c['tasks'][0]['receipts'][1].__setitem__('evidence_refs',[])),
 ('second_calculation_missing',lambda c:c['executor_results'][0]['calculation_receipts'].pop()),
 ('duplicate_calculation',lambda c:c['executor_results'][0]['calculation_receipts'].__setitem__(1,copy.deepcopy(c['executor_results'][0]['calculation_receipts'][0]))),
 ('extra_claim_no_calculation',lambda c:c['executor_results'][0]['claims'].append(copy.deepcopy(c['executor_results'][0]['claims'][0]))),
 ('wrong_audience',lambda c:c['request_plan']['tasks'][0]['source_span'].__setitem__('text','บุคคลทั่วไป เล่น PC 30 นาที เสียกี่บาท')),
 ('wrong_service',lambda c:c['request_plan']['tasks'][0]['source_span'].__setitem__('text','นักศึกษา PSU เล่น VR 30 นาที เสียกี่บาท')),
 ('total_requested_not_alternatives',lambda c:c['request_plan']['tasks'][0]['source_span'].__setitem__('text','นักศึกษา PSU เล่น PC 30 นาที ราคารวมเท่าไหร่')),
 ('multi_person_total_unsupported',lambda c:c['request_plan']['tasks'][0]['source_span'].__setitem__('text','นักศึกษา PSU 2 คน เล่น PC 30 นาที เสียกี่บาท')),
 ('repeated_duration_ambiguous',lambda c:c['request_plan']['tasks'][0]['source_span'].__setitem__('text','นักศึกษา PSU เล่น PC 30 นาที 60 นาที เสียกี่บาท')),
 ('stale_snapshot',lambda c:c['request_plan']['snapshot'].__setitem__('epoch',-1)),
 ('rejected_executor',lambda c:c['executor_results'][0].__setitem__('status','rejected')),
 ('fatal_receipt',lambda c:c['tasks'][0].__setitem__('fatal',['source_receipt_verification_failed']))]
for name,change in mutations:
 c=copy.deepcopy(base);change(c);checks[name]=not proof(c)
out=R/('alternative_duration_controls_'+str(time.time_ns()));out.mkdir();report={'all_passed':all(checks.values()),'checks':checks,'scope':'saved natural source-backed contract replay, all-lines proof and forced negative controls; no model, authority or full semantic proof'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
