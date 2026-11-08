"""Isolated owner API save/edit/withdraw observed through the actual chat API."""
import json,pathlib,sys,time,urllib.request,uuid
R=pathlib.Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
from app.knowledge.common.registry import template
out=R/('http_lifecycle_'+str(time.time_ns()));out.mkdir()
session=json.loads((R/'system/data/knowledge/owner-session.json').read_text('utf8'))
assert pathlib.Path(session['db']).resolve()==(R/'system/data/knowledge/common.sqlite').resolve()
token=session['url'].split('#token=',1)[1];rows=[]
def post(port,path,data,owner=False):
 headers={'Content-Type':'application/json'}
 if owner:headers['Authorization']='Bearer '+token
 req=urllib.request.Request(f'http://127.0.0.1:{port}'+path,data=json.dumps(data,ensure_ascii=False).encode(),headers=headers,method='POST')
 with urllib.request.urlopen(req,timeout=195) as response:return json.load(response)
def chat(question):
 result=post(8125,'/api/chat',{'question':question,'locale':'en','client_session_id':'hybrid-smoke-'+uuid.uuid4().hex,'client_turn_id':uuid.uuid4().hex,'debug':True,'recent_history':[]})
 rows.append({'question':question,'response':result});return result
rid='hybrid_trial_http_device_'+uuid.uuid4().hex[:8]
r=template('equipment_model');r['record_id']=rid;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
for k,v in {'name':{'th':'Hybrid Smoke Device','en':'Hybrid Smoke Device'},'device_type':'console'}.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
checks={};saved=None
try:
 saved=post(8126,'/api/save',{'attest':True,'record':r,'expected_version':0,'change_note':'isolated synthetic HTTP smoke; not business source'},True)['record']
 first=chat('What device type is Hybrid Smoke Device?');checks['add_visible_through_chat']='console' in first.get('answer','').lower()
 saved['fields']['device_type']['value']='pc'
 saved=post(8126,'/api/save',{'attest':True,'record':saved,'expected_version':saved['revision'],'change_note':'isolated synthetic type change'},True)['record']
 second=chat('What device type is Hybrid Smoke Device?');checks['edit_visible_no_stale_value']='pc' in second.get('answer','').lower() and 'console' not in second.get('answer','').lower()
finally:
 if saved:post(8126,'/api/withdraw',{'id':rid},True)
third=chat('What device type is Hybrid Smoke Device?');checks['withdrawn_value_not_delivered']='console' not in third.get('answer','').lower() and not any(x in third.get('answer','').lower() for x in ['**ชนิดอุปกรณ์**: pc','**device type**: pc'])
with urllib.request.urlopen('http://127.0.0.1:8125/health',timeout=5) as response:health=json.load(response)
checks['correct_build']=health['common_loaded_build']['build_id']=='common-r135-hybrid48-trial'
checks['correct_runtime']=health['runtime']['version']=='R135-Hybrid48'
checks['automatic_logs_exist']=bool(list((R/'runtime/logs').glob('*.jsonl'))) or (R/'runtime/logs/transcripts.sqlite').exists()
report={'all_passed':all(checks.values()),'checks':checks,'fixture_record_id':rid,'scope':'actual local owner/chat HTTP; synthetic isolated data, not production authority or general semantic acceptance'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
