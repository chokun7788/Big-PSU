"""Three sequential HTTP delivery checks against the separate citation preview."""
import json
import time
import urllib.request
import uuid
from pathlib import Path

P=Path(__file__).resolve().parent
URL='http://127.0.0.1:8139/'
health=json.load(urllib.request.urlopen(URL+'health',timeout=5))
assert health['runtime']['version']=='R135-Bounded-citations'
out=P/('citation_http_'+str(time.time_ns()));out.mkdir()
results=[];checks={}
for locale,q in [('th','ยกเลิกการจองต้องทำล่วงหน้ากี่ชั่วโมง'),('en','Can I smoke inside the studio?'),('th','นักศึกษา PSU เล่น PC ราคาเท่าไหร่')]:
 body={'question':q,'locale':locale,'client_session_id':'citation-'+uuid.uuid4().hex,'client_turn_id':uuid.uuid4().hex,'recent_history':[],'debug':False}
 req=urllib.request.Request(URL+'api/chat',data=json.dumps(body,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'},method='POST')
 with urllib.request.urlopen(req,timeout=45) as response: result=json.load(response)
 results.append({'question':q,'response':result})
 (out/'DETAILS.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
 i=str(len(results));checks['http_ok_'+i]=result.get('ok') is True
 sources=result.get('sources',[])
 if len(results)<3:
  checks['verified_link_'+i]=bool(sources) and all(s.get('url')=='https://esports.computing.psu.ac.th/' for s in sources)
  checks['citation_marker_'+i]='[S' in result.get('answer','')
 else:
  checks['student_zero_retained']='0 บาท' in result.get('answer','')
  checks['no_price_image_citation']=not sources and '[S' not in result.get('answer','')
report={'all_passed':all(checks.values()),'checks':checks,'runtime':health['runtime']['version'],
 'scope':'3 sequential HTTP requests, no full evaluation rerun; HTTP success alone is not correctness or authority; model admission not independently proved'}
(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'output':str(out),**report},ensure_ascii=False));assert report['all_passed']
