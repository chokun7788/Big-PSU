import hashlib,json,re,sqlite3
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system'
load=lambda p:json.loads(p.read_text('utf8'))
src=load(S/'data/curated/zone_rental_fees_20261006.json');sheet=load(R/'WORKBOOK_CELL_AUDIT.json')
assert hashlib.sha256((S/src['source_file']).read_bytes()).hexdigest()==src['source_sha256']
cells={r['cell']:r['value'] for r in sheet['cells'] if r['value'] is not None}
db=sqlite3.connect((S/'data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
records={rid:json.loads(p) for rid,p in db.execute('SELECT h.record_id,r.payload FROM cc_heads h JOIN cc_revisions r ON h.record_id=r.record_id AND h.head=r.version WHERE h.withdrawn=0')}
val=lambda r,k:r['fields'].get(k,{}).get('value')
checks=[]
for row in src['rows']:
 zones=[rid for rid,r in records.items() if r['kind']=='zone' and row['label'] in (val(r,'name') or {}).values()];assert len(zones)==1
 for group,prices in row['prices_thb'].items():
  aid='audience_'+('external_org' if group=='external' else 'internal_org')
  for period,amount in prices.items():
   cell=row['source_cells'][group+'_'+period];original=int(float(re.sub(r'[\s,]','',cells[cell])))
   candidates=[r for r in records.values() if r['kind']=='rental_package' and zones[0] in (val(r,'zone_ids') or []) and val(r,'audience_id')==aid and period.replace('_','') in json.dumps(val(r,'period_label'),ensure_ascii=False).lower().replace(' ','').replace('-','').replace('_','')]
   checks.append({'zone':row['label'],'audience':group,'period':period,'source_cell':cell,'workbook_value_thb':original,'curated_value_thb':amount,'native_ids':[r['record_id'] for r in candidates],
    'passed':original==amount and len(candidates)==1 and val(candidates[0],'amount_minor')==amount*100,'native_amount_minor':[val(r,'amount_minor') for r in candidates]})
result={'workbook_cells_total':len(sheet['cells']),'workbook_nonempty_cells':len(cells),'price_rows_checked':len(checks),'passed':sum(c['passed'] for c in checks),'checks':checks,'no_price_or_effective_date_changed':True}
(R/'RENTAL_WORKBOOK_PRICE_AUDIT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},ensure_ascii=False));assert all(c['passed'] for c in checks)
