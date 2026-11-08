import json,os,time
from unittest.mock import patch
from verification_support import R,snapshot
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.native_intents import propose
from app.knowledge.common.domain_flow.routing import split_needs
from app.knowledge.common.domain_flow.requested_output import device,allows
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
out=R/('intent_output_'+str(time.time_ns()));out.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'sessions.sqlite');e=Engine.from_snapshot(snapshot());checks={};details=[]
for name,q,expected in [('headset','ขอสอบถามหน่อยครับ Pulse Elite Wireless Headset ใช้งานยังไง','equipment_pulse_elite_headset'),('wheel','How do I use the Logitech G923 TRUEFORCE Racing Wheel','equipment_logitech_g923')]:
 u=propose(e.index,q);checks[name+'_usage_intent']=u is not None and len(u.tasks)==1 and u.tasks[0].facet=='usage'
 with patch('urllib.request.urlopen',side_effect=AssertionError('no inference')):a=CommonAnswerer(DraftSnapshotView(CommonStore(R/'system/data/knowledge/common.sqlite'))).answer(q,locale='auto',at='2026-11-08T12:00:00+07:00',planner=None)
 claims=a.decision_artifact.get('domain_flow',{}).get('typed_claims',[])
 checks[name+'_actual_usage_not_specs']=bool(claims) and all(c['facet']=='usage' for c in claims)
 details.append({'question':q,'answer':a.answer,'artifact':a.decision_artifact})
q='PUBG: BATTLEGROUNDS ใช้จอยยังไง';facts=e.index.bind('C05',q)
checks['controller_request_recognised']=device(e.index,q)=='controller'
checks['unknown_device_cannot_prove_gamepad']=bool(facts) and all(not allows(e.index,q,f) for f in facts)
checks['no_device_constraint_preserves_generic_bindings']=bool(facts) and all(allows(e.index,'PUBG: BATTLEGROUNDS มีปุ่มอะไรบ้าง',f) for f in facts)
checks['two_distinct_compound_needs']=len(split_needs('Tekken 8 ปุ่มอะไร แล้ว PC ราคาเทาไหร่',e.index))==2
checks['coordinated_objects_not_two_tasks']=len(split_needs('มีเมาส์และคีย์บอร์ดไหม',e.index))==1
checks['unknown_equipment_not_forced_to_usage']=propose(e.index,'How do I use Unknown Amber Device') is None
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
query='PUBG: BATTLEGROUNDS มีปุ่มอะไรบ้าง';u=Understanding([MeaningTask(query,'game_controls','C05','list','input_bindings')],True,'controlled',{'model_called':False})
base=e.answer(query,'th',at='2026-11-08T12:00:00+07:00',allow_llm=False,understanding=u)
checks['positive_generic_control_still_delivered']=bool(base['claims'])
query='PUBG: BATTLEGROUNDS ใช้จอยยังไง';u2=Understanding([MeaningTask(query,'game_controls','C05','list','input_bindings')],True,'controlled',{'model_called':False})
task=compile_request(query,u2,e.index,base['execution_contract']['request_plan']['snapshot']).tasks[0]
checks['forced_wrong_device_claim_rejected']=bool(assess(e.index,task,base['needs'][0],base['execution_contract']['request_plan']['snapshot'],query)['fatal'])
query='บุคคลทั่วไป เล่น Cockpit 2 ชั่วโมง เสียกี่บาท แล้วจองยังงไ';u3=propose(e.index,query)
checks['booking_typo_retains_two_needs']=u3 is not None and {t.category for t in u3.tasks}=={'C06','C08'}
report={'all_passed':all(checks.values()),'checks':checks,'source_only':True,'new_full_evaluation_started':False}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
