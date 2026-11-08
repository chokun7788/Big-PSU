from test_r66_reader import answer,a
import json
from app.knowledge.common.query_scope import lexical_rule_topics,rule_selection
from app.knowledge.common.query_contract import semantic_clauses
from app.knowledge.common.registry import value
from app.pipeline.competition_taxonomy import detect_competition_facet
q='กติกา CS2 ช่วงเตรียมตัวมีผู้เล่นได้กี่คนและในพื้นที่แข่งกินดื่มอะไรได้บ้าง';r=answer(q);p=r.decision_artifact['query_plan'];print(json.dumps(p,ensure_ascii=False,indent=2))
with a.store.connect() as c:rs=a.store.heads(c)
children=[x for x in rs.values() if x['kind']=='competition_rule' and value(x,'competition_id')=='competition_competition_rules_cs2_psu_phuket_2026']
def body(r,k):return ' '.join(str(x or '') for x in (value(r,k) or {}).values())
for clause in semantic_clauses(p['query_without_entity']):
 print('CLAUSE',clause,'FACET',detect_competition_facet(clause));print([value(x,'heading') for x in lexical_rule_topics(clause,children,body)])
