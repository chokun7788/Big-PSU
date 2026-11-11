"""Fixed focused matrix; source-only serial requests, no hidden retry or grade edits."""
import hashlib,json,os,time,sys
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.migrated_view import MigratedView
cases=[]
def case(id,q,locale='th',contains=(),equal=None,no_hits=False):cases.append(dict(id=id,question=q,locale=locale,contains=list(contains),equal_to=equal,no_hits=no_hits))
case('price_clean','PC นักศึกษา PSU ราคาเท่าไหร่',contains=['0 บาท'])
case('price_missing_character','PC นักศึกษา PSU ราคเท่าไหร่',contains=['0 บาท'])
case('cockpit_total','บุคคลทั่วไป เล่น Cockpit 2 ชั่วโมง เสียกี่บาท',contains=['400 บาท'])
case('compound_booking_typo','บุคคลทั่วไป เล่น Cockpit 2 ชั่วโมง เสียกี่บาท แล้วจองยังงไ',contains=['400 บาท','สลิป'])
case('catalog_clean','มีเกมอะไรบ้าง',contains=['Nintendo Switch'])
case('keyboard_neighbour','มีเกสอะไรบ้าง',equal='catalog_clean')
case('character_missing','มีเกอะไรบ้าง',equal='catalog_clean')
case('character_repeated','มีเกมมอะไรบ้าง',equal='catalog_clean')
case('character_transposed','มีกเมอะไรบ้าง',equal='catalog_clean')
case('token_repeated','มีเกมเกมอะไรบ้าง',equal='catalog_clean')
case('compound_semicolon','มีเกมอะไรบ้าง; PC นักศึกษา PSU ราคาเท่าไหร่ แล้วจองยังไง',contains=['0 บาท','สลิป','TEKKEN 8'])
case('compound_reordered','PC นักศึกษา PSU ราคาเท่าไหร่; จองยังไง แล้วมีเกมอะไรบ้าง',contains=['0 บาท','สลิป','TEKKEN 8'])
case('compound_mixed','มีเกมอะไรบ้าง and also PC นักศึกษา PSU ราคาเท่าไหร่ แล้วจองยังไง',contains=['0 บาท','สลิป','TEKKEN 8'])
case('compound_unspaced','มีเกมอะไรบ้างแล้วจองยังไง',contains=['Nintendo Switch','สลิป'])
case('same_price_repeated','PC นักศึกษา PSU ราคาเท่าไหร่; PC นักศึกษา PSU ราคาเท่าไหร่',contains=['0 บาท'])
case('same_booking_repeated','จองยังไง; จองยังไง',contains=['สลิป'])
case('unknown_entity_sibling','PC นักศึกษา PSU ราคาเท่าไหร่; Andaman Hotel อยู่ที่ไหน',contains=['0 บาท'])
case('unknown_fact_sibling','PC นักศึกษา PSU ราคาเท่าไหร่; กาแล็กซี่นี้มีชื่ออะไร',contains=['0 บาท'])
case('missing_content_word','มีอะไรบ้าง',contains=['หมายถึงเกม'],no_hits=True)
case('negative_typo','ไม่มีเกสอะไรบ้าง',contains=['ยืนยันความหมาย'],no_hits=True)
case('negative_catalog','ไม่มีเกมอะไรบ้าง',contains=['ยังยืนยันรายชื่อเกมที่ไม่มี'],no_hits=True)
case('duplicate_duration','PSU Student เล่น VR 1 ชั่วโมง 1 ชั่วโมง เสียกี่บาท',contains=['ระยะเวลา'],no_hits=True)
case('unknown_edition','TEKKEN 9 ปุ่มอะไร',no_hits=True)
case('device_location_typo','Driving Force Shifter อยู่ซนไหน',contains=['Cockpit'])
case('english_clean','Are drinks allowed','en',contains=['designated'])
case('english_typo','Are drins allowwd','en',equal='english_clean')
case('sessions_source','จองได้สูงสุดกี่รอบ',contains=['6'])
stage=sys.argv[1] if len(sys.argv)>1 else 'after'
manifest_path=R/'ROBUSTNESS_MATRIX_MANIFEST.json'
encoded=json.dumps(cases,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
digest=hashlib.sha256(encoded).hexdigest()
if manifest_path.exists():assert json.loads(manifest_path.read_text(encoding='utf8'))['sha256']==digest,'manifest changed'
else:manifest_path.write_text(json.dumps({'sha256':digest,'cases':cases,'requests':len(cases),'worker_count':1,'scope':'focused known and new variants; not unseen or broad eval; predeclared bounded expectations'},ensure_ascii=False,indent=2),encoding='utf8')
view=MigratedView(R/'system/data/knowledge/verified_sources.sqlite');snap=view.snapshot()
class Pinned:
 path=view.path
 def snapshot(self):return snap
 def still_current(self,s):return True
 def connect(self,**kwargs):return view.connect(**kwargs)
reader=CommonAnswerer(Pinned());out=R/('robustness_'+stage+'_'+str(time.time_ns()));out.mkdir();rows=[];answers={};started=time.perf_counter()
for c in cases:
 before=time.perf_counter();error=None
 try:
  with patch('urllib.request.urlopen',side_effect=AssertionError('No model/HTTP permitted')),patch.dict(os.environ,{'PSU_ANALYSIS_BUDGET_SEC':'0'}):r=reader.answer(c['question'],locale=c['locale'],at='2026-11-11T22:50:00+07:00',planner=None)
  checks={'required_fragments':all(s.casefold() in r.answer.casefold() for s in c['contains']),'source_absent_when_required':not c['no_hits'] or not r.hits,'equivalence_to_clean':c['equal_to'] is None or r.answer==answers[c['equal_to']]}
  if c['id'] in {'unknown_entity_sibling','unknown_fact_sibling'}:checks['not_reported_complete']=(r.decision_artifact or {}).get('response_type')!='answer'
  if c['id']=='unknown_entity_sibling':checks['no_borrowed_center_address']=not any(h.get('record_id')=='center_psu_phuket' and h.get('field') in {'address','floor','building','map_url'} for h in r.hits)
  row={'id':c['id'],'question':c['question'],'checks':checks,'passed':all(checks.values()),'answer':r.answer,'hits':r.hits,'artifact':r.decision_artifact};answers[c['id']]=r.answer
 except Exception as exc:row={'id':c['id'],'question':c['question'],'passed':False,'error_type':type(exc).__name__,'error':str(exc)}
 row['wall_seconds']=time.perf_counter()-before;rows.append(row)
 (out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
 print(json.dumps({'case':c['id'],'passed':row['passed'],'seconds':round(row['wall_seconds'],3)},ensure_ascii=False),flush=True)
report={'requests':len(rows),'passed':sum(x['passed'] for x in rows),'failed_ids':[x['id'] for x in rows if not x['passed']],'all_passed':all(x['passed'] for x in rows),'manifest_sha256':digest,'elapsed_seconds':time.perf_counter()-started,'model_calls':0,'http_requests':0,'scope':'focused serial source-only output/source-scope expectations; not semantic accuracy or full regression score'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
