import sys,json,hashlib,re,subprocess
from pathlib import Path
B=Path(__file__).resolve().parent;tag=sys.argv[1];read=lambda p:json.loads(p.read_text(encoding='utf-8'));sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
d=read(B/('DEPLOY_'+tag)/'APPLIED.json');root=Path(d['project_root']);verified=read(B/('VERIFIED_'+tag+'.json'));delivery=read(B/('CANDIDATE_DELIVERED_'+tag+'.json'));errors=[]
for row in d['files']:
 if sha(Path(row['target']))!=row['after_sha256']:errors.append('Deployed source changed: '+row['path'])
 if row['backup'] and sha(Path(row['backup']))!=row['before_sha256']:errors.append('Before backup differs: '+row['path'])
for path,h in d['protected_databases'].items():
 if sha(Path(path))!=h:errors.append('Protected DB changed: '+path)
if sha(Path(delivery['candidate_path']))!=verified['database_sha256']:errors.append('Delivered candidate differs from tested snapshot')
documents=['R66_FINAL_REPORT_TH.md','FLOW_R66_COMPLETE_TH.md','REPAIR_LEDGER_TH.md','OWNER_CONFIRMATION_REQUIRED_TH.md','REMAINING_FAILURE_ANALYSIS_TH.md','TRANSLATION_FAILURE_TAXONOMY_TH.md','PUBLICATION_BLOCKERS_TH.md','CURRENT_RESIDUALS_'+tag+'_TH.md','BEFORE_AFTER_'+tag+'.md','R66_HANDOFF_FINAL_TH.md'];links=set()
for name in documents:
 p=B/name
 if not p.is_file() or p.stat().st_size==0:errors.append('Missing/empty document: '+name);continue
 for path in re.findall(r'\]\((C:/[^)]+)\)',p.read_text(encoding='utf-8')):
  links.add(path)
  if not Path(path).exists():errors.append('Broken local link in '+name+': '+path)
status=subprocess.run(['git','status','--short'],cwd=root,capture_output=True,text=True,check=True).stdout
new=B/('PROJECT_GIT_STATUS_after_'+tag+'.txt');assert not new.exists();new.write_text(status,encoding='utf-8')
assert '?? data/knowledge/migration_r63_20261013/' in status,'Original untracked R63 folder missing'
result={'tested_tag':tag,'deployed_code_files':len(d['files']),'before_backups_verified':sum(bool(r['backup']) for r in d['files']),'protected_database_hashes_unchanged':not any('Protected DB' in x for x in errors),'delivered_candidate_matches_tested_sha256':sha(Path(delivery['candidate_path']))==verified['database_sha256'],'documents_checked':len(documents),'unique_absolute_local_links_checked':len(links),'original_untracked_r63_folder_present':True,'restart_performed':False,'portable_packages_updated':False,'errors':errors}
out=B/('ARTIFACT_QA_'+tag+'.json');assert not out.exists();out.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(result,ensure_ascii=False,indent=2));assert not errors
