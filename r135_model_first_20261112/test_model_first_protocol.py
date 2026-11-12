"""Mocked transport/source controls; NEVER count these as model capability."""
import json,os,time
from unittest.mock import patch
from verification_support import R
os.environ.update({'PSU_MODEL_FIRST_TRIAL':'1','PSU_CONVERSATION_STATE_PATH':str(R/'protocol_runtime/conversations.sqlite')})
from app.knowledge.common.model_first import parse
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.migrated_view import MigratedView
checks={};q='Tekken 8 อยู่โซนไหน แล้วเครื่องไหนพร้อมให้เล่น Tekken 8 บ้าง'
plan=parse('[["Z",0,2],["R",3,6]]',q)
checks['two_need_exact_raw_spans']=len(plan)==2 and all(q[n['source_span']['start']:n['source_span']['end']]==n['quote'] for n in plan)
for name,content in [('non_json','hello'),('invalid_code','[["FAKE",0,2]]'),('negative_offset','[["Z",-1,2]]'),('out_of_bounds','[["Z",0,999]]'),('duplicate','[["Z",0,2],["Z",0,2]]'),('facts_injected','[["P",0,2,0]]')]:
 try:parse(content,q);checks[name+'_rejected']=False
 except (ValueError,TypeError,KeyError):checks[name+'_rejected']=True
reader=CommonAnswerer(MigratedView(R/'system/data/knowledge/verified_sources.sqlite'));rows=[]
def ask(question,content=None,error=None):
 response={'model':'psu-r129:latest','message':{'content':content}}
 with patch('app.knowledge.common.domain_flow.model_gateway.call',side_effect=error,return_value=response),patch('urllib.request.urlopen',side_effect=AssertionError('No real HTTP in protocol controls')):
  result=reader.answer(question,locale='th',planner=None)
 rows.append({'q':question,'answer':result.answer,'mode':result.mode,'artifact':result.decision_artifact});return result
r=ask(q,'[["Z",0,2],["R",3,6]]');checks['mocked_two_need_source_plus_clarification']='PC Zone' in r.answer and 'หมายถึงเครื่องที่รองรับเกม' in r.answer and 'partial' in r.mode
r=ask(q,error=TimeoutError('synthetic timeout'));checks['timeout_not_silent_native_fallback']='unavailable' in r.mode and not r.hits and 'PC Zone' not in r.answer
r=ask(q,'not json');checks['bad_schema_not_silent_native_fallback']='unavailable' in r.mode and not r.hits
r=ask('Tekken 9 อยู่โซนไหน','[["Z",0,2]]');checks['wrong_game_edition_not_substituted']=not r.hits and 'PC Zone' not in r.answer
r=ask('นักศึกษา PSU เล่น PC ราคาเท่าไหร่','[["P",0,4]]');checks['normal_source_zero_price_retained']='0 บาท' in r.answer and bool(r.hits)
out=R/('protocol_controls_'+str(time.time_ns()));out.mkdir();report={'all_passed':all(checks.values()),'checks':checks,'actual_model_calls':0,'mocked_gateway':True,'scope':'literal range/schema handling and source guard wiring; not actual model reasoning accuracy'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8');(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
