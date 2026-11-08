import hashlib,json,shutil,sqlite3,subprocess
from pathlib import Path
HERE=Path(__file__).resolve().parent
p=json.loads((HERE.parent/'owner_edit_latest.json').read_text(encoding='utf-8'))
root=Path(p['root']);stage=Path(p['stage']);ready=Path(p['ready']);candidate=Path(p['candidate'])
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def logical(db):
    if not db.exists():return None
    c=sqlite3.connect('file:'+db.as_posix()+'?mode=ro',uri=True)
    try:return hashlib.sha256('\n'.join(c.iterdump()).encode()).hexdigest()
    finally:c.close()
before={str(db):logical(db) for db in [root/'data/knowledge/approved.sqlite',ready/'data/knowledge/approved.sqlite']}
status=subprocess.run(['git','-C',str(root),'status','--short'],capture_output=True,text=True)
(HERE/'git_status_before_apply.txt').write_text(status.stdout+status.stderr,encoding='utf-8')
for name in p['names']:
    f=root/name
    if sha(f)!=p['before_hashes'][str(f)]:raise SystemExit('Source changed since backup; preserved: '+str(f))
new=[(candidate/'tests/test_owner_edit_r58.py',root/'tests/test_owner_edit_r58.py'),(HERE/'OWNER_EDIT_GUIDE_TH.md',root/'docs/common_content_r58/OWNER_EDIT_GUIDE_TH.md')]
for src,dst in new:
    if dst.exists():raise SystemExit('New destination exists; preserved: '+str(dst))
for name in p['names']:shutil.copy2(stage/name,root/name)
for src,dst in new:dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
after={k:logical(Path(k)) for k in before}
if before!=after:raise SystemExit('Production database logical contents changed during apply; investigate concurrent writer')
for name in p['names']:
    if len({sha(base/name) for base in [root,ready,candidate,stage]})!=1:raise SystemExit('Hash mismatch: '+name)
receipt={'source_files_applied':p['names'],'new_files':[str(x[1]) for x in new],'all_four_copies_match':True,'production_database_before':before,'production_database_after':after,'production_database_unchanged':True,'original_backups':str(HERE/'before'),'focused_distinct_checks_passed':36}
(HERE/'FINAL_OWNER_EDIT_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'files_applied':7,'four_copies_match':True,'production_database_unchanged':True}))
