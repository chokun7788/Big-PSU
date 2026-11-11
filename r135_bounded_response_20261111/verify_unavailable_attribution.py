"""Replay saved artifacts, not model requests; preserve failure and empty proof."""
import copy,json,sqlite3,time
from types import SimpleNamespace
from verification_support import R
from app.knowledge.common.result_contract import status,finalize
from app.pipeline.schemas import PipelineAnswer,PipelineRoute,EntityBundle,ValidationResult

e=R.parent/'r135_verified_eval200_20261111/evaluation'
db=sqlite3.connect((e/'runtime/logs/transcripts.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
rows=[];checks={};counts={}
for row in map(json.loads,(e/'RESULTS.jsonl').open(encoding='utf8')):
 m=db.execute('SELECT metadata_json FROM chat_messages WHERE session_id=? AND role=? ORDER BY id DESC LIMIT 1',(row['session_id'],'assistant')).fetchone()
 art=json.loads(m[0]).get('decision_artifact',{})
 if (art.get('query_plan') or {}).get('method')!='r101_model_unavailable':continue
 result=PipelineAnswer(answer=row['response']['answer'],hits=[],elapsed=0,mode=row['response']['mode'],confidence=0,
  route=PipelineRoute('knowledge','common_read',0,'unavailable','medium','saved replay'),entities=EntityBundle(),validation=ValidationResult(True),decision_artifact=copy.deepcopy(art))
 state,reasons=status(result);updated=finalize(result,row['question'])
 reason=reasons[0];counts[reason]=counts.get(reason,0)+1
 checks['replay_'+row['key']]=state=='temporary_failure' and reason in {'model_admission_unavailable','model_timeout'} and all('store_or_snapshot_unavailable' not in n.get('reason_codes',[]) for n in updated.decision_artifact['need_results']) and updated.answer==result.answer and not updated.hits and not updated.decision_artifact.get('claim_packets')
 rows.append({'key':row['key'],'new_reason':reason,'state':state})
db.close()
for name,art,expected in [('real_store_error',{'store_error_type':'OperationalError','response_type':'unavailable'},'store_or_snapshot_unavailable'),('snapshot_error',{'response_type':'unavailable','query_plan':{'method':'r102_snapshot_unavailable'}},'store_or_snapshot_unavailable'),('retry',{'response_type':'retry'},'snapshot_changed_during_read'),('unknown_provider',{'response_type':'unavailable'},'checking_service_unavailable')]:
 result=SimpleNamespace(decision_artifact=art,route=SimpleNamespace(answer_type='unavailable'),validation=SimpleNamespace(errors=[]))
 checks[name]=status(result)==('temporary_failure',[expected])
checks['fifteen_cases_replayed']=len(rows)==15
out=R/('unavailable_attribution_'+str(time.time_ns()));out.mkdir()
report={'all_passed':all(checks.values()),'checks':checks,'replayed_origins':counts,'http_requests':0,'model_calls':0,
 'scope':'saved replay and explicit store-error/unknown-provider metadata controls; reason attribution only, no unavailable answers fixed or full score changed'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8');(out/'DETAILS.json').write_text(json.dumps(rows,indent=2),encoding='utf8')
print(json.dumps({'output':str(out),**report}));assert report['all_passed']
