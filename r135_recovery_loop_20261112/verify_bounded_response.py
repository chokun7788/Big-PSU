import json,os,time,types,urllib.request
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.flow_context import request_context
from app.knowledge.common.bounded_time import timeout,remaining
from app.knowledge.common.domain_flow.model_gateway import call,legacy_open,ModelBudgetExhausted
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.store import CommonStore
out=R/('bounded_response_'+str(time.time_ns()));out.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'sessions.sqlite');checks={}
with request_context() as ctx:
 checks['long_model_call_capped']=0<timeout(60)<=5
 ctx.started=time.perf_counter()-21
 checks['expired_budget_zero']=remaining()==0 and timeout(60)==0
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP forbidden')),patch('app.pipeline.llm_health.llm_call_allowed',side_effect=AssertionError('must reject before admission')):
  try:call(types.SimpleNamespace(timeout=60,model='fixture'),{'messages':[]})
  except ModelBudgetExhausted:checks['expired_gateway_skips_admission']=True
  try:legacy_open(urllib.request.Request('http://127.0.0.1/',data=json.dumps({'model':'fixture'}).encode()))
  except ModelBudgetExhausted:checks['expired_legacy_skips_admission']=True
with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP forbidden')),patch.dict(os.environ,{'PSU_ANALYSIS_BUDGET_SEC':'0'}):
 result=CommonAnswerer(DraftSnapshotView(CommonStore(R/'system/data/knowledge/common.sqlite'))).answer('บุคคลทั่วไป เล่น Cockpit 2 ชั่วโมง เสียกี่บาท แล้วจองยังงไ',locale='th',at='2026-11-08T12:00:00+07:00',planner=None)
 claims=result.decision_artifact.get('domain_flow',{}).get('typed_claims',[])
 checks['typed_price_still_delivered']=any(c.get('facet')=='amount' and c.get('numeric')==400 for c in claims)
 checks['typed_booking_still_delivered']=any(c.get('facet')=='owner_policy' for c in claims)
report={'checks':checks,'all_passed':len(checks)==6 and all(checks.values()),'scope':'fake clock/admission and source-only natural response; no live inference or hard deadline proof'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps({'answer':result.answer,'artifact':result.decision_artifact},ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}),flush=True);assert report['all_passed']
