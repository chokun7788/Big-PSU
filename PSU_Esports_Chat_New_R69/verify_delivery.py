"""Read-only comparison of preserved R68 and the new installation."""
import ast,collections,hashlib,json,sqlite3,sys,urllib.request
from pathlib import Path
B=Path(__file__).resolve().parent;OLD=B.parent/'r68_source_completion_20261016'
OUT=B/'verification'/(sys.argv[1] if len(sys.argv)>1 else 'delivery01');OUT.mkdir(parents=True,exist_ok=False)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def db_info(p):
 with sqlite3.connect(p.resolve().as_uri()+'?mode=ro',uri=True) as c:
  tables={}
  for name, in c.execute("select name from sqlite_master where type='table' and name not like 'sqlite_%' order by name").fetchall():
   # Names come only from SQLite schema metadata, not user input.
   rows=c.execute('select * from "'+name.replace('"','""')+'"').fetchall()
   lines=sorted(json.dumps(r,ensure_ascii=False,separators=(',',':')) for r in rows)
   tables[name]={'rows':len(rows),'logical_sha256':hashlib.sha256('\n'.join(lines).encode()).hexdigest()}
  return {'integrity_check':c.execute('pragma integrity_check').fetchone()[0],'tables':tables,'counts':dict(c.execute('select kind,count(*) from cc_heads where withdrawn=0 group by kind')),'active':dict(c.execute('select key,value from cc_meta'))['active'],'approvals':c.execute('select count(*) from cc_approvals').fetchone()[0]}
source=db_info(OLD/'candidate06.sqlite');seed=db_info(B/'seed_R68_preserved.sqlite');new=db_info(B/'system/data/knowledge/common.sqlite')
manifest=json.loads((B/'R68_SOURCE_CODE_MANIFEST.json').read_text('utf8'))
unchanged_source=all(sha(OLD/r['path'])==r['sha256'] for r in manifest)
changes=[r['path'] for r in manifest if sha(B/r['path'])!=r['sha256']]
errors=[];parsed=0
for p in (B/'system/app').rglob('*.py'):
 try:ast.parse(p.read_text('utf-8-sig'),filename=str(p));parsed+=1
 except (SyntaxError,UnicodeError) as e:errors.append({'path':str(p.relative_to(B)),'error':str(e)})
try:
 with urllib.request.urlopen('http://127.0.0.1:8101/health',timeout=3) as response:network={'health_http_status':response.status,'response':json.load(response)}
except Exception as e:
 reason=getattr(e,'reason',e)
 network={'health_http_status':None,'error_type':type(e).__name__,'reason_type':type(reason).__name__,'errno':getattr(reason,'errno',None),'winerror':getattr(reason,'winerror',None),'message':str(e),'verified_browser_chat':False}
result={'source_R68_code_unchanged':unchanged_source,'source_R68_code_files':len(manifest),'source_seed_target_all_logical_tables_equal':source['tables']==seed['tables']==new['tables'],'seed_file_unchanged':sha(B/'seed_R68_preserved.sqlite')==json.loads((B/'MIGRATION_BASELINE.json').read_text('utf8'))['seed_sha256'],'source':source,'target':new,'changed_existing_code_only_in_new_folder':changes,'python_files_parsed':parsed,'syntax_errors':errors,'local_http_check':network,'scope':'Migration consistency and syntax, not semantic correctness or owner approval'}
(OUT/'RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
docs=B/'docs';docs.mkdir(exist_ok=True)
for source_path,name in [(OLD/'FORMAT_GUIDE_R68_TH.md','FORMAT_GUIDE_R68_TH.md'),(B.parent/'r67_migration_parity_20261015/FORMAT_SPEC_R67_TH.md','FORMAT_SPEC_R67_TH.md'),(B.parent/'r67_migration_parity_20261015/OWNER_CONFIRMATION_REQUIRED_R67_TH.md','OWNER_CONFIRMATION_REQUIRED_R67_TH.md')]:
 (docs/name).write_bytes(source_path.read_bytes())
print(json.dumps({k:v for k,v in result.items() if k not in {'source','target'}},ensure_ascii=False,indent=2))
print(json.dumps({'heads':sum(new['counts'].values()),'counts':new['counts'],'active':new['active'],'approvals':new['approvals']},ensure_ascii=False))
raise SystemExit(not unchanged_source or source['tables']!=seed['tables'] or source['tables']!=new['tables'] or bool(errors))
