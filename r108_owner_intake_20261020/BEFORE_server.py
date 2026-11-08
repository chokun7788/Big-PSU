"""Loopback-only questionnaire. Responses never write into chatbot knowledge."""
import base64,hashlib,json,mimetypes,os,re,threading,uuid
from datetime import datetime
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit
R=Path(__file__).resolve().parent;D=R/'responses';D.mkdir(exist_ok=True);A=D/'attachments';A.mkdir(exist_ok=True)
DATA=json.loads((R/'questions.json').read_text('utf8'));IDS={q['id'] for q in DATA['questions']};LOCK=threading.RLock()
TOKEN=uuid.uuid4().hex;HASH=hashlib.sha256((R/'questions.json').read_bytes()).hexdigest()
STATE=D/'answers.json';EVENTS=D/'events.jsonl';MAX=30*1024*1024
def now():return datetime.now().astimezone().isoformat()
def read():
 if STATE.exists():return json.loads(STATE.read_text('utf8'))
 return {'schema_version':'psu-owner-responses-1','question_set_sha256':HASH,'revision':0,'respondent':{},'answers':{},'attachments':{},'updated_at':None,'production_applied':False}
def catalog():
 data=json.loads(json.dumps(DATA,ensure_ascii=False));patch=R/'QUESTION_UPDATES.json'
 if patch.exists():
  updates=json.loads(patch.read_text('utf8'))
  for q in data['questions']:
   if q['id'] in updates.get('questions',{}):q.update(updates['questions'][q['id']])
  if 'known_answers' in updates:data['known_answers']=updates['known_answers']
  data['owner_update']=updates.get('owner_update')
 return data
def save(s,event):
 s['revision']+=1;s['updated_at']=now();s['production_applied']=False
 with EVENTS.open('a',encoding='utf8') as f:f.write(json.dumps({'at':now(),'revision':s['revision'],**event},ensure_ascii=False)+'\n')
 tmp=D/'answers.tmp';tmp.write_text(json.dumps(s,ensure_ascii=False,indent=2),'utf8');os.replace(tmp,STATE)
def simple_state():
 path=D/'simple_answers.json'
 return json.loads(path.read_text('utf8')) if path.exists() else {'schema_version':'psu-simple-owner-responses-1','answers':{},'updated_at':None}
def simple_save(s,event):
 s['updated_at']=now();tmp=D/'simple_answers.tmp';tmp.write_text(json.dumps(s,ensure_ascii=False,indent=2),'utf8');os.replace(tmp,D/'simple_answers.json')
 with (D/'simple_events.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps({'at':now(),**event},ensure_ascii=False)+'\n')
def simple_questions():return json.loads((R/'simple_questions.json').read_text('utf8'))
class H(BaseHTTPRequestHandler):
 def log_message(self,fmt,*args):print(now(),fmt%args,flush=True)
 def send(self,code,data,ctype='application/json; charset=utf-8'):
  raw=data if isinstance(data,bytes) else json.dumps(data,ensure_ascii=False).encode('utf8')
  self.send_response(code);self.send_header('Content-Type',ctype);self.send_header('Content-Length',str(len(raw)));self.send_header('Cache-Control','no-store');self.send_header('X-Content-Type-Options','nosniff');self.end_headers();self.wfile.write(raw)
 def do_GET(self):
  path=urlsplit(self.path).path
  if path=='/api/simple-state':
   with LOCK:self.send(200,{'questions':simple_questions(),'responses':simple_state(),'token':TOKEN,'question_set_sha256':hashlib.sha256((R/'simple_questions.json').read_bytes()).hexdigest()})
   return
  if path=='/api/state':
   with LOCK:self.send(200,{'questions':catalog(),'answers':read(),'token':TOKEN,'question_set_sha256':HASH})
   return
  if path=='/api/health':self.send(200,{'app':'psu-owner-questions-r107','question_count':len(IDS)});return
  static={'/':'index.html','/index.html':'index.html','/app.js':'app.js','/style.css':'style.css'}
  if path in static:
   p=R/static[path];self.send(200,p.read_bytes(),(mimetypes.guess_type(p.name)[0] or 'text/plain')+'; charset=utf-8');return
  if path.startswith('/attachment/'):
   id=path.rsplit('/',1)[-1]
   with LOCK:info=read()['attachments'].get(id)
   if not info:self.send(404,{'error':'ไม่พบไฟล์'});return
   p=A/info['stored_name']
   if not p.is_file():self.send(404,{'error':'ไม่พบไฟล์บนเครื่อง'});return
   raw=p.read_bytes();self.send_response(200);self.send_header('Content-Type','application/octet-stream');self.send_header('Content-Disposition','attachment; filename="'+id+Path(info['name']).suffix+'"');self.send_header('Content-Length',str(len(raw)));self.send_header('X-Content-Type-Options','nosniff');self.end_headers();self.wfile.write(raw);return
  self.send(404,{'error':'ไม่พบหน้านี้'})
 def do_POST(self):
  if self.headers.get('X-Questionnaire-Token')!=TOKEN:self.send(403,{'error':'กรุณาโหลดหน้าเว็บใหม่ก่อนบันทึก'});return
  origin=self.headers.get('Origin')
  if origin and origin!='http://'+self.headers.get('Host',''):self.send(403,{'error':'ไม่อนุญาตต้นทางนี้'});return
  try:
   length=int(self.headers.get('Content-Length','0'))
   if length<1 or length>MAX:raise ValueError('ข้อมูลใหญ่เกินกำหนด')
   body=json.loads(self.rfile.read(length));path=urlsplit(self.path).path
   with LOCK:
    s=read()
    if path in {'/api/simple-draft','/api/simple-submit'}:
     catalog=simple_questions();prompts={q['id']:q for q in catalog['questions']};ss=simple_state()
     if path=='/api/simple-draft':
      id=body.get('id');text=body.get('text')
      if id not in prompts or not isinstance(text,str) or len(text)>30000:raise ValueError('คำตอบไม่ถูกต้องหรือยาวเกินกำหนด')
      prior=ss['answers'].get(id,{});submitted=prior.get('submitted_at') if text==prior.get('text') else None
      ss['answers'][id]={'text':text,'updated_at':now(),'submitted_at':submitted};simple_save(ss,{'action':'draft','question_id':id,'text':text});self.send(200,{'saved':True,'updated_at':ss['updated_at']});return
     incoming=body.get('answers')
     if not isinstance(incoming,dict) or not incoming:raise ValueError('กรอกอย่างน้อยหนึ่งข้อก่อนส่ง')
     if any(id not in prompts or not isinstance(text,str) or not text.strip() or len(text)>30000 for id,text in incoming.items()):raise ValueError('พบคำตอบว่างหรือรหัสคำถามไม่ถูกต้อง')
     submitted_at=now();entries=[]
     for id,text in incoming.items():
      ss['answers'][id]={'text':text,'updated_at':submitted_at,'submitted_at':submitted_at}
      entries.append({**prompts[id],'answer':text})
     bundle={'schema_version':'psu-simple-owner-submission-1','submitted_at':submitted_at,'production_applied':False,'answers':entries}
     folder=D/'submissions';folder.mkdir(exist_ok=True);filename='PSU-owner-answers-'+datetime.now().strftime('%Y%m%d-%H%M%S')+'-'+uuid.uuid4().hex[:6]+'.json';(folder/filename).write_text(json.dumps(bundle,ensure_ascii=False,indent=2),'utf8')
     simple_save(ss,{'action':'submit','filename':filename,'answers':entries});self.send(200,{'saved':True,'count':len(entries),'filename':filename,'submission':bundle});return
    if path=='/api/answer':
     id=body.get('id');answer=body.get('answer')
     if id not in IDS or not isinstance(answer,dict):raise ValueError('รหัสคำถามไม่ถูกต้อง')
     allowed={'unanswered','partial','answered','unknown','no_policy','not_applicable','deferred'}
     if answer.get('status') not in allowed:raise ValueError('สถานะคำตอบไม่ถูกต้อง')
     clean={k:str(answer.get(k,''))[:30000] for k in ['text','source','effective_from','effective_until','note','remaining_question']};clean['status']=answer['status'];clean['updated_at']=now()
     for k in ['source_batch_id','source_items']:
      if k in s['answers'].get(id,{}):clean[k]=s['answers'][id][k]
     if clean['status']=='answered' and not clean['text'].strip():raise ValueError('กรุณาใส่คำตอบก่อนเลือก “ให้คำตอบแล้ว”')
     for k in ['effective_from','effective_until']:
      if clean[k] and not re.fullmatch(r'\d{4}-\d{2}-\d{2}',clean[k]):raise ValueError('วันที่ต้องเป็น YYYY-MM-DD')
     s['answers'][id]=clean;save(s,{'action':'answer','question_id':id,'value':clean});self.send(200,{'saved':True,'updated_at':s['updated_at'],'revision':s['revision']});return
    if path=='/api/prefill':
     batch=body.get('batch_id');proposed=body.get('answers')
     if not isinstance(batch,str) or not re.fullmatch(r'[a-zA-Z0-9_-]{1,100}',batch) or not isinstance(proposed,dict) or any(k not in IDS for k in proposed):raise ValueError('ชุดคำตอบไม่ถูกต้อง')
     for id,v in proposed.items():
      if not isinstance(v,dict) or v.get('status') not in {'unanswered','partial','answered'} or not isinstance(v.get('text'),str):raise ValueError('ข้อมูลเติมคำตอบไม่ถูกต้อง')
      if v['status'] in {'partial','answered'} and not v['text'].strip():raise ValueError('คำตอบต้องมีข้อความ')
      if v['status']=='partial' and not v.get('remaining_question'):raise ValueError('ตอบบางส่วนต้องระบุส่วนที่เหลือ')
     existing=s['answers'];inserted=[];skipped=[]
     if STATE.exists():(D/('before_prefill_'+uuid.uuid4().hex+'.json')).write_bytes(STATE.read_bytes())
     for id,v in proposed.items():
      prior=existing.get(id,{})
      if prior and (prior.get('text','').strip() or prior.get('note','').strip() or prior.get('status','unanswered')!='unanswered'):
       skipped.append(id);continue
      clean={k:str(v.get(k,''))[:30000] for k in ['text','source','effective_from','effective_until','note','remaining_question']};clean.update(status=v['status'],updated_at=now(),source_batch_id=batch,source_items=v.get('source_items',[]));existing[id]=clean;inserted.append(id)
     save(s,{'action':'owner_chat_prefill','batch_id':batch,'answers':{k:existing[k] for k in inserted},'skipped':skipped});self.send(200,{'saved':True,'inserted':inserted,'skipped':skipped,'revision':s['revision']});return
    if path=='/api/respondent':
     s['respondent']={k:str(body.get(k,''))[:500] for k in ['name','role']};save(s,{'action':'respondent','value':s['respondent']});self.send(200,{'saved':True});return
    if path=='/api/attachment':
     id=body.get('question_id');filename=body.get('name','')
     if id not in IDS or not isinstance(filename,str):raise ValueError('คำถามหรือชื่อไฟล์ไม่ถูกต้อง')
     filename=Path(filename.replace('\\','/')).name[:200];raw=base64.b64decode(body.get('data',''),validate=True)
     if len(raw)>20*1024*1024:raise ValueError('แนบได้ไม่เกิน 20 MB ต่อไฟล์')
     ext=Path(filename).suffix.lower()
     if ext not in {'.pdf','.png','.jpg','.jpeg','.webp','.txt','.md','.json','.csv','.xlsx','.docx'}:raise ValueError('ชนิดไฟล์ไม่รองรับ ใช้ PDF รูปภาพ เอกสาร หรือ Excel')
     aid=uuid.uuid4().hex;stored=aid+ext;(A/stored).write_bytes(raw)
     info={'id':aid,'question_id':id,'name':filename,'stored_name':stored,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'uploaded_at':now()};s['attachments'][aid]=info;save(s,{'action':'attachment','value':info});self.send(200,info);return
    if path=='/api/import':
     obj=body.get('responses')
     if not isinstance(obj,dict) or obj.get('schema_version')!='psu-owner-responses-1' or obj.get('question_set_sha256')!=HASH:raise ValueError('ไฟล์คำตอบไม่ตรงกับแบบฟอร์มชุดนี้')
     proposed=obj.get('answers')
     if not isinstance(proposed,dict) or any(k not in IDS for k in proposed):raise ValueError('พบรหัสคำถามที่ไม่อยู่ในชุดนี้')
     for k,v in proposed.items():
      if not isinstance(v,dict) or v.get('status') not in {'unanswered','partial','answered','unknown','no_policy','not_applicable','deferred'}:raise ValueError('ข้อมูลคำตอบไม่ถูกต้อง')
      if v.get('status')=='answered' and not str(v.get('text','')).strip():raise ValueError('พบสถานะตอบแล้วที่ไม่มีคำตอบ')
     if STATE.exists():(D/('before_import_'+uuid.uuid4().hex+'.json')).write_bytes(STATE.read_bytes())
     for k,v in proposed.items():
      clean={f:str(v.get(f,''))[:30000] for f in ['text','source','effective_from','effective_until','note','remaining_question']};clean.update(status=v['status'],updated_at=now());clean.update({k:v[k] for k in ['source_batch_id','source_items'] if k in v});s['answers'][k]=clean
     save(s,{'action':'import','answers':proposed});self.send(200,{'saved':True,'count':len(proposed),'note':'นำเข้าเฉพาะข้อความคำตอบ ไฟล์แนบยังใช้ไฟล์ที่มีในเครื่องนี้'});return
    self.send(404,{'error':'ไม่พบคำสั่ง'})
  except (ValueError,TypeError,KeyError,json.JSONDecodeError) as e:self.send(400,{'error':str(e)})
  except Exception as e:
   print(type(e).__name__,str(e),flush=True);self.send(500,{'error':'บันทึกไม่สำเร็จ กรุณาเก็บข้อความไว้แล้วลองใหม่'})
def main():
 for port in range(8120,8140):
  try:server=ThreadingHTTPServer(('127.0.0.1',port),H);break
  except OSError:continue
 else:raise RuntimeError('ไม่มีพอร์ตว่างระหว่าง 8120–8139')
 url=f'http://127.0.0.1:{port}/';(R/'session.json').write_text(json.dumps({'pid':os.getpid(),'url':url,'started_at':now()},ensure_ascii=False,indent=2),'utf8');print('Local: '+url,flush=True);server.serve_forever()
if __name__=='__main__':main()
