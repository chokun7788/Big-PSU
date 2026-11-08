from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent/'r123_contract_execution_20261023'
src=(P/'verify_foundation05.py').read_text('utf8').replace("S=R/'revision05_system'","S=R/'revision03_system'")
src=src.replace("load(R/'LINEAGE.json')['database_sha256']","freeze[str((S/'data/knowledge/common.sqlite').resolve())]")
# Retained foundation gates, with all prior fixtures and prior labels preserved.
assert "S=R/'revision03_system'" in src
(R/'verify_foundation.py').write_text(src,'utf8')
print('Prepared existing source/graph/plan gates against R124 revision03')
