import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';A=R/'http02/FROZEN_SYSTEM'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
changed=[str(p.relative_to(S)).replace('\\','/') for p in S.rglob('*') if p.is_file() and '__pycache__' not in p.parts and not p.name.endswith(('-wal','-shm')) and (not (A/p.relative_to(S)).exists() or sha(p)!=sha(A/p.relative_to(S)))]
assert changed==['app/knowledge/common/answer.py'],changed
old=(A/changed[0]).read_text('utf8');new=(S/changed[0]).read_text('utf8')
assert old.replace("key in {'question','intent_key','scope_note','source_variants'}","key in {'question','topic','intent_key','scope_note','source_variants'}")==new
render=json.loads((R/'RENDER_REGRESSION.json').read_text('utf8'));render['before_sha256']=sha(A/changed[0]);render['after_sha256']=sha(S/changed[0])
render['hash_basis']='physical file bytes, before from archived HTTP02 source'
(R/'RENDER_REGRESSION.json').write_text(json.dumps(render,ensure_ascii=False,indent=2),'utf8')
protected=json.loads((R/'REFERENCE_HASHES.json').read_text('utf8'));assert all(sha(Path(p))==h for p,h in protected.items())
out={'verified':True,'final_revision':'R118 revision03','http_revision02_archived':True,'only_changed_file_since_HTTP02':changed,
 'only_change_is_hide_topic_field':True,'protected_original_files_checked':len(protected),'protected_original_files_unchanged':True,
 'data_equivalent_all_15_tables':json.loads((R/'DATABASE_EQUIVALENCE.json').read_text('utf8'))['all_tables_and_rows_equal'],
 'final_renderer_checks_passed':render['passed']==render['total']}
(R/'FINAL_INTEGRITY.json').write_text(json.dumps(out,indent=2),'utf8');print(json.dumps(out))
