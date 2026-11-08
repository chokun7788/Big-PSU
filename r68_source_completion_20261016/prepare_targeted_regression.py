import shutil
from pathlib import Path
B=Path(__file__).resolve().parent;S=B.parent/'r67_migration_parity_20261015'
for name in ['RAW_RECOVERY.json','RAW_RECOVERY_LINEAGE.json']:
 shutil.copy2(S/name,B/name)
s=(S/'test_migration_behavior.py').read_text('utf8').replace("configure('common',enabled)","configure('common',enabled,db=B/'candidate04.sqlite')").replace("B/'common.sqlite'","B/'candidate04.sqlite'")
(B/'test_preserved_behavior.py').write_text(s,encoding='utf8')
s=(S/'test_owner_compatibility.py').read_text('utf8').replace("B/'common.sqlite'","B/'candidate04.sqlite'")
(B/'test_owner_compatibility.py').write_text(s,encoding='utf8')
s=(S/'test_followups.py').read_text('utf8').replace("B/'common.sqlite'","B/'candidate04.sqlite'").replace("configure('common',False)","configure('common',False,db=B/'candidate04.sqlite')").replace('FOLLOWUPS_final06.json','FOLLOWUPS_r68.json')
(B/'test_followups.py').write_text(s,encoding='utf8')
print('Prepared targeted regression tests against the R68 candidate; no legacy/full rerun')
