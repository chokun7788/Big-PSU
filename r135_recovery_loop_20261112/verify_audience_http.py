"""Seven serial natural chat controls, including requested prices and ambiguity."""
import json,re,time,urllib.request,uuid
from pathlib import Path
R=Path(__file__).resolve().parent;URL='http://127.0.0.1:8144/'
h=json.load(urllib.request.urlopen(URL+'health',timeout=5));assert h['runtime']['version']=='R135-Recovery-loop02'
cases=[('นักศึกษาต่งามหาลัย เล่น Nintendo Switch 30 นาที เสียกี่บาท','th','ask'),('student plays Nintendo Switch for 30 minutes how much','en','ask'),('นักศึกษา PSU เล่น Nintendo Switch 30 นาที เสียกี่บาท','th','psu'),('นักศึกษาต่างมหาลัย เล่น Nintendo Switch 30 นาที เสียกี่บาท','th','foreign'),('Nintendo Switch ราคาแต่ละกลุ่มเท่าไหร่','th','all'),('นักศึกษาต่งามหาลัย เล่น Nintendo Switch 30 นาที เสียกี่บาท แล้วจองยังไง','th','compound'),('ไม่ใช่นักศึกษา PSU เล่น Nintendo Switch 30 นาที เสียกี่บาท','th','ask')]
out=R/('audience_http_'+str(time.time_ns()));out.mkdir();checks={};rows=[]
for n,(q,locale,kind) in enumerate(cases):
 body={'question':q,'locale':locale,'client_session_id':'audience-'+uuid.uuid4().hex,'client_turn_id':uuid.uuid4().hex,'recent_history':[],'debug':False}
 req=urllib.request.Request(URL+'api/chat',data=json.dumps(body,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'},method='POST');started=time.perf_counter()
 with urllib.request.urlopen(req,timeout=45) as response:result=json.load(response)
 answer=result.get('answer','');rows.append({'question':q,'response':result,'seconds':time.perf_counter()-started})
 checks[f'http_ok_{n}']=result.get('ok') is True
 if kind in {'ask','compound'}:
  checks[f'asks_group_{n}']='ยืนยันกลุ่มผู้ใช้' in answer or 'confirm your user group' in answer
  checks[f'no_unselected_price_{n}']=not re.search(r'(?<!\d)\d+\s*(?:บาท|THB)',answer,re.I)
 if kind=='psu':checks['normal_psu_zero']=bool(re.search(r'(?<!\d)0\s*บาท',answer))
 if kind=='foreign':checks['normal_foreign_fifty']='50 บาท' in answer and not re.search(r'(?<!\d)0\s*บาท',answer)
 if kind=='all':checks['requested_all_groups_retained']=all(s in answer for s in ['PSU Student and Staff','PSU Alumni and General Student','General Adult'])
 if kind=='compound':checks['booking_sibling_survives']='สลิป' in answer and 'partial' in result.get('mode','')
 (out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
report={'all_passed':all(checks.values()),'requests':len(rows),'checks':checks,'scope':'serial natural candidate HTTP; role ambiguity/positives, not full semantic or backend model acceptance'}
(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
