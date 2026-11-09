"""Capture pre-verifier price payload in isolated draft DB; no model calls."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow import task_execution,integration,obligation_verifier
out=R/('pc_assessment_'+str(time.time_ns()));out.mkdir()
src=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
dst=sqlite3.connect(out/'source.sqlite');src.backup(dst);dst.close();src.close()
os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'sessions.sqlite')
rows=[];current=''
original=obligation_verifier.assess
def observe(index,task,result,snapshot,question=''):
    ledger=original(index,task,result,snapshot,question)
    if task.category=='C06':rows.append({'outer_question':current,'task_question':question,'plan':copy.deepcopy(result.get('plan')),'computations':copy.deepcopy(result.get('computations')),'claims':copy.deepcopy(result.get('claims')),'fatal':ledger.get('fatal')})
    return ledger
with patch.object(task_execution,'assess',observe),patch.object(obligation_verifier,'assess',observe),patch('urllib.request.urlopen',side_effect=AssertionError('HTTP forbidden')):
    for current in ['PC ราคาเท่าไหร่','Tekken 8 ปุ่มอะไร แล้ว PC ราคาเท่าไหร่']:
        result=CommonAnswerer(DraftSnapshotView(CommonStore(out/'source.sqlite'))).answer(current,locale='th',at='2026-11-08T12:00:00+07:00',planner=None)
        print(json.dumps({'question':current,'answer':result.answer},ensure_ascii=False),flush=True)
(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'output':str(out),'captured':len(rows),'model_calls':0}),flush=True)
