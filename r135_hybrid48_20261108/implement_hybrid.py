"""Apply candidate-local integration changes and emit the initial route matrix."""
import json, pathlib
ROOT=pathlib.Path(__file__).resolve().parent
SYSTEM=ROOT/'system'
import sys
sys.path.insert(0,str(SYSTEM))
from app.knowledge.common.domain_flow.capabilities import SUPPORTED
folder=SYSTEM/'app/knowledge/common/domain_flow'
routes={}
for cat,operations in SUPPORTED.items():
    for op,fields in operations.items():
        for field in fields:
            key='|'.join([cat,op,field])
            routes[key]={'reader':'r134_compat' if key=='C03|detail|device_type' else 'r135',
                'acceptance':'candidate_pending_focused_checks',
                'scope':'registered adapter; per-request source/semantic constraints still checked'}
(folder/'hybrid_routes.json').write_text(json.dumps({'version':'r135-hybrid48-routing-v1','routes':routes},ensure_ascii=False,indent=2),'utf8')
p=folder/'engine.py';s=p.read_text(encoding='utf8');needle='    def plan(self,category,question,at=None,meaning=None):\n'
assert s.count(needle)==1
s=s.replace(needle,needle+'        from .hybrid_policy import plan\n        return plan(self,category,question,at,meaning,self._r135_plan)\n\n    def _r135_plan(self,category,question,at=None,meaning=None):\n',1);p.write_text(s,'utf8')
p=folder/'result_contract.py';s=p.read_text(encoding='utf8');needle="'claims':copy.deepcopy(result.get('claims',[])),'receipts':receipts,'calculation_receipts':calculations,"
assert s.count(needle)==1;s=s.replace(needle,needle+"\n  'reader_route':copy.deepcopy(metadata.get('hybrid_route')),",1);p.write_text(s,'utf8')
p=SYSTEM/'app/knowledge/common/answer.py';s=p.read_text(encoding='utf8');needle='        return attach_runtime(attach(out,context,engine.index.records),context,snapshot,index=engine.index)'
assert s.count(needle)==1;s=s.replace(needle,"        result=attach_runtime(attach(out,context,engine.index.records),context,snapshot,index=engine.index)\n        from .domain_flow.hybrid_policy import attach as attach_hybrid\n        from dataclasses import replace\n        return replace(result,decision_artifact=attach_hybrid(dict(result.decision_artifact or {})))",1);p.write_text(s,'utf8')
p=SYSTEM/'app/knowledge/common/build_info.py';s=p.read_text(encoding='utf8').replace("'common-r135-complete-flow-audit'","'common-r135-hybrid48-trial'");p.write_text(s,'utf8')
print(json.dumps({'routes':len(routes),'compatibility_routes':[k for k,v in routes.items() if v['reader']=='r134_compat']}))
