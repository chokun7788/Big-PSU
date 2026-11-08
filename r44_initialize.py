import hashlib,json,shutil,uuid,zipfile,xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
BASE=Path(__file__).resolve().parent;ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
SOURCE=Path(r'D:\Download New\ค่าบริการครึ่งวันและเต็มวัน PSU Esports Studio - Phuket (1).xlsx')
OUT=BASE/('r44_package_fees_'+datetime.now().strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6]);OUT.mkdir()
with (BASE/'r44_current_path.txt').open('x',encoding='utf-8') as f:f.write(str(OUT))
hashes={}
for folder in ('app','web_chat','deployment_templates','tests','data/curated'):
 for p in (ROOT/folder).rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts:
   rel=p.relative_to(ROOT);dest=OUT/'before'/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest);hashes[rel.as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
for rel in ('booking_dashboard/center_schedule.json','app/calculator/service_fee.py','data/competition_rules/competition_rule_chunks.jsonl','data/competition_rules/review/competition_rule_claim_v2_review_queue.jsonl'):
 hashes[rel]=hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()
with (OUT/'before_manifest.json').open('x',encoding='utf-8') as f:json.dump(hashes,f,indent=2)
shutil.copy2(SOURCE,OUT/SOURCE.name)
NS={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(SOURCE) as z:
 shared=[]
 if 'xl/sharedStrings.xml' in z.namelist():
  for si in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',NS):shared.append(''.join(t.text or '' for t in si.findall('.//m:t',NS)))
 sheets=ET.fromstring(z.read('xl/workbook.xml')).findall('m:sheets/m:sheet',NS)
 relationships={r.attrib['Id']:r.attrib['Target'] for r in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
 rows=[]
 for sheet in sheets:
  rid=sheet.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'];target=relationships[rid];target=target.lstrip('/') if target.startswith('/') else 'xl/'+target
  xml=ET.fromstring(z.read(target));entries=[]
  for row in xml.findall('m:sheetData/m:row',NS):
   cells=[]
   for cell in row.findall('m:c',NS):
    value=cell.findtext('m:v',default='',namespaces=NS);kind=cell.attrib.get('t','')
    if kind=='s':value=shared[int(value)] if value else ''
    elif kind=='inlineStr':value=''.join(t.text or '' for t in cell.findall('.//m:t',NS))
    formula=cell.findtext('m:f',default='',namespaces=NS)
    if value or formula:cells.append(dict(cell=cell.attrib['r'],value=value,formula=formula))
   if cells:entries.append(cells)
  rows.append(dict(sheet=sheet.attrib['name'],dimension=xml.find('m:dimension',NS).attrib if xml.find('m:dimension',NS) is not None else None,merges=[m.attrib['ref'] for m in xml.findall('m:mergeCells/m:mergeCell',NS)],rows=entries))
 images=[]
 for name in z.namelist():
  if name.startswith('xl/media/'):
   path=OUT/'media'/Path(name).name;path.parent.mkdir(exist_ok=True);path.write_bytes(z.read(name));images.append(str(path))
 result=dict(source=str(SOURCE),sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),sheets=rows,images=images,other_parts=[n for n in z.namelist() if any(k in n for k in ('comment','drawing','vml'))])
 with (OUT/'WORKBOOK_EXTRACTION.json').open('x',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
 print(OUT)
 for sheet in rows:
  print('SHEET',sheet['sheet'],sheet['dimension'],'MERGES',sheet['merges'])
  for row in sheet['rows']:print(json.dumps(row,ensure_ascii=False))
 print('IMAGES',images,'OTHER',result['other_parts'])
