"""Replay captured model plans after adapter repair; zero new inference."""
import json,os,time
from unittest.mock import patch
from verification_support import R
os.environ['PSU_MODEL_FIRST_TRIAL']='1'
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.migrated_view import MigratedView
source=R/'real_model_batch_1794469085935882400/DETAILS.json'
rows=[];reader=CommonAnswerer(MigratedView(R/'system/data/knowledge/verified_sources.sqlite'))
for saved in json.loads(source.read_text(encoding='utf8')):
 content=saved['audit']['raw_model_content']
 with patch('app.knowledge.common.domain_flow.model_gateway.call',return_value={'message':{'content':content}}),patch('urllib.request.urlopen',side_effect=AssertionError('Replay cannot call HTTP')):
  result=reader.answer(saved['question'],locale='th',planner=None)
 rows.append({'id':saved['id'],'question':saved['question'],'captured_plan':content,'answer':result.answer,'mode':result.mode,'artifact':result.decision_artifact})
out=R/('saved_plan_replay_'+str(time.time_ns()));out.mkdir()
(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
report={'actual_model_calls':0,'source':str(source),'rows':[{'id':r['id'],'mode':r['mode'],'answer':r['answer']} for r in rows],'scope':'captured-plan source-adapter replay, not model reasoning retest'}
(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report},ensure_ascii=False))
