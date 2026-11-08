"""Do not label a curated alias as literal original-question identity."""
import ast,json,os,sys,time
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'));os.environ['PSU_COMMON_CHAT_PROFILE']='r69-migration-preview'
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.scope import reference_time
reader=CommonAnswerer(MigratedView(R/'system/data/knowledge/common.sqlite'))
source=json.loads((R.parent/'r107_owner_questions_20261020/owner_update_50/SOURCE_OWNER_50.json').read_text('utf8'))
q={i['number']:i['question'] for i in source['source_items']};checks={}
for n,expected in [(27,True),(11,False)]:
 result=reader.answer(q[n],locale='th',at=reference_time('2026-10-25T12:00:00+07:00'),planner=None)
 contract=result.decision_artifact['execution_contract']
 checks[str(n)+'_literal_identity_honest']=contract['question_identity_checked'] is expected
 checks[str(n)+'_no_semantic_entailment_overclaim']=contract['whole_question_semantics_verified'] is False
checks['all_python_syntax_valid']=all(ast.parse(p.read_text('utf-8-sig')) is not None for p in [*R.glob('*.py'),*(R/'system').rglob('*.py')])
out=R/('source_match_metadata_'+str(time.time_ns()));out.mkdir();r={'all_passed':all(checks.values()),'checks':checks,'new_benchmark_questions':0,'model_inferences':0}
(out/'RESULT.json').write_text(json.dumps(r,indent=2),'utf8');print(json.dumps(r))
assert r['all_passed']
