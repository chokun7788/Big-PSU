"""Reuse retained integration contracts against this candidate, not the baseline."""
from pathlib import Path
import shutil
R=Path(__file__).resolve().parent;B=R.parent/'r106_complete_flow_20261020'
for name in ['scenario_support.py','test_owner_lifecycle.py','test_http_contracts.py','test_live_bindings.py']:
    target=R/name
    if target.exists():continue
    s=(B/name).read_text('utf8')
    if name=='test_http_contracts.py':
        s=s.replace("'common-r102-complete-contract-flow'","'common-r114-domain-flow'")
        s=s.replace("health.get('common_loaded_build',{}).get('build_id')=='common-r114-domain-flow'","health.get('common_loaded_build',{}).get('build_id')=='common-r114-domain-flow'")
    target.write_text(s,'utf8')
(R/'fixtures').mkdir(exist_ok=True)
if not (R/'fixtures/BASE_SYNTHETIC.sqlite').exists():shutil.copy2(B/'fixtures/BASE_SYNTHETIC.sqlite',R/'fixtures/BASE_SYNTHETIC.sqlite')
print('Retained owner/HTTP integration contracts copied; only expected candidate build ID changed.')
