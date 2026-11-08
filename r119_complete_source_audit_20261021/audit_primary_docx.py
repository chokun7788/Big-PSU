"""Read-only OOXML paragraph/text audit against executable native rule text."""
import hashlib,json,re,sqlite3,unicodedata,xml.etree.ElementTree as ET,zipfile
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system'
db=sqlite3.connect((S/'data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
records={rid:json.loads(p) for rid,p in db.execute('SELECT h.record_id,r.payload FROM cc_heads h JOIN cc_revisions r ON h.record_id=r.record_id AND h.head=r.version WHERE h.withdrawn=0')}
value=lambda r,k:r.get('fields',{}).get(k,{}).get('value')
def text(v):
 if isinstance(v,str):return v
 if isinstance(v,dict):return '\n'.join(text(x) for x in v.values())
 if isinstance(v,list):return '\n'.join(text(x) for x in v)
 return ''
def norm(s):return re.sub(r'\s|[\u200b\ufeff\u00ad]','',unicodedata.normalize('NFKC',s))
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
files=list(Path('D:/Download New').glob('*.docx'));rows=[]
for token,ident in [('VALORANT','competition_competition_rules_valorant_psu_phuket_2026'),('Counter-Strike 2','competition_competition_rules_cs2_psu_phuket_2026'),('Arena of Valor','competition_competition_rules_rov_blueket_2025_men'),('Tekken 8','competition_competition_rules_tekken8_psu_esports')]:
 candidates=[p for p in files if token in p.name];assert len(candidates)==1
 p=candidates[0];raw=p.read_bytes();h=hashlib.sha256(raw).hexdigest()
 with zipfile.ZipFile(p) as z:doc=ET.fromstring(z.read('word/document.xml'))
 paras=[''.join(n.text or '' for n in par.findall('.//w:t',ns)) for par in doc.findall('.//w:p',ns)]
 paras=[s for s in paras if s.strip()]
 native=[r for r in records.values() if r['kind']=='competition_rule' and value(r,'competition_id')==ident]
 assert native,(token,ident)
 body='\n'.join(text(value(r,k)) for r in native for k in ['heading','text']);normalized=norm(body)
 check=[{'paragraph':i+1,'text':s,'present_in_native_rule_text':norm(s) in normalized} for i,s in enumerate(paras)]
 rows.append({'path':str(p),'sha256':h,'native_competition_id':ident,'native_clauses':len(native),'paragraphs':len(paras),'matched':sum(c['present_in_native_rule_text'] for c in check),'paragraph_checks':check,'source_file_unchanged':hashlib.sha256(p.read_bytes()).hexdigest()==h})
result={'files':rows,'documents_checked':len(rows),'paragraphs_checked':sum(r['paragraphs'] for r in rows),'matched':sum(r['matched'] for r in rows),'unmatched':[{'path':r['path'],**c} for r in rows for c in r['paragraph_checks'] if not c['present_in_native_rule_text']],'scope':'Text/run content and table-cell paragraphs only; no layout approval or rendering claim; original DOCX files untouched.'}
(R/'PRIMARY_DOCX_AUDIT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({k:v for k,v in result.items() if k!='files'},ensure_ascii=False))
