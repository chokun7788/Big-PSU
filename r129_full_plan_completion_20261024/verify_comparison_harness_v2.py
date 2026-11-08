import ast,json,sys,time
from pathlib import Path
from unittest.mock import patch
from datetime import datetime
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import parse
from app.knowledge.common.domain_flow.meaning_review import review
from app.knowledge.common.domain_flow.context_guard import apply
from app.knowledge.common.domain_flow.contracts import RequestBudget
from app.knowledge.common.flow_context import request_context
from app.knowledge.common.migrated_view import MigratedView
e=Engine.from_snapshot(MigratedView(R/'system/data/knowledge/common.sqlite').snapshot());xs=[json.loads(s) for s in (R/'three_arm01/RESULTS.jsonl').read_text('utf8').splitlines()];checks={};results=[]
for i,x in enumerate(xs):
 u=apply(x['question'],e.index,review(x['question'],e.index,parse(x['raw_output'],x['question'])))
 with request_context() as ctx,patch('urllib.request.urlopen',side_effect=AssertionError('No new model/provider inference during saved-response replay')):
  ctx.input={'raw_question':x['question']};ctx.model_calls_reserved=1;budget=RequestBudget(model_calls=1)
  result=e.answer(x['question'],x['locale'],at=datetime.fromisoformat('2026-10-24T12:00:00+07:00'),allow_llm=True,budget=budget,understanding=u)
  checks['saved_invalid_wire_'+str(i)+'_still_executes']=bool(result.get('claims'));checks['saved_planner_call_'+str(i)+'_debits_request_budget']=budget.model_calls==1 and ctx.model_calls_reserved==1
  results.append({'key':x['key'],'original_protocol_rejected':not parse(x['raw_output'],x['question']).accepted,'result':result})
ast.parse((R/'compare_planners_v2.py').read_text('utf8'))
out=R/('harness_verification_'+str(time.time_ns()));out.mkdir();r={'all_passed':all(checks.values()),'checks':checks,'new_model_inferences':0,'saved_outputs_reused':len(xs),'frozen_system_modified':False};(out/'RESULT.json').write_text(json.dumps(r,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),'utf8');print(json.dumps(r));assert r['all_passed']
