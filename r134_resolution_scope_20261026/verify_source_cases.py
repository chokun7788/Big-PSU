"""Existing authored source cases through the repaired compiler/readers; no model."""
import collections,json,time
from dataclasses import asdict
from verification_support import R,snapshot
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.native_intents import propose
from app.knowledge.common.domain_flow.meaning_review import review
from app.knowledge.common.domain_flow.understanding import Understanding
from app.knowledge.common.domain_flow.scope import reference_time
engine=Engine.from_snapshot(snapshot())
prior=json.loads((R.parent/'r131_diagnostic_review_20261025/CONSOLIDATED_SOURCE_REVIEW.json').read_text('utf8'))['cases']
tag='local_'+str(time.time_ns());out=R/tag;out.mkdir()
rows=[]
for case in prior:
 q=case['question'];native=propose(engine.index,q)
 proposal=native if native is not None else review(q,engine.index,Understanding(reason='repair_verification',event={'model_called':False}))
 try:
  result=engine.answer(q,'auto',at=reference_time('2026-10-16T12:00:00+07:00'),allow_llm=False,understanding=proposal)
  rows.append({'key':case['key'],'question':q,'old_answer':case['saved_answer'],'old_confirmed_content_failure':case['confirmed_content_scope_omission_example'],'proposal':proposal.as_dict(),'result':result,'answer_changed':result['answer']!=case['saved_answer'],'source_adjudication':'pending_review_not_automatic_pass'})
 except Exception as e:
  import traceback
  rows.append({'key':case['key'],'question':q,'error':repr(e),'traceback':traceback.format_exc()})
with (out/'CASES.jsonl').open('w',encoding='utf8') as f:
 for row in rows:f.write(json.dumps(row,ensure_ascii=False)+'\n')
summary={'cases':len(rows),'exceptions':[{'key':x['key'],'error':x['error']} for x in rows if 'error' in x],'changed_answers':sum(x.get('answer_changed',False) for x in rows),'statuses':dict(collections.Counter(x.get('result',{}).get('status') for x in rows)),'no_model_or_assistant_calls':True,'semantic_accuracy':None}
(out/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8')
(R/'LATEST_LOCAL_REVIEW.json').write_text(json.dumps({'output':str(out),**summary},ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'output':str(out),**summary},ensure_ascii=False))
