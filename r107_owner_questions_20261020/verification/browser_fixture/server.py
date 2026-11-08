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
def save(s,event):
 s['revision']+=1;s['updated_at']=now();s['production_applied']=False
 with EVENTS.open('a',encoding='utf8') as f:f.write(json.dumps({'at':now(),'revision':s['revision'],**event},ensure_ascii=False)+'\n')
 tmp=D/'answers.tmp';tmp.write_text(json.dumps(s,ensure_ascii=False,indent=2),'utf8');os.replace(tmp,STATE)
class H(BaseHTTPRequestHandler):
 def log_message(self,fmt,*args):print(now(),fmt%args,flush=True)
 def send(self,code,data,ctype='application/json; charset=utf-8'):
  raw=data if isinstance(data,bytes) else json.dumps(data,ensure_ascii=False).encode('utf8')
  self.send_response(code);self.send_header('Content-Type',ctype);self.send_header('Content-Length',str(len(raw)));self.send_header('Cache-Control','no-store');self.send_header('X-Content-Type-Options','nosniff');self.end_headers();self.wfile.write(raw)
 def do_GET(self):
  path=urlsplit(self.path).path
  if path=='/api/state':
   with LOCK:self.send(200,{'questions':DATA,'answers':read(),'token':TOKEN,'question_set_sha256':HASH})
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
    if path=='/api/answer':
     id=body.get('id');answer=body.get('answer')
     if id not in IDS or not isinstance(answer,dict):raise ValueError('รหัสคำถามไม่ถูกต้อง')
     allowed={'unanswered','answered','unknown','no_policy','not_applicable','deferred'}
     if answer.get('status') not in allowed:raise ValueError('สถานะคำตอบไม่ถูกต้อง')
     clean={k:str(answer.get(k,''))[:30000] for k in ['text','source','effective_from','effective_until','note']};clean['status']=answer['status'];clean['updated_at']=now()
     if clean['status']=='answered' and not clean['text'].strip():raise ValueError('กรุณาใส่คำตอบก่อนเลือก “ให้คำตอบแล้ว”')
     for k in ['effective_from','effective_until']:
      if clean[k] and not re.fullmatch(r'\d{4}-\d{2}-\d{2}',clean[k]):raise ValueError('วันที่ต้องเป็น YYYY-MM-DD')
     s['answers'][id]=clean;save(s,{'action':'answer','question_id':id,'value':clean});self.send(200,{'saved':True,'updated_at':s['updated_at'],'revision':s['revision']});return
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
      if not isinstance(v,dict) or v.get('status') not in {'unanswered','answered','unknown','no_policy','not_applicable','deferred'}:raise ValueError('ข้อมูลคำตอบไม่ถูกต้อง')
      if v.get('status')=='answered' and not str(v.get('text','')).strip():raise ValueError('พบสถานะตอบแล้วที่ไม่มีคำตอบ')
     if STATE.exists():(D/('before_import_'+uuid.uuid4().hex+'.json')).write_bytes(STATE.read_bytes())
     for k,v in proposed.items():
      clean={f:str(v.get(f,''))[:30000] for f in ['text','source','effective_from','effective_until','note']};clean.update(status=v['status'],updated_at=now());s['answers'][k]=clean
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
