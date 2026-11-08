"""Preserve owner replies and attached source documents; extract without editing."""
import collections,hashlib,json,shutil,zipfile
from pathlib import Path
import xml.etree.ElementTree as ET
R=Path(__file__).resolve().parent;B=R.parent;raw=R/'sources';raw.mkdir(exist_ok=True)
files={
 'valorant':'D:/Download New/กฎระเบียบและรูปแบบการแข่งขัน VALORANT รายการ PSU Phuket VALORANT 2026 Tournament.docx',
 'cs2':'D:/Download New/กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 รายการ PSU Phuket CS2 2026 Tournament.docx',
 'rov':'D:/Download New/กติกาการแข่งขัน Arena of Valor (RoV) รายการ Blueket Games 2025 ประเภททีมชาย.docx',
 'tekken':'D:/Download New/กฎระเบียบและรูปแบบการแข่งขัน Tekken 8 รายการ PSU Esports ปะทะมันส์ สนั่นจอ.docx'}
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'};manifest=[]
for game,path in files.items():
 p=Path(path);target=raw/(game+'.docx')
 if target.exists() and target.read_bytes()!=p.read_bytes():raise RuntimeError('Source snapshot already differs: '+game)
 if not target.exists():shutil.copy2(p,target)
 with zipfile.ZipFile(target) as z:
  doc=ET.fromstring(z.read('word/document.xml'));paragraphs=[]
  for index,para in enumerate(doc.findall('.//w:p',ns),1):
   text=''.join('\t' if n.tag=='{'+ns['w']+'}tab' else '\n' if n.tag=='{'+ns['w']+'}br' else n.text or '' for n in para.iter() if n.tag in ['{'+ns['w']+'}t','{'+ns['w']+'}tab','{'+ns['w']+'}br'])
   if not text.strip():continue
   num=para.find('./w:pPr/w:numPr',ns);style=para.find('./w:pPr/w:pStyle',ns)
   paragraphs.append({'paragraph':index,'text':text,'style':style.get('{'+ns['w']+'}val') if style is not None else None,'numbering_xml':ET.tostring(num,encoding='unicode') if num is not None else None})
  media=[x for x in z.namelist() if x.startswith('word/media/')];tables=len(doc.findall('.//w:tbl',ns))
 data={'game':game,'original_path':path,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'paragraphs':paragraphs,'tables':tables,'embedded_media':media,'note':'Text extraction retains paragraph order and OOXML list metadata; embedded images are not inferred as text.'}
 (R/(game+'_EXTRACT.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2),'utf8');(R/(game+'_TEXT.txt')).write_text('\n'.join(f"[P{x['paragraph']:04}] {x['text']}" for x in paragraphs),'utf8');manifest.append({k:v for k,v in data.items() if k!='paragraphs'}|{'paragraph_count':len(paragraphs)})
form=B/'r107_owner_questions_20261020'
for name in ['simple_questions.json','responses/simple_answers.json','responses/simple_events.jsonl','responses/answers.json','QUESTION_UPDATES.json']:
 source=form/name;dest=R/('BEFORE_'+name.replace('/','__'))
 if source.exists() and not dest.exists():shutil.copy2(source,dest)
(R/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),'utf8')
print(json.dumps([{k:x[k] for k in ['game','paragraph_count','tables','embedded_media']} for x in manifest],ensure_ascii=False))
