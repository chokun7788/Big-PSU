"""Actual local-model schema/selection gate using isolated synthetic evidence."""
import json,sys,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
from app.knowledge.common.domain_flow.model import EvidenceSelector,MODEL
from app.knowledge.common.domain_flow.contracts import RequestBudget
from test_scopes_protocol import fact
out=R/'verification'/sys.argv[1];out.mkdir(parents=True,exist_ok=False)
with urllib.request.urlopen('http://127.0.0.1:11434/api/tags',timeout=5) as response:tags=json.load(response)
digest=next(x['digest'] for x in tags['models'] if x['name']==MODEL)
assert digest=='b1f251ef835962b270ba48266d4e32e6f90b29f10930d0712ef5eaabec773a05'
a=fact('C01','room_alpha','address','Alpha Room','address','Synthetic building A')
b=fact('C03','pad_beta','controllers','Beta Pad','controllers per console','3 controllers')
tasks=[{'question':'What is the address of Alpha Room?','language':'en','facts':[a,b]},
 {'question':'How many controllers does Beta Pad provide?','language':'en','facts':[a,b]},
 {'question':'What is the private salary of the Gamma Room manager?','language':'en','facts':[a,b]}]
plans,event=EvidenceSelector(timeout=35).select(tasks,RequestBudget())
checks={'transport':event['transport_ok'],'all_items_valid':event['schema_ok'],'address_selection':plans[0].ids==[a['id']],
 'controller_selection':plans[1].ids==[b['id']],'unsupported_field_abstention':plans[2].ids==[] and plans[2].status=='missing_source'}
(out/'RESULT.json').write_text(json.dumps({'model':MODEL,'digest':digest,'checks':checks,'event':event,'plans':[vars(p) for p in plans]},ensure_ascii=False,indent=2),'utf8')
print(json.dumps(checks));raise SystemExit(not all(checks.values()))
