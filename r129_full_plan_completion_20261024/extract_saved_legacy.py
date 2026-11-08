"""Read original legacy results without issuing any old-flow question."""
import collections,gzip,hashlib,importlib.util,json
from pathlib import Path
R=Path(__file__).resolve().parent;OLD=R.parent/'r64_full_comparison_20261013'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
spec=importlib.util.spec_from_file_location('r64_saved_readonly',OLD/'analyze.py');reader=importlib.util.module_from_spec(spec);spec.loader.exec_module(reader)
published=json.loads((OLD/'ANALYSIS_LATEST.json').read_text('utf8'));assert published['legacy_llm']['complete'] and json.loads((OLD/'FULL_TEST_COMPLETE.json').read_text('utf8'))['complete']
paths=[OLD/'model_matrix/legacy_RESULTS.jsonl.gz']+sorted(OLD.glob('model_matrix_*/legacy_RESULTS.jsonl.gz'));paths=[p for p in paths if p.exists()]
seen=set();counts=collections.Counter();by_requested=collections.defaultdict(collections.Counter)
out=R/'SAVED_LEGACY_ROWS.jsonl.gz'
with gzip.open(out,'xt',encoding='utf8') as f:
 for path in paths:
  for row in reader.read(path):
   key=row['key']
   if key in seen:continue
   seen.add(key);counts['requests']+=1;grades=[];locale=row.get('requested_locale','auto')
   for g in row.get('grades',[]):
    counts['grades']+=1;counts['passed']+=int(g['passed']);by_requested[locale]['grades']+=1;by_requested[locale]['passed']+=int(g['passed'])
    grades.append({k:g.get(k) for k in ['file','row','variant','id','passed','failures','content_asserted','content_checks_passed','evidence_level']})
   f.write(json.dumps({'key':key,'requested_locale':locale,'effective_locale':row.get('effective_locale'),'exception':row.get('exception'),'grades':grades,'saved_raw_file':str(path.resolve())},ensure_ascii=False)+'\n')
assert counts['requests']==20554 and counts['grades']==55811 and counts['passed']==42601,dict(counts)
for c in by_requested.values():c['strict_percent']=round(100*c['passed']/c['grades'],4)
summary={'arm':'R64 legacy LLM allowed','complete':True,'counts':dict(counts),'by_requested_locale':dict(by_requested),'published_by_effective_locale':published['legacy_llm']['by_language'],'published_positive_content':{k:v for k,v in published['legacy_llm']['counts'].items() if 'content' in k},'published_language_basis':'effective locale, do not compare against requested locale without rebucketing','saved_results_reused_no_baseline_inference':True,'source_data_backend_clock_deadline_versions_differ_from_R129':True,'causal_flow_effect':False,'source_files':{str(p.resolve()):sha(p) for p in paths+[OLD/'ANALYSIS_LATEST.json',OLD/'FULL_TEST_COMPLETE.json']},'extracted_rows_sha256':sha(out)}
(R/'SAVED_LEGACY_REFERENCE.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'counts':dict(counts),'by_requested_locale':dict(by_requested),'new_model_inferences':0}))
