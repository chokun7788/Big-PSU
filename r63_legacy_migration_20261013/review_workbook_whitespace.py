import copy,json
from pathlib import Path
OUT=Path(__file__).resolve().parent
raw=json.loads((OUT/'WORKBOOK_CHECK.json').read_text(encoding='utf-8'))
reviewed=copy.deepcopy(raw)
for c in reviewed['checks']:
 if not c['passed'] and isinstance(c.get('expected'),str) and isinstance(c.get('actual'),str):
  c['passed']=c['actual'].strip()==c['expected'].strip()
  c['review']='Trim outer whitespace only; original cell retained in raw check and archived workbook'
reviewed['passed']=sum(c['passed'] for c in reviewed['checks'])
(OUT/'WORKBOOK_REVIEWED.json').write_text(json.dumps(reviewed,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'passed':reviewed['passed'],'total':reviewed['total']}))
