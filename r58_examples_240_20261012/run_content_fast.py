"""All 5,020 content queries against ONE immutable demo release.
Snapshot loading is reused, while each answer still checks the database epoch.
This evaluates content/routing, never benchmark whole-request or LLM latency.
"""
import json
from pathlib import Path
import build_and_test as task
class OneReleaseStore(task.CommonStore):
    def freeze(self):self.frozen=super().snapshot();return self
    def snapshot(self):return self.frozen
if __name__=='__main__':
    root=task.BASE
    store=OneReleaseStore(task.DB).freeze()
    if not store.frozen['allow_demo']:raise SystemExit('Refuse non-demo database')
    if len(store.frozen['release']['records'])!=240:raise SystemExit('Expected 240 records')
    task.BASE=root/'content_round2'
    task.BASE.mkdir(exist_ok=False)
    task.filejson('EVALUATION_SCOPE.json',{'warning':task.WARNING,'mode':'one validated immutable release reused for content tests','epoch_checked_for_every_answer':True,'actual_common_answerer':True,'llm':False,'live_wordpress':False,'human_review':False,'not_latency_benchmark':True,'expected_nested_contact_rendering_fixed':True})
    task.run_tests(store)
