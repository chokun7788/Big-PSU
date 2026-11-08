"""Check the existing 50 owner statements against read-only candidate paths.

No new benchmark questions, no model or provider inference, no data mutation.
"""
import hashlib,json,os,sys,time,traceback
from pathlib import Path
from datetime import datetime
from unittest.mock import patch
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'));os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_DOMAIN_FLOW_ENABLED='1')
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.answer import CommonAnswerer
source=json.loads((R.parent/'r107_owner_questions_20261020/owner_update_50/SOURCE_OWNER_50.json').read_text('utf8'))
db=R/'system/data/knowledge/common.sqlite';before=hashlib.sha256(db.read_bytes()).hexdigest();reader=CommonAnswerer(MigratedView(db));OUT=R/('owner_read_audit_'+str(time.time_ns()));OUT.mkdir();rows=[]
with (OUT/'RESULTS.jsonl').open('x',encoding='utf8') as f,patch('urllib.request.urlopen',side_effect=AssertionError('Network forbidden in source-read audit')):
 for item in source['source_items']:
  row={'number':item['number'],'question':item['question'],'owner_answer':item['answer'],'source_usable':item['usable_answer'],'semantic_status':'manual_scope_review_required'}
  try:
   out=reader.answer(item['question'],locale='th',at=datetime.fromisoformat('2026-10-25T12:00:00+07:00'),planner=None);art=out.decision_artifact or {}
   row.update(answer=out.answer,validation_ok=out.validation.ok,response_type=art.get('response_type'),query_plan=art.get('query_plan'),execution_contract=art.get('execution_contract'),understanding=art.get('understanding'),claims=art.get('domain_flow',{}).get('typed_claims',[]))
  except Exception as exc:row.update(error=repr(exc),traceback=traceback.format_exc())
  rows.append(row);f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush()
  print(str(item['number'])+' '+str(row.get('response_type'))+' '+str(row.get('answer',row.get('error','')))[:155],flush=True)
assert before==hashlib.sha256(db.read_bytes()).hexdigest()
(OUT/'COMPLETE.json').write_text(json.dumps({'source_items_read':len(rows),'new_questions':0,'model_inferences':0,'network_requests':0,'database_unchanged':True,'semantic_accuracy_not_claimed':True},indent=2),'utf8');(R/'OWNER_READ_AUDIT_LATEST.json').write_text(json.dumps({'output':str(OUT),'source_items':50},indent=2),'utf8')
