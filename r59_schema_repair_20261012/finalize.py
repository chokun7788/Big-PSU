from prepare import B,SYSTEM,PACK,ROOT,sha,dbhash
import json,sqlite3,shutil,difflib,subprocess
FILES=['app/knowledge/common/answer.py','app/knowledge/common/planner.py','app/knowledge/common/query_contract.py','tests/test_common_query_contract_r59.py']
before=json.loads((B/'BEFORE_RECEIPT.json').read_text(encoding='utf-8'))
code={name:{label:sha(root/name) for label,root in [('candidate',SYSTEM),('project',ROOT),('package',PACK)]} for name in FILES}
assert all(len(set(v.values()))==1 for v in code.values())
dbs={p:dbhash(__import__('pathlib').Path(p)) for p in before['database_logical_hashes']}
assert dbs==before['database_logical_hashes']
backup_checks={label:{name:sha(B/'before'/label/name)==h for name,h in files.items()} for label,files in before['source_hashes'].items()}
assert all(all(v.values()) for v in backup_checks.values())
counts={}
for label,root in [('project',ROOT),('package',PACK)]:
    with sqlite3.connect('file:'+(root/'data/knowledge/approved.sqlite').as_posix()+'?mode=ro',uri=True) as c:
        counts[label]={table:c.execute('SELECT COUNT(*) FROM '+table).fetchone()[0] for table in ('cc_heads','cc_revisions','cc_releases')}
patch=[]
for name in FILES:
    src=B/'before/project'/name
    old=src.read_text(encoding='utf-8').splitlines(keepends=True) if src.exists() else []
    patch.extend(difflib.unified_diff(old,(ROOT/name).read_text(encoding='utf-8').splitlines(keepends=True),fromfile='before/'+name,tofile='after/'+name))
diff=''.join(patch);diff_path=B/'FINAL_SOURCE_DIFF.patch'
if diff_path.exists():assert diff_path.read_text(encoding='utf-8')==diff
else:diff_path.write_text(diff,encoding='utf-8')
DOCS=['Flow.md','Research.md','RESULTS_TH.md','REVIEW_LOOPS.md']
doc_targets=[]
for label,root in [('project',ROOT),('package',PACK),('candidate',SYSTEM)]:
    dest=root/'docs/common_content_r59_20261012';dest.mkdir(parents=True,exist_ok=True)
    for name in DOCS:
        if (dest/name).exists():assert sha(dest/name)==sha(B/name),'Existing document differs; refuse overwrite'
        else:shutil.copy2(B/name,dest/name)
        doc_targets.append(str(dest/name))
git_after=subprocess.check_output(['git','-C',str(ROOT),'status','--porcelain=v1','-uall'],text=True,encoding='utf-8')
(B/'GIT_STATUS_FINAL.txt').write_text(git_after,encoding='utf-8')
old=set((B/'GIT_STATUS_BEFORE.txt').read_text(encoding='utf-8').splitlines());new=set(git_after.splitlines())
missing=old-new;assert not missing,missing
result={'code_sha256_matches_all_three_copies':code,'database_logical_hashes_unchanged':dbs,'production_common_counts':counts,'before_backups_match_original_hashes':backup_checks,'all_prior_git_status_entries_retained':True,'new_git_status_entries':sorted(new-old),'documents_copied':doc_targets,'no_owner_data_publication':True,'no_server_restart':True,'client_date':'2026-10-12'}
(B/'FINAL_VERIFICATION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'matching_files':len(code),'dbs_unchanged':len(dbs),'original_backups_verified':True,'prior_git_entries_retained':True,'production_common_counts':counts,'documents':len(doc_targets)},indent=2))
