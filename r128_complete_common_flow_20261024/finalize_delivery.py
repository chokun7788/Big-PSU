import hashlib,json,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent
def load(name):return json.loads((R/name).read_text('utf8'))
e=load('EVIDENCE.json');a=load('ACTIVATION.json');run=load('FINAL_RUN.json')
assert e['implementation_scope_complete'] and a['all_passed'] and run['source_unchanged']
assert all(v['result']['all_passed'] for v in e['gates'].values())
with urllib.request.urlopen(a['url']+'/health',timeout=4) as f:h=json.load(f)
assert h['runtime']['version']=='R128' and h['runtime']['python']['pid']==a['pid']
frozen=json.loads((Path(run['api']['output'])/'FINAL_SOURCE_FREEZE.json').read_text('utf8'))
assert all(hashlib.sha256((R/'system'/p).read_bytes()).hexdigest()==sha for p,sha in frozen.items())
names=['FULL_FLOW_TH.md','DELIVERY_REPORT_TH.md','DEVELOPMENT_REVIEW_TH.md','ALL_RESPONSES_TH.md','EVIDENCE.json','ACTIVATION.json','Start-R128.cmd','start_stack.py','start_candidate.py','start_model.py','serve_api.py','serve_model.py','context_contract.py','Open-Owner-Content.cmd','open_owner.py','owner_editor.py','UI_R128.png']
manifest={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in names};manifest.update({'system/'+p:sha for p,sha in frozen.items()});manifest['system/data/knowledge/common.sqlite']=e['database']['sha256']
(R/'DELIVERY_FREEZE.json').write_text(json.dumps(manifest,indent=2),'utf8')
result={'status':'implementation_scope_completed_and_activated','scope':e['implementation_scope'],'main_http_requests':123,'overall_semantic_accuracy':None,'full_20554_test_run':False,'source_unchanged_during_main_suite':True,'original_and_parent_unchanged':e['protected_sources'],'real_database_unchanged':True,'approvals_changed':False,'preview_url':a['url'],'preview_pid':a['pid'],'production_R78_replaced':False,'reports':names[:4],'remaining_data_limits_documented':True,'delivery_files':len(manifest)}
(R/'COMPLETE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8');print(json.dumps(result,ensure_ascii=False,indent=2))
