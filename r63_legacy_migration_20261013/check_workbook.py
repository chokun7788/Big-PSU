import hashlib,json,sys
from pathlib import Path
import openpyxl
OUT=Path(sys.argv[1])
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
data=json.loads((ROOT/'data/curated/zone_rental_fees_20261006.json').read_text(encoding='utf-8'))
p=ROOT/data['source_file'];wb=openpyxl.load_workbook(p,read_only=True,data_only=True);ws=wb[data['source_sheet']]
checks=[]
checks.append({'item':'original_workbook_sha256','passed':hashlib.sha256(p.read_bytes()).hexdigest()==data['source_sha256']})
for row in data['rows']:
 for group,prices in row['prices_thb'].items():
  for period,amount in prices.items():
   cell=row['source_cells'][group+'_'+period];actual=ws[cell].value
   checks.append({'item':row['id']+' '+group+' '+period,'cell':cell,'expected':amount,'actual':actual,'passed':actual==amount})
 for key in ['seats','equipment']:
  cell=row['source_cells'][key];expected=row['seats'] if key=='seats' else row['equipment_th'];actual=ws[cell].value
  checks.append({'item':row['id']+' '+key,'cell':cell,'expected':expected,'actual':actual,'passed':actual==expected})
for note in data['source_notes']:checks.append({'item':'note '+note['cell'],'actual':ws[note['cell']].value,'expected':note['text_th'],'passed':ws[note['cell']].value==note['text_th']})
wb.close()
result={'passed':sum(x['passed'] for x in checks),'total':len(checks),'checks':checks}
(OUT/'WORKBOOK_CHECK.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}))
if not all(x['passed'] for x in checks):raise SystemExit(1)
