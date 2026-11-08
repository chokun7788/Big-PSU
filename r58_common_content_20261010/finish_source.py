import json,hashlib,shutil
from pathlib import Path
OUT=Path(__file__).resolve().parent;CAND=OUT/'system/PSU_Esports_Chatbot_Local';ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
plan=json.loads((OUT/'source_apply_plan.json').read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
updates=['app/knowledge/common/store.py','tests/test_common_content_r58.py']
for rel in updates:
    if sha(ROOT/rel)!=plan['new_files'][rel]:raise SystemExit('Source changed since our apply; no overwrite: '+rel)
    backup=OUT/'new_file_before_fix'/rel;backup.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/rel,backup)
    shutil.copy2(CAND/rel,ROOT/rel)
for p in (OUT/'docs').glob('*.md'):
    dst=ROOT/'docs/common_content_r58'/p.name
    if dst.exists() and sha(dst)!=plan['new_files']['docs/common_content_r58/'+p.name]:raise SystemExit('Owner doc changed independently: '+p.name)
    shutil.copy2(p,dst)
report={rel:{'before':plan['new_files'][rel],'after':sha(ROOT/rel)} for rel in updates}
(OUT/'source_followup_fix.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print('Final source repair and detailed report saved; original dirty source and owner data retained.')
