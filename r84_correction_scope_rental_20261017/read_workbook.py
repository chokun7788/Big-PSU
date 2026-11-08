"""Read only OOXML source extraction. Does not export/change the workbook."""
import hashlib,json,sqlite3,zipfile,xml.etree.ElementTree as ET
from pathlib import Path
B=Path(__file__).resolve().parent
source=Path('D:/Download New/ค่าบริการครึ่งวันและเต็มวัน PSU Esports Studio - Phuket (1).xlsx')
archived=B.parent/'r78_web_session_check_20261016/system/data/sources/zone_rental_fees_20261006.xlsx'
ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(source) as z:
 shared=[]
 if 'xl/sharedStrings.xml' in z.namelist():shared=[''.join(n.itertext()) for n in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',ns)]
 sheets=ET.fromstring(z.read('xl/workbook.xml')).findall('m:sheets/m:sheet',ns)
 cells={}
 for cell in ET.fromstring(z.read('xl/worksheets/sheet1.xml')).findall('.//m:c',ns):
  v=cell.find('m:v',ns);val=v.text if v is not None else ''
  if cell.get('t')=='s':val=shared[int(val)]
  elif cell.get('t')=='inlineStr':val=''.join(cell.find('m:is',ns).itertext())
  elif val:
   try:val=float(val);val=int(val) if val.is_integer() else val
   except ValueError:pass
  cells[cell.get('r')]=val
out={'source_path':str(source),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'sheet_names':[s.get('name') for s in sheets],'cells':cells,'archived_exists':archived.exists(),'archived_sha256':hashlib.sha256(archived.read_bytes()).hexdigest() if archived.exists() else None}
(B/'WORKBOOK_SOURCE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({**out,'cells':{k:v for k,v in cells.items() if v!=''}},ensure_ascii=False))
