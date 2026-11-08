import ast,difflib,hashlib,json,sqlite3,sys
from pathlib import Path
B=Path(__file__).resolve().parent;m=json.loads((B/'BASELINE_MANIFEST.json').read_text(encoding='utf8'));src=Path(m['source'])
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
changed=[f['path'] for f in m['files'] if not (src/'system'/f['path']).is_file() or sha(src/'system'/f['path'])!=f['sha256']]
def tables(p):
    c=sqlite3.connect(p.as_uri()+'?mode=ro',uri=True);out={}
    try:
        for name,sql in c.execute("select name,sql from sqlite_master where type='table' and name not like 'sqlite_%' order by name"):
            rows=sorted(json.dumps([x.hex() if isinstance(x,bytes) else x for x in r],ensure_ascii=False,separators=(',',':')) for r in c.execute('select * from "'+name.replace('"','""')+'"'))
            out[name]={'rows':len(rows),'schema':sql,'sha256':hashlib.sha256('\n'.join(rows).encode()).hexdigest()}
    finally:c.close()
    return out
a=src/'system/data/knowledge/common.sqlite';b=B/'system/data/knowledge/common.sqlite';ta,tb=tables(a),tables(b)
diff=[];code=[]
for p in sorted((B/'system/app').rglob('*.py')):
    if 'vendor' in p.parts:continue
    rel=p.relative_to(B/'system');old=src/'system'/rel
    if old.exists() and sha(p)==sha(old):continue
    new=p.read_text(encoding='utf8');ast.parse(new,filename=str(p));code.append(rel.as_posix())
    diff.extend(difflib.unified_diff(old.read_text(encoding='utf8').splitlines(True) if old.exists() else [],new.splitlines(True),fromfile='R74/system/'+rel.as_posix(),tofile='R75/system/'+rel.as_posix()))
result={'source':str(src),'source_manifest_count':len(m['files']),'source_files_changed':changed,'logical_tables_equal':ta==tb,
    'database_source_sha256':sha(a),'database_copy_sha256':sha(b),'tables':tb,'changed_code_syntax_checked':code,
    'heads':tb['cc_heads']['rows'],'approvals':tb['cc_approvals']['rows'],'real_model_inference_verified':False}
suffix='_'+sys.argv[1] if len(sys.argv)>1 else ''
with (B/('DELIVERY_QA'+suffix+'.json')).open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
with (B/('CHANGESET'+suffix+'.patch')).open('x',encoding='utf8') as f:f.writelines(diff)
print(json.dumps({k:v for k,v in result.items() if k!='tables'}));raise SystemExit(bool(changed) or ta!=tb)
