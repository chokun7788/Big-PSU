"""Read-only inventory of fields and evidence paths, not an owner approval."""
import json,collections,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent;d=json.loads((R/'SOURCE_REFERENCE.json').read_text('utf8'))
records=d['records'];facts=d['facts'];kinds=collections.Counter(r['kind'] for r in records.values())
states=collections.Counter();unknown=collections.Counter()
for r in records.values():
 for k,f in r.get('fields',{}).items():
  states[f.get('status','missing')]+=1
  if f.get('status')!='known':unknown[(r['kind'],k,f.get('status','missing'))]+=1
offered={f['record_id'] for f in facts if f['category']=='C04' and f['facet']=='studio_services'}
zoned={f['record_id'] for f in facts if f['category']=='C04' and f['facet']=='zone'}
gaps=[]
for rid in sorted(offered-zoned):
 f=next(f for f in facts if f['record_id']==rid and f['facet']=='studio_services')
 gaps.append({'record_id':rid,'title':f['subject'],'confirmed_services':f['value'],'evidence_refs':f['evidence_refs'],'reason':'no_evidenced_game_offer_service_resource_zone_path'})
persons=[r for r in records.values() if r['kind']=='person']
public=collections.Counter(r['fields'].get('public_scope',{}).get('status','missing') for r in persons)
rates=collections.Counter(r['fields'].get('calculation_rule',{}).get('status','missing') for r in records.values() if r['kind']=='rate')
services=[{'record_id':rid,'name':r['fields'].get('name',{}).get('value'),'resource_ids_state':r['fields'].get('resource_ids',{}).get('status','missing')} for rid,r in records.items() if r['kind']=='service' and r['fields'].get('resource_ids',{}).get('status')!='known']
out={'snapshot_records':len(records),'snapshot_facts_before_R118_projection':len(facts),'by_kind':dict(kinds),'field_states':dict(states),
 'person_public_scope_states':dict(public),'rate_calculation_rule_states':dict(rates),'offered_games':len(offered),'games_with_zone_paths':len(zoned),
 'offered_games_without_zone_paths':gaps,'services_without_confirmed_resource_ids':services,
 'unknown_or_non_known_fields':[{'kind':k,'field':f,'state':s,'count':n} for (k,f,s),n in unknown.most_common()]}
(R/'SOURCE_GAPS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
doc=['# R118 — ข้อมูลที่ยังจำกัดคำตอบ','','ตรวจ snapshot เดียวกับ R117 revision04 โดยไม่แก้ source หรือ approvals การนับช่อง not_applicable/unknown/conflicted ไม่ใช่การนับคำตอบผิดหรือจำนวนคำถามที่ตอบไม่ได้','',
 f'- Records {len(records)}; projected facts ก่อนเพิ่ม metadata R118 {len(facts)}',
 f'- Person public_scope states: {dict(public)}',f'- Rate calculation_rule states: {dict(rates)}',
 f'- เกมที่มีบริการยืนยัน {len(offered)}; มีเส้นทางยืนยันถึงโซน {len(zoned)}; ขาดเส้นทาง {len(gaps)}','',
 '## เกมที่ยืนยันบริการได้แต่ยังเชื่อมไปถึงโซนไม่ได้','','| เกม | บริการที่มีหลักฐาน |','|---|---|']
for g in gaps:doc.append(f"| {g['title']['en']} | {g['confirmed_services']['en']} |")
doc+=['','## ความหมายต่อการแก้ Flow','','1. ห้ามเอาชื่อ platform ที่ตรงกับชื่อโซนมาแทน relation ที่ขาด ควรเติม service.resource_ids และ resource.zone_id พร้อมหลักฐานถ้ามีข้อมูลต้นฉบับยืนยันจริง',
 '2. public_scope ต้องมาจากสถานะเจ้าของข้อมูลที่ถูกต้อง ตัวอ่าน inverse ช่วยหาเจอ แต่ไม่ใช่ใบอนุญาตเผยแพร่',
 '3. สูตรคำนวณต้องตรงหน่วย/ช่วงเวลา/กลุ่ม การมีราคา 60 นาทีไม่รับรองว่าจะคิด 30 นาทีหรือหลายชั่วโมงแบบ linear เสมอ',
 '4. calendar open_periods ที่ขัดแย้งไม่ใช่ bookable_periods ไม่มีรายการจองไม่เท่ากับศูนย์ปิด',
 '5. ชื่อฉบับเกมและฉบับการแข่งขันต้องยืนยัน ID ให้ตรง ห้ามเลือกอีก edition เพราะมีข้อมูลมากกว่า',
 '6. กรณี keyword/clause fail ให้ดู source และคำตอบรายข้อก่อนนับเป็น content failure',
 '', 'รายการทุกช่องและ source evidence ดู SOURCE_GAPS.json โดย source ที่ใช้เป็น draft snapshot ไม่ใช่สถานะเผยแพร่ production']
(R/'02_SOURCE_GAPS_TH.md').write_text('\n'.join(doc),'utf8')
print(json.dumps({k:v for k,v in out.items() if k not in {'unknown_or_non_known_fields','offered_games_without_zone_paths','services_without_confirmed_resource_ids'}},ensure_ascii=False))
