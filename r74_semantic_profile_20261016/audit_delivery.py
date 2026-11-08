"""Preservation audit, stored-result regrading, and readable code diff."""
import difflib,hashlib,json,sqlite3,sys
from pathlib import Path
B=Path(__file__).resolve().parent;manifest=json.loads((B/'BASELINE_MANIFEST.json').read_text(encoding='utf8'));src=Path(manifest['source'])
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
changed=[f['path'] for f in manifest['files'] if not (src/'system'/f['path']).is_file() or sha(src/'system'/f['path'])!=f['sha256']]
def serial(x):return x.hex() if isinstance(x,bytes) else x
def tables(path):
    c=sqlite3.connect(path.as_uri()+'?mode=ro',uri=True)
    try:
        result={}
        for name,sql in c.execute("select name,sql from sqlite_master where type='table' and name not like 'sqlite_%' order by name"):
            quoted='"'+name.replace('"','""')+'"'
            rows=sorted(json.dumps([serial(v) for v in row],ensure_ascii=False,separators=(',',':')) for row in c.execute('select * from '+quoted))
            result[name]={'rows':len(rows),'schema':sql,'sha256':hashlib.sha256('\n'.join(rows).encode()).hexdigest()}
        return result
    finally:c.close()
left=src/'system/data/knowledge/common.sqlite';right=B/'system/data/knowledge/common.sqlite'
before=tables(left);after=tables(right)
sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import validate
store=CommonStore(right)
with store.connect() as c:
    records=store.heads(c);sources=store.sources(c)
    errors={rid:validate(r,records,sources) for rid,r in records.items() if validate(r,records,sources)}
    meta=dict(c.execute('select key,value from cc_meta'))
    approvals=c.execute('select count(*) from cc_approvals').fetchone()[0]
qa={'source':str(src),'source_manifest_count':len(manifest['files']),'source_files_changed':changed,
    'source_database_sha256':sha(left),'copied_database_sha256':sha(right),
    'logical_tables_equal':before==after,'logical_tables_source':before,'logical_tables_copy':after,
    'heads':len(records),'schema_errors':errors,'approvals':approvals,'actual_active_release':meta.get('active'),
    'old_facts_revisions_sources_metadata_unchanged':before==after,'model_inference_verified':False,
    'new_schema_or_data_migration':False}
with (B/'DELIVERY_QA.json').open('x',encoding='utf8') as f:json.dump(qa,f,ensure_ascii=False,indent=2)

# Same stored answers, corrected oracle. No new requests or changed old logs.
from payment_boundary_cases import CASES
for tag in ('baseline_boundary01','boundary01','boundary02'):
    old=[json.loads(line) for line in (B/'results'/tag/'ANSWERS.jsonl').read_text(encoding='utf8').splitlines()]
    reviewed=[]
    for row,case in zip(old,CASES):
        assert row['question']==case['question']
        a=row['answer'];hits={h.get('record_id') for h in row['hits']};errors=[]
        errors += ['missing:'+x for x in case['need'] if x.casefold() not in a.casefold()]
        errors += ['forbidden:'+x for x in case['forbid'] if x.casefold() in a.casefold()]
        if case.get('expected_source') not in (None,*hits):errors.append('missing_expected_source')
        if case.get('expected_sources_any') and not hits&set(case['expected_sources_any']):errors.append('missing_any_expected_source')
        if case.get('expected_topic') and row['artifact'].get('query_plan',{}).get('unconfirmed_topic')!=case['expected_topic']:errors.append('wrong_topic')
        if 'validation_rejected' in row['errors']:errors.append('validation_rejected')
        if row['artifact'].get('migration',{}).get('legacy_fallback_used') is not False:errors.append('legacy_fallback_status')
        reviewed.append({'index':row['index'],'locale':case['locale'],'question':case['question'],'original_passed':row['passed'],
            'original_errors':row['errors'],'reviewed_passed':not errors,'reviewed_errors':errors})
    result={'source_results':tag,'new_requests':0,'count':len(reviewed),'passed':sum(r['reviewed_passed'] for r in reviewed),
        'by_language':{lang:{'count':sum(r['locale']==lang for r in reviewed),'passed':sum(r['locale']==lang and r['reviewed_passed'] for r in reviewed)} for lang in ('th','en')},
        'oracle_correction':'Accept either of the two source-backed bank_account FAQ records; deadline record ID corrected. Content requirements unchanged.',
        'cases':reviewed}
    with (B/'results'/tag/'ORACLE_REVIEW.json').open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
diff=[];changes=[]
for p in sorted((B/'system').rglob('*')):
    if not p.is_file() or p.suffix not in {'.py','.html','.js','.json'} or '__pycache__' in p.parts:continue
    rel=p.relative_to(B/'system');previous=src/'system'/rel
    old=previous.read_text(encoding='utf8') if previous.exists() else ''
    new=p.read_text(encoding='utf8')
    if old!=new:
        changes.append(rel.as_posix())
        diff.extend(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='R73/system/'+rel.as_posix(),tofile='R74/system/'+rel.as_posix()))
with (B/'CHANGESET.patch').open('x',encoding='utf8') as f:f.writelines(diff)
with (B/'CODE_CHANGE_SUMMARY.json').open('x',encoding='utf8') as f:json.dump({'system_files_changed':changes,'source_unchanged':not changed},f,indent=2)
print(json.dumps({'source_files_changed':changed,'logical_tables_equal':before==after,'heads':len(records),'schema_errors':len(errors),'approvals':approvals,'active':meta.get('active'),'changed_code':changes},ensure_ascii=False))
raise SystemExit(bool(changed) or before!=after or bool(qa['schema_errors']))
