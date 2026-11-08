"""Apply a review finding only after HTTP01 ends; preserve its exact system."""
import hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';OUT=R/'http01'
done=json.loads((OUT/'TEST_COMPLETE.json').read_text('utf8'));assert done['complete']
freeze=json.loads((OUT/'RUN_FREEZE.json').read_text('utf8'))['files']
assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in freeze.items())
shutil.copytree(S,OUT/'FROZEN_SYSTEM',ignore=shutil.ignore_patterns('__pycache__','*.pyc','*-wal','*-shm'))
p=S/'app/knowledge/common/domain_flow/readers.py';src=p.read_text('utf8');before=hashlib.sha256(src.encode()).hexdigest()
block="""    if cat not in {'C06','C07','C11','C12','C13'}:
        from .legacy_profile import plan as source_profile
        profiled=source_profile(index,cat,q)
        if profiled is not None:return profiled
"""
assert src.count(block)==1
src=src.replace(block,'')
needle="    return field_reader(index,cat,q,at)\n"
replacement="""    result=field_reader(index,cat,q,at)
    # Exact typed fields/relations and locked guards take precedence over an
    # older broad query profile. Profiles recover unresolved wording only.
    if result.ids or result.locked:return result
    if cat not in {'C06','C07','C11','C12','C13'}:
        from .legacy_profile import plan as source_profile
        profiled=source_profile(index,cat,q)
        if profiled is not None:return profiled
    return result
"""
assert src.count(needle)==1;src=src.replace(needle,replacement);p.write_text(src,'utf8')
renderer=S/'app/knowledge/common/domain_flow/engine.py';body=renderer.read_text('utf8')
line='            blocks.append(f"{f[\'subject\'][lang]} — {f[\'label\'][lang]}: {shown} [S{len(blocks)+1}]")'
new='''            subject=f['subject'][lang]
            if f.get('legacy_search') and re.search(r'\\.\\*|\\(\\?:|\\\\[wsdb]|\\|',subject):subject=''
            prefix=(subject+' — ') if subject else ''
            blocks.append(f"{prefix}{f['label'][lang]}: {shown} [S{len(blocks)+1}]")'''
assert body.count(line)==1;renderer.write_text(body.replace(line,new),'utf8')
(R/'REVISION02_CHANGE.json').write_text(json.dumps({'finding':'A broad legacy PC equipment regex profile preempted an exact Gaming Chair zone field. Native field/relationship answers now precede legacy wording fallback; internal pattern-only titles are hidden from customer text.','path':str(p),'before_sha256':before,'after_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'presentation_path':str(renderer),'data_changed':False,'http01_frozen_system_preserved':True},ensure_ascii=False,indent=2),'utf8')
runner=(R/'run_http.py').read_text('utf8').replace("OUT=R/'http01'","OUT=R/'http02'").replace("'run_http.py','BASELINE_CHECK_V2.json'","'run_http.py','run_http02.py','BASELINE_CHECK_V2.json'")
(R/'run_http02.py').write_text(runner,'utf8')
print('Exact HTTP01 system archived; revision02 prioritizes typed fields and hides pattern-only titles.')
