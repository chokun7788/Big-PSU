from prepare import B,SYSTEM,ROOT,PACK,sha
import json,shutil
prior=json.loads((B/'PROPAGATION_RECEIPT.json').read_text(encoding='utf-8'))
expected={r['target']:r['sha256'] for r in prior['copied']}
rows=[]
for label,root in [('project',ROOT),('package',PACK)]:
    for name in ['app/knowledge/common/query_contract.py','tests/test_common_query_contract_r59.py']:
        target=root/name;assert sha(target)==expected[str(target)],'Deployed file changed outside this task'
        backup=B/'before_final_thai_guard'/label/name;backup.parent.mkdir(parents=True,exist_ok=True)
        assert not backup.exists();shutil.copy2(target,backup);shutil.copy2(SYSTEM/name,target)
        rows.append({'target':str(target),'before_sha256':expected[str(target)],'sha256':sha(target),'backup':str(backup)})
(B/'THAI_GUARD_PROPAGATION.json').write_text(json.dumps(rows,indent=2),encoding='utf-8');print(rows)
