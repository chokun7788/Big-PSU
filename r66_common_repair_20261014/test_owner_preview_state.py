"""Actual owner preview HTTP, readonly isolated candidate view, no approvals."""
import sys,json,unittest,threading,urllib.request
from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
from test_r66_reader import a,B
from harness import configure
from app.knowledge.common.owner_server import make_handler
enabled=len(sys.argv)>1 and sys.argv[1]=='1';configure('common',enabled)
class OwnerPreview(unittest.TestCase):
 def run_turns(self,lang):
  server=ThreadingHTTPServer(('127.0.0.1',0),BaseHTTPRequestHandler);port=server.server_address[1];server.RequestHandlerClass=make_handler(a.store,'r66-fixture-token','fixture',port);thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start();history=[]
  turns=['บุคคลทั่วไปเล่น PC 2 ชั่วโมงกี่บาท','ถ้าเป็นศิษย์เก่าล่ะ','แล้ว 1 ชั่วโมงล่ะ'] if lang=='th' else ['PC for 2 hours, general adult price?','What about alumni?','And for 1 hour?']
  try:
   for q,amount,minutes in zip(turns,['140.00 THB','50.00 THB','25.00 THB'],[120,120,60]):
    req=urllib.request.Request(f'http://127.0.0.1:{port}/api/preview',data=json.dumps({'question':q,'locale':lang,'history':history,'draft':False},ensure_ascii=False).encode(),headers={'Authorization':'Bearer r66-fixture-token','Content-Type':'application/json'})
    with urllib.request.urlopen(req,timeout=20) as res:body=json.load(res)
    self.assertIn(('รวม ' if lang=='th' else 'total ')+amount,body['answer']);self.assertEqual(body['common_read_state']['constraints'],{'duration_minutes':minutes});self.assertEqual(body['trace']['query_plan']['unresolved_clauses'],[])
    history.extend([{'role':'user','content':q},{'role':'assistant','content':body['answer'],'common_read_state':body['common_read_state']}])
  finally:server.shutdown();server.server_close();thread.join(3)
 def test_thai_preview_uses_the_server_typed_state(self):self.run_turns('th')
 def test_english_preview_uses_the_server_typed_state(self):self.run_turns('en')
if __name__=='__main__':
 r=unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(OwnerPreview));p=B/('OWNER_PREVIEW_STATE_'+str(len(list(B.glob('OWNER_PREVIEW_STATE_*.json')))+1)+'.json');p.write_text(json.dumps({'tests_run':r.testsRun,'llm_enabled':enabled,'actual_http':True,'candidate_evaluation_view_only':True,'failures':[{'test':str(t),'stack':s} for t,s in r.failures],'errors':[{'test':str(t),'stack':s} for t,s in r.errors]},ensure_ascii=False,indent=2),encoding='utf-8');raise SystemExit(0 if r.wasSuccessful() else 1)
