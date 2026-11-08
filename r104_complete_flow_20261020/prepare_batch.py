"""P6: compile/schema/FK/fixture preparation only. Zero chatbot/model calls."""
import ast,json,os,sys,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path[:0]=[str(R/'system'),str(R)]
os.environ.update(PSU_COMMON_ALLOW_DEMO='1',PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_ESPORTS_NOW='2026-10-20T12:00:00+07:00')
errors=[]
for p in [*(R/'system/app').rglob('*.py'),*R.glob('*.py')]:
 try:ast.parse(p.read_text('utf8'),filename=str(p))
 except (SyntaxError,UnicodeDecodeError) as e:errors.append(str(e))
if errors:raise SystemExit(json.dumps(errors))
from scenario_support import Fixture
from acceptance_cases import QUESTIONS,variants
from app.knowledge.common.registry import CATALOG,SCHEMAS,release_errors
from app.knowledge.common.read_graph import REQUIRED
from app.knowledge.common.task_contracts import TASKS
assert len(CATALOG)==24 and set(REQUIRED)==set(TASKS) and len(TASKS)==32
(R/'fixtures').mkdir(exist_ok=True)
base=R/'fixtures/BASE_SYNTHETIC.sqlite'
if base.exists():raise SystemExit('Refusing to overwrite prepared fixture; preserve prior preflight evidence')
fixture=Fixture(base)
with fixture.store.connect() as c:
 validation=release_errors(fixture.store.heads(c),fixture.store.sources(c),demo=True)
if validation:
 (R/'PREFLIGHT_FAILED.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2),'utf8')
 raise SystemExit(json.dumps(validation,ensure_ascii=False))
spec=json.loads((R.parent/'r97_flow_reassessment_20261019/FLOW_SPEC.json').read_text('utf8'));source={c['id']:c for c in spec['cases']}
jobs=[]
for cid,pair in QUESTIONS.items():
 for locale in ['th','en','auto']:
  language='th' if locale=='th' or locale=='auto' else 'en'
  for vi,q in enumerate(variants(pair[language=='en'],language)):
   jobs.append({'id':cid+'_'+locale+'_'+str(vi),'scenario':cid,'locale':locale,'wording_index':vi,'question':q,
     'r97_original_question':source[cid]['utterance'],'fixture_precondition':source[cid]['fixture_precondition'],'expected_invariant':source[cid]['expected_behavior'],
     'fixture_factory':'scenario_support.Fixture + acceptance_cases.execute','model_protocol_simulated':cid=='C31','live_provider':'simulated',
     'design_note':('Alternative source-backed utterance exercises the model failure/deadline path; a deterministic early clarification would not exercise that failure.' if cid in {'C31','C32'} else 'Source-backed fixture names/translation preserve the requested behavioral invariant.')})
assert len(jobs)==444 and len({j['id'] for j in jobs})==444
(R/'BATCH_JOBS.json').write_text(json.dumps(jobs,ensure_ascii=False,indent=2),'utf8')
report={'status':'static_preflight_passed','syntax_errors':errors,'schema_kinds':len(CATALOG),'task_graphs':len(TASKS),'r97_scenarios':len(QUESTIONS),
 'scenario_variants':len(jobs),'fixture_publication_validation_errors':validation,'fixture_sha256':hashlib.sha256(base.read_bytes()).hexdigest(),
 'chatbot_requests':0,'model_calls':0,'runtime_behavior_verified':False}
(R/'PREFLIGHT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8');print(json.dumps(report,ensure_ascii=False))
