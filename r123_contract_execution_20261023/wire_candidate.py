"""Wire compiled execution into isolated Engine and expose audit in packaging."""
import ast,json
from pathlib import Path
R=Path(__file__).resolve().parent;D=R/'system/app/knowledge/common/domain_flow'
p=D/'engine.py';x=p.read_text('utf8');needle='    def answer(self,question,locale='
assert x.count(needle)==1
x=x.replace(needle,'    def _legacy_answer(self,question,locale=',1)
x+='''\n    def answer(self,question,locale='auto',category=None,at=None,allow_llm=True,history=None,budget=None,understanding=None):
        from .task_execution import execute
        return execute(self,question,locale,category,at,allow_llm,history,budget,understanding)
'''
needle="        if not selected and plan.metadata.get('context_clarification'):"
x=x.replace(needle,"        if not selected and plan.metadata.get('execution_notice'):\n            blocks=[plan.metadata['execution_notice'][lang]]\n"+needle)
ast.parse(x);p.write_text(x,'utf8')
p=D/'integration.py';x=p.read_text('utf8')
needle="'need_results':rows,'understanding':result.get('understanding',{}),'domain_flow':"
assert needle in x
x=x.replace(needle,"'need_results':rows,'understanding':result.get('understanding',{}),'execution_contract':result.get('execution_contract',{}),'domain_flow':")
needle="'reason_codes':[n['reason']],'receipts':receipts,'claim_packets':n['claims'],'semantic_correctness_verified':False}"
assert needle in x
x=x.replace(needle,"'reason_codes':[n['reason']],'receipts':receipts,'claim_packets':n['claims'],'execution_contract':n.get('execution_contract',{}),'semantic_correctness_verified':False}")
ast.parse(x);p.write_text(x,'utf8')
# Fix a source-confirmed normalization risk documented in R122: strip both
# raw and normalized word-duration text before broadening the comparison pool.
p=D/'meaning_reader.py';x=p.read_text('utf8')
needle="for text in durations:scope=scope.replace(text,' ')"
assert needle in x;x=x.replace(needle,"for text in durations:scope=scope.replace(text,' ').replace(execution_query(index,text,meaning),' ')")
ast.parse(x);p.write_text(x,'utf8')
print('Compiled Engine and public audit packaging wired; native calendar/live special adapters retained')
