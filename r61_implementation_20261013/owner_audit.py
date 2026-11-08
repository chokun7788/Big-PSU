from pathlib import Path
import json,sys
from prepare import B,SYSTEM,ROOT
sys.path.insert(0,str(SYSTEM))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import validate,CATALOG
store=CommonStore(ROOT/'data/knowledge/approved.sqlite');snap=store.snapshot()
with store.connect() as c:records=store.heads(c);sources=store.sources(c)
items=[]
for rid,r in sorted(records.items()):
 errors=validate(r,records,sources,publish=True,demo=False)
 unknown=[f['key'] for f in CATALOG[r['kind']]['fields'] if r['fields'][f['key']]['status']!='known']
 values={key:{'status':f['status'],'value':f['value'],'evidence_refs':f['evidence_refs']} for key,f in r['fields'].items()}
 questions=[]
 for error in errors:
  if 'validity' in error.lower() or 'Time-sensitive' in error:questions.append('รายการ '+rid+' เริ่มมีผลวัน/เวลาใด และสิ้นสุดเมื่อใดถ้ามี?')
  else:questions.append('รายการ '+rid+': กรุณายืนยันหรือเติม '+error)
 items.append({'record_id':rid,'kind':r['kind'],'revision':r['revision'],'publication_errors':errors,'unknown_or_nonapplicable':unknown,'fields_for_review':values,'specific_questions':list(dict.fromkeys(questions)),'approval_required_before_publish':True})
out={'read_only':True,'production_facts_not_changed':True,'heads':len(items),'active_release':snap['active'],'epoch':snap['epoch'],'items':items}
with (B/'OWNER_REVIEW_PACKET.json').open('x',encoding='utf-8') as f:json.dump(out,f,ensure_ascii=False,indent=2)
text='# รายการตรวจข้อมูลเจ้าของ — อ่านอย่างเดียว\n\nยังไม่อนุมัติหรือเผยแพร่ ข้อมูลทุกข้ออยู่ใน OWNER_REVIEW_PACKET.json พร้อม values และ locators. ไม่ต้องยืนยันภาษาอังกฤษเดิมซ้ำเพียงเพราะทำ audit นี้\n\n| รายการ | หมวด | รุ่น | ปัญหาที่ขวาง publish |\n|---|---|---:|---|\n'
for item in items:text+='| '+item['record_id']+' | '+item['kind']+' | '+str(item['revision'])+' | '+('; '.join(item['publication_errors']) or 'ไม่มี technical blocker; ยังต้อง factual approval')+' |\n'
with (B/'OWNER_REVIEW_PACKET.md').open('x',encoding='utf-8') as f:f.write(text)
print('Read-only owner review packet:',len(items),'draft records;',sum(bool(i['publication_errors']) for i in items),'with technical publication blockers')
