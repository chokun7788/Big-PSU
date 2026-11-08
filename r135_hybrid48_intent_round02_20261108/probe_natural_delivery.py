"""New natural compound/platform observations; isolated DB, no model calls."""
import json,os,sqlite3,sys,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
out=R/('natural_delivery_'+str(time.time_ns()));out.mkdir()
source=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
copy=sqlite3.connect(out/'copy.sqlite');source.backup(copy);copy.close();source.close()
os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'sessions.sqlite')
answerer=CommonAnswerer(DraftSnapshotView(CommonStore(out/'copy.sqlite')))
questions=['บุคคลทั่วไป เล่น Cockpit 2 ชั่วโมง เสียกี่บาท แล้วจองยังงไ',
           'Tekken 8 ปุ่มอะไร แล้ว PC ราคาเท่าไหร่',
           'Monster Hunter Rise ใช้จอยยังไง',
           'Monster Hunter Rise Nintendo Switch ใช้จอยยังไง',
           'Monster Hunter Rise PS5 ใช้จอยยังไง',
           'Monster Hunter Rise ใช้จอยหรือคีย์บอร์ดยังไง']
focused='--compound-only' in sys.argv
if focused:questions=[questions[0],'How much does a General Adult pay for Cockpit for 2 hours and how do I book?']
rows=[]
for question in questions:
    with patch('urllib.request.urlopen',side_effect=AssertionError('model/provider HTTP forbidden')):
        result=answerer.answer(question,locale='auto',at='2026-11-08T12:00:00+07:00',planner=None)
    artifact=result.decision_artifact
    row={'question':question,'answer':result.answer,'artifact':artifact};rows.append(row)
    flow=artifact.get('domain_flow',{})
    print(json.dumps({'question':question,'answer':result.answer,'claims':[(c.get('category'),c.get('facet'),c.get('record_id')) for c in flow.get('typed_claims',[])],'terminal':artifact.get('terminal_state')},ensure_ascii=False),flush=True)
(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'output':str(out),'observations':len(rows),'model_calls':0,'acceptance':False}))
if focused:
    checks={}
    for number,row in enumerate(rows):
        artifact=row['artifact'];contract=artifact['execution_contract'];constraints=contract['verifier_result']['constraint_coverage']['constraints']
        checks[str(number)+'_both_tasks_planned']={t['category'] for t in contract['request_plan']['tasks']}=={'C06','C08'}
        checks[str(number)+'_price_and_booking_claims']=any(c.get('facet')=='amount' for c in artifact['domain_flow'].get('typed_claims',[])) and any(c.get('facet')=='owner_policy' for c in artifact['domain_flow'].get('typed_claims',[]))
        checks[str(number)+'_duration_source_proven']=any(c['kind']=='duration' and c['status']=='structurally_supported' for c in constraints)
        checks[str(number)+'_no_false_duration_notice']='ยังยืนยันการใช้เงื่อนไขต่อไปนี้' not in row['answer'] and 'Application of these requested constraints remains unverified' not in row['answer']
        checks[str(number)+'_validity_stays_unconfirmed']=('ยังไม่ยืนยันวันเริ่ม' in row['answer'] if number==0 else 'no new effective interval was established' in row['answer'].lower())
    report={'all_passed':all(checks.values()),'checks':checks,'model_calls':0,'scope':'natural source-only TH/EN compound response, not model or publication acceptance'}
    (out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');print(json.dumps(report),flush=True)
    assert report['all_passed']
