"""Reuse an actual server-written clarification, then supply its missing role."""
import json,re,time,urllib.request,uuid
from pathlib import Path
R=Path(__file__).resolve().parent;URL='http://127.0.0.1:8144/'
prior=max(R.glob('audience_http_*/DETAILS.json'),key=lambda p:p.stat().st_mtime)
initial=json.loads(prior.read_text(encoding='utf8'))[0]['response'];assert initial.get('ok') and initial.get('session_id')
out=R/('audience_followup_http_'+str(time.time_ns()));out.mkdir();rows=[];checks={}
for n,session in enumerate([initial['session_id'],'audience-independent-'+uuid.uuid4().hex]):
 body={'question':'นักศึกษาต่างมหาลัย','locale':'th','client_session_id':session,'client_turn_id':uuid.uuid4().hex,'recent_history':[],'debug':False}
 req=urllib.request.Request(URL+'api/chat',data=json.dumps(body,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'},method='POST')
 with urllib.request.urlopen(req,timeout=45) as response:result=json.load(response)
 rows.append({'question':body['question'],'response':result,'uses_prior_server_session':n==0});answer=result.get('answer','')
 checks[f'ok_{n}']=result.get('ok') is True
 if n==0:
  checks['role_reply_resumes_service']='Nintendo Switch' in answer
  checks['role_reply_uses_foreign_rate']='50 บาท' in answer and not re.search(r'(?<!\d)0\s*บาท',answer)
 else:checks['separate_session_not_borrowing_rate']=not re.search(r'(?<!\d)\d+\s*บาท',answer)
 (out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
report={'all_passed':all(checks.values()),'checks':checks,'requests':len(rows),'initial_clarification_reused_from':str(prior.relative_to(R)),'scope':'actual server-session follow-up and separate-session control; no client-provided trusted history or facts'}
(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
