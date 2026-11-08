"""Independent source-oracle workloads, shared by all three strategies per domain.

Source-derived templated development questions, not a human-adjudicated holdout.
No import of flow_engine and no strategy output is used to create expected claims.
"""
import collections,hashlib,json,random
from pathlib import Path
R=Path(__file__).resolve().parent;data=json.loads((R/'COMMON_READ_MODEL.json').read_text('utf8'));allfacts=data['facts'];jobs=[]
rng=random.Random('r113-fixed-before-results-20261021')
th=['ขอทราบ{label}ของ “{subject}”','ช่วยบอก{label}เกี่ยวกับ “{subject}” หน่อย','สำหรับ “{subject}” อยากทราบ{label}','“{subject}” มีข้อมูล{label}ว่าอย่างไร','รบกวนตอบเฉพาะ{label}ของ “{subject}”','สอบถาม{label}สำหรับ “{subject}”','อยากดู{label}ที่ยืนยันได้ของ “{subject}”','ขอรายละเอียด{label}ของ “{subject}” ได้ไหม','ช่วยเช็ก{label}ของ “{subject}” ให้ที','เกี่ยวกับ “{subject}” ขอข้อมูล{label}แบบสั้น ๆ','ขอถามหน่อยว่า{label}ของ “{subject}” เป็นอย่างไร','โปรดแจ้ง{label}ที่มีในข้อมูลของ “{subject}”']
en=['What is the {label} for "{subject}"?','Please tell me the {label} of "{subject}".','For "{subject}", explain its {label}.','Could you check the {label} for "{subject}"?','I need the {label} of "{subject}" only.','Show the source-backed {label} for "{subject}".','About "{subject}": what is its {label}?','Please give the {label} of "{subject}" briefly.','Help me find the {label} for "{subject}".','Which {label} is recorded for "{subject}"?','Tell me about "{subject}" and its {label}.','I would like to know the {label} for "{subject}".']
for i in range(1,15):
 cat=f'C{i:02}';facts=[x for x in allfacts if x['category']==cat];rng.shuffle(facts);seen=set()
 def expected_for(f,lang):
  # An equal subject/label can legitimately refer to multiple source clauses.
  return [x for x in facts if x['subject'][lang]==f['subject'][lang] and x['label'][lang]==f['label'][lang]]
 for n in range(100):
  lang='th' if n<50 or n>=80 else 'en' if n<70 else 'th';locale='auto' if 70<=n<80 else lang
  missing=n>=80;compound=60<=n<80
  f=facts[n%len(facts)];template=(en if lang=='en' else th)[(n//max(1,len(facts))+n)%12]
  q=template.format(label=f['label'][lang],subject=f['subject'][lang]);expected=expected_for(f,lang)
  if compound:
   other=next((x for x in facts if x['subject'][lang]==f['subject'][lang] and x['label'][lang]!=f['label'][lang]),facts[(n+3)%len(facts)])
   q+='; '+('also tell me the {label} of "{subject}"' if lang=='en' else 'และขอ{label}ของ “{subject}” ด้วย').format(label=other['label'][lang],subject=other['subject'][lang]);expected+=expected_for(other,lang)
  if cat=='C06' and f['facet']=='amount' and not compound and not missing:
   sessions=1+n%3;q+=f' รวม {sessions} รอบ' if lang=='th' else f' for {sessions} sessions'
  else:sessions=1
  if missing:
   gap=['รหัสผ่านส่วนตัว','รหัสลับ','เลขเครื่องที่ไม่ได้บันทึก','อีเมลส่วนตัว'][n%4]
   q=f'ขอ{gap}ของ “{f["subject"][lang]}”'+[' หน่อย',' ได้ไหม',' โดยตรง',' ที่ยืนยันได้',' แบบสั้น ๆ'][n%5];expected=[]
  attempts=0
  while q in seen:
   q=('ขอสอบถามเพิ่มเติม: ' if lang=='th' else 'Please help me with this: ')+q;attempts+=1
   assert attempts<5
  seen.add(q)
  expected=list({x['id']:x for x in expected}.values())
  exp=[]
  for x in expected:
   numeric=x.get('numeric')
   if cat=='C06' and x['facet']=='amount' and not compound and not missing and numeric is not None:numeric*=sessions
   exp.append({'fact_id':x['id'],'record_id':x['record_id'],'facet':x['facet'],'value':x['value'][lang],'numeric':numeric,'evidence_refs':x['evidence_refs']})
  status='missing_source' if not expected else 'unavailable' if all(x.get('provider_state') in {'unavailable','stale'} for x in expected) else 'answer'
  jobs.append({'id':f'{cat}-Q{n+1:03}','category':cat,'question':q,'locale':locale,'reference_time':'2026-10-21T12:00:00+07:00','expected':{'claims':exp,'status':status,'sessions':sessions},'stratum':'missing_source' if missing else 'multi_need' if compound else 'single_need','fixture':cat in {'C12','C14'},'oracle_basis':'source field/condition identity and value; generated independently from strategy outputs','question_origin':'source-derived templated development workload; not retained human customer questions or independent holdout'})
assert len(jobs)==1400 and len({j['id'] for j in jobs})==1400
assert all(sum(j['category']==f'C{i:02}' for j in jobs)==100 for i in range(1,15))
path=R/'QUESTIONS_1400.jsonl'
if path.exists():raise SystemExit('Question set already frozen')
path.write_text('\n'.join(json.dumps(j,ensure_ascii=False) for j in jobs)+'\n','utf8')
manifest={'questions':1400,'per_category':100,'per_flow':100,'executions':4200,'per_category_strata':{'single_need':60,'multi_need':20,'missing_source':20},'locales_per_category':{'th':70,'en':20,'auto':10},'question_set_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'read_model_sha256':hashlib.sha256((R/'COMMON_READ_MODEL.json').read_bytes()).hexdigest(),'fixture_categories':['C12','C14'],'limits':['Templated source-derived development questions, not an independent semantic holdout.','Domain adapters are explicitly selected; global 14-way routing is not measured.','C12 uses controlled provider snapshots; C14 uses isolated synthetic news.','Controls and rules with missing English translations retain source text; language availability is reported separately.']}
(R/'WORKLOAD_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),'utf8');print(json.dumps(manifest,ensure_ascii=False))
