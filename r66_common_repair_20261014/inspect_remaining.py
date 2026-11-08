import sys,json,re
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value
s=CommonStore(B/'common.sqlite')
with s.connect() as c:records=s.heads(c)
bad=[]
def walk(v,path):
 if isinstance(v,dict):
  if set(v)=={'th','en'} and isinstance(v.get('en'),str):
   try:j=json.loads(v['en'])
   except ValueError:j=None
   if isinstance(j,(dict,list)):bad.append({'record_id':rid,'kind':r['kind'],'field':field,'path':path,'th':v['th'],'en':v['en']})
  else:
   for k,x in v.items():walk(x,path+[k])
 elif isinstance(v,list):
  for i,x in enumerate(v):walk(x,path+[i])
for rid,r in records.items():
 for field,f in r['fields'].items():walk(f['value'],[])
print('STRUCTURED_TRANSLATION_ERRORS',json.dumps(bad,ensure_ascii=False,indent=2))
(B/'STRUCTURED_TRANSLATION_REVIEW.json').write_text(json.dumps(bad,ensure_ascii=False,indent=2),encoding='utf-8')
for rid,r in records.items():
 if r['kind'] not in {'competition_rule','faq','policy'}:continue
 title=value(r,'heading') or value(r,'question') or value(r,'subject')
 txt=value(r,'text') or value(r,'answer') or value(r,'details')
 raw=json.dumps([title,txt],ensure_ascii=False)
 if re.search(r'1-1|สูงสุด 3 Sessions|มาถึงสนามแข่ง|must arrive|30 minutes before|กินดื่ม|ภาชนะที่ปิด|macro',raw,re.I):print('RELEVANT_SOURCE',rid,raw)
