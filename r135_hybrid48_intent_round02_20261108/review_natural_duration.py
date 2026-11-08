"""Review saved TH/EN natural deliveries against current source verifier.

The first English assertion used a different caveat phrase; preserve that
failure and inspect the actual rendered owner-validity sentence here.
"""
import json
from verification_support import R
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.request_verifier import verify
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
folder=R/'natural_delivery_1794131357810259200'
rows=json.loads((folder/'DETAILS.json').read_text('utf8'))
idx=Engine.from_snapshot(DraftSnapshotView(CommonStore(folder/'copy.sqlite')).snapshot()).index
checks={}
for number,row in enumerate(rows):
    contract=row['artifact']['execution_contract'];claims=row['artifact']['domain_flow']['typed_claims']
    reviewed=verify(idx,row['question'],contract,row['answer'])
    checks[str(number)+'_price_and_booking_preserved']={t['category'] for t in contract['request_plan']['tasks']}=={'C06','C08'} and any(c.get('facet')=='amount' and c.get('numeric')==400 for c in claims) and any(c.get('facet')=='owner_policy' for c in claims)
    checks[str(number)+'_duration_final_source_guard_passes']=any(c['kind']=='duration' and c['status']=='structurally_supported' for c in reviewed['constraint_coverage']['constraints'])
    checks[str(number)+'_false_notice_absent']='ยังยืนยันการใช้เงื่อนไขต่อไปนี้' not in row['answer'] and 'Application of these requested constraints remains unverified' not in row['answer']
    checks[str(number)+'_validity_caveat_retained']=('ยังไม่ยืนยันวันเริ่ม' in row['answer'] if number==0 else 'no new effective interval was established' in row['answer'].lower())
    checks[str(number)+'_raw_spans_preserved']=all(row['question'][t['source_span']['start']:t['source_span']['end']]==t['source_span']['text'] for t in contract['request_plan']['tasks'])
report={'all_passed':all(checks.values()),'checks':checks,'saved_observations':str(folder),'model_calls':0,'whole_question_semantics_verified':False,'initial_english_caveat_assertion_failed_and_preserved':True}
(R/'NATURAL_DURATION_REVIEW.json').write_text(json.dumps(report,indent=2),'utf8');print(json.dumps(report),flush=True)
assert report['all_passed']
