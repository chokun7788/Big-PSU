"""Sequential chat HTTP checks after wiring recovery into both common readers."""
import json,time,urllib.request,uuid
from pathlib import Path
P=Path(__file__).resolve().parent;URL='http://127.0.0.1:8143/'
health=json.load(urllib.request.urlopen(URL+'health',timeout=5));assert health['runtime']['version']=='R135-Shared-contract-round02'
out=P/('typo_http_'+str(time.time_ns()));out.mkdir();checks={};rows=[]
def ask(q,locale='th'):
 body={'question':q,'locale':locale,'client_session_id':'typo-'+uuid.uuid4().hex,'client_turn_id':uuid.uuid4().hex,'recent_history':[],'debug':False}
 request=urllib.request.Request(URL+'api/chat',data=json.dumps(body,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'},method='POST')
 with urllib.request.urlopen(request,timeout=45) as r:a=json.load(r)
 rows.append({'question':q,'response':a});checks['http_'+str(len(rows))]=a.get('ok') is True
 (out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8');return a
base=ask('มีเกมอะไรบ้าง');checks['catalog_positive']='Nintendo Switch' in base.get('answer','') and len(base.get('answer',''))>100
for q in ['มีเกสอะไรบ้าง','มีเกอะไรบ้าง','มีเกมมอะไรบ้าง']:
 a=ask(q);checks['same_delivery_'+q]=a.get('answer')==base.get('answer')
a=ask('มีอะไรบ้าง');checks['missing_whole_word_asks']='หมายถึงเกม' in a.get('answer','') and not a.get('sources')
a=ask('PC นักศึกษา PSU ราคเท่าไหร่');checks['price_zero_retained']='0 บาท' in a.get('answer','')
a=ask('บุคคลทั่วไป เล่น Cockpit 2 ชั่วโมง เสียกี่บาท แล้วจองยังงไ');checks['existing_compound_not_broken']='400 บาท' in a.get('answer','') and 'สลิป' in a.get('answer','')
en=ask('Are drinks allowed','en');typo=ask('Are drins allowwd','en');checks['english_positive_and_equivalent']='designated' in en.get('answer','').lower() and typo.get('answer')==en.get('answer')
a=ask('ไม่มีเกสอะไรบ้าง');checks['negative_typo_asks_confirmation']='ยืนยันความหมาย' in a.get('answer','') and not a.get('sources')
a=ask('ไม่มีเกมอะไรบ้าง');checks['negative_catalog_not_offered_list']='ยังยืนยันรายชื่อเกมที่ไม่มี' in a.get('answer','') and not a.get('sources')
report={'all_passed':all(checks.values()),'checks':checks,'requests':len(rows),'scope':'11 sequential HTTP controls, not a full evaluation or general typo accuracy estimate'}
(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report},ensure_ascii=False));assert report['all_passed']
