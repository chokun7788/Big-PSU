"""Document integrity and preserved-source checks only. No chat/model calls."""
import hashlib,json,re
from pathlib import Path
R=Path(__file__).resolve().parent;ROOT=R.parent;OLD=ROOT/'r122_context_scope_calendar_20261022'
names=['FLOW_MAIN_TH.md','DATA_CONTRACTS_TH.md','IMPLEMENTATION_EVALUATION_TH.md','DESIGN_REVIEW_TH.md']
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
texts={name:(R/name).read_text('utf8') for name in names}
for name,text in texts.items():
 assert len(text)>1000,name
 assert text.count('```')%2==0,('unclosed_fence',name)
 for target in re.findall(r'\]\(([^)]+)\)',text):
  if not target.startswith(('https://','http://','#')):assert (R/target).is_file(),(name,target)
assert all('C'+str(i).zfill(2) in texts['FLOW_MAIN_TH.md'] for i in range(1,15))
assert all('R'+str(i).zfill(2) in texts['FLOW_MAIN_TH.md'] for i in range(13))
assert all('P'+str(i) in texts['IMPLEMENTATION_EVALUATION_TH.md'] for i in range(9))
examples=re.findall(r'```json\n(.*?)\n```',texts['DATA_CONTRACTS_TH.md'],re.S)
assert len(examples)==1
example=json.loads(examples[0]);q=example['raw_question']
assert all(t['source_quote'] in q for t in example['tasks'])
assert all(s['quote'] in q for s in example['slots'])
assert all(e['mention'] in q for e in example['entities'])
assert all(b['quote'] in q for b in example['shared_bindings'])
tasks={t['id'] for t in example['tasks']};entities={e['id'] for e in example['entities']}
assert all(t['target_ref'] in entities for t in example['tasks'])
assert all(b['from_entity'] in entities and b['to_task'] in tasks for b in example['shared_bindings'])
protected={}
for path in [OLD/'api02/RUN_FREEZE.json',OLD/'ellipsis01/RUN_FREEZE.json',OLD/'comparison01/RUN_FREEZE.json',ROOT/'r121_context_planner_training_20261022/PROTECTED_INPUTS.json',ROOT/'r121_context_planner_training_20261022/train02/RUN_FREEZE.json']:
 manifest=json.loads(path.read_text('utf8'))
 for p,h in manifest.items():
  assert p not in protected or protected[p]==h,('conflicting_freeze',p)
  protected[p]=h
changed=[p for p,h in protected.items() if not Path(p).is_file() or sha(Path(p))!=h]
assert not changed,changed
result={'status':'design_ready_for_implementation','design_only':True,'candidate_implemented':False,'new_training':False,'new_chat_requests':0,'full_test_started':False,'new_production_install':False,'coverage_categories':[f'C{i:02}' for i in range(1,15)],'runtime_stages':[f'R{i:02}' for i in range(13)],'implementation_phases':[f'P{i}' for i in range(9)],'design_review_passes':3,'document_checks':{'local_links_resolve':True,'fences_balanced':True,'example_json_parsed':True,'example_quotes_and_references_bound':True},'preserved_source_files_checked':len(protected),'preserved_source_files_changed':changed,'document_sha256':{name:sha(R/name) for name in names},'semantic_accuracy':None,'next_phase':'P0 contracts/capability matrix, then P1 task graph and verifiers'}
(R/'PLAN_STATUS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'status':result['status'],'documents':len(names),'preserved_files_checked':len(protected),'changed':len(changed),'chat_requests':0},ensure_ascii=False))
