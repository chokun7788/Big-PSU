"""Unit check of real packaging against a pinned snapshot and captured output.

The finish stub captures package fields; this is not a real HTTP/model test.
"""
import json,os,sys,time
from dataclasses import dataclass
from pathlib import Path
R=Path(__file__).resolve().parent;ROOT=R.parent;OLD=ROOT/'r122_context_scope_calendar_20261022';S=R/'revision04_system'
os.environ['PSU_COMMON_CHAT_PROFILE']='r69-migration-preview';sys.path.insert(0,str(S))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.understanding import parse
from app.knowledge.common.domain_flow.meaning_review import review
from app.knowledge.common.domain_flow.integration import package
@dataclass
class Captured:
 decision_artifact:dict
class Reader:
 def finish(self,snapshot,started,answer,hits,plan,obs,response):
  self.answer=answer;self.hits=hits
  return Captured({'response_type':response})
snapshot=MigratedView(S/'data/knowledge/common.sqlite').snapshot();engine=Engine.from_snapshot(snapshot)
row=json.loads((OLD/'comparison01/trained/RESULTS.jsonl').read_text('utf8').splitlines()[0]);u=row['response']['decision_artifact']['understanding'];q=u['event']['input_question']
meaning=parse(u['event']['raw_content'],q);meaning.event['raw_content']=u['event']['raw_content'];meaning=review(q,engine.index,meaning)
result=engine.answer(q,'en',at='2026-10-21T12:00:00+07:00',allow_llm=False,understanding=meaning)
reader=Reader();out=package(reader,snapshot,time.perf_counter(),q,result)
checks={'compiled_request_in_public_artifact':out.decision_artifact['execution_contract']['path']=='compiled_legacy_wire',
 'per_need_obligations_in_public_artifact':all(n['execution_contract'].get('obligations') for n in out.decision_artifact['need_results']),
 'public_artifact_does_not_claim_semantic_verification':not out.decision_artifact['execution_contract']['whole_question_semantics_verified'],
 'source_hits_stay_within_snapshot':all(h['source_id'] in snapshot['release']['sources'] for h in reader.hits),
 'answer_preserved_by_packaging':reader.answer==result['answer']}
target=R/('PACKAGE_VERIFICATION_'+str(time.time_ns())+'.json');target.write_text(json.dumps({'all_passed':all(checks.values()),'checks':checks,'actual_http_test':False,'new_model_calls':0,'artifact':out.decision_artifact},ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'checks':checks,'output':str(target)},ensure_ascii=False,indent=2),flush=True);assert all(checks.values())
