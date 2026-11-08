"""Small isolated persistence/HTTP checks; no chatbot tests or production writes."""
import base64,hashlib,importlib.util,json,tempfile,threading,urllib.request,urllib.error
from pathlib import Path
R=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('form_server',R/'server.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
checks=[]
with tempfile.TemporaryDirectory(prefix='psu-owner-form-') as temp:
 m.D=Path(temp);m.A=m.D/'attachments';m.A.mkdir();m.STATE=m.D/'answers.json';m.EVENTS=m.D/'events.jsonl'
 server=m.ThreadingHTTPServer(('127.0.0.1',0),m.H);thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start();url='http://127.0.0.1:'+str(server.server_port)
 def req(path,obj=None,token=True):
  headers={'Content-Type':'application/json'}
  if token:headers['X-Questionnaire-Token']=m.TOKEN
  r=urllib.request.Request(url+path,data=json.dumps(obj).encode() if obj is not None else None,headers=headers)
  try:
   with urllib.request.urlopen(r) as response:return response.status,response.read()
  except urllib.error.HTTPError as e:return e.code,e.read()
 def check(name,ok):
  checks.append({'check':name,'passed':bool(ok)});assert ok,name
 code,body=req('/api/state');state=json.loads(body);check('302 unique questions load',code==200 and len(state['questions']['questions'])==302)
 id=m.DATA['questions'][0]['id'];sample={'status':'answered','text':'ตัวอย่างตรวจการบันทึกเท่านั้น','source':'QA fixture','effective_from':'','effective_until':'','note':''}
 check('missing token rejected',req('/api/answer',{'id':id,'answer':sample},False)[0]==403)
 check('answer saved',req('/api/answer',{'id':id,'answer':sample})[0]==200)
 saved=json.loads(req('/api/state')[1])['answers'];check('answer survives reload and disk read',saved['answers'][id]['text']==sample['text'] and m.read()['answers'][id]['status']=='answered')
 check('empty answered rejected',req('/api/answer',{'id':id,'answer':{**sample,'text':''}})[0]==400)
 check('unknown status separate',req('/api/answer',{'id':id,'answer':{**sample,'status':'unknown','text':''}})[0]==200 and m.read()['answers'][id]['status']=='unknown')
 check('partial answer retained with explicit remaining question',req('/api/answer',{'id':id,'answer':{**sample,'status':'partial','remaining_question':'ยังขาดเงื่อนไขใด'}})[0]==200 and m.read()['answers'][id]['remaining_question']=='ยังขาดเงื่อนไขใด')
 id2=m.DATA['questions'][1]['id'];code,body=req('/api/prefill',{'batch_id':'qa_sample','answers':{id:{**sample,'status':'answered'},id2:{**sample,'status':'partial','remaining_question':'ส่วนที่เหลือ'}}});prefill=json.loads(body)
 check('prefill never overwrites existing human answer',code==200 and id in prefill['skipped'] and m.read()['answers'][id]['status']=='partial')
 check('prefill inserts only matching blank question',id2 in prefill['inserted'] and m.read()['answers'][id2]['status']=='partial')
 check('partial prefill without remaining rejected',req('/api/prefill',{'batch_id':'qa_bad','answers':{id2:{**sample,'status':'partial'}}})[0]==400)
 check('wrong question set import rejected',req('/api/import',{'responses':{'schema_version':'psu-owner-responses-1','question_set_sha256':'wrong','answers':{}}})[0]==400)
 state=m.read();check('valid import backed up',req('/api/import',{'responses':state})[0]==200 and bool(list(m.D.glob('before_import_*.json'))))
 code,body=req('/api/attachment',{'question_id':id,'name':'proof.txt','data':base64.b64encode(b'QA evidence').decode()});info=json.loads(body);check('attachment persisted and downloadable',code==200 and req('/attachment/'+info['id'])[1]==b'QA evidence')
 check('unsafe extension rejected',req('/api/attachment',{'question_id':id,'name':'run.exe','data':'YQ=='})[0]==400)
 check('no arbitrary static file',req('/server.py')[0]==404 and req('/../questions.json')[0]==404)
 check('new answer events kept',len(m.EVENTS.read_text('utf8').splitlines())>=4)
 server.shutdown();server.server_close()
db=R.parent/'r106_complete_flow_20261020/system/data/knowledge/common.sqlite';check('source DB unchanged',hashlib.sha256(db.read_bytes()).hexdigest()==m.DATA['source_database_sha256'])
out={'scope':'isolated questionnaire HTTP/storage checks, no LLM or chatbot rerun','checks':checks,'passed':sum(x['passed'] for x in checks),'total':len(checks)};(R/'VERIFICATION.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8');print(json.dumps(out,ensure_ascii=False))
